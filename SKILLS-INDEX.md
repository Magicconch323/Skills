# Skills 索引

> 唯一实体位置：`.cursor/skills/<skill-name>/SKILL.md`（独立仓库 Magicconch323/Skills）。文件夹名 = SKILL.md 里的 `name`。
> 维护：大管家 Bot。最后更新：2026-10-15。共 33 个。

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
| 自写 | **web-design-workflow** | 「现在开始网页设计」总工作流：选栈、加载其他前端 skill、反 AI 模板审美 | `.cursor/skills/web-design-workflow/SKILL.md` |
| 自写 | **web-self-check** | 网页交付前 Playwright 截图 + 交互验收，不合格自动再改 | `.cursor/skills/web-self-check/SKILL.md` |
| 本地封装 | **animejs** | 使用本地 Anime.js v4（skills/网页设计/libs/animejs）做轻量动效 | `.cursor/skills/animejs/SKILL.md` |
| 本地封装 | **gsap** | 使用本地 GSAP 3（skills/网页设计/libs/gsap）做滚动/时间轴动效 | `.cursor/skills/gsap/SKILL.md` |
| 本地封装 | **react-bits** | 使用本地 React Bits 组件做 React 动效 | `.cursor/skills/react-bits/SKILL.md` |
| 本地封装 | **awesome-claude-design** | 68 个品牌 DESIGN.md 索引（skills/网页设计/upstream/awesome-claude-design） | `.cursor/skills/awesome-claude-design/SKILL.md` |
| 第三方 | **impeccable** | 前端设计语言：设计/改版/审查/打磨 UI（上游全量原归档 skills/_archive 已删除；当前用 `.cursor/skills/impeccable/`） | `.cursor/skills/impeccable/SKILL.md` |
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
- 音乐：`lyrics-author` 写词 → `chord-sheet` 出谱 → `suno-prompt` 生成。

## 已归档 / 已移除（2026-10-15 整理）

| 项目 | 去向 |
|---|---|
| `skills/_archive/`（含 anthropic / impeccable / ui-ux 上游副本） | **已删除**（2026-10-15）；运行时以 `.cursor/skills/` 为准 |
| `skills/my skill/` + `.cursor/skills/vocal-separator/` | **已删除**（2026-10-15；人声分离不再需要） |
| `skills/网页设计/libs/react-bits`、`tools/` | **从未落地 / 已不存在**；react-bits 用 npm/CLI，见该 skill |
| 失效联接（`.agents/skills` 等） | 已删联接 |

## 2026-10-16 专家 skill 扩充

| Bot | Skill | 说明 |
|---|---|---|
| 品牌资产 | graphic-design-foundations | 平面设计基础：网格、版式、字体、色彩、层级 |
| 品牌资产 | spatial-aesthetics | 室内设计与空间美学：尺度、光、材质、动线 |
| 品牌资产 | visual-style-atlas | 审美与风格流派图谱：识别特征与适用场景 |
| 品牌资产 | aesthetic-profile | 主人个人审美档案的建立与维护 |
| 品牌资产 | brand-building-logic | 成功品牌的要素与底层逻辑 |
| 品牌资产 | brand-strategy-market-sense | 广告与战略基础、市场商业感、跟进时事 |
| 内容运营 | copywriting-craft | 文案写作功底：标题、钩子、结构、改稿 |
| 内容运营 | consumer-psychology | 人性与说服心理：真诚前提下的影响力 |
| 内容运营 | platform-content-ops | 平台内容运营：小红书/B站/抖音的选题、节奏与复盘 |
| 内容运营 | short-video-scripting | 短视频与长视频脚本：钩子、节奏、分镜 |
| 外贸管理 | b2b-cold-email | 外贸开发信与客户开发流程 |
| 外贸管理 | incoterms-trade-docs | 贸易术语、单证与收款 |
| 外贸管理 | negotiation-business-english | 商务英语与谈判 |
| 外贸管理 | steel-market-intel | 钢材外贸市场与贸易政策情报 |
| 大师 | bazi-classics | 八字古籍体系：格局、用神、调候 |
| 大师 | ziwei-doushu | 紫微斗数：命盘结构与解读 |
| 大师 | yijing-study | 易经与占卜：卦象、爻辞、义理 |
| 大师 | western-astrology | 西洋占星与星座：星盘结构 |
| 小秘书 | time-management-systems | 时间管理体系：GTD、时间块、深度工作 |
| 小秘书 | goal-systems-habits | 目标与习惯：OKR、习惯系统 |
| 小秘书 | decision-retrospective | 决策与复盘：概率思维、事前验尸 |
| 日常 | objective-qa-method | 客观问答方法：先查再答、给证据 |
| 日常 | source-evaluation | 信息源评估与辟谣 |
| 日常 | practical-life-knowledge | 生活实用常识：消费维权、合同、安全 |
| 灵感伙伴 | story-structure | 故事结构：冲突、人物弧、节拍 |
| 灵感伙伴 | worldbuilding | 世界观构建：规则、历史、细节 |
| 灵感伙伴 | chinese-poetics | 中文诗学与修辞：意境、炼字 |
| 灵感伙伴 | creative-ideation | 发散方法：联想、组合、约束 |
| 网络工程师 | networking-fundamentals | 网络基础：分层、TCP/IP、DNS、路由 |
| 网络工程师 | proxy-protocols | 代理协议与客户端：Clash/mihomo、TLS 伪装 |
| 网络工程师 | server-hardening | 服务器安全加固与运维 |
| 网页工程师 | ux-usability-heuristics | 可用性原则：好不好用 |
| 网页工程师 | web-performance-feel | 性能与手感：不卡顿 |
| 网页工程师 | web-accessibility | 无障碍与语义：WCAG |
| 软件工程师 | software-design-principles | 软件设计：降低复杂度 |
| 软件工程师 | game-design | 游戏设计：核心循环与数值 |
| 软件工程师 | wechat-miniprogram | 微信小程序开发规范 |
| 软件工程师 | debugging-method | 调试方法论 |
