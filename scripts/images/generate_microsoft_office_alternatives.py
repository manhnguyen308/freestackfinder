#!/usr/bin/env python3
"""
Feature image generator: Free Microsoft Office alternatives in 2026
Output : static/img/microsoft-office-alternatives.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Replaces a 1200x800 stock photo. Suite facts come from
content/productivity/microsoft-office-alternatives.md. The same-DOCX check it
mentions is the article's own September 2026 evidence, scoped to this page.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, WARN,
    panel_list, note_card, card_featured, card_grid, card_bar,
)

ACCENT = "#6366f1"   # Productivity silo, indigo

c = Canvas()

x0, y0, x1, y1 = panel_list(c, "Office suites and their main limit", [
    ("#3b82f6", "Google Workspace",   "Browser collaboration",        "Up to 15 GB",      WARN),
    ("#22c55e", "LibreOffice",        "Offline desktop files",        "No live co-editing", WARN),
    ("#06b6d4", "OnlyOffice Desktop", "Heavy .docx compatibility",    "Fewer add-ons",    WARN),
    ("#ef4444", "WPS Office",         "Office-like interface",        "Upsell prompts",   WARN),
], section="Best for and main limit")

# Article: "first test whether a free suite preserves" your files
note_card(c, ACCENT, x0, y0 + 28 + 4 * 62, x1, y1, "Before switching",
          "Test one real file before moving your work")

card_featured(
    c, ACCENT,
    initials = "GD",
    name     = "Google Docs, Sheets, Slides",
    tagline  = "Best for collaboration",
    note     = "Free in a browser, with up to 15 GB of storage shared across Google services",
)

card_grid(c, [
    ("#22c55e", "LO", "LibreOffice",    "Full offline suite with no subscription"),
    ("#06b6d4", "OO", "OnlyOffice",     "Compare it when .docx fidelity matters"),
    ("#ef4444", "WP", "WPS Office",     "Ribbon layout with subscription offers"),
    ("#64748b", "DX", "Same DOCX test", "One file opened in three editors, September 2026"),
])

card_bar(
    c, ACCENT,
    title    = "Free Microsoft Office alternatives in 2026",
    subtitle = "Google Docs  ·  LibreOffice  ·  OnlyOffice  ·  WPS Office",
)

c.save("microsoft-office-alternatives.webp")
