#!/usr/bin/env python3
"""
Feature image generator: Free AI email tools for drafting and replies in 2026
Output : static/img/free-ai-email-tools.webp  (1200x630 px)
Silo   : Cloud   Accent: #06b6d4

Drafting depth and free-use limits come from the comparison table in
content/cloud/free-ai-email-tools.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#06b6d4"   # Cloud silo, cyan

c = Canvas()

panel_table(c, ACCENT, "Drafting help and free limits",
    ["Tool", "Drafts", "Free use"],
    [
        ("Gmail Smart Compose", [("Predictive", NEUTRAL),   ("No cap", GOOD)]),
        ("Compose AI",          [("Full drafts", GOOD),     ("Monthly credits", WARN)]),
        ("ChatGPT free",        [("Full drafts", GOOD),     ("Varies", WARN)]),
        ("Boomerang",           [("Scoring only", NEUTRAL), ("10 a month", WARN)]),
        ("Spike",               [("Full drafts", GOOD),     ("10 queries", WARN)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Gm",
    name     = "Gmail Smart Compose",
    tagline  = "Start with the tool in your inbox",
    note     = "Predictive text and short replies inside Gmail, with no usage cap",
)

card_grid(c, [
    ("#3b82f6", "CA", "Compose AI",   "Full drafts in Gmail or Outlook, monthly credits"),
    ("#22c55e", "GP", "ChatGPT free", "Longer drafts from pasted context"),
    ("#eab308", "Bo", "Boomerang",    "Email quality scoring for Gmail"),
    ("#8b5cf6", "Sp", "Spike",        "Standalone email app with limited queries"),
])

card_bar(
    c, ACCENT,
    title    = "Free AI email tools in 2026",
    subtitle = "Gmail Smart Compose  ·  Compose AI  ·  ChatGPT  ·  Boomerang  ·  Spike",
)

c.save("free-ai-email-tools.webp")
