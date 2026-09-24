#!/usr/bin/env python3
"""
Feature image generator: Free Adobe Illustrator alternatives in 2026
Output : static/img/illustrator-alternatives.webp  (1200x630 px)
Silo   : Creative   Accent: #f97316

Tool list and export formats come from
content/creative/illustrator-alternatives.md (Inkscape, LibreOffice Draw,
SVG-edit, Canva Free). Vectr was dropped after it moved to paid plans only; the
fourth grid cell repeats the article's advice on when to keep Illustrator. The
previous image showed Gravit Designer, which the article does not cover, and an
Adobe-style "Ai" mark.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_DIM, GOOD,
    card_window, card_featured, card_grid, card_bar, mix, logo_path,
)

ACCENT = "#f97316"   # Creative silo, orange
SELECT = "#60a5fa"

c = Canvas()


def bezier(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        pts.append((
            u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1],
        ))
    return pts


# ── LEFT PANEL: vector canvas with a path being edited ────────────────────────
x0, y0, x1, y1 = card_window(c, "Inkscape: logo.svg")

# Tool column
for k in range(6):
    ty = y0 + k * 38
    active = k == 1
    c.rect(x0, ty, x0 + 30, ty + 30, mix(ACCENT, WIN_BG, 0.75) if active else CARD_BG, r=6)
    col = ACCENT if active else TEXT_DIM
    if k == 0:
        c.poly([(x0 + 10, ty + 8), (x0 + 10, ty + 22), (x0 + 14, ty + 18), (x0 + 20, ty + 23)], col)
    elif k == 1:   # node tool
        c.line([(x0 + 8, ty + 22), (x0 + 22, ty + 8)], col, 2)
        c.rect(x0 + 5, ty + 19, x0 + 11, ty + 25, col)
        c.rect(x0 + 19, ty + 5, x0 + 25, ty + 11, col)
    elif k == 2:
        c.rect(x0 + 8, ty + 8, x0 + 22, ty + 22, None, r=2, outline=col, width=2)
    elif k == 3:
        c.circle(x0 + 15, ty + 15, 7, None, outline=col, width=2)
    elif k == 4:
        c.text(x0 + 15, ty + 15, "T", 16, col, "bold", anchor="mm")
    else:
        c.poly([(x0 + 15, ty + 7), (x0 + 23, ty + 22), (x0 + 7, ty + 22)], col)

# Canvas
cx0, cy0, cx1, cy1 = x0 + 44, y0, x1, y0 + 262
c.rect(cx0, cy0, cx1, cy1, CARD_BG, r=8)
for gx in range(int(cx0) + 24, int(cx1), 24):
    c.line([(gx, cy0 + 6), (gx, cy1 - 6)], "#20243a")
for gy in range(int(cy0) + 24, int(cy1), 24):
    c.line([(cx0 + 6, gy), (cx1 - 6, gy)], "#20243a")

# A leaf-shaped logo built from two cubic curves
ox, oy = (cx0 + cx1) / 2, (cy0 + cy1) / 2
A = (ox - 110, oy + 70)
B = (ox + 110, oy - 70)
upper = bezier(A, (ox - 110, oy - 60), (ox + 10, oy - 90), B)
lower = bezier(B, (ox + 110, oy + 50), (ox - 10, oy + 90), A)
c.poly(upper + lower, mix(ACCENT, CARD_BG, 0.35))
c.line(upper + lower + [upper[0]], ACCENT, 3)
c.line([A, B], mix(ACCENT, CARD_BG, 0.6), 2)   # leaf vein

# Handles on the selected node
for hx, hy in [(ox - 110, oy - 60), (ox + 110, oy + 50)]:
    anchor = A if hx < ox else B
    c.line([anchor, (hx, hy)], SELECT, 2)
    c.circle(hx, hy, 5, SELECT)
for nx, ny in [A, B]:
    c.rect(nx - 6, ny - 6, nx + 6, ny + 6, "#ffffff", outline=SELECT, width=2)

# Export formats Inkscape lists in the article
ey = cy1 + 16
c.text(cx0, ey + 14, "EXPORT", 12, TEXT_DIM, "semibold", anchor="lm")
ex = cx0 + 70
for fmt in ["SVG", "PDF", "EPS", "PNG"]:
    ex += c.pill(ex, ey, fmt, 13, GOOD, mix(GOOD, WIN_BG, 0.78), h=28, pad_x=14) + 8

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "Ik",
    logo     = logo_path("inkscape.png"),
    name     = "Inkscape",
    tagline  = "Best for open-source vector work",
    note     = "Paths, nodes, and boolean operations on Windows, macOS, and Linux",
)

card_grid(c, [
    ("#22c55e", "LD", "LibreOffice Draw", "Diagrams and page layouts", logo_path("libreoffice-draw.png")),
    ("#8b5cf6", "SE", "SVG-edit",         "Quick SVG edits with no account needed", logo_path("svg-edit.png")),
    ("#ec4899", "Ca", "Canva Free",       "Templates with basic shapes only", logo_path("canva.png")),
    ("#64748b", "Il", "Keep Illustrator", "When .ai handoffs or Adobe plugins matter", logo_path("illustrator.png")),
])

# ── BOTTOM BAR ────────────────────────────────────────────────────────────────
card_bar(
    c, ACCENT,
    title    = "Free Adobe Illustrator alternatives in 2026",
    subtitle = "Inkscape  ·  LibreOffice Draw  ·  SVG-edit  ·  Canva Free",
)

c.save("illustrator-alternatives.webp")
