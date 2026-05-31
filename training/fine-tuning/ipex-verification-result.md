# IPEX Verification Result

Date: 2026-05-31

## Command

```powershell
python -c "import intel_extension_for_pytorch as ipex"
```

## Result

The verification failed:

```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'intel_extension_for_pytorch'
```

PyTorch itself imports successfully:

```powershell
python -c "import torch; print(torch.__version__)"
```

```text
2.12.0+cpu
```

## Assessment

This verifies the earlier install blocker rather than completing the IPEX backend check. The active Windows Python environment does not have a compatible IPEX package installed.
