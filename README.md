# models_lang

Local model fine-tuning and optimization experiments.

## Current Track

The active work is the Intel/OpenVINO LoRA optimization pipeline under `training/fine-tuning`.

Implemented artifacts include:

- LoRA training scaffold with native PyTorch BF16 defaults and optional legacy IPEX hooks: `training/fine-tuning/intel_lora_train.py`
- Hugging Face streaming dataset helpers and tests
- LFM metadata downloader and local preflight validation
- Synthetic 5-step LoRA smoke training
- ONNX export for the smoke model
- OpenVINO IR conversion for the exported ONNX model

## Verification Commands

```powershell
python -m pytest training\tests\test_intel_lora_config.py
python -m pytest training\tests\test_lfm_base_download.py
python training\fine-tuning\download_lfm_base_metadata.py --output-dir C:\tmp\lfm2.5-1.2b-instruct-meta-script
python training\fine-tuning\intel_lora_train.py --preflight-only --metadata-dir C:\tmp\lfm2.5-1.2b-instruct-meta-script --model-id LiquidAI/lfm2.5-1.2b-instruct
python training\fine-tuning\run_lora_smoke.py --steps 5 --output-dir training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke
python training\fine-tuning\export_lora_smoke_onnx.py --checkpoint training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\adapter_smoke.pt --output training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\model.onnx
python training\fine-tuning\convert_onnx_to_openvino_ir.py --onnx training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\model.onnx --output-dir training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-ir --model-name model
```

## Known Environment Caveats

- IPEX is a deprecated optional accelerator for compatible Linux runtimes. It is blocked in the current Windows/Python/PyTorch environment, so the supported Windows path is native PyTorch plus OpenVINO/NNCF.
- OpenVINO telemetry emits access warnings under `AppData\Local\Intel Corporation`, but runtime conversion succeeds.
- `voxcpm` has unresolved environment dependency conflicts unrelated to this smoke pipeline.
