#!/usr/bin/env python3
"""
Feature image generator: Best Free AI Email Tools in 2026
Output : static/img/free-ai-email-tools.webp  (1200×630 px)
Silo   : Cloud   Accent: #06b6d4
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

ACCENT = "#06b6d4"   # Cloud silo — cyan

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock AI email compose window ─────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Compose — AI Draft Assistant")

SIDE  = 20
CTX_W = LEFT_W - SIDE * 2

# AI suggestion chip
chip_y = 48
rrect(draw, SIDE, chip_y, LEFT_W - SIDE, chip_y + 18, 9, ACCENT + "25")
draw.text((SIDE + 8, chip_y + 4), "✦ AI suggestion ready", fill=ACCENT, font=font(8, bold=True))

# Mock compose fields
fields = [
    ("To:", "sarah@company.com"),
    ("Subject:", "Follow-up: Q2 proposal"),
]
fy = chip_y + 26
for label, value in fields:
    draw.text((SIDE, fy), label, fill=TEXT_DIM, font=font(8))
    draw.text((SIDE + 52, fy), value, fill=TEXT_W, font=font(8))
    fy += 16

# Divider
draw.line([SIDE, fy, LEFT_W - SIDE, fy], fill="#1e2030", width=1)
fy += 8

# Mock email body lines
body_lines = [
    "Hi Sarah,",
    "",
    "Thank you for taking the time to meet",
    "yesterday. As discussed, I've attached",
    "the revised Q2 proposal for your review.",
    "",
    "Please let me know if you have any",
]
for line in body_lines:
    if line:
        draw.text((SIDE, fy), line, fill=TEXT_W, font=font(8))
    fy += 13

# Inline AI autocomplete suggestion
fy += 2
rrect(draw, SIDE, fy, LEFT_W - SIDE, fy + 14, 3, ACCENT + "15")
draw.text((SIDE + 4, fy + 2), "questions or would like to discuss further.",
          fill=ACCENT + "cc", font=font(8))
fy += 18

# Action buttons row
btn_y = fy + 4
send_w = 52
rrect(draw, SIDE, btn_y, SIDE + send_w, btn_y + 18, 4, ACCENT)
draw.text((SIDE + 10, btn_y + 4), "Send", fill="#000000", font=font(8, bold=True))

ai_btn_x = SIDE + send_w + 10
rrect(draw, ai_btn_x, btn_y, ai_btn_x + 68, btn_y + 18, 4, CARD_BG)
draw.text((ai_btn_x + 6, btn_y + 4), "✦ Improve tone", fill=TEXT_W, font=font(8))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "AI",
    name        = "Gmail Smart Compose",
    tagline     = "Best built-in AI email — no setup needed",
    line1       = "Predictive compose · Smart Reply",
    line2       = "All Gmail accounts · no usage cap",
    badge       = "Free · built-in",
    license_note= "Included with every Gmail account",
)

draw_grid(draw, ACCENT, [
    ("#3b82f6",  "CA", "Compose AI",  "Full AI drafts · Gmail + Outlook"),
    ("#10b981",  "GP", "ChatGPT",     "Complex drafts · free daily cap"),
    ("#f97316",  "BM", "Boomerang",   "AI quality scorer · free always"),
    ("#8b5cf6",  "SP", "Spike",       "AI app · summarize + draft free"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free AI Email Tools in 2026",
    subtitle = "Gmail Smart Compose  ·  Compose AI  ·  ChatGPT  ·  Boomerang  ·  Spike",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-ai-email-tools.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
