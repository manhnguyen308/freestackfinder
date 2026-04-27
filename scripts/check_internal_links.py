#!/usr/bin/env python3
"""
FreeStackFinder — Internal Link Checker

Validates that internal Markdown links in content files resolve to known Hugo routes.
Skips external URLs, mailto/tel links, anchor-only links, and shortcode syntax.

Usage:
    python3 scripts/check_internal_links.py

Scans all .md files under content/. Builds a route map from front matter and
file paths. Exits with code 1 if broken internal links are found, 0 otherwise.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"

RE_MD_LINK = re.compile(r'\[(?:[^\]]*)\]\(([^)]+)\)')
RE_SLUG = re.compile(r'^slug:\s*"?([^"\n]+)"?', re.MULTILINE)
RE_URL_KEY = re.compile(r'^url:\s*"?([^"\n]+)"?', re.MULTILINE)

# Routes always treated as valid regardless of content files
ALWAYS_VALID = {
    "/",
    "/search/",
    "/start-here/",
    "/about/",
    "/contact/",
    "/disclaimer/",
    "/privacy-policy/",
    "/terms/",
    "/sitemap.xml",
    "/index.json",
}

SILOS = ["business", "cloud", "creative", "productivity", "security", "video"]


def normalize(path):
    """Strip fragment/query, normalize trailing slash. Returns None to skip."""
    if "#" in path:
        path = path[: path.index("#")]
    if "?" in path:
        path = path[: path.index("?")]
    path = path.strip()
    if not path:
        return None
    if not path.startswith("/"):
        return None  # relative — skip
    # Add trailing slash if no file extension in the last segment
    last = path.rsplit("/", 1)[-1]
    if last and "." not in last:
        path = path.rstrip("/") + "/"
    elif not last:
        pass  # already ends with /
    return path


def get_slug(text, stem):
    m = RE_SLUG.search(text)
    return m.group(1).strip() if m else stem


def build_routes():
    routes = set(ALWAYS_VALID)

    for silo in SILOS:
        routes.add(f"/{silo}/")

    for md_path in CONTENT_DIR.rglob("*.md"):
        rel_parts = md_path.relative_to(CONTENT_DIR).parts  # e.g. ('security', 'free-vpn.md')

        try:
            text = md_path.read_text(encoding="utf-8")
        except OSError:
            continue

        # url: override takes full control
        url_m = RE_URL_KEY.search(text)
        if url_m:
            url = url_m.group(1).strip().rstrip("/") + "/"
            if not url.startswith("/"):
                url = "/" + url
            routes.add(url)
            continue

        stem = md_path.stem

        if stem == "_index":
            # Section root — already added via SILOS loop; handle root _index
            if len(rel_parts) == 1:
                routes.add("/")
            continue

        slug = get_slug(text, stem)

        if len(rel_parts) == 1:
            routes.add(f"/{slug}/")
        else:
            section = rel_parts[0]
            routes.add(f"/{section}/{slug}/")

    return routes


def is_internal(raw):
    if not raw:
        return False
    if raw.startswith(("http://", "https://", "mailto:", "tel:", "#", "//")):
        return False
    return raw.startswith("/")


def scan_file(md_path, routes):
    try:
        text = md_path.read_text(encoding="utf-8")
    except OSError:
        return []

    broken = []
    for raw in RE_MD_LINK.findall(text):
        raw = raw.strip()
        if not is_internal(raw):
            continue
        norm = normalize(raw)
        if norm is None:
            continue
        if norm not in routes:
            broken.append((raw, norm))
    return broken


def main():
    routes = build_routes()

    total_files = 0
    total_broken = 0
    files_with_issues = 0

    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        if md_path.name == "_index.md":
            continue

        total_files += 1
        broken = scan_file(md_path, routes)

        if broken:
            files_with_issues += 1
            rel = md_path.relative_to(REPO_ROOT)
            print(f"\n{rel}")
            for raw, norm in broken:
                print(f"  BROKEN  {raw}")
                print(f"          resolved → {norm}")
            total_broken += len(broken)

    print(f"\n{'─' * 52}")
    print(f"Checked : {total_files} files")
    print(f"Routes  : {len(routes)} known")
    print(f"Broken  : {total_broken} internal links")
    print(f"Files   : {files_with_issues} with broken links")

    if total_broken > 0:
        print("\nFAILED — fix broken links before publishing")
        sys.exit(1)
    else:
        print("\nPASSED — all internal links resolve")


if __name__ == "__main__":
    main()
