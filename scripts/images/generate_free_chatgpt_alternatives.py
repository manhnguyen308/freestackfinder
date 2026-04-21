#!/usr/bin/env python3
"""
Feature image generator: Best Free ChatGPT Alternatives in 2026
Output : static/img/free-chatgpt-alternatives.webp  (1200×630 px)
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

# ── LEFT PANEL — mock AI chat interface ──────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Claude — Free AI Assistant")

# Sidebar: tool list
sidebar_x = 10
sidebar_items = [
    ("Claude", True),
    ("Copilot", False),
    ("Gemini", False),
    ("Perplexity", False),
    ("Meta AI", False),
]
item_y = 48
for label, active in sidebar_items:
    bg_color = ACCENT + "33" if active else WIN_BG
    rrect(draw, sidebar_x, item_y, sidebar_x + 90, item_y + 22, 4, bg_color)
    draw.text((sidebar_x + 8, item_y + 5),
              truncate(draw, label, font(9, bold=active), 76),
              fill=ACCENT if active else TEXT_DIM,
              font=font(9, bold=active))
    item_y += 28

# Chat area — right of sidebar
chat_x = 108
rrect(draw, chat_x, 44, LEFT_W - 8, CONTENT_H - 12, 8, CARD_BG)

# User message bubble
msg_y = 56
rrect(draw, chat_x + 8, msg_y, LEFT_W - 18, msg_y + 28, 6, ACCENT + "44")
draw.text((chat_x + 14, msg_y + 8),
          truncate(draw, "What's the best free ChatGPT alternative?", font(9), LEFT_W - chat_x - 36),
          fill=TEXT_W, font=font(9))

# AI response
resp_y = msg_y + 38
rrect(draw, chat_x + 8, resp_y, LEFT_W - 18, resp_y + 20, 4, ACCENT + "22")
draw.text((chat_x + 14, resp_y + 5), "Claude", fill=ACCENT, font=font(8, bold=True))

response_lines = [
    "Claude free is the strongest overall — large",
    "context window, nuanced replies, no credit",
    "card required. Microsoft Copilot gives you",
    "unlimited GPT-4 at zero cost with web search.",
    "",
    "For research with sources: try Perplexity AI.",
    "For Google Workspace: Gemini integrates natively.",
]
line_y = resp_y + 26
for text in response_lines:
    if not text:
        line_y += 5
        continue
    draw.text((chat_x + 14, line_y),
              truncate(draw, text, font(9), LEFT_W - chat_x - 28),
              fill="#c0c4d6", font=font(9))
    line_y += 16

# Cursor
draw.rectangle([chat_x + 14, line_y + 2, chat_x + 15, line_y + 12], fill=ACCENT)

# Bottom stats bar
stats_y = CONTENT_H - 44
draw.rectangle([chat_x + 8, stats_y, LEFT_W - 18, stats_y + 1], fill=ACCENT + "33")
draw.text((chat_x + 14, stats_y + 8),
          "Free plan  ·  Claude 3.5 Sonnet  ·  200K context",
          fill=TEXT_DIM, font=font(9))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials     = "Cl",
    name         = "Claude (Anthropic)",
    tagline      = "Best ChatGPT alternative overall",
    line1        = "200K context window · strong instruction-following",
    line2        = "Long docs, nuanced tasks · no credit card required",
    badge        = "✓ Free plan — no subscription needed",
    license_note = "Web · iOS · Android · claude.ai",
)

draw_grid(draw, ACCENT, [
    ("#3b82f6", "Co", "MS Copilot",   "Unlimited GPT-4 · web search"),
    ("#10b981", "Ge", "Google Gemini", "Workspace integration · Google"),
    ("#f97316", "Pe", "Perplexity",   "Cited sources · research focus"),
    ("#ef4444", "Me", "Meta AI",      "WhatsApp/Instagram · zero setup"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free ChatGPT Alternatives in 2026",
    subtitle = "Claude  ·  Copilot  ·  Gemini  ·  Perplexity  ·  Meta AI",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-chatgpt-alternatives.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
