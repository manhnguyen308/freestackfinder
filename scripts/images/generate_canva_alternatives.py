#!/usr/bin/env python3
"""
Feature image generator: Free Canva alternatives in 2026
Output : static/img/canva-alternatives.webp  (1200x630 px)
Silo   : Creative   Accent: #f97316

Replaces a 1200x1500 portrait stock photo. Tool facts come from
content/creative/canva-alternatives.md. Template thumbnails are drawn shapes.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_MID,
    card_window, card_featured, card_grid, card_bar, mix, logo_path,
)

ACCENT = "#f97316"   # Creative silo, orange

c = Canvas()

# ── LEFT PANEL: template picker by format ─────────────────────────────────────
x0, y0, x1, y1 = card_window(c, "Adobe Express: templates")

# Format tabs taken from the article: social posts, flyers, presentations, video
tx = x0
for i, label in enumerate(["Social post", "Flyer", "Presentation", "Video"]):
    if i == 0:
        tx += c.pill(tx, y0 - 6, label, 13, "#101116", ACCENT, h=28) + 8
    else:
        tx += c.pill(tx, y0 - 6, label, 13, TEXT_MID, CARD_BG, h=28) + 8

GAP = 14
cw = (x1 - x0 - GAP * 2) / 3
top, bottom = y0 + 36, y1


def social(ax, ay, bx, by):
    c.rect(ax, ay, bx, by, "#fb7185", r=8)
    c.circle(bx - 34, ay + 36, 22, "#fde68a")
    c.rect(ax + 14, by - 52, ax + 96, by - 38, "#ffffff", r=4)
    c.rect(ax + 14, by - 30, ax + 70, by - 20, "#ffe4e6", r=4)


def flyer(ax, ay, bx, by):
    c.rect(ax, ay, bx, by, "#1e3a8a", r=8)
    c.rect(ax + 14, ay + 16, bx - 14, ay + 30, "#fbbf24", r=4)
    c.rect(ax + 14, ay + 38, bx - 40, ay + 48, "#93c5fd", r=4)
    c.circle((ax + bx) / 2, (ay + by) / 2 + 20, 34, "#3b82f6")
    c.circle((ax + bx) / 2, (ay + by) / 2 + 20, 20, "#60a5fa")
    c.rect(ax + 14, by - 34, ax + 76, by - 14, "#fbbf24", r=10)


def slide(ax, ay, bx, by):
    c.rect(ax, ay, bx, by, "#f5f5f4", r=8)
    c.rect(ax + 12, ay + 14, ax + 78, ay + 24, "#1c1917", r=3)
    c.rect(ax + 12, ay + 32, ax + 60, ay + 38, "#a8a29e", r=2)
    for k, h in enumerate([18, 30, 24, 38]):
        c.rect(bx - 70 + k * 14, by - 12 - h, bx - 60 + k * 14, by - 12, ACCENT, r=2)


def quote(ax, ay, bx, by):
    c.rect(ax, ay, bx, by, "#134e4a", r=8)
    c.text(ax + 16, ay + 8, "“", 54, "#5eead4", "bold")
    c.rect(ax + 16, ay + 64, bx - 16, ay + 74, "#ccfbf1", r=4)
    c.rect(ax + 16, ay + 82, bx - 40, ay + 92, "#ccfbf1", r=4)
    c.rect(ax + 16, ay + 104, ax + 60, ay + 110, "#5eead4", r=3)


def story(ax, ay, bx, by):
    c.rect(ax, ay, bx, by, "#4c1d95", r=8)
    c.circle((ax + bx) / 2, ay + 64, 32, "#a78bfa")
    c.circle((ax + bx) / 2, ay + 64, 18, "#ede9fe")
    c.rect(ax + 16, ay + 116, bx - 16, ay + 128, "#ffffff", r=4)
    c.rect(ax + 16, ay + 136, bx - 36, ay + 144, "#c4b5fd", r=3)
    c.rect(ax + 16, by - 34, bx - 16, by - 14, "#f97316", r=10)


def promo(ax, ay, bx, by):
    c.rect(ax, ay, bx, by, "#fef3c7", r=8)
    c.rect(ax + 12, ay + 14, ax + 50, ay + 40, "#f97316", r=6)
    c.rect(ax + 60, ay + 16, bx - 12, ay + 24, "#78350f", r=3)
    c.rect(ax + 60, ay + 30, bx - 30, ay + 36, "#b45309", r=3)


# Column 1: square post, then a quote card
col = x0
social(col, top, col + cw, top + cw)
quote(col, top + cw + GAP, col + cw, bottom)
# Column 2: tall flyer, then a short promo
col = x0 + cw + GAP
flyer(col, top, col + cw, bottom - 70)
promo(col, bottom - 56, col + cw, bottom)
# Column 3: 16:9 slide, then a story
col = x0 + (cw + GAP) * 2
slide(col, top, col + cw, top + cw * 9 / 16)
story(col, top + cw * 9 / 16 + GAP, col + cw, bottom)

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "AE",
    logo     = logo_path("adobe-express.png"),
    name     = "Adobe Express",
    tagline  = "Best overall free Canva alternative",
    note     = "Templates, basic photo and video tools, and limited storage on the free tier",
)

card_grid(c, [
    ("#3b82f6", "Pp", "Photopea",           "Layers, masks, and PSD files in a browser", logo_path("photopea.png")),
    ("#22c55e", "MD", "Microsoft Designer", "AI-assisted first drafts with a Microsoft account", logo_path("microsoft-designer.png")),
    ("#8b5cf6", "Px", "Pixlr",              "Quick browser edits and photo cleanup", logo_path("pixlr.png")),
    ("#ec4899", "Pi", "Picsart",            "Phone-first photo effects and social assets", logo_path("picsart.png")),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
card_bar(
    c, ACCENT,
    title    = "Free Canva alternatives in 2026",
    subtitle = "Adobe Express  ·  Photopea  ·  Microsoft Designer  ·  Pixlr  ·  Picsart",
)

c.save("canva-alternatives.webp")
