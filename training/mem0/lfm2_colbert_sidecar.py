"""HTTP sidecar for mem0 retrieval with LFM2-ColBERT-350M.

The sidecar owns the PyLate ColBERT model and PLAID index. mem0 should keep
memory records and metadata in its normal store, then call this service to
upsert searchable memory text and run MaxSim late-interaction searches.
"""

import argparse
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Protocol

from lfm2_colbert_config import COLBERT_MODEL_ID


DEFAULT_INDEX_FOLDER = Path("training/mem0/lfm2-colbert-index")
DEFAULT_INDEX_NAME = "mem0_memories"
DEFAULT_METADATA_PATH = Path("training/mem0/lfm2-colbert-documents.jsonl")


@dataclass(frozen=True)
class SidecarConfig:
    model_id: str = COLBERT_MODEL_ID
    index_folder: Path = DEFAULT_INDEX_FOLDER
    index_name: str = DEFAULT_INDEX_NAME
    metadata_path: Path = DEFAULT_METADATA_PATH
    batch_size: int = 32
    host: str = "127.0.0.1"
    port: int = 8766
    override_index: bool = False
    lazy_load: bool = True


@dataclass(frozen=True)
class DocumentRecord:
    id: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SearchResult:
    id: str
    score: float
    text: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class ColbertAdapter(Protocol):
    config: SidecarConfig

    def upsert(self, documents: list[DocumentRecord], rebuild: bool = False) -> int:
        ...

    def search(self, query: str, k: int = 10, subset: list[str] | None = None) -> list[SearchResult]:
        ...

    def get(self, document_id: str) -> DocumentRecord | None:
        ...

    def count(self) -> int:
        ...

    def ready(self) -> bool:
        ...


class JsonlDocumentStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._records: dict[str, DocumentRecord] = {}
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            raw = json.loads(line)
            self._records[str(raw["id"])] = DocumentRecord(
                id=str(raw["id"]),
                text=str(raw["text"]),
                metadata=dict(raw.get("metadata") or {}),
            )

    def upsert(self, documents: list[DocumentRecord]) -> None:
        for document in documents:
            self._records[document.id] = document
        self.path.parent.mkdir(parents=True, exist_ok=True)
        lines = [json.dumps(asdict(record), sort_keys=True) for record in self._records.values()]
        self.path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")

    def get(self, document_id: str) -> DocumentRecord | None:
        return self._records.get(document_id)

    def count(self) -> int:
        return len(self._records)


class PylateColbertAdapter:
    def __init__(self, config: SidecarConfig) -> None:
        self.config = config
        self.store = JsonlDocumentStore(config.metadata_path)
        self.model = None
        self.index = None
        self.retriever = None
        if not config.lazy_load:
            self._load_pylate(override=config.override_index)

    def _load_pylate(self, override: bool) -> None:
        if self.ready():
            return
        from pylate import indexes, models, retrieve

        self.model = models.ColBERT(model_name_or_path=self.config.model_id)
        if getattr(self.model.tokenizer, "pad_token", None) is None:
            self.model.tokenizer.pad_token = self.model.tokenizer.eos_token
        self.index = indexes.PLAID(
            index_folder=str(self.config.index_folder),
            index_name=self.config.index_name,
            override=override,
        )
        self.retriever = retrieve.ColBERT(index=self.index)

    def upsert(self, documents: list[DocumentRecord], rebuild: bool = False) -> int:
        clean_documents = [validate_document(document) for document in documents]
        self._load_pylate(override=rebuild or self.config.override_index)
        embeddings = self.model.encode(
            [document.text for document in clean_documents],
            batch_size=self.config.batch_size,
            is_query=False,
            show_progress_bar=False,
        )
        self.index.add_documents(
            documents_ids=[document.id for document in clean_documents],
            documents_embeddings=embeddings,
        )
        self.store.upsert(clean_documents)
        return self.store.count()

    def search(self, query: str, k: int = 10, subset: list[str] | None = None) -> list[SearchResult]:
        query_text = validate_query(query)
        self._load_pylate(override=self.config.override_index)
        embeddings = self.model.encode(
            [query_text],
            batch_size=self.config.batch_size,
            is_query=True,
            show_progress_bar=False,
        )
        kwargs: dict[str, Any] = {"queries_embeddings": embeddings, "k": k}
        if subset:
            kwargs["subset"] = subset
        raw_results = self.retriever.retrieve(**kwargs)
        return [self._hydrate_result(item) for item in raw_results[0]]

    def _hydrate_result(self, item: dict[str, Any]) -> SearchResult:
        document_id = str(item["id"])
        record = self.store.get(document_id)
        return SearchResult(
            id=document_id,
            score=float(item["score"]),
            text=record.text if record else None,
            metadata=record.metadata if record else {},
        )

    def get(self, document_id: str) -> DocumentRecord | None:
        return self.store.get(document_id)

    def count(self) -> int:
        return self.store.count()

    def ready(self) -> bool:
        return self.model is not None and self.index is not None and self.retriever is not None


