from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
BG = "#101116"
ACCENT = "#6366f1"  # Productivity silo

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Bottom bar
draw.rectangle([(0, H - 80), (W, H)], fill=ACCENT)
try:
    font_title = ImageFont.truetype("arialbd.ttf", 28)
    font_body  = ImageFont.truetype("arial.ttf",   22)
    font_small = ImageFont.truetype("arial.ttf",   18)
    font_init  = ImageFont.truetype("arialbd.ttf", 22)
except:
    font_title = font_body = font_small = font_init = ImageFont.load_default()

draw.text((30, H - 54), "Best Free Note-Taking Apps in 2026 — FreeStackFinder", font=font_title, fill="white")

# Left panel — mock UI lines
panel_x = 30
for i, line in enumerate(["## Quick capture", "- Google Keep", "- Apple Notes", "- Standard Notes", "- Simplenote", "- Notion free"]):
    col = "#a5b4fc" if line.startswith("##") else "#6b7280"
    draw.text((panel_x, 50 + i * 38), line, font=font_body, fill=col)

# Right panel — featured card + comparison cards
def card(x, y, w, h, label, initials, color):
    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=12, fill="#1e1f2e")
    cx, cy = x + 38, y + h // 2
    draw.ellipse([(cx - 22, cy - 22), (cx + 22, cy + 22)], fill=color)
    draw.text((cx - 10, cy - 12), initials, font=font_init, fill="white")
    draw.text((x + 70, y + h // 2 - 12), label, font=font_body, fill="#e5e7eb")

# Featured card
card(480, 40, 340, 90, "Google Keep — quick capture", "GK", "#34a853")

# 2x2 grid
card(480, 150, 160, 80, "Apple Notes", "AN", "#6366f1")
card(655, 150, 160, 80, "Standard Notes", "SN", "#8b5cf6")
card(480, 245, 160, 80, "Simplenote", "Si", "#3b82f6")
card(655, 245, 160, 80, "Notion Free", "No", "#10b981")

# Silo label
draw.text((480, 345), "Productivity", font=font_small, fill="#6366f1")

out = os.path.join(os.path.dirname(__file__), "static", "img", "free-note-taking-apps.jpg")
img.save(out, "JPEG", quality=92)
print(f"Saved → {out}")
