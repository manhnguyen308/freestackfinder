#!/usr/bin/env python3
"""
FreeStackFinder — Feature Image Inventory Checker

Cross-checks article image: front matter fields against files in static/img/.
Reports missing images (hard errors) and unreferenced files (warnings).

Usage:
    python3 scripts/check_feature_images.py

Scans articles under content/<silo>/ only (not utility pages).
Exits with code 1 if any referenced image is missing from disk, 0 otherwise.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
STATIC_IMG_DIR = REPO_ROOT / "static" / "img"

SILOS = ["business", "cloud", "creative", "productivity", "security", "video"]

RE_IMAGE = re.compile(r'^image:\s*"?(/[^"\n]+)"?', re.MULTILINE)

# Files in static/img/ that are known non-article assets; report as info, not error
KNOWN_NON_ARTICLE = {
    "default-article.jpg",   # fallback placeholder
}


def get_image_ref(text):
    """Return the image path string from front matter, or None."""
    m = RE_IMAGE.search(text)
    return m.group(1).strip() if m else None


def img_path_to_file(ref):
    """Convert /img/file.webp → STATIC_IMG_DIR/file.webp"""
    if ref.startswith("/img/"):
        return STATIC_IMG_DIR / ref[len("/img/"):]
    return STATIC_IMG_DIR / ref.lstrip("/")


def main():
    referenced = set()   # filenames (not full paths) referenced by articles
    errors = []
    warnings = []
    articles_checked = 0
    articles_missing_image_field = []

    for silo in SILOS:
        silo_path = CONTENT_DIR / silo
        if not silo_path.is_dir():
            continue

        for md_path in sorted(silo_path.glob("*.md")):
            if md_path.name == "_index.md":
                continue

            articles_checked += 1
            try:
                text = md_path.read_text(encoding="utf-8")
            except OSError as exc:
                errors.append((md_path, f"Cannot read: {exc}"))
                continue

            ref = get_image_ref(text)
            rel = md_path.relative_to(REPO_ROOT)

            if not ref:
                articles_missing_image_field.append(str(rel))
                continue

            # Check extension
            if not ref.lower().endswith(".webp"):
                warnings.append(f"  WARN    {rel}\n          image: {ref} — expected .webp extension")

            # Check file exists
            img_file = img_path_to_file(ref)
            if img_file.exists():
                referenced.add(img_file.name)
            else:
                errors.append((rel, f"image: {ref} — file not found at static{ref}"))

    # Missing image field
    for path_str in articles_missing_image_field:
        warnings.append(f"  WARN    {path_str}\n          no image: field in front matter")

    # Orphan detection — files in static/img/ not referenced by any silo article
    all_img_files = sorted(STATIC_IMG_DIR.glob("*"))
    orphans = [f for f in all_img_files if f.name not in referenced]

    # Print errors
    if errors:
        print("\nERRORS — referenced images missing from disk:")
        for path, msg in errors:
            print(f"\n  {path}")
            print(f"          {msg}")

    # Print warnings
    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(w)

    # Print orphan report
    if orphans:
        print(f"\nPOSSIBLE ORPHANS — {len(orphans)} file(s) in static/img/ not referenced by any silo article:")
        for f in orphans:
            tag = " (known non-article asset)" if f.name in KNOWN_NON_ARTICLE else ""
            print(f"  {f.name}{tag}")
        print("  Note: do not delete without confirming these are not used by templates or utility pages.")

    # Summary
    print(f"\n{'─' * 52}")
    print(f"Articles checked : {articles_checked}")
    print(f"Images verified  : {len(referenced)}")
    print(f"Missing (errors) : {len(errors)}")
    print(f"Warnings         : {len(warnings)}")
    print(f"Possible orphans : {len(orphans)}")

    if errors:
        print("\nFAILED — fix missing images before publishing")
        sys.exit(1)
    elif warnings or orphans:
        print("\nPASSED with warnings")
    else:
        print("\nPASSED — image inventory clean")


if __name__ == "__main__":
    main()
