#!/usr/bin/env python3
"""
FreeStackFinder — Front Matter Validator

Run before publishing batches to catch common front matter mistakes.

Usage:
    python scripts/validate_front_matter.py

Scans articles under content/<silo>/ (not utility pages), plus the card copy
that renders beside them: hub descriptions and "Where to start" boxes, the
homepage collections and tenets, and the Start Here cards.
Exits with code 1 if errors are found, 0 if clean or warnings only.

Descriptions double as card excerpts, so sameness checks warn (never fail)
when a description repeats one of the retired card formulas:
  - a first word shared with another article in the same silo
  - an imperative opener ("Choose...", "Find...", "Build...")
  - a "[Tool], [Tool], and [Tool]..." list as the opening
  - a trailing list of criteria or uses ("by X, Y, and Z", "for X, Y, or Z")
  - announcement or chatbot phrasing ("Here's what...", "This guide...")
  - an unsourced majority claim ("Most people...")
  - an opening that repeats the title the card already shows
  - a sentence that nearly repeats one on another card in the same silo
See "Sitewide sameness" in website-content-humanizer.md.
"""

import html
import re
import sys
from datetime import datetime, timezone
from itertools import combinations
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
IMPERATIVE_DESC_OPENERS = {
    "Choose", "Find", "Compare", "See", "Pick", "Build", "Get", "Discover", "Explore",
    "Learn", "Browse", "Try", "Use", "Start", "Check", "Read", "Meet", "Save", "Switch",
}
LIST_MARKERS = (" by ", " compared for ", " for ", " with ", " cover ", " covers ")
LIST_MIN_ITEMS = 3
LIST_MAX_ITEM_WORDS = 8        # criteria and uses are noun phrases; anything longer is a clause
OPENING_LIST_MAX_WORDS = 4     # tool names at the start of a "[Tool], [Tool], and [Tool]" opener
TITLE_ECHO_WORDS = 3
RE_DESC_FILLER = re.compile(
    r"\b(here'?s what|here is what|here are the|this guide|in this (?:guide|article|post)"
    r"|we compare|everything you need|read on|find out|let['’]s)\b",
    re.IGNORECASE,
)
RE_VAGUE_MAJORITY = re.compile(
    r"\b(?:most|many) (?:people|users|readers|teams|businesses|creators)\b", re.IGNORECASE
)

# Near-duplicate sentences between cards in the same silo
NEAR_DUP_RUN_CONTENT_WORDS = 3   # a shared run with this many content words repeats a phrase
NEAR_DUP_OVERLAP = 0.4           # share of content words two sentences have in common (Jaccard)
NEAR_DUP_MIN_CONTENT_WORDS = 4   # shorter sentences are too small to compare by overlap
STOPWORDS = frozenset(
    "a an the and or but nor of to in on at for with by from as is are was were be been it its "
    "this that these those than then so if no not can each every one only more most all any "
    "your you their there here into up out over per via while which who what when where how "
    "just also still both between".split()
)

# Other places where cards render side by side
HOME_TEMPLATE = REPO_ROOT / "layouts" / "index.html"
START_HERE = CONTENT_DIR / "start-here.md"
HOME_GRID_SIZE = 6   # "first 6" in the Featured and Latest sections of layouts/index.html
RE_HOME_COLLECTION = re.compile(r'"title"\s+"([^"]+)"\s+"intro"\s+"([^"]+)"')
RE_HOME_TENET = re.compile(r'<strong>([^<]+)</strong><p>([^<]+)</p>')
RE_START_HERE_CARD = re.compile(
    r'<p class="collection-title">([^<]+)</p>\s*<p class="collection-intro">([^<]+)</p>'
)
RE_HUB_PICK = re.compile(r'<li><a href="[^"]+">([^<]+)</a>:\s*([^<]+)</li>')


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


def sentences(desc):
    return re.split(r'(?<=[.!?])\s+', desc.strip())


def is_list(items, max_words):
    """True when comma-separated items form one list of LIST_MIN_ITEMS or more."""
    count = len(items)
    # Without an Oxford comma, "sync and privacy" is still two items
    if items and not re.match(r'(and|or)\s', items[-1]) and re.search(r'\s(and|or)\s', items[-1]):
        count += 1
    if count < LIST_MIN_ITEMS:
        return False
    # "and"/"or" before the final item means the list already ended and a clause follows
    if any(re.match(r'(and|or)\s', item) for item in items[:-1]):
        return False
    return all(len(re.sub(r'^(and|or)\s+', '', item).split()) <= max_words for item in items)


