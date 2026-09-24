#!/usr/bin/env python3
"""
Feature image generator: Free QuickBooks alternatives in 2026
Output : static/img/quickbooks-alternatives.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Free-plan and bank-sync values come from the comparison table in
content/business/quickbooks-alternatives.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN, BAD,
    panel_table, card_featured, card_grid, card_bar, logo_path,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

panel_table(c, ACCENT, "Free plans and bank sync",
    ["Tool", "Free plan", "Bank sync"],
    [
        ("Wave",          [("Yes", GOOD),         ("Paid", WARN)]),
        ("Zoho Books",    [("With limits", WARN), ("Yes", GOOD)]),
        ("Invoice Ninja", [("5 clients", WARN),   ("No", BAD)]),
        ("GnuCash",       [("Yes", GOOD),         ("Manual", WARN)]),
        ("FreshBooks",    [("Trial only", BAD),   ("Yes", GOOD)]),
        ("QuickBooks",    [("Paid only", BAD),    ("Yes", GOOD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "Wa",
    logo     = logo_path("wave.png"),
    name     = "Wave",
    tagline  = "Bookkeeping and invoices for a solo business",
    note     = "Unlimited invoicing on the free plan. Bank sync automation is paid",
)

card_grid(c, [
    ("#ef4444", "ZB", "Zoho Books",    "For freelancers already on Zoho tools", logo_path("zoho-books.png")),
    ("#3b82f6", "IN", "Invoice Ninja", "Project billing for a small client list", logo_path("invoice-ninja.png")),
    ("#8b5cf6", "Gn", "GnuCash",       "Free desktop accounting for offline users", logo_path("gnucash.png")),
    ("#22c55e", "QB", "QuickBooks",    "Keep it for payroll, inventory, or staff", logo_path("quickbooks.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free QuickBooks alternatives in 2026",
    subtitle = "Wave  ·  Zoho Books  ·  Invoice Ninja  ·  GnuCash",
)

c.save("quickbooks-alternatives.webp")
