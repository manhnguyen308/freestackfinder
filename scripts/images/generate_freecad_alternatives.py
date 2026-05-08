#!/usr/bin/env python3
"""
Feature image generator: Best Free FreeCAD Alternatives in 2026
Output : static/img/freecad-alternatives.webp  (1200×630 px)
Silo   : Creative   Accent: #f97316
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image, ImageDraw
from image_helpers import (
    W, H, BG, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM,
    LEFT_W, CONTENT_H, INNER_PAD,
    font, rrect, draw_circle, truncate,
    draw_chrome, draw_featured_card, draw_grid, draw_bar, img_out,
)

ACCENT = "#f97316"   # Creative silo — orange

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — free CAD comparison panel ──────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Free CAD — 2026 Comparison")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

draw.text((SIDE, 44), "Tool & licensing model", fill=TEXT_DIM, font=font(11, bold=True))

tools = [
    (ACCENT,    "Onshape Free",   "Browser CAD · public projects · hobby",  "Best free pro CAD"),
    ("#22c55e", "Fusion 360",     "Personal use · private projects · CAM",  "Home makers"),
    ("#3b82f6", "Tinkercad",      "Primitive shapes · STL · beginners",      "Fastest start"),
    ("#8b5cf6", "SolveSpace",     "Parametric · GPL · lightweight",          "Open-source pick"),
    ("#ef4444", "OpenSCAD",       "Code-driven CAD · GPL · parametric",      "Programmers"),
]

row_y = 64
for col, label, value, status in tools:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 36, 5, CARD_BG)
    draw.rectangle([SIDE, row_y, SIDE + 4, row_y + 36], fill=col)
    draw.text((SIDE + 12, row_y + 4),  label,  fill=TEXT_DIM, font=font(10))
    draw.text((SIDE + 12, row_y + 18), value,  fill=TEXT_W,   font=font(12, bold=True))
    draw.text((LEFT_W - SIDE - 100, row_y + 12),
              truncate(draw, status, font(9), 96),
              fill=col, font=font(9, bold=True))
    row_y += 43

stats = [("Tools compared", "6"), ("Cost", "Free tiers"), ("Use", "Hobby & maker")]
stat_x = SIDE
stat_y = CONTENT_H - 48
for label, val in stats:
    rrect(draw, stat_x, stat_y, stat_x + 130, stat_y + 36, 6, CARD_BG)
    draw.text((stat_x + 8, stat_y + 4),
              truncate(draw, label, font(9), 114),
              fill=TEXT_DIM, font=font(9))
    draw.text((stat_x + 8, stat_y + 18),
              truncate(draw, val, font(12, bold=True), 114),
              fill=TEXT_W, font=font(12, bold=True))
    stat_x += 138

# ── RIGHT PANEL ─────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "On",
    name        = "Onshape Free",
    tagline     = "Best free parametric CAD overall",
    line1       = "Browser-based · version history · collab",
    line2       = "Public projects only · hobby license",
    badge       = "Pro-grade CAD with no install",
    license_note= "Free hobby plan — public documents only",
)

draw_grid(draw, ACCENT, [
    ("#22c55e", "F3", "Fusion 360",   "Personal use · CAD + CAM · private files"),
    ("#3b82f6", "Tk", "Tinkercad",    "Primitive shapes · STL export · beginners"),
    ("#8b5cf6", "SS", "SolveSpace",   "GPL · lightweight · parametric · offline"),
    ("#ef4444", "Os", "OpenSCAD",     "Code-driven · GPL · parametric variants"),
])

# ── BOTTOM BAR ──────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free FreeCAD Alternatives in 2026",
    subtitle = "Onshape  ·  Fusion 360  ·  Tinkercad  ·  SolveSpace  ·  OpenSCAD  ·  LibreCAD",
)

# ── Save ────────────────────────────────────────────────────────────────────
out = img_out("freecad-alternatives.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
