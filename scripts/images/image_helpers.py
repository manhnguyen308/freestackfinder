"""
Shared layout helpers for FreeStackFinder feature image generators.

All generator scripts in this folder import from here to guarantee
consistent layout, font loading, and safe text rendering across images.
"""
import os
from PIL import ImageFont

# ── Canvas & brand ─────────────────────────────────────────────────────────────
W, H      = 1200, 630
BG        = "#101116"
CARD_BG   = "#1a1d27"
WIN_BG    = "#13161f"
TEXT_W    = "#ffffff"
TEXT_DIM  = "#8a8fa8"

# ── Layout zones ───────────────────────────────────────────────────────────────
LEFT_W    = 480
RIGHT_X   = LEFT_W + 20       # 500
RIGHT_W   = W - RIGHT_X - 20  # 680
BOT_H     = 90
CONTENT_H = H - BOT_H         # 540

# Right panel fixed positions
FEAT_X = RIGHT_X
FEAT_Y = 20
FEAT_W = RIGHT_W
FEAT_H = 160
GRID_Y = FEAT_Y + FEAT_H + 16  # 196
CELL_W = (RIGHT_W - 12) // 2   # 334
CELL_H = 90
BAR_Y  = CONTENT_H              # 540

# Minimum inner padding so text never butts against a card edge
INNER_PAD = 14


# ── Font loader ────────────────────────────────────────────────────────────────
def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
            else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arialbd.ttf"  if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


# ── Text measurement ───────────────────────────────────────────────────────────
def measure_w(draw, text, fnt):
    bb = draw.textbbox((0, 0), text, font=fnt)
    return bb[2] - bb[0]

def measure_h(draw, text, fnt):
    bb = draw.textbbox((0, 0), text, font=fnt)
    return bb[3] - bb[1]


# ── Safe text helpers ──────────────────────────────────────────────────────────
def truncate(draw, text, fnt, max_w, suffix="…"):
    """Return text shortened with suffix so it fits within max_w pixels."""
    if measure_w(draw, text, fnt) <= max_w:
        return text
    while text:
        candidate = text.rstrip() + suffix
        if measure_w(draw, candidate, fnt) <= max_w:
            return candidate
        text = text[:-1]
    return suffix


def wrap(draw, text, fnt, max_w):
    """Split text into a list of lines that each fit within max_w pixels."""
    words = text.split()
    lines, buf = [], []
    for word in words:
        test = " ".join(buf + [word])
        if measure_w(draw, test, fnt) <= max_w:
            buf.append(word)
        else:
            if buf:
                lines.append(" ".join(buf))
            buf = [word]
    if buf:
        lines.append(" ".join(buf))
    return lines or [text]


