#!/usr/bin/env python3
"""
Feature image generator: Free website builders in 2026
Output : static/img/free-website-builders.webp  (1200x630 px)
Silo   : Business   Accent: #10b981

Free-plan boundaries come from content/business/free-website-builders.md.
Canva's affiliate program is under review: the image carries no call to action.
Product icons come from scripts/images/logos/ (sources in logos/SOURCES.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, WARN,
    panel_list, card_featured, card_grid, card_bar, logo_path,
)

ACCENT = "#10b981"   # Business silo, emerald

c = Canvas()

panel_list(c, "Where each free plan stops", [
    ("#3b82f6", "Wix",            "800+ templates and apps",      "Wix banner",     WARN),
    ("#22c55e", "Google Sites",   "Multi-page, no builder ads",   "Basic design",   WARN),
    ("#06b6d4", "WordPress.com",  "Blogs and content sites",      "Ads, no plugins", WARN),
    ("#8b5cf6", "Carrd",          "Clean one-page sites",         "No custom domain", WARN),
    ("#ec4899", "Canva Websites", "Design-first creators",        "Domain on Pro",  WARN),
], section="Best for and paid boundary")

card_featured(
    c, ACCENT,
    initials = "Wx",
    logo     = logo_path("wix.png"),
    name     = "Wix",
    tagline  = "Most features on a free plan",
    note     = "Drag-and-drop editor and 800+ templates, on a Wix subdomain with a banner",
)

card_grid(c, [
    ("#22c55e", "GS", "Google Sites",   "Multi-page sites with no builder ads", logo_path("google-sites.png")),
    ("#06b6d4", "WP", "WordPress.com",  "Blogs with unlimited posts on a subdomain", logo_path("wordpress.png")),
    ("#8b5cf6", "Ca", "Carrd",          "Up to 3 one-page sites on carrd.co", logo_path("carrd.png")),
    ("#ec4899", "Cv", "Canva Websites", "Custom domains require Pro", logo_path("canva.png")),
])

card_bar(
    c, ACCENT,
    title    = "Free website builders in 2026",
    subtitle = "Wix  ·  Google Sites  ·  WordPress.com  ·  Carrd  ·  Canva Websites",
)

c.save("free-website-builders.webp")
