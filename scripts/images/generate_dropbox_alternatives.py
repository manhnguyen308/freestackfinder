#!/usr/bin/env python3
"""
Feature image generator: Dropbox alternatives with more free storage in 2026
Output : static/img/dropbox-alternatives.webp  (1200x630 px)
Silo   : Cloud   Accent: #06b6d4

Free storage figures come from the comparison table in
content/cloud/dropbox-alternatives.md. Product icons come from
scripts/images/logos/ (sources listed in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, TEXT_W, TEXT_DIM,
    card_window, card_featured, card_grid, card_bar, mix,
)

ACCENT = "#06b6d4"   # Cloud silo, cyan
LOGOS  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logos")


def logo(name):
    return os.path.join(LOGOS, name)

c = Canvas()

# ── LEFT PANEL: free storage as bars, 20GB = full scale ───────────────────────
x0, y0, x1, y1 = card_window(c, "Free storage by service")

# Proton Drive starts at 2GB; the faded segment is the 3GB its setup tasks unlock.
rows = [
    ("MEGA",          20, 20, "20GB",             "#22c55e"),
    ("Google Drive",  15, 15, "Up to 15GB shared", "#3b82f6"),
    ("Box Free",      10, 10, "10GB",             "#8b5cf6"),
    ("OneDrive",       5,  5, "5GB shared",       "#eab308"),
    ("Proton Drive",   2,  5, "2GB, up to 5GB",   "#ec4899"),
    ("Dropbox Basic",  2,  2, "2GB",              "#ef4444"),
]
NAME_W = 136
bx0, bx1 = x0 + NAME_W, x1
rh = (y1 - y0 + 6) / len(rows)
for i, (name, gb, max_gb, label, col) in enumerate(rows):
    ry = y0 + i * rh
    mid = ry + (rh - 8) / 2
    c.fit_text(x0, mid, name, 16, NAME_W - 12, TEXT_W, "semibold", anchor="lm")
    c.rect(bx0, ry + 4, bx1, ry + rh - 12, CARD_BG, r=8)
    fx1 = bx0 + max(gb / 20, 0.08) * (bx1 - bx0)
    mx1 = bx0 + max(max_gb / 20, 0.08) * (bx1 - bx0)
    if mx1 > fx1:
        c.rect(bx0, ry + 4, mx1, ry + rh - 12, mix(col, CARD_BG, 0.8), r=8)
    c.rect(bx0, ry + 4, fx1, ry + rh - 12, mix(col, CARD_BG, 0.4), r=8)
    lx = mx1 + 10 if gb <= 5 else bx0 + 14
    c.text(lx, mid, label, 14, TEXT_W if gb > 5 else TEXT_DIM, "semibold", anchor="lm")

card_featured(
    c, ACCENT,
    initials = "Me",
    name     = "MEGA",
    tagline  = "Best for maximum free storage",
    note     = "20GB with client-side encryption and desktop sync",
    logo     = logo("mega.png"),
)

card_grid(c, [
    ("#3b82f6", "GD", "Google Drive", "Up to 15GB shared across Drive, Gmail, and Photos",
     logo("google-drive.png")),
    ("#eab308", "OD", "OneDrive",     "5GB shared with Outlook, sync built into Windows",
     logo("onedrive.png")),
    ("#ec4899", "Pr", "Proton Drive", "2GB, up to 5GB after setup, end-to-end encrypted",
     logo("proton-drive.png")),
    ("#8b5cf6", "Bx", "Box Free",     "10GB for business documents",
     logo("box.png")),
])

card_bar(
    c, ACCENT,
    title    = "Dropbox alternatives with more free storage in 2026",
    subtitle = "MEGA  ·  Google Drive  ·  OneDrive  ·  Proton Drive  ·  Box",
)

c.save("dropbox-alternatives.webp")
