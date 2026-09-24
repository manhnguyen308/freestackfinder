#!/usr/bin/env python3
"""
FreeStackFinder — Front Matter Validator

Run before publishing batches to catch common front matter mistakes.

Usage:
    python scripts/validate_front_matter.py

Scans articles under content/<silo>/ only (not utility pages).
Exits with code 1 if errors are found, 0 if clean or warnings only.

Descriptions double as card excerpts, so three sameness checks warn (never
fail) when a description repeats a formula: a first word shared with another
article in the same silo, a retired imperative opener, or a trailing
"by X, Y, and Z" (or "compared for X, Y, and Z") criteria list. See "Sitewide sameness" in
website-content-humanizer.md.
"""

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
STATIC_IMG_DIR = REPO_ROOT / "static" / "img"

SILOS = ["business", "cloud", "creative", "productivity", "security", "video"]

REQUIRED_FIELDS = ["title", "description", "date", "lastmod", "slug", "categories", "image"]
BANNED_KEYS = ["featured", "faqs"]

RE_TOP_KEY = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_-]*):\s*(.*)')
RE_LIST_ITEM = re.compile(r'^[ \t]+-\s+')
RE_QUOTED_DATE = re.compile(r'^"(\d{4}-\d{2}-\d{2})"$')
RE_BARE_DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
RE_IMAGE_PATH = re.compile(r'^"/img/[^"]+\.webp"$')

BUILD_DATE = datetime.now(timezone.utc).date()

# Card-description sameness (warnings only)
RETIRED_DESC_OPENERS = {"Choose", "Find", "Compare", "See", "Pick"}
CRITERIA_MARKERS = (" by ", " compared for ")   # "compared for" is the same formula worded differently
CRITERIA_MIN_ITEMS = 3
CRITERIA_MAX_ITEM_WORDS = 8   # criteria are noun phrases; anything longer is a clause


def parse_front_matter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    fm_lines = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        fm_lines.append(line)

    fields = {}
    current_key = None
    list_buf = []
    in_list = False

    for line in fm_lines:
        if RE_LIST_ITEM.match(line):
            if in_list:
                list_buf.append(line.strip().lstrip("- ").strip().strip('"'))
            continue

        m = RE_TOP_KEY.match(line)
        if m:
            if current_key and in_list:
                fields[current_key] = list_buf[:]
            key, val = m.group(1), m.group(2).strip()
            current_key = key
            if val == "":
                in_list = True
                list_buf = []
                fields[key] = None
            else:
                in_list = False
                list_buf = []
                fields[key] = val

    if current_key and in_list:
        fields[current_key] = list_buf[:]

    return fields


def clean_description(fields):
    """Return the description without surrounding quotes, or "" if absent."""
    desc = fields.get("description") if fields else None
    return str(desc).strip('"') if desc else ""


def description_first_word(desc):
    """First word, case-folded, without surrounding punctuation or quotes."""
    words = desc.split()
    return words[0].strip('.,;:!?"()').lower() if words else ""


def criteria_tail(desc):
    """Return the trailing 'by X, Y, and Z' list in the last sentence, or None."""
    last_sentence = re.split(r'(?<=[.!?])\s+', desc.strip())[-1]
    lowered = last_sentence.lower()
    idx, marker = max((lowered.rfind(m), m) for m in CRITERIA_MARKERS)
    if idx == -1:
        return None
    tail = last_sentence[idx + len(marker):].rstrip(" .!?")
    items = [item.strip() for item in tail.split(",") if item.strip()]
    # Without an Oxford comma, "sync and privacy" is still two items
    count = len(items)
    if items and not re.match(r'(and|or)\s', items[-1]) and re.search(r'\s(and|or)\s', items[-1]):
        count += 1
    if count < CRITERIA_MIN_ITEMS:
        return None
    # "and"/"or" before the final item means the list already ended and a clause follows
    if any(re.match(r'(and|or)\s', item) for item in items[:-1]):
        return None
    if any(len(re.sub(r'^(and|or)\s+', '', item).split()) > CRITERIA_MAX_ITEM_WORDS for item in items):
        return None
    return f"{marker.strip()} {tail}"


