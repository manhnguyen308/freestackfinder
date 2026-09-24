#!/usr/bin/env python3
"""
Feature image generator: Free backup software in 2026
Output : static/img/free-backup-software.webp  (1200x630 px)
Silo   : Cloud   Accent: #06b6d4

The three-layer plan and tool limits come from
content/cloud/free-backup-software.md.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, INFO,
    panel_list, note_card, card_featured, card_grid, card_bar, logo_path,
)

ACCENT = "#06b6d4"   # Cloud silo, cyan

c = Canvas()

x0, y0, x1, y1 = panel_list(c, "A three-layer starting point", [
    ("#3b82f6", "Offsite copy",               "Google Drive or iCloud for active files", "Layer 1", INFO),
    ("#22c55e", "Scheduled encrypted backup", "Duplicati to another destination",        "Layer 2", INFO),
    ("#eab308", "Local external drive",       "A faster restore path",                   "Layer 3", INFO),
], section="Each layer covers a different failure")

note_card(c, ACCENT, x0, y0 + 28 + 3 * 62 + 6, x1, y1, "Before relying on it",
          "Test a restore from the scheduled job")

card_featured(
    c, ACCENT,
    initials = "Du",
    logo     = logo_path("duplicati.png"),
    name     = "Duplicati",
    tagline  = "Best free scheduled encrypted backup",
    note     = "Real backup software, with more setup and a rougher restore workflow",
)

card_grid(c, [
    ("#3b82f6", "GD", "Google Drive",  "Offsite copy for documents. Sync is not backup", logo_path("google-drive.png")),
    ("#ef4444", "BB", "Backblaze",     "Paid unlimited backup for large datasets", logo_path("backblaze.png")),
    ("#64748b", "iC", "iCloud Backup", "Built in for Apple users, 5GB free", logo_path("icloud.png")),
    ("#8b5cf6", "Dc", "Duplicacy",     "Self-managed backup for NAS and power users", logo_path("duplicacy.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free backup software in 2026",
    subtitle = "Duplicati  ·  Google Drive  ·  iCloud  ·  Duplicacy  ·  Backblaze",
)

c.save("free-backup-software.webp")
