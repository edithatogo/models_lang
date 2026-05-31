# INT8 Quantization Verification

Date: 2026-05-31

## Quantization Script

Added:

- `training/fine-tuning/quantize_openvino_ir_int8.py`

The script loads the OpenVINO IR model, creates synthetic calibration data with 16 samples, runs `nncf.quantize`, saves an INT8 OpenVINO IR model, reloads it, and writes a JSON report.

## Dependency Resolution

Initial attempt with `nncf==3.1.0` failed against `openvino==2024.6.0`:

```text
AttributeError: module 'openvino' has no attribute 'Node'
```

The working quantization environment uses:

- `openvino==2024.6.0`
- `openvino-dev==2024.6.0`
- `nncf==2.8.0`

The NNCF downgrade temporarily changed `rich` and `tzdata`; those were restored to the versions required by `hermes-agent`:

- `rich==14.3.3`
- `tzdata==2025.3`

## Command

```powershell
python training\fine-tuning\quantize_openvino_ir_int8.py --xml training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-ir\model.xml --output-dir training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-int8 --model-name model_int8
```

## Result

```text
xml_path=training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-int8\model_int8.xml
bin_path=training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-int8\model_int8.bin
inputs=1
outputs=1
ops=41
int8_related_ops=11
```

Saved files:

- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-int8/model_int8.xml`
- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-int8/model_int8.bin`
- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-int8/model_int8_quantization.json`

## Remaining Environment Caveat

`pip check` still reports unresolved `voxcpm 2.0.3` dependencies and its `datasets<4,>=3` constraint. The INT8 quantization run completed despite those unrelated environment issues.
