#!/usr/bin/env python3
"""
Feature image generator: Free cloud storage in 2026
Output : static/img/free-cloud-storage-comparison.webp  (1200x630 px)
Silo   : Cloud   Accent: #06b6d4

Replaces a 1200x800 stock photo. Storage and limits come from
content/cloud/free-cloud-storage-comparison.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#06b6d4"   # Cloud silo, cyan

c = Canvas()

panel_table(c, ACCENT, "Free space and the limit behind it",
    ["Service", "Free space", "Watch for"],
    [
        ("MEGA",         [("20GB", GOOD),        ("Transfer caps", WARN)]),
        ("Google Drive", [("15GB shared", GOOD), ("Shared quota", WARN)]),
        ("Box",          [("10GB", NEUTRAL),     ("250MB per file", WARN)]),
        ("OneDrive",     [("5GB", NEUTRAL),      ("Small allowance", WARN)]),
        ("Proton Drive", [("Up to 5GB", NEUTRAL), ("Fewer apps", WARN)]),
        ("iCloud",       [("5GB", NEUTRAL),      ("Fills quickly", WARN)]),
    ])

card_featured(
    c, ACCENT,
    initials = "GB",
    name     = "Capacity, sharing, or privacy",
    tagline  = "Pick the job before the gigabytes",
    note     = "MEGA for space, Google Drive for collaboration, Proton Drive for encryption",
)

card_grid(c, [
    ("#22c55e", "Me", "MEGA",         "20GB with a separate transfer allowance"),
    ("#3b82f6", "GD", "Google Drive", "15GB shared with Gmail and Photos"),
    ("#ec4899", "Pr", "Proton Drive", "Up to 5GB, end-to-end encrypted"),
    ("#8b5cf6", "Bx", "Box",          "10GB with a 250MB upload cap per file"),
])

card_bar(
    c, ACCENT,
    title    = "Free cloud storage in 2026: space, privacy, and sync",
    subtitle = "MEGA  ·  Google Drive  ·  Box  ·  OneDrive  ·  Proton Drive  ·  iCloud  ·  Dropbox",
)

c.save("free-cloud-storage-comparison.webp")
