# 网页设计 — 社区 Skill / Rule 索引

> 维护说明：复制 `.mdc` 到项目 `e:/coding/.cursor/rules/`；复制他人 `SKILL.md` 到 `e:/coding/.cursor/skills/<name>/` 或全局 `~/.cursor/skills/`。

## 一、Rule 合集（GitHub）

| 仓库 | 说明 | 链接 |
|------|------|------|
| **awesome-cursorrules** | 最大 Cursor rules 合集；含 shadcn、Tailwind、Next UI、Toss 风等 | https://github.com/PatrickJS/awesome-cursorrules |
| **cursor-designer** | 设计优先：UX/UI/IA/a11y，core + frontend + binders 分层 | https://github.com/spencergoldade/cursor-designer |
| **cursor-ai-tips** | .mdc 写法、Anti-Lazy、Composer 实践 | https://github.com/murataslan1/cursor-ai-tips |

### awesome-cursorrules 里和「网页视觉」强相关

| 文件 | 用途 |
|------|------|
| `rules/cursor-ai-react-typescript-shadcn-ui-cursorrules-p.mdc` | React + TS + shadcn |
| `rules/tailwind-shadcn-ui-integration-cursorrules-prompt-.mdc` | Tailwind + shadcn |
| `rules/react-nextjs-ui-development-cursorrules-prompt-fil.mdc` | Next UI |
| `rules/toss-style-design-system.mdc` | 克制产品 UI、灰阶层级、暗色 |
| `rules/typescript-nodejs-nextjs-react-ui-css-cursorrules-.mdc` | 全栈 TS UI |
| `rules/nextjs15-react19-vercelai-tailwind-cursorrules-prompt-file.mdc` | Next 15 栈 |
| `rules/html-tailwind-css-javascript-cursorrules-prompt-fi.mdc` | 静态 HTML 栈 |
| `rules/anti-sycophancy-code-discipline-cursorrules-prompt-file.mdc` | 减少幻觉/瞎编 API |

**安装示例**（PowerShell，在项目根）：

```powershell
New-Item -ItemType Directory -Force -Path .cursor/rules
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/toss-style-design-system.mdc" -OutFile ".cursor/rules/toss-style-design-system.mdc"
```

**cursor-designer 精简包**（推荐先拷 lean profile）：

```powershell
git clone --depth 1 https://github.com/spencergoldade/cursor-designer.git _tmp-cursor-designer
Copy-Item -Recurse _tmp-cursor-designer/.cursor/rules/core, _tmp-cursor-designer/.cursor/rules/frontend -Destination .cursor/rules/
```

Lean 含：`design-core`、`cursor-behavior-constraints`、`ui-layout-and-density`、`ux-forms-and-validation`、`accessibility-frontend`、`ux-flows-and-feedback`。

---

## 二、Agent Skills 合集

| 仓库 | 说明 | 链接 |
|------|------|------|
| **awesome-agent-skills** | 1000+ skills，多工具通用；可搜 frontend/figma | https://github.com/VoltAgent/awesome-agent-skills |
| **officialskills.sh** | 同上索引的 Web UI | https://officialskills.sh/ |

### 官方 / 高星（网页设计向）

| Skill | 来源 | 链接 |
|-------|------|------|
| frontend-design | Anthropic | https://officialskills.sh/anthropics/skills/frontend-design |
| web-artifacts-builder | Anthropic | https://officialskills.sh/anthropics/skills/web-artifacts-builder |
| canvas-design | Anthropic | https://officialskills.sh/anthropics/skills/canvas-design |
| web-design-guidelines | Vercel Labs | https://officialskills.sh/vercel-labs/skills/web-design-guidelines |
| design-md | Google Labs | https://officialskills.sh/google-labs-code/skills/design-md |
| enhance-prompt | Google Labs | https://officialskills.sh/google-labs-code/skills/enhance-prompt |
| shadcn-ui | Google Labs | https://officialskills.sh/google-labs-code/skills/shadcn-ui |
| react-components | Google Labs | https://officialskills.sh/google-labs-code/skills/react-components |
| frontend-design-review | Microsoft | https://officialskills.sh/microsoft/skills/frontend-design-review |
| frontend-ui-dark-ts | Microsoft | https://officialskills.sh/microsoft/skills/frontend-ui-dark-ts |
| frontend-skill | OpenAI | https://officialskills.sh/openai/skills/frontend-skill |
| figma-implement-design | Figma/OpenAI | https://officialskills.sh/figma/skills/figma-implement-design |
| plan-design-review | garrytan | https://officialskills.sh/garrytan/skills/plan-design-review |
| frontend-dev | MiniMax | https://officialskills.sh/MiniMax-AI/skills/frontend-dev |

