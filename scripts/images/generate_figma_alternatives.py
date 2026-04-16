#!/usr/bin/env python3
"""
Feature image generator: Best Free Figma Alternatives in 2026
Output : static/img/figma-alternatives.webp  (1200×630 px)
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

# ── LEFT PANEL — mock Figma-style UI design canvas ──────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "UI Design — Penpot")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

# Layer panel header
draw.text((SIDE, 44), "Layers", fill=TEXT_DIM, font=font(11, bold=True))

# Layer items
layers = [
    ("Frame", "Header",    ACCENT),
    ("Text",  "Hero Title", "#ffffff"),
    ("Rect",  "CTA Button", "#22c55e"),
    ("Image", "Hero Image", "#3b82f6"),
    ("Frame", "Nav Bar",    "#8b5cf6"),
    ("Group", "Card Grid",  "#f59e0b"),
]
ly = 62
for kind, name, col in layers:
    rrect(draw, SIDE, ly, LEFT_W - SIDE, ly + 28, 4, CARD_BG)
    draw.rectangle([SIDE + 4, ly + 6, SIDE + 16, ly + 22], fill=col + "44", outline=col)
    draw.text((SIDE + 24, ly + 6),
              truncate(draw, f"{kind}: {name}", font(10), CTX_W - 40),
              fill=TEXT_W, font=font(10))
    ly += 34

# Mock canvas area below layers — simple wireframe sketch
canvas_y = ly + 10
canvas_h = CONTENT_H - canvas_y - 50
canvas_w = CTX_W
cx, cy = SIDE, canvas_y

# Canvas background
rrect(draw, cx, cy, cx + canvas_w, cy + canvas_h, 6, CARD_BG)

# Nav bar wireframe
rrect(draw, cx + 8, cy + 8, cx + canvas_w - 8, cy + 28, 3, "#1e2130")
draw.rectangle([cx + 14, cy + 14, cx + 50, cy + 22], fill=ACCENT + "66")
for bx in range(0, 4):
    draw.rectangle([cx + canvas_w - 80 + bx * 18, cy + 14,
                     cx + canvas_w - 66 + bx * 18, cy + 22], fill="#4b556388")

# Hero area wireframe
rrect(draw, cx + 8, cy + 34, cx + canvas_w // 2 - 2, cy + canvas_h - 8, 3, "#1e2130")
draw.rectangle([cx + 16, cy + 44, cx + 140, cy + 54], fill="#ffffff22")
draw.rectangle([cx + 16, cy + 60, cx + 120, cy + 66], fill="#ffffff11")
rrect(draw, cx + 16, cy + 74, cx + 80, cy + 88, 3, ACCENT + "88")

# Image placeholder wireframe
rrect(draw, cx + canvas_w // 2 + 2, cy + 34, cx + canvas_w - 8, cy + canvas_h - 8, 3, "#1e2130")
# Cross lines for image placeholder
img_x0 = cx + canvas_w // 2 + 2
img_y0 = cy + 34
img_x1 = cx + canvas_w - 8
img_y1 = cy + canvas_h - 8
draw.line([(img_x0 + 4, img_y0 + 4), (img_x1 - 4, img_y1 - 4)], fill="#4b556344", width=1)
draw.line([(img_x1 - 4, img_y0 + 4), (img_x0 + 4, img_y1 - 4)], fill="#4b556344", width=1)

# Properties panel label at bottom
stat_y = CONTENT_H - 42
stats = [("Frames", "6"), ("Components", "12"), ("Fonts", "2")]
stat_x = SIDE
for label, val in stats:
    rrect(draw, stat_x, stat_y, stat_x + 126, stat_y + 34, 6, CARD_BG)
    draw.text((stat_x + 8, stat_y + 4),
              truncate(draw, label, font(9), 110),
              fill=TEXT_DIM, font=font(9))
    draw.text((stat_x + 8, stat_y + 18),
              truncate(draw, val, font(12, bold=True), 110),
              fill=TEXT_W, font=font(12, bold=True))
    stat_x += 134

# ── RIGHT PANEL ─────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "Pp",
    name        = "Penpot",
    tagline     = "Best free Figma alternative overall",
    line1       = "Unlimited users · unlimited projects",
    line2       = "Open-source · self-hosted option",
    badge       = "✓ 100% free — no paid tier exists",
    license_note= "Open-source (MPL 2.0) — free forever",
)

draw_grid(draw, ACCENT, [
    ("#42a5f5", "Lu", "Lunacy",      "Free desktop app · built-in assets"),
    ("#7c3aed", "Pl", "Plasmic",     "Visual design → React code"),
    ("#10b981", "QU", "Quant UX",    "Prototyping + usability testing"),
    ("#0acf83", "Fi", "Figma Free",  "3 team files · industry standard"),
])

# ── BOTTOM BAR ──────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Figma Alternatives in 2026",
    subtitle = "Penpot  ·  Lunacy  ·  Plasmic  ·  Quant UX  ·  Figma Starter",
)

# ── Save ────────────────────────────────────────────────────────────────────
out = img_out("figma-alternatives.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
