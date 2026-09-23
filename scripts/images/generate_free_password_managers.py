#!/usr/bin/env python3
"""
Feature image generator: Free password managers in 2026
Output : static/img/free-password-managers.webp  (1200x630 px)
Silo   : Security   Accent: #8b5cf6

Every claim rendered here is taken from content/security/free-password-managers.md.
Dashlane appears only as an excluded option, matching the article.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, panel_list, card_featured, card_grid, card_bar,
)

ACCENT = "#8b5cf6"   # Security silo, violet

c = Canvas()

# Article: "Move email and banking accounts first", then cloud, social, shopping.
panel_list(c, "Vault: move these accounts first", [
    (ACCENT,    "Email",         "Recovery point for everything else", None, None),
    ("#3b82f6", "Banking",       "Highest direct loss if reused",      None, None),
    ("#06b6d4", "Cloud storage", "Holds documents and backups",        None, None),
    ("#ec4899", "Social",        "Identity and contact takeover",      None, None),
    ("#22c55e", "Shopping",      "Saved cards and addresses",          None, None),
], section="Highest value accounts")

card_featured(
    c, ACCENT,
    initials = "BW",
    name     = "Bitwarden",
    tagline  = "Best free option for most people",
    note     = "Unlimited passwords and devices. Premium adds TOTP and emergency access",
)

card_grid(c, [
    ("#3b82f6", "KP", "KeePassXC",   "Local vault file with no cloud account"),
    ("#22c55e", "PP", "Proton Pass", "Unlimited logins and devices, 10 email aliases"),
    ("#06b6d4", "NP", "NordPass",    "Unlimited passwords, one active device"),
    ("#ef4444", "DL", "Dashlane",    "Free plan ended in September 2025"),
])

card_bar(
    c, ACCENT,
    title    = "Free password managers in 2026",
    subtitle = "Bitwarden  ·  KeePassXC  ·  Proton Pass  ·  NordPass",
)

c.save("free-password-managers.webp")
