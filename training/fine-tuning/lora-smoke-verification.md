# LoRA Smoke Verification

Date: 2026-05-31

## Runtime Packages Installed

- `peft==0.19.1`
- `datasets==4.8.5`
- `accelerate==1.13.0`

Pip also changed `fsspec` from `2026.4.0` to `2026.2.0` to satisfy `datasets`.

## Smoke Runner

Added:

- `training/fine-tuning/run_lora_smoke.py`

The smoke runner uses a tiny synthetic LoRA linear layer so verification is offline and bounded. It trains only adapter weights for exactly five steps, then saves the adapter checkpoint and a JSON result file.

## Command

```powershell
python training\fine-tuning\run_lora_smoke.py --steps 5 --output-dir training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke
```

## Result

```text
steps=5
initial_norm=0.03983466
final_norm=2.32895434
changed=True
checkpoint=training\fine-tuning\lfm2.5-1.2b-intel-lora-smoke\adapter_smoke.pt
```

Saved files:

- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/adapter_smoke.pt`
- `training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/smoke_result.json`

## Additional Verification

```powershell
python -m pytest training\tests\test_intel_lora_config.py
```

Result:

```text
6 passed
```

## Dependency Caveat

`pip check` still reports unresolved `voxcpm 2.0.3` dependencies and a `datasets` version mismatch:

```text
voxcpm 2.0.3 has requirement datasets<4,>=3, but you have datasets 4.8.5.
```

The LoRA smoke test completed despite that environment-level conflict.
