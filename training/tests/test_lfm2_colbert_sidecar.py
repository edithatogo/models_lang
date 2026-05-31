import importlib.util
import sys
from pathlib import Path

from fastapi.testclient import TestClient


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "mem0" / "lfm2_colbert_sidecar.py"


def load_module():
    sys.path.insert(0, str(SCRIPT_PATH.parent))
    spec = importlib.util.spec_from_file_location("lfm2_colbert_sidecar", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class FakeAdapter:
    def __init__(self, module):
        self.config = module.SidecarConfig(port=8766)
        self.records = {}

    def upsert(self, documents, rebuild=False):
        for document in documents:
            clean = module.validate_document(document)
            self.records[clean.id] = clean
        return len(self.records)

    def search(self, query, k=10, subset=None):
        module.validate_query(query)
        ids = subset or list(self.records)
        results = []
        for document_id in ids[:k]:
            record = self.records[document_id]
            results.append(
                module.SearchResult(
                    id=document_id,
                    score=42.0 - len(results),
                    text=record.text,
                    metadata=record.metadata,
                )
            )
        return results

    def get(self, document_id):
        return self.records.get(document_id)

    def count(self):
        return len(self.records)

    def ready(self):
        return True


module = load_module()


def test_sidecar_app_upserts_and_searches_documents():
    adapter = FakeAdapter(module)
    client = TestClient(module.create_app(adapter))

    response = client.post(
        "/documents/upsert",
        json={
            "documents": [
                {"id": "mem-1", "text": "User prefers local memory", "metadata": {"user_id": "u1"}},
                {"id": "mem-2", "text": "Use ColBERT MaxSim retrieval", "metadata": {"user_id": "u1"}},
            ]
        },
    )
    assert response.status_code == 200
    assert response.json() == {"indexed_count": 2}

    response = client.post("/search", json={"query": "local memory", "k": 1})
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == "mem-1"
    assert response.json()["results"][0]["metadata"] == {"user_id": "u1"}


def test_sidecar_health_and_mem0_config_expose_late_interaction_contract():
    adapter = FakeAdapter(module)
    client = TestClient(module.create_app(adapter))

    health = client.get("/health").json()
    config = client.get("/mem0/config").json()

    assert health["model_id"] == "LiquidAI/LFM2-ColBERT-350M"
    assert health["scoring"] == "maxsim"
    assert health["ready"] is True
    assert config["sidecar"]["embedding_shape"] == "multi_vector_token_embeddings"
    assert "single-vector" in config["mem0_note"]


def test_sidecar_rejects_blank_documents_and_queries():
    assert client_error("/documents/upsert", {"documents": [{"id": "x", "text": "  "}]}) == 400
    assert client_error("/search", {"query": " "}) == 400


def client_error(path, payload):
    adapter = FakeAdapter(module)
    client = TestClient(module.create_app(adapter))
    return client.post(path, json=payload).status_code
