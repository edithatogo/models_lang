# Publish Readiness

Date: 2026-05-31

## GitHub

Prepared local root repository:

- Repo path: `C:\Users\60217257\repos\models_lang`
- Target GitHub repo: `edithatogo/models_lang`
- Public URL: `https://github.com/edithatogo/models_lang`
- Local commits:
  - `1c05042 feat(training): add Intel OpenVINO LoRA smoke pipeline`
  - `a404510 feat(training): add OpenVINO INT8 smoke artifacts`
  - `2e85f2f test(training): add OpenVINO CPU latency validation`
  - `docs(training): prepare external publish handoff` (this manifest and model-card handoff)
  - `62687c8 docs(training): add Hugging Face repo card metadata`

GitHub publication completed after public visibility approval. `gh repo view edithatogo/models_lang --json name,owner,visibility,url,defaultBranchRef` reported `visibility=PUBLIC`, URL `https://github.com/edithatogo/models_lang`, and default branch `main`. Remote `main` was verified after pushing pipeline and Hugging Face repo-card metadata commit `62687c8633881d3bf83a9224837a53bb0df20da7`; this verification note was pushed afterward.

## Hugging Face

Prepared artifact directory:

- Local path: `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke`
- Target model repo: `edithatogo/lfm2.5-1.2b-intel-lora`
- Public URL: `https://huggingface.co/edithatogo/lfm2.5-1.2b-intel-lora`

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

Hugging Face publication completed after public visibility approval. Upload commit: `https://huggingface.co/edithatogo/lfm2.5-1.2b-intel-lora/commit/91f6077b131deb59b05845d4db689d60329ec774`.

Selected remote files were downloaded to `C:\tmp\models_lang_hf_verify` and compared against local files with SHA-256. The downloaded hashes matched local hashes for `README.md`, `cpu_latency.json`, `openvino-int8/model_int8_quantization.json`, and `model.json`.
