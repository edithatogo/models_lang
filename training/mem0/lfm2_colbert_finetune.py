"""Fine-tune LFM2-ColBERT-350M for mem0 retrieval.

The training path follows PyLate's contrastive ColBERT workflow: a triplet
dataset with `query`, `positive`, and `negative` columns is used to optimize
MaxSim late-interaction retrieval.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_MODEL_ID = "LiquidAI/LFM2-ColBERT-350M"
DEFAULT_OUTPUT_DIR = Path("training/fine-tuning/lfm2-colbert-350m-mem0")
REQUIRED_TRIPLET_FIELDS = ("query", "positive", "negative")


@dataclass(frozen=True)
class ColbertFineTuneConfig:
    model_id: str = DEFAULT_MODEL_ID
    dataset_id: str | None = None
    dataset_name: str | None = None
    dataset_split: str = "train"
    output_dir: Path = DEFAULT_OUTPUT_DIR
    batch_size: int = 8
    eval_ratio: float = 0.01
    max_steps: int = 100
    num_train_epochs: float = 1.0
    learning_rate: float = 3e-6
    temperature: float = 0.02
    fp16: bool = False
    bf16: bool = True
    torch_compile: bool = False


def validate_triplet_example(example: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_TRIPLET_FIELDS if not str(example.get(field) or "").strip()]
    if missing:
        raise ValueError(f"Triplet example is missing required fields: {', '.join(missing)}")


def normalize_triplet_example(example: dict[str, Any]) -> dict[str, str]:
    validate_triplet_example(example)
    return {field: str(example[field]).strip() for field in REQUIRED_TRIPLET_FIELDS}


def run_training(config: ColbertFineTuneConfig) -> None:
    if not config.dataset_id:
        raise ValueError("--dataset-id is required for ColBERT fine-tuning")

    import torch
    from datasets import load_dataset
    from sentence_transformers import SentenceTransformerTrainer, SentenceTransformerTrainingArguments

    from pylate import evaluation, losses, models, utils

    model = models.ColBERT(model_name_or_path=config.model_id)
    if config.torch_compile:
        model = torch.compile(model)

    if config.dataset_name:
        dataset = load_dataset(config.dataset_id, config.dataset_name, split=config.dataset_split)
    else:
        dataset = load_dataset(config.dataset_id, split=config.dataset_split)

    first = normalize_triplet_example(dataset[0])
    del first

    splits = dataset.train_test_split(test_size=config.eval_ratio)
    train_dataset = splits["train"]
    eval_dataset = splits["test"]

    train_loss = losses.Contrastive(model=model, temperature=config.temperature)
    evaluator = evaluation.ColBERTTripletEvaluator(
        anchors=eval_dataset["query"],
        positives=eval_dataset["positive"],
        negatives=eval_dataset["negative"],
    )
    args = SentenceTransformerTrainingArguments(
        output_dir=str(config.output_dir),
        max_steps=config.max_steps,
        num_train_epochs=config.num_train_epochs,
        per_device_train_batch_size=config.batch_size,
        per_device_eval_batch_size=config.batch_size,
        learning_rate=config.learning_rate,
        fp16=config.fp16,
        bf16=config.bf16,
        report_to=[],
        run_name=config.output_dir.name,
    )
    trainer = SentenceTransformerTrainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        loss=train_loss,
        evaluator=evaluator,
        data_collator=utils.ColBERTCollator(tokenize_fn=model.tokenize),
    )
    trainer.train()
    model.save_pretrained(str(config.output_dir))


def parse_args() -> ColbertFineTuneConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-id", default=DEFAULT_MODEL_ID)
    parser.add_argument("--dataset-id")
    parser.add_argument("--dataset-name")
    parser.add_argument("--dataset-split", default="train")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--eval-ratio", type=float, default=0.01)
    parser.add_argument("--max-steps", type=int, default=100)
    parser.add_argument("--num-train-epochs", type=float, default=1.0)
    parser.add_argument("--learning-rate", type=float, default=3e-6)
    parser.add_argument("--temperature", type=float, default=0.02)
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--no-bf16", action="store_true")
    parser.add_argument("--torch-compile", action="store_true")
    args = parser.parse_args()
    return ColbertFineTuneConfig(
        model_id=args.model_id,
        dataset_id=args.dataset_id,
        dataset_name=args.dataset_name,
        dataset_split=args.dataset_split,
        output_dir=args.output_dir,
        batch_size=args.batch_size,
        eval_ratio=args.eval_ratio,
        max_steps=args.max_steps,
        num_train_epochs=args.num_train_epochs,
        learning_rate=args.learning_rate,
        temperature=args.temperature,
        fp16=args.fp16,
        bf16=not args.no_bf16,
        torch_compile=args.torch_compile,
    )


def main() -> None:
    run_training(parse_args())


if __name__ == "__main__":
    main()
