---
license: apache-2.0
tags:
  - openvino
  - int8
  - onnx
  - lora
  - smoke-test
  - cpu
library_name: openvino
pipeline_tag: feature-extraction
---

# LFM Intel LoRA Smoke Artifacts

This repository contains tiny synthetic artifacts for validating an Intel/OpenVINO LoRA optimization pipeline.

It does not contain full `LiquidAI/lfm2.5-1.2b-instruct` model weights. The current Windows environment blocks the IPEX-backed path, so the files here validate the mechanics of LoRA adapter training, ONNX export, OpenVINO IR conversion, INT8 quantization, and CPU inference latency on a small synthetic model.

## Artifacts

- `adapter_smoke.pt`: synthetic LoRA adapter checkpoint from a 5-step smoke run
- `smoke_result.json`: smoke training metrics
- `model.onnx`: ONNX export of the tiny smoke model
- `model.json`: ONNX export metadata
- `openvino-ir/model.xml`: FP OpenVINO IR definition
- `openvino-ir/model.bin`: FP OpenVINO IR weights
- `openvino-ir/model_ir.json`: FP OpenVINO IR conversion metadata
- `openvino-int8/model_int8.xml`: INT8 OpenVINO IR definition
- `openvino-int8/model_int8.bin`: INT8 OpenVINO IR weights
- `openvino-int8/model_int8_quantization.json`: INT8 quantization metadata
- `cpu_latency.json`: CPU latency validation metrics

## CPU Validation

Measured on CPU with 50 iterations after 5 warmups:

- FP mean latency: `0.053568 ms`
- FP p95 latency: `0.065855 ms`
- INT8 mean latency: `0.061286 ms`
- INT8 p95 latency: `0.087240 ms`
- Max FP-vs-INT8 absolute difference: `0.64642227`
- INT8 predictions finite: `true`

## Environment Notes

- `openvino==2024.6.0`
- `openvino-dev==2024.6.0`
- `nncf==2.8.0`
- `onnx==1.21.0`
- `onnxscript==0.7.0`

`nncf==3.1.0` was incompatible with `openvino==2024.6.0` in this environment because `openvino.Node` is not available. `nncf==2.8.0` successfully produced the INT8 IR.

## Intended Use

Use these files as a small reproducible smoke package for pipeline validation. Do not treat them as a real fine-tuned LFM checkpoint.

