#!/usr/bin/env python3
"""
Feature image generator: Best Free Video Editing Software for Mac in 2026
Output : static/img/free-video-editing-mac.webp  (1200×630 px)
Silo   : Video   Accent: #ef4444
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

ACCENT = "#ef4444"   # Video silo — red

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock Mac editor dashboard ────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Mac Video Editors — Free Tier Comparison")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

draw.text((SIDE, 44), "Editor & Mac support", fill=TEXT_DIM, font=font(11, bold=True))

editors = [
    (ACCENT,    "iMovie",          "Pre-installed · Apple Silicon",  "No trial · no watermark"),
    ("#22c55e", "DaVinci Resolve", "macOS 12.4+ · M-chip optimized", "Full color + audio free"),
    ("#3b82f6", "CapCut Desktop",  "Intel + Apple Silicon",          "Auto-captions · templates"),
    ("#f97316", "Kdenlive",        "macOS — open-source",            "Multi-track · FOSS"),
    ("#8b5cf6", "Shotcut",         "Native Apple Silicon build",     "FFmpeg · broad formats"),
]

row_y = 64
for col, label, value, status in editors:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 36, 5, CARD_BG)
    draw.rectangle([SIDE, row_y, SIDE + 4, row_y + 36], fill=col)
    draw.text((SIDE + 12, row_y + 4),  label,  fill=TEXT_DIM, font=font(10))
    draw.text((SIDE + 12, row_y + 18), value,  fill=TEXT_W,   font=font(12, bold=True))
    draw.text((LEFT_W - SIDE - 100, row_y + 12),
              truncate(draw, status, font(9), 96),
              fill=col, font=font(9, bold=True))
    row_y += 43

stats = [("Editors compared", "5"), ("Free forever", "All 5"), ("macOS native", "All 5")]
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

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "iM",
    name        = "iMovie",
    tagline     = "Best free Mac video editor for most users",
    line1       = "Pre-installed · 4K export · Apple Silicon native",
    line2       = "No watermark · iCloud sync · iPhone handoff",
    badge       = "Free with every Mac",
    license_note= "No trial — permanently free",
)

draw_grid(draw, ACCENT, [
    ("#22c55e", "DR", "DaVinci Resolve", "Pro color + audio · M-chip optimized · no watermark"),
    ("#3b82f6", "CC", "CapCut Desktop",  "Auto-captions · social templates · Apple Silicon"),
    ("#f97316", "KD", "Kdenlive",        "Open-source · multi-track · no paid tier"),
    ("#8b5cf6", "SC", "Shotcut",         "FFmpeg formats · Apple Silicon build · free"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Video Editing Software for Mac in 2026",
    subtitle = "iMovie  ·  DaVinci Resolve  ·  CapCut  ·  Kdenlive  ·  Shotcut",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-video-editing-mac.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
