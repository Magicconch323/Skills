# Skills 索引

> 唯一实体位置：`.cursor/skills/<skill-name>/SKILL.md`（独立仓库 Magicconch323/Skills）。文件夹名 = SKILL.md 里的 `name`。
> 维护：资料管家 Bot。最后更新：2026-10-15。共 34 个。

| 来源 | Skill | 用途 | 路径 |
|---|---|---|---|
| 自写 | **auto-iterate** | 同一交付物改满三轮时用三问收敛方向；同一问题改三次不好则转根因讨论 | `.cursor/skills/auto-iterate/SKILL.md` |
| 自写 | **plan-mentor-maverick** | 激进派年度计划导师：维护 年度计划/年度计划.md，以赚钱为北极星做取舍 | `.cursor/skills/plan-mentor-maverick/SKILL.md` |
| 自写 | **task-breakdown-secretary** | 任务拆解秘书：把年度计划拆成每周/每日动作，内置《高性价比人生指南》决策查询 | `.cursor/skills/task-breakdown-secretary/SKILL.md` |
| 自写 | **dispute-reply-ghostwriter** | 纠纷回复代笔：以本人口吻起草克制、守边界的对外纠纷回复 | `.cursor/skills/dispute-reply-ghostwriter/SKILL.md` |
| 自写 | **renovation-knowledge-index** | 装修问答：查 知识库/装修资料 并联网核实（触发词「执行装修skill」） | `.cursor/skills/renovation-knowledge-index/SKILL.md` |
| 自写 | **lyrics-author** | 中文作词：从 知识库/歌词 语料学习个人风格，动笔前先问 5–10 个问题 | `.cursor/skills/lyrics-author/SKILL.md` |
| 自写 | **chord-sheet** | 和弦谱：产出 A4 单页 .docx 和弦谱，存 Project/和弦谱/ | `.cursor/skills/chord-sheet/SKILL.md` |
| 自写 | **suno-prompt** | Suno v6 提示词包：Style / Exclude / Controls / 歌词骨架 + 校验脚本 | `.cursor/skills/suno-prompt/SKILL.md` |
| 自写 | **vocal-separator** | 人声/伴奏分离（audio-separator + UVR 模型）；.venv 为联接，实体在 skills/my skill/vocal-separator/.venv | `.cursor/skills/vocal-separator/SKILL.md` |
| 自写 | **web-design-workflow** | 「现在开始网页设计」总工作流：选栈、加载其他前端 skill、反 AI 模板审美 | `.cursor/skills/web-design-workflow/SKILL.md` |
| 自写 | **web-self-check** | 网页交付前 Playwright 截图 + 交互验收，不合格自动再改 | `.cursor/skills/web-self-check/SKILL.md` |
| 本地封装 | **animejs** | 使用本地 Anime.js v4（skills/网页设计/libs/animejs）做轻量动效 | `.cursor/skills/animejs/SKILL.md` |
| 本地封装 | **gsap** | 使用本地 GSAP 3（skills/网页设计/libs/gsap）做滚动/时间轴动效 | `.cursor/skills/gsap/SKILL.md` |
| 本地封装 | **react-bits** | 使用本地 React Bits 组件做 React 动效 | `.cursor/skills/react-bits/SKILL.md` |
| 本地封装 | **awesome-claude-design** | 68 个品牌 DESIGN.md 索引（skills/网页设计/upstream/awesome-claude-design） | `.cursor/skills/awesome-claude-design/SKILL.md` |
| 第三方 | **impeccable** | 前端设计语言：设计/改版/审查/打磨 UI（上游全量归档于 skills/_archive/impeccable-upstream） | `.cursor/skills/impeccable/SKILL.md` |
| 第三方 | **ui-ux-pro-max** | UI/UX 检索：风格、配色、字体、UX 指南，含 scripts/search.py 与 data/ | `.cursor/skills/ui-ux-pro-max/SKILL.md` |
| Anthropic 官方 | **algorithmic-art** | p5.js 生成艺术 | `.cursor/skills/algorithmic-art/SKILL.md` |
| Anthropic 官方 | **brand-guidelines** | Anthropic 品牌色与字体 | `.cursor/skills/brand-guidelines/SKILL.md` |
| Anthropic 官方 | **canvas-design** | 静态视觉设计（PNG/PDF） | `.cursor/skills/canvas-design/SKILL.md` |
| Anthropic 官方 | **claude-api** | Claude API / SDK 开发 | `.cursor/skills/claude-api/SKILL.md` |
| Anthropic 官方 | **doc-coauthoring** | 结构化协作写文档 | `.cursor/skills/doc-coauthoring/SKILL.md` |
| Anthropic 官方 | **docx** | 读写 Word 文档 | `.cursor/skills/docx/SKILL.md` |
| Anthropic 官方 | **frontend-design** | 高辨识度前端界面 | `.cursor/skills/frontend-design/SKILL.md` |
| Anthropic 官方 | **internal-comms** | 内部沟通文案 | `.cursor/skills/internal-comms/SKILL.md` |
| Anthropic 官方 | **mcp-builder** | 构建 MCP 服务器 | `.cursor/skills/mcp-builder/SKILL.md` |
| Anthropic 官方 | **pdf** | 读写处理 PDF | `.cursor/skills/pdf/SKILL.md` |
| Anthropic 官方 | **pptx** | 读写 PPT | `.cursor/skills/pptx/SKILL.md` |
| Anthropic 官方 | **skill-creator** | 创建/改进/评测 skill | `.cursor/skills/skill-creator/SKILL.md` |
| Anthropic 官方 | **slack-gif-creator** | 制作 Slack 动图 | `.cursor/skills/slack-gif-creator/SKILL.md` |
| Anthropic 官方 | **theme-factory** | 给产物套主题 | `.cursor/skills/theme-factory/SKILL.md` |
| Anthropic 官方 | **web-artifacts-builder** | React + shadcn 复杂 HTML 产物 | `.cursor/skills/web-artifacts-builder/SKILL.md` |
| Anthropic 官方 | **webapp-testing** | Playwright 测试本地网页 | `.cursor/skills/webapp-testing/SKILL.md` |
| Anthropic 官方 | **xlsx** | 读写电子表格 | `.cursor/skills/xlsx/SKILL.md` |

