"""Make the majolica wall tile from the Met albarello (Lazzaro workshop, Palermo). Thonny: press Run."""
# ---------------- SETTINGS ----------------
SRC = 'proj/sicilian-folk-magic/art/originals/09-albarello-back.jpg'
BOX = (612, 560, 812, 760)        # a square of the green foliage panel, in source pixels
OUT = 'proj/sicilian-folk-magic/art/cut/tile.png'
SIZE = 120                        # one quarter of the mirrored tile, px
# ------------------------------------------
import os
from PIL import Image, ImageOps
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
q = Image.open(os.path.join(ROOT, SRC)).convert('RGB').crop(BOX).resize((SIZE, SIZE), Image.LANCZOS)
t = Image.new('RGB', (SIZE * 2, SIZE * 2))
t.paste(q, (0, 0)); t.paste(ImageOps.mirror(q), (SIZE, 0))
t.paste(ImageOps.flip(q), (0, SIZE)); t.paste(ImageOps.flip(ImageOps.mirror(q)), (SIZE, SIZE))
t.save(os.path.join(ROOT, OUT), optimize=True)
print('wrote', OUT, t.size)
