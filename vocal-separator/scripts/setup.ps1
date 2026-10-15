$ErrorActionPreference = "Stop"
$SkillRoot = Split-Path -Parent $PSScriptRoot
$VenvPath = Join-Path $SkillRoot ".venv"

function Find-Python {
    $listed = cmd /c "py -0p 2>nul"
    foreach ($version in @("3.12", "3.11", "3.10")) {
        if ($listed -match ":$version\s") {
            return @("py", "-$version")
        }
    }
    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) { return @("python") }
    throw "Python 3.10+ not found. Install Python 3.11 or 3.12 first."
}

$pythonCmd = Find-Python
Write-Host "Using Python command: $($pythonCmd -join ' ')"

if (-not (Test-Path $VenvPath)) {
    & $pythonCmd[0] $pythonCmd[1..($pythonCmd.Length - 1)] -m venv $VenvPath
}

$pip = Join-Path $VenvPath "Scripts\pip.exe"
$separator = Join-Path $VenvPath "Scripts\audio-separator.exe"

& $pip install --upgrade pip
& $pip install "audio-separator[gpu]"
# audio-separator may pull CPU-only torch; reinstall CUDA build when NVIDIA GPU present
& $pip install --force-reinstall torch torchvision --index-url https://download.pytorch.org/whl/cu128

Write-Host ""
Write-Host "Verifying installation..."
& $separator --env_info

Write-Host ""
Write-Host "Setup complete. Venv: $VenvPath"
