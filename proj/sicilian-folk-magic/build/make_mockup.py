"""Draw the phone hero mockup (390 x 844 at 2x) from the real cutouts, as a PNG still. Thonny: press Run."""
# ---------------- SETTINGS ----------------
CUT = 'proj/sicilian-folk-magic/art/cut'
OUT = 'proj/sicilian-folk-magic/stills/hero-phone.png'
FONT_DIR = '/tmp/claude-0/-home-user-proofer/cf8f853a-9373-582f-88da-40f1aca907cd/scratchpad/fonts'  # gloock.ttf, literata*.ttf
SCALE = 2
# ------------------------------------------
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
S = SCALE
W, H = 390 * S, 844 * S
TILE, PLASTER, INK, BLUE, RED, GOLD, SOFT = '#efe4c8', '#fcf9f2', '#2a1d16', '#1d4f8a', '#a3171f', '#e3a82f', '#6a5646'

def cut(n): return Image.open(os.path.join(ROOT, CUT, n + '.png')).convert('RGBA')
def font(n, px): return ImageFont.truetype(os.path.join(FONT_DIR, n), px * S)

img = Image.new('RGBA', (W, H), TILE)
# majolica wall, washed back so text stays readable
tile = cut('tile')
tile = tile.resize((tile.width * S // 2, tile.height * S // 2))
wall = Image.new('RGBA', (W, H))
for y in range(0, H, tile.height):
    for x in range(0, W, tile.width):
        wall.paste(tile, (x, y))
wash = Image.new('RGBA', (W, H), (239, 228, 200, 200))
wall.alpha_composite(wash)
img.alpha_composite(wall)

# stage: the gilt frame is the proscenium
frame = cut('frame')
fw = W - 16 * S
fh = int(frame.height * fw / frame.width)
frame = frame.resize((fw, fh), Image.LANCZOS)
fa = np.array(frame.split()[3])
cy, cx = fh // 2, fw // 2
# opening = transparent box around the centre
row = fa[cy]; col = fa[:, cx]
l = cx - np.argmax(row[:cx][::-1] > 0); r = cx + np.argmax(row[cx:] > 0)
t = cy - np.argmax(col[:cy][::-1] > 0); b = cy + np.argmax(col[cy:] > 0)
fx, fy = 8 * S, 10 * S
ox0, oy0, ox1, oy1 = fx + l, fy + t, fx + r, fy + b
stage = Image.new('RGBA', (ox1 - ox0, oy1 - oy0), '#f6ecd6')
sd = ImageDraw.Draw(stage)
sw, sh = stage.size
# backdrop: Houël's car of Rosalia, faded, as a painted flat
flat = cut('float')
flat = flat.resize((sw, int(flat.height * sw / flat.width)), Image.LANCZOS)
flat.putalpha(flat.split()[3].point(lambda v: v * 0.45))
stage.alpha_composite(flat, (0, sh - flat.height - 18 * S))
# luminarie arch
for i in range(19):
    a = np.pi * i / 18
    x = sw / 2 - np.cos(a) * sw * 0.46; y = sh * 0.42 - np.sin(a) * sh * 0.34
    sd.ellipse([x - 3 * S, y - 3 * S, x + 3 * S, y + 3 * S], fill=GOLD, outline=INK)
# floor and the slot the sticks come through
sd.rectangle([0, sh - 18 * S, sw, sh], fill='#8a5a3a')
sd.rectangle([0, sh - 18 * S, sw, sh - 15 * S], fill=INK)
# Agatha on her stick, with a hand rod
ag = cut('agatha'); ah = int(sh * 0.62); ag = ag.resize((int(ag.width * ah / ag.height), ah), Image.LANCZOS)
px = sw // 2 - ag.width // 2; py = sh - 18 * S - ah - 22 * S
shadow = Image.new('RGBA', ag.size, (42, 29, 22, 0)); shadow.putalpha(ag.split()[3].point(lambda v: v * 0.35))
stage.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(4 * S)), (px + 6 * S, py + 6 * S))
sd.rectangle([sw // 2 - 3 * S, py + ah - 30 * S, sw // 2 + 3 * S, sh], fill='#7a4a24', outline=INK)
sd.line([px + ag.width - 26 * S, py + ah * 0.55, px + ag.width + 18 * S, sh], fill=INK, width=2 * S)
stage.alpha_composite(ag, (px, py))
img.alpha_composite(stage, (ox0, oy0))
img.alpha_composite(frame, (fx, fy))

d = ImageDraw.Draw(img)
# title ribbon, dropped from the flies
ry = fy + fh + 14 * S
d.polygon([(14 * S, ry), (W - 14 * S, ry), (W - 26 * S, ry + 33 * S), (W - 14 * S, ry + 66 * S), (14 * S, ry + 66 * S),
           (26 * S, ry + 33 * S)], fill=RED)
ft = font('gloock.ttf', 42)
tw = d.textlength('Saints & Spells', font=ft)
d.text(((W - tw) / 2, ry + 8 * S), 'Saints & Spells', font=ft, fill=PLASTER)
# card
cy0 = ry + 84 * S
d.rounded_rectangle([14 * S, cy0, W - 14 * S, H - 14 * S], radius=3 * S, fill=PLASTER)
fb = font('literata.ttf', 18); fi = font('literata-it.ttf', 14); fs = font('literata-sb.ttf', 12)
lines = ['Under every saint in Sicily, the story', 'goes, there’s a goddess wearing a', 'disguise. We put that story on stage',
         'and checked it, claim by claim: who', 'said it first, and what the record', 'shows.']
y = cy0 + 18 * S
for ln in lines:
    d.text((30 * S, y), ln, font=fb, fill=INK); y += 28 * S
y += 8 * S
d.text((30 * S, y), 'A show in eight acts', font=fi, fill=SOFT); y += 22 * S
d.text((30 * S, y), 'BY BRYAN MURPHY · NOVEMBER 22, 2026', font=fs, fill=SOFT)
img.convert('RGB').save(os.path.join(ROOT, OUT), optimize=True)
print('wrote', OUT, img.size)
