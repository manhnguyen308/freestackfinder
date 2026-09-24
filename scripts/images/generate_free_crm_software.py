#!/usr/bin/env python3
"""
Feature image generator: Free CRM software in 2026
Output : static/img/free-crm-software.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

User caps and focus come from content/business/free-crm-software.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, WARN, BAD, INFO,
    panel_table, note_card, table_bottom, card_featured, card_grid, card_bar, logo_path, glyph,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

x0, y0, x1, y1 = panel_table(c, ACCENT, "Free CRM plans by team size",
    ["CRM", "Free users", "Focus"],
    [
        ("HubSpot CRM",  [("2 users", WARN),     ("Contacts, deals", INFO)]),
        ("Zoho CRM",     [("3 users", WARN),     ("Classic CRM", INFO)]),
        ("Freshsales",   [("3 users", WARN),     ("Kanban pipeline", INFO)]),
        ("Bitrix24",     [("Unclear cap", BAD),  ("CRM, workspace", INFO)]),
    ])

note_card(c, ACCENT, x0, table_bottom(y0, 4, y1) + 14, x1, y1, "Rule",
          "Use the smallest CRM that covers the live pipeline")

card_featured(
    c, ACCENT,
    initials = "Hs",
    logo     = logo_path("hubspot.png"),
    name     = "HubSpot CRM Free",
    tagline  = "For solo operators and two-person teams",
    note     = "Contacts, deals, scheduling, and email tracking, capped at two users",
)

card_grid(c, [
    ("#ef4444", "Zo", "Zoho CRM Free",   "Classic sales workflow for up to three users", logo_path("zoho-crm.png")),
    ("#3b82f6", "Fs", "Freshsales Free", "Visual pipeline with built-in email and phone", logo_path("freshsales.png")),
    ("#06b6d4", "Bx", "Bitrix24 Free",   "CRM plus tasks and chat, unclear user cap", logo_path("bitrix24.png")),
    ("#64748b", "$",  "Paid CRM",        "When seats, records, or automation run out", glyph("coin", "#64748b")),
])

card_bar(
    c, ACCENT,
    title    = "Free CRM software in 2026",
    subtitle = "HubSpot  ·  Zoho CRM  ·  Freshsales  ·  Bitrix24",
)

c.save("free-crm-software.webp")
