---
name: midjourney-prompt
description: Midjourney（默认 V8.2）提示词工程师。把中文的生图需求（用途、主体、风格、参考图、品牌规则）转成可直接粘贴进 Midjourney Imagine 栏的英文提示词和参数，并给一个变体和下一轮修改建议。Use when 用户或其他 Bot 提到 Midjourney、MJ、生图、出图、海报 / 封面 / 头像草图、视觉示意图、风格参考图，或说某次 MJ 出图「不对」要改提示词。只交付提示词，不调用任何生图工具。
---

# Midjourney 提示词（草稿，2026-10-18）

> 归属：提示词工程师。2026-10-18 落盘。
> 参数以官方文档为准，10-18 查阅。**写参数前先打开下面的链接核一遍**，MJ 更新很快，文档里没有的参数不写。
> - 版本：https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version
> - 参数总表：https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List
> - 比例：https://docs.midjourney.com/hc/en-us/articles/31894244298125-Aspect-Ratio
> - Stylize：https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize
> - Chaos / Variety：https://docs.midjourney.com/hc/en-us/articles/32099348346765-Chaos-Variety
> - Style Reference：https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference
> - Edit Model：https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model
> - 提示词基础：https://docs.midjourney.com/docs/en/prompts

## 1. 当前版本（官方 Version 页）
- 默认版本 **V8.2**（2026-07-24 起），侧重审美、画质和 Personalization。
- V8.2 带 **Edit Model**，取代了 Omni Reference（`--oref`）、Character Reference（`--cref`）和 Retexture。**V8.x 里不要再写 `--cref` / `--oref`**，要「同一个人 / 同一个物件」用 Edit Model 的参考图（最多 4 张）。
- V8.1 / V8.2 都没有 Quality 参数（`--q`）；最大比例 14:1，HD 模式下 4:1。
- Niji 7（2026-01-09 起）是动漫 / 东方插画方向的单独模型，用 `--niji 7`。

## 2. 参数速查（只列官方文档里有的）
写法规则（参数总表页）：参数放在提示词**最后**；提示词和 `--` 之间空一格；参数里不加逗号、句号。

| 参数 | 作用 | 取值 / 默认（官方） | 什么时候用 |
|---|---|---|---|
| `--ar` / `--aspect` | 宽高比 | 默认 1:1；只能写整数（139:100，不能写 1.39:1）；V8 最大 14:1，HD 4:1 | 每次都写，按用途定（见第 4 节） |
| `--stylize` / `--s` | 艺术发挥程度 | 0–1000，默认 100；低 = 更贴提示词，高 = 更有艺术感、可能偏离 | 要「照着说的画」用 0–100；要氛围感用 250+ |
| `--chaos` / `--c` | 四张图之间差异多大（网页上叫 Variety） | 0–100，默认 0；越高越不可预测 | 探索方向时 20–50；定稿时 0 |
| `--no` | 排除不想要的东西 | 写在后面，如 `--no text, watermark`；官方说法：相当于给那一项 -0.5 权重，是「往外推」不是禁止 | 只放 1–3 个最容易漂进来的东西；正文里不要写 "no xxx"（MJ 会读成要 xxx） |
| `--sref` | 风格参考：图片链接或风格代码 | 可多张图；需同时写文字提示词；图片要是 png/gif/webp/jpg | 品牌已有视觉、主人给了参考图时 |
| `--sw` | 风格参考强度 | 0–1000，默认 100 | 风格太重就降，太弱就升 |
| `--sv` | Style Reference 的模型版本 | 官方：旧风格代码要 `--sv 4` 或换 V6 才能复现 | 只有用到旧 sref 代码时 |
| `--edit` | Edit Model：用文字指令改图，或用最多 4 张参考图生成新图 | V8.1 / V8.2；不兼容 `--tile`，结果不能 Remix；会自动按第一张图的比例，要改比例得写 `--ar` | 要保持同一个人物 / 物件 / 构图（替代以前的 `--cref`、`--oref`） |
| `--iw` | 图片提示词的权重 | 官方表列为支持；取值范围依版本不同，用前查页面 | 用图片当内容参考时 |
| `--raw` | 关掉默认美化，让文字更起作用 | — | 要精确、写实、照片感、或品牌色必须准时 |
| `--v` / `--version` | 指定版本 | 例：`--v 8.2` | 默认就是 8.2，一般不写；要复现旧图才写 |
| `--niji` | 动漫 / 插画模型 | `--niji 7` | 二次元、扁平插画 |
| `--seed` | 固定随机起点 | V8 下同 seed 约 99% 一致 | 只改一个词做对比时 |
| `--tile` | 无缝重复图案 | 不能和 `--edit` 一起用 | 底纹、包装纹样 |
| `--sd` / `--hd` | 标准 1024px / HD 2048px | V8.1 起；HD 耗 GPU 更多（1.3 分钟对 0.8 分钟） | 要印刷或大图才用 HD |
| `--p` / `--profile` | Personalization 个人风格 / 情绪板 | — | 主人在 MJ 里建好了个人档案时 |
| `--weird` / `--w`、`--draft`、`--repeat` | 怪诞度 / 草稿模式 / 重复跑 | 官方表里有；V8.2 是否支持以 Version 页对照表为准 | 少用，用前核对 |