def check_file(path):
    errors = []
    warnings = []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"Cannot read file: {exc}"], []

    fields = parse_front_matter(text)
    if fields is None:
        return ["No front matter found or missing opening --- delimiter"], []

    # Required fields
    for field in REQUIRED_FIELDS:
        val = fields.get(field)
        if val is None or val == "" or val == []:
            errors.append(f"Missing required field: {field}")

    # Banned keys
    for key in BANNED_KEYS:
        if key in fields:
            errors.append(f"Banned key present: '{key}'")

    # noindex on silo article
    noindex_val = str(fields.get("noindex", "false")).lower().strip('"')
    if noindex_val == "true":
        warnings.append("noindex: true on a silo article — only utility pages should be noindexed")

    # draft: true
    draft_val = str(fields.get("draft", "false")).lower().strip('"')
    if draft_val == "true":
        warnings.append("draft: true — article will not be published by Hugo")

    # Date fields
    for df in ("date", "lastmod"):
        raw = fields.get(df)
        if not raw:
            continue
        raw = str(raw)
        if RE_QUOTED_DATE.match(raw):
            date_str = raw.strip('"')
            try:
                parsed = datetime.strptime(date_str, "%Y-%m-%d").date()
                if parsed > BUILD_DATE:
                    if df == "date":
                        errors.append(
                            f"{df}: future date {date_str} (UTC build date is {BUILD_DATE}; Hugo excludes future-dated content by default)"
                        )
                    else:
                        errors.append(f"{df}: future date {date_str} (UTC build date is {BUILD_DATE})")
            except ValueError:
                errors.append(f"{df}: unparseable date value '{date_str}'")
        elif RE_BARE_DATE.match(raw):
            warnings.append(f'{df}: unquoted date {raw} — use "{raw}" format')
        else:
            errors.append(f"{df}: malformed value '{raw}' — expected \"YYYY-MM-DD\"")

    # Image checks
    img_raw = fields.get("image")
    if img_raw and img_raw != "":
        img_raw = str(img_raw)
        if not RE_IMAGE_PATH.match(img_raw):
            errors.append(f"image: unexpected format '{img_raw}' — expected \"/img/filename.webp\"")
        else:
            rel_path = img_raw.strip('"')           # /img/file.webp
            img_file = STATIC_IMG_DIR / rel_path[len("/img/"):]
            if not img_file.exists():
                errors.append(f"image: file not found — static{rel_path}")

    # Description
    desc = fields.get("description", "")
    if desc:
        desc_clean = str(desc).strip('"')
        if desc_clean == "":
            errors.append("description: empty string")
        elif len(desc_clean) < 50:
            warnings.append(f"description: very short ({len(desc_clean)} chars) — aim for 150–160")
        elif len(desc_clean) > 165:
            warnings.append(f"description: long ({len(desc_clean)} chars) — aim for 150–160")

        if desc_clean:
            opener = desc_clean.split()[0].strip('.,;:!?"()')
            if opener in RETIRED_DESC_OPENERS:
                warnings.append(
                    f'description: starts with "{opener}", the retired card formula — lead with a fact specific to this page'
                )
            tail = criteria_tail(desc_clean)
            if tail:
                warnings.append(
                    f'description: ends with a criteria list ("{tail}") — name the one limit that decides this page'
                )

    return errors, warnings


def main():
    total_files = 0
    total_errors = 0
    total_warnings = 0
    files_with_issues = 0
    seen_slugs = {}

    for silo in SILOS:
        silo_path = CONTENT_DIR / silo
        if not silo_path.is_dir():
            continue

        articles = [p for p in sorted(silo_path.glob("*.md")) if p.name != "_index.md"]

        # Group the silo's descriptions by first word; cards in one hub sit side by side
        opener_of = {}
        opener_groups = {}
        for md_path in articles:
            try:
                fields = parse_front_matter(md_path.read_text(encoding="utf-8"))
            except OSError:
                continue
            word = description_first_word(clean_description(fields))
            if word:
                opener_of[md_path] = word
                opener_groups.setdefault(word, []).append(md_path)

        for md_path in articles:
            total_files += 1
            errors, warnings = check_file(md_path)

            word = opener_of.get(md_path)
            peers = [p.name for p in opener_groups.get(word, []) if p != md_path]
            if peers:
                warnings.append(
                    f'description: opens with "{word}", same as {", ".join(peers)} in {silo}/ — vary the first word within a silo'
                )

            # Duplicate slug detection
            text = md_path.read_text(encoding="utf-8")
            sm = re.search(r'^slug:\s*"?([^"\n]+)"?', text, re.MULTILINE)
            if sm:
                slug = sm.group(1).strip()
                if slug in seen_slugs:
                    errors.append(f"Duplicate slug '{slug}' — also in {seen_slugs[slug].name}")
                else:
                    seen_slugs[slug] = md_path

            if errors or warnings:
                files_with_issues += 1
                rel = md_path.relative_to(REPO_ROOT)
                print(f"\n{rel}")
                for e in errors:
                    print(f"  ERROR   {e}")
                for w in warnings:
                    print(f"  WARN    {w}")

            total_errors += len(errors)
            total_warnings += len(warnings)

    print(f"\n{'─' * 52}")
    print(f"Checked : {total_files} articles across {len(SILOS)} silos")
    print(f"Errors  : {total_errors}")
    print(f"Warnings: {total_warnings}")
    print(f"Files   : {files_with_issues} with issues")

    if total_errors > 0:
        print("\nFAILED — fix errors before publishing")
        sys.exit(1)
    elif total_warnings > 0:
        print("\nPASSED with warnings")
    else:
        print("\nPASSED — all articles clean")


if __name__ == "__main__":
    main()
