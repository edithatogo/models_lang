# Intel LoRA Script Notes

Date: 2026-05-31

## Added

- `training/fine-tuning/intel_lora_train.py`
- `training/tests/test_intel_lora_config.py`

## Configuration

The script defaults to:

- Model: `LiquidAI/lfm2.5-1.2b-instruct`
- Output: `training/fine-tuning/lfm2.5-1.2b-intel-lora`
- Mixed precision: BF16
- LoRA rank: `16`
- LoRA alpha: `32`
- LoRA dropout: `0.05`
- Target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`
- IPEX enabled when available

Because IPEX is unavailable in the current Windows environment, the script supports fallback mode by default and has `--require-ipex` for environments where IPEX must be mandatory.

## Verification

```powershell
python -m pytest training\tests\test_intel_lora_config.py
```

Result:

```text
3 passed
```

Pytest reported a cache write warning under `.pytest_cache`, but the tests passed.

## Remaining Runtime Dependencies

Full training execution still requires:

- `peft`
- `datasets`
- `accelerate`

The script imports these lazily only when `run_training` is executed.
