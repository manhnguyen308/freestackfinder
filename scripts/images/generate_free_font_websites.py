#!/usr/bin/env python3
"""
Feature image generator: Free font websites in 2026
Output : static/img/free-font-websites.webp  (1200x630 px)
Silo   : Creative   Accent: #f97316

License models and delivery methods come from the comparison table in
content/creative/free-font-websites.md. The article gives no catalog sizes,
so the image shows none.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM, TEXT_MID, GOOD, WARN,
    card_window, card_featured, card_grid, card_bar, mix, logo_path,
)

ACCENT = "#f97316"   # Creative silo, orange
BLUE   = "#60a5fa"

c = Canvas()

# ── LEFT PANEL: type specimen, then license model per site ────────────────────
x0, y0, x1, y1 = card_window(c, "Font sources by license")

c.rect(x0, y0, x1, y0 + 86, CARD_BG, r=10)
c.text(x0 + 20, y0 + 43, "Aa", 54, ACCENT, "bold", anchor="lm")
c.text(x0 + 110, y0 + 18, "PREVIEW", 12, TEXT_DIM, "semibold")
c.fit_text(x0 + 110, y0 + 38, "Check the license before the style",
           19, x1 - x0 - 130, TEXT_W, "semibold")

COL_LIC, COL_DEL = x0 + 160, x0 + 336
hy = y0 + 104
c.text(x0, hy, "SITE", 13, TEXT_DIM, "semibold")
c.text(COL_LIC, hy, "LICENSE", 13, TEXT_DIM, "semibold")
c.text(COL_DEL, hy, "DELIVERY", 13, TEXT_DIM, "semibold")

rows = [
    ("Google Fonts",  ("Open source", GOOD),      "CDN, download"),
    ("Font Squirrel", ("Commercial focus", BLUE), "Download"),
    ("DaFont",        ("Mixed", WARN),            "Download"),
    ("Fontsource",    ("Open source", GOOD),      "npm"),
    ("1001 Fonts",    ("Mixed", WARN),            "Download"),
]

ry, RH = hy + 24, 42
for site, (lic, col), delivery in rows:
    c.rect(x0, ry, x1, ry + RH - 6, CARD_BG, r=8)
    mid = ry + (RH - 6) / 2
    c.fit_text(x0 + 14, mid, site, 16, COL_LIC - x0 - 22, TEXT_W, "semibold", anchor="lm")
    c.pill(COL_LIC - 2, mid - 12, lic, 12.5, col, mix(col, WIN_BG, 0.78), h=24)
    c.fit_text(COL_DEL, mid, delivery, 14, x1 - COL_DEL - 10, TEXT_MID, anchor="lm")
    ry += RH

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "GF",
    logo     = logo_path("google-fonts.png"),
    name     = "Google Fonts",
    tagline  = "Best overall free font library",
    note     = "Open-source licenses across the catalog, with CDN embedding or download",
)

card_grid(c, [
    ("#22c55e", "FS", "Font Squirrel", "Commercial-use focus. Still read each license", logo_path("font-squirrel.png")),
    ("#ec4899", "Da", "DaFont",        "Mixed licenses, many for personal use only", logo_path("dafont.png")),
    ("#3b82f6", "Fo", "Fontsource",    "npm packages for self-hosting open-source fonts", logo_path("fontsource.png")),
    ("#eab308", "1F", "1001 Fonts",    "Per-font license labels on a mixed catalog", logo_path("1001-fonts.png")),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
card_bar(
    c, ACCENT,
    title    = "Free font websites in 2026",
    subtitle = "Google Fonts  ·  Font Squirrel  ·  DaFont  ·  Fontsource  ·  1001 Fonts",
)

c.save("free-font-websites.webp")
