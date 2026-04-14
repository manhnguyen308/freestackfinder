#!/usr/bin/env python3
"""
Feature image generator: Best Free Note-Taking Apps in 2026
Output : static/img/free-note-taking-apps.jpg  (1200×630 px)
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

# ── LEFT PANEL — mock note-taking app UI ──────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Notes — Google Keep")

# Sidebar: list of notes
SIDE_W  = 172
side_bg = "#0f1118"
draw.rectangle([0, 36, SIDE_W, CONTENT_H], fill=side_bg)

notes = [
    ("Quick Capture",     "Shopping list · personal",  True),
    ("Meeting 14 Apr",    "Q2 planning · action items", False),
    ("Project Ideas",     "Blog, side project, ...",    False),
    ("Book List 2026",    "Reading queue",              False),
    ("Recipes to Try",    "Pasta, Thai, BBQ",           False),
]
note_y = 44
for title, preview, selected in notes:
    bg = ACCENT + "33" if selected else side_bg
    draw.rectangle([2, note_y, SIDE_W - 2, note_y + 46], fill=bg)
    draw.text((10, note_y + 6),
              truncate(draw, title, font(11, bold=True), SIDE_W - 18),
              fill=TEXT_W if selected else TEXT_DIM,
              font=font(11, bold=True))
    draw.text((10, note_y + 24),
              truncate(draw, preview, font(9), SIDE_W - 18),
              fill=TEXT_DIM, font=font(9))
    note_y += 52

# Main editor area (right of sidebar inside left panel)
EDIT_X = SIDE_W + 10
EDIT_W = LEFT_W - EDIT_X - 14

# Editor card
rrect(draw, EDIT_X, 42, LEFT_W - 10, CONTENT_H - 12, 8, CARD_BG)

# Note title in editor
draw.text((EDIT_X + 14, 56),
          truncate(draw, "Quick Capture", font(16, bold=True), EDIT_W - 20),
          fill=TEXT_W, font=font(16, bold=True))
draw.text((EDIT_X + 14, 82),
          truncate(draw, "Apr 14, 2026  · personal", font(10), EDIT_W - 20),
          fill=TEXT_DIM, font=font(10))

# Divider
draw.rectangle([EDIT_X + 14, 100, LEFT_W - 24, 101], fill=ACCENT + "44")

# Note body lines
lines = [
    ("Shopping list:", True),
    ("• Milk, eggs, bread", False),
    ("• Call dentist Thu", False),
    ("• Review Q2 report", False),
    ("", False),
    ("Ideas:", True),
    ("• Start newsletter draft", False),
    ("• Check Notion template", False),
]
line_y = 110
for text, bold in lines:
    if not text:
        line_y += 6
        continue
    draw.text((EDIT_X + 14, line_y),
              truncate(draw, text, font(11, bold=bold), EDIT_W - 20),
              fill=TEXT_W if bold else "#c0c4d6",
              font=font(11, bold=bold))
    line_y += 20

# Cursor blink simulation
draw.rectangle([EDIT_X + 14, line_y + 2, EDIT_X + 15, line_y + 16], fill=ACCENT)

# Tags row
tag_y = CONTENT_H - 48
draw.text((EDIT_X + 14, tag_y),
          "Tags:", fill=TEXT_DIM, font=font(10))
for ti, tag in enumerate(["personal", "todo"]):
    tx = EDIT_X + 46 + ti * 68
    rrect(draw, tx, tag_y - 2, tx + 58, tag_y + 16, 4, ACCENT + "44")
    draw.text((tx + 6, tag_y + 1),
              truncate(draw, tag, font(9), 46),
              fill=ACCENT, font=font(9))

# Free badge
rrect(draw, EDIT_X + 14, CONTENT_H - 26, EDIT_X + 108, CONTENT_H - 8, 4, ACCENT + "33")
draw.text((EDIT_X + 20, CONTENT_H - 23),
          "✓ Completely free", fill=ACCENT, font=font(10, bold=True))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "GK",
    name        = "Google Keep",
    tagline     = "Best for quick capture",
    line1       = "Unlimited notes · labels · reminders",
    line2       = "Syncs across all devices via Google",
    badge       = "✓ Completely free — no paid tier",
    license_note= "Google account required · web + iOS + Android",
)

draw_grid(draw, ACCENT, [
    ("#f97316", "AN", "Apple Notes",     "iOS/Mac only · iCloud sync"),
    ("#3b82f6", "SN", "Standard Notes",  "Encrypted · cross-platform"),
    ("#06b6d4", "Si", "Simplenote",      "Minimal · fast · free forever"),
    ("#10b981", "No", "Notion Free",     "1,000 blocks · web clipper"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Note-Taking Apps in 2026",
    subtitle = "Google Keep  ·  Apple Notes  ·  Standard Notes  ·  Simplenote  ·  Notion",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-note-taking-apps.jpg")
img.save(out, "JPEG", quality=92)
print(f"Saved: {out}")
