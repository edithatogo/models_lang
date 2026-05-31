# LFM Preflight Verification

Date: 2026-05-31

## Command

```powershell
training\fine-tuning\intel_lora_train.py --preflight-only --metadata-dir C:\tmp\lfm2.5-1.2b-instruct-meta-script --model-id LiquidAI/lfm2.5-1.2b-instruct
```

## Result

```json
{
  "metadata_dir": "C:\\tmp\\lfm2.5-1.2b-instruct-meta-script",
  "repo_id": "LiquidAI/lfm2.5-1.2b-instruct",
  "tokenizer_loaded": true,
  "config_loaded": true,
  "tokenized_keys": [
    "attention_mask",
    "input_ids",
    "labels"
  ],
  "token_source": null
}
```

## Assessment

The local metadata-only preflight is working. It verifies that the downloaded tokenizer/config files can be loaded and that the training text formatter and tokenizer plumbing produce the expected training example keys.

This does not complete the full LFM training step, which still requires the full base model checkpoint and a Windows-compatible IPEX path.
