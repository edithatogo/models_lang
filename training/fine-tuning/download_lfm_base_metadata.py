"""Download the small public metadata files for the LFM base model.

This keeps the track moving without pulling the full checkpoint. The script
resolves Hugging Face tokens from the common environment variable names so it
works in the same shell setups used by the rest of the repo.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_REPO_ID = "LiquidAI/lfm2.5-1.2b-instruct"
DEFAULT_OUTPUT_DIR = Path("training/fine-tuning/lfm2.5-1.2b-instruct-meta")
DEFAULT_FILES = (
    "config.json",
    "generation_config.json",
    "special_tokens_map.json",
    "tokenizer_config.json",
    "tokenizer.json",
)


@dataclass(frozen=True)
class DownloadResult:
    repo_id: str
    output_dir: Path
    revision: str | None
    token_source: str | None
    files: tuple[str, ...]


def resolve_hf_token(explicit_token: str | None = None) -> tuple[str | None, str | None]:
    if explicit_token:
        return explicit_token, "explicit"

    for env_name in ("HF_TOKEN", "HUGGINGFACE_HUB_TOKEN", "HF_HUB_TOKEN"):
        token = os.environ.get(env_name)
        if token:
            return token, env_name

    return None, None


def download_lfm_base_metadata(
    repo_id: str = DEFAULT_REPO_ID,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    files: Iterable[str] = DEFAULT_FILES,
    revision: str | None = None,
    token: str | None = None,
) -> DownloadResult:
    from huggingface_hub import snapshot_download

    output_dir.mkdir(parents=True, exist_ok=True)
    resolved_token, token_source = resolve_hf_token(token)
    snapshot_download(
        repo_id=repo_id,
        repo_type="model",
        allow_patterns=list(files),
        local_dir=output_dir,
        local_dir_use_symlinks=False,
        revision=revision,
        token=resolved_token,
    )

    manifest = DownloadResult(
        repo_id=repo_id,
        output_dir=output_dir,
        revision=revision,
        token_source=token_source,
        files=tuple(files),
    )
    (output_dir / "download_manifest.json").write_text(
        json.dumps(
            {
                "repo_id": manifest.repo_id,
                "output_dir": str(manifest.output_dir),
                "revision": manifest.revision,
                "token_source": manifest.token_source,
                "files": list(manifest.files),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-id", default=DEFAULT_REPO_ID)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--revision")
    parser.add_argument("--token")
    parser.add_argument("--files", nargs="+", default=list(DEFAULT_FILES))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = download_lfm_base_metadata(
        repo_id=args.repo_id,
        output_dir=args.output_dir,
        files=args.files,
        revision=args.revision,
        token=args.token,
    )
    print(
        json.dumps(
            {
                "repo_id": result.repo_id,
                "output_dir": str(result.output_dir),
                "revision": result.revision,
                "token_source": result.token_source,
                "files": list(result.files),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
