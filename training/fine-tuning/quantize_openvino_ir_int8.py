"""Quantize an OpenVINO IR model to INT8 with NNCF calibration data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import nncf
import numpy as np
import openvino as ov


def make_calibration_dataset(input_name: str, sample_count: int = 16, seed: int = 13):
    rng = np.random.default_rng(seed)
    samples = [
        {input_name: rng.normal(size=(1, 8)).astype(np.float32)}
        for _ in range(sample_count)
    ]
    return nncf.Dataset(samples)


def quantize_ir(xml_path: Path, output_dir: Path, model_name: str = "model_int8") -> dict[str, str | int]:
    output_dir.mkdir(parents=True, exist_ok=True)
    core = ov.Core()
    model = core.read_model(xml_path)
    input_name = model.inputs[0].get_any_name()
    calibration_dataset = make_calibration_dataset(input_name)

    quantized_model = nncf.quantize(model, calibration_dataset)

    xml_out = output_dir / f"{model_name}.xml"
    bin_out = output_dir / f"{model_name}.bin"
    ov.save_model(quantized_model, xml_out)

    reloaded = core.read_model(xml_out)
    op_types = [op.get_type_name() for op in reloaded.get_ordered_ops()]
    int8_related_ops = sum(1 for op_type in op_types if op_type in {"FakeQuantize", "Convert", "Subtract", "Multiply"})

    report = {
        "source_xml": str(xml_path),
        "xml_path": str(xml_out),
        "bin_path": str(bin_out),
        "inputs": len(reloaded.inputs),
        "outputs": len(reloaded.outputs),
        "ops": len(op_types),
        "int8_related_ops": int8_related_ops,
        "calibration_samples": 16,
    }
    (output_dir / f"{model_name}_quantization.json").write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--xml",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-ir/model.xml"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-int8"),
    )
    parser.add_argument("--model-name", default="model_int8")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = quantize_ir(args.xml, args.output_dir, args.model_name)
    print(f"xml_path={result['xml_path']}")
    print(f"bin_path={result['bin_path']}")
    print(f"inputs={result['inputs']}")
    print(f"outputs={result['outputs']}")
    print(f"ops={result['ops']}")
    print(f"int8_related_ops={result['int8_related_ops']}")
