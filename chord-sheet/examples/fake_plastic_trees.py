"""Example song spec — Radiohead, Fake Plastic Trees.

Run from the skill folder:
    python examples/fake_plastic_trees.py
Produces `Project/和弦谱/fake-plastic-trees.docx`.

This is the reference for how to shape a `Song` spec: swap the data, keep the
structure, and the fixed-partition template renders it identically.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from chord_sheet import Line, Section, Song, render  # noqa: E402


def _verse(title: str, chords: list[str], lyrics: list[str], note: str) -> Section:
    return Section(
        title=title,
        lines=[Line(chord=c, lyric=l) for c, l in zip(chords, lyrics)],
        note=note,
    )


VERSE_CHORDS = [
    "A                    Asus4  Dmaj9/F#",
    "Dmaj9/F#                 E6    Dsus2",
    "              A    Dsus2",
    "A                      Asus4  Dmaj9/F#",
    "Dmaj9/F#              E6     Dsus2",
    "        A       Dsus2",
]


SONG = Song(
    title="Radiohead — Fake Plastic Trees",
    meta="原调 A Major  ·  74 BPM  ·  4/4",
    key_label="A Major",
    degrees=[
        ("1", "A", "A – C# – E"),
        ("2", "Bm", "B – D – F#"),
        ("3", "C#m", "C# – E – G#"),
        ("4", "D", "D – F# – A"),
        ("5", "E", "E – G# – B"),
        ("6", "F#m", "F# – A – C#"),
        ("7", "G#dim", "G# – B – D"),
    ],
    extensions=[
        "Asus4 · Dsus2 · Dmaj9/F#",
        "E6 · Bm7add11 · Amaj7",
    ],
    sections=[
        Section(
            title="前奏 Intro",
            lines=[
                Line(chord="A          Asus4      Dmaj9/F#   Dmaj9/F#"),
                Line(chord="E6         Dsus2      A          Dsus2"),
            ],
            note="重复一遍",
        ),
        _verse(
            "主歌 Verse 1",
            VERSE_CHORDS,
            [
                "Her green plastic watering can",
                "For her fake chinese rubber plant",
                "In the fake plastic earth",
                "That she bought from a rubber man",
                " In a town full of rubber plans",
                "To get rid of itself",
            ],
            "此段落重复两遍",
        ),
        Section(
            title="副歌 Chorus 1",
            lines=[
                Line(chord="             Bm7add11           A", lyric="It wears her out   It wears her out"),
                Line(chord="             Bm7add11           A      Asus4", lyric="It wears her out   It wears her out"),
            ],
        ),
        _verse(
            "主歌 Verse 2",
            VERSE_CHORDS,
            [
                "She lives with a broken man",
                "A cracked polystyrene man",
                "Who just crumbles and burns",
                "He used to do surgery",
                "For girls in the eighties",
                "But gravity always wins",
            ],
            "此段落重复两遍",
        ),
        Section(
            title="副歌 Chorus 2",
            lines=[
                Line(chord="             Bm7add11          A", lyric="And it wears him out  It wears him out"),
                Line(chord="             Bm7add11   Asus4   A", lyric="And it wears him out  It wears him out"),
            ],
        ),
        _verse(
            "主歌 Verse 3",
            VERSE_CHORDS,
            [
                "She looks like the real thing",
                "She tastes like the real thing",
                "My fake plastic love",
                "But I can't help the feeling",
                "I could blow through the ceiling",
                "If I just turn and run",
            ],
            "此段落重复两遍",
        ),
        Section(
            title="副歌 Chorus 3",
            lines=[
                Line(chord="                Bm7add11          A", lyric="And it wears me out   It wears me out"),
                Line(chord="             Bm7add11             A    Amaj7", lyric="It wears me out   It wears me out"),
            ],
        ),
        Section(
            title="尾奏 Outro",
            lines=[
                Line(chord="              Bm7add11", lyric="And if I could be who you wanted"),
                Line(chord="           A", lyric="If I could be who you wanted"),
                Line(chord="    E6      Bm7add11          A    E6", lyric="All the time      All the time"),
                Line(chord="    Bm7add11  A    E6    Bm7add11    A"),
            ],
            note="末行重复至结束",
        ),
    ],
)


if __name__ == "__main__":
    # examples -> chord-sheet -> skills -> .cursor -> coding (repo root)
    out = Path(__file__).resolve().parents[4] / "Project" / "和弦谱" / "fake-plastic-trees.docx"
    written = render(SONG, out, density="normal")
    print(f"Wrote {written}")
