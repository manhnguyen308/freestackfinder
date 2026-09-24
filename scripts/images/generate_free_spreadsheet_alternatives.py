#!/usr/bin/env python3
"""
Feature image generator: Free spreadsheet alternatives in 2026
Output : static/img/free-spreadsheet-alternatives.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Offline and collaboration values come from the comparison table in
content/business/free-spreadsheet-alternatives.md.
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

panel_table(c, ACCENT, "Offline use and collaboration",
    ["Tool", "Offline", "Collaboration"],
    [
        ("Google Sheets",    [("Limited", WARN),     ("Real-time", GOOD)]),
        ("LibreOffice Calc", [("Full", GOOD),        ("No", BAD)]),
        ("Zoho Sheet",       [("No", BAD),           ("Real-time", GOOD)]),
        ("ONLYOFFICE",       [("Desktop app", WARN), ("Real-time", GOOD)]),
        ("Airtable",         [("No", BAD),           ("Real-time", GOOD)]),
    ])

card_featured(
    c, ACCENT,
    initials = "GS",
    logo     = logo_path("google-sheets.png"),
    name     = "Google Sheets",
    tagline  = "Best overall for most users",
    note     = "Real-time browser collaboration with good Excel compatibility",
)

card_grid(c, [
    ("#22c55e", "LC", "LibreOffice Calc", "Offline desktop with strong Excel support", logo_path("libreoffice-calc.png")),
    ("#ef4444", "ZS", "Zoho Sheet",       "For businesses already using Zoho", logo_path("zoho-sheet.png")),
    ("#3b82f6", "OO", "ONLYOFFICE Docs",  "The closest Excel format fidelity", logo_path("onlyoffice.png")),
    ("#eab308", "At", "Airtable",         "Spreadsheet and database hybrid", logo_path("airtable.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free spreadsheet alternatives in 2026",
    subtitle = "Google Sheets  ·  LibreOffice Calc  ·  Zoho Sheet  ·  ONLYOFFICE  ·  Airtable",
)

c.save("free-spreadsheet-alternatives.webp")
