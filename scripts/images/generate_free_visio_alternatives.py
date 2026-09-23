#!/usr/bin/env python3
"""
Feature image generator: Free Microsoft Visio alternatives in 2026
Output : static/img/free-visio-alternatives.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Document caps come from content/business/free-visio-alternatives.md.
The flowchart is a generic mock-up with no product claims.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, TEXT_W, TEXT_DIM,
    card_window, card_featured, card_grid, card_bar, mix,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

# ── LEFT PANEL: a flowchart on a dotted canvas ────────────────────────────────
x0, y0, x1, y1 = card_window(c, "Diagram: order process")

for gx in range(int(x0) + 10, int(x1), 22):
    for gy in range(int(y0), int(y1), 22):
        c.circle(gx, gy, 1.2, "#262a38")

cx = (x0 + x1) / 2
LINE_C = "#8a8fa8"


def arrow(ax, ay, bx, by):
    c.line([(ax, ay), (bx, by)], LINE_C, 2)
    if ax == bx:
        d = 1 if by > ay else -1
        c.poly([(bx - 6, by - 9 * d), (bx + 6, by - 9 * d), (bx, by)], LINE_C)
    else:
        d = 1 if bx > ax else -1
        c.poly([(bx - 9 * d, by - 6), (bx - 9 * d, by + 6), (bx, by)], LINE_C)


def box(bx0, by0, bx1, by1, label, col, r=8):
    c.rect(bx0, by0, bx1, by1, mix(col, CARD_BG, 0.7), r=r, outline=col, width=2)
    c.fit_text((bx0 + bx1) / 2, (by0 + by1) / 2, label, 15, bx1 - bx0 - 16, TEXT_W, "semibold", anchor="mm")


# Start
box(cx - 70, y0, cx + 70, y0 + 40, "Order received", ACCENT, r=20)
arrow(cx, y0 + 40, cx, y0 + 70)
# Decision
dy = y0 + 118
c.poly([(cx, dy - 48), (cx + 88, dy), (cx, dy + 48), (cx - 88, dy)], mix("#eab308", CARD_BG, 0.7))
c.line([(cx, dy - 48), (cx + 88, dy), (cx, dy + 48), (cx - 88, dy), (cx, dy - 48)], "#eab308", 2)
c.text(cx, dy, "In stock?", 15, TEXT_W, "semibold", anchor="mm")
# Yes branch
arrow(cx, dy + 48, cx, dy + 84)
c.text(cx + 10, dy + 64, "Yes", 12, TEXT_DIM, "semibold", anchor="lm")
box(cx - 70, dy + 84, cx + 70, dy + 124, "Ship order", "#3b82f6")
arrow(cx, dy + 124, cx, dy + 152)
box(cx - 70, dy + 152, cx + 70, y1, "Send invoice", "#3b82f6")
# No branch
arrow(cx + 88, dy, x1 - 110, dy)
c.text(cx + 100, dy - 12, "No", 12, TEXT_DIM, "semibold", anchor="lm")
box(x1 - 110, dy - 22, x1 - 6, dy + 22, "Reorder", "#ec4899")
# Left note
box(x0 + 6, dy - 22, cx - 110, dy + 22, "Notify team", "#8b5cf6")
arrow(cx - 88, dy, cx - 110, dy)

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "dr",
    name     = "draw.io (diagrams.net)",
    tagline  = "Best overall free Visio alternative",
    note     = "Unlimited diagrams and every shape library, in the cloud or on desktop",
)

card_grid(c, [
    ("#f97316", "Lu", "Lucidchart Free", "Guided cloud editor, 3 editable documents"),
    ("#eab308", "Mi", "Miro Free",       "Whiteboard diagrams, 3 editable boards"),
    ("#8b5cf6", "Wh", "Whimsical Free",  "Wireframes and flowcharts, 50 objects a month"),
    ("#3b82f6", "Vi", "Keep Visio",      "When the Visio file format decides the job"),
])

card_bar(
    c, ACCENT,
    title    = "Free Microsoft Visio alternatives in 2026",
    subtitle = "draw.io  ·  Lucidchart  ·  Miro  ·  Whimsical",
)

c.save("free-visio-alternatives.webp")
