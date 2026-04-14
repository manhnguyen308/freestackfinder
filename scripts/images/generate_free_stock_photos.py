#!/usr/bin/env python3
"""
Feature image generator: Best Free Stock Photo Sites in 2026
Output : static/img/free-stock-photos.webp  (1200×630 px)
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

# ── LEFT PANEL — mock photo browser ───────────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Unsplash — Free Stock Photos")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2   # 440px

# Search bar
rrect(draw, SIDE, 38, LEFT_W - SIDE, 62, 8, CARD_BG)
draw.text((SIDE + 14, 46),
          truncate(draw, "🔍  architecture  interior  minimal", font(11), CTX_W - 20),
          fill=TEXT_DIM, font=font(11))

# Photo tile grid — 2 columns × 3 rows
TILE_W  = (CTX_W - 10) // 2
TILE_H  = 72
tile_x0 = [SIDE, SIDE + TILE_W + 10]
tiles   = [
    ("#2d3550", "Nature"),  ("#1e2a40", "Business"),
    ("#2a3048", "City"),    ("#1d2538", "People"),
    ("#253040", "Tech"),    ("#20293c", "Abstract"),
]
for i, (col, label) in enumerate(tiles):
    tx = tile_x0[i % 2]
    ty = 72 + (i // 2) * (TILE_H + 8)
    rrect(draw, tx, ty, tx + TILE_W, ty + TILE_H, 6, col)
    # Camera placeholder
    draw.text((tx + TILE_W // 2 - 10, ty + TILE_H // 2 - 10),
              "📷", font=font(14))
    draw.text((tx + 8, ty + TILE_H - 18),
              truncate(draw, label, font(9), TILE_W - 16),
              fill=TEXT_DIM, font=font(9))
    # CC0 badge on first tile only
    if i == 0:
        bw = TILE_W - 12
        rrect(draw, tx + TILE_W - bw // 2 - 20, ty + 6,
              tx + TILE_W - 6, ty + 20, 3, ACCENT)
        draw.text((tx + TILE_W - bw // 2 - 16, ty + 8),
                  "CC0", fill="#000000", font=font(8, bold=True))

# Attribution / commercial use badges
badge_y = 72 + 3 * (TILE_H + 8) + 8
rrect(draw, SIDE, badge_y, SIDE + 200, badge_y + 26, 6, ACCENT + "33")
draw.text((SIDE + 10, badge_y + 6),
          "✓ No attribution required", fill=ACCENT, font=font(11, bold=True))

rrect(draw, SIDE + 208, badge_y, SIDE + 390, badge_y + 26, 6, ACCENT + "33")
draw.text((SIDE + 218, badge_y + 6),
          "✓ Commercial use", fill=ACCENT, font=font(11, bold=True))

# Photo count
draw.text((SIDE, badge_y + 36),
          truncate(draw, "3,000,000+ photos · free to download · no sign-up needed",
                   font(10), CTX_W),
          fill=TEXT_DIM, font=font(10))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "U",
    name        = "Unsplash",
    tagline     = "Best overall quality",
    line1       = "3M+ photos · no attribution required",
    line2       = "Free for personal and commercial use",
    badge       = "✓ No registration required",
    license_note= "Unsplash License — no attribution, no fee",
)

draw_grid(draw, ACCENT, [
    ("#05a081", "PE", "Pexels",   "3M+ photos · 60K+ videos · CC0"),
    ("#1f8400", "PX", "Pixabay",  "4M+ items · photos + vectors"),
    ("#96bf48", "BU", "Burst",    "E-commerce focus · Shopify"),
    ("#e84445", "RS", "Reshot",   "50K+ authentic images · free"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Stock Photo Sites in 2026",
    subtitle = "Unsplash  ·  Pexels  ·  Pixabay  ·  Burst  ·  Reshot",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-stock-photos.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
