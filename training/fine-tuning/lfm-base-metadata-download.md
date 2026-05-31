# LFM Base Metadata Download

Date: 2026-05-31

## Script

- `training/fine-tuning/download_lfm_base_metadata.py`

## Fetch Result

Downloaded only the small public metadata files for `LiquidAI/lfm2.5-1.2b-instruct` into:

- `C:\tmp\lfm2.5-1.2b-instruct-meta-script`

Fetched files:

- `config.json`
- `generation_config.json`
- `special_tokens_map.json`
- `tokenizer_config.json`
- `tokenizer.json`

The downloader resolved no token in this shell (`token_source=null`) because the repository metadata files are public.

## Notes

This advances the track's local model setup without pulling the full checkpoint weights. The full model download and IPEX-backed training path remain blocked on this Windows host.
