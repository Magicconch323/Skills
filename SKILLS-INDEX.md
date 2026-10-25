# Skills 索引

> 唯一实体位置：`.cursor/skills/<skill-name>/SKILL.md`（独立仓库 Magicconch323/Skills）。文件夹名 = SKILL.md 里的 `name`。
> 维护：大管家 Bot。最后更新：2026-10-24（用户级：fortune/bazi/cyber-divination 待重审；人名 baby-name/chinese-naming 已归档；已删 namer/brand-naming/naming-assistant）。

| 来源 | Skill | 用途 | 路径 |
|---|---|---|---|
| 自写 | **auto-iterate** | 同一交付物改满三轮时用三问收敛方向；同一问题改三次不好则转根因讨论 | `.cursor/skills/auto-iterate/SKILL.md` |
| 自写 | **plan-mentor-maverick** | 激进派年度计划导师：维护 年度计划/年度计划.md，以赚钱为北极星做取舍 | `.cursor/skills/plan-mentor-maverick/SKILL.md` |
| 自写 | **task-breakdown-secretary** | 任务拆解秘书：把年度计划拆成每周/每日动作，内置《高性价比人生指南》决策查询 | `.cursor/skills/task-breakdown-secretary/SKILL.md` |
| 自写 | **dispute-reply-ghostwriter** | 纠纷回复代笔：以本人口吻起草克制、守边界的对外纠纷回复 | `.cursor/skills/dispute-reply-ghostwriter/SKILL.md` |
| 自写 | **renovation-knowledge-index** | 装修问答：查 知识库/装修资料 并联网核实（触发词「执行装修skill」）；2026-10-16 起归图书馆 | `.cursor/skills/renovation-knowledge-index/SKILL.md` |
| 自写 | **chord-sheet** | 和弦谱：产出 A4 单页 .docx 和弦谱，存 Project/和弦谱/ | `.cursor/skills/chord-sheet/SKILL.md` |
| 自写 | **suno-prompt** | Suno v6 提示词包：Style / Exclude / Controls / 歌词骨架 + 校验脚本（归提示词工程师） | `.cursor/skills/suno-prompt/SKILL.md` |
| 自写 | **midjourney-prompt** | Midjourney V8.2 提示词：固定结构、参数速查、中文转英文（归提示词工程师） | `.cursor/skills/midjourney-prompt/SKILL.md` |
| 自写 | **audio-analysis** | 音频节奏分析：beat_this + librosa → 节拍网格/粗分鼓点/段落 JSON + CSV（归音频工程师；10/23 前不运行） | `.cursor/skills/audio-analysis/SKILL.md` |
| 自写 | **web-design-workflow** | 「现在开始网页设计」总工作流：选栈、加载其他前端 skill、反 AI 模板审美 | `.cursor/skills/web-design-workflow/SKILL.md` |
| 自写 | **web-self-check** | 网页交付前 Playwright 截图 + 交互验收，不合格自动再改 | `.cursor/skills/web-self-check/SKILL.md` |
| 本地封装 | **animejs** | 使用本地 Anime.js v4（skills/网页设计/libs/animejs）做轻量动效 | `.cursor/skills/animejs/SKILL.md` |
| 本地封装 | **gsap** | 使用本地 GSAP 3（skills/网页设计/libs/gsap）做滚动/时间轴动效 | `.cursor/skills/gsap/SKILL.md` |
| 本地封装 | **react-bits** | 使用本地 React Bits 组件做 React 动效 | `.cursor/skills/react-bits/SKILL.md` |
| 本地封装 | **awesome-claude-design** | 68 个品牌 DESIGN.md 索引（skills/网页设计/upstream/awesome-claude-design） | `.cursor/skills/awesome-claude-design/SKILL.md` |
| Anthropic 官方 | **docx** | 读写 Word 文档 | `.cursor/skills/docx/SKILL.md` |
| Anthropic 官方 | **frontend-design** | 高辨识度前端界面 | `.cursor/skills/frontend-design/SKILL.md` |
| Anthropic 官方 | **pdf** | 读写处理 PDF | `.cursor/skills/pdf/SKILL.md` |
| Anthropic 官方 | **pptx** | 读写 PPT | `.cursor/skills/pptx/SKILL.md` |
| Anthropic 官方 | **skill-creator** | 创建/改进/评测 skill | `.cursor/skills/skill-creator/SKILL.md` |
| Anthropic 官方 | **webapp-testing** | Playwright 测试本地网页 | `.cursor/skills/webapp-testing/SKILL.md` |
| Anthropic 官方 | **xlsx** | 读写电子表格 | `.cursor/skills/xlsx/SKILL.md` |

## 功能重叠（已保留，按场景选用）

- 年度计划：`plan-mentor-maverick` 定方向，`task-breakdown-secretary` 拆执行。
- 图像：品牌顾问定方向 → `midjourney-prompt` 出提示词（提示词工程师）→ 主人在 Midjourney 生成。

## 已归档 / 已移除（2026-10-15 整理）

| 项目 | 去向 |
|---|---|
| `skills/my skill/` + `.cursor/skills/vocal-separator/` | **已删除**（2026-10-15；人声分离不再需要） |
| `skills/网页设计/libs/react-bits`、`tools/` | **从未落地 / 已不存在**；react-bits 用 npm/CLI，见该 skill |
| 失效联接（`.agents/skills` 等） | 已删联接 |

## 2026-10-16 专家 skill 扩充

| Bot | Skill | 说明 |
|---|---|---|
| 大师 | bazi-classics | 八字古籍体系：格局、用神、调候 |
| 大师 | ziwei-doushu | 紫微斗数：命盘结构与解读 |
| 大师 | yijing-study | 易经与占卜：卦象、爻辞、义理 |
| 大师 | western-astrology | 西洋占星与星座：星盘结构 |
| 网页工程师、软件工程师 | web-physics-realism | 自写：物理真实感总入口（大白话→参数、选型、默认配置、自检、参考图+截图选项卡流程）；references 含 majidmanzarpour 引擎选型文档（MIT） |

## 2026-10-16 图书馆新建 · 日常法律 skill

| Bot | Skill | 说明 |
|---|---|---|
| 图书馆 | renovation-knowledge-index | （自日常划入）装修资料检索 |

## 2026-10-22 登记 · 空窗期新装

| 来源 | Skill | 用途 | 路径 |
|---|---|---|---|

| 用户级 GitHub | **bazi** | jinchenma94/bazi-skill「赛博算命」：八字排盘 `pai_pan.py`（归大师） | `C:\Users\Administrator\.cursor\skills\bazi\` |
| 用户级 GitHub | **cyber-divination** | fysh1010/cyber-divination：小六壬/八字/婚姻/奇门综合占卜（归大师；排盘优先 bazi） | `C:\Users\Administrator\.cursor\skills\cyber-divination\` |
| 用户级 GitHub | **fortune** | ai-freer/fortune-skill：八字+紫微（归大师；排盘优先 bazi，紫微可用本 skill） | `C:\Users\Administrator\.cursor\skills\fortune\` |
| 用户级 GitHub | **chinese-naming** | **已撤销归档** Bots/_版本/已撤销-skill-20261024/chinese-naming/（主人 t537） |
| 用户级 GitHub | **baby-name** | **已撤销归档** Bots/_版本/已撤销-skill-20261024/baby-name/（主人 t537） |

