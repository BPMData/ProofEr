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
from PIL import Image

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

CREDITS = {
    'rosalia': ('Saint Rosalia', 'Anthony van Dyck, <i>Saint Rosalie Interceding for the Plague-stricken of Palermo</i>, 1624 (detail). The Met, 71.41. CC0.'),
    'float': ('Rosalia’s car', 'Jean Houël, <i>The car of Saint Rosalia</i>, aquatint, 1780s. Wellcome Collection, 7145i. Public Domain Mark.'),
    'agatha': ('Saint Agatha', '<i>Saint Agatha</i>, bronze statuette, Italian (probably Naples), mid-17th c. The Met, 197071. CC0.'),
    'bust': ('A reliquary bust', '<i>Reliquary Bust of Saint Juliana</i>, circle of Giovanni di Bartolo, c. 1376. The Met, 61.266. CC0. A stand-in: Agatha’s own bust in Catania is by Giovanni di Bartolo.'),
    'lucy': ('Saint Lucy', 'Francisco de Zurbarán, <i>Saint Lucy</i>, c. 1625/30. National Gallery of Art, 1943.7.11. Public domain.'),
    'joseph': ('Saint Joseph', '<i>St. Joseph</i>, crèche figure, attributed to Salvatore di Franco, Naples, 2nd half 18th c. The Met, 64.164.3a–c. CC0.'),
    'goddess': ('A goddess', 'Terracotta bust (Persephone or Demeter), Greek, made in Sicily, 4th c. BCE. The Met, 1994.600.1–.2. CC0.'),
    'isis': ('Isis', '<i>Statuette of Isis nursing Horus</i>, Egyptian, Late Period, 664–332 BCE. The Met, 553002. CC0.'),
    'albarello': ('A Palermo jar', '<i>Albarello</i> (pharmacy jar), Lazzaro workshop, Palermo, 2nd half 16th c. The Met, 188537. CC0. Its foliage also makes the tile wall.'),
    'frame': ('The proscenium', 'Gilt ripple frame, Sicilian(?), late 17th c. The Met, 1975.1.2326. CC0.'),
    'exvoto': ('An ex-voto', 'Ex-voto: a man falls in a Roman street while his wife prays to Sansovino’s Virgin and Child, 27 May 1851. Rome, not Sicily. Wellcome Collection, 44879i. Public Domain Mark.'),
    'angel1': ('An angel', '<i>Angel</i>, crèche figure, Naples, 2nd half 18th c. The Met (crèche angels, 64.164). CC0.'),
}
IMGS = {k: webp(k) for k in CREDITS if k not in ('frame', 'float', 'exvoto')}
IMGS['float'] = webp('float', 520)
IMGS['exvoto'] = webp('exvoto', 520)
IMGS['angel1m'] = webp('angel1', mirror=True)
FRAME = webp('frame', 640)
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
              'Copy supplied by Bryan from Sicilian Post.'),
    'gramsci': ('Antonio Gramsci', 'Photograph by an unknown photographer, about 1922. Public domain by age. Copy supplied by '
                'Bryan from Wikimedia Commons (File:Gramsci.png).'),
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
        ('Lucy’s whole body', [('Venice', 'claim', ''), ('Metz', 'claim', ''), ('Syracuse', 'empty', 'the original tomb, empty')], 'Our count: two claims, Venice and Metz.'),
        ('Lucy’s head', [('Venice', 'synth', ''), ('Bourges', 'synth', '')], 'Our own comparison of two separate reports.'),
        ('Agatha', [('Catania', 'claim', 'the body'), ('Palermo', 'claim', 'her arm'), ('31 places', 'synth', 'outside Catania, per one tourism list')], 'Spread, not doubled.'),
        ('Louis IX', [('Monreale', 'claim', 'entrails'), ('Monreale?', 'synth', 'heart, by one medieval account'), ('Saint-Denis?', 'synth', 'heart, says Le Goff')], 'The heart is disputed.'),
        ('Rosalia', [('Palermo', 'claim', 'the bones, in a silver urn')], ''),
        ('Mary’s hair', [('Messina', 'claim', 'with the Letter')], ''),
    ]
    out = ['<figure class="chart cabinet" aria-labelledby="cab-cap"><div class="drawers">']
    for name, ds, note in groups:
        out.append(f'<div class="dgroup"><h3>{name}</h3><div class="drow">')
        for place, kind, sub in ds:
            out.append(f'<div class="drawer {kind}"><b>{place}</b>{f"<small>{sub}</small>" if sub else ""}</div>')
        out.append(f'</div>{f"<p>{note}</p>" if note else ""}</div>')
    out.append('</div><figcaption id="cab-cap">The relic cabinet, opened: one drawer for each place that claims a relic '
               'met in this show, side by side when two places claim the same part. Plain drawers are claims the sources '
               'report; striped drawers rest on one source or on our own comparison; the dashed drawer is an empty tomb. '
               'Counts only, not an inventory.</figcaption></figure>')
    return ''.join(out)

