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
