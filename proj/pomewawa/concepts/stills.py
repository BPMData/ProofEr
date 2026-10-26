# Builds three concept stills (SVG, 1600x900): two phone screens each. Only checked figures from figures.md.
W, H = 1600, 900
PW, PH = 390, 800          # phone screen (scaled ~ iPhone 390x844)
def phone(x, inner, bg):
    return (f'<g transform="translate({x},50)"><rect x="-12" y="-12" width="{PW+24}" height="{PH+24}" rx="46" fill="#000"/>'
            f'<clipPath id="c{x}"><rect width="{PW}" height="{PH}" rx="36"/></clipPath>'
            f'<g clip-path="url(#c{x})"><rect width="{PW}" height="{PH}" fill="{bg}"/>{inner}</g></g>')
def svg(body, bg, caption):
    title, lines = caption
    out = f'<text x="980" y="200" font-family="Helvetica,Arial,sans-serif" font-size="52" font-weight="800" fill="#222">{title}</text>'
    for k, ln in enumerate(lines):
        out += f'<text x="980" y="{290+k*52}" font-family="Helvetica,Arial,sans-serif" font-size="32" fill="#333">{ln}</text>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{bg}"/>{body}{out}</svg>')
def t(x, y, s, size, fill, weight=400, anchor="start", family="Helvetica,Arial,sans-serif", extra=""):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'

# ---------- A: Fight card ----------
ink, bg, acc, dim = "#F4EFE6", "#121212", "#FF6A2B", "#A9A39A"
cond = "'Arial Narrow','Helvetica Neue',Arial,sans-serif"
a1 = (t(30, 70, "TONIGHT · ONE ROUND · ALL NUMBERS CHECKED", 13, acc, 700, family=cond) +
      t(30, 175, "POMEWAWA", 50, ink, 900, family=cond, extra='letter-spacing="-2"') +
      t(30, 225, "Pomeranian × Chihuahua", 17, dim) +
      t(PW/2, 330, "VS", 64, acc, 900, "middle", cond) +
      t(30, 435, "CANE CORSO", 50, ink, 900, family=cond, extra='letter-spacing="-2"') +
      t(30, 485, "The big guy", 17, dim) +
      f'<rect x="30" y="560" width="{PW-60}" height="2" fill="{acc}"/>' +
      t(30, 610, "Spoiler: the Corso wins the fight.", 22, ink, 700) +
      t(30, 645, "The little guy wins the rest.", 22, ink, 400) +
      t(30, 740, "Scroll for the tale of the tape ↓", 16, dim))
rows = [("TYPICAL LIFESPAN", "11.8 yrs", "8.1 yrs", "Chihuahua vs Cane Corso, UK, 584,734 dogs (2024)", "L"),
        ("BITE FORCE", "—", "“700 PSI”", "No study ever measured it. That number is internet lore.", "MYTH"),
        ("PICKS FIGHTS WITH STRANGERS", "top tier", "—", "Chihuahuas, owner survey, 30+ breeds (2008)", "L"),
        ("FIGHT", "loses", "wins", "We're not cowards here.", "R")]
a2 = t(30, 60, "TALE OF THE TAPE", 30, ink, 900, family=cond) + t(36, 92, "POMEWAWA", 14, dim, 700, family=cond) + t(PW-36, 92, "CANE CORSO", 14, dim, 700, "end", cond)
y = 140
for lab, l, r, note, win in rows:
    a2 += f'<rect x="20" y="{y-30}" width="{PW-40}" height="148" rx="10" fill="#1E1E1E"/>'
    a2 += t(36, y, lab, 14, dim, 700, family=cond)
    a2 += t(36, y+52, l, 38, acc if win == "L" else ink, 900, family=cond)
    a2 += t(PW-36, y+52, r, 38, acc if win == "R" else ink, 900, "end", cond)
    if win == "MYTH":
        a2 += f'<g transform="translate({PW-90},{y-8}) rotate(-8)"><rect x="-52" y="-22" width="104" height="36" fill="none" stroke="{acc}" stroke-width="3"/>' + t(0, 5, "MYTH", 22, acc, 900, "middle", cond) + '</g>'
    a2 += t(36, y+90, note, 13, dim)
    y += 165
