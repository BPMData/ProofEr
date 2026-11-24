"""Build "Saints & Spells" (Sicilian folk magic) from copy.md, figures.md and the cutouts.

Thonny-friendly: press Run. Writes a draft page (fonts still linked from Google) to OUT; then run
tools/embed_fonts.py on it (or let EMBED_FONTS do it here) to make the single offline file.
"""
# ---------------- SETTINGS ----------------
PIECE = 'proj/sicilian-folk-magic'
OUT = 'proj/sicilian-folk-magic/build/out/sicilian-folk-magic.html'
IMG_HEIGHT = 560            # puppet height inside the page, px (about 2x their largest on-screen size)
IMG_QUALITY = 70            # WebP quality
EMBED_FONTS = True          # also write OUT with the fonts inlined (via tools/embed_fonts.py)
# ------------------------------------------
import base64, html, io, json, os, re, sys
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = lambda *a: os.path.join(ROOT, PIECE, *a)

# ---------- images ----------
def webp(name, h=IMG_HEIGHT, mirror=False):
    im = Image.open(P('art', 'cut', name + '.png')).convert('RGBA')
    if h and im.height > h:
        im = im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
    if mirror:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    b = io.BytesIO(); im.save(b, 'WEBP', quality=IMG_QUALITY, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()

def cc(code, ver):
    return f'<a href="https://creativecommons.org/licenses/{code}/{ver}/">CC {code.upper()} {ver}</a>'

CREDITS = {
    'rosalia': ('Saint Rosalia', 'Anthony van Dyck, <i>Saint Rosalie Interceding for the Plague-stricken of Palermo</i>, 1624 (detail). The Met, 71.41. CC0.'),
    'float': ('Rosalia’s car', 'Jean Houël, <i>The car of Saint Rosalia</i>, aquatint, 1780s. Wellcome Collection, 7145i. Public Domain Mark.'),
    'agatha': ('Saint Agatha', '<i>Saint Agatha</i>, bronze statuette, Italian (probably Naples), mid-17th c. The Met, 197071. CC0.'),
    'bust': ('Agatha’s bust', 'Giovanni di Bartolo, reliquary bust of Saint Agatha, 1376, Catania Cathedral. Photo: Riccardo Spoto, 2007, via Wikimedia Commons; released into the public domain by the author. Cut out for the stage.'),
    'lucy': ('Saint Lucy', 'Francisco de Zurbarán, <i>Saint Lucy</i>, c. 1625/30. National Gallery of Art, 1943.7.11. Public domain.'),
    'joseph': ('Saint Joseph', '<i>St. Joseph</i>, crèche figure, attributed to Salvatore di Franco, Naples, 2nd half 18th c. The Met, 64.164.3a–c. CC0.'),
    'goddess': ('A goddess', 'Terracotta bust (Persephone or Demeter), Greek, made in Sicily, 4th c. BCE. The Met, 1994.600.1–.2. CC0.'),
    'isis': ('Isis', '<i>Statuette of Isis nursing Horus</i>, Egyptian, Late Period, 664–332 BCE. The Met, 553002. CC0.'),
    'albarello': ('A Palermo jar', '<i>Albarello</i> (pharmacy jar), Lazzaro workshop, Palermo, 2nd half 16th c. The Met, 188537. CC0. Its foliage also makes the tile wall.'),
    'frame': ('The proscenium', 'Gilt ripple frame, Sicilian(?), late 17th c. The Met, 1975.1.2326. CC0.'),
    'exvoto': ('An ex-voto', 'Ex-voto: a man falls in a Roman street while his wife prays to Sansovino’s Virgin and Child, 27 May 1851. Rome, not Sicily. Wellcome Collection, 44879i. Public Domain Mark.'),
    'angel1': ('An angel', '<i>Angel</i>, crèche figure, Naples, 2nd half 18th c. The Met (crèche angels, 64.164). CC0.'),
    'benedict': ('Saint Benedict the Moor', 'Polychrome and gilt wood sculpture of <i>Saint Benedict of Palermo</i>, c. 1734, attributed to José Montes de Oca (Minneapolis Institute of Art, 2010.27.2). Photo: 19h00s at the National Gallery of Art, 2022, via Wikimedia Commons, ' + cc('by-sa', '4.0') + '. Cut out for the stage.'),
    'steri': ('An auto-da-fé', 'Bernard Picart (with C. Du Bosc), <i>An auto-da-fé of the Spanish Inquisition held in a church</i>, 18th-century engraving. Wellcome Collection, V0041640, ' + cc('by', '4.0') + '.'),
}
IMGS = {k: webp(k) for k in CREDITS if k not in ('frame', 'float', 'exvoto', 'bust', 'steri')}
IMGS['bust'] = webp('agathabust')   # the real bust (Bryan's photo, Nov 23); bust.png is the old Juliana stand-in
IMGS['float'] = webp('float', 520)
IMGS['exvoto'] = webp('exvoto', 520)
IMGS['steri'] = webp('steri', 520)
IMGS['angel1m'] = webp('angel1', mirror=True)
# Pitrè, Gramsci and de Martino on the stage (Bryan, Nov 24): cut from the same photos as the call-out portraits
# (art/originals/18-20; make_cutouts.py 'matte'). Their credits reuse PORTRAITS below.
STAGE_PEOPLE = ('pitre', 'gramsci', 'demartino')
for _k in STAGE_PEOPLE:
    IMGS[_k] = webp(_k)
FRAME = webp('frame', 640)

# ---------- zoom (Bryan, Nov 23: click a painting or statue to see it up close) ----------
# Same-repo relative WebP assets (no external network loads; check_offline.py passes).
ZOOM_SRC = {'rosalia': ('01-rosalia-vandyck', 1400), 'float': ('02-houel-car-rosalia', 1400), 'agatha': ('03-agatha-bronze', 1000),
            'bust': ("Busto_di_Sant'Agata.jpg", 1400), 'lucy': ('05-lucy-zurbaran', 1400), 'joseph': ('06-joseph', 1000),
            'goddess': ('07-goddesses-front', 1000), 'isis': ('08-isis-front', 1000), 'albarello': ('09-albarello-front', 1000),
            'exvoto': ('11-exvoto', 1400), 'angel1': ('12-angel-1', 1000),
            'benedict': ('16-benedict-moor.jpg', 1200), 'steri': ('17-steri-inquisition.jpg', 1400)}
ZOOM_QUALITY = 62
ASSET_DIRS = [
    os.path.join(ROOT, 'pieces', 'assets', 'sicilian-folk-magic'),
    os.path.join(ROOT, 'proj', 'sicilian-folk-magic', 'build', 'out', 'assets', 'sicilian-folk-magic'),
]
for _d in ASSET_DIRS:
    os.makedirs(_d, exist_ok=True)
def zoomimg(key, name, side, crop=None, lift=False):
    im = Image.open(P('art', 'originals', name if '.' in name else name + '.jpg')).convert('RGB')
    if crop:
        L, T, R, B = crop; im = im.crop((int(L * im.width), int(T * im.height), int(R * im.width), int(B * im.height)))
    if lift:
        im = ImageOps.autocontrast(im, cutoff=1)
    im.thumbnail((side, side), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'WEBP', quality=ZOOM_QUALITY, method=6)
    raw = b.getvalue()
    for _d in ASSET_DIRS:
        with open(os.path.join(_d, f'{key}.webp'), 'wb') as fh:
            fh.write(raw)
    return f'assets/sicilian-folk-magic/{key}.webp'
ZOOM = {k: zoomimg(k, *v) for k, v in ZOOM_SRC.items()}

# ---------- pictures in the text (Bryan, Nov 23: Act 6) ----------
# key: (original file, name, caption (our words), credit, alt text)
FIGS = {
    'bosch': ('14-bosch-fish', 'Riders on a fish',
              'Flying, as a Netherlandish painter imagined it around 1500: a man and a woman ride a huge fish through the sky. '
              'Bosch left no key to who they are.',
              'Hieronymus Bosch, <i>The Temptation of Saint Anthony</i>, right wing (detail), about 1500–10. Museu Nacional de '
              'Arte Antiga, Lisbon, inv. 1498 Pint. Public domain.',
              'Detail of a Bosch painting: a man with a lantern on a pole and a woman in a white headdress sit astride a large flying fish.'),
    'guidobono': ('15-guidobono-sorceress', 'The Sorceress',
                  'A painter’s sorceress, among animals, an open book and a fire. Nothing ties her to Sicily’s ladies from '
                  'outside, whose trials describe night visits and healing, not books of spells.',
                  'Bartolomeo Guidobono, <i>The Sorceress</i>, about 1690. Cantor Arts Center, Stanford University. Public domain.',
                  'A painting of a young woman in a white blouse and blue skirt bending toward a dog and a gazelle, with a fire and an open book at her feet.'),
    'gratteri': ('13-gratteri-portrait', 'A studio portrait',
                 'A woman in an old studio portrait, from the visitgratteri.com site. Her name, and the photographer’s, '
                 'aren’t recorded.',
                 'Photographer unknown, 19th century, via visitgratteri.com.',
                 'An old sepia photograph of a woman in a dark dress with a lace collar, standing with one hand on a chair.'),
}
def figthumb(name, side=760):
    im = Image.open(P('art', 'originals', name if '.' in name else name + '.jpg')).convert('RGB')
    im.thumbnail((side, side), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'WEBP', quality=IMG_QUALITY, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
for k, v in FIGS.items():
    ZOOM[k] = zoomimg(k, v[0], 1600 if k == 'bosch' else 1200)
FIG_CREDITS = {k: (v[1], v[3]) for k, v in FIGS.items()}

# ---------- relic photos for the cabinet (Bryan's files and licences, Nov 23) ----------
# key: (original file, zoom side, crop or None, name, credit). CC licences need the author, the licence link and a note of changes.
RELICS = {
    'urn': ('Urna_Santa_Rosalia_PA_14_07_2019_01.jpg', 1600, None, 'Rosalia’s urn',
            'The silver urn of Saint Rosalia, enthroned in the nave of Palermo Cathedral, 14 July 2019. Photo: Effems, '
            'own work, via Wikimedia Commons, ' + cc('by-sa', '4.0') + '. Resized.'),
    'capello': ('Reliquia_del_Sacro_Capello_di_Palmi_-_002.jpg', 1400, (0.14, 0.14, 0.86, 0.86), 'The hair at Palmi',
                'Reliquary of the Holy Hair, Palmi, 2014; the label reads “De Capillis” (“of the hair”). Photo: Palminellafede, '
                'own work, via Wikimedia Commons, ' + cc('by-sa', '4.0') + '. Cropped and contrast raised.'),
    'lettera': ('Virgin-to-Messina-1674-78_Bibliotheca_Fictiva_nr._8699204.png', 1600, None, 'The Letter, copied out',
                '<i>Lettera di Maria Vergine ai Messinesi</i>, manuscript, Messina(?), about 1674–78. Bibliotheca Fictiva '
                'Collection, Sheridan Libraries, Johns Hopkins University. Public domain.'),
    'lucybody': ('The_relics_of_Santa_Lucia,_Chiesa_di_San_Geremia,_Venice_(37060531904).jpg', 1600, None, 'Lucy in Venice',
                 'The relics of Saint Lucy, church of San Geremia, Venice, 2017. Photo: Dimitris Kamaras, ' + cc('by', '2.0') + '. Resized.'),
    'louis': ('Tomb_of_Louis_IX_of_France_-_Cathedral_of_Monreale_-_Italy_2015_(2).jpeg', 1600, None, 'Louis IX at Monreale',
              'Tomb of Louis IX, Monreale Cathedral, 2015. © José Luiz Bernardes Ribeiro / ' + cc('by-sa', '4.0') + '. Resized.'),
}
for k, v in RELICS.items(): ZOOM[k] = zoomimg(k, v[0], v[1], v[2], lift=(k == 'capello'))
def relic_thumb(name, crop=None, lift=False):
    im = Image.open(P('art', 'originals', name if '.' in name else name + '.jpg')).convert('RGB')
    if crop:
        L, T, R, B = crop; im = im.crop((int(L * im.width), int(T * im.height), int(R * im.width), int(B * im.height)))
    if lift:
        im = ImageOps.autocontrast(im, cutoff=1)
    im = ImageOps.fit(im, (128, 128), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'WEBP', quality=ZOOM_QUALITY, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
THUMBS = {
    'bust': relic_thumb(ZOOM_SRC['bust'][0]),
    'urn': relic_thumb(RELICS['urn'][0]),
    'capello': relic_thumb(RELICS['capello'][0], RELICS['capello'][2], lift=True),
    'lucybody': relic_thumb(RELICS['lucybody'][0]),
    'louis': relic_thumb(RELICS['louis'][0]),
}
FIG_CREDITS.update({k: (v[3], v[4]) for k, v in RELICS.items()})
FIGS['lettera'] = (RELICS['lettera'][0], RELICS['lettera'][3],
                   'The Letter as Messina wanted to see it: a copy made in the 1670s, probably sold to pilgrims who came for the '
                   'feast. Mary’s name heads it; the harbour of Messina runs along the bottom.',
                   RELICS['lettera'][4],
                   'A wide illuminated manuscript page: Latin text in the centre, coats of arms in the corners, a painted '
                   'scene of Mary at the top and a view of a harbour with ships along the bottom.')
def figure_html(k):
    f = FIGS[k]
    return (f'<figure class="infig"><button type="button" class="figbtn" data-z="{k}" aria-label="See {html.escape(f[1])} up close">'
            f'<img src="{figthumb(f[0])}" alt="{html.escape(f[4])}" loading="lazy"></button>'
            f'<figcaption>{f[2]} <span class="credit">{f[3]}</span></figcaption></figure>')
TILE = webp('tile', None)

# ---------- figures: sources by ID ----------
fig = open(P('figures.md'), encoding='utf-8').read()
SRC = {}
for ln in fig.splitlines():
    m = re.match(r'^\|\s*(X\d-\d+[a-z]?)\s*\|', ln)
    if m:
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        if len(cells) >= 4:
            SRC[m.group(1)] = cells[3]
TALLY = {}
for ln in fig.splitlines():
    m = re.match(r'^\|\s*(T\d+)\s*\|', ln)
    if m:
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        TALLY[m.group(1)] = re.findall(r'X2-\d+', cells[3])

def ids_in(ref):
    out = re.findall(r'X\d-\d+[a-z]?', ref)
    for a, b in re.findall(r'T(\d+)[–-]T(\d+)', ref):
        for t in range(int(a), int(b) + 1):
            out += TALLY.get(f'T{t}', [])
    for t in re.findall(r'\bT(\d+)\b', ref):
        out += TALLY.get(f'T{t}', [])
    if 'fingerbone tally' in ref:
        for v in TALLY.values():
            out += v
    return out

# ---------- copy ----------
copy = open(P('copy.md'), encoding='utf-8').read()
copy = copy.split('\n---\n', 1)[1]
# build-time edits (logged in STATUS): the ex-voto line had no source; use X1-168 instead
copy = copy.replace(
    'Churches still fill with silver hearts, eyes and limbs left as thanks for a cure. [**needs a source line**: X1-171\nonly says the dated Sicilian painted tablets are 19th–20th c.]',
    'An ex-voto is a thank-you made visible. Painted ones show the danger, the person saved and the holy helper; wax, '
    'metal or terracotta ones show the healed body part. The Palermo scholar I. E. Buttitta calls a painted ex-voto a '
    '"standing declaration of debt" to the saint. [X1-168 (Buttitta, named)]')
copy = re.sub(r'\[\*\*Left out until sourced:\*\*[^\]]*\]\n', '', copy)
gloss_part = copy.split('## Glosses')[1]
call_part = copy.split('## Call-outs')[1].split('## Glosses')[0]
copy = copy.split('## Call-outs')[0]

# call-outs: '- **Name** | dates | portrait-key: text [ids]'  (Bryan, Nov 23: drill-downs for people and peoples)
PORTRAITS = {
    'pitre': ('Giuseppe Pitrè', 'Photograph by an unknown photographer, before 1916 (Pitrè died that year). Public domain by age. '
              'From Sicilian Post.'),
    'gramsci': ('Antonio Gramsci', 'Photograph by an unknown photographer, about 1922. Public domain by age. '
                'From Wikimedia Commons (File:Gramsci.png).'),
    'demartino': ('Ernesto de Martino', 'Photograph by F.DelDongo, about 1956, from Wikimedia Commons '
                  '(File:Album_mix_005_Muzi_Epifani_Ernesto_de_Martino.jpg), '
                  '<a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="noopener">CC BY-SA 4.0</a>. '
                  'Cropped to de Martino alone; this crop is shared under the same licence.'),
    'gebelin': ('Antoine Court de Gébelin', 'Engraving by François Huot after André Pujos, 1784, via Wikimedia Commons '
                '(File:Antoine-court-de-gebelin-pujos-huot-1784.jpg). Public domain.'),
    'etteilla': ('Etteilla (Jean-Baptiste Alliette)', 'Engraving by an unknown artist, 1790, from <i>Cours théorique et pratique du livre de Thot</i>, '
                 'via Wikimedia Commons (File:ALLIETTE.jpg). Public domain.'),
    'papus': ('Papus (Gérard Encausse)', 'Photograph by Eugène Pirou, 1893, BnF Gallica, via Wikimedia Commons '
              '(File:Gerard Encausse.jpeg). Public domain.'),
    'waite': ('Arthur Edward Waite', 'Photograph by an unknown photographer, early 1880s, via Wikimedia Commons '
              '(File:ArthurEdwardWaite~1880.JPG). Public domain.'),
    'smith': ('Pamela Colman Smith', 'Photograph by an unknown photographer, published in <i>The Craftsman</i>, October 1912, '
              'via Wikimedia Commons (File:Pamela Colman Smith circa 1912.jpg). Public domain in the US (PD-1923).'),
    'crowley': ('Aleister Crowley', 'Photograph by an unknown photographer, 1910 (Golden Dawn regalia, publicity for <i>The Rites of Eleusis</i>), '
                'via Wikimedia Commons (File:Aleister Crowley, Golden Dawn.jpg). Public domain.'),
}
def portrait(k):
    b = open(P('art', 'portraits', k + '.jpg'), 'rb').read()
    return 'data:image/jpeg;base64,' + base64.b64encode(b).decode()
CALLOUT, CALL_IDS = {}, {}
for item in re.split(r'\n- ', '\n' + call_part.split('\n', 1)[1].strip()):
    item = ' '.join(item.split())
    m = re.match(r'\*\*(.+?)\*\* \| (.*?) \| (\w*): (.*?)\s*(\[[^\]]*\])?$', item)
    if not m:
        continue
    key, sub, img, text = m.group(1), m.group(2), m.group(3), m.group(4)
    CALLOUT[key] = dict(title=key if key[0].isupper() else sub, sub=sub if key[0].isupper() else '', text=text,
                        img=portrait(img) if img else '', credit=PORTRAITS[img][1] if img else '')
    CALL_IDS[key] = re.findall(r'X\d-\d+[a-z]?', m.group(5) or '')

GLOSS = {}
for item in re.split(r'\n- ', '\n' + gloss_part.split('\n', 1)[1]):
    item = ' '.join(item.split())
    m = re.match(r'(\*[^*]+\*(?: / \*[^*]+\*)?): (.*?)\s*(\[[^\]]*\])?$', item)
    if not m:
        continue
    terms = re.findall(r'\*([^*]+)\*', m.group(1))
    defs = m.group(2).split(' / ') if len(terms) > 1 and ' / ' in m.group(2) else [m.group(2)] * len(terms)
    for t, d in zip(terms, defs):
        GLOSS[t] = d

def smart(s):
    s = re.sub(r'(^|[\s(\[“])"', r'\1“', s)
    s = s.replace('"', '”')
    s = re.sub(r"(\w)'(\w)", r'\1’\2', s)
    s = re.sub(r"(^|\s)'", r'\1‘', s)
    return s.replace("'", '’')

USED_CALLS = []
def inline(s):
    s = html.escape(s, quote=False)
    s = smart(s)
    def call(key, label):
        USED_CALLS.append(key)
        return (f'<button type="button" class="gloss callout" aria-expanded="false" data-callout="{html.escape(key)}">'
                f'{label}</button>')
    s = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', lambda m: call(m.group(2), m.group(1)), s)
    s = re.sub(r'\[([^\[\]]+)\]\((https://[^)\s]+)\)', r'<a href="\2" rel="noopener">\1</a>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', lambda m: call(m.group(1), f'<strong>{m.group(1)}</strong>') if m.group(1) in CALLOUT
               else f'<strong>{m.group(1)}</strong>', s)
    def em(m):
        t = m.group(1)
        if t in GLOSS:
            return (f'<button type="button" class="gloss" aria-expanded="false" data-gloss="{html.escape(GLOSS[t])}">'
                    f'<i>{t}</i></button>')
        return f'<i>{t}</i>'
    s = re.sub(r'(?<![\w*])\*([^*\n]+?)\*(?![\w*])', em, s)
    return s

REF = re.compile(r'\s*\[((?:X\d|tally|fingerbone|brief|premise|T\d)[^\]]*)\]')

def stamp_html(txt):
    parts = [p.strip() for p in txt.split('·')]
    claim = inline(parts[1]) if len(parts) > 1 else ''
    verdict = inline(parts[2]) if len(parts) > 2 else ''
    return (f'<div class="myth" data-stamp="{html.escape(parts[1] if len(parts) > 1 else "")}">'
            f'<span class="stampbox" aria-hidden="true">Myth-check</span>'
            f'<p><span class="vh">Myth-check. Claim: </span><span class="claim">{claim}</span>'
            f'<span class="verdict"><span class="vh">What the record shows: </span>{verdict}</span></p></div>')

def check_html(txt):
    parts = [x.strip() for x in txt.split('·', 1)]
    claim = parts[0] if parts else ''
    verdict = parts[1] if len(parts) > 1 else ''
    return f'<div class="myth-sm"><span class="mtag">Record check</span><p><span class="mclaim">{inline(claim)}</span><span class="mverd">{inline(verdict)}</span></p></div>'

sections = re.split(r'\n(?=## )', copy.strip())
SECS = []
for sec in sections:
    head, _, body = sec.partition('\n')
    m = re.match(r'## (\d+) · (.*)', head)
    num, title = int(m.group(1)), m.group(2).strip()
    ids, blocks = [], []
    paras = [p for p in re.split(r'\n\s*\n', body.strip()) if p.strip() and p.strip() != '---']
    for p in paras:
        for r in REF.findall(p):
            ids += ids_in(r)
        for k in CALLOUT:
            if f'**{k}**' in p or f'|{k}]]' in p:
                ids += CALL_IDS[k]
        p = REF.sub('', p)
        lines = p.split('\n')
        if p.startswith('>'):
            continue  # margin voices cut (Bryan, Nov 23)
        elif re.match(r'_cabinet \w+_$', p.strip()):
            blocks.append(f'{{{{CAB:{p.strip()[9:-1]}}}}}')   # a drawer fills partway through the section
        elif re.match(r'_scene \d+_$', p.strip()):
            blocks.append(f'{{{{BEAT:{p.strip()[7:-1]}}}}}')   # stage switches partway through the section
        elif re.match(r'_figure \w+_$', p.strip()):
            blocks.append(figure_html(p.strip()[8:-1]))
        elif p.startswith('_[Unit chart'):
            blocks.append('{{UNIT}}')
        elif p.startswith('_'):
            cue = p.strip('_ \n')
            blocks.append(f'<!-- cue: {html.escape(cue)} -->')
        elif p.startswith('**Stamps:**'):
            items = re.split(r'\n- ', '\n' + p.split('\n', 1)[1].strip())
            for it in items:
                it = ' '.join(it.split())
                if it:
                    blocks.append(stamp_html(it))
        elif p.startswith('**Stamp:**'):
            chunks = re.split(r'\*\*Stamp:\*\*', p)
            for ch in chunks:
                ch = ' '.join(ch.split())
                if not ch:
                    continue
                # a stamp ends at its verdict; a sentence after it (capital letter after the 2nd '·' part) is prose
                mm = re.match(r'(MYTH-CHECK · [^·]+ · .+?)(?:\s+((?:The|A|An) [A-Z]?.*))?$', ch)
                if mm and mm.group(2) and len(mm.group(1).split('·')) >= 3:
                    blocks.append(stamp_html(mm.group(1)))
                    blocks.append(f'<p>{inline(mm.group(2))}</p>')
                else:
                    blocks.append(stamp_html(ch))
        elif p.startswith('**Check:**'):
            blocks.append(check_html(' '.join(p[len('**Check:**'):].split())))
        elif all(ln.startswith(('- ', '  ')) for ln in lines) or (lines[0].endswith(':') and len(lines) > 1 and lines[1].startswith('- ')):
            lead = ''
            if not lines[0].startswith('- '):
                lead = f'<p>{inline(lines[0])}</p>'
                lines = lines[1:]
            items = re.split(r'\n- ', '\n' + '\n'.join(lines))
            lis = ''.join(f'<li>{inline(" ".join(it.split()).lstrip("- "))}</li>' for it in items if it.strip())
            blocks.append(lead + f'<ul>{lis}</ul>')
        else:
            blocks.append(f'<p>{inline(" ".join(p.split()))}</p>')
    SECS.append(dict(num=num, title=title, blocks=blocks, ids=list(dict.fromkeys(ids))))

# ---------- charts ----------
def timeline_svg():
    # year scale, 500–1900; points and ranges from copy section 3 (X1 rows)
    ev = [(535, 535, 'Byzantium takes the island'), (831, 831, 'Arabs take Palermo'),
          (1061, 1091, 'Normans conquer the island'), (1071, 1072, 'Palermo falls (1071–72)'),
          (1130, 1130, 'Roger II crowned; Kingdom of Sicily'), (1194, 1266, 'Hohenstaufen'),
          (1266, 1282, 'Angevins'), (1282, 1282, 'Sicilian Vespers; Aragon'),
          (1443, 1443, 'One king for Naples and Sicily'), (1487, 1487, 'First Spanish inquisitor'),
          (1713, 1713, 'Savoy'), (1720, 1734, 'Austria'), (1782, 1782, 'Inquisition abolished'),
          (1816, 1816, 'Kingdom of the Two Sicilies')]
    W, H, x0, x1 = 360, 760, 70, 0
    y = lambda yr: 30 + (yr - 500) / 1400 * (H - 60)
    s = [f'<svg viewBox="0 0 {W} {H}" class="tl" role="img" aria-labelledby="tl-t">',
         '<title id="tl-t">Timeline, 500 to 1900, drawn to scale by year</title>']
    for yr in range(500, 1901, 100):
        s.append(f'<line x1="56" x2="64" y1="{y(yr):.1f}" y2="{y(yr):.1f}" class="tick"/>'
                 f'<text x="50" y="{y(yr) + 4:.1f}" class="yr" text-anchor="end">{yr}</text>')
    s.append(f'<line x1="64" x2="64" y1="{y(500):.1f}" y2="{y(1900):.1f}" class="axis"/>')
    last = -99
    for a, b, lab in ev:
        inq = ' inq' if 'nquisit' in lab else ''
        ya, yb = y(a), y(b)
        if b > a:
            s.append(f'<rect x="60" y="{ya:.1f}" width="8" height="{max(yb - ya, 2):.1f}" class="span"/>')
        else:
            s.append(f'<circle cx="64" cy="{ya:.1f}" r="4.5" class="pt{inq}"/>')
        ty = max((ya + yb) / 2 + 4, last + 15)
        last = ty
        yrs = f'{a}' if a == b else f'{a}–{b}'
        s.append(f'<line x1="70" x2="96" y1="{(ya + yb) / 2:.1f}" y2="{ty - 4:.1f}" class="lead"/>'
                 f'<text x="100" y="{ty:.1f}" class="lab{inq}"><tspan class="lyr">{yrs}</tspan> {html.escape(lab)}</text>')
    s.append('</svg>')
    return ''.join(s)

def strip_svg():
    # May 1624 to July 1625, by day
    import datetime as dt
    d0, d1 = dt.date(1624, 5, 1), dt.date(1625, 7, 31)
    ev = [(dt.date(1624, 5, 15), 'May 1624', 'plague reaches Palermo', 'month'),
          (dt.date(1624, 7, 15), '15 Jul 1624', 'bones found', ''),
          (dt.date(1624, 7, 27), '27 Jul 1624', 'elected patron', 'hit'),
          (dt.date(1624, 11, 15), 'Nov 1624', 'commission set up', 'month'),
          (dt.date(1625, 2, 4), '4 Feb 1625', 'Bonelli’s vision', ''),
          (dt.date(1625, 2, 15), 'Feb 1625', 'bones declared hers', 'hit month'),
          (dt.date(1625, 6, 9), '9 Jun 1625', 'first procession', ''),
          (dt.date(1625, 7, 15), '15 Jul 1625', 'plague declared over', '')]
    W, H = 360, 520
    span = (d1 - d0).days
    y = lambda d: 20 + (d - d0).days / span * (H - 40)
    s = [f'<svg viewBox="0 0 {W} {H}" class="strip" role="img" aria-labelledby="st-t">',
         '<title id="st-t">May 1624 to July 1625, drawn to scale by day</title>']
    m = d0
    i = 0
    while m <= d1:
        yy = y(m)
        s.append(f'<line x1="64" x2="72" y1="{yy:.1f}" y2="{yy:.1f}" class="tick"/>')
        if m.month in (1, 7) or i == 0:
            s.append(f'<text x="58" y="{yy + 4:.1f}" class="yr" text-anchor="end">{m.strftime("%b %Y")}</text>')
        m = dt.date(m.year + (m.month == 12), m.month % 12 + 1, 1); i += 1
    s.append(f'<line x1="72" x2="72" y1="{y(d0):.1f}" y2="{y(d1):.1f}" class="axis"/>')
    ya, yb = y(dt.date(1624, 7, 27)), y(dt.date(1625, 2, 15))
    yn = y(dt.date(1624, 11, 15))
    gy = (ya + 17 + yn) / 2 - 6
    s.append(f'<rect x="68" y="{ya:.1f}" width="8" height="{yb - ya:.1f}" class="gap"/>'
             f'<text x="100" y="{gy:.1f}" class="gaplab">Patron for about seven</text>'
             f'<text x="100" y="{gy + 16:.1f}" class="gaplab">months before the proof</text>')
    last = -99
    for d, when, what, cls in ev:
        yy = y(d)
        ty = max(yy + 4, last + 17); last = ty
        mark = (f'<rect x="66" y="{yy - 6:.1f}" width="12" height="12" class="pt month"/>' if 'month' in cls
                else f'<circle cx="72" cy="{yy:.1f}" r="5" class="pt"/>')
        s.append(mark + f'<text x="100" y="{ty:.1f}" class="lab{" hit" if "hit" in cls else ""}">'
                 f'<tspan class="lyr">{when}</tspan> {html.escape(what)}</text>'
                 f'<line x1="80" x2="96" y1="{yy:.1f}" y2="{ty - 4:.1f}" class="lead"/>')
    s.append('</svg>')
    return ''.join(s)

def unit_html():
    # Bryan, Nov 23: no plain cubes. Penitent's hats (the coroza) for people tried, one hat = 10 people;
    # stakes for people executed, one stake = 1 person, any charge.
    cw, ch, cols = 14, 19, 25
    out = ['<svg viewBox="0 0 350 {H}" aria-hidden="true" focusable="false">',
           '<defs><symbol id="cone" viewBox="0 0 14 19"><path d="M7 1 L11.6 15.2 L2.4 15.2 Z"/><rect x="1" y="15.2" width="12" height="2.6" rx="1"/></symbol>',
           '<symbol id="stk" viewBox="0 0 26 34"><g style="fill:var(--sp);stroke:var(--so);stroke-width:var(--sw)"><rect x="11" y="2" width="4" height="30"/><rect x="6" y="9" width="14" height="3"/></g>',
           '<path style="fill:var(--sf);stroke:var(--so);stroke-width:var(--sw)" d="M3 32 C 2 26, 7 25, 6 20 C 10 23, 11 27, 13 24 C 15 27, 17 22, 20 20 C 19 25, 24 26, 23 32 Z"/></symbol></defs>']
    out.append('<text x="0" y="13" class="k">One hat = 10 people tried, 1487–1782</text>')
    y = 22
    groups = [('about 1,000 charged with magic or witchcraft', 100, 'cone magic'),
              ('everyone else tried: about 5,000 more', 500, 'cone'),
              ('outlined: the range, up to 7,000 in all', 100, 'cone range')]
    for lab, n, cls in groups:
        out.append(f'<text x="0" y="{y + 13}" class="k{" gold" if "magic" in cls else ""}">{lab}</text>')
        y += 20
        for i in range(n):
            out.append(f'<use href="#cone" x="{(i % cols) * cw}" y="{y + (i // cols) * ch}" width="{cw}" height="{ch}" class="{cls}"/>')
        y += (n // cols) * ch + 10
    y += 10
    out.append(f'<text x="0" y="{y + 13}" class="k">One stake = one person executed in person,</text>'
               f'<text x="0" y="{y + 29}" class="k">1540–1700, for any charge</text>')
    y += 38
    for i in range(52):
        out.append(f'<g class="stake{" open" if i >= 25 else ""}"><use href="#stk" x="{(i % 13) * 26.9:.1f}" y="{y + (i // 13) * 36}" width="26" height="34"/></g>')
    y += 4 * 36 + 6
    out.append(f'<text x="0" y="{y + 12}" class="k">solid: 25 in the surviving reports</text>'
               f'<text x="0" y="{y + 28}" class="k">outlined: up to 52 in a fuller count</text>')
    y += 38
    out.append('</svg>')
    svg = ''.join(out).replace('{H}', str(y))
    return f'''<figure class="chart unit" aria-labelledby="unit-cap">
{svg}
<figcaption id="unit-cap">Everyone the Sicilian Inquisition tried, 1487–1782, against the people it executed. Top: one
penitent’s hat (the <i>coroza</i> the convicted wore) is 10 people; about 6,000 to 7,000 were tried (the outlined hats
are the range), and about 1,000 of them were charged with magic or witchcraft. Bottom: one stake is one person; 25 to 52
were executed in person between 1540 and 1700, for any charge. Almost none were for witchcraft: no woman is known to
have been executed as a witch.</figcaption>
</figure>'''

def cabinet_html():
    groups = [
        ('Lucy’s whole body', [('Venice', 'claim', '', 'lucybody'), ('Metz', 'claim', '', ''), ('Syracuse', 'empty', 'the original tomb, empty', '')], 'Our count: two claims, Venice and Metz.'),
        ('Lucy’s head', [('Venice', 'synth', '', ''), ('Bourges', 'synth', '', '')], 'Our own comparison of two separate reports.'),
        ('Agatha', [('Catania', 'claim', 'the body', 'bust'), ('Palermo', 'claim', 'her arm', ''), ('31 places', 'synth', 'outside Catania, per one tourism list', '')], 'Spread, not doubled.'),
        ('Louis IX', [('Monreale', 'claim', 'entrails', 'louis'), ('Monreale?', 'synth', 'heart, by one medieval account', ''), ('Saint-Denis?', 'synth', 'heart, says Le Goff', '')], 'The heart is disputed.'),
        ('Rosalia', [('Palermo', 'claim', 'the bones, in a silver urn', 'urn')], ''),
        ('Mary’s hair', [('Messina', 'claim', 'with the Letter', 'capello')], ''),
    ]
    out = ['<figure class="chart cabinet" aria-labelledby="cab-cap"><div class="drawers">']
    for name, ds, note in groups:
        out.append(f'<div class="dgroup"><h3>{name}</h3><div class="drow">')
        for place, kind, sub, z in ds:
            head = f'<button type="button" class="zbtn" data-z="{z}" aria-label="See {place} relic up close">{place}</button>' if z else place
            out.append(f'<div class="drawer {kind}"><b>{head}</b>{f"<small>{sub}</small>" if sub else ""}</div>')
        out.append(f'</div>{f"<p>{note}</p>" if note else ""}</div>')
    out.append('</div><figcaption id="cab-cap">The relic cabinet, opened: one drawer for each place that claims a relic '
               'met in this show, side by side when two places claim the same part. Plain drawers are claims the sources '
               'report; striped drawers rest on one source or on our own comparison; the dashed drawer is an empty tomb. '
               'Counts only, not an inventory. Click underlined places to inspect the relic photo.</figcaption></figure>')
    return ''.join(out)

def route_svg():
    return '''<figure class="chart route" aria-labelledby="route-cap">
<svg viewBox="0 0 420 310" role="img" aria-labelledby="route-t"><title id="route-t">Routes from Sicily, not to scale</title>
<defs>
<marker id="arr1" viewBox="0 0 10 10" refX="7.5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M1 1.5 L8.5 5 L1 8.5 z" fill="#2a1d16"/></marker>
<marker id="arr2" viewBox="0 0 10 10" refX="7.5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M1 1.5 L8.5 5 L1 8.5 z" fill="#1d4f8a"/></marker>
</defs>
<rect width="420" height="310" class="sea"/>
<!-- Western Europe, Iberia & Italian boot -->
<path class="land" d="M292 0 L420 0 L420 112 C 402 104, 386 88, 370 72 L352 104 L356 122 L344 130 L338 118 L322 86 L312 64 C 300 66, 290 72, 286 76 L276 74 L254 78 L252 96 L256 112 L272 118 L288 106 L296 74 L276 62 L274 36 L292 0 Z"/>
<!-- North African rim framing the Mediterranean -->
<path class="land" d="M254 136 L294 136 C 322 142, 344 150, 368 150 L420 154 L420 198 L250 198 C 248 176, 250 156, 254 136 Z"/>
<!-- New Spain / Mexico, Central America & Caribbean -->
<path class="land" d="M0 44 L86 44 L84 62 L66 72 C 62 84, 70 96, 86 96 L94 84 L102 88 L98 104 L108 118 L124 128 L120 134 L102 128 L82 116 L54 114 L24 94 L0 74 Z"/>
<path class="land" d="M106 72 Q 116 68 128 76 Q 118 82 106 76 Z M132 78 Q 140 76 146 81 Q 138 86 132 82 Z"/>
<!-- South America: Venezuela coast & Brazil Atlantic bulge -->
<path class="land" d="M124 130 L144 130 L166 138 L194 160 L212 184 L204 218 L178 258 L156 310 L114 310 L108 242 L94 188 L104 150 Z"/>
<!-- Sicily -->
<path class="island" d="M320 132 L338 128 L334 141 L322 138 Z"/>
<!-- Solid routes: Sicily -> Lisbon -> Brazil -> Venezuela -->
<path class="r1" d="M328 134 C 304 132, 280 116, 258 96"/>
<path class="r1" marker-end="url(#arr1)" d="M258 96 C 232 138, 214 170, 194 196"/>
<path class="r1" marker-end="url(#arr1)" d="M192 200 C 170 176, 154 156, 140 142"/>
<!-- Dashed route: Sicily -> New Spain -->
<path class="r2" marker-end="url(#arr2)" d="M328 134 C 246 48, 148 48, 72 88"/>
<circle class="cp" cx="328" cy="134" r="4.5"/><text x="348" y="148" class="ml">Sicily</text>
<circle class="cp" cx="258" cy="96" r="4"/><text x="246" y="92" class="ml" text-anchor="end">Lisbon, by 1609</text>
<circle class="cp" cx="66" cy="90" r="4"/><text x="10" y="20" class="ml">New Spain: Rosalia;</text><text x="10" y="36" class="ml">Joseph patron, 1555</text>
<circle class="cp" cx="136" cy="138" r="4"/><text x="148" y="122" class="ml">Venezuela: the drums</text>
<circle class="cp" cx="192" cy="200" r="4"/><text x="210" y="216" class="ml">Brazil, early 1600s</text>
<!-- Compact legend -->
<line x1="258" y1="256" x2="282" y2="256" class="r1"/><text x="288" y="260" class="leg">Benedict’s cult</text>
<line x1="258" y1="274" x2="282" y2="274" class="r2"/><text x="288" y="278" class="leg">Rosalia &amp; Joseph</text>
<text x="408" y="298" class="nts" text-anchor="end">not to scale</text>
</svg>
<figcaption id="route-cap">Not to scale. Solid line: Benedict the Moor’s cult, carried by Black Catholic brotherhoods
through Lisbon (a confraternity by 1609) to Brazil and the Spanish and Portuguese New World from the early 1600s,
and on to Venezuela. Dashed line: Rosalia to New Spain with the Jesuits and the Spanish crown; Saint Joseph was made
patron of the Mexican Church in 1555.</figcaption></figure>'''

def listbox(title, inner):
    return f'<details class="aslist"><summary>{title}</summary>{inner}</details>'

# place charts
for s in SECS:
    if s['num'] == 3:
        i = next(k for k, b in enumerate(s['blocks']) if b.startswith('<p>Then the island changed hands'))
        lst = s['blocks'][i]
        s['blocks'][i] = ('<p>Then the island changed hands, again and again.</p><figure class="chart tlfig" aria-labelledby="tl-cap">'
                          + timeline_svg() + '<figcaption id="tl-cap">Who ruled Sicily, 500 to 1900, to scale by year. Bars are spans; '
                          'dots are single years. The two Inquisition dates are in blue.</figcaption></figure>'
                          + listbox('Read it as a list', lst.split('</p>', 1)[1]))
    if s['num'] == 5:
        i = next(k for k, b in enumerate(s['blocks']) if b.startswith('<p>Here is the timeline'))
        lst = s['blocks'][i]
        s['blocks'][i] = ('<p>Here is the timeline, and it is the punchline.</p><figure class="chart stfig" aria-labelledby="st-cap">'
                          + strip_svg() + '<figcaption id="st-cap">Palermo, May 1624 to July 1625, to scale by day. Squares '
                          'mark dates known only to the month.</figcaption></figure>' + listbox('Read it as a list', lst.split('</p>', 1)[1]))
    if s['num'] == 9:
        s['blocks'] = [unit_html() if b == '{{UNIT}}' else b for b in s['blocks']]
    if s['num'] == 10:
        i = next(k for k, b in enumerate(s['blocks']) if b.startswith('<p>Palermo Cathedral says its Chapel of the Relics'))
        s['blocks'].insert(i + 1, cabinet_html())
    if s['num'] == 11:
        i = next(k for k, b in enumerate(s['blocks']) if '<strong>Rosalia</strong>' in b)
        s['blocks'].insert(i + 1, route_svg())

# ---------- stage scenes ----------
# each puppet: [kind, key, x% (centre), height% of stage, extra]
SCENES = {
    0: dict(lights=True, cast=[['teller', '', 27, 62], ['tarot', '', 62, 31, 'down']]),
    1: dict(lights=True, cast=[['teller', '', 27, 62], ['tarot', '', 62, 31, 'read']]),
    14: dict(lights=True, cast=[['teller', '', 27, 62, 'unmask'], ['card', 'Milan, 1440s', 70, 44, 'a card game']]),
    15: dict(lights=True, cast=[['img', 'isis', 18, 56], ['img', 'goddess', 44, 50], ['img', 'agatha', 74, 62]]),
    # the three thinkers as cut-paper puppets (Bryan, Nov 24), each with the name tag the old cards carried
    2: dict(cast=[['img', 'pitre', 20, 46, 'Pitrè', 'Palermo · 1910'], ['img', 'gramsci', 50, 50, 'Gramsci', 'prison notebooks'],
                  ['img', 'demartino', 80, 49, 'de Martino', 'Sud e magia · 1959']]),
    3: dict(cast=[['card', '535', 23, 36, 'Byzantium'], ['card', '831', 50, 42, 'Arabs take Palermo'], ['card', '1071–72', 77, 36, 'Normans']]),
    4: dict(sea=True, cast=[['boat', 'bust', 62, 54], ['img', 'agatha', 25, 46]]),
    5: dict(back='float', cast=[['img', 'rosalia', 50, 64]]),
    6: dict(cast=[['letter', 'Messina · “AD 42”', 50, 56]]),
    7: dict(cast=[['img', 'joseph', 24, 70], ['table', '', 59, 40]]),
    8: dict(night=True, cast=[['print', 'exvoto', 50, 58]]),
    9: dict(night=True, cast=[['img', 'albarello', 22, 58], ['eye', '', 56, 40], ['horn', '', 82, 36]]),
    16: dict(night=True, cast=[['print', 'steri', 34, 56], ['card', 'Steri · 1601–1782', 73, 42, '2 men for magic']]),
    17: dict(night=True, cast=[['card', 'Donne di fuora', 50, 44, 'Tues · Thu · Sat']]),
    10: dict(cast=[['img', 'lucy', 33, 60], ['img', 'bust', 67, 54]], cabinet=True),
    11: dict(sea=True, cast=[['img', 'benedict', 28, 60], ['ship', '', 64, 52]]),
    12: dict(lights=True, bow=True, cast=[['img', 'angel1', 12, 50], ['img', 'agatha', 28, 50], ['img', 'rosalia', 50, 58],
                                         ['img', 'lucy', 70, 56], ['img', 'joseph', 81, 58], ['img', 'angel1m', 90, 50]]),
    13: dict(curtain=True, cast=[]),
}
CAB = {4: 'Agatha’s body · Catania', 5: 'Rosalia’s bones · Palermo', 6: 'Mary’s hair · Messina', 10: 'Lucy’s body · Venice, or Metz',
       'louis': 'Louis IX’s insides · Monreale'}
CAB_ORDER = [4, 5, 6, 10, 'louis']   # the order a reader meets them
# What each drawer holds, shown in the cabinet pop-up (our words; sources in the acts). z = a zoom picture key, once cleared.
CAB_INFO = {
    4: ('Most of her bones, in a jewelled silver bust of 1376, carried through Catania on her feast days. The jewels are '
        'gifts left over the centuries.', 'bust'),
    5: ('Bones found in a cave in 1624 and credited with ending the plague; they ride in a silver urn.', 'urn'),
    6: ('A lock of hair said to be Mary’s, kept in a small gold case and carried on the June float. Messina gave one hair '
        'to Palmi, across the strait, for its help in a plague; this is Palmi’s case.', 'capello'),
    10: ('Claimed whole by two cities at once. In Venice she lies under glass, face hidden by a silver mask; at the far end '
         'her bare, dried feet show. Syracuse, where she was buried, keeps the empty tomb.', 'lucybody'),
    'louis': ('The French king died on crusade in 1270; his entrails were buried here, his bones went to Paris. Whether the '
              'entrails are still in this tomb is not settled.', 'louis'),
}

# ---------- sections html ----------
def section_html(s):
    n, t = s['num'], s['title']
    night = ' night' if n in (8, 9) else ''
    if n == 0:
        ACTS = '<nav aria-label="Acts"><ul class="acts">' + ''.join(
            f'<li><a href="#s{k}">{v.split(" · ")[0].replace(" (night)", "")}</a></li>'
            for k, v in sorted(ACT_NAMES.items()) if v.startswith('Act ')) + '<li><a href="#s13">Sources</a></li></ul></nav>'
        return f'''<header class="sec hero" id="s0" data-scene="0">
<div class="card"><p class="kicker">A show in eight acts</p><h1 class="herotitle">Saints <span class="amp">&amp;</span> Spells</h1><p class="dek">A friendly guide to Sicily’s saints, spells and the stories outsiders tell about them,
checked claim by claim.</p>
<p class="byline">By Bryan Murphy · November 22, 2026</p>
{ACTS}<p class="howto">Scroll, and the stage changes with each act. Underlined words and names open a short note. Point at or tap a puppet to see where it comes from, and click a painting or statue to see it up close. Red stamps are
myth-checks.</p></div></header>'''
    if n == 13:
        return ''
    act = re.match(r'(Act \d+)(?: \(night\))? · (.*)', t)
    if act:
        h = f'<p class="kicker">{act.group(1)}{" · night" if night else ""}</p><h2>{inline(act.group(2))}</h2>'
    else:
        h = f'<h2>{inline(t)}</h2>'
    cab = f' data-cabinet="{html.escape(CAB[n])}"' if n in CAB else ''
    inner, open_beat, beat_scene = [], False, n
    for b in s['blocks']:
        m = re.match(r'\{\{BEAT:(\d+)\}\}$', b) or re.match(r'\{\{CAB:(\w+)\}\}$', b)
        if m and b.startswith('{{CAB'):
            if open_beat:
                inner.append('</div>')
            inner.append(f'<div class="beat" data-scene="{beat_scene}" data-cabinet="{html.escape(CAB[m.group(1)])}">'); open_beat = True
        elif m:
            beat_scene = m.group(1)
            if open_beat:
                inner.append('</div>')
            inner.append(f'<div class="beat" data-scene="{m.group(1)}">'); open_beat = True
        else:
            inner.append(b)
    if open_beat:
        inner.append('</div>')
    return (f'<section class="sec{night}" id="s{n}" data-scene="{n}"{cab}><div class="card">{h}'
            + '\n'.join(inner) + '</div></section>')

ACT_NAMES = {s['num']: s['title'] for s in SECS}

def clean_src(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', t)
    return t.replace('**', '')

def sources_html():
    out = ['<section class="sec" id="s13" data-scene="13"><div class="card"><h2>About these numbers</h2>',
           '''<p>Every number on this page comes from a table of checked figures. The research ran as many independent
passes (different searches, different sources) whose results were cross-checked against each other: each figure
needed two independent sources, preferably the original institution, book or journal. Where sources disagree, the
page shows a range or names the disagreement: 1071–72 for Palermo’s fall, “about 1040” for Agatha’s removal, about
6,000 to 7,000 people tried, 25 to 52 executions.</p>
<p>“Dozens tried” for the <i>donne di fuora</i> is deliberate: counts run from 65 to 77 to 193, depending on what is
counted (people in the surviving reports, one historian’s charges of contact with the dead, perhaps every woman named).
Counts that come from a single document name that document in the sentence: Pitrè’s survey, the Sicilian Region’s
2013 register, Pitrè’s tally of painted tablets, Napoli’s worm-charmers, the collectors in Intorre’s study, Palermo
Cathedral’s 17 reliquaries. The relic drawers are what the sources report, not an inventory; “two claims” for Lucy’s
body and head is our own comparison. No survey of evil-eye belief in Sicily turned up, so the page says nothing about
how many Sicilians hold it today. Beliefs are written as beliefs.</p>
<p>The myth-check stamps mark claims that circulate widely and that the record does not support. A stamp means
“no evidence found”, never “proven false”, unless it says so.</p>''',
           '<h2 id="sources">Sources</h2><p class="small">By act, as recorded in the checked figures table. “Via” means the '
           'source was read as cited by the next one; “lead” means a source used to find others, not to settle a figure.</p>']
    for s in SECS:
        if not s['ids'] or s['num'] in (0, 13):
            continue
        items = []
        for i in s['ids']:
            for piece in re.split(r';\s+(?![^()]*\))', SRC.get(i, '')):
                piece = piece.strip().rstrip('.')
                if piece and piece not in items:
                    items.append(piece)
        if items:
            out.append(f'<h3>{inline(s["title"])}</h3><ul class="src">' +
                       ''.join(f'<li>{clean_src(x)}</li>' for x in items) + '</ul>')
    out.append('<h3>Pictures</h3><ul class="src">' + ''.join(f'<li><b>{a}:</b> {b}</li>' for a, b in list(CREDITS.values()) + list(FIG_CREDITS.values())) +
               '<li><b>Drawn for this page:</b> the scholars’ and rulers’ placards, the boat, the letter, the table, the ship, '
               'the blue glass eye charm, the coral horn charm, the fortune-teller costume, the Paris occultist and the tarot cards. No open-licensed picture of Antonio of Noto is shown.</li>' + ''.join(f'<li><b>Portrait of {a}:</b> {b}</li>' for a, b in PORTRAITS.values()) +
               '</ul>')
    out.append('<h3>Type</h3><p class="small">Gloock (display) and Literata (text), both under the SIL Open Font License.</p>')
    out.append('<p class="small">Made with ProofEr. Research and drafting by Claude for Bryan Murphy, November 2026.</p></div></section>')
    return ''.join(out)

body = '\n'.join(section_html(s) for s in SECS) + sources_html()

tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template.html'), encoding='utf-8').read()
for n, sc in SCENES.items():
    t = ACT_NAMES.get(n, '')
    m2 = re.match(r'(Act \d+)(?: \(night\))? · ([^:]+)', t)
    sc['title'] = (f'{m2.group(1)} · {m2.group(2)}' if m2 else
                   {0: 'Saints & Spells', 1: 'Overture', 14: 'Overture', 15: 'Overture', 16: 'Act 6 · Witches & healers', 17: 'Act 6 · Witches & healers', 2: 'The goddess story', 3: 'Sicily 101', 12: 'Curtain call', 13: 'Sources'}.get(n, ''))
    sc['title'] = {7: 'Act 4 · St Joseph', 10: 'Act 7 · Relics', 11: 'Act 8 · Americas'}.get(n, sc['title'])
CALL_DATA = {k: dict(v, text=inline(v['text']), sub=inline(v['sub'])) for k, v in CALLOUT.items()}
CAB_DATA = [dict(label=CAB[k], note=CAB_INFO[k][0], z=CAB_INFO[k][1]) for k in CAB_ORDER]
STAGE_CREDITS = {k: (PORTRAITS[k][0], PORTRAITS[k][1] + ' Cut out for the stage.') for k in STAGE_PEOPLE}
ALL_CREDITS = {**CREDITS, **FIG_CREDITS, **STAGE_CREDITS}
data = dict(cab=CAB_DATA, callouts=CALL_DATA, imgs=IMGS, zoom=ZOOM, thumbs=THUMBS, names={k: v[0] for k, v in ALL_CREDITS.items()}, credits={k: v[1] for k, v in ALL_CREDITS.items()}, scenes=SCENES)
page = (tpl.replace('{{BODY}}', body)
           .replace('{{FRAME}}', FRAME).replace('{{TILE}}', TILE)
           .replace('{{DATA}}', json.dumps(data, ensure_ascii=False)))
out = os.path.join(ROOT, OUT)
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(page)
print('wrote', OUT, f'{len(page) / 1e6:.2f} MB')

if EMBED_FONTS:
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import importlib
    ef = importlib.import_module('embed_fonts')
    ef.HTML_IN, ef.HTML_OUT = out, out
    try:
        ef.main()
        print('fonts embedded', f'{os.path.getsize(out) / 1e6:.2f} MB')
    except Exception as exc:
        existing = os.path.join(ROOT, 'pieces', 'sicilian-folk-magic.html')
        m = re.search(r'<style>\s*/\* Fonts from Google Fonts.*?</style>', open(existing, encoding='utf-8').read(), re.S) if os.path.exists(existing) else None
        if not m:
            raise RuntimeError(f'Font embedding failed ({exc}) and no cached font block found in {existing}') from exc
        txt = open(out, encoding='utf-8').read()
        txt = ef.CSS_LINK.sub(lambda _: m.group(0), txt)
        txt = ef.PRECONNECT.sub('', txt)
        open(out, 'w', encoding='utf-8').write(txt)
        print('reused embedded fonts from existing pieces/sicilian-folk-magic.html (offline fallback):', f'{os.path.getsize(out) / 1e6:.2f} MB')
