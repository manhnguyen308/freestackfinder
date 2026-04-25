#!/usr/bin/env python3
"""
Feature image generator: Best Free Resume Builders in 2026
Output : static/img/free-resume-builders.webp  (1200×630 px)
Silo   : Business   Accent: #10b981
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

ACCENT = "#10b981"   # Business silo — emerald

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# ── LEFT PANEL — mock resume editor UI ───────────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "Canva — Resume Editor")

# Toolbar strip
TOOL_Y = 38
draw.rectangle([0, TOOL_Y, LEFT_W, TOOL_Y + 28], fill="#0f1118")
tool_labels = ["Templates", "Text", "Layout", "Download"]
tx = 12
for t in tool_labels:
    tw = measure_w(draw, t, font(10))
    draw.text((tx, TOOL_Y + 8), t, fill=TEXT_DIM, font=font(10))
    tx += tw + 18

# Highlight "Templates" as active
first_tw = measure_w(draw, "Templates", font(10))
rrect(draw, 8, TOOL_Y + 5, 8 + first_tw + 8, TOOL_Y + 23, 4, ACCENT + "44")
draw.text((12, TOOL_Y + 8), "Templates", fill=ACCENT, font=font(10, bold=True))

# Resume page mock
PAGE_X = 10
PAGE_Y = 72
PAGE_W = LEFT_W - 20
PAGE_H = CONTENT_H - PAGE_Y - 10

rrect(draw, PAGE_X, PAGE_Y, PAGE_X + PAGE_W, PAGE_Y + PAGE_H, 6, "#1c1f2e")

doc_x = PAGE_X + 16
doc_y = PAGE_Y + 14

# Name / title header block
rrect(draw, PAGE_X + 4, PAGE_Y + 4, PAGE_X + PAGE_W - 4, PAGE_Y + 52, 5, ACCENT + "22")
draw.rectangle([PAGE_X + 4, PAGE_Y + 4, PAGE_X + 8, PAGE_Y + 52], fill=ACCENT)
draw.text((doc_x + 4, PAGE_Y + 10),
          truncate(draw, "Alex Morgan", font(16, bold=True), PAGE_W - 40),
          fill=TEXT_W, font=font(16, bold=True))
draw.text((doc_x + 4, PAGE_Y + 32),
          truncate(draw, "Product Manager  ·  alex@email.com", font(10), PAGE_W - 40),
          fill=ACCENT, font=font(10))

doc_y = PAGE_Y + 60

# Section: Experience
draw.text((doc_x, doc_y),
          "EXPERIENCE", fill=ACCENT, font=font(9, bold=True))
draw.rectangle([doc_x, doc_y + 14, PAGE_X + PAGE_W - 16, doc_y + 15], fill=ACCENT + "44")
doc_y += 20

exp_items = [
    ("Senior PM · Startup Co.", "2023 – Present"),
    ("• Led 0→1 product launch, 40k users", ""),
    ("• Defined roadmap across 3 teams", ""),
]
for title, date in exp_items:
    bold = not title.startswith("•")
    row_color = TEXT_W if bold else "#b0b5c8"
    draw.text((doc_x, doc_y),
              truncate(draw, title, font(10, bold=bold), PAGE_W - 60),
              fill=row_color, font=font(10, bold=bold))
    if date:
        draw.text((PAGE_X + PAGE_W - 80, doc_y),
                  date, fill=TEXT_DIM, font=font(9))
    doc_y += 16

doc_y += 6

# Section: Skills
draw.text((doc_x, doc_y),
          "SKILLS", fill=ACCENT, font=font(9, bold=True))
draw.rectangle([doc_x, doc_y + 14, PAGE_X + PAGE_W - 16, doc_y + 15], fill=ACCENT + "44")
doc_y += 20

skills = ["Roadmap planning", "Stakeholder comms", "Data analysis", "Agile / Scrum"]
sx = doc_x
for s in skills:
    sw = measure_w(draw, s, font(9)) + 14
    if sx + sw > PAGE_X + PAGE_W - 16:
        sx = doc_x
        doc_y += 22
    rrect(draw, sx, doc_y, sx + sw, doc_y + 18, 4, ACCENT + "33")
    draw.text((sx + 7, doc_y + 3), s, fill=ACCENT, font=font(9))
    sx += sw + 6

doc_y += 28

# Section: Education
draw.text((doc_x, doc_y),
          "EDUCATION", fill=ACCENT, font=font(9, bold=True))
draw.rectangle([doc_x, doc_y + 14, PAGE_X + PAGE_W - 16, doc_y + 15], fill=ACCENT + "44")
doc_y += 20
draw.text((doc_x, doc_y),
          truncate(draw, "BSc Business Administration", font(10, bold=True), PAGE_W - 32),
          fill=TEXT_W, font=font(10, bold=True))
draw.text((PAGE_X + PAGE_W - 80, doc_y), "2018–2022", fill=TEXT_DIM, font=font(9))

# ATS badge
rrect(draw, doc_x, CONTENT_H - 30, doc_x + 150, CONTENT_H - 10, 4, "#10b981" + "33")
draw.text((doc_x + 8, CONTENT_H - 26),
          "✓ ATS-friendly format", fill=ACCENT, font=font(10, bold=True))

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "Cv",
    name        = "Canva",
    tagline     = "Best free resume builder",
    line1       = "Templates · drag-and-drop editor",
    line2       = "Free PDF download, no watermark",
    badge       = "✓ Free download — no subscription needed",
    license_note= "Browser-based · Google account optional",
)

draw_grid(draw, ACCENT, [
    ("#3b82f6", "GD", "Google Docs",      "ATS-safe · export PDF/Word"),
    ("#ef4444", "In", "Indeed Builder",   "Apply on Indeed directly"),
    ("#8b5cf6", "Rc", "Resume.com",       "Guided prompts · free PDF"),
    ("#f97316", "Kk", "Kickresume",       "Polished templates · limited free"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Resume Builders in 2026",
    subtitle = "Canva  ·  Google Docs  ·  Indeed  ·  Resume.com  ·  No hidden paywalls",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-resume-builders.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
