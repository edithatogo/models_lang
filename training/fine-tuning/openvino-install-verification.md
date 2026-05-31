# OpenVINO Install Verification

Date: 2026-05-31

## Installed Packages

- `openvino==2024.6.0`
- `openvino-dev==2024.6.0`
- `openvino-telemetry==2025.2.0`

Pip resolved `openvino-dev==2024.6.0` with `openvino==2024.6.0`.

## Dependency Changes

- `numpy` changed from `2.4.6` to `1.26.4`
- `networkx` changed from `3.6.1` to `3.1`

These versions were selected by pip to satisfy `openvino-dev==2024.6.0`.

## Verification Commands

```powershell
python -c "import openvino as ov; print(ov.__version__)"
python -c "import torch, numpy, networkx; print(torch.__version__); print(numpy.__version__); print(networkx.__version__)"
python -m pip show openvino openvino-dev
python -m pip check
```

## Results

OpenVINO import succeeded:

```text
2024.6.0-17404-4c0f47d2335-releases/2024/6
```

PyTorch and dependency imports succeeded:

```text
2.12.0+cpu
1.26.4
3.1
```

`pip check` reports missing dependencies for `voxcpm 2.0.3`:

```text
datasets, funasr, gradio, inflect, modelscope, simplejson, spaces, torchcodec, wetext
```

No OpenVINO dependency conflict was reported.
