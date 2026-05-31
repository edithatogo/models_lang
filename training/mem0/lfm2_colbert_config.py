"""mem0 embedding and fine-tuning contract for Liquid LFM models.

LFM2-ColBERT-350M is a late-interaction retriever. It returns token-level
embeddings scored with MaxSim, so mem0 integrations must use a ColBERT adapter
or sidecar instead of a plain single-vector embedding provider.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


COLBERT_MODEL_ID = "LiquidAI/LFM2-ColBERT-350M"
FACT_EXTRACTOR_MODEL_ID = "LiquidAI/lfm2.5-1.2b-instruct"
DEFAULT_CONFIG_PATH = Path("training/mem0/mem0_lfm2_colbert_config.json")
DEFAULT_FACT_ADAPTER_DIR = Path("training/fine-tuning/lfm2.5-1.2b-mem0-lora")
DEFAULT_COLBERT_ADAPTER_DIR = Path("training/fine-tuning/lfm2-colbert-350m-mem0")


@dataclass(frozen=True)
class ColbertRetrievalConfig:
    provider: str = "lfm2-colbert"
    model_id: str = COLBERT_MODEL_ID
    adapter: str = "pylate-colbert"
    index_backend: str = "plaid"
    vector_store_metadata: str = "chroma"
    scoring: str = "maxsim"
    embedding_shape: str = "multi_vector_token_embeddings"
    document_max_tokens: int = 512
    query_max_tokens: int = 32
    output_dim: int = 128


@dataclass(frozen=True)
class FactExtractionFineTuneConfig:
    model_id: str = FACT_EXTRACTOR_MODEL_ID
    method: str = "lora"
    output_dir: str = DEFAULT_FACT_ADAPTER_DIR.as_posix()
    dataset_schema: str = "dialogue_to_strict_json_facts"
    trainer_entrypoint: str = "training/fine-tuning/intel_lora_train.py"
    default_target_modules: tuple[str, ...] = ("q_proj", "k_proj", "v_proj", "o_proj")
    lora_r: int = 16
    lora_alpha: int = 32


@dataclass(frozen=True)
class ColbertFineTuneConfig:
    model_id: str = COLBERT_MODEL_ID
    method: str = "contrastive_late_interaction"
    output_dir: str = DEFAULT_COLBERT_ADAPTER_DIR.as_posix()
    dataset_schema: str = "query_positive_negative_triplets"
    trainer_entrypoint: str = "training/mem0/lfm2_colbert_finetune.py"
    scoring: str = "maxsim"


def build_mem0_config() -> dict[str, Any]:
    fact_extraction = asdict(FactExtractionFineTuneConfig())
    fact_extraction["default_target_modules"] = list(fact_extraction["default_target_modules"])

    return {
        "mem0": {
            "embedding_model": asdict(ColbertRetrievalConfig()),
            "requires_late_interaction_adapter": True,
            "single_vector_embedding_provider": False,
            "notes": [
                "Use LiquidAI/LFM2-ColBERT-350M for retrieval embeddings.",
                "Store mem0 records and metadata in Chroma, but route vector scoring through the ColBERT adapter/index.",
                "Do not collapse token embeddings to a single vector unless a separate recall baseline is being tested.",
            ],
        },
        "fine_tuning": {
            "fact_extraction": fact_extraction,
            "retrieval": asdict(ColbertFineTuneConfig()),
            "pipeline_order": [
                "prepare_dialogue_to_fact_jsonl",
                "fine_tune_fact_extractor_lora",
                "prepare_query_positive_negative_triplets",
                "fine_tune_lfm2_colbert_retriever",
                "build_colbert_plaid_index",
                "verify_mem0_memory_create_and_search",
            ],
        },
    }


def validate_mem0_config(config: dict[str, Any]) -> None:
    embedding_model = config["mem0"]["embedding_model"]
    retrieval_finetune = config["fine_tuning"]["retrieval"]
    fact_finetune = config["fine_tuning"]["fact_extraction"]

    if embedding_model["model_id"] != COLBERT_MODEL_ID:
        raise ValueError(f"mem0 embedding model must be {COLBERT_MODEL_ID}")
    if embedding_model["scoring"] != "maxsim":
        raise ValueError("LFM2-ColBERT must use MaxSim scoring")
    if embedding_model["embedding_shape"] != "multi_vector_token_embeddings":
        raise ValueError("LFM2-ColBERT must be configured as a multi-vector retriever")
    if config["mem0"]["single_vector_embedding_provider"] is not False:
        raise ValueError("LFM2-ColBERT is not a plain single-vector embedding provider")
    if retrieval_finetune["model_id"] != COLBERT_MODEL_ID:
        raise ValueError("retrieval fine-tune stage must target the ColBERT model")
    if fact_finetune["model_id"] != FACT_EXTRACTOR_MODEL_ID:
        raise ValueError("fact extraction fine-tune stage must target the LFM2.5 instruct model")


def write_config(path: Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    config = build_mem0_config()
    validate_mem0_config(config)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    return config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_CONFIG_PATH)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = write_config(args.output)
    print(json.dumps(config, indent=2))


if __name__ == "__main__":
    main()
