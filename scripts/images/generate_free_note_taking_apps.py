#!/usr/bin/env python3
"""
Feature image generator: Free note-taking apps in 2026
Output : static/img/free-note-taking-apps.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Encryption and platform values come from the comparison table in
content/productivity/free-note-taking-apps.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar, logo_path,
)

ACCENT = "#6366f1"   # Productivity silo, indigo

c = Canvas()

panel_table(c, ACCENT, "Capture, encryption, and platforms",
    ["App", "Encryption", "Platforms"],
    [
        ("Google Keep",    [("Standard", NEUTRAL),   ("All", GOOD)]),
        ("Apple Notes",    [("iCloud", NEUTRAL),     ("Apple only", WARN)]),
        ("Standard Notes", [("End to end", GOOD),    ("All, Linux", GOOD)]),
        ("Simplenote",     [("Standard", NEUTRAL),   ("All, Linux", GOOD)]),
        ("Notion free",    [("Standard", NEUTRAL),   ("All", GOOD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "GK",
    logo     = logo_path("google-keep.png"),
    name     = "Google Keep",
    tagline  = "Best for fast capture",
    note     = "Quick notes and lists inside a Google account",
)

card_grid(c, [
    ("#eab308", "AN", "Apple Notes",    "Text, scans, handwriting, and sharing on Apple", logo_path("apple-notes.png")),
    ("#22c55e", "SN", "Standard Notes", "Encryption first, plain-text notes", logo_path("standard-notes.png")),
    ("#3b82f6", "Si", "Simplenote",     "Plain text and Markdown, nothing more", logo_path("simplenote.png")),
    ("#64748b", "N",  "Notion free",    "Databases and project notes, with more setup", logo_path("notion.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free note-taking apps in 2026",
    subtitle = "Google Keep  ·  Apple Notes  ·  Standard Notes  ·  Simplenote  ·  Notion",
)

c.save("free-note-taking-apps.webp")
