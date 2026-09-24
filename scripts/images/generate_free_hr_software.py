#!/usr/bin/env python3
"""
Feature image generator: Free HR software in 2026
Output : static/img/free-hr-software.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Employee limits and self-service values come from the comparison table in
content/business/free-hr-software.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar, logo_path,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

panel_table(c, ACCENT, "Team limits and self-service",
    ["Tool", "Free limit", "Self-service"],
    [
        ("Zoho People",   [("5 employees", WARN), ("Yes", GOOD)]),
        ("OrangeHRM CE",  [("Self-hosted", WARN), ("Yes", GOOD)]),
        ("Homebase",      [("1 location", WARN),  ("No", BAD)]),
        ("Bitrix24",      [("Unlimited", GOOD),   ("Partial", WARN)]),
        ("Google Sheets", [("DIY", NEUTRAL),      ("No", BAD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "ZP",
    logo     = logo_path("zoho-people.png"),
    name     = "Zoho People",
    tagline  = "Best cloud HR records on a free plan",
    note     = "Leave, employee records, and self-service for teams of up to five",
)

card_grid(c, [
    ("#3b82f6", "OH", "OrangeHRM CE",  "Open-source HR system you host yourself", logo_path("orangehrm.png")),
    ("#eab308", "Hb", "Homebase",      "Scheduling and time tracking for one location", logo_path("homebase.png")),
    ("#06b6d4", "Bx", "Bitrix24",      "HR tools inside a wider workspace", logo_path("bitrix24.png")),
    ("#22c55e", "GS", "Google Sheets", "Manual records when nothing else fits", logo_path("google-sheets.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free HR software in 2026",
    subtitle = "Zoho People  ·  OrangeHRM  ·  Homebase  ·  Bitrix24  ·  Google Sheets",
)

c.save("free-hr-software.webp")
