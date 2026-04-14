#!/usr/bin/env python3
"""
Feature image generator: Best Free Invoicing Software in 2026
Output : static/img/free-invoicing-software.webp  (1200×630 px)
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

# ── LEFT PANEL — mock invoice UI ──────────────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Invoice #1042  —  Wave")

SIDE  = 20   # horizontal margin inside left panel
CTX_W = LEFT_W - SIDE * 2   # usable width = 440px

# Invoice header block
rrect(draw, SIDE, 48, LEFT_W - SIDE, 148, 6, CARD_BG)
draw.text((SIDE + 16, 60), "INVOICE", fill=ACCENT, font=font(14, bold=True))
draw.text((SIDE + 16, 80), "#1042",   fill=TEXT_W,  font=font(20, bold=True))
draw.text((SIDE + 16, 112), "Date: Apr 13, 2026", fill=TEXT_DIM, font=font(11))
draw.text((SIDE + 16, 128), "Due:  Apr 27, 2026", fill=TEXT_DIM, font=font(11))

# Column header
hdr_y = 160
draw.rectangle([SIDE, hdr_y, LEFT_W - SIDE, hdr_y + 20], fill=ACCENT + "28")
draw.text((SIDE + 14, hdr_y + 3), "Description",
          fill=ACCENT, font=font(11, bold=True))
AMT_X = LEFT_W - SIDE - 78
draw.text((AMT_X, hdr_y + 3), "Amount",
          fill=ACCENT, font=font(11, bold=True))

# Line items
rows = [
    ("Web Design — 8 hrs",       "$800.00"),
    ("Strategy session — 2 hrs", "$200.00"),
    ("Hosting setup (one-off)",   "$120.00"),
]
row_y = hdr_y + 24
for desc, amt in rows:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 26, 4, CARD_BG)
    draw.text((SIDE + 14, row_y + 5),
              truncate(draw, desc, font(11), AMT_X - SIDE - 28),
              fill=TEXT_W, font=font(11))
    draw.text((AMT_X, row_y + 5), amt, fill=TEXT_W, font=font(11, bold=True))
    row_y += 32

# Total row
tot_y = row_y + 8
rrect(draw, SIDE, tot_y, LEFT_W - SIDE, tot_y + 34, 6, ACCENT + "33")
draw.text((SIDE + 14, tot_y + 8), "TOTAL DUE",
          fill=ACCENT, font=font(12, bold=True))
draw.text((AMT_X - 10, tot_y + 8), "$1,120.00",
          fill=ACCENT, font=font(14, bold=True))

# Pay Now button
btn_y = tot_y + 50
rrect(draw, SIDE + 110, btn_y, SIDE + 290, btn_y + 32, 6, ACCENT)
draw.text((SIDE + 150, btn_y + 7),
          truncate(draw, "Pay Now →", font(13, bold=True), 130),
          fill="#000000", font=font(13, bold=True))
draw.text((SIDE + 14, btn_y + 9),
          truncate(draw, "Wave  ✓ Free", font(10), 90),
          fill=TEXT_DIM, font=font(10))

# Tool dots
tool_dots = [
    ("#10b981", "WV"),
    ("#e44c0e", "ZI"),
    ("#3e7ef5", "IN"),
    ("#00bc70", "SQ"),
]
dot_x   = LEFT_W - 36
dot_y   = btn_y + 60
fnt_sm  = font(10, bold=True)
for col, lbl in tool_dots:
    draw_circle(draw, dot_x, dot_y, 14, col, lbl, "#ffffff", fnt_sm)
    dot_y += 36

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "W",
    name        = "Wave",
    tagline     = "Best overall free plan",
    line1       = "Unlimited invoices · unlimited clients",
    line2       = "Full accounting built in",
    badge       = "✓ Free forever",
    license_note= "Revenue from payment processing — no subscription fee",
)

draw_grid(draw, ACCENT, [
    ("#e44c0e", "ZI", "Zoho Invoice",    "5 clients · 1,000 invoices/yr"),
    ("#3e7ef5", "IN", "Invoice Ninja",   "20 clients · time tracking"),
    ("#00bc70", "SQ", "Square Invoices", "Unlimited · e-sig contracts"),
    ("#1890ff", "PP", "PayPal Invoicing","Unlimited · widely trusted"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Invoicing Software in 2026",
    subtitle = "Wave  ·  Zoho Invoice  ·  Invoice Ninja  ·  Square  ·  PayPal",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-invoicing-software.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
