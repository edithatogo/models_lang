"""Run a bounded 5-step LoRA smoke test on synthetic data.

This avoids downloading a base model while still verifying the mechanics the
track cares about: trainable LoRA adapter weights change and a checkpoint saves.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import torch
from torch import nn


@dataclass
class SmokeResult:
    steps: int
    initial_norm: float
    final_norm: float
    changed: bool
    checkpoint_path: Path


class TinyLoraLinear(nn.Module):
    def __init__(self, in_features: int = 8, out_features: int = 4, rank: int = 2, alpha: int = 4):
        super().__init__()
        self.base = nn.Linear(in_features, out_features)
        for parameter in self.base.parameters():
            parameter.requires_grad = False

        self.lora_a = nn.Parameter(torch.randn(in_features, rank) * 0.01)
        self.lora_b = nn.Parameter(torch.zeros(rank, out_features))
        self.scaling = alpha / rank

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        base_output = self.base(inputs)
        lora_output = inputs @ self.lora_a @ self.lora_b
        return base_output + (lora_output * self.scaling)

    def adapter_state_dict(self) -> dict[str, torch.Tensor]:
        return {
            "lora_a": self.lora_a.detach().clone(),
            "lora_b": self.lora_b.detach().clone(),
        }


def adapter_norm(model: TinyLoraLinear) -> float:
    return sum(parameter.detach().float().norm().item() for parameter in (model.lora_a, model.lora_b))


def run_smoke(output_dir: Path, steps: int = 5, seed: int = 13) -> SmokeResult:
    torch.manual_seed(seed)
    output_dir.mkdir(parents=True, exist_ok=True)

    model = TinyLoraLinear()
    optimizer = torch.optim.AdamW((model.lora_a, model.lora_b), lr=0.1)
    loss_fn = nn.MSELoss()

    inputs = torch.randn(16, 8)
    targets = torch.randn(16, 4)
    initial_norm = adapter_norm(model)

    for _ in range(steps):
        optimizer.zero_grad(set_to_none=True)
        with torch.autocast(device_type="cpu", dtype=torch.bfloat16):
            predictions = model(inputs)
            loss = loss_fn(predictions.float(), targets)
        loss.backward()
        optimizer.step()

    final_norm = adapter_norm(model)
    checkpoint_path = output_dir / "adapter_smoke.pt"
    torch.save(model.adapter_state_dict(), checkpoint_path)

    result = SmokeResult(
        steps=steps,
        initial_norm=initial_norm,
        final_norm=final_norm,
        changed=abs(final_norm - initial_norm) > 1e-8,
        checkpoint_path=checkpoint_path,
    )

    report_path = output_dir / "smoke_result.json"
    report_path.write_text(
        json.dumps(
            {
                "steps": result.steps,
                "initial_norm": result.initial_norm,
                "final_norm": result.final_norm,
                "changed": result.changed,
                "checkpoint_path": str(result.checkpoint_path),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("training/fine-tuning/lfm2.5-1.2b-intel-lora-smoke"),
    )
    parser.add_argument("--steps", type=int, default=5)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    smoke_result = run_smoke(args.output_dir, steps=args.steps)
    if not smoke_result.changed:
        raise SystemExit("LoRA adapter weights did not change")
    if not smoke_result.checkpoint_path.exists():
        raise SystemExit(f"Checkpoint was not saved: {smoke_result.checkpoint_path}")
    print(f"steps={smoke_result.steps}")
    print(f"initial_norm={smoke_result.initial_norm:.8f}")
    print(f"final_norm={smoke_result.final_norm:.8f}")
    print(f"changed={smoke_result.changed}")
    print(f"checkpoint={smoke_result.checkpoint_path}")
