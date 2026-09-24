#!/usr/bin/env python3
"""
Feature image generator: Free Grammarly alternatives in 2026
Output : static/img/grammarly-alternatives.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Replaces a 1200x901 stock photo. Word limits and style depth come from the
comparison table in content/productivity/grammarly-alternatives.md.
Grammarly is a declined affiliate program: the image carries no call to action.
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

panel_table(c, ACCENT, "Free limits and editing depth",
    ["Tool", "Free limit", "Style help"],
    [
        ("LanguageTool",   [("Length cap varies", WARN), ("Basic", NEUTRAL)]),
        ("ProWritingAid",  [("500 words", WARN),         ("Deep", GOOD)]),
        ("Hemingway",      [("Unlimited web", GOOD),     ("Readability", NEUTRAL)]),
        ("Google Docs",    [("Unlimited", GOOD),         ("Basic", NEUTRAL)]),
        ("Grammarly Free", [("Unlimited", GOOD),         ("Limited", WARN)]),
    ])

card_featured(
    c, ACCENT,
    initials = "LT",
    logo     = logo_path("languagetool.png"),
    name     = "LanguageTool",
    tagline  = "Best for multilingual writers",
    note     = "Browser grammar and style checks in more than 30 languages",
)

card_grid(c, [
    ("#22c55e", "PW", "ProWritingAid",    "Structural feedback, 500 words a session", logo_path("prowritingaid.png")),
    ("#eab308", "He", "Hemingway Editor", "Readability checks for cutting clutter", logo_path("hemingway.png")),
    ("#3b82f6", "GD", "Google Docs",      "Built-in checks for existing Docs users", logo_path("google-docs.png")),
    ("#64748b", "Gr", "Grammarly Free",   "Spelling, grammar, and a tone display", logo_path("grammarly.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free Grammarly alternatives in 2026",
    subtitle = "LanguageTool  ·  ProWritingAid  ·  Hemingway Editor  ·  Google Docs",
)

c.save("grammarly-alternatives.webp")
