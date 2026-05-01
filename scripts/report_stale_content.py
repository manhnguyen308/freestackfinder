#!/usr/bin/env python3
"""
Report stale FreeStackFinder articles by lastmod date.

Usage:
    python scripts/report_stale_content.py

Scans content/ silo subdirectories only. Excludes _index.md and draft articles.
Flags articles whose lastmod is 6+ months old for editorial review.
Exit code is always 0 unless a file cannot be parsed.
"""

import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"

SILOS = ["business", "cloud", "creative", "productivity", "security", "video"]

DRAFT_RE = re.compile(r"^\s*draft\s*:\s*true\b", re.IGNORECASE | re.MULTILINE)
LASTMOD_RE = re.compile(r'^\s*lastmod\s*:\s*"?(\d{4}-\d{2}-\d{2})"?', re.IGNORECASE | re.MULTILINE)
STALE_DAYS = 183
TODAY = datetime.now(timezone.utc).date()


def read_front_chunk(path):
    return path.read_text(encoding="utf-8")[:2048]


def is_draft(text):
    return bool(DRAFT_RE.search(text))


def article_lastmod(text):
    match = LASTMOD_RE.search(text)
    if not match:
        return None

    try:
        return datetime.strptime(match.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


def iter_articles():
    for silo in SILOS:
        silo_path = CONTENT_DIR / silo
        if not silo_path.is_dir():
            continue

        for md_path in sorted(silo_path.glob("*.md")):
            if md_path.name == "_index.md":
                continue
            yield silo, md_path


def main():
    stale = []
    missing = []
    checked = 0

    for silo, md_path in iter_articles():
        text = read_front_chunk(md_path)
        if is_draft(text):
            continue

        checked += 1
        lastmod = article_lastmod(text)
        rel = f"{silo}/{md_path.name}"

        if lastmod is None:
            missing.append(rel)
            continue

        age_days = (TODAY - lastmod).days
        if age_days >= STALE_DAYS:
            stale.append((rel, lastmod, age_days))

    stale.sort(key=lambda row: row[1])

    print()
    print("  Stale content report")
    print(f"  Checked: {checked} published articles")
    print(f"  Rule: lastmod {STALE_DAYS}+ days old")
    print()

    if stale:
        print(f"  Articles to review: {len(stale)}")
        print(f"  {'Article':<42} {'Lastmod':<10}  Age")
        print(f"  {'-'*42} {'-'*10}  {'-'*10}")
        for rel, lastmod, age_days in stale:
            print(f"  {rel:<42} {lastmod}  {age_days} days")
        print()
    else:
        print("  No stale articles found.")
        print()

    if missing:
        print("  Articles missing parseable lastmod:")
        for rel in missing:
            print(f"  - {rel}")
        print()


if __name__ == "__main__":
    main()
