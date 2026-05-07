#!/usr/bin/env python3
"""
Feature image generator: Best Free Open-Source Video Editors in 2026
Output : static/img/free-open-source-video-editors.webp  (1200×630 px)
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

# ── LEFT PANEL — open-source editor comparison panel ─────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Open-Source Video Editors — 2026 Comparison")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

draw.text((SIDE, 44), "Editor & open-source status", fill=TEXT_DIM, font=font(11, bold=True))

editors = [
    (ACCENT,    "Kdenlive",     "Multi-track NLE · GPL · all platforms",  "Best all-round pick"),
    ("#22c55e", "Shotcut",      "FFmpeg · broad format support · GPL",     "Format compatibility"),
    ("#3b82f6", "OpenShot",     "Drag-and-drop · GPL · beginner-friendly", "Best for beginners"),
    ("#f97316", "Blender VSE",  "3D integration · GPL · node compositor",  "Blender users"),
    ("#8b5cf6", "Olive",        "Node-based · GPL · pre-release",          "Worth tracking"),
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

stats = [("Editors compared", "5"), ("License", "GPL · Free"), ("Platforms", "Win/Mac/Linux")]
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
    initials    = "KD",
    name        = "Kdenlive",
    tagline     = "Best all-round open-source NLE",
    line1       = "Multi-track · proxy editing · 4K support",
    line2       = "KDE project · GPL · Windows, Mac, Linux",
    badge       = "Best overall open-source pick",
    license_note= "Free forever — no watermarks, no paid tier",
)

draw_grid(draw, ACCENT, [
    ("#22c55e", "SC", "Shotcut",     "FFmpeg formats · GPL · multi-track · cross-platform"),
    ("#3b82f6", "OS", "OpenShot",    "Beginner-friendly · GPL · simple timeline · free"),
    ("#f97316", "BL", "Blender VSE", "3D integration · GPL · node compositor · free"),
    ("#8b5cf6", "OL", "Olive",       "Node-based compositing · GPL · pre-release"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Open-Source Video Editors in 2026",
    subtitle = "Kdenlive  ·  Shotcut  ·  OpenShot  ·  Blender VSE  ·  Olive",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-open-source-video-editors.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
