# Publish Verification

Date: 2026-05-31

## GitHub

- Repository: `https://github.com/edithatogo/models_lang`
- Visibility: `PUBLIC`
- Default branch: `main`
- Verified pipeline/repo-card commit on remote `main`: `62687c8633881d3bf83a9224837a53bb0df20da7`
- This verification note was pushed afterward, so the live branch head may be newer.

Commands used:

```powershell
gh repo view edithatogo/models_lang --json name,owner,visibility,url,defaultBranchRef
git ls-remote --heads origin main
```

## Hugging Face

- Model repository: `https://huggingface.co/edithatogo/lfm2.5-1.2b-intel-lora`
- Upload commit: `https://huggingface.co/edithatogo/lfm2.5-1.2b-intel-lora/commit/91f6077b131deb59b05845d4db689d60329ec774`

Selected remote files were downloaded to `C:\tmp\models_lang_hf_verify` and compared against local files with SHA-256.

Matched hashes:

- `README.md`: `046A73E0AFE6E3E0A6540D633BAA97143CAFD1BF34A3B5B02E3A6CBA9EAC9990`
- `cpu_latency.json`: `3227B9D637F7796972F5DC3647D477EDD2028C5900435322EB61727A02C7FD67`
- `openvino-int8/model_int8_quantization.json`: `1B1FA873E82C2971D11AADEE43D02C6494C31DAFD7A0572BEC0DED843F7DFE41`
- `model.json`: `006C23B3B97004F1B57BC84D86D8A497E9235380816D48A8EA9EA7BCF60D6F4F`

Commands used:

```powershell
hf repo create edithatogo/lfm2.5-1.2b-intel-lora --type model --public --exist-ok
hf upload edithatogo/lfm2.5-1.2b-intel-lora training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke . --repo-type model
hf download edithatogo/lfm2.5-1.2b-intel-lora README.md cpu_latency.json openvino-int8/model_int8_quantization.json model.json --repo-type model --local-dir C:\tmp\models_lang_hf_verify --force-download
Get-FileHash -Algorithm SHA256 <local-and-downloaded-files>
```
