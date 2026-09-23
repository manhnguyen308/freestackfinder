#!/usr/bin/env python3
"""
Feature image generator: Free two-factor authentication apps in 2026
Output : static/img/best-free-2fa-apps.webp  (1200x630 px)
Silo   : Security   Accent: #8b5cf6

Platforms and backup models come from content/security/best-free-2fa-apps.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#8b5cf6"   # Security silo, violet

c = Canvas()

panel_table(c, ACCENT, "Authenticators compared",
    ["App", "Platforms", "Open source"],
    [
        ("Aegis",          [("Android", NEUTRAL),      ("Yes", GOOD)]),
        ("Ente Auth",      [("All platforms", NEUTRAL), ("Yes", GOOD)]),
        ("2FAS",           [("iOS, Android", NEUTRAL), ("Yes", GOOD)]),
        ("Bitwarden TOTP", [("Premium", WARN),         ("Yes", GOOD)]),
        ("Authy",          [("iOS, Android", NEUTRAL), ("No", BAD)]),
        ("Google Authenticator",    [("iOS, Android", NEUTRAL), ("No", BAD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Ae",
    name     = "Aegis Authenticator",
    tagline  = "Encrypted local vault on Android",
    note     = "Encrypted backups and exports decide what happens when a phone is lost",
)

card_grid(c, [
    ("#3b82f6", "En", "Ente Auth",      "Encrypted sync across mobile, desktop, and web"),
    ("#22c55e", "2F", "2FAS",           "iOS and Android with optional cloud backup"),
    ("#06b6d4", "BW", "Bitwarden TOTP", "Codes beside passwords with Premium"),
    ("#64748b", "Au", "Authy",          "For existing mobile users, not open source"),
])

card_bar(
    c, ACCENT,
    title    = "Free two-factor authentication apps in 2026",
    subtitle = "Aegis  ·  Ente Auth  ·  2FAS  ·  Bitwarden  ·  Authy",
)

c.save("best-free-2fa-apps.webp")
