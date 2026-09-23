#!/usr/bin/env python3
"""
Feature image generator: Free accounting software in 2026
Output : static/img/free-accounting-software.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Tool facts come from content/business/free-accounting-software.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, INFO,
    panel_list, card_featured, card_grid, card_bar,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

panel_list(c, "Where the books live", [
    ("#10b981", "Wave",       "Invoices, bills, and bookkeeping",   "Cloud",       INFO),
    ("#ef4444", "Zoho Books", "Cloud accounting and client portal", "Cloud",       INFO),
    ("#3b82f6", "Akaunting",  "Open source, self-hosted for free",  "Self-hosted", WARN),
    ("#eab308", "Manager",    "Unlimited transactions on desktop",  "Offline",     GOOD),
    ("#8b5cf6", "GnuCash",    "Open-source double-entry",           "Offline",     GOOD),
], section="Bookkeeping model")

card_featured(
    c, ACCENT,
    initials = "Wa",
    name     = "Wave",
    tagline  = "Best overall for freelancers",
    note     = "Invoices and bookkeeping free. Bank imports and receipt capture need Pro",
)

card_grid(c, [
    ("#ef4444", "ZB", "Zoho Books", "For Zoho users, with regional revenue caps"),
    ("#3b82f6", "Ak", "Akaunting",  "Open source, needs a PHP and MySQL server"),
    ("#eab308", "Mg", "Manager",    "Offline desktop books for a single user"),
    ("#8b5cf6", "Gn", "GnuCash",    "Double-entry for disciplined sole proprietors"),
])

card_bar(
    c, ACCENT,
    title    = "Free accounting software in 2026",
    subtitle = "Wave  ·  Zoho Books  ·  Akaunting  ·  Manager  ·  GnuCash",
)

c.save("free-accounting-software.webp")