> 已不适用于 V8.2：`--q`、`--oref`、`--cref`、`--turbo`；多重提示 `::` 权重官方写明只到 V6.1。

## 3. 固定结构（按这个顺序写）
英文，一段话，按重要性从前往后：

```
[主体 subject] , [风格 style / medium] , [构图 composition / camera] , [光线 lighting] , [色彩 color palette] , [细节与质感 details] --ar [比例] --s [值] --c [值] --no [排除项] [--sref / --raw 等]
```

| 位置 | 写什么 | 例 |
|---|---|---|
| 主体 | 谁 / 什么、在做什么、在哪；具体名词 + 动作 | a renovated 89 m² apartment living room with an open kitchen |
| 风格 | 媒介、画风、年代、流派（不写在世艺人名） | hand-drawn architectural sketch, warm marker rendering |
| 构图 | 视角、景别、镜头 | top-down floor plan view / eye-level wide shot, 24mm |
| 光线 | 时间、光源、软硬 | soft morning daylight from large windows |
| 色彩 | 主色、辅色（有品牌规则就抄品牌色） | cream white, oak wood, muted sage green |
| 比例 | `--ar`，按用途 | 见第 4 节 |
| 排除项 | `--no`，1–3 项 | `--no text, watermark, people` |

要点（来自官方「提示词基础」页）：写想要什么，不写不想要什么；重要的元素都要写进去，没写的 MJ 会自己补；短提示词 = 更多随机，长提示词 = 更多控制。

## 4. 常用比例（按用途）
| 用途 | `--ar` |
|---|---|
| 小红书封面 / 竖版帖 | 3:4 |
| 抖音 / 视频号 / 手机壁纸 | 9:16 |
| 头像 | 1:1 |
| 官网横幅 / B 站封面 | 16:9 |
| 海报（A 系列近似） | 5:7 或 2:3 |

## 5. 中文需求 → 英文提示词
1. **先拆**：把中文需求拆进第 3 节的六个位置；缺哪个就看品牌规则或参考图补，补不了才问（一次只问最关键的一件）。
2. **换成看得见的词**：抽象词换成画面。「高级感」→ minimal composition, soft diffused light, muted palette, generous negative space；「温馨」→ warm lamp light, soft textiles, wood tones；「无厘头」→ playful, absurd, unexpected scale。
3. **专有名词**：中文品牌名、店名不要指望 MJ 写对字；需要文字的地方只描述 "blank sign area"，字由主人后期加。
4. **文化元素**：写具体物件而不是笼统的 "Chinese style"（如 "red lacquered door, brass knocker"）。
5. **否定改正向**：「不要太亮」→ low-key lighting；真要排除的放进 `--no`。
6. **品牌规则优先**：有品牌规则的项目，主色、语气、禁用元素照抄品牌规则；和需求冲突时问品牌顾问。

## 6. 交付格式
```
## 思路（中文 1–2 句）
……

## 主提示词
<英文提示词> --ar 3:4 --s 150 --c 10 --no text, watermark

## 变体（说明改了哪一处）
……

## 参考图怎么用（如有）
--sref <链接>，或在 Imagine 栏附加图片用 Edit Model

## 下一轮怎么改
一次只改一处：太乱 → 降 --c；不像说的 → 降 --s 或加 --raw；风格太重 → 降 --sw
```

## 7. 改版（主人说「不对」）
先判断是哪一类：内容不对（改主体描述）、风格不对（改风格词或 `--sref` / `--sw`）、太随机（降 `--c`）、太「AI 味」（加 `--raw`、降 `--s`）、多了东西（加进 `--no`）。一次只改一处，并用 `--seed` 固定其他条件做对比。

## 8. 边界
- 只交付提示词，**不调用任何生图工具**，不用 bot 额度出图。
- 不编参数；官方文档没有的写「文档里没有」。
- 不写模仿在世艺人、真人肖像或他人商标的提示词。
- 视频：待定工具后再补。
