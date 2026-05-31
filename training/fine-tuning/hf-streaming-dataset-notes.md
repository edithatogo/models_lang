# Hugging Face Streaming Dataset Notes

Date: 2026-05-31

## Added to `intel_lora_train.py`

- `dataset_split` and `max_length` fields on `TrainingConfig`
- `--dataset-split` and `--max-length` CLI arguments
- `load_streaming_dataset(dataset_id, split)` using `load_dataset(..., streaming=True)`
- `format_training_text(example)` supporting:
  - ready-made `text` examples
  - instruction/input/output records
- `tokenize_training_example(example, tokenizer, max_length)` that copies `input_ids` into `labels`

The training path now maps the streaming dataset through the reusable tokenizer helper.

## Verification

```powershell
python -m pytest training\tests\test_intel_lora_config.py
```

Result:

```text
6 passed
```

Pytest reported a cache write warning under `.pytest_cache`, but the tests passed.

## Runtime Notes

Full Hugging Face dataset streaming still requires the `datasets` package, which is not installed in the active environment. The import remains lazy so configuration tests can run without pulling training dependencies.
