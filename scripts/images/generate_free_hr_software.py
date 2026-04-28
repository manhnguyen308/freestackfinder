#!/usr/bin/env python3
"""
Feature image generator: Best Free HR Software in 2026
Output : static/img/free-hr-software.webp  (1200×630 px)
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

# ── LEFT PANEL — mock HR dashboard ──────────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "HR Overview — Team Status")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

# Section label
draw.text((SIDE, 44), "People at a glance", fill=TEXT_DIM, font=font(11, bold=True))

# HR metric rows
metrics = [
    (ACCENT,    "Employees",        "8",     "Active"),
    ("#3b82f6", "Leave requests",   "3",     "Pending"),
    ("#6366f1", "Onboarding",       "1",     "In progress"),
    ("#f59e0b", "Documents",        "12",    "On file"),
    ("#8b5cf6", "Time tracked",     "40 h",  "This week"),
]

row_y = 64
for col, label, value, status in metrics:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 36, 5, CARD_BG)
    draw.rectangle([SIDE, row_y, SIDE + 4, row_y + 36], fill=col)
    draw.text((SIDE + 12, row_y + 4),  label,  fill=TEXT_DIM, font=font(10))
    draw.text((SIDE + 12, row_y + 18), value,  fill=TEXT_W,   font=font(12, bold=True))
    draw.text((LEFT_W - SIDE - 80, row_y + 12),
              truncate(draw, status, font(9), 76),
              fill=col, font=font(9, bold=True))
    row_y += 43

# Stats bar at bottom of left panel
stats = [("Employees", "8"), ("On leave", "2"), ("Open roles", "1")]
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
    initials    = "ZP",
    name        = "Zoho People",
    tagline     = "Best cloud HRIS for small teams",
    line1       = "Up to 5 employees · leave management · self-service",
    line2       = "Employee records · onboarding checklists · reports",
    badge       = "Free up to 5 employees",
    license_note= "Free tier — paid plans unlock larger teams",
)

draw_grid(draw, ACCENT, [
    ("#f97316", "OR", "OrangeHRM",   "Open source · self-hosted · no user cap"),
    ("#22c55e", "HB", "Homebase",    "Scheduling · time clock · 1 location free"),
    ("#1a1a2e", "B2", "Bitrix24",    "Unlimited users · leave calendar · HR drive"),
    ("#34a853", "GS", "Google Sheets","DIY records · leave tracking · always free"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free HR Software in 2026",
    subtitle = "Zoho People  ·  OrangeHRM  ·  Homebase  ·  Bitrix24",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-hr-software.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
