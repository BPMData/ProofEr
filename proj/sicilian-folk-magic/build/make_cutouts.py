"""Cut the public-domain artworks in art/originals into paper cutouts for the puppets.

Thonny-friendly: press Run. Needs Pillow, numpy and opencv-python-headless.
Writes transparent PNGs (with a white paper rim, like scissor-cut card) to art/cut/.
"""
# ---------------- SETTINGS ----------------
ORIGINALS = 'proj/sicilian-folk-magic/art/originals'
OUT = 'proj/sicilian-folk-magic/art/cut'
WORK_SIZE = 900          # long side used for GrabCut (speed)
OUT_HEIGHT = 720         # height of each finished cutout, px
RIM = 7                  # white paper rim width at OUT_HEIGHT, px
# name: (source file, crop box as fractions (left, top, right, bottom), mode)
#   mode 'cut' = GrabCut the object off its background; 'print' = keep the rectangle, deckled paper edge
ITEMS = {
    'rosalia':   ('01-rosalia-vandyck.jpg',  (0.10, 0.02, 0.80, 0.62), 'cut'),
    'float':     ('02-houel-car-rosalia.jpg', (0.0, 0.0, 1.0, 1.0), 'print'),
    'agatha':    ('03-agatha-bronze.jpg',    (0.0, 0.0, 1.0, 1.0), 'cut'),
    'bust':      ('04-bust-front.jpg',       (0.04, 0.0, 0.92, 0.97), 'cut'),
    'lucy':      ('05-lucy-zurbaran.jpg',    (0.0, 0.0, 1.0, 1.0), 'cut'),
    'joseph':    ('06-joseph.jpg',           (0.0, 0.0, 1.0, 1.0), 'cut'),
    'goddess':   ('07-goddesses-front.jpg',  (0.02, 0.0, 0.52, 1.0), 'cut'),
    'isis':      ('08-isis-front.jpg',       (0.0, 0.0, 1.0, 1.0), 'cut'),
    'albarello': ('09-albarello-front.jpg',  (0.0, 0.0, 1.0, 1.0), 'cut'),
    'frame':     ('10-frame.jpg',            (0.0, 0.0, 1.0, 1.0), 'cut'),
    'exvoto':    ('11-exvoto.jpg',           (0.0, 0.0, 1.0, 1.0), 'print'),
    'angel1':    ('12-angel-1.jpg',          (0.0, 0.0, 1.0, 1.0), 'cut'),
    'agathabust': ("Busto_di_Sant'Agata.jpg", (0.0, 0.07, 0.92, 1.0), 'cut'),   # the real bust, Catania (Bryan's photo, Nov 23)
}
ONLY = []                # e.g. ['agathabust'] to redo one
# 'disc' items: (centre x, centre y, radius) in source pixels, plus the hanging string as a box
DISCS = {}
HOLLOW = ['frame']      # cut the bright mirror out of the middle (the frame becomes a window)                # e.g. ['rosalia'] to redo one
# ------------------------------------------
import os, sys
import numpy as np, cv2
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def grabcut(rgb):
    h, w = rgb.shape[:2]
    s = WORK_SIZE / max(h, w)
    small = cv2.resize(rgb, (int(w * s), int(h * s)), interpolation=cv2.INTER_AREA)
    sh, sw = small.shape[:2]
    mask = np.zeros((sh, sw), np.uint8)
    m = int(0.02 * max(sh, sw))
    rect = (m, m, sw - 2 * m, sh - 2 * m)
    bg, fg = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    cv2.grabCut(cv2.cvtColor(small, cv2.COLOR_RGB2BGR), mask, rect, bg, fg, 6, cv2.GC_INIT_WITH_RECT)
    a = np.where((mask == 1) | (mask == 3), 255, 0).astype(np.uint8)
    # keep the largest blob, fill holes
    n, lab, stats, _ = cv2.connectedComponentsWithStats(a)
    if n > 1:
        big = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
        a = np.where(lab == big, 255, 0).astype(np.uint8)
    cnts, _ = cv2.findContours(a, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    a = np.zeros_like(a); cv2.drawContours(a, cnts, -1, 255, -1)
    a = cv2.morphologyEx(a, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    return cv2.resize(a, (w, h), interpolation=cv2.INTER_LINEAR)

def finish(img, alpha, mode):
    # scale to OUT_HEIGHT
    s = OUT_HEIGHT / img.height
    img = img.resize((max(1, int(img.width * s)), OUT_HEIGHT), Image.LANCZOS)
    alpha = alpha.resize(img.size, Image.LANCZOS)
    a = np.array(alpha)
    if mode == 'print':
        rng = np.random.default_rng(7)
        h, w = a.shape
        a[:] = 0
        pad = RIM * 2
        a[pad:h - pad, pad:w - pad] = 255
    a = np.where(a > 127, 255, 0).astype(np.uint8)
    # scissor-cut paper: grow the shape, simplify to a polygon with straight snips
    rim = cv2.dilate(a, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (RIM * 2 + 1, RIM * 2 + 1)))
    if mode == 'hollow':
        paper = rim
    else:
        cnts, _ = cv2.findContours(rim, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        paper = np.zeros_like(rim)
        for c in cnts:
            poly = cv2.approxPolyDP(c, 3.0, True)
            cv2.fillPoly(paper, [poly], 255)
    # pad so the rim never touches the edge
    P = RIM * 2
    W, H = img.width + 2 * P, img.height + 2 * P
    out = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    paper_img = Image.new('RGBA', (W, H), (252, 249, 242, 0))
    pa = np.zeros((H, W), np.uint8); pa[P:P + img.height, P:P + img.width] = paper
    paper_img.putalpha(Image.fromarray(pa))
    out.alpha_composite(paper_img)
    art = img.convert('RGBA'); art.putalpha(Image.fromarray(a))
    out.alpha_composite(art, (P, P))
    return out

def main():
    src_dir, out_dir = os.path.join(ROOT, ORIGINALS), os.path.join(ROOT, OUT)
    os.makedirs(out_dir, exist_ok=True)
    for name, (fn, box, mode) in ITEMS.items():
        if ONLY and name not in ONLY:
            continue
        im = Image.open(os.path.join(src_dir, fn)).convert('RGB')
        L, T, R, B = box
        im = im.crop((int(L * im.width), int(T * im.height), int(R * im.width), int(B * im.height)))
        if mode == 'disc':
            (cx, cy, r), (sx0, sy0, sx1, sy1) = DISCS[name]
            a = np.zeros((im.height, im.width), np.uint8)
            cv2.circle(a, (cx, cy), r, 255, -1)
            a[sy0:sy1, sx0:sx1] = np.where(np.array(im.convert('L'))[sy0:sy1, sx0:sx1] > 150, 255, 0)
            alpha = Image.fromarray(a); bb = alpha.getbbox()
            im, alpha, mode = im.crop(bb), alpha.crop(bb), 'cut'
        elif mode == 'cut':
            alpha = Image.fromarray(grabcut(np.array(im)))
            bb = alpha.getbbox()
            im, alpha = im.crop(bb), alpha.crop(bb)
        else:
            alpha = Image.new('L', im.size, 255)
        if name in HOLLOW:
            a = np.array(alpha); g = np.array(im.convert('L'))
            h, w = g.shape
            ff = (g > 150).astype(np.uint8) * 255
            n, lab = cv2.connectedComponents(ff)
            inner = lab == lab[h // 2, w // 2]
            ys, xs = np.nonzero(inner)            # the opening is rectangular: clear its whole box
            a[ys.min():ys.max() + 1, xs.min():xs.max() + 1] = 0
            alpha = Image.fromarray(a)
            mode = 'hollow'
        out = finish(im, alpha, mode)
        out.save(os.path.join(out_dir, name + '.png'), optimize=True)
        print('wrote', name, out.size)

if __name__ == '__main__':
    main()
