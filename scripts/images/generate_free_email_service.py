#!/usr/bin/env python3
"""
Feature image generator: Free email services in 2026
Output : static/img/free-email-service.webp  (1200x630 px)
Silo   : Cloud   Accent: #06b6d4

Storage and encryption values come from the comparison table in
content/cloud/free-email-service.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#06b6d4"   # Cloud silo, cyan

c = Canvas()

panel_table(c, ACCENT, "Storage and privacy by inbox",
    ["Service", "Free storage", "Encrypted"],
    [
        ("Gmail",       [("15GB shared", GOOD),   ("No", BAD)]),
        ("Proton Mail", [("1GB", WARN),           ("Yes", GOOD)]),
        ("Outlook.com", [("15GB", GOOD),          ("No", BAD)]),
        ("Zoho Mail",   [("5GB a user", NEUTRAL), ("No", BAD)]),
        ("Tuta",        [("1GB", WARN),           ("Yes", GOOD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Gm",
    name     = "Gmail",
    tagline  = "Best free email for most people",
    note     = "15GB of shared storage and close ties to Docs, Drive, and Calendar",
)

card_grid(c, [
    ("#8b5cf6", "Pm", "Proton Mail", "End-to-end encrypted mail, 1GB free"),
    ("#3b82f6", "Ol", "Outlook.com", "15GB for Microsoft app users"),
    ("#ef4444", "Zo", "Zoho Mail",   "Custom domain in selected regions"),
    ("#22c55e", "Tu", "Tuta",        "Encrypted subject lines and calendar"),
])

card_bar(
    c, ACCENT,
    title    = "Free email services in 2026",
    subtitle = "Gmail  ·  Proton Mail  ·  Outlook.com  ·  Zoho Mail  ·  Tuta",
)

c.save("free-email-service.webp")
