#!/usr/bin/env python3
"""Check j.aicu.ai shortlinks defined in qa/shortlinks.yml.

For each entry, verifies:
  1. Reachability (HTTP < 400 after following redirects)
  2. Destination match (final URL contains `expect_contains`, if set)

Entries marked `bot_protected: true` accept 403/503 as reachable. Amazon and
similar sites block CI runners by IP, and a false QA failure files a noisy
issue. The shortlink itself is still exercised — only the destination's
refusal to answer a robot is tolerated.

Shared between GitHub Actions (.github/workflows/qa.yml) and the local
Windows QA runner (qa/qa_local.ps1). Requires PyYAML.

Exit code: 0 if all entries pass, 1 if any fail.
"""

from __future__ import annotations

import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

TIMEOUT_SECONDS = 30
USER_AGENT = "Book-SG26-QA/1.0"
REGISTRY = Path(__file__).resolve().parent / "shortlinks.yml"


def check(url: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        method="GET",
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            return resp.status, resp.geturl()
    except urllib.error.HTTPError as e:
        return e.code, getattr(e, "url", url) or url
    except Exception as e:
        return 0, f"({type(e).__name__}: {e})"


def main() -> int:
    if not REGISTRY.exists():
        print(f"ERROR: registry not found: {REGISTRY}", file=sys.stderr)
        return 2

    with REGISTRY.open(encoding="utf-8") as fp:
        data = yaml.safe_load(fp) or {}
    entries = data.get("shortlinks") or []
    if not entries:
        print("ERROR: no entries in qa/shortlinks.yml", file=sys.stderr)
        return 2

    failed: list[tuple[str, str]] = []
    for entry in entries:
        code = entry.get("code", "?")
        url = entry["url"]
        expect = (entry.get("expect_contains") or "").strip()
        description = entry.get("description", "")
        bot_protected = bool(entry.get("bot_protected"))

        status, dest = check(url)
        reachable = 200 <= status < 400
        if not reachable and bot_protected and status in (403, 429, 503):
            reachable = True
            expect = ""  # destination refused to answer; nothing to match against
        destination_ok = (expect.lower() in dest.lower()) if (reachable and expect) else reachable

        if reachable and destination_ok:
            marker = "ok  "
            note = "  [bot-blocked; reachability only]" if status in (403, 429, 503) else ""
        elif reachable and not destination_ok:
            marker = "FAIL"
            note = f"  [expected substring '{expect}' not in final URL]"
            failed.append((code, f"destination mismatch (got {dest}, expected substring '{expect}')"))
        else:
            marker = "FAIL"
            note = f"  [HTTP {status}]"
            failed.append((code, f"unreachable (HTTP {status})"))

        print(f"{marker} : {code:8s} {url}  -> HTTP {status}  (final: {dest}){note}")
        if description:
            print(f"         description: {description}")

    print()
    print(f"Checked {len(entries)} shortlink(s).")
    if failed:
        print(f"{len(failed)} shortlink(s) failed:")
        for code, reason in failed:
            print(f"  - {code}: {reason}")
        return 1
    print("All shortlinks reachable and resolve to expected destinations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
