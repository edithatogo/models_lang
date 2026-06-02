import importlib.util
import json
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "mem0" / "build_mem0_datasets.py"


def load_module():
    spec = importlib.util.spec_from_file_location("build_mem0_datasets", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_render_chat_record_uses_lfm_template_and_strict_json():
    module = load_module()
    record = module.render_chat_record(module.DEFAULT_SCENARIOS[0])

    assert "<|im_start|>system" in record["text"]
    assert "<|im_start|>assistant" in record["text"]
    assert record["extracted_facts"] == ["The user is in the Australia/Sydney timezone."]
    module.validate_fact_record(record)


def test_retrieval_triplets_are_query_positive_negative_records():
    module = load_module()
    triplets = module.render_retrieval_triplets(module.DEFAULT_SCENARIOS)

    assert len(triplets) == len(module.DEFAULT_SCENARIOS) * 2
    assert {"query", "positive", "negative", "positive_id", "negative_id"} <= set(triplets[0])
    for triplet in triplets:
        module.validate_triplet(triplet)


def test_build_datasets_writes_manifest_and_jsonl_files():
    module = load_module()
    output_dir = Path("training/mem0/.tmp_dataset_builder_test")

    try:
        result = module.build_datasets(output_dir)
        manifest = json.loads((output_dir / module.MANIFEST_JSON).read_text(encoding="utf-8"))
        fact_rows = (output_dir / module.FACT_EXTRACTION_JSONL).read_text(encoding="utf-8").splitlines()
        triplet_rows = (output_dir / module.RETRIEVAL_TRIPLETS_JSONL).read_text(encoding="utf-8").splitlines()
        document_rows = (output_dir / module.SIDECAR_DOCUMENTS_JSONL).read_text(encoding="utf-8").splitlines()

        assert result.fact_records == len(module.DEFAULT_SCENARIOS)
        assert result.retrieval_triplets == len(module.DEFAULT_SCENARIOS) * 2
        assert result.sidecar_documents == len(module.DEFAULT_SCENARIOS)
        assert manifest["fact_records"] == result.fact_records
        assert len(fact_rows) == result.fact_records
        assert len(triplet_rows) == result.retrieval_triplets
        assert len(document_rows) == result.sidecar_documents
    finally:
        for path in output_dir.glob("*"):
            path.unlink()
        output_dir.rmdir()
