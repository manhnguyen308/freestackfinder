#!/usr/bin/env python3
"""
Feature image generator: Free password managers in 2026
Output : static/img/free-password-managers.webp  (1200x630 px)
Silo   : Security   Accent: #8b5cf6

Every claim rendered here is taken from content/security/free-password-managers.md.
Dashlane and LastPass appear only as excluded options, matching the article.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image, ImageDraw
from image_helpers import (
    W, H, BG, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM,
    LEFT_W, CONTENT_H, FEAT_X, RIGHT_W, GRID_Y, CELL_H,
    font, rrect, truncate, measure_w,
    draw_chrome, draw_featured_card, draw_grid, draw_bar, img_out,
)

ACCENT = "#8b5cf6"   # Security silo, violet

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL: mock vault showing the accounts the article says to move first ─
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Vault: move these accounts first")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

draw.text((SIDE, 44), "HIGHEST VALUE ACCOUNTS",
          fill=TEXT_DIM, font=font(10, bold=True))

# Article: "Start with email, banking, cloud storage, social accounts,
# and shopping accounts, then replace reused passwords gradually."
accounts = [
    (ACCENT,    "Email",         "Recovery point for everything else"),
    ("#3b82f6", "Banking",       "Highest direct loss if reused"),
    ("#06b6d4", "Cloud storage", "Holds documents and backups"),
    ("#a855f7", "Social",        "Identity and contact takeover"),
    ("#22c55e", "Shopping",      "Saved cards and addresses"),
]

row_y, ROW_H, ROW_GAP = 66, 48, 10
for col, label, note in accounts:
    rrect(draw, SIDE, row_y, LEFT_W - SIDE, row_y + ROW_H, 6, CARD_BG)
    draw.rectangle([SIDE, row_y + 8, SIDE + 3, row_y + ROW_H - 8], fill=col)

    # Masked password dots, drawn as circles so rendering never depends on glyphs.
    dots_r, dots_gap, dots_n = 3, 9, 8
    dots_w = (dots_n - 1) * dots_gap
    dots_x = LEFT_W - SIDE - 14 - dots_w
    text_avail = dots_x - (SIDE + 14) - 12

    draw.text((SIDE + 14, row_y + 9),
              truncate(draw, label, font(13, bold=True), text_avail),
              fill=TEXT_W, font=font(13, bold=True))
    draw.text((SIDE + 14, row_y + 28),
              truncate(draw, note, font(10), text_avail),
              fill=TEXT_DIM, font=font(10))

    dy = row_y + ROW_H // 2
    for i in range(dots_n):
        cx = dots_x + i * dots_gap
        draw.ellipse([cx - dots_r, dy - dots_r, cx + dots_r, dy + dots_r],
                     fill="#4a4f66")
    row_y += ROW_H + ROW_GAP

# Two habits the article names as the real wins, as chips
draw.text((SIDE, 372), "THEN PROTECT THE VAULT",
          fill=TEXT_DIM, font=font(10, bold=True))

chips = ["Unique password per site", "2FA on email and vault"]
chip_x, CHIP_H = SIDE, 30
for label in chips:
    tw = measure_w(draw, label, font(10))
    cw = tw + 24
    # Clamp so a chip can never bleed past the panel edge.
    if chip_x + cw > LEFT_W - SIDE:
        cw = (LEFT_W - SIDE) - chip_x
        label = truncate(draw, label, font(10), cw - 24)
    rrect(draw, chip_x, 394, chip_x + cw, 394 + CHIP_H, 6, CARD_BG)
    draw.text((chip_x + 12, 394 + 9), label, fill=ACCENT, font=font(10))
    chip_x += cw + 10

# Vault stats strip
stats = [("Accounts stored", "32"), ("Reused", "0"), ("2FA enabled", "12")]
stat_x, stat_y, STAT_W = SIDE, CONTENT_H - 60, 140
for label, val in stats:
    rrect(draw, stat_x, stat_y, stat_x + STAT_W, stat_y + 40, 6, CARD_BG)
    draw.text((stat_x + 10, stat_y + 6),
              truncate(draw, label, font(9), STAT_W - 20),
              fill=TEXT_DIM, font=font(9))
    draw.text((stat_x + 10, stat_y + 20),
              truncate(draw, val, font(13, bold=True), STAT_W - 20),
              fill=TEXT_W, font=font(13, bold=True))
    stat_x += STAT_W + 10

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials     = "BW",
    name         = "Bitwarden",
    tagline      = "Best free option for most people",
    line1        = "Free: unlimited passwords, unlimited devices",
    line2        = "Open source, end-to-end encrypted, audited",
    badge        = "FIDO2 security keys included on free",
    license_note = "Premium $19.80/year adds TOTP and emergency access",
)

draw_grid(draw, ACCENT, [
    ("#3b82f6", "KP", "KeePassXC",   "Local vault file, no cloud account"),
    ("#a855f7", "PP", "Proton Pass", "Unlimited logins, 2 vaults, 10 aliases"),
    ("#06b6d4", "NP", "NordPass",    "Unlimited passwords, 1 active device"),
    ("#ef4444", "DL", "Dashlane",    "Free plan ended September 2025"),
])

# Excluded-option note. Wording tracks the article: the free plan has been
# limited to one device type since 2021.
NOTE_Y = GRID_Y + (CELL_H + 12) * 2
rrect(draw, FEAT_X, NOTE_Y, FEAT_X + RIGHT_W, NOTE_Y + 34, 6, CARD_BG)
draw.rectangle([FEAT_X, NOTE_Y + 8, FEAT_X + 3, NOTE_Y + 26], fill="#ef4444")
draw.text((FEAT_X + 14, NOTE_Y + 10),
          truncate(draw, "Not ranked: LastPass free is limited to one device type",
                   font(11), RIGHT_W - 28),
          fill=TEXT_DIM, font=font(11))

# The article's decision order: "device sync first, sharing second, and
# advanced recovery features third."
RANK_Y = NOTE_Y + 50
draw.text((FEAT_X, RANK_Y), "WHAT SEPARATES THE FREE PLANS",
          fill=TEXT_DIM, font=font(10, bold=True))

rank_x, RANK_W, RANK_H = FEAT_X, (RIGHT_W - 24) // 3, 36
for i, label in enumerate(["1. Device sync", "2. Sharing", "3. Recovery"], start=0):
    rrect(draw, rank_x, RANK_Y + 20, rank_x + RANK_W, RANK_Y + 20 + RANK_H, 6, CARD_BG)
    draw.text((rank_x + 12, RANK_Y + 20 + 11),
              truncate(draw, label, font(11, bold=True), RANK_W - 24),
              fill=ACCENT, font=font(11, bold=True))
    rank_x += RANK_W + 12

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Free password managers in 2026",
    subtitle = "Bitwarden  ·  KeePassXC  ·  Proton Pass  ·  NordPass",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-password-managers.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out} ({os.path.getsize(out) / 1024:.1f} KB)")
