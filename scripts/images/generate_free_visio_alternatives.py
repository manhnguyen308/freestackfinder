#!/usr/bin/env python3
"""
Feature image generator: Best Free Microsoft Visio Alternatives in 2026
Output : static/img/free-visio-alternatives.webp  (1200×630 px)
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

# ── LEFT PANEL — mock draw.io diagram editor ──────────────────────────────────
draw.rectangle([0, 0, LEFT_W, CONTENT_H], fill=WIN_BG)
draw_chrome(draw, "draw.io — System Architecture")

# Toolbar strip
TOOL_Y = 38
draw.rectangle([0, TOOL_Y, LEFT_W, TOOL_Y + 28], fill="#0f1118")
tool_labels = ["File", "Edit", "View", "Extras", "Help"]
tx = 12
for t in tool_labels:
    tw = measure_w(draw, t, font(10))
    draw.text((tx, TOOL_Y + 8), t, fill=TEXT_DIM, font=font(10))
    tx += tw + 18

# Shape palette sidebar (narrow strip on left of canvas)
PAL_X = 0
PAL_W = 56
draw.rectangle([PAL_X, TOOL_Y + 28, PAL_X + PAL_W, CONTENT_H], fill="#0d0f18")
palette_labels = ["Flow", "UML", "Net", "AWS", "More"]
py = TOOL_Y + 38
for lbl in palette_labels:
    draw.text((PAL_X + 8, py), lbl, fill=TEXT_DIM, font=font(9))
    py += 22

# Highlight "Flow" as active
rrect(draw, PAL_X + 4, TOOL_Y + 34, PAL_X + PAL_W - 4, TOOL_Y + 52, 3, ACCENT + "44")
draw.text((PAL_X + 8, TOOL_Y + 38), "Flow", fill=ACCENT, font=font(9, bold=True))

# Canvas area (rest of left panel after palette)
CANVAS_X = PAL_W + 4
CANVAS_W = LEFT_W - CANVAS_X - 4

# Draw a simple flowchart on the canvas
# Node dimensions
NW, NH = 110, 32
NX = CANVAS_X + (CANVAS_W - NW) // 2

def node(y, label, color=CARD_BG, text_color=TEXT_W, is_decision=False):
    """Draw a flowchart node rectangle."""
    nx = CANVAS_X + (CANVAS_W - NW) // 2
    rrect(draw, nx, y, nx + NW, y + NH, 6, color)
    lw = measure_w(draw, label, font(10, bold=True))
    draw.text((nx + (NW - lw) // 2, y + (NH - 12) // 2),
              label, fill=text_color, font=font(10, bold=True))
    return nx, y

def connector(y_top, y_bot):
    """Draw a vertical connector arrow."""
    cx = CANVAS_X + CANVAS_W // 2
    draw.line([(cx, y_top), (cx, y_bot - 6)], fill=TEXT_DIM, width=1)
    draw.polygon([(cx - 4, y_bot - 6), (cx + 4, y_bot - 6), (cx, y_bot)], fill=TEXT_DIM)

FLOW_Y = 76
node(FLOW_Y, "Start", ACCENT + "cc", "#000000")
connector(FLOW_Y + NH, FLOW_Y + NH + 16)

node(FLOW_Y + NH + 16, "Process data", CARD_BG, TEXT_W)
connector(FLOW_Y + NH*2 + 16, FLOW_Y + NH*2 + 32)

# Decision diamond (approximated with a rectangle + label)
DY = FLOW_Y + NH*2 + 32
rrect(draw, NX, DY, NX + NW, DY + NH, 6, "#1e293b")
draw.text((NX + 6, DY + 8), "Valid?", fill=TEXT_W, font=font(10, bold=True))
# Yes/No branch labels
draw.text((NX + NW + 4, DY + 8), "Yes →", fill=ACCENT, font=font(9))
draw.text((NX - 32, DY + 8), "← No", fill="#ef4444", font=font(9))
connector(DY + NH, DY + NH + 16)

node(DY + NH + 16, "Send output", CARD_BG, TEXT_W)
connector(DY + NH*2 + 16, DY + NH*2 + 32)

node(DY + NH*2 + 32, "End", "#374151", TEXT_W)

# Property panel hint (right side of canvas)
PP_X = NX + NW + 12
PP_W = LEFT_W - PP_X - 4
if PP_W > 40:
    draw.text((PP_X, FLOW_Y), "Shape", fill=TEXT_DIM, font=font(9, bold=True))
    props = ["Fill", "Stroke", "Font", "Size"]
    py2 = FLOW_Y + 16
    for p in props:
        draw.text((PP_X, py2), p, fill=TEXT_DIM, font=font(8))
        py2 += 14

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
draw_featured_card(
    draw, ACCENT,
    initials    = "Di",
    name        = "draw.io (diagrams.net)",
    tagline     = "Best free Visio alternative",
    line1       = "Unlimited diagrams · all shape libraries · desktop + browser",
    line2       = "Flowchart · UML · ERD · Network · AWS · Azure · BPMN",
    badge       = "✓ Completely free — open source, no account required",
    license_note= "Browser + desktop app · Google Drive / Confluence integration",
)

draw_grid(draw, ACCENT, [
    ("#3b82f6", "Lc", "Lucidchart Free",   "3 documents · real-time collaboration"),
    ("#f97316", "Mi", "Miro Free",         "3 boards · whiteboard + flowcharts"),
    ("#8b5cf6", "Wh", "Whimsical Free",    "4 boards · flowcharts + wireframes"),
    ("#6b7280", "LO", "LibreOffice Draw",  "Offline · Visio-compatible · free"),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
draw_bar(
    draw, ACCENT,
    title    = "Best Free Microsoft Visio Alternatives in 2026",
    subtitle = "draw.io  ·  Lucidchart Free  ·  Miro  ·  Whimsical  ·  No subscription needed",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out = img_out("free-visio-alternatives.webp")
img.save(out, "WEBP", quality=82, method=4)
print(f"Saved: {out}")
