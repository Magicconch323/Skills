#!/usr/bin/env bash
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV_PATH="$SKILL_ROOT/.venv"

pick_python() {
  for candidate in python3.12 python3.11 python3.10 python3; do
    if command -v "$candidate" >/dev/null 2>&1; then
      echo "$candidate"
      return 0
    fi
  done
  echo "Python 3.10+ not found." >&2
  exit 1
}

PYTHON="$(pick_python)"
echo "Using Python: $PYTHON"

if [[ ! -d "$VENV_PATH" ]]; then
  "$PYTHON" -m venv "$VENV_PATH"
fi

# shellcheck disable=SC1091
source "$VENV_PATH/bin/activate"
pip install --upgrade pip
pip install "audio-separator[gpu]"
pip install --force-reinstall torch torchvision --index-url https://download.pytorch.org/whl/cu128

echo ""
echo "Verifying installation..."
audio-separator --env_info

echo ""
echo "Setup complete. Venv: $VENV_PATH"
