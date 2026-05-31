# CPU Latency Verification

Date: 2026-05-31

## Validation Script

Added:

- `training/fine-tuning/validate_openvino_cpu_latency.py`

The script compiles both FP OpenVINO IR and INT8 OpenVINO IR on CPU, runs warmup iterations, records measured latency, checks that INT8 predictions are finite, compares INT8 output against FP output, and writes JSON metrics.

## Command

```powershell
python training\fine-tuning\validate_openvino_cpu_latency.py --iterations 50 --warmup 5 --fp-xml training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-ir\model.xml --int8-xml training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\openvino-int8\model_int8.xml --output training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\cpu_latency.json
```

## Result

```text
device=CPU
iterations=50
int8_mean_ms=0.061286
int8_p95_ms=0.087240
max_abs_diff=0.64642227
predictions_finite=True
```

Metrics file:

- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/cpu_latency.json`

Summary:

- FP mean latency: `0.053568 ms`
- FP p95 latency: `0.065855 ms`
- INT8 mean latency: `0.061286 ms`
- INT8 p95 latency: `0.087240 ms`
- Max absolute FP vs INT8 difference: `0.64642227`
- INT8 predictions finite: `true`

## Additional Checks

```powershell
python -m pytest training\tests\test_intel_lora_config.py
```

Result:

```text
6 passed
```

`pip check` still reports unresolved `voxcpm 2.0.3` dependencies and the `datasets<4,>=3` mismatch, but the CPU inference validation completed successfully.
