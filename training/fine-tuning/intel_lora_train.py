"""LoRA fine-tuning entrypoint with optional Intel PyTorch optimizations.

The script is intentionally import-light: heavyweight training dependencies are
loaded only when `run_training` executes so configuration tests can run quickly.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class IpexResolution:
    available: bool
    module: Any | None = None
    reason: str = ""


@dataclass(frozen=True)
class TrainingConfig:
    model_id: str = "LiquidAI/lfm2.5-1.2b-instruct"
    dataset_id: str | None = None
    dataset_split: str = "train"
    max_length: int = 1024
    output_dir: Path = Path("training/fine-tuning/lfm2.5-1.2b-intel-lora")
    max_steps: int = 5
    learning_rate: float = 2e-4
    per_device_train_batch_size: int = 1
    gradient_accumulation_steps: int = 4
    lora_r: int = 16
    lora_alpha: int = 32
    lora_dropout: float = 0.05
    target_modules: tuple[str, ...] = ("q_proj", "k_proj", "v_proj", "o_proj")
    dtype: str = "bf16"
    use_ipex: bool = True
    require_ipex: bool = False


@dataclass(frozen=True)
class PreflightResult:
    metadata_dir: Path
    repo_id: str
    tokenizer_loaded: bool
    config_loaded: bool
    tokenized_keys: tuple[str, ...]
    token_source: str | None = None


def resolve_ipex(use_ipex: bool, require_ipex: bool) -> IpexResolution:
    if not use_ipex:
        return IpexResolution(available=False, reason="IPEX disabled by configuration")

    try:
        import intel_extension_for_pytorch as ipex  # type: ignore
    except ModuleNotFoundError as exc:
        reason = f"intel_extension_for_pytorch is unavailable: {exc}"
        if require_ipex:
            raise RuntimeError(reason) from exc
        return IpexResolution(available=False, reason=reason)

    return IpexResolution(available=True, module=ipex, reason="IPEX available")


def resolve_hf_token(explicit_token: str | None = None) -> tuple[str | None, str | None]:
    if explicit_token:
        return explicit_token, "explicit"

    for env_name in ("HF_TOKEN", "HUGGINGFACE_HUB_TOKEN", "HF_HUB_TOKEN"):
        token = os.environ.get(env_name)
        if token:
            return token, env_name

    return None, None


def torch_dtype(dtype: str):
    import torch

    if dtype == "bf16":
        return torch.bfloat16
    if dtype == "fp32":
        return torch.float32
    raise ValueError(f"Unsupported dtype: {dtype}")


def optimize_model_with_ipex(model, ipex_resolution: IpexResolution, dtype: str):
    if not ipex_resolution.available:
        return model

    return ipex_resolution.module.optimize(model, dtype=torch_dtype(dtype))


def format_training_text(example: dict[str, Any]) -> str:
    text = str(example.get("text") or "").strip()
    if text:
        return text

    instruction = str(example.get("instruction") or "").strip()
    input_text = str(example.get("input") or "").strip()
    output = str(example.get("output") or "").strip()

    sections = []
    if instruction:
        sections.append(f"### Instruction:\n{instruction}")
    if input_text:
        sections.append(f"### Input:\n{input_text}")
    if output:
        sections.append(f"### Response:\n{output}")

    return "\n\n".join(sections)


def tokenize_training_example(example: dict[str, Any], tokenizer, max_length: int) -> dict[str, Any]:
    tokenized = tokenizer(
        format_training_text(example),
        truncation=True,
        max_length=max_length,
    )
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized


def load_streaming_dataset(dataset_id: str, split: str):
    from datasets import load_dataset

    return load_dataset(dataset_id, split=split, streaming=True)


def load_model_metadata(metadata_dir: Path, local_files_only: bool = True):
    from transformers import AutoConfig, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(metadata_dir, local_files_only=local_files_only)
    config = AutoConfig.from_pretrained(metadata_dir, local_files_only=local_files_only)
    return tokenizer, config


def preflight_model_metadata(
    metadata_dir: Path,
    repo_id: str,
    token: str | None = None,
) -> PreflightResult:
    resolved_token, token_source = resolve_hf_token(token)
    tokenizer, config = load_model_metadata(metadata_dir, local_files_only=True)
    tokenized = tokenize_training_example(
        {
            "instruction": "Summarize the metadata readiness for this model.",
            "input": f"repo_id={repo_id}",
            "output": "Metadata files are present and can be loaded locally.",
        },
        tokenizer,
        max_length=64,
    )
    return PreflightResult(
        metadata_dir=metadata_dir,
        repo_id=repo_id,
        tokenizer_loaded=tokenizer is not None,
        config_loaded=config is not None,
        tokenized_keys=tuple(sorted(tokenized.keys())),
        token_source=token_source if resolved_token else None,
    )


def run_training(config: TrainingConfig) -> None:
    if config.dataset_id is None:
        raise ValueError("--dataset-id is required for training")

    import torch
    from peft import LoraConfig, get_peft_model
    from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

    ipex_resolution = resolve_ipex(config.use_ipex, config.require_ipex)
    dtype = torch_dtype(config.dtype)

    tokenizer = AutoTokenizer.from_pretrained(config.model_id)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(config.model_id, torch_dtype=dtype)
    model = optimize_model_with_ipex(model, ipex_resolution, config.dtype)

    lora_config = LoraConfig(
        r=config.lora_r,
        lora_alpha=config.lora_alpha,
        lora_dropout=config.lora_dropout,
        target_modules=list(config.target_modules),
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)

    dataset = load_streaming_dataset(config.dataset_id, config.dataset_split)
    tokenized_dataset = dataset.map(
        lambda example: tokenize_training_example(example, tokenizer, config.max_length)
    )

    args = TrainingArguments(
        output_dir=str(config.output_dir),
        max_steps=config.max_steps,
        learning_rate=config.learning_rate,
        per_device_train_batch_size=config.per_device_train_batch_size,
        gradient_accumulation_steps=config.gradient_accumulation_steps,
        bf16=config.dtype == "bf16",
        fp16=False,
        logging_steps=1,
        save_steps=max(1, config.max_steps),
        report_to=[],
    )

    trainer = Trainer(model=model, args=args, train_dataset=tokenized_dataset)
    trainer.train()
    model.save_pretrained(config.output_dir)
    tokenizer.save_pretrained(config.output_dir)


def parse_args() -> tuple[TrainingConfig, Path, bool]:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument(
        "--metadata-dir",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-instruct-meta"),
    )
    parser.add_argument("--model-id", default=TrainingConfig.model_id)
    parser.add_argument("--dataset-id")
    parser.add_argument("--dataset-split", default=TrainingConfig.dataset_split)
    parser.add_argument("--max-length", type=int, default=TrainingConfig.max_length)
    parser.add_argument("--output-dir", type=Path, default=TrainingConfig.output_dir)
    parser.add_argument("--max-steps", type=int, default=TrainingConfig.max_steps)
    parser.add_argument("--learning-rate", type=float, default=TrainingConfig.learning_rate)
    parser.add_argument("--batch-size", type=int, default=TrainingConfig.per_device_train_batch_size)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=TrainingConfig.gradient_accumulation_steps)
    parser.add_argument("--dtype", choices=("bf16", "fp32"), default=TrainingConfig.dtype)
    parser.add_argument("--disable-ipex", action="store_true")
    parser.add_argument("--require-ipex", action="store_true")
    args = parser.parse_args()

    config = TrainingConfig(
        model_id=args.model_id,
        dataset_id=args.dataset_id,
        dataset_split=args.dataset_split,
        max_length=args.max_length,
        output_dir=args.output_dir,
        max_steps=args.max_steps,
        learning_rate=args.learning_rate,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        dtype=args.dtype,
        use_ipex=not args.disable_ipex,
        require_ipex=args.require_ipex,
    )
    return config, args.metadata_dir, args.preflight_only


if __name__ == "__main__":
    config, metadata_dir, preflight_only = parse_args()
    if preflight_only or config.dataset_id is None:
        preflight = preflight_model_metadata(
            metadata_dir=metadata_dir,
            repo_id=config.model_id,
        )
        print(
            json.dumps(
                {
                    "metadata_dir": str(preflight.metadata_dir),
                    "repo_id": preflight.repo_id,
                    "tokenizer_loaded": preflight.tokenizer_loaded,
                    "config_loaded": preflight.config_loaded,
                    "tokenized_keys": list(preflight.tokenized_keys),
                    "token_source": preflight.token_source,
                },
                indent=2,
            )
        )
    else:
        run_training(config)
