---
name: awesome-claude-design
description: >-
  Use the local index at e:/coding/skills/网页设计/upstream/awesome-claude-design
  for 68 brand DESIGN.md inspirations (Linear, Stripe, Notion, Vercel, etc.).
  TRIGGER when the user wants a specific brand aesthetic, design system scaffold,
  or mentions DESIGN.md / Claude Design / getdesign.md. Download DESIGN.md files
  into skills/网页设计/design-systems/ for reuse.
---

# Awesome Claude Design（本地索引）

上游：[VoltAgent/awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) · 本地索引 `skills/网页设计/upstream/awesome-claude-design/README.md`

## 是什么

68 个品牌的 **DESIGN.md** 灵感清单，每个文件描述：色彩、字体、组件、布局、Do/Don't 等 9 个章节，供 AI 直接生成一致 UI。

**仓库本身不含 DESIGN.md 文件**，只有 README 链接；文件从 [getdesign.md](https://getdesign.md) 下载。

## 本地路径

| 用途 | 路径 |
|------|------|
| 品牌索引 README | `e:/coding/skills/网页设计/upstream/awesome-claude-design/README.md` |
| 已下载 DESIGN.md | `e:/coding/skills/网页设计/design-systems/` |

## 工作流

1. 用户说目标风格（如「像 Linear 那样克制」）→ 读索引找最接近的品牌
2. 若 `design-systems/` 尚无该文件 → 提示用户从 getdesign.md 下载，或先用 README 里的描述作参考
3. 与 `impeccable` 或 `frontend-design` skill 组合实现代码

## 分类速览（索引内）

- AI 平台：Claude、Mistral、ElevenLabs…
- 开发者工具：Cursor、Vercel、Raycast…
- SaaS：Linear、Notion、Stripe…
- 消费科技：Apple、Spotify、Airbnb…

完整列表见上游 README。
