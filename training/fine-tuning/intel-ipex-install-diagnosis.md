# Intel Extension for PyTorch Install Diagnosis

Date: 2026-05-31

## Current Environment

- OS: Windows
- Python: 3.11.15
- Active Python environment: `C:\Users\60217257\AppData\Local\hermes\hermes-agent\venv`
- PyTorch: `2.12.0+cpu`
- WSL: not installed

## Commands Run

```powershell
python -c "import torch; print(torch.__version__)"
python -c "import intel_extension_for_pytorch as ipex; print(ipex.__version__)"
python -m pip index versions intel-extension-for-pytorch
python -m pip index versions intel_extension_for_pytorch
wsl --status
```

## Result

`intel_extension_for_pytorch` is not installed, and pip cannot find a compatible Windows wheel for either package spelling in the active Python environment.

Current Intel documentation says Intel Extension for PyTorch is scheduled for end of life by the end of March 2026 and recommends using native PyTorch going forward because Intel CPU and GPU hardware support has been upstreamed. The PyPI package files for the latest IPEX release are Linux `manylinux` wheels, not Windows wheels.

## Conclusion

The task `Install intel-extension-for-pytorch matching PyTorch version` is blocked in the current Windows environment. A supported path would require a Linux environment with a PyTorch/IPEX-compatible version pair, or replacing this template step with native PyTorch 2.12 Intel CPU/GPU validation.
