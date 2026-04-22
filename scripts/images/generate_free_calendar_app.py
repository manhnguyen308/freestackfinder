#!/usr/bin/env python3
"""
Feature image generator: Best Free Calendar Apps in 2026
Output : static/img/free-calendar-app.webp  (1200×630 px)
Silo   : Productivity   Accent: #6366f1
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image, ImageDraw
from image_helpers import (
    W, H, BG, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM,
    LEFT_W, CONTENT_H, INNER_PAD,
    font, rrect, draw_circle, truncate, measure_w,
    draw_chrome, draw_featured_card, draw_grid, draw_bar, img_out,
)

ACCENT = "#6366f1"   # Productivity silo — indigo

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock calendar interface ─────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Google Calendar — April 2026")

# Mini month grid header
grid_top = 48
day_labels = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
cell_w = (LEFT_W - 20) // 7
for i, label in enumerate(day_labels):
    x = 10 + i * cell_w + cell_w // 2
    draw.text((x - 6, grid_top), label, fill=TEXT_DIM, font=font(8))

# Calendar date grid — 5 weeks
days = list(range(1, 31))
row, col = 0, 0
day_y_start = grid_top + 18
for day in range(1, 31):
    cx = 10 + col * cell_w + cell_w // 2
    cy = day_y_start + row * 20
    is_today = (day == 22)
    is_event = day in (7, 14, 15, 21, 22, 28)
    if is_today:
        rrect(draw, cx - 9, cy - 2, cx + 9, cy + 14, 8, ACCENT)
        draw.text((cx - 5 if day < 10 else cx - 8, cy + 1),
                  str(day), fill=TEXT_W, font=font(9, bold=True))
    elif is_event:
        draw.text((cx - 5 if day < 10 else cx - 8, cy + 1),
                  str(day), fill=ACCENT, font=font(9, bold=True))
        draw.rectangle([cx - 3, cy + 14, cx + 3, cy + 15], fill=ACCENT)
    else:
        draw.text((cx - 5 if day < 10 else cx - 8, cy + 1),
                  str(day), fill=TEXT_DIM, font=font(9))
    col += 1
    if col == 7:
        col = 0
        row += 1

# Upcoming events panel
events_y = day_y_start + row * 20 + 12
draw.rectangle([10, events_y, LEFT_W - 10, events_y + 1], fill=ACCENT + "44")

event_items = [
    ("Today", "Team standup · 9:00 AM", ACCENT),
    ("Today", "Client review · 2:00 PM", "#10b981"),
    ("Wed 24", "Product demo · 11:00 AM", "#f97316"),
    ("Fri 26", "Weekly review · 4:00 PM", "#3b82f6"),
]
ev_y = events_y + 8
for date_label, title, color in event_items:
    draw.text((14, ev_y), date_label, fill=TEXT_DIM, font=font(8))
    rrect(draw, 52, ev_y, 54, ev_y + 12, 1, color)
    draw.text((58, ev_y),
              truncate(draw, title, font(9), LEFT_W - 72),
              fill=TEXT_W, font=font(9))
    ev_y += 18
    if ev_y > CONTENT_H - 20:
        break

# Bottom label
draw.text((14, CONTENT_H - 20), "Free plan  ·  Unlimited events  ·  Gmail sync",
          fill=TEXT_DIM, font=font(9))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials     = "GC",
    name         = "Google Calendar",
    tagline      = "Best free calendar for most people",
    line1        = "Unlimited events · Gmail auto-detection",
    line2        = "Cross-platform · Google Meet integration",
    badge        = "✓ Free forever with Google account",
    license_note = "Web · iOS · Android · calendar.google.com",
)

draw_grid(draw, ACCENT, [
    ("#8b5cf6", "NC", "Notion Calendar", "Links events to Notion docs"),
    ("#a8a8b3", "AC", "Apple Calendar",  "iCloud sync · Apple ecosystem"),
    ("#ef4444", "PC", "Proton Calendar", "End-to-end encrypted events"),
    ("#10b981", "ZC", "Zoho Calendar",   "Team scheduling · Zoho suite"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Calendar Apps in 2026",
    subtitle = "Google Calendar  ·  Notion  ·  Apple  ·  Proton  ·  Zoho",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-calendar-app.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
