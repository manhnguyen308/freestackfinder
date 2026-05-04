#!/usr/bin/env python3
"""
Feature image generator: Best Free Video Conferencing Tools in 2026
Output : static/img/free-video-conferencing.webp  (1200×630 px)
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

# ── LEFT PANEL — mock meeting dashboard ──────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Video Meeting — Active Session")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

draw.text((SIDE, 44), "Participants & status", fill=TEXT_DIM, font=font(11, bold=True))

participants = [
    (ACCENT,    "Google Meet",   "100 participants",  "No limit 1:1"),
    ("#22c55e", "Jitsi Meet",    "Unlimited",         "No account needed"),
    ("#3b82f6", "Microsoft Teams","100 participants",  "60 min limit"),
    ("#f97316", "Whereby",       "100 participants",  "Permanent room"),
    ("#8b5cf6", "Zoho Meeting",  "100 participants",  "Webinar support"),
]

row_y = 64
for col, label, value, status in participants:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 36, 5, CARD_BG)
    draw.rectangle([SIDE, row_y, SIDE + 4, row_y + 36], fill=col)
    draw.text((SIDE + 12, row_y + 4),  label,  fill=TEXT_DIM, font=font(10))
    draw.text((SIDE + 12, row_y + 18), value,  fill=TEXT_W,   font=font(12, bold=True))
    draw.text((LEFT_W - SIDE - 100, row_y + 12),
              truncate(draw, status, font(9), 96),
              fill=col, font=font(9, bold=True))
    row_y += 43

stats = [("Tools compared", "6"), ("Time limits", "None–60 min"), ("Free forever", "All")]
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
    initials    = "GM",
    name        = "Google Meet",
    tagline     = "Best free video conferencing for most users",
    line1       = "100 participants · browser-based · no download needed",
    line2       = "Unlimited 1:1 calls · Calendar integration · screen share",
    badge       = "Free with a Google account",
    license_note= "Free tier — no credit card required",
)

draw_grid(draw, ACCENT, [
    ("#22c55e", "JM", "Jitsi Meet",   "No account · unlimited duration · open-source"),
    ("#3b82f6", "MT", "Teams Free",   "Microsoft 365 integration · persistent channels"),
    ("#f97316", "WB", "Whereby",      "Permanent room URL · 100 participants · no download"),
    ("#8b5cf6", "ZM", "Zoho Meeting", "Webinar support · scheduling · attendance reports"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Video Conferencing Tools in 2026",
    subtitle = "Google Meet  ·  Jitsi Meet  ·  Teams  ·  Whereby  ·  Zoho Meeting",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-video-conferencing.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
