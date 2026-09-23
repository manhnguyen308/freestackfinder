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


# ══════════════════════════════════════════════════════════════════════════════
# Card-legible layout
#
# The layout above uses 10 to 13 px text, which shrinks to 3 or 4 px when the
# image is shown as a ~350 px wide article card. The helpers below keep the same
# visual language (dark UI panel, featured card, 2x2 grid, accent bar) with
# larger type, fewer lines, and a 56 px safe margin on every side.
#
# Drawing happens at SS times the final size and is downsampled, so circles,
# rounded corners, and text edges come out anti-aliased.
# ══════════════════════════════════════════════════════════════════════════════
from PIL import Image, ImageDraw

SS       = 2                  # supersampling factor
M        = 56                 # outer safe margin
TOP      = 40
BAR2_Y   = 486                # accent bar top

WIN_X0, WIN_Y0, WIN_X1, WIN_Y1 = M, TOP, 560, 446
RX0, RX1 = 592, W - M         # right column, 552 wide
FEAT2_Y0, FEAT2_Y1 = TOP, 190
CELL2_W  = (RX1 - RX0 - 16) // 2   # 268
CELL2_H  = 112
GRID2_Y  = 206

LINE     = "#262a38"          # hairlines and dividers
TEXT_MID = "#b4b9cc"
GOOD     = "#22c55e"
WARN     = "#eab308"
BAD      = "#ef4444"
NEUTRAL  = "#8a8fa8"
INFO     = "#60a5fa"
INK      = "#101116"          # text on the accent bar


def ui_font(size, weight="regular"):
    """Segoe UI when available (regular, semibold, bold), else the font() fallback."""
    files = {
        "regular":  "C:/Windows/Fonts/segoeui.ttf",
        "semibold": "C:/Windows/Fonts/seguisb.ttf",
        "bold":     "C:/Windows/Fonts/segoeuib.ttf",
    }
    p = files.get(weight, files["regular"])
    if os.path.exists(p):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return font(size, bold=(weight != "regular"))


