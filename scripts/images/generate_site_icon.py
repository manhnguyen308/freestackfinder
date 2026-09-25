#!/usr/bin/env python3
"""
Site icon generator: the stacked F
Outputs: static/favicon.ico (16, 32, 48), favicon-16x16.png, favicon-32x32.png,
         favicon-96x96.png, apple-touch-icon.png, android-chrome-192x192.png,
         android-chrome-512x512.png

An F built from three separate blocks, for the "stack" in FreeStackFinder:
a white stem, a white top arm, and a light teal middle arm on a brand teal
tile (--primary in docs/DESIGN-SYSTEM.md).

Every size is drawn on its own pixel grid and box-reduced from 4x, so edges
land on whole pixels and the 16px tab icon stays sharp. The Apple touch icon
is a full square because iOS applies its own corner mask.
"""
import os
from PIL import Image, ImageDraw

STATIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "static")
TEAL = "#0F766E"        # --primary
TEAL_LIGHT = "#5EEAD4"  # middle arm
WHITE = "#FFFFFF"
SS = 4                  # supersampling factor

# Blocks as (x0, y0, x1, y1, colour) on a 0..1 grid
BLOCKS = [
    (.25, .22, .41, .78, WHITE),       # stem
    (.47, .22, .78, .37, WHITE),       # top arm
    (.47, .44, .69, .58, TEAL_LIGHT),  # middle arm
]


def draw_icon(n, rounded=True):
    """The icon at n x n pixels. rounded=False gives a full square tile."""
    im = Image.new("RGBA", (n * SS, n * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    tile_r = round(n * SS * .22) if rounded else 0
    d.rounded_rectangle([0, 0, n * SS - 1, n * SS - 1], radius=tile_r, fill=TEAL)
    snap = lambda v: round(v * n) * SS
    # square blocks below 48px: a 1px rounding only blurs the corners there
    block_r = round(n * .035) * SS if n >= 48 else 0
    for x0, y0, x1, y1, col in BLOCKS:
        d.rounded_rectangle([snap(x0), snap(y0), snap(x1) - 1, snap(y1) - 1],
                            radius=block_r, fill=col)
    return im.reduce(SS)


def save(im, name, **kw):
    path = os.path.join(STATIC, name)
    im.save(path, **kw)
    print(f"  {name:<28} {im.size[0]}x{im.size[1]}  {os.path.getsize(path) / 1024:.1f} KB")


if __name__ == "__main__":
    for n in (16, 32, 96):
        save(draw_icon(n), f"favicon-{n}x{n}.png", optimize=True)
    for n in (192, 512):
        save(draw_icon(n), f"android-chrome-{n}x{n}.png", optimize=True)
    save(draw_icon(180, rounded=False).convert("RGB"), "apple-touch-icon.png", optimize=True)
    # favicon.ico carries hand-drawn 16, 32, and 48px frames rather than resized copies
    frames = {n: draw_icon(n) for n in (16, 32, 48)}
    save(frames[48], "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)],
         append_images=[frames[16], frames[32]])
