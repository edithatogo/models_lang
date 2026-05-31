import importlib.util
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "mem0" / "lfm2_colbert_finetune.py"


def load_module():
    spec = importlib.util.spec_from_file_location("lfm2_colbert_finetune", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_default_colbert_finetune_config_targets_lfm2_colbert():
    module = load_module()
    config = module.ColbertFineTuneConfig()

    assert config.model_id == "LiquidAI/LFM2-ColBERT-350M"
    assert config.output_dir.as_posix() == "training/fine-tuning/lfm2-colbert-350m-mem0"
    assert config.temperature == 0.02
    assert config.bf16 is True


def test_normalize_triplet_example_trims_required_fields():
    module = load_module()

    normalized = module.normalize_triplet_example(
        {"query": " q ", "positive": " p ", "negative": " n ", "ignored": "x"}
    )

    assert normalized == {"query": "q", "positive": "p", "negative": "n"}


def test_validate_triplet_example_rejects_missing_required_fields():
    module = load_module()

    try:
        module.validate_triplet_example({"query": "q", "positive": "p"})
    except ValueError as exc:
        assert "negative" in str(exc)
    else:
        raise AssertionError("Expected missing negative field to raise")
