#!/usr/bin/env python3
"""
Feature image generator: Free FreeCAD alternatives in 2026
Output : static/img/freecad-alternatives.webp  (1200x630 px)
Silo   : Creative   Accent: #f97316

Privacy and offline values come from the comparison table in
content/creative/freecad-alternatives.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM, GOOD, WARN, BAD,
    card_window, card_featured, card_grid, card_bar, mix, logo_path,
)

ACCENT = "#f97316"   # Creative silo, orange

c = Canvas()

# ── LEFT PANEL: private projects and offline use per tool ─────────────────────
x0, y0, x1, y1 = card_window(c, "Private files and offline use")

COL_PRIV, COL_OFF = 318, 436
c.text(x0, y0, "TOOL", 13, TEXT_DIM, "semibold")
c.text(COL_PRIV, y0, "PRIVATE", 13, TEXT_DIM, "semibold")
c.text(COL_OFF, y0, "OFFLINE", 13, TEXT_DIM, "semibold")

rows = [
    ("Onshape Free", ("Public", BAD), ("No", BAD)),
    ("Fusion 360",   ("Yes", GOOD),   ("Partly", WARN)),
    ("Tinkercad",    ("Yes", GOOD),   ("No", BAD)),
    ("SolveSpace",   ("Yes", GOOD),   ("Yes", GOOD)),
    ("OpenSCAD",     ("Yes", GOOD),   ("Yes", GOOD)),
    ("LibreCAD",     ("Yes", GOOD),   ("Yes", GOOD)),
]

ry, RH = y0 + 30, 50
for label, (p_txt, p_col), (o_txt, o_col) in rows:
    c.rect(x0, ry, x1, ry + RH - 8, CARD_BG, r=8)
    c.fit_text(x0 + 16, ry + (RH - 8) / 2, label, 17, COL_PRIV - x0 - 28,
               TEXT_W, "semibold", anchor="lm")
    for cx, txt, col in [(COL_PRIV, p_txt, p_col), (COL_OFF, o_txt, o_col)]:
        c.pill(cx - 2, ry + 8, txt, 13, col, mix(col, WIN_BG, 0.78), h=26)
    ry += RH

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "On",
    logo     = logo_path("onshape.png"),
    name     = "Onshape Free",
    tagline  = "Best free parametric CAD overall",
    note     = "Runs in a browser. Every document on the free plan is public",
)

card_grid(c, [
    ("#3b82f6", "F",  "Fusion 360",  "Private projects and CAM, ten editable documents", logo_path("fusion.png")),
    ("#22c55e", "Tk", "Tinkercad",   "Primitive shapes for quick 3D prints", logo_path("tinkercad.png")),
    ("#8b5cf6", "SS", "SolveSpace",  "Lightweight parametric CAD, GPL, works offline", logo_path("solvespace.png")),
    ("#06b6d4", "OS", "OpenSCAD",    "Models written as code, GPL licensed", logo_path("openscad.png")),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
card_bar(
    c, ACCENT,
    title    = "Free FreeCAD alternatives in 2026",
    subtitle = "Onshape  ·  Fusion 360  ·  Tinkercad  ·  SolveSpace  ·  OpenSCAD  ·  LibreCAD",
)

c.save("freecad-alternatives.webp")
