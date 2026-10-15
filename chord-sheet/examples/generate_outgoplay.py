# -*- coding: utf-8 -*-
"""Rebuild Out Go Play chord sheets from Project/和弦谱 only.

Sources (read-only):
  - *_歌词.docx — lyrics / section labels
  - 和弦谱/*.docx — Nashville key/BPM/bar charts (| 6m - 4 - | 5 - 3 - |)
Output (write-only):
  - 成品/*.docx — Chinese filenames; never overwrite sources
Skip: 戏瘾
Blank key/BPM/chords: 小鱼

HAND_EDITED (2026-09-29): 用户已手动改好 成品/空凤梨罐头.docx、成品/不是眼泪.docx，
本脚本只把它们的内容同步进 spec 备查，**不再写出**这两个文件。

格式约定（从用户手改稿学来）：
  - 和弦行按小节写：bars("E F#", "B") -> "| E   F#  | B       |"，一格一小节，
    格内两个和弦各占半小节；不再按歌词音节对位。
  - 重复段落只写 Section(same_as="主歌 Verse 1") -> 「（同主歌 Verse 1）」加粗一行。
  - 段名 > 歌词字号，和弦 > 歌词字号，段落之间留明显空白（见 chord_sheet.PRESETS）。
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, r"e:/coding/.cursor/skills/chord-sheet")
from chord_sheet import Line, Section, Song, bars, render  # noqa: E402

ROOT = Path(r"e:/coding/Project/和弦谱")
# 只写入新建成品目录，绝不覆盖 歌词 / 和弦谱 源文件
OUT = ROOT / "成品"
# 用户手改过的成品：永不覆盖
HAND_EDITED = {"空凤梨罐头.docx", "不是眼泪.docx"}


def L(chord: str = "", lyric: str = "") -> Line:
    return Line(chord=chord, lyric=lyric)


# --- key tables ----------------------------------------------------------- #
DEG_B = [
    ("1", "B", "B – D# – F#"),
    ("2", "C#m", "C# – E – G#"),
    ("3", "D#m", "D# – F# – A#"),
    ("4", "E", "E – G# – B"),
    ("5", "F#", "F# – A# – C#"),
    ("6", "G#m", "G# – B – D#"),
    ("7", "A#dim", "A# – C# – E"),
]
DEG_F = [
    ("1", "F", "F – A – C"),
    ("2", "Gm", "G – Bb – D"),
    ("3", "Am", "A – C – E"),
    ("4", "Bb", "Bb – D – F"),
    ("5", "C", "C – E – G"),
    ("6", "Dm", "D – F – A"),
    ("7", "Edim", "E – G – Bb"),
]
DEG_E = [
    ("1", "E", "E – G# – B"),
    ("2", "F#m", "F# – A – C#"),
    ("3", "G#m", "G# – B – D#"),
    ("4", "A", "A – C# – E"),
    ("5", "B", "B – D# – F#"),
    ("6", "C#m", "C# – E – G#"),
    ("7", "D#dim", "D# – F# – A"),
]
DEG_C = [
    ("1", "C", "C – E – G"),
    ("2", "Dm", "D – F – A"),
    ("3", "Em", "E – G – B"),
    ("4", "F", "F – A – C"),
    ("5", "G", "G – B – D"),
    ("6", "Am", "A – C – E"),
    ("7", "Bdim", "B – D – F"),
]
DEG_A = [
    ("1", "A", "A – C# – E"),
    ("2", "Bm", "B – D – F#"),
    ("3", "C#m", "C# – E – G#"),
    ("4", "D", "D – F# – A"),
    ("5", "E", "E – G# – B"),
    ("6", "F#m", "F# – A – C#"),
    ("7", "G#dim", "G# – B – D"),
]
DEG_G = [
    ("1", "G", "G – B – D"),
    ("2", "Am", "A – C – E"),
    ("3", "Bm", "B – D – F#"),
    ("4", "C", "C – E – G"),
    ("5", "D", "D – F# – A"),
    ("6", "Em", "E – G – B"),
    ("7", "F#dim", "F# – A – C"),
]


def lyric_only(lines: list[str]) -> list[Line]:
    return [L("", x) for x in lines]


# ========================================================================= #
# 1 不是眼泪 — B / 70  【HAND_EDITED：仅同步 spec，不输出】
# ========================================================================= #
def song_yanlei() -> Song:
    v = bars("E F#", "B")
    v_turn = bars("E F#", "G#m C#")
    v_tail = bars("E F#")
    pre = bars("E", "B")
    pre2 = bars("E G#m", "F#")
    ch = bars("B F#", "E")
    return Song(
        title="出去玩！ — 不是眼泪",
        meta="原调 B Major  ·  70 BPM  ·  4/4",
        key_label="B Major",
        degrees=DEG_B,
        extensions=[
            "主歌：E – F# – B；转折 E – F# – G#m – C#",
            "预副：E – B / E – G#m – F#",
            "副歌：B – F# – E / G#m – F# – E",
        ],
        sections=[
            Section(title="前奏 Intro", lines=[L(v), L(v)]),
            Section(
                title="主歌 Verse 1",
                lines=[
                    L(v, "为什么　我的眼里都是泪水"),
                    L(v, "为什么　突然想写一首诗"),
                    L(v_turn, "关于过去　关于过去和涌起的情绪"),
                    L(v_tail, "关于我不虚此行"),
                ],
            ),
            Section(
                title="主歌 Verse 2",
                lines=[
                    L(v, "为什么　那天的我读不懂那颗心"),
                    L(v, "为什么　还是会有残留痕迹"),
                    L(v_turn, "关于过去　关于过去　丈量现在的距离"),
                    L(v, "或许　我只是想证明我自己"),
                ],
            ),
            Section(
                title="预副歌 Pre-Chorus",
                lines=[L(pre, "我无法忘记你"), L(pre2, "我还是会想起")],
            ),
            Section(
                title="副歌 Chorus 1",
                lines=[
                    L(ch, "我把它的温柔　它的体恤　留给自己"),
                    L(ch, "我把它的任性　它的梦境　重塑彻底"),
                    L(ch, "我把它的依靠　它的离去　赋予意义"),
                    L(ch, "我把它的眼神　它的语气　刻进心底"),
                ],
            ),
            Section(title="主歌 Verse 3", same_as="同主歌 Verse 1"),
            Section(title="预副歌 Pre-Chorus", same_as="同预副歌 Pre-Chorus"),
            Section(title="副歌 Chorus 2", same_as="同副歌 Chorus 1"),
            Section(title="副歌 Chorus 3", same_as="同副歌 Chorus 1"),
            Section(title="尾奏 Outro", lines=[L(bars("B", "E")), L(bars("B"))]),
        ],
    )


# ========================================================================= #
# 2 我对我自己说 — F / 127
# ========================================================================= #
def song_ziji() -> Song:
    # 2026-09 谱：1=F。2m/6m/3m 为小三；Rap 的 2、3 未标 m，作大三 G、A。
    # 127 BPM 来自上一版中间稿（新稿未写速度）。
    va = bars("Dm", "Bb")
    vb = bars("Gm Bb", "Dm")
    pre = bars("Bb C", "Dm")
    c_a = bars("Dm", "Bb")
    c_b = bars("F", "C")
    rap = bars("Dm", "Bb", "G", "A")
    return Song(
        title="出去玩！ — 我对我自己说",
        meta="原调 F Major  ·  127 BPM  ·  4/4",
        key_label="F Major",
        degrees=DEG_F,
        extensions=[
            "主歌：Dm – Bb；Gm – Bb | Dm",
            "预副：Bb – C | Dm",
            "副歌：Dm – Bb | F – C；第二遍收 Am",
            "Rap：Dm – Bb – G – A",
        ],
        sections=[
            Section(title="前奏 Intro", lines=[L(bars("Dm", "Bb", "Dm", "Bb"))]),
            Section(
                title="主歌 Verse 1",
                lines=[
                    L(va, "小镇的码头老人卖着旧货"),
                    L(va, "远处的山坡有栋房子褪色"),
                    L(vb, "年轻的人在远方寻找自我"),
                    L(vb, "梦想在现实的兜里　赤裸"),
                    L(va, "有人在沙漠行走寻找骆驼"),
                    L(va, "有人在沙发大口吃着苹果"),
                    L(vb, "反正再次睁开眼将会面临新选择"),
                    L(vb, "那就让我的任性告诉我该怎么做"),
                ],
            ),
            Section(
                title="预副歌 Pre-Chorus 1",
                lines=[
                    L(pre, "我祈祷　有人能记得我"),
                    L(pre, "我祈祷　比昨天更快乐"),
                    L(pre, "我祈祷　能失而复得"),
                    L(pre, "我终于感动了自我"),
                ],
            ),
            Section(
                title="副歌 Chorus 1",
                lines=[
                    L(c_a, "我对我自己说　我对我自己说"),
                    L(c_b, "你是晴空的闪电　惊醒乌云的寂寞"),
                    L(c_a, "我对我自己说　我对我自己说"),
                    L(c_b, "你是燃烧的篝火　燃尽世间的罪恶"),
                    L(bars("Dm", "Dm")),
                ],
                note="末两小节 Dm",
            ),
            Section(
                title="说唱 Rap",
                lines=[
                    L(rap, "我哪里有错　既然你指控我　你的证据最好比我的词更华丽"),
                    L("", "反正好过　寄托于某个人　其实他本身并没有参考性"),
                    L("", "流下的泪水　留下的欢笑　我的证人比你更权威"),
                    L("", "他们说我的纯粹　就是愚蠢的无可救药"),
                    L(rap, "所谓的生　所谓的死　随你们来吧　这是我地址"),
                    L("", "说我的闲话　当然有意思了"),
                    L("", "哪里是天堂　哪里是地狱　要去往哪里都由我来掌舵"),
                    L("", "不需要向谁来证明　我的信仰　听　台下正喊我的名"),
                ],
            ),
            Section(
                title="预副歌 Pre-Chorus 2",
                same_as="同预副歌 Pre-Chorus 1",
                lines=[L(bars("Dm"))],
                note="末多一小节 Dm",
            ),
            Section(
                title="副歌 Chorus 2",
                lines=[
                    L(c_a, "我对我自己说　我对我自己说"),
                    L(c_b, "你是远方的孤岛　候鸟梦中的轮廓"),
                    L(c_a, "我对我自己说　我对我自己说"),
                    L(c_b, "你是岩缝的野草　绽放每一个角落"),
                    L(bars("Dm", "Bb", "F", "C")),
                    L(bars("Am")),
                ],
                note="第三遍无词，收在 Am",
            ),
            Section(
                title="尾奏 Outro",
                lines=[
                    L(bars("Dm", "Bb", "F", "-")),
                    L(bars("Dm", "Bb", "F", "C")),
                    L(bars("Dm")),
                ],
                note="第一行第四小节空",
            ),
        ],
    )


# ========================================================================= #
# 3 绽放 — B / 72
# ========================================================================= #
def song_zhanfang() -> Song:
    loop = bars("B", "G#m", "E", "F#")
    return Song(
        title="出去玩！ — 绽放",
        meta="原调 B Major  ·  72 BPM  ·  4/4",
        key_label="B Major",
        degrees=DEG_B,
        extensions=["全程：B – G#m – E – F#（1–6m–4–5）"],
        sections=[
            Section(title="前奏 Intro", lines=[L(loop), L(loop)], note="重复一遍"),
            Section(
                title="主歌 Verse 1",
                lines=[
                    L(loop, "这是我喜欢的　喜欢的季节"),
                    L(loop, "唱着喜欢的歌　很多"),
                    L(loop, "很多我的快乐　在我生命里像星星闪烁"),
                    L(loop, "我记得　窗外的云朵是散落自由的烟火"),
                    L(loop, "我记得　仲夏晚风温柔拥吻着我"),
                    L(loop, "我记得　树旁的影子陪我度过整个周末"),
                    L(loop, "我记得一切的一切　是生命绽放的时刻"),
                ],
            ),
            Section(
                title="副歌 Chorus 1",
                lines=[
                    L(loop, "如果我忘了　请你告诉我"),
                    L(loop, "全部告诉我"),
                    L(loop, "比如我们的爱如何开始的"),
                    L(loop, "又如何遗憾变成歌　全部告诉我"),
                    L(loop, "如果我要走　请不要挽留　我的朋友"),
                    L(loop, "等黄昏的花开满山时刻"),
                    L(loop, "感谢你陪我一起　走过度过来过"),
                ],
            ),
            Section(title="间奏 Interlude", lines=[L(loop), L(loop)]),
            Section(
                title="主歌 Verse 2",
                lines=[
                    L(loop, "这是我喜欢的　喜欢的季节"),
                    L(loop, "唱着喜欢的歌　是生命绽放的时刻"),
                ],
            ),
            Section(title="副歌 Chorus 2", same_as="同副歌 Chorus 1"),
            Section(title="尾奏 Outro", lines=[L(loop), L(loop)], note="重复至结束"),
        ],
    )


# ========================================================================= #
# 4 燃烧的篝火 — C→C# / 64
# ========================================================================= #
def song_gouhuo() -> Song:
    loop = bars("Am", "G", "F", "E")
    loop2 = bars("A#m", "G#", "F#", "F")
    return Song(
        title="出去玩！ — 燃烧的篝火请你告诉我",
        meta="原调 C Major（副歌末升 C#）  ·  64 BPM  ·  4/4",
        key_label="C Major → C# Major",
        degrees=DEG_C,
        extensions=[
            "主进行：Am – G – F – E",
            "升调后：A#m – G# – F# – F",
        ],
        sections=[
            Section(
                title="主歌 Verse 1",
                lines=[
                    L(loop, "我偶尔也会说谎　在想要逃避的问题上"),
                    L(loop, "我偶尔也会瞎想　如果当时选择了另一条路会怎样"),
                    L(loop, "会不会更加迷茫"),
                    L(loop, "虚伪的笑着捧场　变成我最讨厌的那个模样"),
                    L(loop, "会不会忘了梦想"),
                    L(bars("E"), "忘了我有双翅膀　能飞到任何我想去的地方"),
                ],
            ),
            Section(
                title="预副歌 Pre-Chorus",
                lines=[
                    L(loop, "过去的故事线以无法改变　时间无法停止往前"),
                    L(loop, "那些莫名的奇妙的伟大冒险　在等我遇见　在我消失以前"),
                    L(bars("E")),
                ],
            ),
            Section(
                title="副歌 Chorus 1",
                lines=[
                    L(loop, "燃烧的篝火请你告诉我　此刻的落寞是否遵循因果"),
                    L(loop, "燃烧的篝火请你告诉我　我没有做错只做了不同的选择"),
                    L(loop, "燃烧的篝火请你告诉我　所谓的命运是否用力就能够挣脱"),
                    L(loop, "燃烧的篝火请你告诉我　我是否还是我　或是扑火的飞蛾　还是一望无际的星河"),
                    L(bars("E")),
                ],
            ),
            Section(
                title="间奏 Interlude",
                lines=[L(loop), L(loop)],
                note="键盘四遍，吉他四遍",
            ),
            Section(
                title="副歌 Chorus 2",
                lines=[
                    L(loop, "燃烧的篝火请你告诉我　最后的最后将由谁来朗读我的传说"),
                    L(loop, "燃烧的篝火请你告诉我　我是否还是我　或是扑火的飞蛾　还是一望无际的星河"),
                    L(bars("F"), "（升调预备）"),
                ],
            ),
            Section(
                title="副歌 Chorus 3（升调 C#）",
                same_as="词同副歌 Chorus 1，和弦改用升调进行",
                lines=[L(loop2)],
            ),
        ],
    )


# ========================================================================= #
# 5 空凤梨罐头 — A / 93  【HAND_EDITED：仅同步 spec，不输出】
# ========================================================================= #
def song_guantou() -> Song:
    loop = bars("F#m D", "E C#")
    return Song(
        title="出去玩！ — 空凤梨罐头",
        meta="原调 A Major  ·  93 BPM  ·  4/4",
        key_label="A Major",
        degrees=DEG_A,
        extensions=["主进行：F#m – D – E – C#", "主歌末：D – C#"],
        sections=[
            Section(
                title="前奏 Intro",
                lines=[L(bars("F#m", "F#m")), L(loop), L(loop)],
                note="先 F#m，再进入主进行",
            ),
            Section(
                title="主歌 Verse 1",
                lines=[
                    L(loop, "你只是听说　从他们嘴里听说"),
                    L(loop, "那些关于我　和关于我的沉默"),
                    L(loop, "你只是听说　从他们嘴里听说"),
                    L(loop, "那些恨我的　羡慕的　嫉妒的　讨厌我的实在太多"),
                    L(loop, "你只是听说　仅是他们嘴里听说"),
                    L(loop, "没人会喜欢我　没有人能懂我黑色幽默"),
                    L(loop, "和我的倔强　我的冷漠 我的伪装　和我的软弱"),
                    L(loop, "和我的痛苦都充满着我的躯壳　怎么会感到寂寞"),
                    L(bars("E"), "怎么会感到寂寞"),
                ],
            ),
            Section(
                title="副歌 Chorus 1",
                lines=[
                    L(loop, "给我勇气的另一个我　听我灵魂在唱歌"),
                    L(loop, "唱的是你最爱的那一首　空凤梨罐头"),
                    L(loop, "是我的心啊　你不必斟酌　请疯狂审视我"),
                    L(loop, "就算和他说的一样　那又怎样呢"),
                ],
            ),
            Section(title="间奏 Interlude", lines=[L(loop), L(loop)]),
            Section(title="主歌 Verse 2", same_as="同主歌 Verse 1"),
            Section(title="副歌 Chorus 2", same_as="同副歌 Chorus 1"),
            Section(title="间奏 Interlude", lines=[L(loop)]),
            Section(title="副歌 Chorus 3", same_as="同副歌 Chorus 1"),
        ],
    )


# ========================================================================= #
# 6 我想 — E / 116
# ========================================================================= #
def song_woxiang() -> Song:
    loop = bars("C#m E", "B A")
    return Song(
        title="出去玩！ — 我想",
        meta="原调 E Major  ·  116 BPM  ·  4/4",
        key_label="E Major",
        degrees=DEG_E,
        extensions=["全程：C#m – E – B – A（6m–1–5–4）"],
        sections=[
            Section(title="前奏 Intro", lines=[L(loop), L(loop)], note="重复两遍"),
            Section(
                title="主歌 Verse 1",
                lines=[
                    L(loop, "我把糊里糊涂的勇气都装进身体"),
                    L(loop, "在没有人的夜里给自己打气"),
                    L(loop, "我把屋里屋外的氧气呼吸个干净"),
                    L(loop, "其实我很贪婪这不是一个秘密"),
                    L(loop, "我想留下　几段英雄事迹"),
                    L(loop, "好像有点难度　不如留一下段旋律"),
                    L(loop, "就让他们怀疑　就当我并不在意"),
                    L(loop, "我也是个孩子难过时候也会打给母亲"),
                ],
            ),
            Section(
                title="预副歌 Pre-Chorus",
                lines=[
                    L(loop, "走过沙漠海洋在深夜里嘶吼"),
                    L(loop, "成为夜空中最亮的星给他们指引方向"),
                    L(loop, "成为武将的利刃斩断恶意的目光"),
                    L(loop, "然后把我的愿望统统塞进音箱"),
                ],
            ),
            Section(
                title="副歌 Chorus 1",
                lines=[
                    L(loop, "我想做个无情的杀手"),
                    L(loop, "我想做个完美的爱人"),
                    L(loop, "我想做个快乐的小丑"),
                    L(loop, "我想做个无名的英雄"),
                ],
            ),
            Section(title="独奏 Solo", lines=[L(loop), L(loop)], note="重复一遍"),
            Section(title="预副歌 Pre-Chorus 2", same_as="同预副歌 Pre-Chorus"),
            Section(
                title="副歌 Chorus 2",
                same_as="同副歌 Chorus 1",
                note="末尾多两拍 A（2-beat break）",
            ),
            Section(title="桥段 Bridge", lines=[L(loop)]),
            Section(
                title="尾奏 Outro",
                lines=[L(loop, "我想做个无名的英雄")],
                note="末行重复至结束",
            ),
        ],
    )


# ========================================================================= #
# 7 骤雨 — C / 86
# ========================================================================= #
def song_zhouyu() -> Song:
    loop = bars("C", "Am", "F", "G")
    turn_a = bars("C", "Am")
    turn_b = bars("F E", "Dm G")
    return Song(
        title="出去玩！ — 骤雨",
        meta="原调 C Major  ·  86 BPM  ·  4/4",
        key_label="C Major",
        degrees=DEG_C,
        extensions=["主进行：C – Am – F – G", "转折：C – Am | F – E – Dm – G"],
        sections=[
            Section(title="前奏 Intro", lines=[L(loop)]),
            Section(
                title="主歌 Verse 1",
                lines=[
                    L(loop, "一开始只是喜欢　只是喜欢"),
                    L(loop, "然后开始习惯　习惯有你每天都跟我说我晚安"),
                    L(loop, "聊过七彩斑斓湖水里有数不清的船"),
                    L(loop, "聊过金黄色的麦田里有情绪被拨乱"),
                    L(turn_a, "像是一幅画　像是一首歌"),
                    L(turn_b, "每天"),
                ],
            ),
            Section(
                title="主歌 Verse 2",
                lines=[
                    L(loop, "一开始只是喜欢　只是喜欢"),
                    L(loop, "然后开始习惯　习惯有你每天都跟我说我晚安"),
                    L(loop, "聊过万家灯火通明餐桌上留的晚餐"),
                    L(loop, "聊过银装素裹冬天里你炙热的陪伴"),
                    L(loop, "像是一幅画　像是一首歌"),
                    L(loop, "每天"),
                ],
            ),
            Section(
                title="空 Break",
                lines=[L(bars("C", "C", "C"))],
                note="三小节 C，全体停",
            ),
            Section(title="尾奏 Outro", lines=[L(loop), L(loop)], note="重复至结束"),
        ],
    )


# ========================================================================= #
# 9 小鱼 — no key / BPM / chords
# ========================================================================= #
def song_xiaoyu() -> Song:
    return Song(
        title="出去玩！ — 小鱼",
        meta="原调    ·     ·  ",
        key_label="",
        degrees=[],
        extensions=[],
        sections=[
            Section(
                title="主歌 Verse 1",
                lines=lyric_only([
                    "你曾对我说",
                    "你有很多想去的地方",
                    "那里有鲜花和牧场",
                    "红烧鸡翅膀",
                    "可现在怎么像被锁住一样",
                    "无处可逃",
                    "无处可躲",
                    "莫名沉重的欲望",
                    "贪婪的理想",
                    "怎么变得和他一样",
                ]),
            ),
            Section(
                title="副歌 Chorus",
                lines=lyric_only([
                    "去吧",
                    "去所有的地方",
                    "去看那片海洋",
                    "陌生人的故乡",
                    "去吧",
                    "爱上一轮月光",
                    "冷风中的夕阳",
                    "谁都无法阻挡",
                ]),
            ),
            Section(
                title="主歌 Verse 2",
                lines=lyric_only([
                    "我也曾以为",
                    "远方会替你把答案藏好",
                    "可脚步越响",
                    "越像是在逃",
                    "镜子里的你",
                    "一边点头一边摇头",
                    "一边把梦握紧",
                    "一边把梦颠倒",
                    "我也曾把明天",
                    "写进一张 to do list",
                    "一半被划掉",
                    "另一半安稳睡在回收箱",
                    "一边在挣扎",
                    "一边躺下",
                    "一边对身边的自己说",
                    "你也曾把远方",
                    "折进一张旧车票",
                    "夜里反复看　看　看",
                    "他将会带你去向何方",
                    "一边怕被辜负一边放不下",
                    "笑话自己是如此狡猾",
                    "可心跳很诚实",
                    "它替你回答",
                    "替你转弯",
                    "替你收拾行囊",
                    "那就走吧",
                    "别问归途有多长",
                ]),
            ),
            Section(title="副歌 Chorus 2", same_as="同副歌 Chorus"),
        ],
    )


# ========================================================================= #
# 10 血色的蔷薇 — G / no BPM
# ========================================================================= #
def song_qiangwei() -> Song:
    # 2026-09 谱：1=G，无 BPM。6m=Em，4=C，5=D，1=G。
    # 谱面 2 未标 m，且对照写 2:A，按 A 大三（不是调内 Am）。
    loop = bars("Em", "C A")
    pre = bars("C", "A", "Em", "D")
    ch = bars("Em", "G", "C", "A")
    verse_groups = [
        ("嚼不烂所谓的错对", "咽不下廉价的喜悲", "影子拖着无尽的疲惫", "全都是累赘"),
        ("我把刀口向内一推", "心脏毫无防备", "掌心攥死　无解的迷宫", "种下一团带刺的泪"),
        ("谁决定黑白", "决定幸福被贱卖", "好戏还没开场", "怎么能往下坠"),
        ("我在原地徘徊", "捡起地上的同类", "掌心渗出红色的绝对", "没烧透的是我的体会"),
    ]
    verse_lines: list[Line] = []
    for a, b, c, d in verse_groups:
        verse_lines.append(L(loop, a))
        verse_lines.append(L("", b))
        verse_lines.append(L(loop, c))
        verse_lines.append(L("", d))
    return Song(
        title="出去玩！ — 血色的蔷薇",
        meta="原调 G Major  ·  4/4",
        key_label="G Major",
        degrees=DEG_G,
        extensions=[
            "前奏 / 主歌 / Solo：Em | C – A",
            "预副：C – A – Em – D；末 C – D",
            "副歌：Em – G – C – A",
            "借用：A（2 级大三和弦）",
        ],
        sections=[
            Section(title="前奏 Intro", lines=[L(loop), L(loop)], note="重复一遍"),
            Section(title="主歌 Verse 1", lines=verse_lines),
            Section(
                title="预副歌 Pre-Chorus",
                lines=[L(pre), L(pre), L(bars("C", "D"))],
            ),
            Section(
                title="副歌 Chorus 1",
                lines=[
                    L(ch, "血色的蔷薇"),
                    L("", "站立着枯萎"),
                    L("", "不需要安慰"),
                    L(ch, "血色的蔷薇"),
                    L("", "学不会下跪"),
                    L("", "骄傲地粉碎"),
                ],
            ),
            Section(
                title="独奏 Solo",
                lines=[L(loop), L(loop)],
                note="同前奏进行，共 12 小节（此两行重复三遍）",
            ),
            Section(title="主歌 Verse 2", same_as="同主歌 Verse 1"),
            Section(title="预副歌 Pre-Chorus 2", same_as="同预副歌 Pre-Chorus"),
            Section(
                title="副歌 Chorus 2",
                same_as="同副歌 Chorus 1",
                note="进行四遍",
            ),
            Section(
                title="尾奏 Outro",
                lines=[L(loop), L(bars("Em"))],
                note="前奏进行三遍后停在 Em",
            ),
        ],
    )


# density 以 Word 实测单页为准（2026-09-29 逐首核对）
SONGS = [
    ("不是眼泪.docx", song_yanlei, "compact"),
    ("我对我自己说.docx", song_ziji, "dense"),
    ("绽放.docx", song_zhanfang, "compact"),
    ("燃烧的篝火请你告诉我.docx", song_gouhuo, "compact"),
    ("空凤梨罐头.docx", song_guantou, "compact"),
    ("我想.docx", song_woxiang, "compact"),
    ("骤雨.docx", song_zhouyu, "normal"),
    ("小鱼.docx", song_xiaoyu, "compact"),
    ("血色的蔷薇.docx", song_qiangwei, "compact"),
]


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    # 安全：禁止写进源目录
    assert OUT.resolve() != (ROOT / "和弦谱").resolve()
    only = set(sys.argv[1:])
    for zh, factory, density in SONGS:
        if zh in HAND_EDITED:
            print(f"SKIP {zh}  (hand-edited, never overwrite)")
            continue
        if only and zh not in only:
            continue
        path = render(factory(), OUT / zh, density=density)
        print(f"OK {path}  [{density}]")
