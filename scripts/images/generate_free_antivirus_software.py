#!/usr/bin/env python3
"""
Feature image generator: Free antivirus software in 2026
Output : static/img/free-antivirus-software.webp  (1200x630 px)
Silo   : Security   Accent: #8b5cf6

Real-time protection and platform values come from the comparison table in
content/security/free-antivirus-software.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar, logo_path,
)

ACCENT = "#8b5cf6"   # Security silo, violet

c = Canvas()

panel_table(c, ACCENT, "Real-time protection by tool",
    ["Tool", "Real-time", "Platforms"],
    [
        ("Windows Defender", [("Yes", GOOD),         ("Windows", NEUTRAL)]),
        ("Malwarebytes",     [("Manual scan", WARN), ("Win, Mac", NEUTRAL)]),
        ("Avast Free",       [("Yes", GOOD),         ("Win, Mac, mobile", NEUTRAL)]),
        ("AVG Free",         [("Yes", GOOD),         ("Win, Mac, mobile", NEUTRAL)]),
        ("Bitdefender",      [("Yes", GOOD),         ("Windows", NEUTRAL)]),
    ])

card_featured(
    c, ACCENT,
    initials = "WD",
    logo     = logo_path("windows-defender.png"),
    name     = "Windows Defender",
    tagline  = "Start with the protection already installed",
    note     = "Real-time protection on Windows 10 and 11, with published AV-TEST and AV-Comparatives results",
)

card_grid(c, [
    ("#3b82f6", "Mb", "Malwarebytes", "On-demand second opinion, no real-time on free", logo_path("malwarebytes.png")),
    ("#f97316", "Av", "Avast Free",   "Feature-rich, with a data collection history", logo_path("avast.png")),
    ("#22c55e", "AV", "AVG Free",     "Same engine and parent company as Avast", logo_path("avg.png")),
    ("#ef4444", "Bd", "Bitdefender",  "Focused real-time protection on Windows", logo_path("bitdefender.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free antivirus software in 2026",
    subtitle = "Windows Defender  ·  Malwarebytes  ·  Avast  ·  AVG  ·  Bitdefender",
)

c.save("free-antivirus-software.webp")
