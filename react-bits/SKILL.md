---
name: react-bits
description: Use the local React Bits copy at e:/coding/skills/网页设计/libs/react-bits for animated React UI (text effects, backgrounds, interactive components). TRIGGER when the user asks for React animation components, react-bits, reactbits, BlurText, split text, animated backgrounds, shadcn animated components, or memorable landing-page motion in React/Next/Vite. Do NOT use for vanilla HTML-only pages — use animejs skill instead.
---

# React Bits（本地）

[React Bits](https://github.com/DavidHDev/react-bits) — 110+ 动画 React 组件。官方站 [reactbits.dev](https://reactbits.dev)。

合集目录：`e:/coding/skills/网页设计/libs/`（与 animejs、gsap 同目录，见 `libs/README.md`）。

## 本地路径

| 用途 | 路径 |
|------|------|
| **TS + Tailwind 源码（优先抄）** | `e:/coding/skills/网页设计/libs/react-bits/src/ts-tailwind/` |
| **TS + CSS** | `e:/coding/skills/网页设计/libs/react-bits/src/ts-default/` |
| **本地说明** | `e:/coding/skills/网页设计/libs/react-bits/README-LOCAL.md` |
| **上游 README** | `e:/coding/skills/网页设计/libs/react-bits/README.md` |

目录结构：`{Category}/{ComponentName}/`，例如 `TextAnimations/BlurText/BlurText.tsx`。

## 何时用 React Bits vs Anime.js

| 场景 | 库 |
|------|-----|
| 单 HTML、Vanilla、已有 rAF 物理页 | **Anime.js**（`skills/网页设计/libs/animejs`） |
| React / Next / Vite 组件、落地页炫字/背景 | **React Bits** |

## 安装到用户项目

### CLI（需联网，与官网一致）

```bash
npx shadcn@latest add @react-bits/BlurText-TS-TW
```

组件名与变体以 [reactbits.dev](https://reactbits.dev) 页面为准（`-TS-TW`、`-JS-CSS` 等）。

### 从本地复制

1. 在官网确认组件名与变体（如 `BlurText` + `TS-TW`）。
2. 打开 `src/ts-tailwind/TextAnimations/BlurText/`（路径随分类变化）。
3. 复制 `.tsx` 及页面列出的依赖；检查 `package.json` 中常见 peer：`motion`、`gsap`、`three` 等。
4. 按组件调整 Tailwind / CSS 变量。

## 本地预览全部组件

```powershell
cd e:\coding\skills\libs\react-bits
npm install
npm run dev
```

## 分类速查

- **TextAnimations** — 模糊/拆分/渐变/滚动揭示文字
- **Components** — 卡片、导航、Dock、画廊等 UI
- **Backgrounds** — 全屏动态背景
- **Animations** — 通用动效片段

## 创意工具（仅在线）

Background Studio、Shape Magic、Texture Lab： [reactbits.dev/tools](https://reactbits.dev/tools)

## 许可证

MIT + Commons Clause（见上游 `LICENSE.md`）。
