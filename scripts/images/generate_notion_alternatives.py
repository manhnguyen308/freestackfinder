#!/usr/bin/env python3
"""
Feature image generator: Free Notion alternatives in 2026
Output : static/img/notion-alternatives.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Storage and offline values come from the comparison table in
content/productivity/notion-alternatives.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#6366f1"   # Productivity silo, indigo

c = Canvas()

panel_table(c, ACCENT, "Where your notes live",
    ["Tool", "Storage", "Offline"],
    [
        ("Obsidian",    [("Local files", GOOD),   ("Full", GOOD)]),
        ("Logseq",      [("Local files", GOOD),   ("Full", GOOD)]),
        ("Anytype",     [("Local, sync", GOOD),   ("Full", GOOD)]),
        ("Coda",        [("Cloud", NEUTRAL),      ("No", BAD)]),
        ("Joplin",      [("Your cloud", GOOD),    ("Full", GOOD)]),
        ("Notion free", [("Cloud", NEUTRAL),      ("Downloads", WARN)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Ob",
    name     = "Obsidian",
    tagline  = "Best for a personal knowledge base",
    note     = "Local Markdown files, offline access, and a large plugin library",
)

card_grid(c, [
    ("#22c55e", "Lq", "Logseq",  "Open-source outliner for linked notes"),
    ("#3b82f6", "Ay", "Anytype", "Block editor closer to Notion, encrypted sync"),
    ("#ec4899", "Co", "Coda",    "Docs and wikis for document-centric teams"),
    ("#06b6d4", "Jo", "Joplin",  "Open-source notes synced to your own cloud"),
])

card_bar(
    c, ACCENT,
    title    = "Free Notion alternatives in 2026",
    subtitle = "Obsidian  ·  Logseq  ·  Anytype  ·  Coda  ·  Joplin",
)

c.save("notion-alternatives.webp")
