#!/usr/bin/env python3
"""
Feature image generator: Best Free Team Email Tools in 2026
Output : static/img/free-team-email.webp  (1200×630 px)
Silo   : Cloud   Accent: #06b6d4
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

ACCENT = "#06b6d4"   # Cloud silo — cyan

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock team inbox / admin panel ────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Team Inbox — Zoho Mail")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

# Folder sidebar
sidebar_w = 90
draw.rectangle([0, 38, sidebar_w, CONTENT_H], fill="#0d0f18")
sidebar_items = ["Inbox", "Sent", "Drafts", "Spam", "Shared"]
for i, label in enumerate(sidebar_items):
    sy = 52 + i * 22
    if i == 0:
        rrect(draw, 4, sy - 2, sidebar_w - 4, sy + 16, 4, ACCENT + "30")
        draw.text((10, sy), label, fill=ACCENT, font=font(9, bold=True))
    else:
        draw.text((10, sy), label, fill=TEXT_DIM, font=font(9))

# Email list rows
mx = sidebar_w + 10
row_entries = [
    ("alex@team.com", "Q2 budget review — attached", "10:42 AM"),
    ("sara@team.com", "Welcome to the team — onboarding", "9:15 AM"),
    ("noreply@zoom.us", "Meeting recording ready", "Yesterday"),
]
ey = 48
for sender, subject, time in row_entries:
    row_y = ey
    rrect(draw, mx, row_y, LEFT_W - SIDE, row_y + 32, 5, CARD_BG)
    draw.text((mx + 8, row_y + 5), truncate(draw, sender, font(9, bold=True), 90),
              fill=TEXT_W, font=font(9, bold=True))
    draw.text((mx + 8, row_y + 18), truncate(draw, subject, font(8), CTX_W - sidebar_w - 20),
              fill=TEXT_DIM, font=font(8))
    draw.text((LEFT_W - SIDE - 50, row_y + 5), time, fill=TEXT_DIM, font=font(8))
    ey += 38

# User avatars row (team members)
avatar_y = ey + 8
draw.text((mx, avatar_y), "Team members:", fill=TEXT_DIM, font=font(8))
avatar_colors = [ACCENT, "#6366f1", "#10b981", "#f97316", "#8b5cf6"]
avatar_initials = ["AJ", "SR", "MK", "PL", "ZO"]
for i, (col, ini) in enumerate(zip(avatar_colors, avatar_initials)):
    ax = mx + 90 + i * 26
    draw_circle(draw, ax + 10, avatar_y + 8, 10, col, ini)

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "ZM",
    name        = "Zoho Mail",
    tagline     = "Best free team email — custom domain",
    line1       = "5 users · 5GB each · custom domain",
    line2       = "Webmail + mobile · no credit card",
    badge       = "Free · up to 5 users",
    license_note= "Freemium — paid plans from $1/user/month",
)

draw_grid(draw, ACCENT, [
    ("#ef4444",  "SP", "Spike",       "Email-as-chat · 5 users free"),
    ("#8b5cf6",  "PM", "Proton Mail", "Encrypted · individual free"),
    ("#10b981",  "TN", "Tutanota",    "Open-source · privacy focus"),
    ("#6366f1",  "GL", "Gmail Delg.", "Delegate access · workaround"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Team Email Tools in 2026",
    subtitle = "Zoho Mail  ·  Spike  ·  Proton Mail  ·  Tutanota  ·  Gmail Delegates",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-team-email.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
