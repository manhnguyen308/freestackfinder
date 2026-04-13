#!/usr/bin/env python3
"""
Feature image generator for: Best Free Invoicing Software in 2026
Output: static/img/free-invoicing-software.jpg (1200x630px)
Silo: Business  Accent: #10b981
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
BG       = "#101116"
CARD_BG  = "#1a1d27"
ACCENT   = "#10b981"   # Business silo — emerald green
TEXT_W   = "#ffffff"
TEXT_DIM = "#8a8fa8"
WIN_BG   = "#13161f"

out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "static", "img")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "free-invoicing-software.jpg")

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── font helpers ──────────────────────────────────────────────────────────────
def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def circle(cx, cy, r, color, text="", text_color="#ffffff", fnt=None):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)
    if text and fnt:
        bb = draw.textbbox((0, 0), text, font=fnt)
        tw, th = bb[2]-bb[0], bb[3]-bb[1]
        draw.text((cx - tw//2, cy - th//2), text, fill=text_color, font=fnt)

def rounded_rect(x0, y0, x1, y1, r, color):
    draw.rectangle([x0+r, y0, x1-r, y1], fill=color)
    draw.rectangle([x0, y0+r, x1, y1-r], fill=color)
    for cx, cy in [(x0+r, y0+r), (x1-r, y0+r), (x0+r, y1-r), (x1-r, y1-r)]:
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)

# ── layout constants ──────────────────────────────────────────────────────────
LEFT_W   = 480   # left panel width
RIGHT_X  = LEFT_W + 20
RIGHT_W  = W - RIGHT_X - 20
BOT_H    = 90    # bottom bar height
CONTENT_H = H - BOT_H

# ── LEFT PANEL — mock invoice UI ─────────────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)

# macOS window chrome
chrome_y = 18
for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
    draw.ellipse([16 + i*22 - 6, chrome_y-6, 16 + i*22 + 6, chrome_y+6], fill=col)

# Title bar text
draw.text((80, chrome_y - 7), "Invoice #1042  —  Wave", fill=TEXT_DIM, font=font(12))

# Invoice header block
draw.rectangle([20, 50, LEFT_W-20, 150], fill=CARD_BG)
draw.text((36, 62), "INVOICE", fill=ACCENT, font=font(16, bold=True))
draw.text((36, 84), "#1042", fill=TEXT_W, font=font(22, bold=True))
draw.text((36, 116), "Date: Apr 13, 2026", fill=TEXT_DIM, font=font(12))
draw.text((36, 132), "Due: Apr 27, 2026", fill=TEXT_DIM, font=font(12))

# Invoice line items
rows = [
    ("Web Design — 8 hrs", "$800.00"),
    ("Strategy session — 2 hrs", "$200.00"),
    ("Hosting setup (one-off)", "$120.00"),
]
y = 168
draw.rectangle([20, y-4, LEFT_W-20, y+14], fill=ACCENT + "22")
draw.text((36, y), "Description", fill=ACCENT, font=font(11, bold=True))
draw.text((LEFT_W-90, y), "Amount", fill=ACCENT, font=font(11, bold=True))

y += 24
for desc, amt in rows:
    draw.rectangle([20, y-2, LEFT_W-20, y+22], fill=CARD_BG)
    draw.text((36, y+2), desc, fill=TEXT_W, font=font(12))
    draw.text((LEFT_W-90, y+2), amt, fill=TEXT_W, font=font(12, bold=True))
    y += 30

# Total
draw.rectangle([20, y+8, LEFT_W-20, y+36], fill=ACCENT + "33")
draw.text((36, y+14), "TOTAL DUE", fill=ACCENT, font=font(13, bold=True))
draw.text((LEFT_W-110, y+14), "$1,120.00", fill=ACCENT, font=font(16, bold=True))

# Pay now button
btn_y = y + 52
rounded_rect(140, btn_y, 340, btn_y+34, 6, ACCENT)
draw.text((185, btn_y+7), "Pay Now →", fill="#000000", font=font(14, bold=True))

# "Sent by Wave — free forever" label
draw.text((36, btn_y+10), "Wave  ✓ Free", fill=TEXT_DIM, font=font(11))

# Small tool logos column on the left edge
tool_dots = [
    ("#10b981", "WV"),  # Wave
    ("#e44c0e", "ZI"),  # Zoho Invoice
    ("#3e7ef5", "IN"),  # Invoice Ninja
    ("#00bc70", "SQ"),  # Square
]
dot_x = LEFT_W - 40
dot_start_y = 310
fnt_sm = font(10, bold=True)
for col, label in tool_dots:
    circle(dot_x, dot_start_y, 14, col, label, "#ffffff", fnt_sm)
    dot_start_y += 40

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
# Featured card — Wave
FEAT_X = RIGHT_X
FEAT_W = RIGHT_W
FEAT_Y = 20
FEAT_H = 160

rounded_rect(FEAT_X, FEAT_Y, FEAT_X+FEAT_W, FEAT_Y+FEAT_H, 10, CARD_BG)
# accent left bar
draw.rectangle([FEAT_X, FEAT_Y+10, FEAT_X+4, FEAT_Y+FEAT_H-10], fill=ACCENT)

circle(FEAT_X+44, FEAT_Y+50, 28, ACCENT, "W", "#000000", font(18, bold=True))

draw.text((FEAT_X+84, FEAT_Y+22), "Wave", fill=TEXT_W, font=font(20, bold=True))
draw.text((FEAT_X+84, FEAT_Y+50), "Best overall free plan", fill=ACCENT, font=font(13))
draw.text((FEAT_X+84, FEAT_Y+72), "Unlimited invoices · Unlimited clients", fill=TEXT_DIM, font=font(12))
draw.text((FEAT_X+84, FEAT_Y+90), "Full accounting built in", fill=TEXT_DIM, font=font(12))

draw.text((FEAT_X+14, FEAT_Y+120), "✓ Free forever", fill=ACCENT, font=font(12, bold=True))
draw.text((FEAT_X+14, FEAT_Y+138), "Payment processing revenue model — no subscription", fill=TEXT_DIM, font=font(11))

# 2×2 comparison grid
tools_grid = [
    ("#e44c0e", "ZI", "Zoho Invoice",    "5 clients · 1,000 invoices/yr"),
    ("#3e7ef5", "IN", "Invoice Ninja",   "20 clients · time tracking"),
    ("#00bc70", "SQ", "Square Invoices", "Unlimited · e-sig contracts"),
    ("#1890ff", "PP", "PayPal Invoicing","Unlimited · client familiarity"),
]

GRID_Y = FEAT_Y + FEAT_H + 16
CELL_W = (FEAT_W - 12) // 2
CELL_H = 90

for i, (col, initials, name, sub) in enumerate(tools_grid):
    col_off = i % 2
    row_off = i // 2
    cx = FEAT_X + col_off * (CELL_W + 12)
    cy = GRID_Y + row_off * (CELL_H + 12)

    rounded_rect(cx, cy, cx+CELL_W, cy+CELL_H, 8, CARD_BG)
    circle(cx+30, cy+CELL_H//2, 22, col, initials, "#ffffff", font(11, bold=True))
    draw.text((cx+62, cy+18), name, fill=TEXT_W, font=font(13, bold=True))
    draw.text((cx+62, cy+38), sub, fill=TEXT_DIM, font=font(10))

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
BAR_Y = CONTENT_H
draw.rectangle([0, BAR_Y, W, H], fill=ACCENT)

# Site badge
draw.text((28, BAR_Y+12), "FreeStackFinder.com", fill="#000000", font=font(12, bold=True))

# Article title
draw.text((28, BAR_Y+34), "Best Free Invoicing Software in 2026", fill="#000000", font=font(22, bold=True))

# Tools subtitle
draw.text((28, BAR_Y+66), "Wave  ·  Zoho Invoice  ·  Invoice Ninja  ·  Square", fill="#000000", font=font(13))

# ── save ──────────────────────────────────────────────────────────────────────
img.save(out_path, "JPEG", quality=92)
print(f"Saved: {out_path}")
