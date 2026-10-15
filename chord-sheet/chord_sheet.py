"""Chord-sheet generator — fixed-partition A4 Word template.

The layout is fixed by this module. To produce a new chart you only supply a
`Song` spec (title, key reference, sections); positions never need manual
adjustment. See SKILL.md for the workflow and `examples/` for a worked spec.

Usage:
    from chord_sheet import Song, Section, Line, bars, render
    Line(chord=bars("E F#", "B"), lyric="为什么　我的眼里都是泪水")
    render(song, "path/to/output.docx", density="normal")
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


# Near-black: magenta washes out on B&W print; black + bold stays legible.
CHORD_COLOR = RGBColor(0x11, 0x11, 0x11)
NOTE_COLOR = RGBColor(0x55, 0x55, 0x55)


# --------------------------------------------------------------------------- #
# Data model — this is what a song "is" to the template.
# --------------------------------------------------------------------------- #
@dataclass
class Line:
    """One printed row. chord and/or lyric may be empty.

    - chord + lyric  -> chord printed above the lyric (verse/chorus)
    - chord only     -> instrumental line (intro/interlude/outro)
    - lyric only     -> lyric with no chord change
    """

    chord: str = ""
    lyric: str = ""


@dataclass
class Section:
    title: str                       # e.g. "主歌 Verse 1"
    lines: list[Line] = field(default_factory=list)
    note: str = ""                   # short note, e.g. "此段落重复两遍"
    # 重复段落：只写「（同主歌 Verse 1）」一行加粗正文，不再粘贴歌词。
    # 渲染顺序：标题 → same_as 行 → lines → note。
    same_as: str = ""
    # 默认不换栏：正文先灌满左栏，溢出再进右栏（见 render / noBalancedColumns）。
    # 仅在极少数需要强制右栏起笔时才设 True。
    column_break_before: bool = False


def bars(*cells: str, slots: int | None = None) -> str:
    """Format chord bars as `| E   F#  | B       |`.

    Each argument is one bar; chords inside a bar are whitespace-separated and
    fall on equal subdivisions (2 chords = half-bar each). Use "-" for a
    held/empty bar. Cell width is uniform within the line so bar lines stack.
    Keep ≤ 4 single-chord bars or ≤ 2 two-chord bars per line for column width.
    """
    split = [c.split() if c.strip() else ["-"] for c in cells]
    n = slots or max(len(s) for s in split)
    width = max(4, max(len(ch) for s in split for ch in s) + 1)
    out = []
    for s in split:
        padded = s + [""] * (n - len(s))
        out.append("| " + "".join(ch.ljust(width) for ch in padded))
    return "".join(out) + "|"


@dataclass
class Song:
    title: str                       # "Artist — Title"
    meta: str                        # "原调 A Major  ·  74 BPM  ·  4/4"
    key_label: str                   # "和弦" heading suffix, e.g. "A Major"
    degrees: list[tuple[str, str, str]]   # (级数, 和弦, 组成音) for 1..7
    extensions: list[str]            # extra/extended chords used, free lines
    sections: list[Section]


# --------------------------------------------------------------------------- #
# Density presets — the single-page knob. Everything scales from here.
# --------------------------------------------------------------------------- #
@dataclass
class Style:
    body: float          # lyric font pt
    chord: float         # chord font pt (> body)
    heading: float       # section heading pt (> body)
    header: float        # header/meta + key-reference font pt
    note: float          # note font pt
    title: float         # song title pt
    lyric_after: float   # space after a lyric line (within a section)
    chord_after: float   # space after a chord line (glued to lyric)
    section_before: float  # space before a section heading (gap between sections)
    section_after: float
    block_after: float   # space after the header block
    line_spacing: float  # in-paragraph line spacing (multiple)


PRESETS: dict[str, Style] = {
    # 2026-09-29 用户验收：重复段落已折叠成「同 X」，正文可以放大；
    # 段名 > 歌词；和弦 > 歌词；段落之间留明显空白。单页仍靠 density 控制。
    "normal": Style(
        body=13, chord=15, heading=14.5, header=10, note=9.5, title=18,
        lyric_after=10, chord_after=0, section_before=18, section_after=4,
        block_after=6, line_spacing=1.05,
    ),
    "compact": Style(
        body=12, chord=14, heading=13.5, header=9.5, note=9, title=16,
        lyric_after=8, chord_after=0, section_before=16, section_after=3,
        block_after=5, line_spacing=1.0,
    ),
    "tight": Style(
        body=11.5, chord=13.5, heading=12.5, header=9, note=8.5, title=15,
        lyric_after=6, chord_after=0, section_before=14, section_after=3,
        block_after=4, line_spacing=1.0,
    ),
    # 最后一档：词量大的歌（如 Rap 段）仍要塞进一页时用
    "dense": Style(
        body=11, chord=13, heading=12, header=9, note=8.5, title=15,
        lyric_after=4, chord_after=0, section_before=11, section_after=2,
        block_after=4, line_spacing=1.0,
    ),
}


# --------------------------------------------------------------------------- #
# Low-level helpers
# --------------------------------------------------------------------------- #
def _set_a4_margins(section) -> None:
    section.page_height = Cm(29.7)
    section.page_width = Cm(21)
    section.top_margin = Cm(1.2)
    section.bottom_margin = Cm(1.2)
    # 1.0cm 左右边距：双栏每栏约 9.1cm，容得下 4 小节单和弦 / 2 小节双和弦的 bar 行
    section.left_margin = Cm(1.0)
    section.right_margin = Cm(1.0)


def _set_columns(section, count: int = 2, space_twips: int = 420) -> None:
    """Two newspaper columns: fill left top→bottom, then right. Do not balance."""
    sect_pr = section._sectPr
    found = sect_pr.xpath("./w:cols")
    cols = found[0] if found else OxmlElement("w:cols")
    if not found:
        sect_pr.append(cols)
    cols.set(qn("w:num"), str(count))
    cols.set(qn("w:space"), str(space_twips))
    # Word默认会把 continuous 双栏左右拉齐；关掉后先灌满左栏再进右栏
    if not sect_pr.xpath("./w:noBalancedColumns"):
        nb = OxmlElement("w:noBalancedColumns")
        sect_pr.append(nb)


def _remove_table_borders(table) -> None:
    tbl_pr = table._tbl.tblPr
    if tbl_pr is None:
        tbl_pr = OxmlElement("w:tblPr")
        table._tbl.insert(0, tbl_pr)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "nil")
        borders.append(e)
    tbl_pr.append(borders)


def _spacing(p, *, before: float, after: float, line_spacing: float) -> None:
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    p.paragraph_format.line_spacing = line_spacing


def _font(run, name: str, size: float, *, bold: bool = False, color: RGBColor | None = None) -> None:
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = color


class _Writer:
    """Bundles the document + active style so section helpers stay tidy."""

    def __init__(self, style: Style) -> None:
        self.doc = Document()
        self.style = style
        _set_a4_margins(self.doc.sections[0])

    # -- generic paragraph ------------------------------------------------- #
    def para(
        self,
        container,
        text: str,
        *,
        font: str = "Arial",
        size: float,
        bold: bool = False,
        color: RGBColor | None = None,
        align=WD_ALIGN_PARAGRAPH.LEFT,
        before: float = 0,
        after: float = 2,
        reuse_first: bool = False,
        keep_with_next: bool = False,
    ) -> None:
        if reuse_first and container.paragraphs and not container.paragraphs[0].runs:
            p = container.paragraphs[0]
        else:
            p = container.add_paragraph()
        p.alignment = align
        _spacing(p, before=before, after=after, line_spacing=self.style.line_spacing)
        if keep_with_next:
            # 段名 / 和弦行 不能孤零零留在栏底，要跟下一行一起走
            p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        _font(run, font, size, bold=bold, color=color)

    # -- header ------------------------------------------------------------ #
    def title_block(self, song: Song) -> None:
        """Title (left) + meta (right) on one fixed row."""
        st = self.style
        table = self.doc.add_table(rows=1, cols=2)
        _remove_table_borders(table)
        table.autofit = False
        table.columns[0].width = Cm(12.0)
        table.columns[1].width = Cm(6.0)
        left, right = table.rows[0].cells
        left.width = Cm(12.0)
        right.width = Cm(6.0)
        left.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.BOTTOM
        right.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.BOTTOM
        self.para(left, song.title, size=st.title, bold=True, after=0, reuse_first=True)
        self.para(right, song.meta, size=st.header, align=WD_ALIGN_PARAGRAPH.RIGHT, after=0, reuse_first=True)
        spacer = self.doc.add_paragraph()
        spacer.paragraph_format.space_after = Pt(st.block_after)

    def key_reference(self, song: Song) -> None:
        """Fixed 3-zone frame: 和弦 (two mini-cols) | 拓展和弦."""
        st = self.style
        table = self.doc.add_table(rows=2, cols=3)
        _remove_table_borders(table)
        table.autofit = False
        table.columns[0].width = Cm(5.8)
        table.columns[1].width = Cm(5.8)
        table.columns[2].width = Cm(5.6)

        title_row = table.rows[0]
        title_row.cells[0].merge(title_row.cells[1])
        self.para(title_row.cells[0], f"和弦 · {song.key_label}", size=st.header, bold=True, after=2, reuse_first=True)
        self.para(title_row.cells[2], "拓展和弦", size=st.header, bold=True, after=2, reuse_first=True)

        left_cell, mid_cell, right_cell = table.rows[1].cells
        if song.degrees:
            half = (len(song.degrees) + 1) // 2  # left gets the extra when odd (e.g. 4/3)
            for i, (deg, chord, notes) in enumerate(song.degrees[:half]):
                text = f"{deg}  {chord}  {notes}".rstrip()
                self.para(left_cell, text, size=st.header, after=2, reuse_first=(i == 0))
            for i, (deg, chord, notes) in enumerate(song.degrees[half:]):
                text = f"{deg}  {chord}  {notes}".rstrip()
                self.para(mid_cell, text, size=st.header, after=2, reuse_first=(i == 0))
        if song.extensions:
            for i, line in enumerate(song.extensions):
                self.para(right_cell, line, font="Courier New", size=st.header, after=2, reuse_first=(i == 0))

        spacer = self.doc.add_paragraph()
        spacer.paragraph_format.space_after = Pt(st.block_after)

    # -- body -------------------------------------------------------------- #
    def column_break(self) -> None:
        p = self.doc.add_paragraph()
        _spacing(p, before=0, after=0, line_spacing=self.style.line_spacing)
        run = p.add_run()
        br = OxmlElement("w:br")
        br.set(qn("w:type"), "column")
        run._r.append(br)

    def section(self, sec: Section, *, first: bool) -> None:
        st = self.style
        self.para(
            self.doc, sec.title, size=st.heading, bold=True,
            before=0 if first else st.section_before, after=st.section_after,
            keep_with_next=True,
        )
        if sec.same_as:
            # 重复段：一行加粗正文「（同主歌 Verse 1）」，不再重复歌词
            self.para(self.doc, f"（{sec.same_as}）", size=st.body, bold=True, after=st.lyric_after)
        for line in sec.lines:
            if line.chord:
                # Bold + near-black: readable after B&W photocopy/print.
                self.para(
                    self.doc, line.chord, font="Courier New", size=st.chord,
                    bold=True, color=CHORD_COLOR, after=st.chord_after,
                    keep_with_next=bool(line.lyric),
                )
            if line.lyric or not line.chord:
                self.para(self.doc, line.lyric, size=st.body, after=st.lyric_after)
        if sec.note:
            self.para(self.doc, sec.note, size=st.note, color=NOTE_COLOR, after=st.section_after)


def render(song: Song, out_path: str | Path, *, density: str = "normal") -> Path:
    """Render `song` to a single-page A4 .docx and return the written path.

    density: "normal" | "compact" | "tight" — shrink to keep one page.
    """
    if density not in PRESETS:
        raise ValueError(f"density must be one of {list(PRESETS)}, got {density!r}")
    w = _Writer(PRESETS[density])

    w.title_block(song)
    w.key_reference(song)

    body = w.doc.add_section(WD_SECTION.CONTINUOUS)
    _set_a4_margins(body)
    _set_columns(body, count=2, space_twips=420)

    first_in_col = True
    for sec in song.sections:
        if sec.column_break_before:
            w.column_break()
            first_in_col = True
        w.section(sec, first=first_in_col)
        first_in_col = False

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        try:
            out_path.unlink()
        except PermissionError:
            out_path = out_path.with_name(out_path.stem + "-new" + out_path.suffix)
    w.doc.save(out_path)
    return out_path
