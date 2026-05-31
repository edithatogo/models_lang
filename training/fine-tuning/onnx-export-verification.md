# ONNX Export Verification

Date: 2026-05-31

## Runtime Packages Installed

- `onnx==1.21.0`
- `onnxscript==0.7.0`
- `onnx_ir==0.2.1`
- `ml_dtypes==0.5.4`

`onnxscript` is required by the PyTorch 2.12 ONNX exporter.

## Export Script

Added:

- `training/fine-tuning/export_lora_smoke_onnx.py`

The script reloads the synthetic LoRA smoke checkpoint, exports the model to ONNX, validates it with `onnx.checker.check_model`, and writes a JSON export report.

## Command

```powershell
python training\fine-tuning\export_lora_smoke_onnx.py --checkpoint training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\adapter_smoke.pt --output training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\model.onnx
```

## Result

```text
onnx_path=training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\model.onnx
opset=18
nodes=5
```

Saved files:

- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/model.onnx`
- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/model.json`

Validation:

```powershell
python -c "import onnx; m=onnx.load('training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/model.onnx'); onnx.checker.check_model(m); print(len(m.graph.node))"
```

Result:

```text
5
```

## Notes

PyTorch emitted warnings about `dynamic_axes` with the dynamo exporter and missing optional torchvision registrations. The export and ONNX checker validation still succeeded.
