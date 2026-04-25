#!/usr/bin/env python3
"""
Feature image generator: Best Free PDF Editor Alternatives in 2026
Output : static/img/free-pdf-editor-alternatives.webp  (1200×630 px)
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

# ── LEFT PANEL — mock PDF editor UI ──────────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "PDFgear — Contract_2026.pdf")

# Toolbar strip
TOOL_Y = 38
draw.rectangle([0, TOOL_Y, LEFT_W, TOOL_Y + 28], fill="#0f1118")
tools = ["Edit", "Annotate", "Sign", "Merge", "Compress"]
tx = 12
for t in tools:
    tw = measure_w(draw, t, font(10))
    draw.text((tx, TOOL_Y + 8), t, fill=TEXT_DIM, font=font(10))
    tx += tw + 18

# Active tool highlight (Edit)
first_tw = measure_w(draw, "Edit", font(10))
rrect(draw, 8, TOOL_Y + 5, 8 + first_tw + 8, TOOL_Y + 23, 4, ACCENT + "44")
draw.text((12, TOOL_Y + 8), "Edit", fill=ACCENT, font=font(10, bold=True))

# PDF page simulation
PAGE_X = 10
PAGE_Y = 72
PAGE_W = LEFT_W - 20
PAGE_H = CONTENT_H - PAGE_Y - 10

rrect(draw, PAGE_X, PAGE_Y, PAGE_X + PAGE_W, PAGE_Y + PAGE_H, 6, "#1c1f2e")

# PDF content lines simulating a contract document
doc_x = PAGE_X + 16
doc_y = PAGE_Y + 14

draw.text((doc_x, doc_y),
          "Service Agreement — 2026",
          fill=TEXT_W, font=font(13, bold=True))
doc_y += 24

draw.rectangle([doc_x, doc_y, PAGE_X + PAGE_W - 16, doc_y + 1], fill=ACCENT + "55")
doc_y += 10

# Simulated body text blocks
body_lines = [
    "This agreement is entered into by the parties",
    "named below, effective April 2026.",
    "",
    "1. Scope of Services",
    "   The contractor agrees to deliver the",
    "   deliverables outlined in Schedule A.",
    "",
    "2. Payment Terms",
]
for line in body_lines:
    if not line:
        doc_y += 6
        continue
    bold = line.startswith(("1.", "2.", "3."))
    draw.text((doc_x, doc_y),
              truncate(draw, line, font(10, bold=bold), PAGE_W - 32),
              fill=TEXT_W if bold else "#b0b5c8",
              font=font(10, bold=bold))
    doc_y += 17

# Highlighted annotation block
HL_Y = doc_y + 2
rrect(draw, doc_x, HL_Y, PAGE_X + PAGE_W - 16, HL_Y + 20, 3, ACCENT + "33")
draw.text((doc_x + 6, HL_Y + 4),
          truncate(draw, "   Payment due within 14 days of invoice.", font(10), PAGE_W - 44),
          fill=ACCENT, font=font(10))

# Comment bubble
CB_X = doc_x + 6
CB_Y = HL_Y + 26
rrect(draw, CB_X, CB_Y, CB_X + 160, CB_Y + 30, 5, CARD_BG)
draw.text((CB_X + 8, CB_Y + 5),
          "Reviewed", fill=ACCENT, font=font(9, bold=True))
draw.text((CB_X + 8, CB_Y + 18),
          "Check net-30 terms", fill=TEXT_DIM, font=font(9))

# Signature line
SIG_Y = PAGE_Y + PAGE_H - 60
draw.rectangle([doc_x, SIG_Y, doc_x + 140, SIG_Y + 1], fill=TEXT_DIM + "88")
draw.text((doc_x, SIG_Y + 5),
          "Signature", fill=TEXT_DIM, font=font(9))

# Signed badge
rrect(draw, doc_x + 150, SIG_Y - 6, doc_x + 248, SIG_Y + 14, 4, "#10b981" + "33")
draw.text((doc_x + 158, SIG_Y - 3),
          "✓ Signed", fill="#10b981", font=font(10, bold=True))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "PG",
    name        = "PDFgear",
    tagline     = "Best free desktop PDF editor",
    line1       = "Edit text · annotate · sign · merge",
    line2       = "No watermarks · no page limits · free",
    badge       = "✓ Full editor — no subscription needed",
    license_note= "Windows & Mac · desktop install required",
)

draw_grid(draw, ACCENT, [
    ("#8b5cf6", "P2", "PDF24 Tools",    "Browser toolkit · no login"),
    ("#06b6d4", "Se", "Sejda",          "Browser editor · 3 tasks/hr free"),
    ("#10b981", "Lo", "LibreOffice",    "Offline editing · full suite"),
    ("#f97316", "Xo", "Xodo",          "Annotate & sign · mobile-ready"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free PDF Editor Alternatives in 2026",
    subtitle = "PDFgear  ·  PDF24 Tools  ·  Sejda  ·  LibreOffice  ·  Xodo",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-pdf-editor-alternatives.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
