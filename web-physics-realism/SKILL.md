---
name: web-physics-realism
description: >-
  网页/游戏里"像真的一样"的物理真实感总入口：光影反光、重力、摩擦、弹性、碰撞、关节、拖拽惯性、弹簧手感。
  把主人的大白话（像两层纸、太飘、不够弹、太亮、像塑料、太滑）翻译成技术参数，按需求选对技术
  （本地 gsap Inertia/Physics2D/PhysicsProps、anime spring、Matter.js、three.js PBR、Rapier），
  并用参考图对照 + 2-3 版截图选项卡的流程交付。凡是 3D 物品、光照阴影、物理动效、"不真实/不自然"类反馈都先读本 skill。
---

# 网页物理真实感（web-physics-realism）

## 0. 硬规则（必须遵守）

1. **涉及光源方向、阴影、反光，或物体受力/碰撞/堆叠/掉落时，禁止用 CSS 叠片、手调渐变或手写位移去"假装"。** 必须用下面第 2 节对应的真引擎（three.js 光照 / 物理引擎 / 物理插件）。理由：CSS 没有光源和受力概念，每处方向都要人工对齐，改一处错一处。
2. 同一画面只能有**一个主光方向**；所有高光、阴影、露边都由它推出来，不能各自手调。
3. 每次交付必须附截图，并和主人给的参考图并排自检（第 5 节）。
4. 改已有项目前先用选项卡问主人是否换技术（例如把 CSS 伪 3D 换成 three.js），并遵守项目的 LOCK/LOG 规则。
5. 不确定主人要的效果时，不要猜一版就交：出 2–3 版截图让他点选（第 6 节）。

## 1. 大白话 → 参数对照表

| 主人说 | 实际问题 | 调什么（方向） |
|---|---|---|
| 像两层纸 / 太薄 / 没体积 | 缺厚度、侧面、接触阴影 | 建真实厚度的几何体；侧面比正面暗 10–30%；加接触阴影（ContactShadows / 阴影接收平面） |
| 浮着 / 没落地 / 像贴上去的 | 物体和地面之间没阴影 | 开 `castShadow/receiveShadow`；加接触阴影；阴影 `bias` 约 -0.0005、`normalBias` 0.02 防止漏光/条纹 |
| 反光方向不对 / 露边方向乱 | 多个"假光源" | 只留一盏主光（DirectionalLight），高光、阴影全由它产生；环境贴图负责整体反射 |
| 太亮 / 发白 / 过曝 | 曝光或色调映射错误 | `toneMapping = ACESFilmicToneMapping`，`toneMappingExposure` 降到 0.8–1.0；主光强度降低 |
| 发灰 / 发闷 / 颜色脏 | 色彩空间错 | `outputColorSpace = SRGBColorSpace`；颜色贴图设 sRGB；不要叠太多环境光 |
| 像塑料 / 不像金属 | 材质参数不对 | 金属：metalness 1、roughness 0.2–0.4；塑料：metalness 0、roughness 0.4–0.6；必须有环境贴图，否则金属是黑的 |
| 屏幕/玻璃没质感 | 缺清漆反射 | `MeshPhysicalMaterial`：clearcoat 1、clearcoatRoughness 0.05–0.1；玻璃加 transmission 1、ior 1.5 |
| 太飘 / 慢动作 / 像在水里 | 重力太小或阻尼不对 | 重力用真实的 9.81 m/s²（注意场景单位：1 单位 = 1 米）；物体尺寸按真实比例；linearDamping 0–0.1 |
| 太沉 / 太死板 | 阻尼过大、没有回弹 | 降低 damping；适当加 restitution（弹性） |
| 不够弹 / 没弹性 | 弹性系数低 | restitution 提到 0.6–0.8（球类）；弹簧动画降低 damping、提高 stiffness |
| 弹个不停 / 抖 | 弹性过高或步长不稳 | restitution ≤ 0.9；固定步长 1/60；见 `physics-tuning` skill |
| 太滑 / 停不下来 | 摩擦太小 | friction 提到 0.6–1.0；加 linearDamping |
| 太涩 / 推不动 | 摩擦太大 | friction 降到 0.1–0.3 |
| 穿模 / 穿过去了 | 高速物体漏检测 | 开 CCD（连续碰撞检测）；碰撞体用简单形状；见 `physics-tuning` |
| 拖完一松手就停 / 不跟手 | 缺惯性 | gsap InertiaPlugin 或 Draggable `inertia: true`；anime draggable 的释放惯性 |
| 动画生硬 / 像机器 | 用了线性缓动 | 换弹簧（spring）：stiffness 100–300、damping 10–30、mass 1 |