def route_svg():
    return '''<figure class="chart route" aria-labelledby="route-cap">
<svg viewBox="0 0 360 300" role="img" aria-labelledby="route-t"><title id="route-t">Routes from Sicily, not to scale</title>
<path class="sea" d="M0 0h360v300H0z"/>
<path class="land" d="M250 40 l40 -6 l46 8 l10 30 l-30 22 l-26 -10 l-40 4 z"/>
<path class="land" d="M206 70 l18 -10 l14 6 l-6 24 l-20 4 z"/>
<path class="land" d="M40 150 l30 -10 l26 20 l-6 40 l-30 20 l-24 -16 z"/>
<path class="land" d="M10 60 l50 -10 l30 20 l-20 30 l-40 0 z"/>
<path class="island" d="M292 104 l22 -4 l14 3 l-10 14 l-16 3 z"/>
<path class="r1" d="M300 108 C 260 110, 240 80, 222 74"/>
<path class="r1" d="M222 74 C 170 110, 110 140, 74 170"/>
<path class="r1" d="M74 170 C 60 150, 50 120, 46 92"/>
<path class="r2" d="M300 112 C 240 200, 120 250, 40 236"/>
<circle class="cp" cx="304" cy="106" r="5"/><text x="300" y="132" class="ml">Sicily</text>
<circle class="cp" cx="222" cy="74" r="4"/><text x="200" y="58" class="ml">Lisbon, by 1609</text>
<circle class="cp" cx="74" cy="170" r="4"/><text x="80" y="192" class="ml">Brazil, early 1600s</text>
<circle class="cp" cx="46" cy="92" r="4"/><text x="14" y="44" class="ml">Venezuela: the drums</text>
<circle class="cp" cx="40" cy="236" r="4"/><text x="12" y="262" class="ml">New Spain: Rosalia;</text><text x="12" y="278" class="ml">Joseph patron, 1555</text>
<text x="350" y="292" class="nts" text-anchor="end">not to scale</text>
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
        i = next(k for k, b in enumerate(s['blocks']) if b.startswith('<p>What we did find'))
        s['blocks'].insert(i + 1, cabinet_html())
    if s['num'] == 11:
        i = next(k for k, b in enumerate(s['blocks']) if '<strong>Rosalia</strong>' in b)
        s['blocks'].insert(i + 1, route_svg())

# ---------- stage scenes ----------
# each puppet: [kind, key, x% (centre), height% of stage, extra]
SCENES = {
    0: dict(back='float', lights=True, cast=[['img', 'agatha', 22, 52], ['img', 'rosalia', 52, 60], ['img', 'lucy', 80, 60]]),
    1: dict(lights=True, cast=[['img', 'isis', 18, 56], ['img', 'goddess', 44, 50], ['img', 'agatha', 74, 62]], stamp='Myth-check: claim by claim'),
    2: dict(cast=[['card', 'Pitrè', 23, 36, 'Palermo · 1910'], ['card', 'Gramsci', 50, 40, 'prison notebooks'], ['card', 'de Martino', 77, 36, 'Sud e magia · 1959']]),
    3: dict(cast=[['card', '535', 23, 36, 'Byzantium'], ['card', '831', 50, 42, 'Arabs take Palermo'], ['card', '1071–72', 77, 36, 'Normans']]),
    4: dict(sea=True, cast=[['boat', 'bust', 58, 62], ['img', 'agatha', 22, 50]]),
    5: dict(back='float', cast=[['img', 'rosalia', 50, 64]]),
    6: dict(cast=[['letter', 'Messina · “AD 42”', 50, 56]]),
    7: dict(cast=[['img', 'joseph', 24, 70], ['table', '', 64, 40]]),
    8: dict(night=True, cast=[['print', 'exvoto', 50, 58]]),
    9: dict(night=True, cast=[['img', 'albarello', 22, 58], ['eye', '', 56, 40], ['horn', '', 82, 36]]),
    10: dict(cast=[['img', 'lucy', 26, 64], ['img', 'bust', 72, 56]], cabinet=True),
    11: dict(sea=True, cast=[['ship', '', 50, 56]]),
    12: dict(lights=True, bow=True, cast=[['img', 'angel1', 12, 50], ['img', 'agatha', 28, 50], ['img', 'rosalia', 50, 58],
                                         ['img', 'lucy', 70, 56], ['img', 'joseph', 81, 58], ['img', 'angel1m', 90, 50]]),
    13: dict(curtain=True, cast=[]),
}
CAB = {4: 'Agatha’s body · Catania', 5: 'Rosalia’s bones · Palermo', 6: 'Mary’s hair · Messina'}

# ---------- sections html ----------
def section_html(s):
    n, t = s['num'], s['title']
    night = ' night' if n in (8, 9) else ''
    if n == 0:
        ACTS = '<nav aria-label="Acts"><ul class="acts">' + ''.join(
            f'<li><a href="#s{k}">{v.split(" · ")[0].replace(" (night)", "")}</a></li>'
            for k, v in sorted(ACT_NAMES.items()) if v.startswith('Act ')) + '<li><a href="#s13">Sources</a></li></ul></nav>'
        return f'''<header class="sec hero" id="s0" data-scene="0">
