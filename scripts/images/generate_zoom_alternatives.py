#!/usr/bin/env python3
"""
Feature image generator: Free Zoom alternatives in 2026
Output : static/img/zoom-alternatives.webp  (1200x630 px)
Silo   : Video   Accent: #ef4444

Group-call limits come from the comparison table in
content/video/zoom-alternatives.md. Jitsi and Discord publish no duration cap.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, TEXT_W, TEXT_DIM, GOOD, WARN, BAD,
    card_window, card_featured, card_grid, card_bar, mix,
)

ACCENT = "#ef4444"   # Video silo, red

c = Canvas()

# ── LEFT PANEL: group-call time limit as bars (60 minutes = full scale) ───────
x0, y0, x1, y1 = card_window(c, "Group call time limit, free plans")

rows = [
    ("Whereby",     30,   "30 min",           BAD),
    ("Zoom Basic",  40,   "40 min",           BAD),
    ("Google Meet", 60,   "60 min",           WARN),
    ("Teams Free",  60,   "60 min",           WARN),
    ("Jitsi Meet",  None, "No fixed limit",   GOOD),
    ("Discord",     None, "No published cap", GOOD),
]
NAME_W = 132
bx0, bx1 = x0 + NAME_W, x1
rh = (y1 - y0 + 6) / len(rows)
for i, (name, minutes, label, col) in enumerate(rows):
    ry = y0 + i * rh
    mid = ry + (rh - 8) / 2
    c.fit_text(x0, mid, name, 16, NAME_W - 12, TEXT_W, "semibold", anchor="lm")
    c.rect(bx0, ry + 4, bx1, ry + rh - 12, CARD_BG, r=8)
    frac = 1.0 if minutes is None else minutes / 60
    fx1 = bx0 + frac * (bx1 - bx0)
    c.rect(bx0, ry + 4, fx1, ry + rh - 12, mix(col, CARD_BG, 0.45), r=8)
    c.text(bx0 + 14, mid, label, 14, TEXT_W, "semibold", anchor="lm")

card_featured(
    c, ACCENT,
    initials = "GM",
    name     = "Google Meet",
    tagline  = "Best free video calling for most users",
    note     = "Browser calls: 24 hours one to one, 60 minutes for groups of up to 100",
)

card_grid(c, [
    ("#3b82f6", "Ji", "Jitsi Meet", "Open source with link-based guest access"),
    ("#8b5cf6", "Te", "Teams Free", "Best for users of Microsoft apps"),
    ("#22c55e", "Di", "Discord",    "Informal teams and long-running calls"),
    ("#eab308", "Wb", "Whereby",    "Reusable room for small client calls"),
])

card_bar(
    c, ACCENT,
    title    = "Free Zoom alternatives in 2026",
    subtitle = "Google Meet  ·  Jitsi Meet  ·  Microsoft Teams  ·  Discord  ·  Whereby",
)

c.save("zoom-alternatives.webp")
