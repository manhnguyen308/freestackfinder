#!/usr/bin/env python3
"""
Feature image generator: Best Free Website Builders in 2026
Output : static/img/free-website-builders.webp  (1200×630 px)
Silo   : Business   Accent: #10b981
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

ACCENT = "#10b981"   # Business silo — emerald

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock website builder / page editor UI ───────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Website Builder — Page Editor")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2   # 440px

# Section label
draw.text((SIDE, 44), "Page sections", fill=TEXT_DIM, font=font(11, bold=True))

# Simulate page section blocks being arranged in the editor
sections = [
    (ACCENT,    "HEADER",  "Hero — headline + call to action"),
    ("#3b82f6", "ABOUT",   "About — short intro + photo"),
    ("#6366f1", "SERVICES","Services — 3-column feature grid"),
    ("#f59e0b", "GALLERY", "Gallery — image portfolio"),
    ("#8b5cf6", "CONTACT", "Contact — form + map embed"),
]

blk_y = 64
for col, tag, desc in sections:
    rrect(draw, SIDE, blk_y, LEFT_W - SIDE, blk_y + 38, 5, CARD_BG)
    # Left color bar
    draw.rectangle([SIDE, blk_y, SIDE + 5, blk_y + 38], fill=col)
    # Tag pill
    PILL_W = 72
    rrect(draw, SIDE + 12, blk_y + 9, SIDE + 12 + PILL_W, blk_y + 28, 4, col + "30")
    draw.text((SIDE + 16, blk_y + 11),
              tag, fill=col, font=font(10, bold=True))
    # Description
    draw.text((SIDE + 92, blk_y + 12),
              truncate(draw, desc, font(10), CTX_W - 80),
              fill=TEXT_DIM, font=font(10))
    blk_y += 45

# Add/drag hint
draw.text((SIDE, blk_y + 8), "+ Drag to reorder  ·  + Add section",
          fill=TEXT_DIM, font=font(9))

# Stats bar at bottom of left panel
stats = [("Templates", "800+"), ("Sections", "Free"), ("Hosting", "Included")]
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
    initials    = "Wx",
    name        = "Wix",
    tagline     = "Most features on a free plan",
    line1       = "800+ templates · full drag-and-drop editor",
    line2       = "App market · SEO tools · mobile editor",
    badge       = "Free plan · wixsite.com subdomain",
    license_note= "Freemium — custom domain requires paid plan",
)

draw_grid(draw, ACCENT, [
    ("#34a853", "GS", "Google Sites",    "100% free · no ads · multi-page"),
    ("#3b82f6", "WP", "WordPress.com",   "Best for blogs · unlimited posts"),
    ("#1a1a2e", "Ca", "Carrd",           "Clean one-pager · fast setup"),
    ("#7c3aed", "CV", "Canva Websites",  "Design-to-web · Canva users"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Website Builders in 2026",
    subtitle = "Wix  ·  Google Sites  ·  WordPress.com  ·  Carrd  ·  Canva Websites",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-website-builders.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
