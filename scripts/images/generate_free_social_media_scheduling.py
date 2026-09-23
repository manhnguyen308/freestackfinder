#!/usr/bin/env python3
"""
Feature image generator: Free social media scheduling tools in 2026
Output : static/img/free-social-media-scheduling.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Channel and queue limits come from
content/business/free-social-media-scheduling.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, NEUTRAL,
    panel_table, note_card, table_bottom, card_featured, card_grid, card_bar,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

x0, y0, x1, y1 = panel_table(c, ACCENT, "Channel and queue limits",
    ["Tool", "Scope", "Free queue"],
    [
        ("Buffer",        [("3 channels", NEUTRAL),   ("10 each", WARN)]),
        ("Metricool",     [("1 brand", NEUTRAL),      ("20 a month", WARN)]),
        ("Later",         [("IG, TikTok", NEUTRAL),   ("In settings", NEUTRAL)]),
        ("Meta Suite",    [("FB, Instagram", NEUTRAL), ("No fee", GOOD)]),
    ])

note_card(c, ACCENT, x0, table_bottom(y0, 4, y1) + 14, x1, y1, "Agencies",
          "Several brands usually need a paid tier")

card_featured(
    c, ACCENT,
    initials = "Bu",
    name     = "Buffer",
    tagline  = "Best overall for small teams",
    note     = "Three channels, ten queued posts on each, and basic analytics",
)

card_grid(c, [
    ("#3b82f6", "Mc", "Metricool",           "Scheduling plus 30 days of analytics"),
    ("#ec4899", "La", "Later",               "Visual Instagram and TikTok planning"),
    ("#06b6d4", "Me", "Meta Business Suite", "Native Facebook and Instagram scheduling"),
    ("#64748b", "Hs", "Hootsuite",           "No longer the default free plan"),
])

card_bar(
    c, ACCENT,
    title    = "Free social media scheduling tools in 2026",
    subtitle = "Buffer  ·  Metricool  ·  Later  ·  Meta Business Suite",
)

c.save("free-social-media-scheduling.webp")