A = svg(phone(60, a1, bg) + phone(500, a2, bg), "#E9E4DA", ("A. Fight card", ["Fight-night poster.", "Pomewawa vs Cane Corso,", "a tale of the tape.", "Loud, deadpan, sporty.", "", "Avoids: cute, pastel."]))

# ---------- B: Field guide plate ----------
ink, bg, acc, dim = "#2A2520", "#F2EBDD", "#8C2F1B", "#6E655A"
serif = "Georgia,'Times New Roman',serif"
s = 8  # px per cm
base = 690
b1 = (t(28, 64, "PLATE I", 14, acc, 700, extra='letter-spacing="3"') +
      t(28, 120, "A big dog,", 44, ink, 700, family=serif) + t(28, 168, "shrunk on purpose.", 44, ink, 700, family=serif, extra='font-style="italic"') +
      t(28, 210, "Same breed standard, two sizes. Drawn to scale.", 16, dim))
# ruler
for cm in range(0, 51, 10):
    yy = base - cm*s
    b1 += f'<line x1="28" y1="{yy}" x2="44" y2="{yy}" stroke="{ink}" stroke-width="1.5"/>' + t(50, yy+5, f"{cm} cm", 12, dim)
b1 += f'<line x1="36" y1="{base}" x2="36" y2="{base-50*s}" stroke="{ink}" stroke-width="1.5"/>'
def dog(x, hcm, label, sub):
    h = hcm*s; w = 100
    return (f'<rect x="{x}" y="{base-h}" width="{w}" height="{h}" fill="none" stroke="{ink}" stroke-width="2" stroke-dasharray="4 4"/>'
            f'<line x1="{x}" y1="{base-h}" x2="{x+w}" y2="{base-h}" stroke="{acc}" stroke-width="3"/>' +
            t(x, base-h-12, f"{hcm} cm", 18, acc, 700) + t(x, base+28, label, 15, ink, 700) + t(x, base+48, sub, 13, dim))
b1 += dog(130, 49, "Wolfspitz", "the cousin") + dog(260, 22, "Pomeranian", "")
b1 += f'<line x1="20" y1="{base}" x2="{PW-20}" y2="{base}" stroke="{ink}" stroke-width="1"/>'
b1 += t(28, 770, "Height at the shoulder, FCI standard 97.", 12, dim)
b2 = t(28, 64, "PLATE II", 14, acc, 700, extra='letter-spacing="3"') + t(28, 112, "A short history", 34, ink, 700, family=serif)
ev = [("1520", "Cortés sees “little dogs” sold for eating in the Aztec market."),
      ("c.1777", "Gainsborough paints a Pomeranian and her puppy."),
      ("1900", "The AKC recognizes the Pomeranian."),
      ("1904", "…and the Chihuahua. First one registered: “Midget.”"),
      ("1912", "Titanic sinks. 3 dogs survive. 2 are Pomeranians.")]
y = 175
b2 += f'<line x1="98" y1="150" x2="98" y2="590" stroke="{ink}" stroke-width="1.5"/>'
for yr, txt in ev:
    b2 += f'<circle cx="98" cy="{y-6}" r="6" fill="{acc}"/>' + t(84, y, yr, 17, ink, 700, "end", serif)
    words, line, lines = txt.split(), "", []
    for wd in words:
        if len(line + wd) > 30: lines.append(line); line = ""
        line += wd + " "
    lines.append(line)
    for k, ln in enumerate(lines): b2 += t(116, y + k*21, ln.strip(), 16, ink)
    y += 88
