# models_lang

Local model fine-tuning and optimization experiments.

## Current Track

The active work is the Intel/OpenVINO LoRA optimization pipeline under `training/fine-tuning`.

Implemented artifacts include:

- LoRA training scaffold with native PyTorch BF16 defaults and optional legacy IPEX hooks: `training/fine-tuning/intel_lora_train.py`
- Hugging Face streaming dataset helpers and tests
- LFM metadata downloader and local preflight validation
- mem0 retrieval embedding contract pinned to `LiquidAI/LFM2-ColBERT-350M`
- Bootstrap mem0 fact-extraction and retrieval-triplet dataset builder
- LFM2-ColBERT contrastive triplet fine-tuning entrypoint and local sidecar for mem0 retrieval
- Synthetic 5-step LoRA smoke training
- ONNX export for the smoke model
- OpenVINO IR conversion for the exported ONNX model

## Verification Commands

```powershell
python -m pytest training\tests\test_intel_lora_config.py
python -m pytest training\tests\test_lfm_base_download.py
python -m pytest training\tests\test_mem0_lfm2_colbert_config.py
python -m pytest training\tests\test_lfm2_colbert_finetune.py
python -m pytest training\tests\test_mem0_dataset_builder.py
python training\fine-tuning\download_lfm_base_metadata.py --output-dir C:\tmp\lfm2.5-1.2b-instruct-meta-script
python training\fine-tuning\intel_lora_train.py --preflight-only --metadata-dir C:\tmp\lfm2.5-1.2b-instruct-meta-script --model-id LiquidAI/lfm2.5-1.2b-instruct
python training\mem0\lfm2_colbert_config.py --output training\mem0\mem0_lfm2_colbert_config.json
python training\mem0\build_mem0_datasets.py --output-dir training\mem0\datasets\bootstrap
python training\mem0\lfm2_colbert_sidecar.py --host 127.0.0.1 --port 8766
python training\mem0\lfm2_colbert_finetune.py --dataset-id sentence-transformers/msmarco-bm25 --dataset-name triplet --max-steps 100
python training\fine-tuning\run_lora_smoke.py --steps 5 --output-dir training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke
python training\fine-tuning\export_lora_smoke_onnx.py --checkpoint training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\adapter_smoke.pt --output training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\model.onnx
python training\fine-tuning\convert_onnx_to_openvino_ir.py --onnx training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\model.onnx --output-dir training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-ir --model-name model
```

## Known Environment Caveats

- IPEX is a deprecated optional accelerator for compatible Linux runtimes. It is blocked in the current Windows/Python/PyTorch environment, so the supported Windows path is native PyTorch plus OpenVINO/NNCF.
- OpenVINO telemetry emits access warnings under `AppData\Local\Intel Corporation`, but runtime conversion succeeds.
- PyLate/FastPLAID for the mem0 ColBERT sidecar installs a Torch 2.9-aligned stack and can conflict with the OpenVINO/NNCF smoke environment. Prefer an isolated sidecar environment when running both workflows.
- `voxcpm` has unresolved environment dependency conflicts unrelated to this smoke pipeline.
