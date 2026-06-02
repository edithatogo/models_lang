# mem0 LFM2-ColBERT Integration

This directory pins mem0 retrieval to `LiquidAI/LFM2-ColBERT-350M`.

LFM2-ColBERT-350M is a late-interaction retriever, not a conventional
single-vector embedding model. The mem0 integration should therefore use a
ColBERT adapter or sidecar for token-level document/query embeddings and MaxSim
scoring. Chroma can still hold memory records and metadata, but retrieval
scoring must run through the ColBERT index/adapter layer.

The pipeline has two fine-tuning stages:

1. `LiquidAI/lfm2.5-1.2b-instruct` LoRA fine-tuning for strict JSON fact
   extraction from dialogue.
2. `LiquidAI/LFM2-ColBERT-350M` retrieval fine-tuning on query, positive
   document, and negative document triples for mem0 search quality.

Generate the checked config with:

```powershell
python training\mem0\lfm2_colbert_config.py --output training\mem0\mem0_lfm2_colbert_config.json
```

Build the bootstrap mem0 datasets with:

```powershell
python training\mem0\build_mem0_datasets.py --output-dir training\mem0\datasets\bootstrap
```

This writes:

- `fact_extraction.jsonl`: LFM chat-template examples that map dialogue to strict JSON facts.
- `retrieval_triplets.jsonl`: query, positive memory, and negative memory triples for ColBERT.
- `sidecar_documents.jsonl`: memory records ready for `/documents/upsert`.
- `manifest.json`: counts and file names for verification.

Install and run the sidecar:

```powershell
pip install -r training\mem0\requirements-colbert-sidecar.txt
python training\mem0\lfm2_colbert_sidecar.py --host 127.0.0.1 --port 8766
```

By default the sidecar lazy-loads PyLate and `LiquidAI/LFM2-ColBERT-350M`.
This lets `/health` and `/mem0/config` come up immediately; the first
`/documents/upsert` or `/search` request loads the actual ColBERT model and
PLAID index. Use `--eager-load` only when you want startup to block until the
model is fully initialized.

The sidecar exposes:

- `GET /health`
- `GET /mem0/config`
- `POST /documents/upsert`
- `POST /search`
- `GET /documents/{document_id}`

`POST /documents/upsert` accepts memory records as:

```json
{
  "documents": [
    {
      "id": "mem0-memory-id",
      "text": "memory text to retrieve",
      "metadata": {
        "user_id": "user-123"
      }
    }
  ]
}
```

Runtime note for this Windows environment: installing `pylate` succeeds and the
sidecar starts, but PyLate currently installs a Torch 2.9-aligned FastPLAID
stack and pip reports version conflicts with the existing OpenVINO/NNCF smoke
environment. Keep the sidecar dependency set isolated if OpenVINO/NNCF
quantization work is running in parallel.

`POST /search` accepts:

```json
{
  "query": "what memory should I retrieve?",
  "k": 10
}
```

Run the retrieval fine-tune stage with a Hugging Face triplet dataset:

```powershell
python training\mem0\lfm2_colbert_finetune.py --dataset-id sentence-transformers/msmarco-bm25 --dataset-name triplet --max-steps 100 --output-dir training\fine-tuning\lfm2-colbert-350m-mem0
```
