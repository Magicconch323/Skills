---
name: animejs
description: Use the local Anime.js v4 copy at e:/coding/skills/网页设计/libs/animejs for all frontend DOM/CSS/SVG/canvas animations. TRIGGER whenever the user asks for web animations, motion, easing, timelines, stagger, scroll-driven animation, draggable UI motion, or mentions anime.js/animejs — even if they only say "做个动画" or "加过渡". Prefer this library over hand-written requestAnimationFrame or raw CSS keyframes unless the effect is trivial (single hover opacity). For React component libraries use react-bits skill instead.
---

# Anime.js（本地）

合集目录：`e:/coding/skills/网页设计/libs/`（与 gsap、react-bits 同目录）。

## 本地路径（唯一权威来源）

| 用途 | 路径 |
|------|------|
| **运行时 ESM 打包** | `e:/coding/skills/网页设计/libs/animejs/dist/bundles/anime.esm.min.js` |
| **运行时 UMD** | `e:/coding/skills/网页设计/libs/animejs/dist/bundles/anime.umd.min.js` |
| **模块化 + 类型** | `e:/coding/skills/网页设计/libs/animejs/dist/modules/index.js` + `index.d.ts` |
| **官方 examples** | `e:/coding/skills/网页设计/libs/animejs/examples/` |
| **说明** | `e:/coding/skills/网页设计/libs/animejs/README-LOCAL.md` |

上游：[juliangarnier/anime](https://github.com/juliangarnier/anime) · 文档 [animejs.com](https://animejs.com) · 当前版本见 `animejs/VERSION.txt`（4.4.1）。

## 引用规则

1. **默认**：静态 HTML / 无打包 → `<script type="module">` + `import { animate, stagger } from '相对路径/skills/网页设计/libs/animejs/dist/bundles/anime.esm.min.js'`；或 UMD `<script src=".../anime.umd.min.js">`。
2. **Vite/Webpack**：`import { animate, createTimeline, stagger } from '…/skills/网页设计/libs/animejs/dist/modules/index.js'` 或配置 alias `@libs/animejs`。
3. **不要**默认用 CDN，除非用户明确要求。
4. **v4 API**：`animate(targets, params)`，不是 v3 的 `anime({ targets, … })`。
5. 复杂序列用 `createTimeline()`；多元素 delay 用 `stagger()`；需要抄写法时先读 `examples/` 里相近示例。

## 最小模板

```html
<script type="module">
  import { animate, stagger } from '../../../../skills/网页设计/libs/animejs/dist/bundles/anime.esm.min.js';

  animate('.item', {
    translateX: 80,
    opacity: [0, 1],
    duration: 600,
    delay: stagger(80),
    ease: 'outExpo',
  });
</script>
```

```js
import { animate, createTimeline, stagger } from 'e:/coding/skills/网页设计/libs/animejs/dist/modules/index.js';

const tl = createTimeline();
tl.add('.a', { x: 100, duration: 500 })
  .add('.b', { y: 40 }, '+=200')
  .init();
```

## 常用参数

- **targets**：选择器、Node、NodeList、对象（对象属性动画）
- **duration**（ms）、**delay**、**ease**（如 `inOutQuint`、`outExpo`、spring）
- **loop** / **alternate** / **autoplay**（默认 true）
- 属性：`x`/`y`/`translateX`、`rotate`、`scale`、`opacity`、CSS 变量；支持 `{ from, to }` 或数组 `[a, b]`
- **控制**：`anim.pause()` / `play()` / `restart()` / `revert()`；`anim.then()` / `finished`

## 子模块（按需 import）

```js
import { createDraggable } from '…/dist/modules/draggable/index.js';
import { createScope } from '…/dist/modules/scope/index.js';
import { onScroll } from '…/dist/modules/events/index.js';
import * as svg from '…/dist/modules/svg/index.js';
import * as text from '…/dist/modules/text/index.js';
```

## 与现有页面集成

- 已有 `requestAnimationFrame` 物理循环：用 anime 做 **一次性/补间/入场**，物理仍用 rAF；避免对同一 transform 双写。
- 拖拽逻辑若已用 pointer 事件，可选用 `createDraggable` 或仅对「松手回弹」用 `animate`。

## 迁移

v3 → v4：<https://github.com/juliangarnier/anime/wiki/Migrating-from-v3-to-v4>
