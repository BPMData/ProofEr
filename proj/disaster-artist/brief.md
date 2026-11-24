# Brief: Disaster Artist (Van Gogh)

Status: APPROVED 2026-11-24 by Bryan (his own build brief, uploaded) · Stage: research · Mode: from scratch · Budget: standard · Client: Bryan · Sign-off: Bryan
Usage: Opus coordinator with Sonnet research workers (research + outline only in this pass)

_Bryan supplied the full build brief below, word for word as uploaded on 2026-11-24. It replaces the interview: format
(interactive data essay), audience, tone, aesthetic and depth are all fixed in it. Prose comes later via Gemini, so
this pass stops at the outline (brief §9 steps 1–2)._

## Decisions log
- 2026-11-24 · "Can you start a new agent to start the planning and building the rough outline of this? You don't need to do everything, it turned out we really needed to bring in gemini last time to get the writing style and tone right, but we can start the research parts and such." · Research, image sourcing and outline only; no essay prose in this pass.
- 2026-11-24 · "i also connected findanyphoto which is free for 50 searches so be strategic about them" · Find Any Photo used sparingly, only for period photographs.

---

# DISASTER ARTIST — a data essay about Vincent van Gogh

**Build brief for the executing agent. Read the whole file before researching. The user builds "data essays": single self-contained HTML files that read like longform magazine features and argue like papers. This brief fixes the thesis, the plot, the tone, the format, and the data. Your job is research, verification, writing in the specified voice, and hand-built implementation.**

---

## 0. The one-line brief

**Van Gogh is the canonical "disaster artist": a genuinely great painter and a genuinely great disaster, and the data shows the two were the same machine. Build a seven-chapter scrollytelling data essay that proves it — and lands the moral: you don't want to be a disaster artist.**

The essay's engine is a set of oppositions the charts make visible:

- ~900 paintings vs. effectively zero lifetime sales
- two paintings a week vs. one customer (his brother)
- a decade of genius vs. ~18,000 francs of subsidy
- 37 years vs. a century of posthumous price inflation from 400 francs to $82.5 million
- the beloveds who couldn't say no vs. the one town that could (petition: ~30 signatures, February 1889)

---

## 1. What a "data essay" is (the house format — follow it exactly)

The user has four existing essays in this exact format (Terezín/Vedem; Holocaust by country; Knife Country; Sicilian folk magic). They define the spec. Distilled:

**Delivery & tech**
- ONE `.html` file, plus an image asset tree committed to the user's GitHub repo (the repo is the archive and the host). Everything else inline: CSS, JS, fonts. No third-party requests at runtime — images load from the same repo via relative paths only, so the page works at any base path (GitHub Pages, a subfolder, wherever).
- Fonts: download open-license Google Fonts, base64-embed as `@font-face` woff2 (latin + latin-ext slices only). Variable fonts preferred.
- NO charting libraries. No d3, no GSAP, no CDN anything. All charts are hand-built inline SVG (vanilla `createElementNS`), all scroll choreography is hand-rolled (`getBoundingClientRect` + `requestAnimationFrame` + IntersectionObserver). The existing essays ship 60–70KB of hand-written JS.
- Mobile breakpoints 375 / 768 / 1024 / 1440. Zero console errors and zero 404s are release gates.
- Accessibility is house style: visible `:focus-visible` (gold outline), `prefers-reduced-motion` degrades every scene to its final state, aria-pressed on segmented controls, dialogs closable three ways.

**Typography (house system)**
- Serif body (literary, high readability; ~19px, line-height ~1.6, measure ~36rem, max-width on paragraphs).
- Condensed grotesk display face (variable width axis strongly preferred) for kickers, H2s, stat numerals, buttons, captions.
- Kicker: uppercase, wide letter-spacing, ~0.78rem, 800 weight, red.
- H2: display face, 900 weight, condensed, clamp(2rem,6.4vw,3.6rem), tight leading.
- Footnotes: `<sup class="fn">` with links to a numbered `#sources` list at the end.
- Byline "By Bryan Murphy" and a date.

**Palette (house tokens, reuse these exact values)**
```
--paper:#F2EDE3; --paper2:#E9E1CF; --ink:#1B1A17; --mute:#5C564C; --rule:#C9C0AE;
--red:#8E1C15; --red-ink:#B3261E; --gold:#E2B44B;
--iron:#33383D; --indigo:#1E2A57;
--onfield:#F4EFE6; --onfield-mute:#D9D2C4;
```
Per-essay signature: recolor "field" chapters (full-bleed dark/colored sections). This essay gets two new field colors derived from his palette: `--ochre:#B57708` (sunflower chapter) and keep `--indigo` (Starry Night chapter, with star specks as texture). Everything else stays on the house tokens.

