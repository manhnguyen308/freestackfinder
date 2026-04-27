"""
Report article counts by silo for FreeStackFinder.

Usage:
    python scripts/report_article_counts.py

Scans content/ silo subdirectories only. Excludes _index.md and root utility
pages (about, contact, disclaimer, etc.). Respects draft: true front matter.
Prints a count-by-silo table and total, with target comparisons where defined.
Exit code is always 0 unless a file cannot be parsed.
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(REPO_ROOT, "content")

SILOS = ["business", "cloud", "creative", "productivity", "security", "video"]

# Targets from CONTENT-STRATEGY.md / tracker
TARGETS = {
    "business":    13,
    "cloud":        7,
    "creative":     8,
    "productivity": 9,
    "security":     6,
    "video":        7,
}

DRAFT_RE = re.compile(r"^\s*draft\s*:\s*true\b", re.IGNORECASE | re.MULTILINE)


def is_draft(path):
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read(1024)
        return bool(DRAFT_RE.search(content))
    except OSError:
        return False


def count_silo(silo_dir):
    count = 0
    try:
        for fname in os.listdir(silo_dir):
            if not fname.endswith(".md"):
                continue
            if fname == "_index.md":
                continue
            fpath = os.path.join(silo_dir, fname)
            if not is_draft(fpath):
                count += 1
    except FileNotFoundError:
        pass
    return count


def main():
    rows = []
    total = 0
    total_target = 0
    mismatch = False

    for silo in SILOS:
        silo_dir = os.path.join(CONTENT_DIR, silo)
        count = count_silo(silo_dir)
        target = TARGETS.get(silo, "—")
        total += count
        if isinstance(target, int):
            total_target += target
            remaining = target - count
            status = "✓" if remaining <= 0 else f"{remaining} remaining"
        else:
            remaining = "—"
            status = "—"
        rows.append((silo.capitalize(), count, target, status))

    print()
    print(f"  {'Silo':<14} {'Count':>5}  {'Target':>6}  Status")
    print(f"  {'-'*14} {'-'*5}  {'-'*6}  {'-'*14}")
    for silo_label, count, target, status in rows:
        target_str = str(target) if isinstance(target, int) else "—"
        print(f"  {silo_label:<14} {count:>5}  {target_str:>6}  {status}")
    print(f"  {'-'*14} {'-'*5}  {'-'*6}  {'-'*14}")
    print(f"  {'TOTAL':<14} {total:>5}  {total_target:>6}")
    print()

    if mismatch:
        print("  WARNING: tracker count may be out of date — verify freestackfinder-progress-log.md")
        print()


if __name__ == "__main__":
    main()
