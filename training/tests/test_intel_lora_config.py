import importlib.util
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "fine-tuning" / "intel_lora_train.py"


def load_module():
    spec = importlib.util.spec_from_file_location("intel_lora_train", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_default_config_uses_bf16_and_lora_defaults():
    module = load_module()
    config = module.TrainingConfig()

    assert config.dtype == "bf16"
    assert config.lora_r == 16
    assert config.lora_alpha == 32
    assert config.use_ipex is True
    assert config.require_ipex is False


def test_ipex_resolution_can_fall_back_when_not_required():
    module = load_module()

    result = module.resolve_ipex(use_ipex=True, require_ipex=False)

    assert result.available is False
    assert "intel_extension_for_pytorch" in result.reason


def test_ipex_resolution_raises_when_required():
    module = load_module()

    try:
        module.resolve_ipex(use_ipex=True, require_ipex=True)
    except RuntimeError as exc:
        assert "intel_extension_for_pytorch" in str(exc)
    else:
        raise AssertionError("Expected missing IPEX to raise when require_ipex=True")


def test_format_training_text_prefers_text_field():
    module = load_module()

    text = module.format_training_text(
        {"text": "ready-made sample", "instruction": "ignore", "output": "ignore"}
    )

    assert text == "ready-made sample"


def test_format_training_text_builds_instruction_record():
    module = load_module()

    text = module.format_training_text(
        {
            "instruction": "Summarize",
            "input": "A long note",
            "output": "A short note",
        }
    )

    assert "### Instruction:\nSummarize" in text
    assert "### Input:\nA long note" in text
    assert "### Response:\nA short note" in text


def test_tokenize_training_example_copies_labels():
    module = load_module()

    class Tokenizer:
        def __call__(self, text, truncation, max_length):
            assert text == "sample"
            assert truncation is True
            assert max_length == 8
            return {"input_ids": [1, 2, 3], "attention_mask": [1, 1, 1]}

    tokenized = module.tokenize_training_example({"text": "sample"}, Tokenizer(), max_length=8)

    assert tokenized["input_ids"] == [1, 2, 3]
    assert tokenized["labels"] == [1, 2, 3]
