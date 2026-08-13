#!/usr/bin/env python3
"""Verify the Table of Contents in a Markdown file stays in sync with headings.

Scoped to a single Markdown file (default: Que_README.md). For every
``## N- ...`` question heading it computes the GitHub heading anchor and checks
that:

  * the heading has exactly one matching TOC entry, and
  * every TOC entry points at an existing heading (no stale links),
  * in the same order, with no duplicate anchors.

Anchor generation mirrors GitHub / github-slugger: lowercase, drop characters
that are not word/space/hyphen, then turn spaces into hyphens (no collapsing).
"""

from __future__ import annotations

import pathlib
import re
import sys

HEADING_RE = re.compile(r"^## (\d+-\s.*\S)\s*$")
TOC_ENTRY_RE = re.compile(r"^- \[.*]\(#([^)]+)\)\s*$")
TOC_HEADING = "## Table of Contents"


def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def main(argv: list[str]) -> int:
    path = pathlib.Path(argv[1] if len(argv) > 1 else "Que_README.md")
    lines = path.read_text(encoding="utf-8").splitlines()

    # Collect question headings (in order) and their anchors.
    headings: list[str] = []
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            headings.append(slugify(m.group(1)))

    # Collect TOC anchors from within the "Table of Contents" section only.
    toc: list[str] = []
    in_toc = False
    for line in lines:
        if line.strip() == TOC_HEADING:
            in_toc = True
            continue
        if in_toc and line.startswith("## "):
            break
        if in_toc:
            m = TOC_ENTRY_RE.match(line)
            if m:
                toc.append(m.group(1))

    errors: list[str] = []
    if not toc:
        errors.append("No Table of Contents entries found.")

    dupes = sorted({a for a in toc if toc.count(a) > 1})
    if dupes:
        errors.append(f"Duplicate TOC anchors: {dupes}")

    missing = [a for a in headings if a not in toc]  # heading with no TOC entry
    stale = [a for a in toc if a not in headings]  # TOC entry with no heading
    if missing:
        errors.append(f"{len(missing)} heading(s) missing from TOC, e.g. #{missing[0]}")
    if stale:
        errors.append(f"{len(stale)} stale TOC link(s) with no heading, e.g. #{stale[0]}")
    if not missing and not stale and toc != headings:
        errors.append("TOC order does not match heading order.")

    print(f"headings={len(headings)} toc_entries={len(toc)} problems={len(errors)}")
    for e in errors:
        print(f"::error file={path}::{e}")
        print(f"  - {e}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

