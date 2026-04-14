#!/usr/bin/env python3
"""
Feature image generator: Best Free CRM Software in 2026
Output : static/img/free-crm-software.jpg  (1200×630 px)
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

# ── LEFT PANEL — mock CRM contacts + pipeline UI ──────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "CRM — HubSpot Free")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2   # 440px

# Pipeline bar label
draw.text((SIDE, 44), "Pipeline", fill=TEXT_DIM, font=font(11, bold=True))

# Pipeline stage track
stages = [
    ("Lead",      0.20, "#4b5563"),
    ("Qualified", 0.38, ACCENT + "aa"),
    ("Proposal",  0.26, ACCENT),
    ("Closed",    0.16, "#34d399"),
]
BAR_X = SIDE
BAR_Y0 = 62
BAR_H  = 18
BAR_FULL_W = CTX_W
x_cursor = BAR_X
for label, frac, color in stages:
    seg_w = int(BAR_FULL_W * frac)
    if seg_w < 2:
        seg_w = 2
    draw.rectangle([x_cursor, BAR_Y0, x_cursor + seg_w, BAR_Y0 + BAR_H], fill=color)
    if seg_w > 36:
        draw.text((x_cursor + 4, BAR_Y0 + 3),
                  truncate(draw, label, font(9, bold=True), seg_w - 6),
                  fill="#000000", font=font(9, bold=True))
    x_cursor += seg_w

# Column header for contacts table
hdr_y = 90
draw.rectangle([SIDE, hdr_y, LEFT_W - SIDE, hdr_y + 18], fill=ACCENT + "28")
draw.text((SIDE + 44, hdr_y + 3), "Name / Company",
          fill=ACCENT, font=font(10, bold=True))
draw.text((LEFT_W - 96, hdr_y + 3), "Stage",
          fill=ACCENT, font=font(10, bold=True))

# Contact rows
contacts = [
    ("#34a853", "SC", "Sarah Chen",    "Acme Corp",    "Qualified"),
    ("#3b82f6", "JP", "James Park",    "TechCo Ltd",   "Proposal"),
    ("#f59e0b", "LW", "Lisa Wong",     "StartUp Inc",  "Lead"),
    ("#8b5cf6", "MS", "Marco Silva",   "Corp Group",   "Closed Won"),
    ("#ef4444", "RT", "Rachel Torres", "Bright Media", "Lead"),
]
row_y = hdr_y + 22
for col, initials, name, company, stage in contacts:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 34, 4, CARD_BG)

    draw_circle(draw, SIDE + 16, row_y + 17, 12, col,
                initials[:2], "#ffffff", font(9, bold=True))

    draw.text((SIDE + 34, row_y + 4),
              truncate(draw, name, font(11, bold=True), 120),
              fill=TEXT_W, font=font(11, bold=True))
    draw.text((SIDE + 34, row_y + 19),
              truncate(draw, company, font(9), 120),
              fill=TEXT_DIM, font=font(9))

    # Stage pill
    stage_color = ACCENT if stage == "Closed Won" else (
        ACCENT + "88" if stage == "Proposal" else "#4b556388"
    )
    PILL_W = 80
    pill_x = LEFT_W - SIDE - PILL_W - 4
    rrect(draw, pill_x, row_y + 8, pill_x + PILL_W, row_y + 26, 4, stage_color)
    draw.text((pill_x + 6, row_y + 10),
              truncate(draw, stage, font(9), PILL_W - 10),
              fill="#000000", font=font(9, bold=True))

    row_y += 40

# Stats row at bottom
stats = [("Contacts", "—"), ("Deals", "—"), ("Users", "3 free")]
stat_x = SIDE
stat_y = CONTENT_H - 42
for label, val in stats:
    rrect(draw, stat_x, stat_y, stat_x + 126, stat_y + 34, 6, CARD_BG)
    draw.text((stat_x + 8, stat_y + 4),
              truncate(draw, label, font(9), 110),
              fill=TEXT_DIM, font=font(9))
    draw.text((stat_x + 8, stat_y + 18),
              truncate(draw, val, font(12, bold=True), 110),
              fill=TEXT_W, font=font(12, bold=True))
    stat_x += 134

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "HS",
    name        = "HubSpot CRM",
    tagline     = "Best free CRM overall",
    line1       = "Unlimited contacts · unlimited users",
    line2       = "Pipeline, email, forms — all free",
    badge       = "✓ Free forever — no credit card needed",
    license_note= "Freemium — advanced features in paid tiers",
)

draw_grid(draw, ACCENT, [
    ("#e34c26", "ZC", "Zoho CRM",    "3 users free · automations"),
    ("#06b6d4", "FS", "Freshsales",  "3 users free · built-in phone"),
    ("#1a56db", "B2", "Bitrix24",    "Unlimited users · tasks + chat"),
    ("#7c3aed", "No", "Notion CRM",  "Free template · flexible"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free CRM Software in 2026",
    subtitle = "HubSpot  ·  Zoho CRM  ·  Freshsales  ·  Bitrix24  ·  Notion",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-crm-software.jpg")
img.save(out, "JPEG", quality=92)
print(f"Saved: {out}")
