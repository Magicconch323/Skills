# Anime.js 本地库

[Anime.js](https://github.com/juliangarnier/anime) v4 · 文档 [animejs.com](https://animejs.com)

根目录：`e:/coding/skills/网页设计/libs/animejs/`

| 路径 | 说明 |
|------|------|
| `dist/bundles/anime.esm.min.js` | ESM 单文件（静态 HTML 推荐） |
| `dist/bundles/anime.umd.min.js` | UMD 单文件 |
| `dist/modules/index.js` | 模块化入口 + 类型 |
| `examples/` | 官方示例（`npm run open:examples`） |
| `src/` | 源码 |

## 引用示例

```html
<script type="module">
  import { animate, stagger } from '../../../../skills/网页设计/libs/animejs/dist/bundles/anime.esm.min.js';
  animate('.item', { x: 120, opacity: [0, 1], delay: stagger(80) });
</script>
```

v3 → v4 迁移：<https://github.com/juliangarnier/anime/wiki/Migrating-from-v3-to-v4>