---

## 三、社区单项 Skill（值得单独装）

| 项目 | 说明 | 链接 |
|------|------|------|
| **ui-design-brain** | 60+ 组件最佳实践/反模式，补 frontend-design 组件知识 | https://github.com/carmahhawwari/ui-design-brain |
| **cursor-designer** | 见上一节 rules，偏 UX 流程 | 同上 |

安装 ui-design-brain 典型路径：

```powershell
git clone https://github.com/carmahhawwari/ui-design-brain.git _tmp-uib
Copy-Item -Recurse _tmp-uib/skills/ui-design-brain e:/coding/.cursor/skills/ui-design-brain
```

（以该仓库 README 为准，目录名可能为 `ui-design-brain`。）

---

## 四、本机已有（`e:/coding`）

| 类型 | 路径 |
|------|------|
| 触发 rule | `.cursor/rules/web-design-start.mdc` |
| 本 workflow | `.cursor/skills/web-design-workflow/` |
| 视觉实现 | `.cursor/skills/frontend-design/` |
| UI/UX 检索 | `.cursor/skills/ui-ux-pro-max/` → `.cursor/skills/ui-ux-pro-max/` |
| 改版 / audit | `.cursor/skills/impeccable/` → `.cursor/skills/impeccable/`（上游 `_archive` 已删） |
| 品牌 DESIGN.md | `.cursor/skills/awesome-claude-design/` + `skills/网页设计/design-systems/` |
| 复杂 React 产物 | `.cursor/skills/web-artifacts-builder/` |
| 动效 | `.cursor/skills/animejs/`、`gsap/`、`react-bits/` |
| 主题 | `.cursor/skills/theme-factory/` |
| Figma MCP | Cursor 插件 + `figma-*` skills（插件缓存目录） |
| 本地资源 | `e:/coding/skills/网页设计/`（libs、tools、upstream、design-systems） |

> `.cursor/skills/` 是独立的 skills 仓库（在 Plan 的 `.gitignore` 里）；换新电脑若 skill 缺失，运行 `scripts/setup-cursor-skills.ps1` 拉取。

---

## 五、推荐组合

| 场景 | Rule（可选） | Skill |
|------|----------------|-------|
| 个人落地页 | toss-style 或仅 start rule | frontend-design |
| 产品后台 | cursor-designer lean + toss-style | frontend-design + webapp-testing |
| React 营销页 | shadcn mdc from awesome-cursorrules | frontend-design + react-bits |
| 设计稿还原 | — | figma-implement-design + frontend-design |
| 静态单页动效（轻量） | — | frontend-design + animejs |
| 静态单页动效（滚动/时间轴） | — | frontend-design + gsap |
| 选配色 / UX 规范 | — | ui-ux-pro-max + frontend-design |
| 像 Linear / Stripe 风格 | — | awesome-claude-design + DESIGN.md |
| 改版 / 打磨现有 UI | — | impeccable + frontend-design |

---

## 六、Cursor 文档

- Agent Skills：https://cursor.com/blog/agent-best-practices
- 项目 Rules：`.cursor/rules/*.mdc`（`description` + `globs` + `alwaysApply`）

触发词：**现在开始网页设计**

