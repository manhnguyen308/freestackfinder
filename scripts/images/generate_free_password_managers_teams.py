#!/usr/bin/env python3
"""
Feature image generator: Free password managers for teams in 2026
Output : static/img/free-password-managers-teams.webp  (1200x630 px)
Silo   : Security   Accent: #8b5cf6

Hosting and team-size limits come from
content/security/free-password-managers-teams.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD, NEUTRAL,
    panel_table, note_card, table_bottom, card_featured, card_grid, card_bar, logo_path, glyph,
)

ACCENT = "#8b5cf6"   # Security silo, violet

c = Canvas()

x0, y0, x1, y1 = panel_table(c, ACCENT, "Team sharing without a paid seat",
    ["Option", "Hosting", "Team size"],
    [
        ("Bitwarden Orgs",    [("Cloud", GOOD),       ("2 users", WARN)]),
        ("Vaultwarden",       [("Self-hosted", WARN), ("Community", NEUTRAL)]),
        ("Passbolt CE",       [("Self-hosted", WARN), ("Unlimited", GOOD)]),
        ("KeePassXC vault",   [("Shared file", NEUTRAL), ("No per-user", BAD)]),
    ])

# The article's closing rule
note_card(c, ACCENT, x0, table_bottom(y0, 4, y1) + 14, x1, y1, "Before onboarding",
          "Name a vault owner before onboarding")

card_featured(
    c, ACCENT,
    initials = "BW",
    logo     = logo_path("bitwarden.png"),
    name     = "Bitwarden Free Organizations",
    tagline  = "Best cloud-hosted free option",
    note     = "Two users and two shared collections, with cloud sync",
)

card_grid(c, [
    ("#3b82f6", "VW", "Vaultwarden",  "Unofficial Bitwarden-compatible server", logo_path("vaultwarden.png")),
    ("#22c55e", "Pb", "Passbolt CE",  "Unlimited users, self-hosted only", logo_path("passbolt.png")),
    ("#06b6d4", "KP", "KeePassXC",    "Shared local file, no per-user controls", logo_path("keepassxc.png")),
    ("#64748b", "$",  "Paid teams",   "When no one can maintain a server", glyph("tag", "#64748b")),
])

card_bar(
    c, ACCENT,
    title    = "Free password managers for teams in 2026",
    subtitle = "Bitwarden  ·  Vaultwarden  ·  Passbolt  ·  KeePassXC",
)

c.save("free-password-managers-teams.webp")
