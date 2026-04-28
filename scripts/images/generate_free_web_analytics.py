#!/usr/bin/env python3
"""
Feature image generator: Best Free Web Analytics Tools in 2026
Output : static/img/free-web-analytics.webp  (1200×630 px)
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

# ── LEFT PANEL — mock analytics dashboard ────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Web Analytics — Traffic Overview")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

# Section label
draw.text((SIDE, 44), "Traffic sources", fill=TEXT_DIM, font=font(11, bold=True))

# Simulate analytics source rows with bar + metric
sources = [
    (ACCENT,    "Organic Search",  "62%", 310),
    ("#3b82f6", "Direct",          "18%",  90),
    ("#6366f1", "Referral",        "12%",  60),
    ("#f59e0b", "Social",           "5%",  25),
    ("#8b5cf6", "Email",            "3%",  15),
]

bar_y = 64
BAR_MAX = 230
for col, label, pct, width in sources:
    # Row background
    rrect(draw, SIDE, bar_y, LEFT_W - SIDE, bar_y + 36, 5, CARD_BG)
    # Colour strip
    draw.rectangle([SIDE, bar_y, SIDE + 4, bar_y + 36], fill=col)
    # Label
    draw.text((SIDE + 12, bar_y + 4), label, fill=TEXT_W, font=font(10, bold=True))
    # Progress bar track
    track_x = SIDE + 12
    track_y = bar_y + 22
    track_w = BAR_MAX
    draw.rectangle([track_x, track_y, track_x + track_w, track_y + 8], fill="#1e2130")
    draw.rectangle([track_x, track_y, track_x + width, track_y + 8], fill=col)
    # Percentage
    draw.text((track_x + track_w + 8, track_y - 2), pct, fill=col, font=font(10, bold=True))
    bar_y += 43

# Stats bar at bottom of left panel
stats = [("Pageviews", "18.4k"), ("Sessions", "11.2k"), ("Avg. Time", "2m 14s")]
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
    initials    = "G4",
    name        = "Google Analytics 4",
    tagline     = "Most capable free analytics platform",
    line1       = "Unlimited pageviews · acquisition & conversion reports",
    line2       = "Search Console integration · Looker Studio export",
    badge       = "Free · Cookie consent required",
    license_note= "Free — BigQuery export needs additional setup",
)

draw_grid(draw, ACCENT, [
    ("#00a4ef", "Cl", "Microsoft Clarity",  "Free heatmaps · session recordings"),
    ("#34a853", "SC", "Search Console",      "Search queries · impressions · CTR"),
    ("#1a1a2e", "Um", "Umami",               "Privacy-friendly · self-hosted"),
    ("#f97316", "Ma", "Matomo On-Premise",   "Full-depth · open source · self-hosted"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Web Analytics Tools in 2026",
    subtitle = "GA4  ·  Search Console  ·  Microsoft Clarity  ·  Umami  ·  Matomo",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-web-analytics.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
