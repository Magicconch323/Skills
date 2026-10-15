---
name: web-design-workflow
description: >-
  用户说「现在开始网页设计」时执行完整网页/UI 设计工作流：选栈、加载 frontend-design 等 skill、
  应用反 AI 模板约束、Figma/动效分支、社区 rule 索引。网页设计、落地页、仪表盘、美化 UI、
  开始设计、web design workflow。
---

# 网页设计工作流

## 触发

用户消息包含：**现在开始网页设计** → 同时遵守 `e:/coding/Project/出去玩官网/.cursor/rules/web-design-start.mdc`。

## 流程（按序）

### 1. 澄清（缺则问，已有则跳过）

- 目标页面/组件、受众、参考（链接/截图/Figma）
- 栈：HTML 单文件 / Vite+React / Next / 现有项目路径
- 美学关键词一句（例：「纸质感编辑风」「深色仪表盘克制」）

### 2. 选 skill 组合

| 需求 | 必读 skill 路径 |
|------|-----------------|
| 高辨识度页面（默认） | `e:/coding/.cursor/skills/frontend-design/SKILL.md` |
| UI/UX 检索（配色/字体/UX 指南） | `e:/coding/.cursor/skills/ui-ux-pro-max/SKILL.md` |
| 改版 / audit / polish UI | `e:/coding/.cursor/skills/impeccable/SKILL.md` |
| 品牌 DESIGN.md 风格 | `e:/coding/.cursor/skills/awesome-claude-design/SKILL.md` |
| React+shadcn 多组件/状态 | `e:/coding/.cursor/skills/web-artifacts-builder/SKILL.md` |
| 纯 HTML/JS 动画（轻量） | `e:/coding/.cursor/skills/animejs/SKILL.md` |
| 纯 HTML/JS 动画（滚动/时间轴/Draggable） | `e:/coding/.cursor/skills/gsap/SKILL.md` |
| React 动效组件库 | `e:/coding/.cursor/skills/react-bits/SKILL.md` |
| 主题换肤 | `e:/coding/.cursor/skills/theme-factory/SKILL.md` |
| 静态海报 PNG/PDF | `e:/coding/.cursor/skills/canvas-design/SKILL.md` |
| 交互分析画布 | `C:/Users/Administrator/.cursor/skills-cursor/canvas/SKILL.md` |
| Figma 读/写 | `figma-use` + MCP `plugin-figma-figma` |
| 浏览器验收 | `e:/coding/.cursor/skills/webapp-testing/SKILL.md` |

### 3. 设计前（frontend-design 要点）

- 选定**单一**美术方向并写进回复首段（tone + 差异化一句）
- 字体：display + body 配对，避免 Inter/Space Grotesk 默认组合
- 色：主色 + 强调色 + CSS 变量；避免 Tailwind 默认 `blue-500` 墙
- 动效：优先高影响时刻（入场 stagger）；轻量用 animejs，滚动叙事/复杂序列用 gsap，React 用 react-bits

### 4. 实现

- 匹配项目已有目录与命名；最小 diff
- 表单/反馈参考 UX：标签、inline 错误、`role="alert"`
- 有设计稿则先 `get_design_context` 或用户截图再编码

### 5. 交付清单

- [ ] 可本地打开/运行的入口说明
- [ ] 美学方向一句话
- [ ] 主要文件列表
- [ ] 已知限制或未做范围（若有）

## 社区资源

完整链接与安装说明见 **[REFERENCES.md](./REFERENCES.md)**。

## 与专用 skill 的分工

| 本 workflow | 其他 skill |
|-------------|------------|
| 编排、选型、触发 | `frontend-design` 管审美细则 |
| 索引 GitHub 资源 | `ui-design-brain`（社区）管 60+ 组件模式 |
| 默认反模板 | `cursor-designer`（社区）管 UX/a11y 规则包 |
