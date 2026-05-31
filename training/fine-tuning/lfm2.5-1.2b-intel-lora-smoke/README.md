# LFM Intel LoRA Smoke Artifacts

This repository snapshot contains a bounded synthetic smoke test for the Intel/OpenVINO LoRA optimization pipeline.

The artifacts are intentionally tiny. They verify pipeline mechanics without downloading or publishing full LFM model weights.

## Files

- `adapter_smoke.pt`: synthetic LoRA adapter checkpoint from a 5-step smoke run
- `smoke_result.json`: smoke run metrics
- `model.onnx`: ONNX export of the tiny smoke model
- `model.json`: ONNX export metadata
- `openvino-ir/model.xml`: OpenVINO IR model definition
- `openvino-ir/model.bin`: OpenVINO IR weights
- `openvino-ir/model_ir.json`: OpenVINO IR conversion metadata

## Status

The real IPEX-backed path is blocked on the current Windows environment because `intel_extension_for_pytorch` is not available for the active PyTorch/Python pairing. The smoke pipeline uses native PyTorch and OpenVINO APIs where available.

