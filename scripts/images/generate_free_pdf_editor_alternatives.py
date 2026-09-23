#!/usr/bin/env python3
"""
Feature image generator: Free PDF editors in 2026
Output : static/img/free-pdf-editor-alternatives.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

Task-to-tool mapping and free limits come from
content/productivity/free-pdf-editor-alternatives.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, panel_list, card_featured, card_grid, card_bar,
)

ACCENT = "#6366f1"   # Productivity silo, indigo

c = Canvas()

panel_list(c, "Pick the tool by the edit", [
    ("#6366f1", "Edit PDF text",          "PDFgear or Sejda",               None, None),
    ("#22c55e", "Annotate and comment",   "Xodo or PDFgear",                None, None),
    ("#3b82f6", "Fill and sign forms",    "PDFgear, Xodo, or Sejda",        None, None),
    ("#eab308", "Merge, split, compress", "PDF24 Tools or PDFgear",         None, None),
    ("#ec4899", "Edit offline, no account", "LibreOffice Draw or PDFgear",  None, None),
], section="Task and best free tool")

card_featured(
    c, ACCENT,
    initials = "PG",
    name     = "PDFgear",
    tagline  = "Best free desktop PDF editor",
    note     = "Text and layout edits with no watermark or page cap",
)

card_grid(c, [
    ("#eab308", "24", "PDF24 Tools",      "Browser toolkit, no account required"),
    ("#3b82f6", "Sj", "Sejda",            "3 tasks an hour, 200 pages per file"),
    ("#22c55e", "LD", "LibreOffice Draw", "Offline editing for LibreOffice users"),
    ("#ec4899", "Xo", "Xodo",             "Annotation and signing on mobile"),
])

card_bar(
    c, ACCENT,
    title    = "Free PDF editors in 2026",
    subtitle = "PDFgear  ·  PDF24 Tools  ·  Sejda  ·  LibreOffice Draw  ·  Xodo",
)

c.save("free-pdf-editor-alternatives.webp")
