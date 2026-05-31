# OpenVINO IR Conversion Verification

Date: 2026-05-31

## Conversion Script

Added:

- `training/fine-tuning/convert_onnx_to_openvino_ir.py`

The script converts an ONNX model with `openvino.convert_model`, saves OpenVINO IR with `openvino.save_model`, reloads the `.xml` through `ov.Core().read_model`, and writes a JSON report.

## Command

```powershell
python training\fine-tuning\convert_onnx_to_openvino_ir.py --onnx training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\model.onnx --output-dir training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-ir --model-name model
```

## Result

```text
xml_path=training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-ir\model.xml
bin_path=training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-ir\model.bin
inputs=1
outputs=1
ops=15
```

Saved files:

- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-ir/model.xml`
- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-ir/model.bin`
- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-ir/model_ir.json`

File sizes:

- `model.xml`: 6844 bytes
- `model.bin`: 120 bytes

## Reload Verification

```powershell
python -c "import openvino as ov; core=ov.Core(); m=core.read_model('training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-ir/model.xml'); print(len(m.inputs)); print(len(m.outputs)); print(len(m.get_ordered_ops()))"
```

Result:

```text
1
1
15
```

## Notes

OpenVINO emitted telemetry directory warnings because it could not create `AppData\Local\Intel Corporation`; conversion and reload still succeeded. During conversion, OpenVINO also logged a failed attempt to interpret the ONNX file as a PyTorch `.pt2` archive before successfully converting it as ONNX.
