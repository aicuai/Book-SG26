#!/usr/bin/env python3
"""Validate all .ipynb and .json files in the repository.

Shared between GitHub Actions (.github/workflows/qa.yml) and the local
Windows QA runner (qa/qa_local.ps1). Uses stdlib only.

Exit code: 0 if all files parse, 1 if any fail.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

EXCLUDE_DIRS = {".git", "node_modules", ".ipynb_checkpoints", "__pycache__", ".claude"}
TARGET_SUFFIXES = {".ipynb", ".json"}


def iter_targets(root: Path):
    """Yield tracked .ipynb/.json files. Falls back to rglob if git is unavailable."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=root,
            capture_output=True,
            check=True,
        )
        files = [
            root / Path(p.decode("utf-8"))
            for p in out.stdout.split(b"\0")
            if p
        ]
        for p in sorted(files):
            if p.is_file() and p.suffix in TARGET_SUFFIXES:
                yield p
        return
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix not in TARGET_SUFFIXES:
            continue
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        yield p


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    failed: list[tuple[str, str]] = []
    total = 0

    for f in iter_targets(root):
        total += 1
        rel = f.relative_to(root).as_posix()
        try:
            with f.open(encoding="utf-8") as fp:
                json.load(fp)
            print(f"ok   : {rel}")
        except (json.JSONDecodeError, UnicodeDecodeError, OSError) as e:
            msg = f"{type(e).__name__}: {e}"
            print(f"FAIL : {rel}  ({msg})")
            failed.append((rel, msg))

    print()
    print(f"Checked {total} file(s).")
    if failed:
        print(f"{len(failed)} file(s) failed JSON validation:")
        for rel, msg in failed:
            print(f"  - {rel}: {msg}")
        return 1
    print("All JSON files valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
