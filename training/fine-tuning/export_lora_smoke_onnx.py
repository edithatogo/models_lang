"""Export the synthetic LoRA smoke model to ONNX and validate the graph."""

from __future__ import annotations

import argparse
import contextlib
import io
import importlib.util
import json
import sys
from pathlib import Path

import torch


SMOKE_SCRIPT = Path(__file__).with_name("run_lora_smoke.py")


def load_smoke_module():
    spec = importlib.util.spec_from_file_location("run_lora_smoke", SMOKE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def export_onnx(checkpoint_path: Path, output_path: Path) -> dict[str, str | int]:
    import onnx

    smoke = load_smoke_module()
    model = smoke.TinyLoraLinear()
    state = torch.load(checkpoint_path, map_location="cpu")
    model.lora_a.data.copy_(state["lora_a"])
    model.lora_b.data.copy_(state["lora_b"])
    model.eval()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    example_inputs = torch.randn(1, 8)
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        torch.onnx.export(
            model,
            example_inputs,
            output_path,
            input_names=["inputs"],
            output_names=["outputs"],
            dynamic_axes={"inputs": {0: "batch"}, "outputs": {0: "batch"}},
            opset_version=18,
        )

    onnx_model = onnx.load(output_path)
    onnx.checker.check_model(onnx_model)

    report = {
        "checkpoint_path": str(checkpoint_path),
        "onnx_path": str(output_path),
        "opset": 18,
        "graph_name": onnx_model.graph.name,
        "inputs": len(onnx_model.graph.input),
        "outputs": len(onnx_model.graph.output),
        "nodes": len(onnx_model.graph.node),
    }
    report_path = output_path.with_suffix(".json")
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/adapter_smoke.pt"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/model.onnx"),
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = export_onnx(args.checkpoint, args.output)
    print(f"onnx_path={result['onnx_path']}")
    print(f"opset={result['opset']}")
    print(f"nodes={result['nodes']}")
