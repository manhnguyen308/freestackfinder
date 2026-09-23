#!/usr/bin/env python3
"""
Feature image generator: Free video conferencing in 2026
Output : static/img/free-video-conferencing.webp  (1200x630 px)
Silo   : Video   Accent: #ef4444

Call limits and participant counts come from the "Meeting limits at a glance"
table in content/video/free-video-conferencing.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#ef4444"   # Video silo, red

c = Canvas()

panel_table(c, ACCENT, "Meeting limits at a glance",
    ["Tool", "Group calls", "Video seats"],
    [
        ("Google Meet",   [("60 min", WARN),       ("100", NEUTRAL)]),
        ("Jitsi Meet",    [("No limit listed", GOOD), ("Varies", NEUTRAL)]),
        ("Teams Free",    [("60 min", WARN),       ("100", NEUTRAL)]),
        ("Whereby",       [("30 min", BAD),        ("4", NEUTRAL)]),
        ("Zoho Meeting",  [("60 min", WARN),       ("100", NEUTRAL)]),
        ("Discord",       [("None", GOOD),         ("25", NEUTRAL)]),
    ])

card_featured(
    c, ACCENT,
    initials = "GM",
    name     = "Google Meet",
    tagline  = "The default choice for most users",
    note     = "Browser group calls up to 60 minutes with 100 participants",
)

card_grid(c, [
    ("#3b82f6", "Ji", "Jitsi Meet",   "Guests join by link, and you can self-host"),
    ("#8b5cf6", "Te", "Teams Free",   "For groups already using Microsoft apps"),
    ("#22c55e", "Wb", "Whereby",      "Permanent room for short calls of four"),
    ("#eab308", "Zo", "Zoho Meeting", "Structured sessions and basic webinars"),
])

card_bar(
    c, ACCENT,
    title    = "Free video conferencing in 2026",
    subtitle = "Google Meet  ·  Jitsi  ·  Teams  ·  Whereby  ·  Zoho Meeting  ·  Discord",
)

c.save("free-video-conferencing.webp")
