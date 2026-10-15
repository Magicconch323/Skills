---
name: react-bits
description: Animated React UI components via React Bits (text effects, backgrounds, interactive). TRIGGER for React animation components, react-bits, BlurText, split text, animated backgrounds, or landing-page motion in React/Next/Vite. Prefer CLI/npm — local skills/网页设计/libs/react-bits does NOT exist. For vanilla HTML use animejs skill instead.
---

# React Bits

[React Bits](https://github.com/DavidHDev/react-bits) — 110+ 动画 React 组件。官方站 [reactbits.dev](https://reactbits.dev)。

> **2026-10-15**：`skills/网页设计/libs/react-bits` **目录不存在**。不要写相对路径引用本地 react-bits。请用 CLI / npm。同目录仍有权威 `animejs`、`gsap`。

## 何时用 React Bits vs Anime.js

| 场景 | 库 |
|------|-----|
| 单 HTML、Vanilla、已有 rAF 物理页 | **Anime.js**（`skills/网页设计/libs/animejs`） |
| React / Next / Vite 组件、落地页炫字/背景 | **React Bits**（本 skill · CLI） |

## 安装到用户项目

### CLI（需联网，与官网一致）

```bash
npx shadcn@latest add @react-bits/BlurText-TS-TW
```

组件名与变体以 [reactbits.dev](https://reactbits.dev) 页面为准（`-TS-TW`、`-JS-CSS` 等）。

### npm

按官网说明安装 peer（常有 `motion` / `gsap` / `three`），再按组件文档引入。

## 与网页设计资源的关系

- 权威动效运行时：`skills/网页设计/libs/animejs`、`libs/gsap`（网页工程师）
- 本 skill **不**依赖本地 react-bits 副本
