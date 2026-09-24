#!/usr/bin/env python3
"""
Feature image generator: Free Mac video editors in 2026
Output : static/img/free-video-editing-mac.webp  (1200x630 px)
Silo   : Video   Accent: #ef4444

macOS requirements and watermark notes come from the comparison table in
content/video/free-video-editing-mac.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar, logo_path,
)

ACCENT = "#ef4444"   # Video silo, red

c = Canvas()

panel_table(c, ACCENT, "Mac requirements and watermarks",
    ["Editor", "macOS", "Watermark"],
    [
        ("iMovie",          [("15.6 or later", NEUTRAL),  ("None", GOOD)]),
        ("DaVinci Resolve", [("14 or later", NEUTRAL),    ("None", GOOD)]),
        ("CapCut Desktop",  [("Intel, Silicon", NEUTRAL), ("Asset risk", WARN)]),
        ("Kdenlive",        [("13 or later", NEUTRAL),    ("None", GOOD)]),
        ("Shotcut",         [("Intel, Silicon", NEUTRAL), ("None", GOOD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "iM",
    logo     = logo_path("imovie.png"),
    name     = "iMovie",
    tagline  = "Apple's free starter editor",
    note     = "Cuts, titles, soundtracks, and green screen, but no true multicamera editor",
)

card_grid(c, [
    ("#3b82f6", "DR", "DaVinci Resolve", "Full timeline, color, and audio, no watermark", logo_path("davinci-resolve.png")),
    ("#22c55e", "Cc", "CapCut Desktop",  "Short social clips with auto captions", logo_path("capcut.png")),
    ("#8b5cf6", "Kd", "Kdenlive",        "Open-source multi-track, separate Mac builds", logo_path("kdenlive.png")),
    ("#eab308", "Sc", "Shotcut",         "Broad format support for unusual codecs", logo_path("shotcut.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free Mac video editors in 2026",
    subtitle = "iMovie  ·  DaVinci Resolve  ·  CapCut  ·  Kdenlive  ·  Shotcut",
)

c.save("free-video-editing-mac.webp")