b2 += (f'<g transform="translate({PW/2},690) rotate(-4)"><rect x="-165" y="-48" width="330" height="92" fill="none" stroke="{acc}" stroke-width="3"/>' +
       t(0, -18, "MYTH CHECK", 15, acc, 700, "middle", extra='letter-spacing="3"') +
       t(0, 8, "“Aztec dogs were hot-water bottles”", 15, ink, 400, "middle", serif) +
       t(0, 32, "No old record backs it.", 15, acc, 700, "middle") + '</g>')
B = svg(phone(60, b1, bg) + phone(500, b2, bg), "#E3DACA", ("B. Field guide", ["Old naturalist plates", "with modern data.", "Everything to scale.", "Dry, smart, curious.", "", "Avoids: meme noise."]))

# ---------- C: Case file ----------
ink, bg, acc, dim = "#1F2328", "#E6E2D3", "#B3261E", "#5A5F66"
mono = "'Courier New',Courier,monospace"
c1 = (f'<rect x="0" y="0" width="{PW}" height="92" fill="#C9C2A8"/>' + t(24, 56, "CASE FILE № 1520-A", 22, ink, 700, family=mono) +
      t(24, 150, "SUBJECT:", 15, dim, 700, family=mono) + t(24, 200, "THE POMEWAWA", 40, ink, 700, family=mono) +
      t(24, 260, "Known aliases:", 15, dim, 700, family=mono) + t(24, 288, "Techichi (alleged)", 16, ink, family=mono) +
      t(24, 340, "Height:", 15, dim, 700, family=mono) + t(24, 368, "shin-level", 16, ink, family=mono) +
      t(24, 420, "Ancestry:", 15, dim, 700, family=mono) + t(24, 448, "ancient Mexican dogs,", 16, ink, family=mono) +
      t(24, 470, "mother's side (mtDNA)", 16, ink, family=mono) +
      f'<g transform="translate({PW/2},600) rotate(-10)"><rect x="-150" y="-40" width="300" height="80" fill="none" stroke="{acc}" stroke-width="4"/>' +
      t(0, 12, "SMALL. ARMED.", 30, acc, 700, "middle", mono) + '</g>')
c2 = (t(24, 60, "PRIOR RECORD", 26, ink, 700, family=mono) + f'<line x1="24" y1="76" x2="{PW-24}" y2="76" stroke="{ink}"/>')
items = [("1520", "Sold as food, Aztec market.", "Cortés, Second Letter"),
         ("2008", "Top tier for biting, or trying", "to, with strangers.", "Duffy et al., owner survey"),
         ("2013", "Shorter breed = more snapping,", "barking. 8,301 dogs, 49 breeds.", "McGreevy et al."),
         ("2024", "Outlives a Cane Corso:", "11.8 years vs 8.1.", "McMillan et al., 584,734 dogs")]
y = 130
for it in items:
    c2 += t(24, y, it[0], 18, acc, 700, family=mono)
    for k, ln in enumerate(it[1:-1]): c2 += t(100, y + k*22, ln, 15, ink, family=mono)
    c2 += t(100, y + (len(it)-2)*22 + 6, it[-1], 12, dim, family=mono)
    y += 120
c2 += t(24, 640, "EVIDENCE REJECTED:", 15, dim, 700, family=mono) + t(24, 668, "“743 PSI Kangal bite”", 16, ink, family=mono)
c2 += f'<line x1="20" y1="663" x2="250" y2="663" stroke="{acc}" stroke-width="3"/>' + t(24, 694, "never measured. Internet lore.", 14, acc, family=mono)
C = svg(phone(60, c1, bg) + phone(500, c2, bg), "#D8D3C2", ("C. Case file", ["Police rap sheet on", "a tiny suspect.", "Priors, aliases, evidence.", "Deadpan, funny, nosy.", "", "Avoids: sappy dog-mom."]))

for name, s_ in (("A", A), ("B", B), ("C", C)):
    open(f"concept-{name}.svg", "w").write(s_)
print("ok")
