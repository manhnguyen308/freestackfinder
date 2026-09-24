#!/usr/bin/env python3
"""
Feature image generator: Free stock photo sites in 2026
Output : static/img/free-stock-photos.webp  (1200x630 px)
Silo   : Creative   Accent: #f97316

Library facts come from content/creative/free-stock-photos.md, which compares
Unsplash, Pexels, Pixabay, and Burst. Photo tiles are drawn shapes, not photos.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_DIM, TEXT_MID, GOOD, WARN,
    card_window, card_featured, card_grid, card_bar, mix, logo_path, glyph,
)

ACCENT = "#f97316"   # Creative silo, orange

c = Canvas()

# ── LEFT PANEL: search bar, result tiles, license chips ───────────────────────
x0, y0, x1, y1 = card_window(c, "Free photo library")

# Search bar with a drawn magnifier
c.rect(x0, y0 - 4, x1, y0 + 34, CARD_BG, r=19)
c.circle(x0 + 24, y0 + 13, 7, None, outline=TEXT_DIM, width=2)
c.line([(x0 + 29, y0 + 18), (x0 + 35, y0 + 24)], TEXT_DIM, 2)
c.text(x0 + 46, y0 + 15, "Search free photos", 15, TEXT_DIM, anchor="lm")

GAP = 12
tw = (x1 - x0 - GAP * 2) / 3
th = 112
ty0 = y0 + 48


def tile(i, painter, bg):
    col, row = i % 3, i // 3
    tx = x0 + col * (tw + GAP)
    ty = ty0 + row * (th + GAP)
    c.rect(tx, ty, tx + tw, ty + th, bg, r=8)
    painter(tx, ty)


def mountains(tx, ty):
    c.circle(tx + tw - 34, ty + 28, 12, "#fde68a")
    c.poly([(tx + 6, ty + th - 6), (tx + 52, ty + 36), (tx + 92, ty + th - 6)], "#4c5b8f")
    c.poly([(tx + 56, ty + th - 6), (tx + 102, ty + 48), (tx + tw - 6, ty + th - 6)], "#6d7fc0")


def sunset(tx, ty):
    c.circle(tx + tw / 2, ty + 58, 22, "#fb923c")
    c.rect(tx + 4, ty + 60, tx + tw - 4, ty + th - 4, "#7c2d12", r=6)
    for k in range(3):
        c.rect(tx + 24 + k * 10, ty + 70 + k * 8, tx + tw - 24 - k * 10, ty + 73 + k * 8, "#fdba74", r=1)


def city(tx, ty):
    heights = [40, 62, 34, 70, 48, 56]
    bw = (tw - 20) / len(heights)
    for k, h in enumerate(heights):
        bx = tx + 10 + k * bw
        c.rect(bx, ty + th - 8 - h, bx + bw - 4, ty + th - 8, "#94a3b8" if k % 2 else "#64748b", r=2)


def product(tx, ty):
    c.rect(tx + tw / 2 - 30, ty + th - 22, tx + tw / 2 + 30, ty + th - 14, "#1e293b", r=4)
    c.rect(tx + tw / 2 - 22, ty + 30, tx + tw / 2 + 22, ty + th - 20, "#f472b6", r=8)
    c.rect(tx + tw / 2 - 12, ty + 22, tx + tw / 2 + 12, ty + 32, "#be185d", r=3)


def abstract(tx, ty):
    c.circle(tx + 46, ty + 50, 28, "#8b5cf6")
    c.circle(tx + 80, ty + 44, 22, "#22d3ee")
    c.circle(tx + 104, ty + 66, 18, "#f59e0b")


def forest(tx, ty):
    for k, (dx, r, col) in enumerate([(34, 22, "#15803d"), (74, 28, "#16a34a"), (114, 20, "#22c55e")]):
        c.rect(tx + dx - 3, ty + 56, tx + dx + 3, ty + th - 10, "#78350f")
        c.circle(tx + dx, ty + 50, r, col)


tile(0, mountains, "#1e2a4a")
tile(1, sunset,    "#3b1d0e")
tile(2, city,      "#1e293b")
tile(3, product,   "#fce7f3")
tile(4, abstract,  "#1a1d27")
tile(5, forest,    "#0f2a1c")

cy = ty0 + 2 * th + GAP + 16
cx = x0
for label, col in [("Commercial use", GOOD), ("No attribution", GOOD), ("Check people and logos", WARN)]:
    cx += c.pill(cx, cy, label, 13, col, mix(col, WIN_BG, 0.78), h=28) + 10

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "U",
    logo     = logo_path("unsplash.png"),
    name     = "Unsplash",
    tagline  = "Best overall for photography quality",
    note     = "No attribution required. Model releases are not guaranteed for every image",
)

card_grid(c, [
    ("#22c55e", "Pe", "Pexels",     "Photos and video clips in one library", logo_path("pexels.png")),
    ("#3b82f6", "Pi", "Pixabay",    "Photos, vectors, video, and music", logo_path("pixabay.png")),
    ("#8b5cf6", "Bu", "Burst",      "Product and e-commerce photos from Shopify", logo_path("shopify-burst.png")),
    ("#64748b", "Pd", "Paid stock", "Worth it when releases or exclusivity matter", glyph("tag", "#64748b")),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
card_bar(
    c, ACCENT,
    title    = "Free stock photo sites in 2026",
    subtitle = "Unsplash  ·  Pexels  ·  Pixabay  ·  Burst",
)

c.save("free-stock-photos.webp")
