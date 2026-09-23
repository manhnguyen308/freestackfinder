#!/usr/bin/env python3
"""
Feature image generator: Free resume builders in 2026
Output : static/img/free-resume-builders.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

The situation-to-tool mapping comes from content/business/free-resume-builders.md.
Canva's affiliate program is under review: the image carries no call to action.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, panel_list, card_featured, card_grid, card_bar,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

panel_list(c, "Match the builder to the application", [
    ("#3b82f6", "Large corporate employer", "Google Docs, clean ATS format", None, None),
    ("#ec4899", "Creative or startup role",  "Canva, for layout control",     None, None),
    ("#06b6d4", "Active Indeed applicant",   "Indeed Resume Builder",         None, None),
    ("#eab308", "First resume or return to work", "Resume.com, guided prompts", None, None),
    ("#8b5cf6", "Word-compatible output",    "Google Docs or Word Online",    None, None),
], section="Situation and best tool")

card_featured(
    c, ACCENT,
    initials = "Ca",
    name     = "Canva",
    tagline  = "Best free resume builder for most people",
    note     = "Free PDF and PNG downloads. Designed layouts can reduce ATS parsing accuracy",
)

card_grid(c, [
    ("#3b82f6", "GD", "Google Docs",  "ATS-friendly resumes with full control"),
    ("#06b6d4", "In", "Indeed",       "Build and apply directly on Indeed"),
    ("#eab308", "Re", "Resume.com",   "Guided builder with a free download"),
    ("#ef4444", "!",  "Paid exports", "Some builders charge for the final download"),
])

card_bar(
    c, ACCENT,
    title    = "Free resume builders in 2026 with PDF downloads",
    subtitle = "Canva  ·  Google Docs  ·  Indeed Resume Builder  ·  Resume.com",
)

c.save("free-resume-builders.webp")