def criteria_tail(desc):
    """Return a trailing 'by X, Y, and Z' style list in the last sentence, or None."""
    last_sentence = sentences(desc)[-1]
    lowered = last_sentence.lower()
    # Try every marker position from the right, so a "for" inside a list item
    # does not hide the "by" that starts the list
    positions = sorted(
        ((m.start(), marker) for marker in LIST_MARKERS
         for m in re.finditer(re.escape(marker), lowered)),
        reverse=True,
    )
    for idx, marker in positions:
        tail = last_sentence[idx + len(marker):].rstrip(" .!?")
        items = [item.strip() for item in tail.split(",") if item.strip()]
        if is_list(items, LIST_MAX_ITEM_WORDS):
            return f"{marker.strip()} {tail}"
    return None


def looks_like_name(text):
    """Product names start with a capital or digit, or read like a domain (diagrams.net)."""
    first = text.split()[0] if text.split() else ""
    return bool(first) and (first[0].isupper() or first[0].isdigit() or "." in first)


def opening_list(desc):
    """Return the '[Tool], [Tool], and [Tool]' run that opens the description, or None."""
    segments = [s.strip() for s in sentences(desc)[0].split(",")]
    for end in range(LIST_MIN_ITEMS - 1, len(segments)):
        if not re.match(r'(and|or)\s+\S', segments[end]):
            continue
        names = segments[:end]
        # "Inkscape covers logos, icons, and SVG work" lists objects, not tools
        if all(1 <= len(n.split()) <= OPENING_LIST_MAX_WORDS and looks_like_name(n) for n in names):
            return ", ".join(names + [segments[end]])
        return None
    return None


def sentence_tokens(sentence):
    return [t.strip(".'") for t in re.findall(r"[a-z0-9][a-z0-9.'+-]*", sentence.lower())]


def content_words(tokens):
    return {t for t in tokens if t not in STOPWORDS and len(t) > 1}


def shared_run(a, b):
    """Longest run of consecutive tokens common to a and b, ranked by content words."""
    best, best_score = [], (0, 0)
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                run = a[i - cur[j]:i]
                score = (len(content_words(run)), cur[j])
                if score > best_score:
                    best, best_score = run, score
        prev = cur
    return best


def near_duplicate(sentences_a, sentences_b):
    """Compare every sentence of one card with every sentence of another.

    Returns (shared phrase or None, sentence from a, sentence from b), or None.
    """
    for x in sentences_a:
        for y in sentences_b:
            tx, ty = sentence_tokens(x), sentence_tokens(y)
            run = shared_run(tx, ty)
            if len(content_words(run)) >= NEAR_DUP_RUN_CONTENT_WORDS:
                return " ".join(run), x, y
            cx, cy = content_words(tx), content_words(ty)
            if min(len(cx), len(cy)) >= NEAR_DUP_MIN_CONTENT_WORDS and \
                    len(cx & cy) / len(cx | cy) >= NEAR_DUP_OVERLAP:
                return None, x, y
    return None


def group_warnings(cards, where, first_word=True, near_dup=True, pair_ok=None):
    """Sameness warnings for cards that render side by side, keyed by source path.

    Each card is a dict with path, ref (how other warnings name it), prefix
    (how its own warnings start), and text.
    """
    found = {}

    if first_word:
        by_word = {}
        for card in cards:
            word = description_first_word(card["text"])
            if word:
                by_word.setdefault(word, []).append(card)
        for word, group in by_word.items():
            for card in group:
                peers = [c["ref"] for c in group if c is not card]
                if peers:
                    found.setdefault(card["path"], []).append(
                        f'{card["prefix"]} opens with "{word}", same as {", ".join(peers)} {where} — vary the first word'
                    )

    if near_dup:
        for a, b in combinations(cards, 2):
            if pair_ok and not pair_ok(a, b):
                continue
            match = near_duplicate(sentences(a["text"]), sentences(b["text"]))
            if not match:
                continue
            phrase, sentence_a, sentence_b = match
            for card, other, theirs in ((a, b, sentence_b), (b, a, sentence_a)):
                if phrase:
                    msg = f'shares "{phrase}" with {other["ref"]} {where} — cards shown together should not repeat a phrase'
                else:
                    short = theirs if len(theirs) <= 70 else theirs[:67].rstrip() + "..."
                    msg = f'nearly repeats a sentence in {other["ref"]} ("{short}") {where} — rewrite one of them'
                found.setdefault(card["path"], []).append(f'{card["prefix"]} {msg}')

    return found


