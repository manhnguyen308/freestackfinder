#!/usr/bin/env python3
"""
Feature image generator: Free time tracking software in 2026
Output : static/img/free-time-tracking-software.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

User caps and invoicing come from the comparison table in
content/business/free-time-tracking-software.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

panel_table(c, ACCENT, "User caps and billing",
    ["Tool", "Users", "Invoicing"],
    [
        ("Clockify",        [("5 max", WARN),        ("No", BAD)]),
        ("Toggl Track",     [("5 max", WARN),        ("No", BAD)]),
        ("RescueTime Lite", [("1, desktop", NEUTRAL), ("No", BAD)]),
        ("TimeCamp",        [("Unlimited", GOOD),    ("No", BAD)]),
        ("Harvest",         [("1 seat", WARN),       ("Full", GOOD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Cl",
    name     = "Clockify",
    tagline  = "Shared tracking for up to five users",
    note     = "Shared projects and timers for a small team, with unlimited projects",
)

card_grid(c, [
    ("#ec4899", "Tg", "Toggl Track",     "Quick browser timer for individuals"),
    ("#3b82f6", "RT", "RescueTime Lite", "Automatic background tracking on desktop"),
    ("#eab308", "TC", "TimeCamp",        "Unlimited users, top-level projects only"),
    ("#f97316", "Hv", "Harvest",         "Solo invoicing, one seat and two projects"),
])

card_bar(
    c, ACCENT,
    title    = "Free time tracking software in 2026",
    subtitle = "Clockify  ·  Toggl Track  ·  RescueTime  ·  TimeCamp  ·  Harvest",
)

c.save("free-time-tracking-software.webp")
