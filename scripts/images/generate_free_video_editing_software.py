#!/usr/bin/env python3
"""
Feature image generator: Free video editing software in 2026
Output : static/img/free-video-editing-software.webp  (1200x630 px)
Silo   : Video   Accent: #ef4444

Replaces a 1200x800 stock photo. Tool facts come from
content/video/free-video-editing-software.md. The timeline is a generic mock-up.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_DIM, LINE,
    card_window, card_featured, card_grid, card_bar, mix, logo_path,
)

ACCENT = "#ef4444"   # Video silo, red

c = Canvas()

# ── LEFT PANEL: viewer above a three-track timeline ───────────────────────────
x0, y0, x1, y1 = card_window(c, "Timeline: project edit")

# Viewer with a simple scene and transport controls
vx0, vy0, vx1, vy1 = x0 + 60, y0 - 4, x1 - 60, y0 + 172
c.rect(vx0, vy0, vx1, vy1, "#0b1220", r=8)
c.rect(vx0 + 6, vy0 + 6, vx1 - 6, vy1 - 34, "#1e3a5f", r=6)
c.circle(vx1 - 70, vy0 + 44, 18, "#fbbf24")
c.poly([(vx0 + 6, vy1 - 34), (vx0 + 110, vy0 + 70), (vx0 + 210, vy1 - 34)], "#2563eb")
c.poly([(vx0 + 150, vy1 - 34), (vx0 + 250, vy0 + 84), (vx1 - 6, vy1 - 34)], "#3b82f6")
mid = (vx0 + vx1) / 2
c.poly([(mid - 6, vy1 - 25), (mid - 6, vy1 - 9), (mid + 8, vy1 - 17)], "#e5e7eb")
c.rect(mid - 36, vy1 - 23, mid - 26, vy1 - 11, "#8a8fa8", r=2)
c.rect(mid + 26, vy1 - 23, mid + 36, vy1 - 11, "#8a8fa8", r=2)

# Tracks
ty = vy1 + 20
c.line([(x0, ty - 8), (x1, ty - 8)], LINE)
tracks = [
    ("V2", [(0.30, 0.52, "#8b5cf6"), (0.70, 0.86, "#8b5cf6")]),
    ("V1", [(0.00, 0.28, "#3b82f6"), (0.29, 0.63, "#06b6d4"), (0.64, 1.00, "#3b82f6")]),
    ("A1", [(0.00, 0.63, "#22c55e"), (0.64, 1.00, "#16a34a")]),
]
lane_x0, lane_x1 = x0 + 44, x1
for label, clips in tracks:
    c.rect(x0, ty, x0 + 36, ty + 40, CARD_BG, r=6)
    c.text(x0 + 18, ty + 20, label, 13, TEXT_DIM, "semibold", anchor="mm")
    c.rect(lane_x0, ty, lane_x1, ty + 40, mix(CARD_BG, WIN_BG, 0.4), r=6)
    for a, b, col in clips:
        cx0 = lane_x0 + 3 + a * (lane_x1 - lane_x0 - 6)
        cx1 = lane_x0 + 3 + b * (lane_x1 - lane_x0 - 6) - 3
        c.rect(cx0, ty + 4, cx1, ty + 36, mix(col, WIN_BG, 0.35), r=5)
        if label == "A1":
            for k in range(int(cx0) + 6, int(cx1) - 4, 6):
                h = 5 + (k * 7) % 11
                c.line([(k, ty + 20 - h), (k, ty + 20 + h)], mix(col, "#ffffff", 0.2), 2)
        else:
            c.rect(cx0, ty + 4, cx0 + 4, ty + 36, col, r=2)
    ty += 48

# Playhead
px = lane_x0 + 0.45 * (lane_x1 - lane_x0)
c.line([(px, vy1 + 8), (px, ty - 6)], ACCENT, 2)
c.poly([(px - 7, vy1 + 6), (px + 7, vy1 + 6), (px, vy1 + 14)], ACCENT)

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "DR",
    logo     = logo_path("davinci-resolve.png"),
    name     = "DaVinci Resolve",
    tagline  = "Best for depth and professional growth",
    note     = "No watermark. The free version covers 8-bit formats up to 60fps at Ultra HD",
)

card_grid(c, [
    ("#22c55e", "Cc", "CapCut Desktop", "Short social clips, watermark risk with stock assets", logo_path("capcut.png")),
    ("#3b82f6", "OS", "OpenShot",       "Drag and drop editing for a first project", logo_path("openshot.png")),
    ("#8b5cf6", "Kd", "Kdenlive",       "Open-source multi-track with proxy editing", logo_path("kdenlive.png")),
    ("#eab308", "Sc", "Shotcut",        "When file imports are the main problem", logo_path("shotcut.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free video editing software in 2026",
    subtitle = "DaVinci Resolve  ·  CapCut  ·  OpenShot  ·  Kdenlive  ·  Shotcut",
)

c.save("free-video-editing-software.webp")
