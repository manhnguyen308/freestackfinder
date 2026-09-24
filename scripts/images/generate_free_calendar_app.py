#!/usr/bin/env python3
"""
Feature image generator: Free calendar apps in 2026
Output : static/img/free-calendar-app.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Tool strengths come from content/productivity/free-calendar-app.md.
The week view is a generic mock-up with no product claims.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM, LINE,
    card_window, card_featured, card_grid, card_bar, mix, accent_text, logo_path,
)

ACCENT = "#6366f1"   # Productivity silo, indigo

c = Canvas()

# ── LEFT PANEL: a five-day week view ──────────────────────────────────────────
x0, y0, x1, y1 = card_window(c, "Calendar: this week")

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
TIME_W = 44
col_w = (x1 - x0 - TIME_W) / len(days)
top = y0 + 30
for i, d in enumerate(days):
    cx = x0 + TIME_W + i * col_w
    c.text(cx + col_w / 2, y0 + 8, d, 14,
           accent_text(ACCENT, WIN_BG) if i == 2 else TEXT_DIM, "semibold", anchor="mm")
    if i == 2:
        c.rect(cx + 2, top, cx + col_w - 2, y1, mix(ACCENT, WIN_BG, 0.9), r=6)
hours = ["9", "10", "11", "12", "1", "2", "3"]
hh = (y1 - top) / len(hours)
for k, h in enumerate(hours):
    yy = top + k * hh
    c.text(x0 + TIME_W - 12, yy + 2, h, 12, TEXT_DIM, anchor="ra")
    c.line([(x0 + TIME_W, yy), (x1, yy)], LINE)

events = [
    (0, 0.0, 1.0, "#3b82f6", "Team sync"),
    (0, 3.0, 4.5, "#22c55e", "Focus time"),
    (1, 1.0, 2.0, "#ec4899", "Client call"),
    (1, 4.5, 5.5, "#3b82f6", "Review"),
    (2, 0.5, 2.0, ACCENT,    "Planning"),
    (2, 5.0, 6.0, "#eab308", "1:1"),
    (3, 2.0, 3.0, "#06b6d4", "Lunch"),
    (3, 4.0, 5.5, "#22c55e", "Focus time"),
    (4, 0.0, 1.0, "#3b82f6", "Team sync"),
    (4, 2.5, 4.0, "#ec4899", "Demo"),
]
for d, a, b, col, label in events:
    ex0 = x0 + TIME_W + d * col_w + 5
    ex1 = ex0 + col_w - 10
    ey0, ey1 = top + a * hh + 3, top + b * hh - 3
    c.rect(ex0, ey0, ex1, ey1, mix(col, WIN_BG, 0.55), r=6)
    c.rect(ex0, ey0, ex0 + 4, ey1, col, r=2)
    c.fit_text(ex0 + 10, ey0 + 6, label, 12.5, ex1 - ex0 - 14, TEXT_W, "semibold")

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "GC",
    logo     = logo_path("google-calendar.png"),
    name     = "Google Calendar",
    tagline  = "Best for most users",
    note     = "Gmail adds events automatically, and it works across platforms",
)

card_grid(c, [
    ("#64748b", "N",  "Notion Calendar", "Keyboard-led scheduling beside Notion", logo_path("notion-calendar.png")),
    ("#3b82f6", "Ap", "Apple Calendar",  "Zero-setup iCloud sync on iPhone, iPad, and Mac", logo_path("apple-calendar.png")),
    ("#8b5cf6", "Pr", "Proton Calendar", "End-to-end encrypted events", logo_path("proton-calendar.png")),
    ("#ef4444", "Zo", "Zoho Calendar",   "Team scheduling linked to Zoho CRM", logo_path("zoho-calendar.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free calendar apps in 2026",
    subtitle = "Google Calendar  ·  Notion Calendar  ·  Apple Calendar  ·  Proton  ·  Zoho",
)

c.save("free-calendar-app.webp")
