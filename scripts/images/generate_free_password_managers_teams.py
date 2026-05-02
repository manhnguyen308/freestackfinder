#!/usr/bin/env python3
"""
Feature image generator: Best Free Password Managers for Teams in 2026
Output : static/img/free-password-managers-teams.webp  (1200×630 px)
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

# ── LEFT PANEL — mock team vault dashboard ────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Team Vault — Shared Collections")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

# Section label
draw.text((SIDE, 44), "Shared credentials", fill=TEXT_DIM, font=font(11, bold=True))

# Vault rows
vaults = [
    (ACCENT,    "Production servers",   "8 items",  "3 members"),
    ("#3b82f6", "Client portals",       "14 items", "2 members"),
    ("#10b981", "Dev tools & APIs",     "22 items", "5 members"),
    ("#f59e0b", "Social & marketing",   "6 items",  "2 members"),
    ("#ef4444", "Finance & billing",    "4 items",  "1 member"),
]

row_y = 64
for col, label, items, members in vaults:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + 36, 5, CARD_BG)
    draw.rectangle([SIDE, row_y, SIDE + 4, row_y + 36], fill=col)
    draw.text((SIDE + 12, row_y + 4),  label,  fill=TEXT_DIM, font=font(10))
    draw.text((SIDE + 12, row_y + 18), items,  fill=TEXT_W,   font=font(12, bold=True))
    draw.text((LEFT_W - SIDE - 80, row_y + 12),
              truncate(draw, members, font(9), 76),
              fill=col, font=font(9, bold=True))
    row_y += 43

# Stats bar
stats = [("Team members", "5"), ("Collections", "5"), ("Items shared", "54")]
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
    initials    = "BW",
    name        = "Bitwarden",
    tagline     = "Best free team password manager",
    line1       = "Free: 2 users cloud · unlimited self-hosted",
    line2       = "Open-source · end-to-end encrypted · audited",
    badge       = "Free organizations tier",
    license_note= "Teams plan from $3/user/month",
)

draw_grid(draw, ACCENT, [
    ("#6366f1", "VW", "Vaultwarden",  "Self-hosted · Bitwarden API · low resources"),
    ("#22c55e", "PB", "Passbolt",     "Open source · GPG · fine-grained sharing"),
    ("#1a1a2e", "KP", "KeePassXC",    "Shared file · any cloud storage · zero cost"),
    ("#3b82f6", "BH", "Self-Host",    "Unlimited users · full features · own server"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Password Managers for Teams in 2026",
    subtitle = "Bitwarden  ·  Vaultwarden  ·  Passbolt  ·  KeePassXC",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-password-managers-teams.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
