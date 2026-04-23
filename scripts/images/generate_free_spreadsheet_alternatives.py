#!/usr/bin/env python3
"""
Feature image generator: Best Free Spreadsheet Alternatives in 2026
Output : static/img/free-spreadsheet-alternatives.webp  (1200×630 px)
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

# ── LEFT PANEL — mock spreadsheet UI ─────────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Google Sheets — Q2 Budget Tracker")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

# Formula bar
rrect(draw, SIDE, 44, LEFT_W - SIDE, 66, 4, CARD_BG)
draw.text((SIDE + 10, 51), "fx", fill=ACCENT, font=font(11, bold=True))
draw.text((SIDE + 32, 51), "=SUM(D2:D7)", fill=TEXT_DIM, font=font(10))

# Column headers
COL_LABELS = ["A", "B — Category", "C — Budget", "D — Actual", "E — Delta"]
COL_X      = [SIDE, SIDE + 28, SIDE + 148, SIDE + 248, SIDE + 348]
COL_W      = [26, 118, 98, 98, 68]
hdr_y = 72
draw.rectangle([SIDE, hdr_y, LEFT_W - SIDE, hdr_y + 18], fill=ACCENT + "30")
for i, (label, cx, cw) in enumerate(zip(COL_LABELS, COL_X, COL_W)):
    draw.text((cx + 4, hdr_y + 3),
              truncate(draw, label, font(9, bold=True), cw - 6),
              fill=ACCENT, font=font(9, bold=True))

# Spreadsheet rows
rows = [
    ("1", "Salaries",     "$24,000", "$23,450", "+$550"),
    ("2", "Software",     " $3,600", " $3,820", "-$220"),
    ("3", "Marketing",    " $6,000", " $5,100", "+$900"),
    ("4", "Office",       " $1,200", " $1,190", "+$10"),
    ("5", "Contractors",  " $8,000", " $8,750", "-$750"),
    ("6", "Misc",         "   $800", "   $620", "+$180"),
]
highlight_row = 2   # zero-indexed — "Software" row highlighted
row_y = hdr_y + 22
for idx, (num, cat, budget, actual, delta) in enumerate(rows):
    bg = ACCENT + "18" if idx == highlight_row else CARD_BG
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 22, 3, bg)
    vals = [num, cat, budget, actual, delta]
    for val, cx, cw in zip(vals, COL_X, COL_W):
        color = ("#ef4444" if val.startswith("-") else
                 ACCENT    if val.startswith("+") else TEXT_W)
        draw.text((cx + 4, row_y + 5),
                  truncate(draw, val, font(10), cw - 6),
                  fill=color, font=font(10))
    row_y += 26

# Totals row
rrect(draw, SIDE, row_y + 2, LEFT_W - SIDE, row_y + 24, 3, ACCENT + "28")
draw.text((COL_X[1] + 4, row_y + 7), "TOTAL", fill=ACCENT, font=font(10, bold=True))
draw.text((COL_X[2] + 4, row_y + 7), "$43,600", fill=TEXT_W, font=font(10, bold=True))
draw.text((COL_X[3] + 4, row_y + 7), "$42,930", fill=TEXT_W, font=font(10, bold=True))
draw.text((COL_X[4] + 4, row_y + 7), "+$670", fill=ACCENT, font=font(10, bold=True))

# Mini chart — horizontal bars
chart_y = row_y + 34
draw.text((SIDE, chart_y), "Spending vs Budget", fill=TEXT_DIM, font=font(10, bold=True))
chart_y += 16
bar_data = [
    ("Salaries",    0.98),
    ("Software",    1.06),
    ("Marketing",   0.85),
]
for label, ratio in bar_data:
    draw.text((SIDE, chart_y + 2), label, fill=TEXT_DIM, font=font(9))
    bar_x = SIDE + 88
    bar_w = int(120 * min(ratio, 1.0))
    rrect(draw, bar_x, chart_y + 1, bar_x + 120, chart_y + 13, 3, CARD_BG)
    bar_color = "#ef4444" if ratio > 1.0 else ACCENT
    rrect(draw, bar_x, chart_y + 1, bar_x + bar_w, chart_y + 13, 3, bar_color)
    pct = f"{int(ratio * 100)}%"
    draw.text((bar_x + 124, chart_y + 2), pct,
              fill=bar_color, font=font(9, bold=True))
    chart_y += 18

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "GS",
    name        = "Google Sheets",
    tagline     = "Best free spreadsheet for most users",
    line1       = "Formulas, pivot tables, real-time collaboration",
    line2       = "Works in any browser — no install needed",
    badge       = "✓ Completely free — no limits for personal use",
    license_note= "Free for personal · Workspace plans for teams",
)

draw_grid(draw, ACCENT, [
    ("#1473e6", "LC", "LibreOffice Calc", "Full offline · no limits · open-source"),
    ("#e8401c", "ZS", "Zoho Sheet",       "Cloud · best in Zoho ecosystem"),
    ("#4b9cd3", "OO", "ONLYOFFICE",       "Best Excel format fidelity"),
    ("#f59e0b", "AT", "Airtable",         "Spreadsheet + database hybrid"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Spreadsheet Alternatives in 2026",
    subtitle = "Google Sheets  ·  LibreOffice Calc  ·  Zoho Sheet  ·  ONLYOFFICE  ·  Airtable",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-spreadsheet-alternatives.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
