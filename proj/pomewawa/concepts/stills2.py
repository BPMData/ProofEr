# Round 2: direction B (field guide, to scale) with A's punch. Two palettes. Only checked figures.
W, H = 1600, 900
PW, PH = 390, 800
SANS = "'Arial Narrow','Helvetica Neue',Arial,sans-serif"
BODY = "Helvetica,Arial,sans-serif"
SERIF = "Georgia,'Times New Roman',serif"
def t(x, y, s, size, fill, weight=400, anchor="start", family=BODY, extra=""):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'
def phone(x, inner, bg):
    return (f'<g transform="translate({x},50)"><rect x="-12" y="-12" width="{PW+24}" height="{PH+24}" rx="46" fill="#000"/>'
            f'<clipPath id="c{x}"><rect width="{PW}" height="{PH}" rx="36"/></clipPath>'
            f'<g clip-path="url(#c{x})"><rect width="{PW}" height="{PH}" fill="{bg}"/>{inner}</g></g>')
def stamp(x, y, top, mid, bot, acc, ink, rot=-5, w=300):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><rect x="{-w/2}" y="-50" width="{w}" height="96" fill="none" stroke="{acc}" stroke-width="4"/>'
            + t(0, -20, top, 16, acc, 900, "middle", SANS, 'letter-spacing="3"') + t(0, 6, mid, 15, ink, 400, "middle", SERIF)
            + t(0, 32, bot, 17, acc, 900, "middle", SANS) + '</g>')

def screens(ink, bg, acc, dim, rule):
    # Screen 1: hero + to-scale plate
    s1 = (t(26, 62, "PLATE I · DRAWN TO SCALE", 13, acc, 900, family=SANS, extra='letter-spacing="2"') +
          t(26, 125, "TINY.", 54, ink, 900, family=SANS, extra='letter-spacing="-1"') +
          t(26, 180, "ANCIENT.", 54, ink, 900, family=SANS, extra='letter-spacing="-1"') +
          t(26, 235, "UNBOTHERED.", 54, acc, 900, family=SANS, extra='letter-spacing="-1"') +
          t(26, 292, "The Pomewawa: Pomeranian × Chihuahua.", 16, dim) +
          t(26, 314, "Every number checked.", 16, dim))
    base, s = 700, 7
    for cm in (0, 10, 20, 30, 40, 50):
        yy = base - cm*s
        s1 += f'<line x1="26" y1="{yy}" x2="{PW-26}" y2="{yy}" stroke="{rule}" stroke-width="1"/>' + t(26, yy-4, f"{cm}", 11, dim)
    for x, hcm, lab, sub in ((80, 49, "Wolfspitz", "the cousin"), (230, 22, "Pomeranian", "")):
        h = hcm*s
        s1 += f'<rect x="{x}" y="{base-h}" width="110" height="{h}" fill="{ink if hcm==22 else "none"}" stroke="{ink}" stroke-width="2"/>'
        s1 += t(x, base-h-10, f"{hcm} cm", 30, acc if hcm == 22 else ink, 900, family=SANS)
        s1 += t(x, base+24, lab, 15, ink, 700) + (t(x, base+43, sub, 13, dim) if sub else "")
    s1 += t(26, 772, "Height at the shoulder (cm), FCI standard 97. Same breed standard.", 11, dim)
    # Screen 2: lifespan bars (zero baseline) + myth stamp + Titanic
    s2 = (t(26, 62, "PLATE IV · HOW LONG THEY LAST", 13, acc, 900, family=SANS, extra='letter-spacing="2"') +
          t(26, 120, "OUTLIVES THE", 44, ink, 900, family=SANS) + t(26, 166, "BIG GUY.", 44, ink, 900, family=SANS) +
          t(26, 196, "Typical age at death, UK, 584,734 dogs (2024).", 14, dim))
    scale = 22  # px per year; 0 baseline at x=26
    for y, yrs, lab, hot in ((240, 11.8, "Chihuahua", True), (318, 8.1, "Cane Corso", False)):
        s2 += f'<rect x="26" y="{y}" width="{yrs*scale}" height="40" fill="{acc if hot else dim}"/>'
        s2 += t(26 + yrs*scale + 8, y+30, f"{yrs}", 30, acc if hot else ink, 900, family=SANS)
        s2 += t(26, y+60, lab, 14, ink, 700)
    s2 += t(26, 404, "0 years at the left edge.", 11, dim)
    s2 += t(26, 440, "(The Corso does win the fight. We checked.)", 15, ink, 400, family=SERIF, extra='font-style="italic"')
    s2 += stamp(PW/2, 545, "MYTH CHECK", "“Aztec dogs were hot-water bottles”", "NO OLD RECORD BACKS IT", acc, ink)
    s2 += (f'<line x1="26" y1="630" x2="{PW-26}" y2="630" stroke="{rule}" stroke-width="1"/>' +
           t(26, 690, "2 of 3", 54, acc, 900, family=SANS) + t(205, 668, "dogs that survived", 16, ink, 700) +
           t(205, 690, "the Titanic were", 16, ink, 700) + t(205, 712, "Pomeranians.", 16, ink, 700) +
           t(26, 745, "1912 · Liverpool Museums, Encyclopedia Titanica", 11, dim))
    return s1, s2

def build(name, title, lines, pal, page_bg):
    ink, bg, acc, dim, rule = pal
    s1, s2 = screens(ink, bg, acc, dim, rule)
    side = f'<text x="980" y="200" font-family="{BODY}" font-size="52" font-weight="800" fill="#222">{title}</text>'
    for k, ln in enumerate(lines):
        side += f'<text x="980" y="{290+k*52}" font-family="{BODY}" font-size="32" fill="#333">{ln}</text>'
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{page_bg}"/>'
           + phone(60, s1, bg) + phone(500, s2, bg) + side + '</svg>')
    open(f"concept-{name}.svg", "w").write(svg)

build("B2a", "B+ Paper", ["Field-guide paper,", "fight-poster type.", "Hot red-orange accent.", "Prints cleanly."],
      ("#211C17", "#F3ECDD", "#C2350F", "#5F5649", "#D8CDB8"), "#E4DBCA")
build("B2b", "B+ Night", ["Same plates,", "dark paper.", "Orange from A.", "Loudest on a phone."],
      ("#F4EFE6", "#16130F", "#FF6A2B", "#A9A091", "#3A342C"), "#E4DBCA")
print("ok")