def draw_text_wrapped(draw, text, fnt, x, y, max_w, fill, line_gap=5):
    """Draw word-wrapped text. Returns the y position after the final line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, fill=fill, font=fnt)
        y += measure_h(draw, "Ay", fnt) + line_gap
    return y


# ── Shape helpers ──────────────────────────────────────────────────────────────
def rrect(draw, x0, y0, x1, y1, r, color):
    """Draw a filled rounded rectangle."""
    draw.rectangle([x0 + r, y0, x1 - r, y1], fill=color)
    draw.rectangle([x0, y0 + r, x1, y1 - r], fill=color)
    for cx, cy in [(x0+r, y0+r), (x1-r, y0+r), (x0+r, y1-r), (x1-r, y1-r)]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def draw_circle(draw, cx, cy, r, color, text="", text_color="#ffffff", fnt=None):
    """Draw a filled circle with centred initials text."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    if text and fnt:
        bb = draw.textbbox((0, 0), text, font=fnt)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        draw.text((cx - tw // 2, cy - th // 2), text, fill=text_color, font=fnt)


# ── Reusable panel sections ────────────────────────────────────────────────────
def draw_chrome(draw, title_text):
    """macOS-style window chrome (three dots + title bar text)."""
    chrome_y = 18
    for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        draw.ellipse([16 + i*22 - 6, chrome_y - 6,
                      16 + i*22 + 6, chrome_y + 6], fill=col)
    safe = truncate(draw, title_text, font(12), LEFT_W - 100)
    draw.text((80, chrome_y - 7), safe, fill=TEXT_DIM, font=font(12))


def draw_featured_card(draw, accent,
                        initials, name, tagline,
                        line1, line2,
                        badge, license_note):
    """Right-panel featured (hero) card."""
    x, y, w, h = FEAT_X, FEAT_Y, FEAT_W, FEAT_H
    rrect(draw, x, y, x + w, y + h, 10, CARD_BG)
    draw.rectangle([x, y + 10, x + 4, y + h - 10], fill=accent)

    draw_circle(draw, x + 44, y + 50, 28, accent,
                initials[:2], "#000000", font(18, bold=True))

    tx    = x + 84
    avail = w - 84 - INNER_PAD

    draw.text((tx, y + 20),
              truncate(draw, name, font(20, bold=True), avail),
              fill=TEXT_W, font=font(20, bold=True))
    draw.text((tx, y + 48),
              truncate(draw, tagline, font(13), avail),
              fill=accent, font=font(13))
    draw.text((tx, y + 68),
              truncate(draw, line1, font(11), avail),
              fill=TEXT_DIM, font=font(11))
    draw.text((tx, y + 84),
              truncate(draw, line2, font(11), avail),
              fill=TEXT_DIM, font=font(11))

    draw.text((x + 14, y + 110),
              truncate(draw, badge, font(12, bold=True), w - 28),
              fill=accent, font=font(12, bold=True))
    draw.text((x + 14, y + 132),
              truncate(draw, license_note, font(10), w - 28),
              fill=TEXT_DIM, font=font(10))


def draw_grid(draw, accent, tools):
    """2×2 comparison grid below the featured card.

    tools — list of (hex_color, initials_str, name_str, subtitle_str)
    """
    for i, (col, initials, name, sub) in enumerate(tools):
        col_off = i % 2
        row_off = i // 2
        cx = FEAT_X + col_off * (CELL_W + 12)
        cy = GRID_Y + row_off * (CELL_H + 12)

        rrect(draw, cx, cy, cx + CELL_W, cy + CELL_H, 8, CARD_BG)
        draw_circle(draw, cx + 32, cy + CELL_H // 2, 22, col,
                    initials[:2], "#ffffff", font(11, bold=True))

        tx    = cx + 64
        avail = CELL_W - 64 - INNER_PAD
        draw.text((tx, cy + 14),
                  truncate(draw, name, font(13, bold=True), avail),
                  fill=TEXT_W, font=font(13, bold=True))
        draw.text((tx, cy + 36),
                  truncate(draw, sub, font(10), avail),
                  fill=TEXT_DIM, font=font(10))


def draw_bar(draw, accent, title, subtitle):
    """Bottom accent bar: site badge, article title, tools line."""
    draw.rectangle([0, BAR_Y, W, H], fill=accent)
    max_w = W - 56

    draw.text((28, BAR_Y + 10),
              "FreeStackFinder.com",
              fill="#000000", font=font(12, bold=True))
    draw.text((28, BAR_Y + 30),
              truncate(draw, title, font(20, bold=True), max_w),
              fill="#000000", font=font(20, bold=True))
    draw.text((28, BAR_Y + 60),
              truncate(draw, subtitle, font(12), max_w),
              fill="#000000", font=font(12))


# ── Output path helper ─────────────────────────────────────────────────────────
def img_out(filename):
    """Resolve absolute path to static/img/<filename> from anywhere in the repo."""
    here    = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.normpath(os.path.join(here, "..", "..", "static", "img"))
    os.makedirs(img_dir, exist_ok=True)
    return os.path.join(img_dir, filename)
