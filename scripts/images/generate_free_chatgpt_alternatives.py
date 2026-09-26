#!/usr/bin/env python3
"""
Feature image generator: Free ChatGPT alternatives in 2026
Output : static/img/free-chatgpt-alternatives.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Free limits come from the comparison table in
content/productivity/free-chatgpt-alternatives.md, and the "Paid adds" column
and card notes from its "What paid plans add" section. No model versions or
prices are named, because the article says limits and model access change often.
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

panel_table(c, ACCENT, "Free limits and what paid plans add",
    ["Tool", "Free limit", "Paid adds"],
    [
        ("Claude free",       [("Session cap", WARN),     ("Claude Code", INFO)]),
        ("Microsoft Copilot", [("Microsoft-set", NEUTRAL), ("Office apps", INFO)]),
        ("Google Gemini",     [("5-hour, weekly", WARN),  ("1M context", INFO)]),
        ("Perplexity",        [("5 Pro a day", WARN),     ("Model choice", INFO)]),
        ("Grok",              [("Unpublished", WARN),    ("Video", INFO)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Cl",
    logo     = logo_path("claude.png"),
    name     = "Claude free",
    tagline  = "Best for long documents",
    note     = "Long-context editing on the free plan; Pro adds Claude Code and Claude Design",
)

card_grid(c, [
    ("#3b82f6", "Co", "Microsoft Copilot", "Web answers free; Office apps with Microsoft 365", logo_path("microsoft-copilot.png")),
    ("#eab308", "Ge", "Google Gemini",     "Google apps fit; video from Google AI Plus", logo_path("google-gemini.png")),
    ("#06b6d4", "Pe", "Perplexity",        "Cited sources; model choice on Pro", logo_path("perplexity.png")),
    ("#64748b", "Gr", "Grok",              "Live X search free; video on SuperGrok", logo_path("grok.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free ChatGPT alternatives in 2026",
    subtitle = "Claude  ·  Microsoft Copilot  ·  Google Gemini  ·  Perplexity  ·  Grok",
)

c.save("free-chatgpt-alternatives.webp")
