#!/usr/bin/env python3
"""
Feature image generator: Free Slack alternatives in 2026
Output : static/img/slack-alternatives.webp  (1200x630 px)
Silo   : Productivity   Accent: #6366f1

The 90-day history window and the alternatives come from
content/productivity/slack-alternatives.md. The chat window is a generic
mock-up; its only claim is the 90-day limit the article states.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_helpers import (
    Canvas, CARD_BG, WIN_BG, TEXT_W, TEXT_DIM, TEXT_MID, WARN, LINE,
    card_window, card_featured, card_grid, card_bar, mix, accent_text,
)

ACCENT = "#6366f1"   # Productivity silo, indigo

c = Canvas()

# ── LEFT PANEL: channel list and a message thread with the history notice ─────
x0, y0, x1, y1 = card_window(c, "Team chat: #design")

SIDE_R = x0 + 124
c.text(x0, y0, "CHANNELS", 12, TEXT_DIM, "semibold")
for i, ch in enumerate(["# general", "# design", "# clients", "# random"]):
    cy = y0 + 26 + i * 36
    if i == 1:
        c.rect(x0 - 6, cy - 4, SIDE_R - 10, cy + 26, mix(ACCENT, WIN_BG, 0.7), r=6)
    c.text(x0, cy + 11, ch, 15, TEXT_W if i == 1 else TEXT_MID,
           "semibold" if i == 1 else "regular", anchor="lm")
c.line([(SIDE_R, y0 - 8), (SIDE_R, y1)], LINE)

mx0 = SIDE_R + 16
# History notice (the article's first constraint)
c.rect(mx0, y0 - 4, x1, y0 + 50, mix(WARN, WIN_BG, 0.82), r=8)
c.text(mx0 + 14, y0 + 12, "Slack Free", 13, WARN, "bold", anchor="lm")
c.fit_text(mx0 + 14, y0 + 32, "Only the last 90 days are visible", 14,
           x1 - mx0 - 28, TEXT_W, "semibold", anchor="lm")

msgs = [
    ("#22c55e", 0.85, 0.55),
    ("#ec4899", 0.70, 0.0),
    ("#3b82f6", 0.90, 0.60),
    ("#eab308", 0.60, 0.0),
]
my = y0 + 68
for col, w1, w2 in msgs:
    c.circle(mx0 + 16, my + 16, 16, col)
    span = x1 - (mx0 + 44)
    c.rect(mx0 + 44, my + 2, mx0 + 44 + 80, my + 12, TEXT_MID, r=4)
    c.rect(mx0 + 44, my + 20, mx0 + 44 + span * w1, my + 30, "#3a3f52", r=4)
    if w2:
        c.rect(mx0 + 44, my + 36, mx0 + 44 + span * w2, my + 46, "#3a3f52", r=4)
    my += 64 if w2 else 50

c.rect(mx0, y1 - 38, x1, y1, CARD_BG, r=8)
c.text(mx0 + 14, y1 - 19, "Message #design", 14, TEXT_DIM, anchor="lm")

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
card_featured(
    c, ACCENT,
    initials = "Di",
    name     = "Discord",
    tagline  = "Best for informal teams",
    note     = "Persistent channels and voice rooms without a 90-day window",
)

card_grid(c, [
    ("#3b82f6", "Te", "Teams Free",  "For teams using Microsoft apps"),
    ("#22c55e", "GC", "Google Chat", "For teams already on Google Workspace"),
    ("#06b6d4", "Mm", "Mattermost",  "Self-hosted chat for small groups"),
    ("#ef4444", "RC", "Rocket.Chat", "Limited self-hosted options"),
])

card_bar(
    c, ACCENT,
    title    = "Free Slack alternatives in 2026",
    subtitle = "Discord  ·  Microsoft Teams  ·  Google Chat  ·  Mattermost  ·  Rocket.Chat",
)

c.save("slack-alternatives.webp")
