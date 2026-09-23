#!/usr/bin/env python3
"""
Feature image generator: Free web analytics tools in 2026
Output : static/img/free-web-analytics.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Data type and cookieless values come from the comparison table in
content/business/free-web-analytics.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, INFO, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

panel_table(c, ACCENT, "What each tool measures",
    ["Tool", "Data", "Cookieless"],
    [
        ("Google Analytics 4", [("Full traffic", INFO),  ("No", BAD)]),
        ("Search Console",     [("Search only", NEUTRAL), ("Yes", GOOD)]),
        ("Microsoft Clarity",  [("Heatmaps", NEUTRAL),   ("No", BAD)]),
        ("Umami",              [("Core traffic", INFO),  ("Yes", GOOD)]),
        ("Matomo",             [("Detailed", INFO),      ("Optional", WARN)]),
    ])

card_featured(
    c, ACCENT,
    initials = "G4",
    name     = "Google Analytics 4",
    tagline  = "Traffic, acquisition, and conversions",
    note     = "No software cost, but consent and privacy work in many regions",
)

card_grid(c, [
    ("#3b82f6", "SC", "Search Console",    "Google Search queries, clicks, and CTR"),
    ("#06b6d4", "Cl", "Microsoft Clarity", "Heatmaps and session replays beside GA4"),
    ("#8b5cf6", "Um", "Umami",             "Privacy-friendly analytics you host"),
    ("#eab308", "Ma", "Matomo",            "Detailed self-hosted reports, paid plugins"),
])

card_bar(
    c, ACCENT,
    title    = "Free web analytics tools in 2026",
    subtitle = "Google Analytics 4  ·  Search Console  ·  Clarity  ·  Umami  ·  Matomo",
)

c.save("free-web-analytics.webp")
