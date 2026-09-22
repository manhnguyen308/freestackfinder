#!/usr/bin/env python3
"""
Feature image generator: Canva Free vs Pro in 2026
Output : static/img/canva-free-vs-paid.webp  (1200x630 px)
Silo   : Creative   Accent: #f97316

Every label is taken from content/creative/canva-free-vs-paid.md. The article
avoids exact quotas because Canva changes them, so the image does too.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM, GOOD, WARN, BAD,
    card_window, card_featured, card_grid, card_bar, mix,
)

ACCENT = "#f97316"   # Creative silo, orange
NEUTRAL = "#8a8fa8"

c = Canvas()

# ── LEFT PANEL: the article's comparison table, reduced to status pills ───────
x0, y0, x1, y1 = card_window(c, "Canva plans compared")

COL_FREE, COL_PRO = 318, 436
c.text(x0, y0, "FEATURE", 13, TEXT_DIM, "semibold")
c.text(COL_FREE, y0, "FREE", 13, TEXT_DIM, "semibold")
c.text(COL_PRO, y0, "PRO", 13, ACCENT, "semibold")

rows = [
    ("Templates",          ("Free set", NEUTRAL), ("Full", GOOD)),
    ("Background remover", ("Limited", WARN),     ("Included", GOOD)),
    ("Magic Resize",       ("No", BAD),           ("Included", GOOD)),
    ("Brand controls",     ("Basic", WARN),       ("Deeper", GOOD)),
    ("Content Planner",    ("No", BAD),           ("Included", GOOD)),
    ("Team workflow",      ("Sharing", NEUTRAL),  ("Roles", GOOD)),
]

ry, RH = y0 + 30, 50
for label, (free_txt, free_col), (pro_txt, pro_col) in rows:
    c.rect(x0, ry, x1, ry + RH - 8, CARD_BG, r=8)
    c.fit_text(x0 + 16, ry + (RH - 8) / 2, label, 17, COL_FREE - x0 - 28,
               TEXT_W, "semibold", anchor="lm")
    for cx, txt, col in [(COL_FREE, free_txt, free_col), (COL_PRO, pro_txt, pro_col)]:
        c.pill(cx - 2, ry + 8, txt, 13, col, mix(col, WIN_BG, 0.78), h=26)
    ry += RH

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "C",
    name     = "Canva Free vs Pro",
    tagline  = "Free covers occasional projects",
    note     = "Pro pays off when background removal, brand settings, "
               "or resizing repeat every week",
)

card_grid(c, [
    ("#3b82f6", "F",  "Stay on Free",  "Casual creators, students, and occasional projects"),
    ("#22c55e", "P",  "Consider Pro",  "Solo professionals, small businesses, and marketers"),
    ("#8b5cf6", "MR", "Magic Resize",  "Not on Free. One design resized for each format"),
    ("#ec4899", "T",  "Team work",     "Pro adds roles, comments, and shared brand assets"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
card_bar(
    c, ACCENT,
    title    = "Canva Free vs Pro in 2026",
    subtitle = "Templates  ·  Background remover  ·  Magic Resize  ·  Brand kits  ·  Team roles",
)

c.save("canva-free-vs-paid.webp")
