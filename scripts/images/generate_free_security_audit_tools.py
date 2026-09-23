#!/usr/bin/env python3
"""
Feature image generator: Free security audit tools in 2026
Output : static/img/free-security-audit-tools.webp  (1200x630 px)
Silo   : Security   Accent: #8b5cf6

Audit targets come from content/security/free-security-audit-tools.md,
which closes with "Run browser checks first, then scoped scans".
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, INFO, WARN,
    panel_list, card_featured, card_grid, card_bar,
)

ACCENT = "#8b5cf6"   # Security silo, violet

c = Canvas()

panel_list(c, "Pick the tool by audit target", [
    ("#22c55e", "SSL Labs, SecurityHeaders", "TLS and header checks",       "Website",    INFO),
    ("#3b82f6", "OWASP ZAP",                 "Web application scanning",    "Web app",    INFO),
    ("#06b6d4", "Nikto",                     "Quick web server scan",       "Web server", INFO),
    ("#ec4899", "Nmap",                      "Network and port discovery",  "Network",    INFO),
    ("#eab308", "Lynis",                     "Linux and Unix hardening",    "Host",       INFO),
    ("#ef4444", "Greenbone CE",              "Multi-host vulnerability scans", "Advanced", WARN),
])

card_featured(
    c, ACCENT,
    initials = "SL",
    name     = "SSL Labs and SecurityHeaders",
    tagline  = "Run browser checks first",
    note     = "Free website checks for TLS and security headers before any scoped scan",
)

card_grid(c, [
    ("#3b82f6", "ZP", "OWASP ZAP",    "Web application scanning, no feature cap"),
    ("#ec4899", "Nm", "Nmap",         "Network and port discovery, open source"),
    ("#eab308", "Ly", "Lynis",        "Local audit for Linux and Unix hardening"),
    ("#ef4444", "GB", "Greenbone CE", "Structured scanning across several hosts"),
])

card_bar(
    c, ACCENT,
    title    = "Free security audit tools in 2026",
    subtitle = "OWASP ZAP  ·  Nmap  ·  Lynis  ·  Nikto  ·  Greenbone  ·  SSL Labs",
)

c.save("free-security-audit-tools.webp")
