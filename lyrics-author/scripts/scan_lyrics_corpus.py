#!/usr/bin/env python3
"""Scan e:/coding/歌词 for changes vs corpus-state.json. Exit 0 always; prints JSON summary."""
from __future__ import annotations

import glob
import json
import os
import sys
from datetime import datetime, timezone

CORPUS = os.environ.get("LYRICS_CORPUS", r"e:/coding/歌词")
STATE = os.environ.get(
    "LYRICS_CORPUS_STATE",
    os.path.join(os.path.dirname(__file__), "..", "corpus-state.json"),
)


def iso_mtime(path: str) -> str:
    st = os.stat(path)
    return datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).isoformat()


def main() -> None:
    exts = ("*.docx", "*.md", "*.txt")
    paths: list[str] = []
    for pat in exts:
        paths.extend(glob.glob(os.path.join(CORPUS, pat)))
    paths = sorted(set(paths))

    current = []
    for p in paths:
        current.append({"name": os.path.basename(p), "mtimeIso": iso_mtime(p), "path": p})

    prev: dict | None = None
    if os.path.isfile(STATE):
        with open(STATE, encoding="utf-8") as f:
            prev = json.load(f)

    changed = True
    if prev and prev.get("files"):
        old = {(x["name"], x.get("mtimeIso")) for x in prev["files"]}
        new = {(x["name"], x["mtimeIso"]) for x in current}
        changed = old != new or len(current) != len(prev["files"])

    out = {
        "corpusRoot": CORPUS.replace("\\", "/"),
        "changed": changed,
        "fileCount": len(current),
        "files": [{"name": x["name"], "mtimeIso": x["mtimeIso"]} for x in current],
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if changed and prev:
        print(
            "\n# ACTION: corpus changed — re-read all text files in corpus, update STYLE_REFERENCE.md, then refresh corpus-state.json with scan_lyrics_corpus.py --write",
            file=sys.stderr,
        )


if __name__ == "__main__":
    if "--write" in sys.argv:
        paths = []
        for pat in ("*.docx", "*.md", "*.txt"):
            paths.extend(glob.glob(os.path.join(CORPUS, pat)))
        paths = sorted(set(paths))
        files = [{"name": os.path.basename(p), "mtimeIso": iso_mtime(p)} for p in paths]
        state = {
            "corpusRoot": CORPUS.replace("\\", "/"),
            "lastScannedIso": datetime.now(timezone.utc).isoformat(),
            "files": files,
        }
        os.makedirs(os.path.dirname(STATE), exist_ok=True)
        with open(STATE, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        print(json.dumps({"written": STATE, "files": len(files)}, ensure_ascii=False))
    else:
        main()
