# Publish Readiness

Date: 2026-05-31

## GitHub

Prepared local root repository:

- Repo path: `C:\Users\60217257\repos\models_lang`
- Target GitHub repo: `edithatogo/models_lang`
- Local commits:
  - `1c05042 feat(training): add Intel OpenVINO LoRA smoke pipeline`
  - `a404510 feat(training): add OpenVINO INT8 smoke artifacts`
  - `2e85f2f test(training): add OpenVINO CPU latency validation`
  - `docs(training): prepare external publish handoff` (this manifest and model-card handoff)

The external GitHub create/push step is blocked pending explicit repo visibility confirmation: `public` or `private`.

## Hugging Face

Prepared artifact directory:

- Local path: `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke`
- Target model repo: `edithatogo/lfm2.5-1.2b-intel-lora`

Files prepared for upload:

- `README.md`
- `MODEL_CARD.md`
- `adapter_smoke.pt`
- `smoke_result.json`
- `model.onnx`
- `model.json`
- `model.onnx.data`
- `openvino-ir/model.xml`
- `openvino-ir/model.bin`
- `openvino-ir/model_ir.json`
- `openvino-int8/model_int8.xml`
- `openvino-int8/model_int8.bin`
- `openvino-int8/model_int8_quantization.json`
- `cpu_latency.json`

The external Hugging Face repo create/upload step is blocked pending explicit repo visibility confirmation: `public` or `private`.
