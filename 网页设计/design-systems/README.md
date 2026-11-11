# DESIGN.md 设计系统库

存放从 [awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) 索引的 **DESIGN.md** 文件。

## 说明

[awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) 仓库本身是**索引**（68 个品牌设计系统清单），`DESIGN.md` 文件需从 [getdesign.md](https://getdesign.md) 按需下载。

## 用法

1. 在 `upstream/awesome-claude-design/README.md` 里选品牌（如 Linear、Stripe、Notion）
2. 下载对应 `DESIGN.md` 放到本目录，例如 `design-systems/linear.DESIGN.md`
3. 做网页时告诉 Agent：「按 `design-systems/linear.DESIGN.md` 的风格实现」

也可用于 Claude Design 上传生成完整 design system package。

## 与 Impeccable 的关系

若项目有 `DESIGN.md`，Impeccable skill 的 `context.mjs` 会自动读取。
