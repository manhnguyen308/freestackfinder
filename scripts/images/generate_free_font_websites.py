#!/usr/bin/env python3
"""
Feature image generator: Best Free Font Websites in 2026
Output : static/img/free-font-websites.webp  (1200×630 px)
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

# ── LEFT PANEL — mock font browser UI ───────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Google Fonts — Browse")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

# Search bar mock
rrect(draw, SIDE, 44, LEFT_W - SIDE, 66, 4, CARD_BG)
draw.text((SIDE + 10, 50), "Search fonts...", fill=TEXT_DIM, font=font(10))

# Filter pills
pills = ["Serif", "Sans-serif", "Monospace", "Display"]
px = SIDE
for p in pills:
    pw = len(p) * 7 + 16
    rrect(draw, px, 72, px + pw, 90, 6, CARD_BG)
    draw.text((px + 8, 75), p, fill=TEXT_DIM, font=font(9))
    px += pw + 6

# Font list items
fonts_list = [
    ("Roboto",       "Sans-serif  · 12 styles",  ACCENT),
    ("Open Sans",    "Sans-serif  · 10 styles",  "#fb923c"),
    ("Lato",         "Sans-serif  · 18 styles",  "#fbbf24"),
    ("Playfair",     "Serif  · 6 styles",        "#a3e635"),
    ("Inter",        "Sans-serif  · 18 styles",  "#38bdf8"),
    ("Merriweather", "Serif  · 4 styles",        "#c084fc"),
]
fy = 98
for name, meta, col in fonts_list:
    rrect(draw, SIDE, fy, LEFT_W - SIDE, fy + 34, 4, CARD_BG)
    draw_circle(draw, SIDE + 16, fy + 17, 10, col)
    draw.text((SIDE + 4, fy + 10),
              name[0].upper(),
              fill="#ffffff", font=font(9, bold=True))
    draw.text((SIDE + 32, fy + 5),
              truncate(draw, name, font(11, bold=True), CTX_W - 50),
              fill=TEXT_W, font=font(11, bold=True))
    draw.text((SIDE + 32, fy + 20),
              truncate(draw, meta, font(9), CTX_W - 50),
              fill=TEXT_DIM, font=font(9))
    fy += 40

# Stats row
stat_y = CONTENT_H - 42
stats = [("Families", "1,400+"), ("Styles", "20,000+"), ("OFL License", "All free")]
stat_x = SIDE
for label, val in stats:
    rrect(draw, stat_x, stat_y, stat_x + 118, stat_y + 34, 6, CARD_BG)
    draw.text((stat_x + 8, stat_y + 4),
              truncate(draw, label, font(9), 104),
              fill=TEXT_DIM, font=font(9))
    draw.text((stat_x + 8, stat_y + 18),
              truncate(draw, val, font(11, bold=True), 104),
              fill=TEXT_W, font=font(11, bold=True))
    stat_x += 126

# ── RIGHT PANEL ─────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials     = "Gf",
    name         = "Google Fonts",
    tagline      = "Best overall free font library",
    line1        = "1,400+ families · open-source licensed",
    line2        = "CDN embed or self-host download",
    badge        = "✓ 100% free — no account required",
    license_note = "SIL Open Font License — commercial use OK",
)

draw_grid(draw, ACCENT, [
    ("#22c55e", "FS", "Font Squirrel", "Curated · commercial-use vetted"),
    ("#f43f5e", "Da", "DaFont",        "90k+ fonts · check license"),
    ("#6366f1", "Fo", "Fontsource",    "npm self-host · GDPR-friendly"),
    ("#eab308", "1k", "1001 Fonts",    "45k+ · clear license labels"),
])

# ── BOTTOM BAR ──────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Font Websites in 2026",
    subtitle = "Google Fonts  ·  Font Squirrel  ·  DaFont  ·  Fontsource  ·  1001 Fonts",
)

# ── Save ────────────────────────────────────────────────────────────────────
out = img_out("free-font-websites.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
