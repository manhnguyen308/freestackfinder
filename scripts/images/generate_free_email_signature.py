#!/usr/bin/env python3
"""
Feature image generator: Best Free Email Signature Makers in 2026
Output : static/img/free-email-signature.webp  (1200×630 px)
Silo   : Cloud   Accent: #3b82f6
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

ACCENT = "#3b82f6"   # Cloud silo — blue

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock email compose window with signature preview ─────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "New Email — Compose")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

# Email compose fields
fields = [
    ("To:", "client@company.com"),
    ("From:", "alex@yourdomain.com"),
    ("Subject:", "Following up — proposal attached"),
]
fy = 44
for label, val in fields:
    draw.text((SIDE, fy), label, fill=TEXT_DIM, font=font(9, bold=True))
    draw.text((SIDE + 52, fy), truncate(draw, val, font(9), CTX_W - 52),
              fill=TEXT_W, font=font(9))
    draw.line([(SIDE, fy + 16), (LEFT_W - SIDE, fy + 16)], fill="#2a2a3a", width=1)
    fy += 22

# Body area
draw.text((SIDE, fy + 4), "Hi Sarah,", fill=TEXT_W, font=font(10))
draw.text((SIDE, fy + 20), "Please find the proposal attached.", fill=TEXT_DIM, font=font(9))
draw.text((SIDE, fy + 34), "Let me know if you have any questions.", fill=TEXT_DIM, font=font(9))

# Divider before signature
sig_y = fy + 58
draw.line([(SIDE, sig_y), (LEFT_W - SIDE, sig_y)], fill="#2a2a3a", width=1)
sig_y += 10

# Signature block preview
rrect(draw, SIDE, sig_y, LEFT_W - SIDE, sig_y + 90, 6, CARD_BG)

# Avatar circle
draw_circle(draw, SIDE + 16 + 22, sig_y + 16 + 22, 22, ACCENT, "AJ")

# Name / title block
tx = SIDE + 16 + 48 + 6
draw.text((tx, sig_y + 12), "Alex Johnson", fill=TEXT_W, font=font(12, bold=True))
draw.text((tx, sig_y + 28), "Senior Account Manager", fill=TEXT_DIM, font=font(9))
draw.text((tx, sig_y + 42), "YourCompany Ltd.", fill=TEXT_DIM, font=font(9))

# Contact row
contact_y = sig_y + 60
draw.text((tx, contact_y), "+1 555 0123", fill=ACCENT, font=font(9))
draw.text((tx + 80, contact_y), "·", fill=TEXT_DIM, font=font(9))
draw.text((tx + 88, contact_y), "yourcompany.com", fill=ACCENT, font=font(9))

# Social icon stubs
icon_y = sig_y + 10
for i, col in enumerate(["#0a66c2", "#1da1f2", "#24292e"]):
    ix = LEFT_W - SIDE - 16 - i * 28
    rrect(draw, ix, icon_y, ix + 20, icon_y + 20, 4, col + "40")

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "Hs",
    name        = "HubSpot Signature",
    tagline     = "Best free — no account required",
    line1       = "No branding · clean HTML output",
    line2       = "Gmail, Outlook, Apple Mail ready",
    badge       = "100% free · no login needed",
    license_note= "Freemium — advanced features via HubSpot",
)

draw_grid(draw, ACCENT, [
    ("#e8462a",  "MS", "MySignature",    "Saved · Gmail/Outlook install"),
    ("#6366f1",  "WS", "WiseStamp",      "Established · broad templates"),
    ("#06b6d4",  "NS", "Newoldstamp",    "Modern design · clean look"),
    ("#64748b",  "SM", "Signature Maker","Minimal · branding-free"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Email Signature Makers in 2026",
    subtitle = "HubSpot  ·  MySignature  ·  WiseStamp  ·  Newoldstamp  ·  Signature Maker",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-email-signature.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
