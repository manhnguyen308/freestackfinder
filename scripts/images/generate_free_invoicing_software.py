#!/usr/bin/env python3
"""
Feature image generator: Free invoicing software in 2026
Output : static/img/free-invoicing-software.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Free-plan limits and fees come from content/business/free-invoicing-software.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, GOOD, WARN,
    panel_list, card_featured, card_grid, card_bar, logo_path,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

panel_list(c, "Invoicing routes and their limit", [
    ("#10b981", "Wave",             "Invoices feed a free ledger",     "Unlimited",  GOOD),
    ("#ef4444", "Zoho Invoice",     "Client portal and reminders",     "500 a year", WARN),
    ("#3b82f6", "Invoice Ninja",    "Project and hourly billing",      "5 clients",  WARN),
    ("#64748b", "Square Invoices",  "Card payments for service work",  "Unlimited",  GOOD),
    ("#06b6d4", "PayPal Invoicing", "Clients who already use PayPal",  "Fees vary",  WARN),
    ("#8b5cf6", "Stripe Invoicing", "API-driven billing",              "0.4% fee",   WARN),
])

card_featured(
    c, ACCENT,
    initials = "Wa",
    logo     = logo_path("wave.png"),
    name     = "Wave",
    tagline  = "Best overall free invoicing",
    note     = "Unlimited invoices tied to free bookkeeping. Automation and receipts are paid",
)

card_grid(c, [
    ("#ef4444", "ZI", "Zoho Invoice",     "Client portal, 2 users, 500 invoices a year", logo_path("zoho-invoice.png")),
    ("#3b82f6", "IN", "Invoice Ninja",    "Project billing for up to 5 hosted clients", logo_path("invoice-ninja.png")),
    ("#64748b", "Sq", "Square Invoices",  "Service businesses taking card payments", logo_path("square.png")),
    ("#8b5cf6", "St", "Stripe Invoicing", "0.4% per paid Starter invoice, plus processing", logo_path("stripe.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free invoicing software in 2026",
    subtitle = "Wave  ·  Zoho Invoice  ·  Invoice Ninja  ·  Square  ·  PayPal  ·  Stripe",
)

c.save("free-invoicing-software.webp")
