import importlib.util
import os
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "fine-tuning" / "download_lfm_base_metadata.py"


def load_module():
    spec = importlib.util.spec_from_file_location("download_lfm_base_metadata", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_resolve_hf_token_prefers_explicit_token():
    module = load_module()
    token, source = module.resolve_hf_token("explicit-token")

    assert token == "explicit-token"
    assert source == "explicit"


def test_resolve_hf_token_prefers_standard_env_vars(monkeypatch):
    module = load_module()
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.delenv("HUGGINGFACE_HUB_TOKEN", raising=False)
    monkeypatch.delenv("HF_HUB_TOKEN", raising=False)
    monkeypatch.setenv("HUGGINGFACE_HUB_TOKEN", "env-token")

    token, source = module.resolve_hf_token()

    assert token == "env-token"
    assert source == "HUGGINGFACE_HUB_TOKEN"


def test_default_files_cover_expected_metadata():
    module = load_module()

    assert module.DEFAULT_FILES == (
        "config.json",
        "generation_config.json",
        "special_tokens_map.json",
        "tokenizer_config.json",
        "tokenizer.json",
    )


def test_preflight_model_metadata_uses_loaded_metadata_and_token_resolution(monkeypatch):
    module = load_module()
    train_module_path = Path(__file__).resolve().parents[1] / "fine-tuning" / "intel_lora_train.py"
    train_spec = importlib.util.spec_from_file_location("intel_lora_train", train_module_path)
    train_module = importlib.util.module_from_spec(train_spec)
    sys.modules[train_spec.name] = train_module
    train_spec.loader.exec_module(train_module)
    observed = {}

    class FakeTokenizer:
        pass

    class FakeConfig:
        pass

    def fake_load_model_metadata(metadata_dir, local_files_only=True):
        observed["metadata_dir"] = metadata_dir
        observed["local_files_only"] = local_files_only
        return FakeTokenizer(), FakeConfig()

    def fake_tokenize_training_example(example, tokenizer, max_length):
        observed["example"] = example
        observed["tokenizer"] = tokenizer
        observed["max_length"] = max_length
        return {"input_ids": [1], "attention_mask": [1], "labels": [1], "extra": [0]}

    monkeypatch.setenv("HF_TOKEN", "env-token")
    monkeypatch.setattr(train_module, "load_model_metadata", fake_load_model_metadata)
    monkeypatch.setattr(train_module, "tokenize_training_example", fake_tokenize_training_example)

    result = train_module.preflight_model_metadata(
        metadata_dir=Path("C:/tmp/lfm2.5-1.2b-instruct-meta-script"),
        repo_id="LiquidAI/lfm2.5-1.2b-instruct",
    )

    assert observed["metadata_dir"] == Path("C:/tmp/lfm2.5-1.2b-instruct-meta-script")
    assert observed["local_files_only"] is True
    assert observed["tokenizer"].__class__.__name__ == "FakeTokenizer"
    assert observed["max_length"] == 64
    assert "repo_id=LiquidAI/lfm2.5-1.2b-instruct" in observed["example"]["input"]
    assert result.tokenizer_loaded is True
    assert result.config_loaded is True
    assert result.token_source == "HF_TOKEN"
