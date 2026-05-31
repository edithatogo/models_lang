# CLI Authentication Verification

Date: 2026-05-31

## Tools Checked

- GitHub CLI: `gh 2.92.0`
- Hugging Face CLI: `hf 1.16.4`
- Legacy `huggingface-cli`: installed shim reports deprecation and directs usage to `hf`

## Verification Commands

```powershell
gh auth status
hf auth whoami
Test-Path -LiteralPath "$env:USERPROFILE\.cache\huggingface\token"
```

## Results

GitHub CLI is authenticated to `github.com` as `edithatogo` using keyring-backed credentials.

Hugging Face CLI is authenticated as `edithatogo`, with organizations:

```text
unimelb-nlp, FlindersUni, RareInsights
```

The Hugging Face token file exists at the standard local cache path.

No token values were written to this file.
