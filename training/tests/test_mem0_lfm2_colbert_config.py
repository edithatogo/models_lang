import importlib.util
import json
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "mem0" / "lfm2_colbert_config.py"


def load_module():
    spec = importlib.util.spec_from_file_location("lfm2_colbert_config", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_mem0_embedding_model_is_lfm2_colbert_late_interaction():
    module = load_module()
    config = module.build_mem0_config()

    embedding_model = config["mem0"]["embedding_model"]

    assert embedding_model["model_id"] == "LiquidAI/LFM2-ColBERT-350M"
    assert embedding_model["scoring"] == "maxsim"
    assert embedding_model["embedding_shape"] == "multi_vector_token_embeddings"
    assert embedding_model["output_dim"] == 128
    assert config["mem0"]["sidecar"]["base_url"] == "http://127.0.0.1:8766"
    assert config["mem0"]["sidecar"]["service_entrypoint"] == "training/mem0/lfm2_colbert_sidecar.py"
    assert config["mem0"]["single_vector_embedding_provider"] is False
    assert config["mem0"]["requires_late_interaction_adapter"] is True


def test_pipeline_keeps_fact_extraction_and_retrieval_finetunes_separate():
    module = load_module()
    config = module.build_mem0_config()

    fact_stage = config["fine_tuning"]["fact_extraction"]
    retrieval_stage = config["fine_tuning"]["retrieval"]

    assert fact_stage["model_id"] == "LiquidAI/lfm2.5-1.2b-instruct"
    assert fact_stage["method"] == "lora"
    assert retrieval_stage["model_id"] == "LiquidAI/LFM2-ColBERT-350M"
    assert retrieval_stage["dataset_schema"] == "query_positive_negative_triplets"
    assert retrieval_stage["trainer_entrypoint"] == "training/mem0/lfm2_colbert_finetune.py"
    assert "start_lfm2_colbert_sidecar" in config["fine_tuning"]["pipeline_order"]
    assert "fine_tune_lfm2_colbert_retriever" in config["fine_tuning"]["pipeline_order"]


def test_write_config_round_trips_and_validates():
    module = load_module()
    output = Path("training/mem0/.tmp_mem0_lfm2_colbert_config.test.json")

    try:
        written = module.write_config(output)
        loaded = json.loads(output.read_text(encoding="utf-8"))

        assert loaded == written
        module.validate_mem0_config(loaded)
    finally:
        output.unlink(missing_ok=True)
