"""Convert a validated ONNX model to OpenVINO IR and verify it reloads."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import openvino as ov


def convert_to_ir(onnx_path: Path, output_dir: Path, model_name: str = "model") -> dict[str, str | int]:
    output_dir.mkdir(parents=True, exist_ok=True)
    xml_path = output_dir / f"{model_name}.xml"
    bin_path = output_dir / f"{model_name}.bin"

    ov_model = ov.convert_model(onnx_path)
    ov.save_model(ov_model, xml_path)

    core = ov.Core()
    reloaded = core.read_model(xml_path)

    report = {
        "onnx_path": str(onnx_path),
        "xml_path": str(xml_path),
        "bin_path": str(bin_path),
        "inputs": len(reloaded.inputs),
        "outputs": len(reloaded.outputs),
        "ops": len(reloaded.get_ordered_ops()),
    }
    (output_dir / f"{model_name}_ir.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--onnx",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/model.onnx"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-ir"),
    )
    parser.add_argument("--model-name", default="model")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = convert_to_ir(args.onnx, args.output_dir, args.model_name)
    print(f"xml_path={result['xml_path']}")
    print(f"bin_path={result['bin_path']}")
    print(f"inputs={result['inputs']}")
    print(f"outputs={result['outputs']}")
    print(f"ops={result['ops']}")
