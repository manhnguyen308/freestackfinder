#!/usr/bin/env python3
"""
Feature image generator: Free ChatGPT alternatives in 2026
Output : static/img/free-chatgpt-alternatives.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Free limits and strengths come from the comparison table in
content/productivity/free-chatgpt-alternatives.md. No model versions are
named, because the article says limits and model access change often.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, WARN, INFO, NEUTRAL,
    panel_table, card_featured, card_grid, card_bar, logo_path,
)

ACCENT = "#6366f1"   # Productivity silo, indigo

c = Canvas()

panel_table(c, ACCENT, "Free limits and key strengths",
    ["Tool", "Free limit", "Strength"],
    [
        ("Claude free",       [("Session cap", WARN),     ("Long context", INFO)]),
        ("Microsoft Copilot", [("Microsoft-set", NEUTRAL), ("Web answers", INFO)]),
        ("Google Gemini",     [("Daily, varies", WARN),   ("Google apps", INFO)]),
        ("Perplexity",        [("5 Pro a day", WARN),     ("Citations", INFO)]),
        ("Meta AI",           [("Regional", WARN),        ("Social apps", INFO)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Cl",
    logo     = logo_path("claude.png"),
    name     = "Claude free",
    tagline  = "Best for long documents",
    note     = "Strong long-context editing within a session-based usage cap",
)

card_grid(c, [
    ("#3b82f6", "Co", "Microsoft Copilot", "Web-grounded answers inside Microsoft apps", logo_path("microsoft-copilot.png")),
    ("#eab308", "Ge", "Google Gemini",     "Search and Workspace fit for Google users", logo_path("google-gemini.png")),
    ("#06b6d4", "Pe", "Perplexity",        "Cited sources, 5 Pro Searches a day", logo_path("perplexity.png")),
    ("#ec4899", "Me", "Meta AI",           "Quick answers inside social apps", logo_path("meta-ai.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free ChatGPT alternatives in 2026",
    subtitle = "Claude  ·  Microsoft Copilot  ·  Google Gemini  ·  Perplexity  ·  Meta AI",
)

c.save("free-chatgpt-alternatives.webp")
