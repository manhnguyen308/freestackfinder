#!/usr/bin/env python3
"""
Feature image generator: Free email signature makers
Output : static/img/free-email-signature.webp  (1200x630 px)
Silo   : Cloud   Accent: #06b6d4

Branding, trial, and account rules come from
content/cloud/free-email-signature.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#06b6d4"   # Cloud silo, cyan

c = Canvas()

panel_table(c, ACCENT, "Ongoing free output and accounts",
    ["Maker", "Free output", "Account"],
    [
        ("HubSpot",         [("Unbranded", GOOD),   ("Not needed", GOOD)]),
        ("MySignature",     [("Branded", WARN),     ("Required", NEUTRAL)]),
        ("Signature Maker", [("Unbranded", GOOD),   ("Not needed", GOOD)]),
        ("WiseStamp",       [("14-day trial", BAD), ("Required", NEUTRAL)]),
        ("Newoldstamp",     [("7-day trial", BAD),  ("Required", NEUTRAL)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Hs",
    name     = "HubSpot Signature Generator",
    tagline  = "Quick setup without an account",
    note     = "Unlimited signatures with no branding added to the output",
)

card_grid(c, [
    ("#3b82f6", "MS", "MySignature",     "One saved signature, with its badge"),
    ("#22c55e", "SM", "Signature Maker", "Simplest free option, no account"),
    ("#eab308", "Ws", "WiseStamp",       "14-day trial, then a paid plan"),
    ("#8b5cf6", "No", "Newoldstamp",     "7-day evaluation before a team plan"),
])

card_bar(
    c, ACCENT,
    title    = "Free email signature makers for Gmail, Outlook, and Apple Mail",
    subtitle = "HubSpot  ·  MySignature  ·  Signature Maker  ·  WiseStamp  ·  Newoldstamp",
)

c.save("free-email-signature.webp")
