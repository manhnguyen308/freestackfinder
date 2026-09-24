#!/usr/bin/env python3
"""
Feature image generator: Free project management software in 2026
Output : static/img/free-project-management-software.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Plan caps come from content/business/free-project-management-software.md.
The Kanban board is a generic mock-up with no product claims.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_DIM,
    card_window, card_featured, card_grid, card_bar, mix, logo_path,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

# ── LEFT PANEL: three-column Kanban board ─────────────────────────────────────
x0, y0, x1, y1 = card_window(c, "Board: website launch")

cols = [
    ("To do", 3, [("#3b82f6", 0.8, 0.5), ("#eab308", 0.7, 0.0), ("#ec4899", 0.9, 0.6)]),
    ("Doing", 3, [(ACCENT, 0.85, 0.55), ("#8b5cf6", 0.6, 0.0), ("#f97316", 0.75, 0.45)]),
    ("Done",  3, [("#22c55e", 0.7, 0.0), ("#06b6d4", 0.8, 0.5), ("#3b82f6", 0.65, 0.0)]),
]
GAP = 12
cw = (x1 - x0 - GAP * 2) / 3
for i, (name, count, cards) in enumerate(cols):
    cx0 = x0 + i * (cw + GAP)
    c.rect(cx0, y0 - 4, cx0 + cw, y1, mix(CARD_BG, WIN_BG, 0.7), r=10)
    c.text(cx0 + 14, y0 + 16, name.upper(), 12, TEXT_DIM, "semibold", anchor="lm")
    c.text(cx0 + cw - 14, y0 + 16, str(count), 12, TEXT_DIM, "semibold", anchor="rm")
    cy = y0 + 34
    for col, w1, w2 in cards:
        h = 92 if w2 else 70
        c.rect(cx0 + 8, cy, cx0 + cw - 8, cy + h, "#252a3a", r=8)
        c.rect(cx0 + 18, cy + 14, cx0 + 54, cy + 22, col, r=4)
        inner = cw - 36
        c.rect(cx0 + 18, cy + 34, cx0 + 18 + inner * w1, cy + 44, "#4a4f66", r=4)
        if w2:
            c.rect(cx0 + 18, cy + 52, cx0 + 18 + inner * w2, cy + 62, "#3a3f52", r=4)
        c.circle(cx0 + cw - 26, cy + h - 18, 10, mix(col, CARD_BG, 0.3))
        cy += h + 10

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "Tr",
    logo     = logo_path("trello.png"),
    name     = "Trello Free",
    tagline  = "Kanban boards for up to ten collaborators",
    note     = "Unlimited cards and Power-Ups, capped at 10 boards",
)

card_grid(c, [
    ("#ef4444", "As", "Asana Personal", "List, board, and calendar for two users", logo_path("asana.png")),
    ("#64748b", "N",  "Notion Free",    "Tasks with docs, 10 guests, 7-day history", logo_path("notion.png")),
    ("#8b5cf6", "CU", "ClickUp Free",   "Unlimited members, 60MB of storage", logo_path("clickup.png")),
    ("#3b82f6", "Li", "Linear Free",    "Two teams and 250 issues for developers", logo_path("linear.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free project management software in 2026",
    subtitle = "Trello  ·  Asana  ·  Notion  ·  ClickUp  ·  Linear",
)

c.save("free-project-management-software.webp")
