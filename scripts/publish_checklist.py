#!/usr/bin/env python3
"""
FreeStackFinder — Pre-Publish Checklist

Prints the publish checklist. When a silo and slug are given, auto-verifies
the file-level items and prints only the remaining manual steps.

Usage:
    python3 scripts/publish_checklist.py
    python3 scripts/publish_checklist.py <silo> <slug>

Examples:
    python3 scripts/publish_checklist.py
    python3 scripts/publish_checklist.py cloud free-ai-email-tools
    python3 scripts/publish_checklist.py productivity free-calendar-app
"""

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FIELDS = ["title", "description", "date", "lastmod", "slug", "categories", "image"]
RE_QUOTED_DATE = re.compile(r'^"(\d{4}-\d{2}-\d{2})"$')
RE_IMAGE_PATH   = re.compile(r'^"/img/[^"]+\.webp"$')
BUILD_DATE = datetime.now(timezone.utc).date()

MANUAL_STEPS = [
    "Internal links: 2–5 relevant links from new article to existing cluster articles",
    "Backlinks: update 1–2 related existing articles to link back to the new article",
    "Run QA: python3 scripts/run_quality_checks.py --with-counts  (must pass 3/3)",
    "Hugo build: hugo --minify — confirm public/<silo>/<slug>/index.html exists",
    "Git: git add + git commit + git push",
]


def parse_front_matter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fm: dict = {}
    current_key = None
    list_buf: list = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r'^([a-zA-Z_][a-zA-Z0-9_-]*):\s*(.*)', line)
        if m:
            if current_key and list_buf:
                fm[current_key] = list_buf
                list_buf = []
            current_key = m.group(1)
            val = m.group(2).strip()
            if val:
                fm[current_key] = val
            # else: value may follow as a list
        elif re.match(r'^[ \t]+-\s+', line) and current_key:
            list_buf.append(line.strip().lstrip("- ").strip())
            fm[current_key] = list_buf
    return fm


def check_article(silo: str, slug: str) -> tuple[list, list]:
    """Return (passed, failed) lists of check messages."""
    passed: list = []
    failed: list = []

    content_path = REPO_ROOT / "content" / silo / f"{slug}.md"
    if not content_path.exists():
        failed.append(f"Content file not found: content/{silo}/{slug}.md")
        return passed, failed
    passed.append(f"Content file found: content/{silo}/{slug}.md")

    fm = parse_front_matter(content_path)
    if not fm:
        failed.append("Front matter could not be parsed (missing opening ---)")
        return passed, failed

    # Required fields
    missing = [f for f in REQUIRED_FIELDS if f not in fm]
    if missing:
        failed.append(f"Missing required fields: {', '.join(missing)}")
    else:
        passed.append("All required front matter fields present")

    # draft: false
    draft_val = fm.get("draft", "").strip().lower().strip('"').strip("'")
    if draft_val == "false":
        passed.append("draft: false — article will be published")
    else:
        failed.append(f"draft is not false (got: {fm.get('draft', 'missing')})")

    # date and lastmod not in the future
    for field in ("date", "lastmod"):
        raw = fm.get(field, "")
        m = RE_QUOTED_DATE.match(raw)
        if m:
            article_date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
            if article_date > BUILD_DATE:
                failed.append(f"{field} is in the future ({m.group(1)}) — Hugo will exclude this article")
            else:
                passed.append(f"{field}: {m.group(1)} — valid")
        else:
            failed.append(f"{field} is not a quoted YYYY-MM-DD string (got: {raw!r})")

    # image field
    img_val = fm.get("image", "")
    if RE_IMAGE_PATH.match(img_val):
        passed.append(f"image field format valid: {img_val}")
        # Derive filename from the image path value
        img_filename = img_val.strip('"').lstrip("/img/")
        img_path = REPO_ROOT / "static" / "img" / img_filename
        if img_path.exists():
            size_kb = img_path.stat().st_size / 1024
            if size_kb <= 200:
                passed.append(f"Feature image exists and is {size_kb:.1f} KB (under 200 KB limit)")
            else:
                failed.append(f"Feature image is {size_kb:.1f} KB — exceeds 200 KB limit")
        else:
            failed.append(f"Feature image not found: static/img/{img_filename}")
    else:
        failed.append(f"image field format invalid (expected \"/img/<name>.webp\", got: {img_val!r})")

    return passed, failed


def print_full_checklist() -> None:
    print()
    print("  Pre-Publish Checklist")
    print("  ─────────────────────")
    items = [
        "Content file exists in correct silo: content/<silo>/<slug>.md",
        "Front matter: all required fields present (title, description, date, lastmod, slug, categories, image)",
        "draft: false",
        "date and lastmod: today's date, quoted YYYY-MM-DD, not in the future",
        "image: points to static/img/<slug>.webp which exists and is under 200 KB",
        "Internal links: 2–5 contextual links from new article to existing cluster articles",
        "Backlinks: 1–2 related existing articles updated to link back to the new article",
        "QA: python3 scripts/run_quality_checks.py --with-counts passes 3/3",
        "Hugo: hugo --minify — 0 errors, public/<silo>/<slug>/index.html confirmed",
        "Git: git add + git commit (clean message) + git push",
    ]
    for i, item in enumerate(items, 1):
        print(f"  {i:>2}. {item}")
    print()


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print_full_checklist()
        return

    if len(args) != 2:
        print("Usage: python3 scripts/publish_checklist.py [<silo> <slug>]", file=sys.stderr)
        sys.exit(1)

    silo, slug = args[0].lower(), args[1].lower()
    passed, failed = check_article(silo, slug)

    print()
    print(f"  Checklist: {silo}/{slug}")
    print(f"  {'─' * (len(silo) + len(slug) + 12)}")
    print()

    for msg in passed:
        print(f"  ✓  {msg}")
    for msg in failed:
        print(f"  ✗  {msg}")

    if MANUAL_STEPS:
        print()
        print("  Remaining manual steps:")
        for step in MANUAL_STEPS:
            print(f"     •  {step}")
    print()

    if failed:
        print(f"  {len(passed)} auto-checks passed · {len(failed)} failed — fix issues before publishing")
        sys.exit(1)
    else:
        print(f"  {len(passed)} auto-checks passed · ready for manual steps above")


if __name__ == "__main__":
    main()