def article_card(path, silo, fields):
    weight = str(fields.get("weight") or "0").strip('"')
    return {
        "path": path, "ref": path.name, "prefix": "description:", "silo": silo,
        "text": clean_description(fields),
        "title": str(fields.get("title") or "").strip('"'),
        "date": str(fields.get("date") or "").strip('"'),
        "weight": float(weight) if re.fullmatch(r'-?\d+(\.\d+)?', weight) else 0.0,
        "draft": str(fields.get("draft", "false")).strip('"').lower() == "true",
    }


def homepage_grids(articles):
    """Approximate the homepage Featured (weight) and Latest (date) grids.

    Mirrors layouts/index.html: Hugo's default order breaks ties (weight
    ascending, date descending, title), then ByParam "weight" or ByDate,
    reversed, first HOME_GRID_SIZE.
    """
    def date_ordinal(a):
        try:
            return datetime.strptime(a["date"], "%Y-%m-%d").date().toordinal()
        except ValueError:
            return 0

    live = [a for a in articles if not a["draft"] and 0 < date_ordinal(a) <= BUILD_DATE.toordinal()]
    default = sorted(live, key=lambda a: (a["weight"], -date_ordinal(a), a["title"].lower()))
    featured = sorted((a for a in default if a["weight"] > 0), key=lambda a: a["weight"])[::-1]
    latest = sorted(default, key=date_ordinal)[::-1]
    return [
        ("in the homepage Featured grid", featured[:HOME_GRID_SIZE]),
        ("in the homepage Latest list", latest[:HOME_GRID_SIZE]),
    ]


def copy_card(path, title, text):
    title, text = html.unescape(title).strip(), html.unescape(text).strip()
    return {"path": path, "ref": f'"{title}"', "prefix": f'card "{title}":', "title": title, "text": text}


def handwritten_groups():
    """Card copy written directly into templates and pages rather than front matter."""
    groups = []

    try:
        home = HOME_TEMPLATE.read_text(encoding="utf-8")
    except OSError:
        home = ""
    collections = [copy_card(HOME_TEMPLATE, t, i) for t, i in RE_HOME_COLLECTION.findall(home)]
    start = home.find("tenets-grid")
    tenet_block = home[start:home.find("</section>", start)] if start != -1 else ""
    tenets = [copy_card(HOME_TEMPLATE, t, p) for t, p in RE_HOME_TENET.findall(tenet_block)]
    groups += [("in the homepage collections", collections), ("in the homepage tenets strip", tenets)]

    try:
        start_here = START_HERE.read_text(encoding="utf-8")
    except OSError:
        start_here = ""
    groups.append(("on the Start Here page",
                   [copy_card(START_HERE, t, i) for t, i in RE_START_HERE_CARD.findall(start_here)]))

    for silo in SILOS:
        hub = CONTENT_DIR / silo / "_index.md"
        try:
            picks = RE_HUB_PICK.findall(hub.read_text(encoding="utf-8"))
        except OSError:
            continue
        groups.append((f'in the {silo} hub\'s "Where to start" box', [copy_card(hub, t, i) for t, i in picks]))

    return [(where, cards) for where, cards in groups if cards]


def copy_formula_warnings(card):
    """Run the single-description checks on hand-written card copy."""
    text = card["text"][:1].upper() + card["text"][1:]   # list items start lowercase
    return [w.replace("description:", card["prefix"], 1)
            for w in description_formula_warnings(text, card["title"])]


def hub_description_warnings():
    """Formula checks on each hub description, plus the intro paragraph printed right below it."""
    found = {}
    for silo in SILOS:
        hub = CONTENT_DIR / silo / "_index.md"
        try:
            text = hub.read_text(encoding="utf-8")
        except OSError:
            continue
        fields = parse_front_matter(text) or {}
        desc = clean_description(fields)
        ws = description_formula_warnings(desc, str(fields.get("title") or "").strip('"'))

        body = text.split("---", 2)[2] if text.count("---") >= 2 else ""
        intro = html.unescape(body.split("<div", 1)[0]).strip()
        match = near_duplicate(sentences(desc), sentences(intro)) if desc and intro else None
        if match:
            phrase, _, theirs = match
            detail = f'shares "{phrase}" with' if phrase else f'nearly repeats ("{theirs[:67]}...") in'
            ws.append(f"description: {detail} the intro paragraph shown right below it — rewrite one of them")
        if ws:
            found[hub] = ws
    return found