def validate_document(document: DocumentRecord) -> DocumentRecord:
    document_id = str(document.id).strip()
    text = str(document.text).strip()
    if not document_id:
        raise ValueError("document id is required")
    if not text:
        raise ValueError(f"document text is required for id={document_id}")
    return DocumentRecord(id=document_id, text=text, metadata=dict(document.metadata or {}))


def validate_query(query: str) -> str:
    query_text = str(query).strip()
    if not query_text:
        raise ValueError("query is required")
    return query_text


def create_app(adapter: ColbertAdapter):
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel, Field

    class DocumentPayload(BaseModel):
        id: str
        text: str
        metadata: dict[str, Any] = Field(default_factory=dict)

    class UpsertRequest(BaseModel):
        documents: list[DocumentPayload]
        rebuild: bool = False

    class SearchRequest(BaseModel):
        query: str
        k: int = 10
        subset: list[str] | None = None

    app = FastAPI(title="LFM2-ColBERT mem0 Sidecar", version="1.0.0")

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "model_id": adapter.config.model_id,
            "index_folder": str(adapter.config.index_folder),
            "index_name": adapter.config.index_name,
            "indexed_count": adapter.count(),
            "ready": adapter.ready(),
            "scoring": "maxsim",
        }

    @app.get("/mem0/config")
    def mem0_config() -> dict[str, Any]:
        return {
            "sidecar": {
                "provider": "lfm2-colbert-sidecar",
                "base_url": f"http://{adapter.config.host}:{adapter.config.port}",
                "model": adapter.config.model_id,
                "embedding_shape": "multi_vector_token_embeddings",
                "scoring": "maxsim",
            },
            "mem0_note": "Use this sidecar for retrieval upsert/search; do not configure it as a single-vector mem0 embedder.",
        }

    @app.post("/documents/upsert")
    def upsert(request: UpsertRequest) -> dict[str, Any]:
        try:
            indexed_count = adapter.upsert(
                [
                    DocumentRecord(
                        id=document.id,
                        text=document.text,
                        metadata=document.metadata,
                    )
                    for document in request.documents
                ],
                rebuild=request.rebuild,
            )
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"indexed_count": indexed_count}

    @app.post("/search")
    def search(request: SearchRequest) -> dict[str, Any]:
        try:
            results = adapter.search(query=request.query, k=request.k, subset=request.subset)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"results": [asdict(result) for result in results]}

    @app.get("/documents/{document_id}")
    def get_document(document_id: str) -> dict[str, Any]:
        document = adapter.get(document_id)
        if document is None:
            raise HTTPException(status_code=404, detail="document not found")
        return asdict(document)

    return app


def parse_args() -> SidecarConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-id", default=COLBERT_MODEL_ID)
    parser.add_argument("--index-folder", type=Path, default=DEFAULT_INDEX_FOLDER)
    parser.add_argument("--index-name", default=DEFAULT_INDEX_NAME)
    parser.add_argument("--metadata-path", type=Path, default=DEFAULT_METADATA_PATH)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8766)
    parser.add_argument("--override-index", action="store_true")
    parser.add_argument("--eager-load", action="store_true")
    args = parser.parse_args()
    return SidecarConfig(
        model_id=args.model_id,
        index_folder=args.index_folder,
        index_name=args.index_name,
        metadata_path=args.metadata_path,
        batch_size=args.batch_size,
        host=args.host,
        port=args.port,
        override_index=args.override_index,
        lazy_load=not args.eager_load,
    )


def main() -> None:
    import uvicorn

    config = parse_args()
    adapter = PylateColbertAdapter(config)
    uvicorn.run(create_app(adapter), host=config.host, port=config.port)


if __name__ == "__main__":
    main()
