#!/usr/bin/env python3
"""
Feature image generator: Free Microsoft Office alternatives in 2026
Output : static/img/microsoft-office-alternatives.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Replaces a 1200x800 stock photo. Suite facts come from
content/productivity/microsoft-office-alternatives.md. The same-DOCX check it
mentions is the article's own September 2026 evidence, scoped to this page.
Product icons come from scripts/images/logos/ (sources listed in
logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, WARN,
    panel_list, note_card, card_featured, card_grid, card_bar,
)

ACCENT = "#6366f1"   # Productivity silo, indigo
LOGOS  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logos")


def logo(name):
    return os.path.join(LOGOS, name)


def docx_file(c, cx, cy, r):
    """Plain document with a folded corner, for the test file rather than a product."""
    x0, x1, y0, y1, f = cx - r * 0.8, cx + r * 0.8, cy - r, cy + r, r * 0.55
    c.poly([(x0, y0), (x1 - f, y0), (x1, y0 + f), (x1, y1), (x0, y1)], "#94a3b8")
    c.poly([(x1 - f, y0), (x1 - f, y0 + f), (x1, y0 + f)], "#cbd5e1")
    for i in range(3):
        ly = cy + i * r * 0.3
        c.rect(x0 + r * 0.3, ly, x1 - r * (0.3 + 0.25 * (i == 2)), ly + r * 0.14, "#334155", r=1)

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
    logo     = logo("google-docs.png"),
)

card_grid(c, [
    ("#22c55e", "LO", "LibreOffice",    "Full offline suite with no subscription",
     logo("libreoffice.png")),
    ("#06b6d4", "OO", "OnlyOffice",     "Compare it when .docx fidelity matters",
     logo("onlyoffice.png")),
    ("#ef4444", "WP", "WPS Office",     "Ribbon layout with subscription offers",
     logo("wps-office.png")),
    ("#64748b", "DX", "Same DOCX test", "One file opened in three editors, September 2026",
     docx_file),
])

card_bar(
    c, ACCENT,
    title    = "Free Microsoft Office alternatives in 2026",
    subtitle = "Google Docs  ·  LibreOffice  ·  OnlyOffice  ·  WPS Office",
)

c.save("microsoft-office-alternatives.webp")