def description_formula_warnings(desc, title):
    """Warnings for a single description that repeats a retired card formula."""
    warnings = []
    words = desc.split()
    if not words:
        return warnings

    opener = words[0].strip('.,;:!?"()')
    if opener in IMPERATIVE_DESC_OPENERS:
        warnings.append(
            f'description: starts with "{opener}", an imperative card opener — lead with a fact specific to this page'
        )

    run = opening_list(desc)
    if run:
        warnings.append(
            f'description: opens with a list of tools ("{run}") — lead with the one fact that separates them'
        )

    tail = criteria_tail(desc)
    if tail:
        warnings.append(
            f'description: ends with a criteria list ("{tail}") — name the one limit that decides this page'
        )

    filler = RE_DESC_FILLER.search(desc)
    if filler:
        warnings.append(
            f'description: uses "{filler.group(0)}", announcement or chatbot phrasing — state the fact instead'
        )

    vague = RE_VAGUE_MAJORITY.search(desc)
    if vague:
        warnings.append(
            f'description: claims something about "{vague.group(0)}" without a source — narrow it to what the page shows'
        )

    title_words = [w.strip('.,;:!?"()').lower() for w in str(title or "").strip('"').split()]
    desc_words = [w.strip('.,;:!?"()').lower() for w in words]
    if len(title_words) >= TITLE_ECHO_WORDS and desc_words[:TITLE_ECHO_WORDS] == title_words[:TITLE_ECHO_WORDS]:
        echo = " ".join(words[:TITLE_ECHO_WORDS])
        warnings.append(
            f'description: repeats the title\'s opening ("{echo}") — the card already shows the title'
        )

    return warnings


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

        warnings.extend(description_formula_warnings(desc_clean, fields.get("title")))

    return errors, warnings


def main():
    results = {}   # path -> [errors, warnings], in print order
    seen_slugs = {}
    articles = []
    total_files = 0

    for silo in SILOS:
        silo_path = CONTENT_DIR / silo
        if not silo_path.is_dir():
            continue

        for md_path in sorted(silo_path.glob("*.md")):
            if md_path.name == "_index.md":
                continue

            errors, warnings = check_file(md_path)

            # Duplicate slug detection
            text = md_path.read_text(encoding="utf-8")
            sm = re.search(r'^slug:\s*"?([^"\n]+)"?', text, re.MULTILINE)
            if sm:
                slug = sm.group(1).strip()
                if slug in seen_slugs:
                    errors.append(f"Duplicate slug '{slug}' — also in {seen_slugs[slug].name}")
                else:
                    seen_slugs[slug] = md_path

            results[md_path] = [errors, warnings]
            total_files += 1
            fields = parse_front_matter(text)
            if fields:
                articles.append(article_card(md_path, silo, fields))

    def add(found):
        for path, ws in found.items():
            results.setdefault(path, [[], []])[1].extend(ws)

    # Cards that render side by side. Hub grids and "More from" sections are
    # one silo; the homepage mixes silos; search results can pair any two.
    for silo in SILOS:
        add(group_warnings([a for a in articles if a["silo"] == silo], f"on the {silo} hub"))
    for where, grid in homepage_grids(articles):
        add(group_warnings(grid, where, near_dup=False))   # repeats are caught by the passes around it
    add(group_warnings(articles, "across silos (search results, homepage grids)", first_word=False,
                       pair_ok=lambda a, b: a["silo"] != b["silo"]))

    # Card copy written outside article front matter
    copy_cards = 0
    for where, cards in handwritten_groups():
        copy_cards += len(cards)
        for card in cards:
            add({card["path"]: copy_formula_warnings(card)})
        add(group_warnings(cards, where))
    add(hub_description_warnings())

    total_errors = total_warnings = files_with_issues = 0
    for path, (errors, warnings) in results.items():
        if errors or warnings:
            files_with_issues += 1
            print(f"\n{path.relative_to(REPO_ROOT)}")
            for e in errors:
                print(f"  ERROR   {e}")
            for w in warnings:
                print(f"  WARN    {w}")
        total_errors += len(errors)
        total_warnings += len(warnings)

    print(f"\n{'─' * 52}")
    print(f"Checked : {total_files} articles across {len(SILOS)} silos")
    print(f"Cards   : {copy_cards} hand-written cards and {len(SILOS)} hub descriptions")
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