## 功能重叠（已保留，按场景选用）

- 网页：`web-design-workflow` 是入口，按需调用 `frontend-design` / `impeccable` / `ui-ux-pro-max` / `animejs` / `gsap` / `react-bits`；交付前 `web-self-check`（依赖 `webapp-testing`）。
- 年度计划：`plan-mentor-maverick` 定方向，`task-breakdown-secretary` 拆执行。
- 音乐：`lyrics-author` 写词 → `chord-sheet` 出谱 → `suno-prompt` 生成 → `vocal-separator` 拆轨。

## 已归档 / 已移除（2026-10-15 整理）

| 项目 | 去向 |
|---|---|
| `skills/skills-main/`（Anthropic 官方仓库副本，与本目录重复） | `skills/_archive/anthropic-skills-main/` |
| `skills/网页设计/upstream/impeccable/`（多平台上游全量） | `skills/_archive/impeccable-upstream/` |
| `skills/网页设计/upstream/ui-ux-pro-max-skill/` | `skills/_archive/ui-ux-pro-max-upstream/` |
| `skills/网页设计/tools/ui-ux-pro-max/`（2026-06 旧副本，styles.csv 较旧） | `skills/_archive/ui-ux-pro-max-tools-copy-20260607/` |
| `skills/tools/`（只有 __pycache__） | `skills/_archive/tools-pycache-only/` |
| `skills/my skill/*` | 实体移入 `.cursor/skills/`；仅留 `vocal-separator/.venv`（运行环境） |
| 39 个指向 `E:\coding\.agents\skills\*` 的失效联接（Matt Pocock 系列：tdd、grill-me、handoff 等）以及 1 个指向 `E:\skills\...` 的失效联接 | 已删除联接本身（目标早已不存在，无内容丢失） |