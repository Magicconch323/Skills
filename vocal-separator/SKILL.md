---
name: vocal-separator
description: >-
  Separates vocals and instrumental stems from audio using UVR-trained models via
  audio-separator CLI. Use when the user uploads or references mp3/wav/flac/m4a and asks to
  分离人声、提取伴奏、去人声、做伴奏、karaoke、stem separation、vocal remover、UVR, or needs
  isolated vocals/instrumental for remix, lyric writing, or live rehearsal.
---

# 人声 / 伴奏分离（UVR 模型）

用 [audio-separator](https://github.com/nomadkaraoke/python-audio-separator) 调用 **Ultimate Vocal Remover** 训练的模型，在命令行完成人声与伴奏分离。不启动 UVR GUI。

## 路径

| 位置 | 路径 |
|------|------|
| 维护源 | `e:/coding/.cursor/skills/vocal-separator` |
| Cursor 加载 | `e:/coding/.cursor/skills/vocal-separator` |
| 虚拟环境 | `e:/coding/.cursor/skills/vocal-separator/.venv` |
| 模型缓存 | `e:/coding/.cursor/skills/vocal-separator/models` |

## 首次使用：检查环境

工作目录 `e:/coding`。若 `.venv` 不存在或 `audio-separator` 不可用，先安装：

**Windows**

```powershell
powershell -ExecutionPolicy Bypass -File ".cursor/skills/vocal-separator/scripts/setup.ps1"
```

**Mac / Linux**

```bash
bash ".cursor/skills/vocal-separator/scripts/setup.sh"
```

安装后验证：

```powershell
& "e:/coding/.cursor/skills/vocal-separator/.venv/Scripts/audio-separator.exe" --env_info
```

应看到 `FFmpeg installed`；有 NVIDIA GPU 时还应看到 CUDA 加速可用。

## 标准工作流

用户给出音频文件后：

1. **确认输入**：接受 `mp3` / `wav` / `flac` / `m4a` / `ogg`；路径含空格用引号。
2. **确认输出目录**（可选）：默认与输入同目录下的 `<文件名>_stems/`。
3. **运行分离脚本**（不要手写一长串 CLI，统一走脚本）：

```powershell
python ".cursor/skills/vocal-separator/scripts/separate.py" "path/to/song.mp3"
```

可选参数：

```powershell
python ".cursor/skills/vocal-separator/scripts/separate.py" "song.mp3" --output-dir "path/to/out"
python ".cursor/skills/vocal-separator/scripts/separate.py" "song.mp3" --model model_bs_roformer_ep_317_sdr_12.9755.ckpt
python ".cursor/skills/vocal-separator/scripts/separate.py" "long.mp3" --chunk-duration 600
```

4. **汇报结果**：列出输出文件完整路径、所用模型、是否 GPU 加速。
5. **交付约定**：默认产出 **vocals** + **instrumental** 两个 stem；文件名带 `(Vocals)` / `(Instrumental)` 或模型对应后缀。

## 默认模型

| 场景 | 模型 |
|------|------|
| 默认（人声/伴奏，质量优先） | `model_bs_roformer_ep_317_sdr_12.9755.ckpt` |
| 用户要更快、可接受略差 | `UVR-MDX-NET-Inst_HQ_3.onnx` |
| 用户要鼓/贝斯/其他多轨 | `htdemucs_ft.yaml`（4 stem） |

换模型：`--model <filename>` 或 `audio-separator -l --list_filter=vocals --list_limit=5` 查表。

## 与 UVR GUI 的关系

- [UVR GUI](https://github.com/Anjok07/ultimatevocalremovergui) 适合手动试听、ensemble、去混响等高级操作。
- 本 Skill 面向 **自动化**：用户丢文件 → Agent 跑脚本 → 返回 stem 路径。
- 模型同源（UVR 训练权重）；无需把整个 UVR 仓库 clone 进工作区。

## 故障排除

| 现象 | 处理 |
|------|------|
| `FFmpeg` 未找到 | 确认 `ffmpeg` 在 PATH；Windows 可用 `winget install ffmpeg` |
| CUDA / ONNX 报错 | 重装 GPU 依赖：`setup.ps1`；或临时 `--device cpu`（慢） |
| 长音频 OOM | 加 `--chunk-duration 300` 或 `600` |
| Python 3.13 装不上 torch | 用 Python 3.10–3.12 建 venv：`py -3.11 -m venv .venv` 后重跑 setup |

## 示例对话

**用户**：帮我把这首歌分离出人声和伴奏  
**Agent**：确认 `song.mp3` 路径 → 跑 `separate.py` → 返回 `song_(Vocals).wav` 与 `song_(Instrumental).wav` 路径。

**用户**：只要伴奏，做卡拉 OK  
**Agent**：同样分离；交付 instrumental stem，并说明 vocals stem 也已生成可供校对。
