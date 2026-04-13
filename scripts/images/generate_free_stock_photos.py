#!/usr/bin/env python3
"""
Feature image generator for: Best Free Stock Photo Sites in 2026
Output: static/img/free-stock-photos.jpg (1200x630px)
Silo: Creative  Accent: #f97316
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
BG       = "#101116"
CARD_BG  = "#1a1d27"
ACCENT   = "#f97316"   # Creative silo — orange
TEXT_W   = "#ffffff"
TEXT_DIM = "#8a8fa8"
WIN_BG   = "#13161f"

out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "static", "img")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "free-stock-photos.jpg")

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── font helpers ──────────────────────────────────────────────────────────────
def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def circle(cx, cy, r, color, text="", text_color="#ffffff", fnt=None):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)
    if text and fnt:
        bb = draw.textbbox((0, 0), text, font=fnt)
        tw, th = bb[2]-bb[0], bb[3]-bb[1]
        draw.text((cx - tw//2, cy - th//2), text, fill=text_color, font=fnt)

def rounded_rect(x0, y0, x1, y1, r, color):
    draw.rectangle([x0+r, y0, x1-r, y1], fill=color)
    draw.rectangle([x0, y0+r, x1, y1-r], fill=color)
    for cx, cy in [(x0+r, y0+r), (x1-r, y0+r), (x0+r, y1-r), (x1-r, y1-r)]:
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)

# ── layout constants ──────────────────────────────────────────────────────────
LEFT_W   = 480
RIGHT_X  = LEFT_W + 20
RIGHT_W  = W - RIGHT_X - 20
BOT_H    = 90
CONTENT_H = H - BOT_H

# ── LEFT PANEL — mock photo browser UI ───────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)

# macOS window chrome
chrome_y = 18
for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
    draw.ellipse([16 + i*22 - 6, chrome_y-6, 16 + i*22 + 6, chrome_y+6], fill=col)
draw.text((80, chrome_y - 7), "Unsplash — Free Stock Photos", fill=TEXT_DIM, font=font(12))

# Search bar mock
rounded_rect(20, 38, LEFT_W-20, 62, 8, CARD_BG)
draw.text((36, 45), "🔍  architecture interior minimal", fill=TEXT_DIM, font=font(12))

# Photo grid mock — 2 columns, 3 rows of placeholder photo tiles
TILE_W = (LEFT_W - 52) // 2
TILE_H = 72
colors_grid = [
    ("#2d3550", "#1e2a40", "#2a3048",
     "#1d2538", "#253040", "#20293c"),
]
tile_y = 74
tile_defs = [
    ("#2d3550", "Nature"),    ("#1e2a40", "Business"),
    ("#2a3048", "City"),      ("#1d2538", "People"),
    ("#253040", "Tech"),      ("#20293c", "Abstract"),
]
col_x = [22, 22 + TILE_W + 8]
row = 0
for i, (col, label) in enumerate(tile_defs):
    tx = col_x[i % 2]
    ty = tile_y + (i // 2) * (TILE_H + 8)
    rounded_rect(tx, ty, tx+TILE_W, ty+TILE_H, 6, col)
    # Small camera icon placeholder
    draw.text((tx + TILE_W//2 - 20, ty + TILE_H//2 - 14), "📷", font=font(14))
    draw.text((tx + 8, ty + TILE_H - 20), label, fill=TEXT_DIM, font=font(10))
    # CC0 badge on first tile
    if i == 0:
        rounded_rect(tx + TILE_W - 48, ty + 6, tx + TILE_W - 6, ty + 20, 3, ACCENT)
        draw.text((tx + TILE_W - 45, ty + 8), "CC0 Free", fill="#000000", font=font(8, bold=True))

# Attribution-free badge
bage_y = tile_y + 3 * (TILE_H + 8) + 10
rounded_rect(20, bage_y, 200, bage_y+28, 6, ACCENT + "33")
draw.text((30, bage_y+7), "✓ No attribution required", fill=ACCENT, font=font(12, bold=True))
draw.text((210, bage_y+7), "✓ Commercial use", fill=ACCENT, font=font(12, bold=True))

# Site count
draw.text((20, bage_y+46), "3,000,000+ photos · Free to download", fill=TEXT_DIM, font=font(11))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
FEAT_X = RIGHT_X
FEAT_W = RIGHT_W
FEAT_Y = 20
FEAT_H = 160

rounded_rect(FEAT_X, FEAT_Y, FEAT_X+FEAT_W, FEAT_Y+FEAT_H, 10, CARD_BG)
draw.rectangle([FEAT_X, FEAT_Y+10, FEAT_X+4, FEAT_Y+FEAT_H-10], fill=ACCENT)

circle(FEAT_X+44, FEAT_Y+50, 28, ACCENT, "U", "#000000", font(18, bold=True))

draw.text((FEAT_X+84, FEAT_Y+22), "Unsplash", fill=TEXT_W, font=font(20, bold=True))
draw.text((FEAT_X+84, FEAT_Y+50), "Best overall quality", fill=ACCENT, font=font(13))
draw.text((FEAT_X+84, FEAT_Y+72), "3M+ photos · No attribution", fill=TEXT_DIM, font=font(12))
draw.text((FEAT_X+84, FEAT_Y+90), "Free personal + commercial use", fill=TEXT_DIM, font=font(12))

draw.text((FEAT_X+14, FEAT_Y+120), "✓ No registration required", fill=ACCENT, font=font(12, bold=True))
draw.text((FEAT_X+14, FEAT_Y+138), "Unsplash License — no attribution, no fee", fill=TEXT_DIM, font=font(11))

# 2×2 comparison grid
tools_grid = [
    ("#05a081", "PE", "Pexels",       "3M+ photos · 60K+ videos"),
    ("#1f8400", "PX", "Pixabay",      "4M+ · photos + vectors"),
    ("#96bf48", "BU", "Burst",        "E-commerce · Shopify"),
    ("#e84445", "RS", "Reshot",       "50K+ authentic images"),
]

GRID_Y = FEAT_Y + FEAT_H + 16
CELL_W = (FEAT_W - 12) // 2
CELL_H = 90

for i, (col, initials, name, sub) in enumerate(tools_grid):
    col_off = i % 2
    row_off = i // 2
    cx = FEAT_X + col_off * (CELL_W + 12)
    cy = GRID_Y + row_off * (CELL_H + 12)

    rounded_rect(cx, cy, cx+CELL_W, cy+CELL_H, 8, CARD_BG)
    circle(cx+30, cy+CELL_H//2, 22, col, initials, "#ffffff", font(11, bold=True))
    draw.text((cx+62, cy+18), name, fill=TEXT_W, font=font(13, bold=True))
    draw.text((cx+62, cy+38), sub, fill=TEXT_DIM, font=font(10))

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
BAR_Y = CONTENT_H
draw.rectangle([0, BAR_Y, W, H], fill=ACCENT)

draw.text((28, BAR_Y+12), "FreeStackFinder.com", fill="#000000", font=font(12, bold=True))
draw.text((28, BAR_Y+34), "Best Free Stock Photo Sites in 2026", fill="#000000", font=font(22, bold=True))
draw.text((28, BAR_Y+66), "Unsplash  ·  Pexels  ·  Pixabay  ·  Burst  ·  Reshot", fill="#000000", font=font(13))

# ── save ──────────────────────────────────────────────────────────────────────
img.save(out_path, "JPEG", quality=92)
print(f"Saved: {out_path}")
