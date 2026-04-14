#!/usr/bin/env python3
"""
Feature image generator: Best Free Time Tracking Software in 2026
Output : static/img/free-time-tracking-software.webp  (1200×630 px)
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

# ── LEFT PANEL — mock time tracker UI ────────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Time Tracker — Clockify")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2   # 440px

# Active timer bar
rrect(draw, SIDE, 44, LEFT_W - SIDE, 82, 6, ACCENT + "22")
draw.text((SIDE + 14, 52),
          truncate(draw, "Client Proposal — Design Project", font(12, bold=True), CTX_W - 110),
          fill=TEXT_W, font=font(12, bold=True))
draw.text((SIDE + 14, 70),
          truncate(draw, "Design", font(10), 80),
          fill=TEXT_DIM, font=font(10))
# Timer display
draw.text((LEFT_W - SIDE - 100, 56),
          "02:14:37", fill=ACCENT, font=font(14, bold=True))
# Stop button
rrect(draw, LEFT_W - SIDE - 30, 54, LEFT_W - SIDE - 8, 76, 4, ACCENT)
draw.rectangle([LEFT_W - SIDE - 24, 59, LEFT_W - SIDE - 14, 71], fill="#000000")

# Column header
hdr_y = 92
draw.rectangle([SIDE, hdr_y, LEFT_W - SIDE, hdr_y + 18], fill=ACCENT + "28")
draw.text((SIDE + 44, hdr_y + 3), "Task / Project",
          fill=ACCENT, font=font(10, bold=True))
draw.text((LEFT_W - SIDE - 74, hdr_y + 3), "Duration",
          fill=ACCENT, font=font(10, bold=True))

# Recent time entries
entries = [
    ("#3b82f6", "CP", "Client Proposal",    "Design Project",   "2h 14m"),
    ("#f59e0b", "EM", "Email & Admin",       "Internal",         "0h 48m"),
    ("#8b5cf6", "LA", "Landing Page Copy",   "Startup Inc",      "3h 05m"),
    ("#ef4444", "RM", "Review & Meeting",    "Corp Group",       "1h 20m"),
    ("#06b6d4", "DR", "Dashboard Redesign",  "TechCo Ltd",       "4h 30m"),
]
row_y = hdr_y + 22
for col, initials, task, project, duration in entries:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 32, 4, CARD_BG)
    draw_circle(draw, SIDE + 16, row_y + 16, 12, col,
                initials[:2], "#ffffff", font(9, bold=True))
    draw.text((SIDE + 34, row_y + 4),
              truncate(draw, task, font(11, bold=True), 160),
              fill=TEXT_W, font=font(11, bold=True))
    draw.text((SIDE + 34, row_y + 18),
              truncate(draw, project, font(9), 160),
              fill=TEXT_DIM, font=font(9))
    draw.text((LEFT_W - SIDE - 70, row_y + 10),
              duration, fill=TEXT_W, font=font(11, bold=True))
    row_y += 38

# Daily total bar
total_y = row_y + 8
rrect(draw, SIDE, total_y, LEFT_W - SIDE, total_y + 32, 6, ACCENT + "33")
draw.text((SIDE + 14, total_y + 8),
          "Today total", fill=TEXT_DIM, font=font(11))
draw.text((LEFT_W - SIDE - 80, total_y + 8),
          "11h 57m", fill=ACCENT, font=font(13, bold=True))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "CL",
    name        = "Clockify",
    tagline     = "Best free time tracker overall",
    line1       = "Unlimited users · unlimited projects",
    line2       = "Timer, timesheets, and team reports",
    badge       = "✓ Free forever — no user limit",
    license_note= "Freemium — billing rates in paid tiers",
)

draw_grid(draw, ACCENT, [
    ("#e05252", "TG", "Toggl Track",   "5 users free · clean interface"),
    ("#4b9cd3", "RT", "RescueTime",    "Auto-tracking · lite plan free"),
    ("#f97316", "TC", "TimeCamp",      "Unlimited users · auto-capture"),
    ("#6b7280", "HV", "Harvest Free",  "1 seat · 2 projects · invoicing"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Time Tracking Software in 2026",
    subtitle = "Clockify  ·  Toggl Track  ·  RescueTime  ·  TimeCamp  ·  Harvest",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-time-tracking-software.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
