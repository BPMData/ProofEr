# Stills critique (Nov 23, 2026)

`stills.html` holds three frames at real size: phone hero 390 × 844, phone Act 6 at night 390 × 844, desktop Act 1
1440 × 900. Puppets are drawn stand-ins; copy is draft.

**Not done:** no PNG captures. This environment has no browser, and installing one was refused, so the frames were
not looked at as images. The drawing code was run against a stub canvas at several times (no errors) and the script
passes a syntax check. The build gate wants a PNG and an inspection: capture the three frames (Bryan's screenshot or
a session with a browser) before `pieces/`.

**Contrast (WCAG, computed from the tokens):** body ink on plaster 15.5:1; byline 7.8; gloss blue 7.9; stamp red on
its paper 6.7; night body 14.5; night gloss 9.6; candle gold 12.0; chart caption 9.3; ink on gold 7.7; ribbon 8.4.
All pass AA, most pass AAA.

**Self-checks:**
- Puppets ride visible sticks through a slot in the stage floor (Bryan, Nov 23); the hand rod is visible too.
- Color never carries meaning alone: the chart's range is hatched as well as dimmer; magic squares are labeled.
- Unit chart is to scale: 600 solid + 100 hatched squares at 10 people each (6,000–7,000), 100 gold (about 1,000);
  executions at one dot per person, 25 solid + 27 open (25–52). Units differ, so the strip has its own label.
- Red is used only for myth-check stamps.
- Risks to watch at build: the phone stage (470 px) takes over half the screen on short phones; shrink to about 40%
  of the viewport. The relic cabinet is tiny on phones; it needs a tap target of 44 px. Gloock is single-weight, so
  the stamp's second line uses Literata.

## Nov 23: hero-phone.png (drawn from the real cutouts)
Still the HTML stills can't be screenshotted here, so `build/make_mockup.py` draws the phone hero (390 × 844 at 2x)
with PIL from Bryan's artworks: the Met's gilt ripple frame as the proscenium, Houël's car of Rosalia as a faded
backdrop flat, the bronze Agatha on a wooden stick with a hand rod, Gloock title ribbon, Literata card. Inspected.
- **Works:** the frame makes the stage instantly a theatre; the stick and rod read as a puppet; the ribbon and card
  type are sharp and comfortably sized; the tile wall stays quiet behind the text.
- **Fix in the build:** at phone width the real frame's border eats ~45% of the stage, so draw it as a CSS
  border-image at about 40% of its thickness; give the floor a plank texture; let the backdrop flat change per act.
- **Sensitivity:** the bronze Agatha is bare-breasted (her martyrdom iconography); fine for adult readers, credited.
