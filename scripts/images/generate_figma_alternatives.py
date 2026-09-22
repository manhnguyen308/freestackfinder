#!/usr/bin/env python3
"""
Feature image generator: Free Figma alternatives in 2026
Output : static/img/figma-alternatives.webp  (1200x630 px)
Silo   : Creative   Accent: #f97316

Plan limits come from content/creative/figma-alternatives.md. The left panel
is a generic wireframe and makes no product claim.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM, TEXT_MID, LINE,
    card_window, card_featured, card_grid, card_bar, mix,
)

ACCENT = "#f97316"   # Creative silo, orange

c = Canvas()

# ── LEFT PANEL: layers list beside a landing-page wireframe ───────────────────
x0, y0, x1, y1 = card_window(c, "Penpot: landing page")

SIDE_R = x0 + 132
c.text(x0, y0, "LAYERS", 12, TEXT_DIM, "semibold")
layers = [
    (ACCENT,    "Nav bar"),
    ("#e5e7eb", "Hero title"),
    ("#22c55e", "CTA button"),
    ("#3b82f6", "Hero image"),
    ("#8b5cf6", "Card grid"),
    ("#eab308", "Footer"),
]
ly = y0 + 26
for i, (col, name) in enumerate(layers):
    if i == 2:
        c.rect(x0 - 6, ly - 4, SIDE_R - 8, ly + 30, mix(ACCENT, WIN_BG, 0.82), r=6)
    c.rect(x0, ly + 6, x0 + 14, ly + 20, col, r=3)
    c.fit_text(x0 + 24, ly + 13, name, 14, SIDE_R - x0 - 36, TEXT_MID, anchor="lm")
    ly += 42

# Frame
fx0, fy0, fx1, fy1 = SIDE_R + 4, y0 - 4, x1, y1
c.rect(fx0, fy0, fx1, fy1, CARD_BG, r=8)
c.rect(fx0 + 14, fy0 + 14, fx0 + 60, fy0 + 26, ACCENT, r=3)
for k in range(3):
    c.rect(fx1 - 30 - k * 34, fy0 + 16, fx1 - 12 - k * 34, fy0 + 24, "#3a3f52", r=3)
c.line([(fx0, fy0 + 40), (fx1, fy0 + 40)], LINE)

# Hero copy and button (left half), image placeholder (right half)
hx = fx0 + 16
c.rect(hx, fy0 + 62, hx + 150, fy0 + 76, "#e5e7eb", r=4)
c.rect(hx, fy0 + 84, hx + 120, fy0 + 98, "#e5e7eb", r=4)
c.rect(hx, fy0 + 110, hx + 130, fy0 + 118, "#4a4f66", r=3)
c.rect(hx, fy0 + 126, hx + 104, fy0 + 134, "#4a4f66", r=3)
c.rect(hx, fy0 + 150, hx + 84, fy0 + 176, "#22c55e", r=6)
# Selection outline around the button
c.rect(hx - 4, fy0 + 146, hx + 88, fy0 + 180, None, r=8, outline="#60a5fa", width=2)
for sx, sy in [(hx - 4, fy0 + 146), (hx + 88, fy0 + 146), (hx - 4, fy0 + 180), (hx + 88, fy0 + 180)]:
    c.rect(sx - 3, sy - 3, sx + 3, sy + 3, "#ffffff")

ix0, iy0, ix1, iy1 = fx0 + 196, fy0 + 58, fx1 - 16, fy0 + 180
c.rect(ix0, iy0, ix1, iy1, "#262b3b", r=6)
c.line([(ix0 + 6, iy0 + 6), (ix1 - 6, iy1 - 6)], "#3a4058", 2)
c.line([(ix0 + 6, iy1 - 6), (ix1 - 6, iy0 + 6)], "#3a4058", 2)

# Card grid row
cw = (fx1 - fx0 - 16 * 2 - 12 * 2) / 3
for k in range(3):
    cx0 = fx0 + 16 + k * (cw + 12)
    c.rect(cx0, fy0 + 200, cx0 + cw, fy1 - 16, "#232736", r=6)
    c.rect(cx0 + 10, fy0 + 212, cx0 + 40, fy0 + 242, "#8b5cf6", r=6)
    c.rect(cx0 + 10, fy0 + 254, cx0 + cw - 16, fy0 + 262, "#4a4f66", r=3)
    c.rect(cx0 + 10, fy0 + 270, cx0 + cw - 34, fy0 + 278, "#3a3f52", r=3)

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "Pp",
    name     = "Penpot",
    tagline  = "Best for open files and self-hosting",
    note     = "Hosted free plan for up to eight team members, "
               "or self-host the open-source edition",
)

card_grid(c, [
    ("#3b82f6", "Lu", "Lunacy",        "Desktop app with local files, ten free cloud documents"),
    ("#8b5cf6", "Pl", "Plasmic",       "Visual builds that export React code"),
    ("#22c55e", "QU", "Quant UX",      "Prototypes with built-in usability tests"),
    ("#ec4899", "Fi", "Figma Starter", "Three collaborative files, three pages each"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
card_bar(
    c, ACCENT,
    title    = "Free Figma alternatives in 2026",
    subtitle = "Penpot  ·  Lunacy  ·  Plasmic  ·  Quant UX  ·  Figma Starter",
)

c.save("figma-alternatives.webp")
