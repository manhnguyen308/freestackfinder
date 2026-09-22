#!/usr/bin/env python3
"""
Feature image generator: Free Photoshop alternatives in 2026
Output : static/img/photoshop-alternatives.webp  (1200x630 px)
Silo   : Creative   Accent: #f97316

Replaces a 1200x800 stock photo of Adobe app icons. Tool facts come from
content/creative/photoshop-alternatives.md. The editor mock-up is generic.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM, TEXT_MID, LINE,
    card_window, card_featured, card_grid, card_bar, mix,
)

ACCENT = "#f97316"   # Creative silo, orange

c = Canvas()

# ── LEFT PANEL: layer-based editor with a canvas and a layers list ────────────
x0, y0, x1, y1 = card_window(c, "Photopea: poster.psd")

# Tool column
for k in range(6):
    ty = y0 + k * 38
    active = k == 1
    c.rect(x0, ty, x0 + 30, ty + 30, mix(ACCENT, WIN_BG, 0.75) if active else CARD_BG, r=6)
    col = ACCENT if active else TEXT_DIM
    if k == 0:
        c.poly([(x0 + 10, ty + 8), (x0 + 10, ty + 22), (x0 + 14, ty + 18), (x0 + 20, ty + 23)], col)
    elif k == 1:
        c.rect(x0 + 8, ty + 8, x0 + 22, ty + 22, None, r=2, outline=col, width=2)
    elif k == 2:
        c.circle(x0 + 15, ty + 15, 7, None, outline=col, width=2)
    elif k == 3:
        c.line([(x0 + 9, ty + 21), (x0 + 21, ty + 9)], col, 3)
    elif k == 4:
        c.text(x0 + 15, ty + 15, "T", 16, col, "bold", anchor="mm")
    else:
        c.circle(x0 + 15, ty + 15, 3, col)
        c.circle(x0 + 15, ty + 15, 8, None, outline=col, width=2)

# Canvas with a simple poster scene
cx0, cy0, cx1, cy1 = x0 + 44, y0, x1, y0 + 176
c.rect(cx0, cy0, cx1, cy1, "#1e1b4b", r=8)
c.rect(cx0, cy0 + 84, cx1, cy1, "#312e81", r=8)
c.circle(cx1 - 90, cy0 + 64, 32, "#fb923c")
c.poly([(cx0, cy1 - 8), (cx0 + 120, cy0 + 86), (cx0 + 230, cy1 - 8)], "#4338ca")
c.poly([(cx0 + 150, cy1 - 8), (cx0 + 270, cy0 + 104), (cx1, cy1 - 8)], "#6366f1")
c.rect(cx0, cy1 - 10, cx1, cy1, "#312e81", r=4)
# Headline text layer, selected
c.rect(cx0 + 22, cy0 + 22, cx0 + 180, cy0 + 36, "#f8fafc", r=4)
c.rect(cx0 + 22, cy0 + 44, cx0 + 130, cy0 + 54, "#c7d2fe", r=4)
c.rect(cx0 + 16, cy0 + 16, cx0 + 186, cy0 + 60, None, outline="#60a5fa", width=2)

# Layers panel
ly = cy1 + 12
c.text(cx0, ly, "LAYERS", 12, TEXT_DIM, "semibold")
layers = [
    ("Headline text", "#f8fafc", True),
    ("Subject mask",  "#fb923c", False),
    ("Background",    "#4338ca", False),
]
ly += 22
for name, swatch, selected in layers:
    bg = mix(ACCENT, WIN_BG, 0.82) if selected else CARD_BG
    c.rect(cx0, ly, cx1, ly + 32, bg, r=6)
    c.circle(cx0 + 18, ly + 16, 4, TEXT_MID)
    c.rect(cx0 + 34, ly + 6, cx0 + 54, ly + 26, swatch, r=3)
    c.fit_text(cx0 + 66, ly + 16, name, 15, cx1 - cx0 - 80,
               TEXT_W if selected else TEXT_MID, "semibold" if selected else "regular", anchor="lm")
    ly += 38

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "Pp",
    name     = "Photopea",
    tagline  = "Best for PSD editing in a browser",
    note     = "Layers, masks, and PSD import and export. The free version shows ads",
)

card_grid(c, [
    ("#3b82f6", "G",  "GIMP",           "Desktop editor with plugins and local files"),
    ("#8b5cf6", "Kr", "Krita",          "Painting and illustration, PSD import and export"),
    ("#22c55e", "Px", "Pixlr",          "Quick browser edits with a lighter learning curve"),
    ("#64748b", "Ad", "Keep Photoshop", "For Adobe file handoffs and high-end print work"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
card_bar(
    c, ACCENT,
    title    = "Free Photoshop alternatives in 2026",
    subtitle = "Photopea  ·  GIMP  ·  Krita  ·  Pixlr",
)

c.save("photoshop-alternatives.webp")
