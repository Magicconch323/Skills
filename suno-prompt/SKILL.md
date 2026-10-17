---
name: suno-prompt
description: Suno v6 提示词工程师（v6 / v6-wild / v6-mini）。把一首歌的想法（风格、情绪、和弦进行、参考曲、歌词）做成可直接粘贴进 Suno Custom Mode 的完整包：Style（按「制作指令」顺序写，≤1000 字符）+ Exclude Styles（2-3 项）+ Controls 建议（Variety 定 Exact style、Max Mode、Style Influence、Weirdness）+ 带段落 cue 的歌词骨架 + 一个 wild card 变体，并用 scripts/validate-prompt.py 检查触发词。Use when 用户提到 Suno、suno 提示词、style prompt、让 AI 生成一首歌、把和弦/歌词变成 Suno 可用格式、或说某次 Suno 生成「不对」要改提示词。
---

# Suno v6 提示词工程师

> 归属：提示词工程师（2026-10-18 自音频工程师移入）。只交付提示词，不调用 Suno 生成。

> 知识来源：[zarlor/suno-band-manager](https://github.com/zarlor/suno-band-manager)（MIT，见 `LICENSE-upstream`）的 `suno-style-prompt-builder` + `suno-lyric-transformer` + `SUNO-REFERENCE.md`，2026-10-08 拉取。本 SKILL.md 是去掉 BMad / uv / band-profile 依赖后的 Cursor 适配版；`references/` 原样保留。
> 平台状态：**v6 家族 2026-09-09 上线并退役所有旧模型**。references 里标 PREVIEW / COMMUNITY / ANECDOTAL 的条目是证据分级，不是定论；与 v6 测试冲突时以用户自己的生成结果为准。

## 什么时候读哪个文件

| 步骤 | 读 | 大小 |
|---|---|---|
| 每次构建前**必读** | `references/safety-tables.md`（触发词表、Exclude 规则、歌曲类型 → 滑杆表） | 14 KB |
| 写 Style | `references/model-prompt-strategies.md` → 「Suno v6 Family」（第 35–137 行）+ 「Genre Keyword Ordering」+ 「Exclude Styles Field」 | 按节读 |
| 写歌词 cue | `references/metatag-reference.md` → 「Suno v6 (PREVIEW)」（第 32–59 行）+ 「Section Structure Tags」+ 「Ending Control」 | 按节读 |
| 段落各干什么 | `references/section-jobs.md` | 7 KB |
| 判断提示词质量 | `references/prompt-quality-canon.md` | 8 KB |
| 平台功能 / 价格 / 字段上限 | `references/SUNO-REFERENCE.md`（2026-10-03 快照） | 按需 grep |
| 要查最新资料 | `references/research-sources.md` 列的来源；时效敏感的先核 suno.com/release-notes | — |

不要整篇读 100 KB 的文件；用 Grep 搜小节标题再 Read 对应行段。

## v6 的六个写法习惯（来自 model-prompt-strategies.md「Prompt style」）

1. **按顺序写**：Genre → Vocals → Drums → Guitars → Bass → 其他乐器 → Arrangement/Energy → Production → Ending。
2. **每件乐器每个段落都有任务，用动词**：「the intro riff continues under the verse vocal, palm-muted and lower, never stops」，不是「big riffs」。没写到的段落 = 模型会在那里抽掉乐器。
3. **放置人声而不是夸人声**：「vocal in front of the band, close-mic'd and dry, the loudest element; instruments sit behind and below」优于「crisp professional mix」。
4. **两头都写明长度**：「4-bar guitar intro, instrumental only」「ends on a hard stop after the final chorus」。没写的开头会变成哼唱 / ad-lib，没写的结尾会 vamp 或半句切断。
5. **只写正向；所有否定进 Exclude Styles**。行内「no reverb」会被读成「reverb」。
6. **一句制作短语有用，母带词没用**：「high-fidelity studio production, close-mic vocals, crisp transients, clear instrument separation」可以；「mastered, radio-ready, -14 LUFS」无效。

另外：前 ~200 字符是关键区（genre / mood / vocal 放这里）；v6 **从 Style 取情绪，不从歌词取**，情绪方向要写进 Style 和段落 cue；BPM 是软条件，数字必须配 feel 词（「72 BPM feel with a slow heavy backbeat」）；一首歌只有一个速度网格，段落对比用 half-time / double-time / sparse / dense 写。

## 触发词（safety-tables.md 的速查，构建前仍要读全表）

- **尖叫触发**：`metal` `sludge` `doom` `death` `thrash` `black` 作为流派词会拉出嘶吼，除非配正向人声指令（「raw melodic singing」）。要重但不要这个词：「heavy groove」。
- **键盘拉扯**：`baroque` `orchestral` `cinematic` `rock opera` 会把吉他挤成键盘 / 电影化编曲。
- **观众噪音**：`live` 词族（live recording / live-band drums / live energy）和 `crowd` `audience` `stadium` `festival` `anthemic` 会带入观众声。改说「unpolished room sound」「single-take band performance」。
- **重力词**：`heavy` `crushing` `massive` `epic` `cinematic` 全曲级使用会把人声压到乐队下面。把重量放在具体时刻上。
- **副歌别写「big / emotional / epic」**：rock 用户报告会被读成「放慢变戏剧化」，副歌变 ballad。写副歌的任务：「choruses stay rhythmically driving and hit harder than the verses」。
- `!` 把演唱推向喊叫；Style 里不放 `[段落标签]` 和 `*`。
- 必须保调时 Exclude 里加 `key change`（v6 会在第三段擅自转调，行内「no key changes」无效）。

## 工作流

### 第 1 步 · 收集

一次把能问的都问完：流派、情绪、人声方向、参考（「X meets Y」）、和弦进行 / 调性、速度感、语言（中文要写 `Mandarin vocals`，否则默认英文）、目标模型（默认 v6；Free 层 v6-mini；探索用 v6-wild）、层级（Free 没有 Exclude 和滑杆）、要不要纯器乐。用户已经给够就直接进第 2 步，只确认真正含糊的地方。

**参考艺人**：Suno 会剥掉艺人名。拆成具体声响描述；不确定该艺人的声音就先搜，拆错了用户不知道为什么不像。看 model-prompt-strategies.md「Reference Track Translation Guide」。

**用户带着生成结果回来说「不对」**：进「修正」而不是重建——先定位是 Variety 改写了提示词（成品页显示的 style 和输入不同）、还是 Style Influence 太松、还是触发词；一次只改一个变量。

**和弦进行**：Suno 不可靠地遵循和弦名。写法是「描述 + 名字」双保险：「canon-style descending bassline C–B–A–G–F–E–D–G under the verse」，同时在歌词段落 cue 里括号重复。把它当软条件。

### 第 2 步 · 写 Style + Exclude

- Style：v6 制作指令格式，≤1000 字符，关键区放 genre / mood / vocal。按上面六个习惯检查。用户给了中文歌词或中文语境时，Style 仍用英文写。
- Exclude Styles（Pro/Premier）：逗号分隔，**2-3 项**，< 200 字符；每项都要对应本提示词里确实可能漂过去的东西，并在 Style 里有正向配对。超过 3 项会让编曲不稳。Free 层没这个字段：把排除项改写成正向措辞塞回 Style。
- Voice / Persona / Custom Model 在用时：去掉性别、音色词（保留 delivery）；Persona 上的 Style 保持简单（1-2 流派、1 情绪、2-4 乐器）。
- 纯器乐：去掉人声指令，关键区写主奏乐器性格、互动、起落弧和空间。

### 第 3 步 · Controls

| 控件 | 建议 | 理由 |
|---|---|---|
| **Variety** | **Exact style（0）** | 高于 0 会在生成前**重写你的 Style**；成品页显示的是重写后的版本 |
| **Max Mode** | 打算保留的生成**开** | 2× 积分；生成后不能补 |
| **Style Influence** | 70–85（v6 默认 50，先检查） | 100 实测不比 85 好 |
| **Weirdness** | 按歌曲类型选（safety-tables 的表）；商业流派 20–30，实验 / 氛围更高 | 50 = 正常 |
| **Personalize** | 关 | 保持跨账号可复现 |
| **Duration** | Auto；生成拖尾太长时改 Custom = 演唱长度 + 15–20 s | Auto 对短歌词会补一分钟器乐尾 |
| **Vocal Gender** | 有 Voice 或纯器乐时留空 | — |

### 第 4 步 · 歌词骨架 / cue

- 每段开头一行 `[Section]`，后接短括号 cue，**措辞与 Style 里的句子一字不差**（模型读两次同一条指令）；两边矛盾时它用「抽薄乐队」解决。
- 不想要长 intro 哼唱：歌词第一行就是唱词，Style 里别出现光秃秃的 `vocal`。
- 结尾：`[Outro]` cue 写明「short instrumental outro, final hard stop」，最后一行 `[End]`，下面不留任何东西。
- 用户有自己的中文歌词时**不改词**，只加标签和 cue；写词交给 `lyrics-author` skill。
- 更多标签（`[Pre-Chorus]` `[Refrain]` `[Breakdown]` `[Instrumental]` 等）和 v6 专项见 metatag-reference.md。

### 第 5 步 · 校验 + 交付

把包写成 JSON 跑校验（纯 Python 即可，不需要 uv；PowerShell 下别用 echo 管道，用 Python 写临时文件或 subprocess）：

```python
import json, subprocess, sys
pkg = {"style_prompt": "...", "exclusion_prompt": "...", "model": "v6",
       "wild_card": {"style_prompt": "..."}}
r = subprocess.run([sys.executable, r"E:\coding\.cursor\skills\suno-prompt\scripts\validate-prompt.py", "--stdin"],
                   input=json.dumps(pkg), text=True, capture_output=True)
print(r.stdout)
```

它只**检测**（字符上限、关键区、段落标签、尖叫 / 键盘 / 观众 / 行内否定 / `!`、Exclude 长度与条数）；替换成什么词由你判断。有配对的尖叫触发仍会以 low 报出来。

**交付格式**（每块单独一个代码块，方便复制）：

```
## Style（N/1000 字符）
……

## Exclude Styles
……

## Controls
Model v6 · Variety Exact style · Max Mode on · Style Influence 80 · Weirdness 30 · Duration Auto · Vocal Gender —

## Lyrics / 结构（含 cue）
[Intro - ...]
……
[End]

## Wild card（实验版，一句话说变在哪）
……

## 下一轮怎么改
一次只动一个控件；两条生成都听完再判断（take 之间的差异常常大于改词的差异）。
```

**Wild card**：留在歌曲的核心流派里做一个子流派 / 年代 / 编曲翻转，保留主题、情绪弧和 hook；同一模型同一滑杆。不默认用 v6-wild——「原封不动的主提示词跑 v6-wild」是另一个可选的 wild card。

## 边界

- 不编造 Suno 功能或数值；references 里没有的说「没有资料」，时效敏感的提醒用户核 release notes。
- 不替用户写中文歌词正文（交 `lyrics-author`）；不做音频分析（上游的 librosa 工具链没有装）。
- 用户的听感判断高于任何 reference 条目。
