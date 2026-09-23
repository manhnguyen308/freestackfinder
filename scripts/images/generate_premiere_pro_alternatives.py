#!/usr/bin/env python3
"""
Feature image generator: Free Adobe Premiere Pro alternatives in 2026
Output : static/img/premiere-pro-alternatives.webp  (1200x630 px)
Silo   : Video   Accent: #ef4444

Use cases and caveats come from the comparison table in
content/video/premiere-pro-alternatives.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, WARN,
    panel_list, card_featured, card_grid, card_bar,
)

ACCENT = "#ef4444"   # Video silo, red

c = Canvas()

panel_list(c, "What each editor replaces", [
    ("#3b82f6", "DaVinci Resolve", "Serious solo editing and finishing", "Format limits",  WARN),
    ("#22c55e", "CapCut Desktop",  "Short-form social content",          "Watermark risk", WARN),
    ("#8b5cf6", "Kdenlive",        "Open-source timeline editing",       "More setup",     WARN),
    ("#06b6d4", "OpenShot",        "Casual editing and basic projects",  "Low ceiling",    WARN),
    ("#eab308", "Shotcut",         "Footage compatibility problems",     "Harder to learn", WARN),
], section="Replacement use and main caveat")

card_featured(
    c, ACCENT,
    initials = "DR",
    name     = "DaVinci Resolve",
    tagline  = "Best overall for serious solo editors",
    note     = "Editing, color, and audio in one app. The free version has real format limits",
)

card_grid(c, [
    ("#22c55e", "Cc", "CapCut Desktop", "For social-first Premiere users"),
    ("#8b5cf6", "Kd", "Kdenlive",       "Open-source timeline for former Premiere users"),
    ("#06b6d4", "OS", "OpenShot",       "If your Premiere use was always light"),
    ("#eab308", "Sc", "Shotcut",        "A format rescue option"),
])

card_bar(
    c, ACCENT,
    title    = "Free Adobe Premiere Pro alternatives in 2026",
    subtitle = "DaVinci Resolve  ·  CapCut  ·  Kdenlive  ·  OpenShot  ·  Shotcut",
)

c.save("premiere-pro-alternatives.webp")
