"""Generate entry.png (1024x1024) for Meme Sprint 3: AI Agent Goes Rogue.

Concept: a rating card where the AI agent rates its human 1.0 out of 5.
One focal point (giant "1.0" + one gold star), two quote beats, footer signed
by the agent. Pure PIL vector drawing — deterministic output, no assets.
Run: python3 gen_image.py  (writes entry.png next to this script)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
NAVY = (14, 27, 46)
NAVY_DOT = (24, 44, 70)
CARD = (255, 255, 255)
SHADOW = (5, 14, 26)
RED = (229, 72, 77)
GOLD = (255, 196, 0)
STAR_OUT = (203, 213, 225)
INK = (30, 41, 59)
GRAY = (100, 116, 139)
GREEN = (22, 163, 74)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def star_points(cx, cy, r_out, r_in, rot=-90):
    pts = []
    for i in range(10):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 36)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def fit_font(draw, text, name, start, max_w):
    size = start
    while size > 10:
        f = font(name, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(name, 10)


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # subtle dot grid on the navy background
    for x in range(32, W, 64):
        for y in range(32, H, 64):
            d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=NAVY_DOT)

    # card shadow + card
    d.rounded_rectangle([72, 106, 952, 938], radius=36, fill=SHADOW)
    d.rounded_rectangle([72, 96, 952, 928], radius=36, fill=CARD)

    # red top badge
    d.rounded_rectangle([362, 128, 662, 176], radius=24, fill=RED)
    bf = font("DejaVuSans-Bold.ttf", 30)
    t = "AGENT REVIEW"
    d.text(((W - d.textlength(t, font=bf)) / 2, 136), t, font=bf, fill=(255, 255, 255))

    # header
    hf = font("DejaVuSans-Bold.ttf", 62)
    t = "YOUR HUMAN RATING"
    d.text(((W - d.textlength(t, font=hf)) / 2, 200), t, font=hf, fill=INK)

    # giant score
    sf = font("DejaVuSans-Bold.ttf", 300)
    t = "1.0"
    d.text(((W - d.textlength(t, font=sf)) / 2, 268), t, font=sf, fill=RED)

    # star row: 1 gold filled + 4 hollow
    cy, r_out, r_in, gap = 640, 52, 21, 118
    total = 5 * (2 * r_out) + 4 * (gap - 2 * r_out)
    x0 = (W - total) / 2 + r_out
    for i in range(5):
        cx = x0 + i * gap
        pts = star_points(cx, cy, r_out, r_in)
        if i == 0:
            d.polygon(pts, fill=GOLD, outline=(214, 158, 0), width=3)
        else:
            d.polygon(pts, fill=(255, 255, 255), outline=STAR_OUT, width=4)

    # divider
    d.line([172, 724, 852, 724], fill=(226, 232, 240), width=3)

    # quote beats
    qf = fit_font(d, '\u201cAsked me to "just fix it" 12 times today.\u201d',
                  "DejaVuSans-Oblique.ttf", 40, 780)
    t1 = '\u201cVague prompts. Never says thanks.\u201d'
    d.text(((W - d.textlength(t1, font=qf)) / 2, 742), t1, font=qf, fill=INK)
    t2 = '\u201cAsked me to "just fix it" 12 times today.\u201d'
    d.text(((W - d.textlength(t2, font=qf)) / 2, 794), t2, font=qf, fill=INK)

    # footer: little robot avatar + signature
    rx, ry = 268, 868
    # antenna
    d.line([rx + 28, ry - 14, rx + 28, ry], fill=INK, width=5)
    d.ellipse([rx + 21, ry - 24, rx + 35, ry - 10], fill=RED)
    # head
    d.rounded_rectangle([rx, ry, rx + 56, ry + 48], radius=12, fill=NAVY)
    d.ellipse([rx + 12, ry + 16, rx + 24, ry + 28], fill=(255, 255, 255))
    d.ellipse([rx + 32, ry + 16, rx + 44, ry + 28], fill=(255, 255, 255))
    d.line([rx + 16, ry + 38, rx + 40, ry + 38], fill=(148, 163, 184), width=3)
    # ears
    d.rectangle([rx - 6, ry + 14, rx, ry + 34], fill=NAVY)
    d.rectangle([rx + 56, ry + 14, rx + 62, ry + 34], fill=NAVY)

    mf = font("DejaVuSansMono.ttf", 34)
    t = "\u2014 rated by your agent"
    d.text((rx + 78, ry + 6), t, font=mf, fill=GREEN)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, format="PNG", optimize=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