<div class="ribbon"><h1>Saints <span class="amp">&amp;</span> Spells</h1></div>
<div class="card"><p class="dek">Under every saint in Sicily, the story goes, there’s a goddess wearing a disguise. We
put that story on stage and checked it, claim by claim: who said it first, and what the record shows.</p>
<p class="byline"><i>A show in eight acts</i><br>By Bryan Murphy · November 22, 2026</p>
{ACTS}<p class="howto">Scroll, and the stage changes with each act. Underlined words and names open a short note. Point at or tap a puppet to see where it comes from. Red stamps are
myth-checks.</p></div></header>'''
    if n == 13:
        return ''
    act = re.match(r'(Act \d+)(?: \(night\))? · (.*)', t)
    if act:
        h = f'<p class="kicker">{act.group(1)}{" · night" if night else ""}</p><h2>{inline(act.group(2))}</h2>'
    else:
        h = f'<h2>{inline(t)}</h2>'
    cab = f' data-cabinet="{html.escape(CAB[n])}"' if n in CAB else ''
    return (f'<section class="sec{night}" id="s{n}" data-scene="{n}"{cab}><div class="card">{h}'
            + '\n'.join(s['blocks']) + '</div></section>')

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
    out.append('<h3>Pictures</h3><ul class="src">' + ''.join(f'<li><b>{a}:</b> {b}</li>' for a, b in CREDITS.values()) +
               '<li><b>Drawn for this page:</b> the scholars’ and rulers’ placards, the boat, the letter, the table, the ship '
               'the blue glass eye charm and the coral horn charm. No open-licensed picture of Benedict the Moor or Antonio of Noto turned up, so '
               'they are not shown.</li>' + ''.join(f'<li><b>Portrait of {a}:</b> {b}</li>' for a, b in PORTRAITS.values()) +
               '<li><b>Ernesto de Martino:</b> no portrait. The photo we had came from a personal site with no photographer, '
               'date or licence, so we could not clear it.</li></ul>')
    out.append('<h3>Type</h3><p class="small">Gloock (display) and Literata (text), both under the SIL Open Font License.</p>')
    out.append('<p class="small">Made with ProofEr. Research and drafting by Claude for Bryan Murphy, November 2026.</p></div></section>')
    return ''.join(out)

body = '\n'.join(section_html(s) for s in SECS) + sources_html()

tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template.html'), encoding='utf-8').read()
for n, sc in SCENES.items():
    t = ACT_NAMES.get(n, '')
    m2 = re.match(r'(Act \d+)(?: \(night\))? · ([^:]+)', t)
    sc['title'] = (f'{m2.group(1)} · {m2.group(2)}' if m2 else
                   {0: 'Saints & Spells', 1: 'Overture', 2: 'Primer', 3: 'Who ruled Sicily', 12: 'Curtain call', 13: 'Sources'}.get(n, ''))
    sc['title'] = {7: 'Act 4 · St Joseph', 10: 'Act 7 · Relics', 11: 'Act 8 · Americas'}.get(n, sc['title'])
CALL_DATA = {k: dict(v, text=inline(v['text']), sub=inline(v['sub'])) for k, v in CALLOUT.items()}
data = dict(callouts=CALL_DATA, imgs=IMGS, names={k: v[0] for k, v in CREDITS.items()}, credits={k: v[1] for k, v in CREDITS.items()}, scenes=SCENES)
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
    ef.main()
    print('fonts embedded', f'{os.path.getsize(out) / 1e6:.2f} MB')
