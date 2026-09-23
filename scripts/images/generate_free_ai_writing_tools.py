#!/usr/bin/env python3
"""
Feature image generator: Free writing tools in 2026
Output : static/img/free-ai-writing-tools.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Free limits and prompting styles come from the comparison table in
content/productivity/free-ai-writing-tools.md. The article asks readers to
verify volatile limits, so the image names no model versions.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, INFO, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar,
)

ACCENT = "#6366f1"   # Productivity silo, indigo

c = Canvas()

panel_table(c, ACCENT, "Free limits and writing style",
    ["Tool", "Free limit", "Style"],
    [
        ("ChatGPT free",      [("Per-tool limits", NEUTRAL), ("Open chat", INFO)]),
        ("Claude free",       [("Session cap", WARN),        ("Open chat", INFO)]),
        ("Microsoft Copilot", [("Microsoft-set", NEUTRAL),   ("Chat, search", INFO)]),
        ("Rytr",              [("10,000 chars/mo", WARN),    ("Templates", GOOD)]),
        ("Google Gemini",     [("Can vary", NEUTRAL),        ("Open chat", INFO)]),
    ])

card_featured(
    c, ACCENT,
    initials = "GP",
    name     = "ChatGPT free",
    tagline  = "General drafting and brainstorming",
    note     = "Limits change quickly, so check caps on the current pricing page",
)

card_grid(c, [
    ("#f97316", "Cl", "Claude free",       "Long documents and edits with many constraints"),
    ("#3b82f6", "Co", "Microsoft Copilot", "Web-grounded writing inside Microsoft services"),
    ("#22c55e", "Ry", "Rytr",              "Short-form templates, 10,000 characters a month"),
    ("#eab308", "Ge", "Google Gemini",     "Drafting connected to Google services"),
])

card_bar(
    c, ACCENT,
    title    = "Free writing tools in 2026",
    subtitle = "ChatGPT  ·  Claude  ·  Microsoft Copilot  ·  Rytr  ·  Google Gemini",
)

c.save("free-ai-writing-tools.webp")
