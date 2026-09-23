#!/usr/bin/env python3
"""
Feature image generator: Free VPNs in 2026
Output : static/img/free-vpn.webp  (1200x630 px)
Silo   : Security   Accent: #8b5cf6

Data caps and country selection come from content/security/free-vpn.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD,
    panel_table, note_card, table_bottom, card_featured, card_grid, card_bar,
)

ACCENT = "#8b5cf6"   # Security silo, violet

c = Canvas()

x0, y0, x1, y1 = panel_table(c, ACCENT, "What each free plan limits",
    ["Plan", "Data", "Countries"],
    [
        ("Proton VPN Free", [("Unlimited", GOOD),   ("Automatic", WARN)]),
        ("Windscribe Free", [("2 or 10 GB", WARN),  ("Selectable", GOOD)]),
        ("TunnelBear Free", [("2 GB", WARN),        ("Paid only", BAD)]),
    ])

# The article's screening rule, below the table
note_card(c, ACCENT, x0, table_bottom(y0, 3, y1) + 14, x1, y1, "Before you install",
          "Skip providers that cannot explain their business model")

card_featured(
    c, ACCENT,
    initials = "Pr",
    name     = "Proton VPN Free",
    tagline  = "Best overall free VPN",
    note     = "Unlimited data, open-source apps, and published third-party audits",
)

card_grid(c, [
    ("#3b82f6", "Ws", "Windscribe", "More server choice, with a monthly data cap"),
    ("#eab308", "TB", "TunnelBear", "2 GB a month for short sessions"),
    ("#22c55e", "$",  "Paid VPN",   "For streaming, P2P, or specific countries"),
    ("#ef4444", "?",  "Unknown free VPNs", "Some show ads or collect more data than expected"),
])

card_bar(
    c, ACCENT,
    title    = "Free VPNs in 2026: what each plan limits",
    subtitle = "Proton VPN  ·  Windscribe  ·  TunnelBear",
)

c.save("free-vpn.webp")
