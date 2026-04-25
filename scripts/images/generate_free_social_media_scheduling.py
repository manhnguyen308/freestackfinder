#!/usr/bin/env python3
"""
Feature image generator: Best Free Social Media Scheduling Tools in 2026
Output : static/img/free-social-media-scheduling.webp  (1200×630 px)
Silo   : Business   Accent: #10b981
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

ACCENT = "#10b981"   # Business silo — emerald

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock social media scheduler UI ───────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Buffer — Content Calendar")

# Toolbar strip
TOOL_Y = 38
draw.rectangle([0, TOOL_Y, LEFT_W, TOOL_Y + 28], fill="#0f1118")
tool_labels = ["Queue", "Calendar", "Analytics", "Channels"]
tx = 12
for t in tool_labels:
    tw = measure_w(draw, t, font(10))
    draw.text((tx, TOOL_Y + 8), t, fill=TEXT_DIM, font=font(10))
    tx += tw + 18

# Highlight "Queue" as active
first_tw = measure_w(draw, "Queue", font(10))
rrect(draw, 8, TOOL_Y + 5, 8 + first_tw + 8, TOOL_Y + 23, 4, ACCENT + "44")
draw.text((12, TOOL_Y + 8), "Queue", fill=ACCENT, font=font(10, bold=True))

# Channel header row
CH_Y = 72
draw.text((14, CH_Y), "Connected channels", fill=TEXT_DIM, font=font(9, bold=True))

channels = [
    ("#3b82f6", "in", "LinkedIn"),
    ("#1da1f2", "X",  "X / Twitter"),
    ("#e1306c", "IG", "Instagram"),
    ("#10b981", "FB", "Facebook"),
]
cx = 14
for col, ini, name in channels:
    cw = measure_w(draw, name, font(9)) + 30
    rrect(draw, cx, CH_Y + 14, cx + cw, CH_Y + 32, 4, col + "33")
    draw_circle(draw, cx + 10, CH_Y + 23, 7, col, ini[:1], "#ffffff", font(7, bold=True))
    draw.text((cx + 20, CH_Y + 16), name, fill=col, font=font(9))
    cx += cw + 6

# Scheduled posts queue
QUEUE_Y = CH_Y + 42
draw.text((14, QUEUE_Y), "Scheduled — next 7 days", fill=TEXT_DIM, font=font(9, bold=True))
QUEUE_Y += 16

posts = [
    ("#3b82f6", "in", "LinkedIn", "Mon 9:00 AM", "5 tips for better remote standups"),
    ("#1da1f2", "X",  "X",        "Mon 11:00 AM","New guide: free scheduling tools →"),
    ("#e1306c", "IG", "Instagram","Tue 8:00 AM", "Behind the scenes this week"),
    ("#10b981", "FB", "Facebook", "Tue 2:00 PM", "How we cut posting time by half"),
    ("#3b82f6", "in", "LinkedIn", "Wed 9:00 AM", "Free tools we use every day"),
]
for col, ini, plat, time, caption in posts:
    rrect(draw, 10, QUEUE_Y, LEFT_W - 10, QUEUE_Y + 40, 6, CARD_BG)
    draw_circle(draw, 28, QUEUE_Y + 20, 12, col, ini[:2], "#ffffff", font(8, bold=True))
    draw.text((46, QUEUE_Y + 5),
              truncate(draw, caption, font(10, bold=True), LEFT_W - 120),
              fill=TEXT_W, font=font(10, bold=True))
    draw.text((46, QUEUE_Y + 22),
              truncate(draw, f"{plat}  ·  {time}", font(9), LEFT_W - 120),
              fill=TEXT_DIM, font=font(9))
    # Status badge
    STATUS_X = LEFT_W - 80
    rrect(draw, STATUS_X, QUEUE_Y + 12, STATUS_X + 64, QUEUE_Y + 28, 4, ACCENT + "33")
    draw.text((STATUS_X + 6, QUEUE_Y + 14), "Scheduled", fill=ACCENT, font=font(8))
    QUEUE_Y += 46

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "Bu",
    name        = "Buffer",
    tagline     = "Best free social media scheduler",
    line1       = "3 channels · queue scheduling · analytics",
    line2       = "Facebook · Instagram · LinkedIn · X · TikTok",
    badge       = "✓ Free plan — no credit card required",
    license_note= "Browser + mobile app · 3-channel limit on free",
)

draw_grid(draw, ACCENT, [
    ("#6366f1", "Mc", "Metricool",       "Analytics + scheduling · 1 brand free"),
    ("#f97316", "La", "Later",           "Visual calendar · Instagram/TikTok"),
    ("#3b82f6", "Mb", "Meta Biz Suite",  "Facebook + Instagram · unlimited free"),
    ("#06b6d4", "Zo", "Zoho Social",     "Zoho-ecosystem users · limited free"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Social Media Scheduling Tools in 2026",
    subtitle = "Buffer  ·  Metricool  ·  Later  ·  Meta Business Suite  ·  No Hootsuite needed",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-social-media-scheduling.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
