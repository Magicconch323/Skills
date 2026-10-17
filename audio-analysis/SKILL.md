---
name: audio-analysis
description: 音频节奏分析：输入一个音频文件，输出节拍网格（BPM、第一拍偏移、每一拍、每小节第一拍）、粗分起音列表（底鼓 / 军鼓和镲）、段落边界（对齐小节，名字由音频工程师标），格式为 JSON + CSV（另附 Audacity 标签文件），交给软件工程师做卡点、节奏游戏、动效同步。Use when 用户或其他 Bot 要「找鼓点 / 节拍 / BPM / 小节 / 段落位置」「给软件工程师打点」「卡点时间表」。不做人声分离、不做鼓分离（Demucs）、不改音频。10/23 用量重置前不运行。
---

# audio-analysis

> **10/23 用量重置前不运行**（主人规定：停写代码、不跑音频分析）。本 skill 只定流程和输出格式；工具安装和第一次运行等 10/23 后经主人同意再做。
> 归属：音频工程师。安装位置：`E:\coding` 下独立虚拟环境（venv），不要装进全局 Python。
> 不做 Demucs / 鼓分离；鼓点只做到粗分 kick / snare_hat。

## 1. 做到哪一档（2026-10-18 主人定）
| 要什么 | 做法 |
|---|---|
| 节拍网格 | BPM、第一拍相对文件开头的偏移、每一拍、每小节第一拍的时间戳（毫秒） |
| 粗分起音 | 底鼓（低频）/ 军鼓和镲（中高频）；不做完整鼓轨分离 |
| 段落 | 自动切边界并对齐到最近小节第一拍；段落名由音频工程师按听感与歌词标 |
| 交给软件工程师 | 毫秒时间戳的 JSON + CSV |

## 2. 用什么工具（10/23 后装进独立 venv）
| 要什么 | 工具 | 说明 |
|---|---|---|
| 节拍、每小节第一拍 | **beat_this**（JKU，MIT，`pip install beat-this`，需 PyTorch） | 命令行 `beat_this 输入文件` |
| BPM、速度曲线 | 由节拍间隔算 | BPM = 60 / 相邻节拍间隔的中位数；同时给逐拍速度曲线；第一拍偏移 = 第一个 downbeat 的 `time_ms` |
| 小节 | 由每小节第一拍切 | 第一拍到下一个第一拍 = 一小节；拍号按每小节拍数的众数判断（多为 4/4） |
| 鼓点（粗分） | **librosa**：HPSS 取打击乐 → `onset_detect` | `kick` / `snare_hat` / `unknown`；准确度中等 |
| 段落边界 | **librosa** `segment` → 对齐到最近小节第一拍 | 只有边界；名字 `label_source: manual` 由音频工程师填 |

不装 madmom、essentia、allin1（Windows 上装不上或要编译）。不用 Demucs。

## 3. 输入
- 首选 **WAV**（无编码延迟）；mp3 / m4a 由 ffmpeg 解码，结果里注明「mp3 解码，可能有几十毫秒以内的偏移」。
- 文件放在对应项目目录里，不放桌面。
- 开工前问清：用途（卡点 / 游戏判定 / 可视化）。

## 4. 输出（同一首歌一个文件夹：`<歌名>_analysis/`）
时间一律**从音频文件第 0 个采样点算起**；`time_s` 保留 3 位小数，`time_ms` 为整数毫秒（四舍五入）。

### 4.1 `analysis.json`（主文件）
```json
{
  "schema_version": "1.0",
  "source": { "file": "song.wav", "duration_s": 213.452, "sample_rate": 44100, "decoded_from_mp3": false },
  "tools": { "beats": "beat_this 1.1.0 (final0)", "onsets_sections": "librosa 1.0.0" },
  "tempo": { "bpm": 128.0, "time_signature": "4/4", "first_downbeat_offset_ms": 512, "stable": true,
             "curve": [ { "time_ms": 512, "bpm": 127.8 } ] },
  "beats": [ { "index": 1, "time_s": 0.512, "time_ms": 512, "bar": 1, "beat_in_bar": 1, "is_downbeat": true } ],
  "bars": [ { "bar": 1, "start_ms": 512, "end_ms": 2387 } ],
  "drum_hits": [ { "time_ms": 512, "type": "kick", "strength": 0.83 } ],
  "sections": [ { "label": "Intro", "label_source": "manual", "start_ms": 0, "end_ms": 15200, "start_bar": 1, "end_bar": 8 } ],
  "checks": { "beat_agreement_ms_p95": 18, "manual_spot_check": "8 bars ok", "notes": [] }
}
```
- `type`：`kick` / `snare_hat` / `unknown`。`strength`：0–1。
- `label_source`：`auto`（只有边界）或 `manual`（音频工程师标过名）。
- `first_downbeat_offset_ms`：第一拍相对文件开头的偏移，节奏游戏对齐要用。

### 4.2 CSV
- `beats.csv`：`index,time_s,time_ms,bar,beat_in_bar,is_downbeat`
- `drum_hits.csv`：`time_s,time_ms,type,strength`
- `sections.csv`：`label,start_s,start_ms,end_s,end_ms,start_bar,end_bar`

### 4.3 `audacity_labels.txt`
Audacity 标签格式；节拍写 `B1.1`，段落写名字。

## 5. 软件工程师怎么用（节奏游戏对齐）
运行时用**音频时钟**，不要用游戏帧时钟：
- Unity：`AudioSettings.dspTime`（见 Unity Manual「Audio Settings」/ dspTime 相关说明）
- Godot：播放位置 + 上次混音到现在的时间 − 输出延迟
- Android Oboe：在音频回调里更新「现在播到哪一秒」（Google Oboe RhythmGame 示例）
- 谱的格式可参考 osu 的 timing points（BPM、第一拍偏移、拍号）

做法：
1. 读 `analysis.json`，按 `beats` / `drum_hits` 的 `time_ms` 排好的数组做时间表。
2. 播放时用音频时钟换算成毫秒，用指针往后走，到点触发。
3. 对齐公式：`now_ms ≈ audio_clock_ms`；判定时加上 `first_downbeat_offset_ms` 理解小节网格，再留一个可调的 **`offset_ms`（总偏移，设备/耳机延迟）**，默认 0。
4. 速度不稳（`tempo.stable = false`）不要用固定 BPM 推算，直接用 `beats` 数组。
5. Web 端可用 `AudioContext.currentTime`（比 `<audio>.currentTime` 更准）。

## 6. 验证（交付前必须做）
1. beat_this 与 librosa 节拍互相对，95% 分位差值写进 `checks.beat_agreement_ms_p95`；超过 70 ms 列出来人工看。
2. BPM 和已知速度比；差一倍或一半要标出来。
3. `audacity_labels.txt` 叠波形，抽查开头、中段、结尾各 8 小节。
4. 段落边界必须落在小节第一拍上；标完名后 `label_source` 改 `manual`。

## 7. 边界
- 不做人声分离、不做鼓分离（Demucs）、不改原音频、不覆盖原文件。
- 10/23 前不安装、不运行。
- 结果写明工具版本与验证结果；验证没做完不交付。
