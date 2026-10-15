---
name: chord-sheet
description: >-
  把一首歌做成「固定分区、可打印」的和弦谱 Word 文档（A4 单页）。用户给一首已发行歌曲，或给一段配文字说明的原创歌词，
  就产出：调式 / 速度 / 拍号、调内 1–7 级和弦对照（含组成音）+ 本曲拓展和弦、以及按段落（前奏/主歌/副歌/桥段/间奏/尾奏）
  排列的和弦谱，和弦压在歌词上、无歌词段落写和弦走向。信息必须有可靠来源、禁止瞎编。触发词：只要用户说
  「做和弦谱」「扒和弦」「这首歌的和弦」「和弦走向」「出个谱」「和弦谱」，或给出歌名/歌词要和弦，或提到
  Project/和弦谱，就使用本 skill。输出为 .docx，存到 e:/coding/Project/和弦谱/。
---

# 和弦谱生成 Chord Sheet

把一首歌变成一张 **A4 单页、可打印** 的和弦谱 Word 文档。版式由 `chord_sheet.py` 固定，你只负责把内容整理成 `Song` 数据结构，再调用 `render()`。**换歌只换内容，不用重新调版式。**

## 核心原则（不可违背）

1. **来源准确、禁止瞎编。** 每个关键字段（调式、BPM、拍号、段落和弦、歌词对齐）都要有依据。
   - **已发行歌曲**：以可靠来源为准（Hooktheory、Ultimate Guitar 高评分谱、GetSongBPM、官方乐谱等）。多来源交叉验证；来源冲突就**列出差异、停下来问用户**，不要自行合并。
   - **用户原创歌**：以用户提供的歌词 / 结构 / 和弦为准，用户就是来源，不存在冲突。用户只给歌词+说明、要你配和弦时，可以推断，但要标明「这是我推断的，供参考」。
   - **找不到可靠来源**：不要编。**停下来告诉用户**「没找到可靠来源」，问他是否：提供来源 / 接受推断版（标注低置信度）/ 换歌。
2. **来源与不确定性只在对话里说明，绝不写进 .docx。** 谱面是干净的成品。
3. **单页是最高优先级。** 所有内容必须挤进一页。装不下就调 `density`（见下），不能续页。
4. **原调优先。** 默认输出录音原调，不换算成 C。用户明确要求换调时，整体移调并**保留段落结构与重复关系不变**。
5. **不确定就停下来问用户**，别猜着往下做。

## 输出格式（固定三区 + 正文双栏）

由 `chord_sheet.py` 保证，不要手改版式：

- **头信息行**：左＝`艺人 — 歌名`，右＝`原调 X  ·  BPM  ·  拍号`（左右排列省纵向空间）。
- **调内和弦对照**：`和弦 · <调>` 区列 1–7 级（级数 + 和弦 + 组成音，自动分左右两小列）；`拓展和弦` 区列本曲用到的 sus/add/slash 等扩展和弦（只列名，不配音）。
- **正文双栏**：按段落排列。段落标题中英并列（`主歌 Verse 1`、`副歌 Chorus`、`前奏 Intro`、`间奏 Interlude`、`桥段 Bridge`、`尾奏 Outro`…），覆盖完整曲式。
  - **栏序（强制）**：左→右、上→下——**先灌满左栏，再从右栏顶继续**。由 `chord_sheet.py` 的 `noBalancedColumns` 保证；**不要**用 `column_break_before` 去「左右拉齐」。
  - **和弦行按小节写**（2026-09-29 用户验收）：用 `bars("E F#", "B")` 生成 `| E   F#  | B       |`，一格一小节、格内多个和弦均分小节（两个 = 各半小节）、`-` 表示空/延音小节。**不再**按歌词音节用空格对位。每行 ≤ 4 个单和弦小节或 ≤ 2 个双和弦小节（栏宽约 9.1cm）。
  - 有歌词：和弦行（近黑加粗 Courier，**大于歌词**）压在歌词行上，`keep_with_next` 保证不与歌词分栏。
  - 无歌词（前奏/间奏/部分尾奏）：只写和弦行。
  - **段名 > 歌词字号**（`Style.heading`），段落之间留明显空白（`section_before`）。
  - 缺调式 / BPM / 和弦：对应位置留空，仍输出完整版式（头信息、对照区、段落）。
  - **重复段落**：`Section(title="主歌 Verse 3", same_as="同主歌 Verse 1")` → 段名下一行加粗正文 `（同主歌 Verse 1）`，不再粘贴歌词/和弦；有额外小节再加 `lines`/`note`。
  - 其他短注：`note`，如 `末尾多两拍 A（2-beat break）` / `重复至结束`。
  - 变体（尾句、最后一段副歌等）：单独开一段或在标题注明。

## 工作流程

1. **确认输入类型**：已发行歌 or 用户原创。
2. **取数据**：
   - 已发行：联网查调式 / BPM / 拍号 / 段落和弦 / 歌词，交叉验证，记下来源（供对话汇报）。
   - 原创：用用户给的歌词与说明，缺和弦就推断并标注。
3. **整理成 `Song` 结构**（见 `examples/fake_plastic_trees.py`）：`title`、`meta`、`key_label`、`degrees`(1–7)、`extensions`、`sections`（每段 `title` / `lines`(Line(chord, lyric)) / `note`）。正文栏序由模板自动处理，一般不要设 `column_break_before`。
4. **调用 render** 生成到 `e:/coding/Project/和弦谱/<英文短横线歌名>.docx`：

```python
import sys; sys.path.insert(0, r"e:/coding/.cursor/skills/chord-sheet")
from chord_sheet import Song, Section, Line, bars, render
render(SONG, r"e:/coding/Project/和弦谱/song-title.docx", density="normal")
```

5. **控单页**：先 `density="normal"`；若溢出依次改 `"compact"` → `"tight"` → `"dense"`。重复段一律先用 `same_as` 折叠——**不要**用换栏去左右拉齐。版式以黑白打印可读为先：歌词字号偏大、和弦近黑加粗且大于歌词、段名大于歌词；塞进一页靠 density，不要为单页把和弦改回品红细字。
   - 页数以 Word 实测为准（COM `ComputeStatistics(2)`，见 `examples/` 说明）；python-docx 算不出分页。
6. **对话汇报**（不写进文件）：用了哪些来源、置信度、有无来源冲突或不确定点。

## 出去玩乐队成品（`Project/和弦谱/成品/`）

- 生成脚本：`examples/generate_outgoplay.py`（源＝`*_歌词.docx` + `和弦谱/*.docx` 的 Nashville 小节谱）。
- **用户手改过的成品永不覆盖**：脚本内 `HAND_EDITED = {"空凤梨罐头.docx", "不是眼泪.docx"}`，只同步 spec 备查。新增手改文件时先加进这个集合。
- 每首 density 已按 Word 实测单页逐首定好（见脚本 `SONGS`），改字号后要重新核对页数。

## 依赖

- `python-docx`（`pip install python-docx`）。
- 生成器：`chord_sheet.py`；参考实现：`examples/fake_plastic_trees.py`。
- 默认输出目录：`e:/coding/Project/和弦谱/`。

## 注意

- Word 打开着目标文件时无法覆盖：`render()` 会自动改存为 `<名>-new.docx` 并返回该路径；提醒用户关掉旧文件后重跑即可覆盖。
- `Line(chord=...)` 无 `lyric` = 纯和弦行；`Line(lyric=...)` 无 `chord` = 纯歌词行；两者都给 = 和弦压词。
