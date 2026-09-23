#!/usr/bin/env python3
"""
Feature image generator: Free team email in 2026
Output : static/img/free-team-email.webp  (1200x630 px)
Silo   : Cloud   Accent: #06b6d4

Account and domain limits come from content/cloud/free-team-email.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#06b6d4"   # Cloud silo, cyan

c = Canvas()

panel_table(c, ACCENT, "Accounts and custom domains",
    ["Service", "Users", "Own domain"],
    [
        ("Zoho Mail",       [("5 users", GOOD),        ("Yes", GOOD)]),
        ("Spike",           [("3 addresses", WARN),    ("spike.team", WARN)]),
        ("Proton Mail",     [("1 per person", NEUTRAL), ("No", BAD)]),
        ("Tuta",            [("1 per person", NEUTRAL), ("No", BAD)]),
        ("Gmail delegates", [("10 delegates", NEUTRAL), ("No", BAD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Zo",
    name     = "Zoho Mail",
    tagline  = "Up to five custom-domain users",
    note     = "Business email on your own domain where the free plan is available",
)

card_grid(c, [
    ("#8b5cf6", "Sp", "Spike",           "Three addresses on a spike.team domain"),
    ("#3b82f6", "Pm", "Proton Mail",     "Separate encrypted account for each person"),
    ("#22c55e", "Tu", "Tuta",            "Private accounts for a small group"),
    ("#ef4444", "Gm", "Gmail delegates", "One account shared with up to 10 delegates"),
])

card_bar(
    c, ACCENT,
    title    = "Free team email in 2026",
    subtitle = "Zoho Mail  ·  Spike  ·  Proton Mail  ·  Tuta  ·  Gmail delegates",
)

c.save("free-team-email.webp")
