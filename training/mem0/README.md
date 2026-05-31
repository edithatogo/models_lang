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

Run the retrieval fine-tune stage with a Hugging Face triplet dataset:

```powershell
python training\mem0\lfm2_colbert_finetune.py --dataset-id sentence-transformers/msmarco-bm25 --dataset-name triplet --max-steps 100 --output-dir training\fine-tuning\lfm2-colbert-350m-mem0
```
