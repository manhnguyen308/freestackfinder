#!/usr/bin/env python3
"""
Feature image generator: Canva Free vs Paid (2026)
Output : static/img/canva-free-vs-paid.webp  (1200×630 px)
Silo   : Creative   Accent: #f97316
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image, ImageDraw
from image_helpers import (
    W, H, BG, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM,
    LEFT_W, CONTENT_H,
    font, rrect, truncate,
    draw_chrome, draw_featured_card, draw_grid, draw_bar, img_out,
)

ACCENT = "#f97316"   # Creative silo — orange
PAID_COL = "#22c55e"
FREE_COL = "#3b82f6"

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — Free vs Paid feature comparison ───────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Canva Free vs Pro — 2026")

SIDE  = 20

# Column headers
draw.text((SIDE, 44), "Feature", fill=TEXT_DIM, font=font(11, bold=True))
draw.text((SIDE + 200, 44), "Free", fill=FREE_COL, font=font(11, bold=True))
draw.text((SIDE + 290, 44), "Pro", fill=PAID_COL, font=font(11, bold=True))

rows = [
    ("Templates",          "Many",      "All"),
    ("Background remover", "Limited",   "Unlimited"),
    ("Brand kits",         "1 basic",   "Multiple"),
    ("Magic Resize",       "—",         "Yes"),
    ("Storage",            "5 GB",      "1 TB"),
    ("Scheduler",          "—",         "Yes"),
    ("Team folders",       "Limited",   "Yes"),
]

row_y = 64
for feature, free_v, paid_v in rows:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 36, 5, CARD_BG)
    draw.rectangle([SIDE, row_y, SIDE + 4, row_y + 36], fill=ACCENT)
    draw.text((SIDE + 12, row_y + 11), truncate(draw, feature, font(12, bold=True), 170),
              fill=TEXT_W, font=font(12, bold=True))
    draw.text((SIDE + 200, row_y + 11), truncate(draw, free_v, font(11), 80),
              fill=TEXT_DIM, font=font(11))
    draw.text((SIDE + 290, row_y + 11), truncate(draw, paid_v, font(11, bold=True), 130),
              fill=PAID_COL, font=font(11, bold=True))
    row_y += 43

stats = [("Tiers", "2"), ("Question", "Worth it?"), ("Use", "Solo & teams")]
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
    initials    = "C",
    name        = "Canva Free vs Pro",
    tagline     = "Honest decision guide for 2026",
    line1       = "Free covers casual creators and one-offs",
    line2       = "Pro pays off for weekly, brand, team work",
    badge       = "Match the tier to real volume",
    license_note= "Free tier is generous · Pro removes friction",
)

draw_grid(draw, ACCENT, [
    (FREE_COL,  "Fr", "Stay Free",   "Casual users · students · one-offs"),
    (PAID_COL,  "Pr", "Go Pro",      "Brand kits · resize · team workflows"),
    ("#8b5cf6", "Bg", "Bg remover",  "Limited free · unlimited on Pro"),
    ("#ef4444", "Tm", "Teams",       "Shared assets · folders · roles"),
])

# ── BOTTOM BAR ──────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Canva Free vs Paid in 2026",
    subtitle = "Free plan limits  ·  Pro features  ·  Who should upgrade  ·  Common mistakes",
)

# ── Save ────────────────────────────────────────────────────────────────────
out = img_out("canva-free-vs-paid.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
