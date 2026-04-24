#!/usr/bin/env python3
"""
Feature image generator: Best Free Accounting Software in 2026
Output : static/img/free-accounting-software.webp  (1200x630 px)
Silo   : Business   Accent: #10b981
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image, ImageDraw
from image_helpers import (
    W, H, BG, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM,
    LEFT_W, CONTENT_H,
    font, rrect, truncate,
    draw_chrome, draw_featured_card, draw_grid, draw_bar, img_out,
)

ACCENT = "#10b981"   # Business silo — emerald

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock accounting dashboard ───────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Wave — Dashboard · April 2026")

SIDE = 20

# KPI cards row
kpi_y = 46
kpi_w = (LEFT_W - SIDE * 2 - 16) // 3
kpis = [
    ("Income",   "$12,480",  ACCENT),
    ("Expenses", " $4,920",  "#ef4444"),
    ("Net",      " $7,560",  ACCENT),
]
for i, (label, val, color) in enumerate(kpis):
    x = SIDE + i * (kpi_w + 8)
    rrect(draw, x, kpi_y, x + kpi_w, kpi_y + 54, 6, CARD_BG)
    draw.text((x + 10, kpi_y + 6), label, fill=TEXT_DIM, font=font(9, bold=True))
    draw.text((x + 10, kpi_y + 22), val, fill=color, font=font(15, bold=True))

# Section header — P&L
sec_y = kpi_y + 66
draw.text((SIDE, sec_y), "Profit & Loss — this month",
          fill=TEXT_W, font=font(11, bold=True))

# Ledger rows
row_y = sec_y + 20
ledger = [
    ("Apr 03", "Client invoice #1042",   " +$3,200", "Income"),
    ("Apr 07", "Software subscriptions", "   -$184", "Expense"),
    ("Apr 12", "Client invoice #1043",   " +$4,100", "Income"),
    ("Apr 18", "Office supplies",        "    -$76", "Expense"),
    ("Apr 22", "Client invoice #1044",   " +$5,180", "Income"),
    ("Apr 24", "Contractor payment",     "   -$900", "Expense"),
]
col_x = [SIDE + 8, SIDE + 72, SIDE + 258, SIDE + 350]
col_w = [60, 180, 88, 70]
hdr_labels = ["Date", "Description", "Amount", "Type"]
rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 18, 3, ACCENT + "28")
for label, cx, cw in zip(hdr_labels, col_x, col_w):
    draw.text((cx, row_y + 3),
              truncate(draw, label, font(9, bold=True), cw - 4),
              fill=ACCENT, font=font(9, bold=True))
row_y += 22

for date, desc, amt, typ in ledger:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 22, 3, CARD_BG)
    amt_color = "#ef4444" if amt.strip().startswith("-") else ACCENT
    vals   = [date, desc, amt, typ]
    colors = [TEXT_DIM, TEXT_W, amt_color, TEXT_DIM]
    for val, cx, cw, clr in zip(vals, col_x, col_w, colors):
        draw.text((cx, row_y + 5),
                  truncate(draw, val, font(10), cw - 4),
                  fill=clr, font=font(10))
    row_y += 26

# Totals band
rrect(draw, SIDE, row_y + 4, LEFT_W - SIDE, row_y + 28, 4, ACCENT + "30")
draw.text((col_x[0], row_y + 10), "NET PROFIT",
          fill=ACCENT, font=font(10, bold=True))
draw.text((col_x[2], row_y + 10), "+$7,560",
          fill=TEXT_W, font=font(11, bold=True))
draw.text((col_x[3], row_y + 10), "Healthy",
          fill=ACCENT, font=font(10, bold=True))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "WV",
    name        = "Wave",
    tagline     = "Best free accounting for freelancers",
    line1       = "Double-entry books · unlimited invoices",
    line2       = "Reconcile bank transactions · P&L reports",
    badge       = "✓ Core accounting stays free — pay only for payroll",
    license_note= "Free Starter · Pro and payroll are paid add-ons",
)

draw_grid(draw, ACCENT, [
    ("#e8401c", "ZB", "Zoho Books",  "Free tier · best inside Zoho suite"),
    ("#6366f1", "AK", "Akaunting",   "Open-source · self-host or cloud"),
    ("#0ea5e9", "MG", "Manager",     "Free desktop · full offline ledger"),
    ("#f59e0b", "GC", "GnuCash",     "Mature open-source double-entry"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Accounting Software in 2026",
    subtitle = "Wave  ·  Zoho Books  ·  Akaunting  ·  Manager  ·  GnuCash",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-accounting-software.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
