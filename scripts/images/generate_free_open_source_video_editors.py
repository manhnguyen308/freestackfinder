#!/usr/bin/env python3
"""
Feature image generator: Open-source video editors in 2026
Output : static/img/free-open-source-video-editors.webp  (1200x630 px)
Silo   : Video   Accent: #ef4444

Platforms and complexity come from the comparison table in
content/video/free-open-source-video-editors.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, INFO, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#ef4444"   # Video silo, red

c = Canvas()

panel_table(c, ACCENT, "Platforms and editing depth",
    ["Editor", "Platforms", "Complexity"],
    [
        ("Kdenlive",    [("Win, Mac, Linux", NEUTRAL), ("Intermediate", INFO)]),
        ("Shotcut",     [("Win, Mac, Linux", NEUTRAL), ("Intermediate", INFO)]),
        ("OpenShot",    [("Win, Mac, Linux", NEUTRAL), ("Beginner", GOOD)]),
        ("Blender VSE", [("Win, Mac, Linux", NEUTRAL), ("Advanced", WARN)]),
        ("Olive",       [("Win, Linux", NEUTRAL),      ("Pre-release", BAD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Kd",
    name     = "Kdenlive",
    tagline  = "Best overall open-source editor",
    note     = "Conventional multi-track timeline with proxy support on Linux, Windows, and Mac",
)

card_grid(c, [
    ("#3b82f6", "Sc", "Shotcut",     "Best for difficult source formats and codecs"),
    ("#22c55e", "OS", "OpenShot",    "Simple projects with the easiest learning curve"),
    ("#f97316", "Bl", "Blender VSE", "For Blender users and motion graphics work"),
    ("#64748b", "Ol", "Olive",       "Worth tracking, not production-ready yet"),
])

card_bar(
    c, ACCENT,
    title    = "Open-source video editors in 2026",
    subtitle = "Kdenlive  ·  Shotcut  ·  OpenShot  ·  Blender VSE  ·  Olive",
)

c.save("free-open-source-video-editors.webp")