class Canvas:
    """1200x630 surface. All coordinates and sizes are given at final scale."""

    def __init__(self, bg=BG):
        self.img  = Image.new("RGB", (W * SS, H * SS), bg)
        self.draw = ImageDraw.Draw(self.img)

    def _f(self, size, weight):
        return ui_font(int(round(size * SS)), weight)

    def rect(self, x0, y0, x1, y1, fill, r=0, outline=None, width=1):
        box = [x0 * SS, y0 * SS, x1 * SS, y1 * SS]
        if r:
            self.draw.rounded_rectangle(box, r * SS, fill=fill,
                                        outline=outline, width=width * SS)
        else:
            self.draw.rectangle(box, fill=fill, outline=outline, width=width * SS)

    def circle(self, cx, cy, r, fill, outline=None, width=1):
        self.draw.ellipse([(cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS],
                          fill=fill, outline=outline, width=width * SS)

    def line(self, pts, fill, width=1):
        self.draw.line([(x * SS, y * SS) for x, y in pts], fill=fill, width=width * SS)

    def poly(self, pts, fill):
        self.draw.polygon([(x * SS, y * SS) for x, y in pts], fill=fill)

    def text_w(self, text, size, weight="regular"):
        bb = self.draw.textbbox((0, 0), text, font=self._f(size, weight))
        return (bb[2] - bb[0]) / SS

    def text(self, x, y, text, size, fill, weight="regular", anchor="la"):
        self.draw.text((x * SS, y * SS), text, fill=fill,
                       font=self._f(size, weight), anchor=anchor)

    def fit_size(self, text, size, max_w, weight="regular", min_size=11):
        """Largest size <= size at which text fits max_w."""
        while size > min_size and self.text_w(text, size, weight) > max_w:
            size -= 0.5
        return size

    def fit_text(self, x, y, text, size, max_w, fill, weight="regular", anchor="la"):
        """Draw text shrunk to fit max_w. Returns the size used."""
        s = self.fit_size(text, size, max_w, weight)
        self.text(x, y, text, s, fill, weight, anchor)
        return s

    def wrap(self, text, size, max_w, weight="regular"):
        lines, buf = [], []
        for word in text.split():
            test = " ".join(buf + [word])
            if not buf or self.text_w(test, size, weight) <= max_w:
                buf.append(word)
            else:
                lines.append(" ".join(buf))
                buf = [word]
        if buf:
            lines.append(" ".join(buf))
        return lines

    def para(self, x, y, text, size, max_w, fill, weight="regular",
             max_lines=2, leading=1.3):
        """Wrapped text, shrunk until it fits in max_lines. Returns the next y."""
        while size > 11 and (
                len(self.wrap(text, size, max_w, weight)) > max_lines
                or any(self.text_w(ln, size, weight) > max_w
                       for ln in self.wrap(text, size, max_w, weight))):
            size -= 0.5
        for ln in self.wrap(text, size, max_w, weight):
            self.text(x, y, ln, size, fill, weight)
            y += size * leading
        return y

    def pill(self, x, y, text, size, fg, bg, pad_x=10, h=None, anchor="left"):
        """Rounded label. anchor='right' puts the right edge at x. Returns width."""
        w = self.text_w(text, size, "semibold") + pad_x * 2
        h = h or size * 1.9
        x0 = x - w if anchor == "right" else x
        self.rect(x0, y, x0 + w, y + h, bg, r=h / 2)
        self.text(x0 + w / 2, y + h / 2, text, size, fg, "semibold", anchor="mm")
        return w

    def save(self, filename, quality=86):
        out = img_out(filename)
        small = self.img.resize((W, H), Image.LANCZOS)
        small.save(out, "WEBP", quality=quality, method=6)
        print(f"Saved: {out} ({os.path.getsize(out) / 1024:.1f} KB)")
        return out


def mix(hex_a, hex_b, t):
    """Blend two #rrggbb colours; t=0 gives a, t=1 gives b."""
    a = [int(hex_a[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(hex_b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(a[i] + (b[i] - a[i]) * t):02x}" for i in range(3))


def _lum(hex_c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex_c[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def on_color(bg):
    """INK or white, whichever reads better on bg."""
    return INK if contrast(INK, bg) >= contrast("#ffffff", bg) else "#ffffff"


def accent_text(accent, bg=CARD_BG):
    """Accent lightened just enough to reach 4.5:1 on a dark card."""
    col, t = accent, 0.0
    while contrast(col, bg) < 4.5 and t < 1:
        t += 0.05
        col = mix(accent, "#ffffff", t)
    return col


def initials_badge(c, cx, cy, r, color, initials, text_color="#ffffff"):
    c.circle(cx, cy, r, color)
    c.text(cx, cy, initials, r * 0.72, text_color, "bold", anchor="mm")


def card_window(c, title, x0=WIN_X0, y0=WIN_Y0, x1=WIN_X1, y1=WIN_Y1):
    """Dark app window with traffic-light chrome. Returns the content box."""
    c.rect(x0, y0, x1, y1, WIN_BG, r=14, outline=LINE)
    for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        c.circle(x0 + 24 + i * 20, y0 + 22, 6, col)
    c.fit_text(x0 + 96, y0 + 22, title, 15, x1 - x0 - 116, TEXT_DIM, anchor="lm")
    c.line([(x0 + 1, y0 + 44), (x1 - 1, y0 + 44)], LINE)
    return x0 + 20, y0 + 60, x1 - 20, y1 - 18


def card_featured(c, accent, initials, name, tagline, note):
    x0, y0, x1, y1 = RX0, FEAT2_Y0, RX1, FEAT2_Y1
    c.rect(x0, y0, x1, y1, CARD_BG, r=14, outline=mix(accent, CARD_BG, 0.55))
    c.rect(x0, y0 + 18, x0 + 5, y1 - 18, accent, r=2)
    initials_badge(c, x0 + 60, y0 + 62, 36, accent, initials, on_color(accent))
    tx = x0 + 114
    avail = x1 - tx - 22
    c.fit_text(tx, y0 + 20, name, 30, avail, TEXT_W, "bold")
    c.fit_text(tx, y0 + 64, tagline, 19, avail, accent_text(accent), "semibold")
    c.para(tx, y0 + 96, note, 16, avail, TEXT_MID, max_lines=2)


def card_grid(c, items):
    """items: four (colour, initials, name, note) tuples."""
    for i, (col, initials, name, note) in enumerate(items):
        x = RX0 + (i % 2) * (CELL2_W + 16)
        y = GRID2_Y + (i // 2) * (CELL2_H + 16)
        c.rect(x, y, x + CELL2_W, y + CELL2_H, CARD_BG, r=12)
        initials_badge(c, x + 36, y + 34, 20, col, initials)
        c.fit_text(x + 66, y + 34, name, 20, CELL2_W - 66 - 16, TEXT_W, "bold", anchor="lm")
        c.para(x + 18, y + 60, note, 15, CELL2_W - 36, TEXT_DIM, max_lines=2)


def card_bar(c, accent, title, subtitle):
    fg = on_color(accent)
    c.rect(0, BAR2_Y, W, H, accent)
    c.text(M, BAR2_Y + 18, "FREESTACKFINDER.COM", 14, mix(fg, accent, 0.25), "bold")
    c.fit_text(M, BAR2_Y + 36, title, 40, W - M * 2, fg, "bold")
    c.fit_text(M, BAR2_Y + 96, subtitle, 19, W - M * 2, mix(fg, accent, 0.15), "semibold")


# ── Reusable left panels ──────────────────────────────────────────────────────
def pill_colors(col):
    return col, mix(col, WIN_BG, 0.78)


def panel_table(c, accent, title, headers, rows, first_w=None):
    """Window with a header row and up to six rows of status pills.

    headers — column labels; the first is the row label column.
    rows    — (label, [(text, colour), ...]) with one pill per extra column.
    """
    x0, y0, x1, y1 = card_window(c, title)
    n = len(headers) - 1
    first_w = first_w or (240 if n == 2 else 200 if n == 3 else 260)
    col_w = (x1 - x0 - first_w) / n
    cols = [x0 + first_w + k * col_w for k in range(n)]
    c.fit_text(x0, y0, headers[0].upper(), 13, first_w - 12, TEXT_DIM, "semibold")
    for k, h in enumerate(headers[1:]):
        c.fit_text(cols[k], y0, h.upper(), 13, col_w - 8,
                   accent_text(accent, WIN_BG) if k == n - 1 and h.lower() in ("pro", "paid") else TEXT_DIM,
                   "semibold")
    count = len(rows)
    rh = min(62, (y1 - (y0 + 30)) / count)
    ry = y0 + 30
    for label, cells in rows:
        c.rect(x0, ry, x1, ry + rh - 8, CARD_BG, r=8)
        mid = ry + (rh - 8) / 2
        c.fit_text(x0 + 16, mid, label, 17, first_w - 28, TEXT_W, "semibold", anchor="lm")
        for k, (txt, col) in enumerate(cells):
            fg, bg = pill_colors(col)
            size = c.fit_size(txt, 13, col_w - 28, "semibold")
            c.pill(cols[k] - 2, mid - 13, txt, size, fg, bg, h=26)
        ry += rh
    return x0, y0, x1, y1


def note_card(c, accent, x0, y0, x1, y1, label, text):
    """Card with an accent strip, a small label, and one or two lines of text."""
    c.rect(x0, y0, x1, y1, CARD_BG, r=10)
    c.rect(x0, y0 + 12, x0 + 4, y1 - 12, accent_text(accent), r=2)
    if y1 - y0 >= 80:
        c.text(x0 + 20, y0 + 16, label.upper(), 12, TEXT_DIM, "semibold")
        c.para(x0 + 20, y0 + 38, text, 18, x1 - x0 - 40, TEXT_W, "semibold", max_lines=2)
    else:
        c.fit_text(x0 + 20, (y0 + y1) / 2, text, 17, x1 - x0 - 40, TEXT_W, "semibold", anchor="lm")


def table_bottom(y0, count, y1):
    """y just below the last row panel_table drew."""
    rh = min(62, (y1 - (y0 + 30)) / count)
    return y0 + 30 + rh * count - 8


def panel_list(c, title, rows, section=None):
    """Window with up to six rows: colour strip, name, note, optional pill.

    rows — (colour, name, note, pill_text or None, pill_colour or None)
    """
    x0, y0, x1, y1 = card_window(c, title)
    ry = y0
    if section:
        c.text(x0, y0, section.upper(), 13, TEXT_DIM, "semibold")
        ry = y0 + 28
    count = len(rows)
    rh = min(62, (y1 - ry + 8) / count)
    for col, name, note, ptxt, pcol in rows:
        c.rect(x0, ry, x1, ry + rh - 8, CARD_BG, r=8)
        c.rect(x0, ry + 10, x0 + 4, ry + rh - 18, col, r=2)
        right = x1 - 14
        if ptxt:
            fg, bg = pill_colors(pcol)
            w = c.pill(right, ry + (rh - 8) / 2 - 13, ptxt, 12.5, fg, bg, h=26, anchor="right")
            right -= w + 12
        avail = right - (x0 + 18)
        if note and rh >= 52:
            c.fit_text(x0 + 18, ry + (rh - 8) / 2 - 10, name, 16.5, avail, TEXT_W, "semibold", anchor="lm")
            c.fit_text(x0 + 18, ry + (rh - 8) / 2 + 12, note, 13.5, avail, TEXT_DIM, anchor="lm")
        else:
            c.fit_text(x0 + 18, ry + (rh - 8) / 2, name, 16.5, avail, TEXT_W, "semibold", anchor="lm")
        ry += rh
    return x0, y0, x1, y1
