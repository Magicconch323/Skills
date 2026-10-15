---
name: gsap
description: >-
  Use the local GSAP 3 copy at e:/coding/skills/网页设计/libs/gsap for scroll-driven
  animation, timelines, draggable UI, FLIP, SplitText, and complex web motion.
  TRIGGER when the user asks for GSAP, ScrollTrigger, scroll animation, timeline
  sequencing, Draggable, or mentions greensock. Prefer over hand-written rAF for
  multi-step motion. For lighter vanilla tweening without scroll plugins, animejs
  skill may suffice.
---

# GSAP（本地）

合集目录：`e:/coding/skills/网页设计/libs/`（与 animejs、react-bits 同目录）。

上游：[greensock/GSAP](https://github.com/greensock/GSAP) · 文档 [gsap.com](https://gsap.com) · 当前版本见 `libs/gsap/VERSION.txt`。

## 本地路径（唯一权威来源）

| 用途 | 路径 |
|------|------|
| **运行时 UMD 核心** | `e:/coding/skills/网页设计/libs/gsap/dist/gsap.min.js` |
| **全插件 UMD 包** | `e:/coding/skills/网页设计/libs/gsap/dist/all.js` |
| **ESM 模块** | `e:/coding/skills/网页设计/libs/gsap/esm/index.js` |
| **按需 ESM 插件** | `e:/coding/skills/网页设计/libs/gsap/esm/ScrollTrigger.js` 等 |
| **TypeScript 类型** | `e:/coding/skills/网页设计/libs/gsap/types/` |
| **源码（仅供阅读）** | `e:/coding/skills/网页设计/libs/gsap/src/` |

## 引用规则

1. **静态 HTML（无打包）**：`<script src="../../../../skills/网页设计/libs/gsap/dist/gsap.min.js">`（相对路径按项目深度调整），插件另加对应 `.min.js`，然后 `gsap.registerPlugin(ScrollTrigger)`。
2. **ESM `<script type="module">`**：`import gsap from '../../../../skills/网页设计/libs/gsap/esm/index.js'`。
3. **Vite/Webpack/React**：配置 alias 指向 `skills/网页设计/libs/gsap/esm`，或 `npm install gsap`（本地副本优先于 CDN）。
4. **不要**默认 CDN，除非用户明确要求。
5. **插件必须 register**：`gsap.registerPlugin(ScrollTrigger, Draggable, …)`。
6. 与 anime.js 共存时：**同一元素不要双写 transform**。

## 最小模板（静态 HTML + ScrollTrigger）

```html
<script src="../../../../skills/网页设计/libs/gsap/dist/gsap.min.js"></script>
<script src="../../../../skills/网页设计/libs/gsap/dist/ScrollTrigger.min.js"></script>
<script>
  gsap.registerPlugin(ScrollTrigger);
  gsap.from('.hero', { opacity: 0, y: 40, duration: 1 });
</script>
```

## 最小模板（ESM）

```html
<script type="module">
  import gsap from '../../../../skills/网页设计/libs/gsap/esm/index.js';
  import ScrollTrigger from '../../../../skills/网页设计/libs/gsap/esm/ScrollTrigger.js';
  gsap.registerPlugin(ScrollTrigger);

  gsap.timeline()
    .from('.a', { opacity: 0, duration: 0.6 })
    .from('.b', { y: 30, duration: 0.5 }, '-=0.2');
</script>
```

## 常用 API

- **gsap.to / from / fromTo(targets, vars)**：补间；`duration`、`delay`、`ease`、`stagger`
- **gsap.timeline()**：序列；`.add()`、position 参数 `'<'` `'+=0.2'`
- **ScrollTrigger**：滚动驱动；`scrub`、`pin`、`start`/`end`
- **Draggable.create**：拖拽 + InertiaPlugin 惯性
- **Flip.from(state, {…})**：布局变化动画
- **SplitText**：文字拆分（需 `SplitText.min.js`）

## 与 web-design-workflow 的关系

说「现在开始网页设计」且需要**滚动叙事 / 复杂时间轴**时：加载本 skill + `frontend-design`；轻量入场用 `animejs`；React 组件动效用 `react-bits`。
