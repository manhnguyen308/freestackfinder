#!/usr/bin/env python3
"""
Feature image generator: Free screen recording software in 2026
Output : static/img/free-screen-recording-software.webp  (1200x630 px)
Silo   : Video   Accent: #ef4444

Time limits and watermark rules come from the comparison table in
content/video/free-screen-recording-software.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#ef4444"   # Video silo, red

c = Canvas()

panel_table(c, ACCENT, "Recording limits on free plans",
    ["Tool", "Time limit", "Watermark"],
    [
        ("OBS Studio",    [("Unlimited", GOOD),      ("None", GOOD)]),
        ("ShareX",        [("Unlimited", GOOD),      ("None", GOOD)]),
        ("Loom Free",     [("5 minutes", WARN),      ("None", GOOD)]),
        ("Screencastify", [("30 min, 10 videos", WARN), ("Yes", BAD)]),
        ("Clipchamp",     [("30 min a clip", WARN),  ("None", GOOD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "OB",
    name     = "OBS Studio",
    tagline  = "Local recording without a service cap",
    note     = "No time limit and no watermark on Windows, Mac, and Linux",
)

card_grid(c, [
    ("#3b82f6", "SX", "ShareX",        "Windows recorder with screenshots and annotation"),
    ("#8b5cf6", "Lo", "Loom Free",     "Shareable clips up to 5 minutes, 25 videos"),
    ("#22c55e", "Sc", "Screencastify", "Ten browser recordings on the free plan"),
    ("#06b6d4", "Cc", "Clipchamp",     "Recording and basic edits in one project"),
])

card_bar(
    c, ACCENT,
    title    = "Free screen recording software in 2026",
    subtitle = "OBS Studio  ·  ShareX  ·  Loom  ·  Screencastify  ·  Clipchamp",
)

c.save("free-screen-recording-software.webp")
