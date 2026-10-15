#!/usr/bin/env python3
"""Separate vocals and instrumental from an audio file using audio-separator (UVR models)."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
VENV_BIN = SKILL_ROOT / ".venv" / ("Scripts" if sys.platform == "win32" else "bin")
AUDIO_SEPARATOR = (
    VENV_BIN / ("audio-separator.exe" if sys.platform == "win32" else "audio-separator")
)
MODELS_DIR = SKILL_ROOT / "models"
DEFAULT_MODEL = "model_bs_roformer_ep_317_sdr_12.9755.ckpt"


def resolve_audio_separator() -> Path:
    if AUDIO_SEPARATOR.exists():
        return AUDIO_SEPARATOR
    found = subprocess.run(
        ["where", "audio-separator"] if sys.platform == "win32" else ["which", "audio-separator"],
        capture_output=True,
        text=True,
        check=False,
    )
    if found.returncode == 0 and found.stdout.strip():
        return Path(found.stdout.strip().splitlines()[0])
    raise SystemExit(
        "audio-separator not found. Run setup first:\n"
        '  powershell -ExecutionPolicy Bypass -File ".cursor/skills/vocal-separator/scripts/setup.ps1"'
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Separate vocals and instrumental stems.")
    parser.add_argument("input", type=Path, help="Input audio file")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory (default: <input_stem>_stems next to input)",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"UVR model filename (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--chunk-duration",
        type=int,
        default=0,
        help="Chunk duration in seconds for long files (0 = disabled)",
    )
    parser.add_argument(
        "--device",
        choices=["auto", "cpu", "cuda"],
        default="auto",
        help="Inference device",
    )
    args = parser.parse_args()

    input_path = args.input.expanduser().resolve()
    if not input_path.is_file():
        raise SystemExit(f"Input file not found: {input_path}")

    output_dir = args.output_dir
    if output_dir is None:
        output_dir = input_path.parent / f"{input_path.stem}_stems"
    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        str(resolve_audio_separator()),
        str(input_path),
        "--model_filename",
        args.model,
        "--model_file_dir",
        str(MODELS_DIR),
        "--output_dir",
        str(output_dir),
    ]
    if args.chunk_duration > 0:
        cmd.extend(["--chunk_duration", str(args.chunk_duration)])
    if args.device == "cpu":
        cmd.extend(["--device", "cpu"])
    elif args.device == "cuda":
        cmd.extend(["--device", "cuda"])

    print("Running:", " ".join(f'"{part}"' if " " in part else part for part in cmd))
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        raise SystemExit(result.returncode)

    stems = sorted(output_dir.glob(f"{input_path.stem}*"))
    if not stems:
        stems = sorted(output_dir.glob("*"))

    print(
        json.dumps(
            {
                "input": str(input_path),
                "output_dir": str(output_dir),
                "model": args.model,
                "stems": [str(p) for p in stems],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