## 2. 按需求分级选型（从简单到复杂，够用即停）

| 需求 | 用什么 | 位置 / 安装 |
|---|---|---|
| 界面手感：弹簧、回弹、跟手 | anime.js spring | 本地 `E:\coding\skills\网页设计\libs\animejs\src\easings\spring\`；配合 `animejs` skill |
| 拖拽甩出后的惯性 | gsap InertiaPlugin + Draggable | 本地 `E:\coding\skills\网页设计\libs\gsap\src\InertiaPlugin.js`、`Draggable.js`；配合 `gsap` skill |
| 2D 抛物线、重力、摩擦（单个物体，不互相碰撞） | gsap Physics2DPlugin（velocity/angle/gravity/friction） | 本地 `...\libs\gsap\src\Physics2DPlugin.js` |
| 让任意属性带速度/加速度/摩擦地变化 | gsap PhysicsPropsPlugin | 本地 `...\libs\gsap\src\PhysicsPropsPlugin.js` |
| 2D 多物体碰撞、堆叠、掉落、约束 | Matter.js（MIT） | `npm i matter-js`；只能 2D |
| 3D 物品的光影、反光、材质（电视、产品展示） | three.js：MeshPhysicalMaterial + RoomEnvironment 或 HDRI + 阴影 + ACES + sRGB | `npm i three`；配合 `threejs-shadow-systems`、`threejs-visual-validation` |
| 3D 重力、碰撞、摩擦、弹性、关节 | Rapier（Apache-2.0） | 原生 JS：`npm i @dimforge/rapier3d-compat`；React 项目：`@react-three/rapier` |
| 引擎怎么选的完整阶梯 | 读 `references/physics-engine-selection.md` | 自写碰撞 → Rapier → cannon-es → Jolt → Ammo；Matter 仅 2D |

不推荐：cannon-es（2022 年后未发版）、ammo.js（难用），除非项目已在用。

## 3. 默认配置

### 3.1 three.js 真实感基线（3D 物品默认就这样起步）

```js
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture; // 反射来源；要更真实可换 HDRI

const key = new THREE.DirectionalLight(0xffffff, 2.5); // 唯一主光
key.position.set(3, 5, 2);
key.castShadow = true;
key.shadow.mapSize.set(2048, 2048);
key.shadow.bias = -0.0005;
key.shadow.normalBias = 0.02;
scene.add(key);

