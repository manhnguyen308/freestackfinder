#!/usr/bin/env python3
"""
Feature image generator: Best Free AI Writing Tools in 2026
Output : static/img/free-ai-writing-tools.webp  (1200×630 px)
Silo   : Productivity   Accent: #6366f1
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image, ImageDraw
from image_helpers import (
    W, H, BG, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM,
    LEFT_W, CONTENT_H, INNER_PAD,
    font, rrect, draw_circle, truncate, measure_w,
    draw_chrome, draw_featured_card, draw_grid, draw_bar, img_out,
)

ACCENT = "#6366f1"   # Productivity silo — indigo

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock AI writing interface ────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Claude — Free AI Writing Assistant")

# Prompt input area at top of editor
prompt_y = 46
rrect(draw, 10, prompt_y, LEFT_W - 10, prompt_y + 36, 6, CARD_BG)
draw.text((20, prompt_y + 10),
          truncate(draw, "Rewrite this intro — make it more concise...", font(10), LEFT_W - 40),
          fill=TEXT_DIM, font=font(10))
# Send button
btn_x = LEFT_W - 56
rrect(draw, btn_x, prompt_y + 7, btn_x + 42, prompt_y + 27, 4, ACCENT)
draw.text((btn_x + 8, prompt_y + 11), "Send", fill=TEXT_W, font=font(9, bold=True))

# AI response card
resp_y = prompt_y + 46
rrect(draw, 10, resp_y, LEFT_W - 10, CONTENT_H - 12, 8, CARD_BG)

# "AI" label badge
rrect(draw, 20, resp_y + 10, 60, resp_y + 26, 4, ACCENT + "55")
draw.text((26, resp_y + 13), "Claude", fill=ACCENT, font=font(9, bold=True))

# Response text lines
response_lines = [
    ("Free AI writing tools have improved dramatically in", False),
    ("2026. You no longer need a subscription to access", False),
    ("GPT-4-class writing assistance — ChatGPT, Claude,", False),
    ("and Copilot all offer strong free tiers.", False),
    ("", False),
    ("Key tools at no cost:", True),
    ("• ChatGPT — daily cap, GPT-4o quality", False),
    ("• Claude — best for long documents", False),
    ("• Copilot — unlimited, GPT-4 backed", False),
]
line_y = resp_y + 34
for text, bold in response_lines:
    if not text:
        line_y += 6
        continue
    draw.text((20, line_y),
              truncate(draw, text, font(10, bold=bold), LEFT_W - 36),
              fill=TEXT_W if bold else "#c0c4d6",
              font=font(10, bold=bold))
    line_y += 18

# Cursor blink
draw.rectangle([20, line_y + 2, 21, line_y + 14], fill=ACCENT)

# Stats bar at bottom of editor
stats_y = CONTENT_H - 44
draw.rectangle([10, stats_y, LEFT_W - 10, stats_y + 1], fill=ACCENT + "33")
draw.text((20, stats_y + 8),
          "Free plan  ·  Claude 3.5 Sonnet  ·  200K context",
          fill=TEXT_DIM, font=font(9))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials     = "Cl",
    name         = "Claude (Anthropic)",
    tagline      = "Best for long-form writing",
    line1        = "Claude 3.5 Sonnet · 200K context window",
    line2        = "Nuanced editing · strong instruction-following",
    badge        = "✓ Free plan — no credit card required",
    license_note = "Web · iOS · Android · claude.ai",
)

draw_grid(draw, ACCENT, [
    ("#10b981", "GP", "ChatGPT Free",    "GPT-4o daily cap · versatile"),
    ("#3b82f6", "Co", "MS Copilot",      "Unlimited GPT-4 · web search"),
    ("#f97316", "Ry", "Rytr",            "10K chars/mo · 40+ templates"),
    ("#ef4444", "CA", "Copy.ai",         "2K words/mo · marketing copy"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free AI Writing Tools in 2026",
    subtitle = "Claude  ·  ChatGPT  ·  Microsoft Copilot  ·  Rytr  ·  Copy.ai",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-ai-writing-tools.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
