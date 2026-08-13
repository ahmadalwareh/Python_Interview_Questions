#!/usr/bin/env python3
"""Syntax-check the ```python fenced code blocks in a Markdown file.

Used by the "README checks" GitHub Actions workflow. It only reads the target
Markdown file (default: Que_README.md) — it imports nothing from the app.

A block is SKIPPED (not an error) when it is intentionally not valid Python 3:
  * it is tagged with a marker comment: ``# ci-skip``
  * it demonstrates legacy syntax (mentions "Python 2")
  * it is a REPL transcript (contains ``>>> ``), which interleaves output

Everything else must compile. Top-level ``await`` is allowed so async
examples don't trip the check. Exits non-zero if any block fails.
"""

from __future__ import annotations

import ast
import pathlib
import sys
import textwrap
import warnings

PYTHON_LANGS = {"python", "py", "python3"}
SKIP_MARKERS = ("# ci-skip", "# ci: skip", "python 2")


def extract_blocks(text: str) -> list[tuple[int, str, str]]:
    """Return (start_line, lang, body) for every fenced code block."""
    blocks: list[tuple[int, str, str]] = []
    lang: str | None = None
    start = 0
    buf: list[str] = []
    for i, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if lang is None:
            if stripped.startswith("```"):
                lang = stripped[3:].strip().lower()
                start = i
                buf = []
        else:
            if stripped.startswith("```"):
                blocks.append((start, lang, "\n".join(buf)))
                lang = None
            else:
                buf.append(line)
    return blocks


def should_skip(body: str) -> bool:
    low = body.lower()
    if any(marker in low for marker in SKIP_MARKERS):
        return True
    if ">>> " in body:  # REPL transcript with interleaved output
        return True
    return False


def main(argv: list[str]) -> int:
    path = pathlib.Path(argv[1] if len(argv) > 1 else "Que_README.md")
    text = path.read_text(encoding="utf-8")

    checked = skipped = 0
    failures: list[tuple[int, SyntaxError]] = []
    for start, lang, body in extract_blocks(text):
        if lang not in PYTHON_LANGS:
            continue
        if should_skip(body):
            skipped += 1
            continue
        checked += 1
        # Dedent so code fences nested under list items don't look "over-indented".
        source = textwrap.dedent(body)
        try:
            with warnings.catch_warnings():
                warnings.simplefilter(
                    "ignore"
                )  # ignore intentional SyntaxWarnings (e.g. `is` with a literal)
                compile(source, f"{path}:block@{start}", "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
        except SyntaxError as exc:
            failures.append((start, exc))

    print(f"python blocks: checked={checked} skipped={skipped} failed={len(failures)}")
    for start, exc in failures:
        # GitHub Actions error annotation
        print(
            f"::error file={path},line={start}::SyntaxError near block: {exc.msg} (line {exc.lineno} of block)"
        )
        print(f"  - {path}:~{start}: {exc.msg}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