const ground = new THREE.Mesh(new THREE.PlaneGeometry(20, 20), new THREE.ShadowMaterial({ opacity: 0.25 }));
ground.rotation.x = -Math.PI / 2;
ground.receiveShadow = true;
scene.add(ground);
```

### 3.2 常见材质参数（three.js PBR）

| 材质 | metalness | roughness | 其他 |
|---|---|---|---|
| 亮面金属（不锈钢、铝） | 1 | 0.15–0.3 | — |
| 拉丝/哑光金属 | 1 | 0.4–0.6 | — |
| 亮面塑料（电视边框） | 0 | 0.3–0.4 | clearcoat 0.3 |
| 哑光塑料 | 0 | 0.6–0.8 | — |
| 屏幕玻璃（关机） | 0 | 0.05 | clearcoat 1，颜色接近黑 |
| 屏幕（开机画面） | 0 | 0.1 | emissiveMap = 画面，emissiveIntensity 1 |
| 透明玻璃 | 0 | 0–0.05 | transmission 1，ior 1.5，thickness 0.01–0.05 |
| 木头 | 0 | 0.6–0.8 | 用木纹贴图 |
| 布料 | 0 | 0.9–1 | sheen 0.5 |

### 3.3 常见材质摩擦 / 弹性（物理引擎近似值，按手感微调）

| 材质组合 | friction | restitution |
|---|---|---|
| 冰 | 0.02–0.05 | 0.1 |
| 钢对钢 | 0.4–0.6 | 0.3–0.5 |
| 木头 | 0.4–0.6 | 0.3–0.5 |
| 塑料 | 0.3–0.5 | 0.4–0.6 |
| 橡胶 | 0.8–1.0 | 0.7–0.85 |
| 篮球/弹力球 | 0.6–0.8 | 0.75–0.9 |
| 布、海绵、泥 | 0.7–1.0 | 0–0.1 |
| 玻璃 | 0.2–0.4 | 0.5–0.7 |

物理默认：重力 (0, -9.81, 0)；固定步长 1/60，帧间隔上限 0.1 秒（见 references）；碰撞体用盒、球、胶囊等简单形状，不用精细模型。

### 3.4 弹簧手感预设（anime spring / motion / react-spring 通用思路）

| 手感 | stiffness | damping | mass |
|---|---|---|---|
| 稳、不回弹（按钮、面板） | 300 | 30 | 1 |
| 轻快、微回弹（卡片） | 200 | 18 | 1 |
| 很弹、Q 弹（图标、提醒） | 250 | 10 | 1 |
| 慢、沉（大物件） | 120 | 20 | 2 |

anime.js v4 的 spring 参数名以本地源码 `libs/animejs/src/easings/spring/` 为准（新版也支持 bounce/duration 写法），用前先看源码。

## 4. 何时必须用真引擎，而不是 CSS 手调

- 需要光源方向一致的高光、阴影、露边 → three.js
- 物体会旋转、看到多个面，且要明暗随角度变化 → three.js
- 两个以上物体互相碰撞、堆叠、推动 → Matter.js（2D）/ Rapier（3D）
- 单个物体抛、落、滑，需要真实的重力和摩擦 → gsap Physics2D（2D）
- 只是 hover、按钮回弹、面板滑入 → CSS 过渡或弹簧动画即可，不必上引擎

## 5. 自检清单（每次交付前逐条过）

- [ ] 截图和参考图并排对比过，差异已列出
- [ ] 只有一个主光方向；所有高光、阴影、露边方向一致
- [ ] 物体和地面接触处有阴影，没有"浮空"
- [ ] 阴影无条纹、无锯齿、无漏光（调 bias/normalBias、mapSize）
- [ ] 色调映射 ACES、输出 sRGB；画面不过曝不发灰
- [ ] 金属/玻璃有环境反射（不是黑的）
- [ ] 物体按真实比例；重力 9.81；固定步长
- [ ] 没有穿模、抖动、无限弹跳
- [ ] 手机上帧率可接受（阴影贴图、像素比 ≤ 2）
- [ ] 用 `threejs-visual-validation` 的截图验证流程过一遍（3D 场景）

## 6. 和主人的沟通流程（主人不写代码）

1. **要参考**：请主人发实物照片、截图或视频（"像这个"），不要求他描述技术细节。
2. **翻译**：用第 1 节的对照表把他的话和参考图翻成参数，用一句大白话复述给他确认。
3. **出 2–3 版**：只改一个变量（如"反光强/中/弱"、"阴影硬/软"、"弹性高/中/低"），各截一张图。
4. **选项卡点选**：一张卡只问一个问题，选项就是这几版截图对应的描述；他选完再细调下一个变量。
5. **记录**：把最终参数写进项目 LOG，下次同类物品直接复用。

## 7. 相关 skill

- `physics-tuning`：步长、抖动、穿模、碰撞分层（引擎无关）
- `threejs-shadow-systems`：three.js 阴影系统细节
- `threejs-visual-validation`：3D 画面截图验证流程
- `gsap`、`animejs`：本地动画库用法
- `references/physics-engine-selection.md`：物理引擎选择阶梯与 Rapier 起步代码（MIT，来源见 references/SOURCE.md）