**Signature mechanics (at least three of these must appear)**
1. **Sticky scrolly scenes**: a ~230vh wrapper, a sticky 100vh inner stage, scroll progress (0–1) drives chart state via rAF. Text captions swap in bands of progress.
2. **Sticky-figure story sections** (≥960px): two-column grid, text column beside a `position:sticky` chart that updates as the text scrolls.
3. **Specimen plates**: bordered "plates" containing interactive charts with segmented button controls (`aria-pressed`) and dynamic readouts.
4. **A persistent fixed UI toy** the user can tap at any time (see §3 — Theo's Ledger).
5. **Verdict stamps** (see §4): a rubber-stamp animation on demand.

**Buttons**: square, ink-on-paper, never pills; uppercase, letter-spaced, ≥44px min-height. `.btn` solid, `.btn.ghost` outlined.

---

## 2. Thesis and chapter plot

### Hero (paper)
- Kicker: `A DATA ESSAY IN SEVEN CHAPTERS`
- H1: **DISASTER ARTIST**
- Standfirst (in the house voice): the man painted roughly two canvases a week for a decade and sold effectively none of them; the essay asks why, and what the machine looked like from inside.
- Stat band (the house "big numbers" strip): `~900 paintings · 1 famous lifetime sale · 1 customer · ~30 petition signatures · ~800 letters · 37 years`
- 2–3 intro paragraphs with footnotes that set the thesis: greatness and disaster were not in tension — they were one process. The market didn't fail to see his value; the structure that prices value was absent from his life in a way the essay will enumerate.
- Signature detail: an SVG ornament of impasto-like arcs under the H1 that stroke-draws in on load (stroke-dashoffset animation, disabled under reduced-motion).
- Also introduce the ledger toy here: one line telling the reader the tab in the corner is Theo's ledger and it will keep score as they scroll.

### Chapter 1 — The Machine (paper): output vs. sales
- **Thesis beat**: he was not a slow-burn misunderstood genius in the romantic sense; he was a *production line*. The disaster is measurable: the two lines never meet.
- **First beat — the prequel gyre**: before the pencil, five dead careers. A horizontal timeline strip, 1869→1880, that the reader scrolls through while each career earns a red ✗ stamp as it dies: Goupil clerk (hired at sixteen through his uncle the partner — *the best launchpad in Europe*; fired 1876 for reading the Bible at the counter and proselytizing the customers) → schoolmaster in Ramsgate/Isleworth (1876) → bookshop clerk in Dordrecht (1877) → theology student in Amsterdam (a year cramming Latin and Greek; abandoned 1878) → lay preacher in the Borinage coal fields (dismissed 1879 for living like the miners and giving away his clothes). End of strip: 1880, the pencil — "the one career that didn't get him fired. It killed him instead." This is the first ring of the gyre and it must be funny; the reader should be laughing before they realize they're watching the origin of a disaster.
- **Sticky scene**: bar chart, paintings per year 1881–1890 (data in §6), bars growing with scroll; overlaid, a dead-flat dashed "lifetime sales" line pinned near zero with a single gold dot at 1890 (400 francs — *The Red Vineyard*). Caption bands: early years ("a painting every four days"), 1888 peak ("Arles: ~200 in fifteen months"), the flat line ("the market's answer, the whole way").
- Side text: the two-a-week pace, the impasto, the working conditions; footnote the catalogue-count caveat.

### Chapter 2 — The Subsidy (ochre field)
- **Thesis beat**: the texture everyone loves was financed. Theo wired 150–250 francs most months for a decade; the subsidy is the invisible co-author of the impasto.
- **Interactive plate**: a stipend calculator — slider for monthly francs (default 200), outputs decade total + honest conversions ("roughly a schoolmaster's wages, every year, for a decade" — hedge the modern-dollar conversions; see §7).
- Text: the wire-transfer loop; the detail that Goupil (the firm that fired Vincent in 1876) paid Theo's salary, so the employer that expelled him funded the paint. Footnote the estimate's basis (letters).

### Interlude — The Shopkeeper (paper, full-bleed plate)
- **The visual centerpiece of the essay.** A dedicated interlude built around *Portrait of Père Tanguy* (1887, Musée Rodin): the paint dealer seated serene in his smock before a wall of ukiyo-e — "the weebiest painting of the nineteenth century," a payment receipt, a dealer selfie, and a wall-scroll flex in one canvas.
- Presentation: full-width plate with the painting at generous size, plus two or three zoomed detail crops of the print wall behind him (each crop labeled — Hiroshige-derived works, a courtesan print, the kabuki actor), and the barter-loop diagram as a small inline figure: Vincent pays the dealer in paintings, paints the dealer in front of merchandise bought from the dealer, as settlement for more merchandise. Closed loop.
- Text beats: Tanguy the deported Communard (New Caledonia, amnestied 1880) who came home and financed the next revolution instead; Mère Tanguy and the cupboard-adjacent stacks of worthless canvases that turned out to be the family fortune at the 1890s auctions. This interlude is where the ukiyo-e wall motif enters the design system (§11) and reappears behind Chapter 3.

### Chapter 3 — The Beloveds (indigo field, star specks)
- **Thesis beat**: he loved things that could not say no. Pull-quote epigraph: *"the patron saint of loving the version of someone you made up."*
- **Sticky scene**: a horizontal "testability scale" (100 → 0). A marker sweeps the scale as the reader scrolls; five stops light up in sequence with year + one-line verdict:
  1. **1873 — Ursula Loyer** (a real person; the verdict was delivered by her mother; the relationship largely existed in his head)
  2. **1881 — Sien Hoornik** (a real person; the family vetoed it; the bill arrived twenty years late — the Scheldt, 1904. Handle with weight, no jokes)
  3. **1888 — Japan** (a nation; cannot reject you — and, via the Meiji state's curated self-export, was catfishing back)
  4. **1888 — The Studio of the South** (a business plan with a co-signer, Gauguin, and a bank, Theo)
  5. **1880–90 — Theo** (a brother; contractually unable to leave)
- Text: the untestability ladder — each beloved after Ursula is less real and less capable of refusing.
- **Image here**: *Japonaiserie: Flowering Plum Tree (after Hiroshige)* (1887, Van Gogh Museum) — his line-for-line copy of Hiroshige bordered with kanji characters lifted from other prints, decorative, unread by him. The wonton-font receipt, painted by hand. Small plate with one zoom crop of the border.

### Chapter 4 — The Roommate (lamplight-yellow stage)
- **Thesis beat**: the one time the structure had to house a real person, it lasted nine weeks.
- **Sticky scene**: a "strain gauge" arc from 23 October to 23 December 1888. Scroll raises the needle through five annotated events: Gauguin's arrival (Theo paid his debts and fare) → the collaboration and the portrait exchange (Gauguin's *Les Misérables* self-as-Christ vs. Vincent's self-as-Buddhist-monk dedicated to Gauguin — note the Fogg portrait's orange robe on green ground) → early December, Gauguin writes Theo the work is unsalable and announces he's leaving → the café argument (flag Gauguin's later razor-at-him claim as self-serving) → December 23 (red): the razor; part of the left ear; Rachel of the rue du Bout d'Arles told to keep it carefully.
- Text: Gauguin leaves forever; Theo arrives by train on Christmas Day; the Studio of the South's total sales: zero. One-beat coda on Gauguin's own gyre: he spent the rest of his life fleeing to ever more remote islands, staging an imaginary paradise over an actual colony, dying in the Marquesas in 1903 still billing himself as the prophet of pure painting — the smug rival won every argument and lost everything real, and his most famous canvas is famous for the gossip.
- **Compare-and-contrast plate (mandatory)**: side-by-side images of the two exchanged self-portraits — Vincent's *Self-Portrait Dedicated to Paul Gauguin* (September 1888, Fogg; orange-ochre robe on mint-green ground, blue piping) and Gauguin's *Self-Portrait "Les Misérables"* (1888, Van Gogh Museum; himself as the suffering Christ, halo, Émile Bernard's portrait behind). Annotate: two bids in the same argument — grandiose humility vs. grandiose inflation; the monk says *the work is sacred*, the Christ says *I am*. Color swatches sampled from the actual downloaded images (dominant-color chips per painting, so the comparison is data, not vibes). Add a third panel if space allows: Gauguin's *Christ in the Garden of Olives* (1889, Norton Museum) — the later doubling-down, red hair as the tell. Footnote that Gauguin's accounts of the razor are self-serving.

### Chapter 5 — Test the Legend (paper; verdict stamps)
- **Thesis beat**: the myth is load-bearing. A claim-by-claim plate in the knife-essay style: segmented buttons, five legends, each answered with a stamped verdict (CONFIRMED / BURNISHED / CONTESTED) that thuds in with a scale animation.
- The five claims and verdicts (data + nuance in §6):
  1. "He sold only one painting in his life." → **BURNISHED**
  2. "He cut off his ear." → **BURNISHED**
  3. "Nobody noticed him until after he died." → **BURNISHED**
  4. "He was self-taught." → **BURNISHED**
  5. "He shot himself in a wheat field." → **CONTESTED**
- Include the two vignettes here as side figures: the February 1889 petition (~30 neighbors' signatures, preserved in the Arles archives — "the one structure that could file paperwork, voting 30–0"); the Dr. Félix Rey portrait later used, per the Pushkin's account, to patch a chicken coop before entering the Pushkin in 1960.

### Chapter 6 — The Fix (paper)
- **Thesis beat**: the market didn't discover the genius; it was administered — by a 28-year-old widow with a baby and a ledger.
- **Counterfactual calibration (mandatory — do not overstate)**: the essay must NOT claim he would have been forgotten without her. The evidence forbids it: Aurier's essay appeared in January 1890, months before he died; Anna Boch bought *The Red Vineyard* as a believer; the avant-garde network (Signac, Bernard, Lautrec, the Nabis) already counted him significant; ~900 extant paintings in a rising modern-art market do not vanish (the cautionary proof that oblivion is possible is Vermeer — but his conditions differed). The defensible claim: she rescued him from *mediation*, not oblivion — without her, the collection likely gets liquidated in the 1890s and scatters into private hands; the German market probably still finds him, but later and on someone else's momentum, without the letters and without the myth. The honest endpoint of that counterfactual is the **Vuillard tier** — respected, museum-collected, expensive, but unknown to normal people. What she actually did was move him a *tier*: from a major Post-Impressionist to the most famous painter on earth. Present this as a reasoned range, never as a verdict — counterfactuals can't be proven, only argued.
- **Figure 1 (waffle)**: 900 squares (~30×30 grid), ~200 highlighted gold = what Johanna van Gogh-Bonger kept intact through decades of controlled sales; the rest dispersed. Caption: the museum's founding collection is her curation.
- **Figure 2 (log line)**: the price curve — 1890: 400 francs (≈$80) → 1901: Bernheim-Jeune retrospective (71 works; the detonation) → 1905: Stedelijk begins buying → 1914: the letters published (the myth engine) → 1960: the chicken-coop portrait enters the Pushkin → 1987: *Irises* $53.9m and a *Sunflowers* £24.75m → 1990: *Portrait of Dr. Gachet* $82.5m (auction record until 2004) → 1973: the Van Gogh Museum opens on the family collection.
- **Johanna's character beat (do not skip)**: she is the essay's final reveal — the last weirdo in the gyre. A 28-year-old widow with a newborn, a foreign apartment stacked with ~200 unsold canvases, and a wealthy family with one instruction: come home. She declined, and ran her dead brother-in-law's afterlife like an intelligence operation for thirty years: controlled supply, strategic loans, exhibitions aimed at the one market (the German Expressionists) actively shopping for a dead ancestor, and then the masterstroke — the edited 1914 letters, history's most effective marketing act, which sanded the friction out of the brothers' marriage of convenience and left the world a hagiography. Frame her as the "evil genius (not really evil)": every manipulation was sympathetic, and it worked so well that the myth she built is still the load-bearing story of the museum. One honest sentence notes what the editing cost — and be precise about whose relationship she edited: Vincent and Theo's *partnership* (their real arrangement: Theo funds, Vincent paints, nobody else allowed in) had constant friction in the letters, and Johanna's selections sanded it into seamless mutual devotion. In flattening the brothers' fights about money and Gauguin, she also flattened her own husband — a significant dealer in his own right, with his own frustrations and half of the argument — into the myth's saintly caretaker: the world kept Vincent and buried the husband a second time, in print. ("She widowed him twice": literal widowhood in January 1891; historiographic in 1914. Deploy the line only with both caveats that follow.) Two honest caveats, both in the text: (a) the archive was already asymmetrical — Vincent's letters to Theo survive almost complete because Theo kept them, Theo's replies mostly lost — so the record leaned Vincent structurally and she curated, not created, the lean; (b) she kept Theo visible as the letters' anchor and named her son for the uncle — she wrote him down to a saint, not out of the story. Modern scholarship (the 2009 complete letters edition) has been recovering the second Theo ever since. (Do not confuse the reader: Johanna was Theo's wife; the marriage was happy, brief — April 1889 to his death, January 1891 — and she never remarried. Their son Vincent Willem, born January 1890, inherited the archive that became the museum.)
- **Images here**: the period photograph of Johanna van Gogh-Bonger with her infant son Vincent Willem (both images PD; Commons has the well-known portrait), and for the price curve's end, *Portrait of Dr. Gachet* — use the Musée d'Orsay second version and let a caption note the irony that the $82.5m record-holder (the first version, 1990) has not been publicly seen since; its location is genuinely unknown.

### Chapter 7 — The Scoreboard (red field)
- **Thesis beat**: the closing ledger. Rows of final numbers (see §6): ~900 paintings; ~1,100 drawings; ~800 letters; ~18,000 francs wired; 1 famous sale; ~30 signatures; 37 years; 100 years from death to record auction.
- Closing essay (3 short paragraphs): the art is the receipt, not the reward; greatness and disaster ran on the same fuel, which is exactly why the recipe is not a career plan. Penultimate beat: the gyre's last turn — the reader has now met the fired clerk, the coal-field preacher, the man in love with a country that didn't exist, the exiled Communard paint-dealer, the self-mythologizing stockbroker, and the widow who ran the whole afterlife from a ledger; the canon, it turns out, is not a gallery of sane men, and nobody gets to be this famous without being this strange. The final line lands the moral the user wants: *you don't want to be a disaster artist — you want the engine without the disaster, and ideally a sister-in-law with a ledger.*
- Then a paper sources block: numbered list matching the essay's `<sup class="fn">` citations.

---

## 3. The persistent toy: Theo's Ledger

- Fixed tab at the bottom corner (house precedent: the knife essay's belt). Closed state: a small slip showing `THEO'S LEDGER — FR. 0`; as the reader scrolls the timeline, the cumulative wired total rises (map document scroll progress onto §6's year-by-year stipend data; end state ≈ 18,000 francs).
- Tap/click opens a dialog (gold top border, like the house lineage dialog) with a year-by-year table and one honest line: the estimate's basis and error bars.
- Must never block content; two-close-ways minimum; reduced-motion safe.

---

## 4. The claims plate — verdict semantics

- **CONFIRMED**: claim survives the paperwork intact.
- **BURNISHED**: true in spirit, wrong in the tidy version — the myth is a rounding of a real number (e.g., "one painting sold" ≈ a near-zero with one famous exception; "cut off his ear" ≈ part of the left ear, whole-ear story burnished by Gauguin's self-serving account).
- **CONTESTED**: the evidence cannot convict either version (the Auvers shooting, per Naifeh & Smith 2011 vs. the traditional account).
- Each verdict gets a 2–4 sentence readout written in the house voice, with its own footnote.

---

## 5. Tone and voice (non-negotiable)

**Register**: literary longform magazine — the house voice. Long, rolling sentences that earn their semicolons; dry wit; direct address to the reader ("Keep an eye on the corner tab"); erudite asides footnoted like a paper. Gallows humor is allowed; cruelty is not. The essay laughs *near* the disaster, never *at* the ill man.

**Voice samples to calibrate against** (mimic this rhythm):

> "He didn't fail at marketing. He was structurally unmarketable — no seller account, no rating, one repeat buyer who was also his brother, and a product in a category the market had not yet invented."

> "The neighbors got exactly what they petitioned for. What it cost them was the view."

> "The imagination produced kitsch; the mirror produced the icon. The doctrinal war, adjudicated by the two surviving objects, goes to the man with the razor."

> "She was right about every painting, and she got to be right at the exact moment it stopped mattering to him."

**Rules**
1. Every number carries a footnote; every uncertain number is hedged in prose ("roughly," "by the museum's account," "catalogues disagree at the margins"). Never fabricate a source, a date, or a figure.
2. The dark material has gravity zones: the ear (factual, restrained), Sien's 1904 death (one sober sentence, no jokes), the Gauguin material if referenced (state the predation plainly), the petition (its cold bureaucratic reasonableness is the horror — let the document speak).
3. Humor lives in structure and juxtaposition — valuation ladders, ledgers, verdicts — not in mocking mental illness or poverty.
4. No emojis anywhere in the document. No exclamation marks in body copy. The wit is declarative.
5. **The gyre rule**: the essay escalates. Each chapter widens the aperture on what these people were — boy, fired clerk, failed preacher, painter of a country that didn't exist, commune architect, petition target, paint-dealer ex-Communard, self-mythologizing rival, widow mastermind — and the humor compounds rather than repeats. Chapter N should make the reader re-read Chapter N−1 differently. Never announce the escalation; let the accumulating weirdness do it.
6. **Internet-meme references**: default is canonical sources only (no memes by name). If the user opts in, contemporary framings (e.g., a comparison to "cockroach wife syndrome"-type internet folklore) may appear at most once, as a footnote aside, never in body copy.
7. Paragraphs: 3–6 sentences, one idea each, max-width ~36rem. Section transitions do narrative work, not "In this section we will…".

---

## 6. Data pack (verify everything marked ✱ during research)

| Item | Value | Status |
|---|---|---|
| Career length as painter | ~10 years (1880–1890) | solid |
| Paintings | ~860–900 (catalogues disagree) | solid, cite range |
| Drawings | ~1,100 | solid |
| Letters | ~800 surviving (650+ between the brothers) | solid |
| Paintings per year (for Ch1 bars) | 1881:1, 1882:30, 1883:80, 1884:100, 1885:120, 1886:60, 1887:75, 1888:200, 1889:140, 1890:65 (≈871 total — label "rounded") | ✱ verify against Van Gogh Museum / de la Faille / Hulsker; adjust to the sourced totals |
| Arles production | ~200 paintings in ~15 months | solid |
| Saint-Rémy production | ~150 in one year | solid |
| The Red Vineyard | sold 1890, ~400 francs, to Anna Boch, at Les XX Brussels | solid |
| Theo stipend | roughly 150–250 F most months; model ledger ≈ 18,000 F cumulative over the decade | ✱ derive monthly figures from the letters; present as an estimate with stated assumptions |
| Goupil | hired 1869 (age 16, via uncle); London 1873; Paris 1875; dismissed spring 1876 | solid |
| Gauguin at Yellow House | arrived 23 Oct 1888; ear incident 23 Dec 1888; ~62 days | solid |
| Petition | February 1889, ~30 signatories, Arles archives | ✱ verify count and date |
| Aurier essay | "Les Isolés: Vincent van Gogh," Mercure de France, January 1890 | solid |
| Boussod & Valadon show | January 1890, ~20 works, no sales (Theo organized, discreet) | ✱ verify count |
| Bernheim-Jeune retrospective | 1901, 71 paintings | solid |
| Letters first published | 1914 | solid |
| Stedelijk acquisitions | 1905 onward | ✱ verify |
| Dr. Rey portrait → chicken coop → Pushkin | by the Pushkin's account; acquired 1960 | ✱ cite the museum's own telling |
| Auctions | *Irises* $53.9m (1987); *Sunflowers* £24.75m (1987); *Portrait of Dr. Gachet* $82.5m (1990, record until 2004) | ✱ verify sale details and houses |
| Van Gogh Museum | opened 1973, founded on the family collection (Johanna → Vincent Willem) | solid |
| Shooting | Auvers, 27 July 1890; died 29 July; traditional suicide vs. Naifeh & Smith (2011) accident theory | solid; present both, verdict CONTESTED |
| Yellow House | destroyed 1944 (wartime bombing) | solid |
| Self-portraits | ~35 | solid |
| Fogg self-portrait (bonze, dedicated to Gauguin) | September 1888, Harvard Art Museums | solid |

**The five claims' fine print** (for Ch5 readouts):
1. *One painting*: the tidy version — he sold, traded and gave away a handful; exactly one famous documented sale. The honest figure is "near zero," and the essay should say so.
2. *The ear*: best reconstruction — part of the left ear; the bandaged self-portraits agree; Gauguin's "he waved the razor at me" account is self-serving and flagged as such.
3. *Ignored*: Aurier's rave (Jan 1890), Les XX exhibitions, Theo's gallery show — "nothing sold" and "nobody noticed" are different sentences; the essay keeps them separate.
4. *Self-taught*: Anton Mauve (cousin by marriage) taught him; a winter at Antwerp's academy; the naive hand was trained.
5. *The shooting*: the wound angle, the absent painting kit, the village's doubts vs. the traditional account; the evidence cannot convict either version.

---

## 7. Research checklist (run before writing; re-run when the draft flags a gap)

1. **Primary anchor**: vangoghletters.org — confirm stipend ranges, the Boussod & Valadon show details, Gauguin's "unsalable" letter, the bonze self-portrait description (the orange-on-green chord; Vincent's own words about painting himself as a Japanese monk).
2. **Counts**: Van Gogh Museum catalogue and one scholarly count (de la Faille / Hulsker) — settle the yearly painting numbers and the "≈900" total; note disagreement in a footnote.
3. **Stipend model**: pull monthly/asked-for amounts from the letters by year; publish the ledger table's assumptions in the dialog.
4. **Petition**: Arles archives — date, signature count, one line on what the signatories asked for.
5. **Prices**: verify the 1987–1990 auction records (sale, date, price, buyer if known) and that Gachet's record stood until 2004; find one defensible 1890 francs→today conversion method and state it.
6. **Chicken coop**: Pushkin Museum's own provenance telling of the Rey portrait; if the museum hedges, the essay hedges identically.
7. **Johanna**: her exhibition/loan history (1892 Kunstkring onward), the 1914 edition's editorial framing, the museum's founding; one solid biography or the Van Gogh Museum's own research pages.
8. **Naifeh & Smith**: summarize their 2011 argument and the scholarly pushback; both get one sentence, no verdict.
9. **Anything the draft asserts that isn't in this pack gets sourced before it ships.** No invented citations, dates, or quotes; if a colorful anecdote can't be traced (e.g., the chicken coop, the cupboard-wedged Tanguy canvases), attribute it in prose to the tradition that tells it.

---

## 8. Visual system

- **Type**: Newsreader (variable serif, body + italics) and Archivo (variable width axis, display/kickers/UI). Base64-embed latin + latin-ext only. Fallback stacks: `Georgia, "Times New Roman", serif` and `"Arial Narrow", Arial, sans-serif`.
- **Tokens**: the house palette (§1) exactly, plus `--ochre:#B57708` for the subsidy chapter field and the existing `--indigo` with star-speck texture for the beloveds chapter. Star texture: tiny radial-gradient dots, two sizes, low opacity — a night-sky field, not a screensaver. The Gauguin chapter stage: warm lamplight yellow gradient with a window rectangle of cooler light; the strain gauge in ink-on-gold, ending red.
- **Signature details** (choose at least three): (1) the ledger tab toy (§3); (2) verdict stamps (§4); (3) stroke-draw impasto-arc ornament under the H1; (4) the waffle of 900 squares with 200 gold; (5) the single gold dot of the 1890 sale on an otherwise flat sales line — this dot recurs as a visual motif (find it again in the Ch6 log-line figure); (6) the testability scale whose marker sweeps right-to-left (untestability rises) against reading direction — do it deliberately, and let a caption explain it.
- **Layout**: hero full-bleed; chapters as "fields" alternating paper / ochre / indigo / paper; story sections two-column with sticky figures ≥960px, stacked with figures inline below that; plates max-width ~44rem centered; sources block on `--paper2`.
- **Motion**: scroll scenes driven by one rAF loop; UI transitions <300ms; everything transform/opacity only; every scene must be complete and legible at progress=1 and under reduced-motion. No autoplaying anything the reader didn't trigger.

## 9. Process (match the user's workflow)

1. **Research first**: run the §7 checklist with deep-research passes before any prose exists. Produce a fact sheet; every essay number must trace to it.
2. **Outline**: chapter-by-chapter outline (title, thesis beat, scene/chart spec, footnotes to attach) — then **stop and ask the user for visual/plot approval before writing**.
3. **Draft**: write full prose in the §5 voice; attach footnotes as you go; re-run targeted research wherever the draft asserts something unsourced.
4. **Rough cut**: implement the full page; then **stop and ask the user for bug/visual feedback** before polish.
5. **Iterate**: fix bugs, tune scenes, verify data one final time against the fact sheet.
6. **QA before delivery**: open at 375/768/1024/1440; screenshot every chapter; click every control (plate buttons, ledger dialog, stamps, sources links) **and open every painting's lightbox, verify the full-resolution image and context panel load**; zero console errors, zero 404s, no dead controls; confirm reduced-motion renders final states; confirm there are **no third-party requests** (network panel: everything same-repo and relative), and that initial load pulls thumbs only.

## 10. Definition of done

- One self-contained `disaster-artist.html` in the house format.
- Seven chapters + interlude + hero + sources; all §2 beats present; at least three §8 signature details; the ledger toy works.
- Every figure footnoted; §6 items marked ✱ verified or hedged in prose.
- **The imagery directive (§11) fully executed**: the Tanguy centerpiece plate, the monk-vs-messiah compare plate, and at least eight paintings reproduced from verified public-domain or open-access sources — all committed to the user's GitHub repo in the three-tier `img/src|full|thumb` structure with the generation script, lazy thumbs on initial load, and the lightbox viewer verified for every painting; a rights list (image → source → license/PD tag) shipped alongside the file.
- The last line of the essay lands the moral: great artist, great disaster — same machine — and you don't want to be one.
- Then hand back with: the file, a one-paragraph summary of what was verified vs. assumed, and the list of open questions for the user.

---

## 11. Imagery directive (mandatory)

The essay must be visibly full of paintings — this is a story about images, told with images. Van Gogh died in 1890 and Gauguin in 1903: **every canvas mentioned is public domain in essentially every jurisdiction.** There is no reason for a single gray placeholder anywhere.

**Sourcing rules**
1. Primary source: **Wikimedia Commons** — but verify each file's own page for the PD tag or license before use; never assume. Prefer high-resolution scans.
2. Prefer institutional open-access programs where they beat Commons quality: **Van Gogh Museum** (open content), **Harvard Art Museums** (CC0 — this covers the Fogg bonze portrait), **The Courtauld** (open access — the bandaged-ear self-portrait), **MoMA** (open access — *Starry Night*), **Rijksmuseum** (CC0 — also good for the Hiroshige prints behind Tanguy), **National Gallery, London** (*Sunflowers*), **Musée d'Orsay**.
3. Every painting ships with a house-style `figcaption`: title, year, collection — and a footnote where provenance matters (chicken coop, missing Gachet, etc.).
4. Ship a rights list with the deliverable: image → source page → license/PD status. No image without a line in that list.
5. Every `<img>` gets meaningful alt text. Decorative crops get empty alt + `aria-hidden`.

**Technical rules (repo-hosted, two-tier)**
- The user hosts essays from a GitHub repo. Commit all painting images to that repo, in three tiers:
  ```
  img/src/    raw museum downloads, kept as the archive (whatever they ship, no recompression)
  img/full/   display masters — max dimension ~2000px, q82 (≈300–500KB each)
  img/thumb/  what the page actually renders — max dimension ~640px, q72 (≈40–80KB each)
  ```
  Filename convention: kebab-case slugs (`pere-tanguy.jpg`). Write and commit the generation script (Python/Pillow or ImageMagick) alongside them so the tiers are reproducible — the user is a developer and expects the pipeline, not just the outputs.
- The HTML references **only `img/thumb/`** on load, with `loading="lazy"`, `decoding="async"`, explicit `width`/`height` (no layout shift), and alt text. Initial page weight target: ≤ ~500KB of imagery total.
- **The viewer**: every painting — thumbs, plates, zoom crops — is click-to-expand. Clicking opens a native `<dialog>` lightbox in the house style (gold top border) containing: the `img/full/` version (max ~90vw/78vh) and a context panel with title, year, collection, credit line, and 1–3 short paragraphs of provenance/context specific to that painting (the chicken coop, the missing Gachet, the unread kanji border, the 400 francs, etc.), plus links to the essay's footnotes where relevant. Context text lives in a small `img/manifest.json` (slug → metadata + context markdown) so the lightbox is data-driven and the panel text is editable in one place.
- Lightbox behavior: Esc, backdrop click, and a close button; focus moves into the dialog on open and returns to the thumbnail on close; prev/next arrows when opened from a multi-image plate (monk vs. messiah, Tanguy crops); body scroll locked while open; keyboard-operable end to end; reduced-motion safe.
- For every compare/zoom plate, sample dominant colors from the actual downloaded pixels to build the swatch chips — the palette analysis should be real, computed at build time, not eyeballed.

**Required plates (minimum eight paintings)**
| Plate | Painting | Collection | Used in |
|---|---|---|---|
| THE CENTERPIECE | *Portrait of Père Tanguy* (1887) | Musée Rodin | Interlude — full-width, plus 2–3 zoom crops of the ukiyo-e wall |
| The monk | *Self-Portrait Dedicated to Paul Gauguin* (1888) | Fogg, Harvard | Ch4 compare plate |
| The messiah | Gauguin, *Self-Portrait "Les Misérables"* (1888) | Van Gogh Museum | Ch4 compare plate |
| The escalation | Gauguin, *Christ in the Garden of Olives* (1889) | Norton Museum | Ch4, third panel |
| The wonton font | *Japonaiserie: Flowering Plum Tree (after Hiroshige)* (1887) | Van Gogh Museum | Ch3, border zoom |
| The gold dot | *The Red Vineyard* (1888) | Pushkin | Ch1/Ch6 — the one famous sale, made visible |
| The house | *The Yellow House* (1888) | Van Gogh Museum | Ch4 |
| The wound | *Self-Portrait with Bandaged Ear and Pipe* (1889) | Courtauld | Ch5 claims plate |
| The sky | *The Starry Night* (1889) | MoMA | Ch3 or Ch7 |
| The sun | *Sunflowers* (1888) | National Gallery, London | Ch2 ochre field |
| The coop portrait | *Portrait of Dr. Félix Rey* (1889) | Pushkin | Ch5 vignette |
| The widow | Photograph of Johanna van Gogh-Bonger with Vincent Willem | Commons (PD photo) | Ch6 |

Others welcome if the draft wants them (*The Potato Eaters* for Ch1's early years; *Van Gogh's Chair* / *Gauguin's Chair* as a quiet Ch4 pair; a Hiroshige original next to the *Japonaiserie* copy — original vs. copy in one plate is the whole argument in a single image).

**The Tanguy design motif**
The ukiyo-e wall in the Tanguy portrait should leak into the design system: use tightly-cropped PD Hiroshige bands (from the Rijksmuseum's CC0 scans) as section-divider strips — the wall reappearing behind the beloveds chapter, under the claims plate, behind the sources list. The essay's visual spine is: a man kept paying his dealer in paintings, and the dealer's wall followed him into the canon.

**The compare plate's data touch**
In the monk-vs-messiah plate, compute each painting's dominant palette and render the swatches as the plate's own figure: "the monk runs orange-on-green with blue trim; the messiah runs blood-red and soot." The color chips are extracted from the images at build time, so the essay's most famous art-historical argument arrives as a measurable chart.
