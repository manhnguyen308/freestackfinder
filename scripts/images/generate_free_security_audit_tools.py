#!/usr/bin/env python3
"""
Feature image generator: Best Free Security Audit Tools in 2026
Output : static/img/free-security-audit-tools.webp  (1200×630 px)
Silo   : Security   Accent: #8b5cf6
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

ACCENT = "#8b5cf6"   # Security silo — violet

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock scan dashboard ─────────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Security Audit — Scan Results")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

draw.text((SIDE, 44), "Latest scan findings", fill=TEXT_DIM, font=font(11, bold=True))

findings = [
    (ACCENT,    "Web headers",     "3 missing",   "Medium"),
    ("#ef4444", "Open ports",      "2 exposed",   "High"),
    ("#22c55e", "TLS grade",       "A+",          "Passed"),
    ("#f59e0b", "CVEs detected",   "1 outdated",  "Warning"),
    ("#3b82f6", "System hardening","62/100",      "Review"),
]

row_y = 64
for col, label, value, status in findings:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 36, 5, CARD_BG)
    draw.rectangle([SIDE, row_y, SIDE + 4, row_y + 36], fill=col)
    draw.text((SIDE + 12, row_y + 4),  label,  fill=TEXT_DIM, font=font(10))
    draw.text((SIDE + 12, row_y + 18), value,  fill=TEXT_W,   font=font(12, bold=True))
    draw.text((LEFT_W - SIDE - 80, row_y + 12),
              truncate(draw, status, font(9), 76),
              fill=col, font=font(9, bold=True))
    row_y += 43

stats = [("Hosts scanned", "4"), ("Issues found", "6"), ("Critical", "1")]
stat_x = SIDE
stat_y = CONTENT_H - 48
for label, val in stats:
    rrect(draw, stat_x, stat_y, stat_x + 130, stat_y + 36, 6, CARD_BG)
    draw.text((stat_x + 8, stat_y + 4),
              truncate(draw, label, font(9), 114),
              fill=TEXT_DIM, font=font(9))
    draw.text((stat_x + 8, stat_y + 18),
              truncate(draw, val, font(12, bold=True), 114),
              fill=TEXT_W, font=font(12, bold=True))
    stat_x += 138

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "ZP",
    name        = "OWASP ZAP",
    tagline     = "Best free web application scanner",
    line1       = "Full scanner · passive + active scan · CI/CD support",
    line2       = "No feature cap · open-source · no registration needed",
    badge       = "Fully free — no paid tier required",
    license_note= "Open-source (Apache 2.0) — no restrictions",
)

draw_grid(draw, ACCENT, [
    ("#ef4444", "NM", "Nmap",          "Network & port discovery · fully open-source"),
    ("#6366f1", "LY", "Lynis",         "Linux/Unix system hardening · 300+ checks"),
    ("#f97316", "NK", "Nikto",         "Web server quick scan · 6 700+ checks"),
    ("#0ea5e9", "GB", "Greenbone CE",  "Vulnerability scanner · 60k+ CVE tests"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Security Audit Tools in 2026",
    subtitle = "OWASP ZAP  ·  Nmap  ·  Lynis  ·  Nikto  ·  Greenbone",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-security-audit-tools.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
