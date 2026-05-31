"""Validate OpenVINO IR inference on CPU and record latency metrics."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import openvino as ov


def percentile(values: list[float], p: float) -> float:
    if not values:
        raise ValueError("Cannot compute percentile of an empty list")
    return float(np.percentile(np.array(values, dtype=np.float64), p))


def run_model(xml_path: Path, inputs: np.ndarray, iterations: int, warmup: int) -> tuple[np.ndarray, list[float]]:
    core = ov.Core()
    compiled = core.compile_model(core.read_model(xml_path), "CPU")
    input_port = compiled.inputs[0]
    output_port = compiled.outputs[0]

    for _ in range(warmup):
        compiled({input_port: inputs})[output_port]

    latencies_ms: list[float] = []
    output = None
    for _ in range(iterations):
        start = time.perf_counter()
        output = compiled({input_port: inputs})[output_port]
        latencies_ms.append((time.perf_counter() - start) * 1000.0)

    return np.asarray(output), latencies_ms


def validate_latency(
    fp_xml: Path,
    int8_xml: Path,
    output_path: Path,
    iterations: int = 50,
    warmup: int = 5,
    seed: int = 13,
) -> dict[str, float | str | int | bool]:
    rng = np.random.default_rng(seed)
    inputs = rng.normal(size=(1, 8)).astype(np.float32)

    fp_output, fp_latencies = run_model(fp_xml, inputs, iterations, warmup)
    int8_output, int8_latencies = run_model(int8_xml, inputs, iterations, warmup)

    max_abs_diff = float(np.max(np.abs(fp_output - int8_output)))
    result = {
        "device": "CPU",
        "iterations": iterations,
        "warmup": warmup,
        "fp_xml": str(fp_xml),
        "int8_xml": str(int8_xml),
        "fp_mean_ms": float(np.mean(fp_latencies)),
        "fp_p50_ms": percentile(fp_latencies, 50),
        "fp_p95_ms": percentile(fp_latencies, 95),
        "int8_mean_ms": float(np.mean(int8_latencies)),
        "int8_p50_ms": percentile(int8_latencies, 50),
        "int8_p95_ms": percentile(int8_latencies, 95),
        "max_abs_diff": max_abs_diff,
        "predictions_finite": bool(np.isfinite(int8_output).all()),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fp-xml",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-ir/model.xml"),
    )
    parser.add_argument(
        "--int8-xml",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/openvino-int8/model_int8.xml"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke/cpu_latency.json"),
    )
    parser.add_argument("--iterations", type=int, default=50)
    parser.add_argument("--warmup", type=int, default=5)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    metrics = validate_latency(args.fp_xml, args.int8_xml, args.output, args.iterations, args.warmup)
    print(f"device={metrics['device']}")
    print(f"iterations={metrics['iterations']}")
    print(f"int8_mean_ms={metrics['int8_mean_ms']:.6f}")
    print(f"int8_p95_ms={metrics['int8_p95_ms']:.6f}")
    print(f"max_abs_diff={metrics['max_abs_diff']:.8f}")
    print(f"predictions_finite={metrics['predictions_finite']}")
