# Disaster Artist: high-resolution image hunt (brief for Gemini Antigravity)

Bryan runs this himself in Gemini Antigravity, as a separate task. Paste everything below the line into a new
Antigravity session opened on the ProofEr repo.

Built from the piece's brief (§11 imagery directive), the approved outline (`outline.md`) and the round-2 research
reports (`research/round2/`). Catalogue numbers (F = de la Faille, JH = Hulsker) are left for you to fill in from the
museum's own page: none were checked in this project's research, so none are given here.

---

## Task

Find, licence-check and download the images below for the Van Gogh data essay "Disaster Artist", in the repo
`bpmdata/proofer`, piece folder `proj/disaster-artist/`.

For every image:
1. Find the **highest-resolution file the holding institution itself offers** (its open-access download or IIIF
   image). Use Wikimedia Commons only where the institution offers nothing, and then pick the largest file whose
   own Commons page shows a public-domain or open licence tag.
2. Open the file's own page and record its licence or public-domain status. Never assume.
3. Save the original download, unchanged, to `proj/disaster-artist/img/src/<slug>.<ext>` (slug given below).
4. Add a row to `proj/disaster-artist/img/rights.md`: slug · title · date · catalogue number (F and JH, read from
   the museum page or the 1970 de la Faille / Hulsker numbers the museum cites) · holding institution · source page
   URL · file URL · pixel size · licence or PD tag, as written on the page.
5. Then run `proj/disaster-artist/scripts/make_image_tiers.py` (open it in Thonny, press Run). It makes the
   `img/full/` and `img/thumb/` copies and `img/sizes.json`. After the three compare-plate paintings are in, run
   `scripts/extract_swatches.py` the same way.

Rules:
- Holding institution first: Van Gogh Museum, Harvard Art Museums, Courtauld, MoMA, National Gallery London,
  Rijksmuseum, Musée d'Orsay, Getty, Norton Museum and the Art Institute of Chicago have open-access or high-res
  programmes. Captions cite the holding institution, never a search engine.
- If no open, high-resolution file exists (likely for the Pushkin's two paintings and for private collections), say
  so in `rights.md`, take the best Commons file with a valid PD tag, and note its size.
- Don't download from stock-photo or print-on-demand sites, and don't use AI-upscaled or recoloured copies.
- Where a row says **check**, the title, date or owner given in the brief may be wrong: confirm it on the museum page
  and write what the page says.

---

## Required (brief §11 and the outline)

| # | Slug | Title | Date | Holding institution | For | Why it's needed |
|---|---|---|---|---|---|---|
| 1 | `pere-tanguy` | *Portrait of Père Tanguy* | 1887 | Musée Rodin, Paris | Interlude, full-width centrepiece, plus 2–3 zoom crops of the Japanese prints on the wall | The shopkeeper who took paintings for paint; the crops show the prints Vincent copied. Needs the largest file available for the crops. |
| 2 | `self-portrait-dedicated-to-gauguin` | *Self-Portrait Dedicated to Paul Gauguin* (the "bonze" portrait) | Sept 1888 | Harvard Art Museums (Fogg), 1951.65 | Ch4 compare plate, left | Vincent as a Japanese monk, sent to Gauguin before he came to Arles. Colours are measured for the swatch chips, so it needs a faithful, uncropped museum file. |
| 3 | `gauguin-les-miserables` | Paul Gauguin, *Self-Portrait "Les Misérables"* (with Émile Bernard's portrait behind) | 1888 | Van Gogh Museum, Amsterdam | Ch4 compare plate, right | Gauguin as Jean Valjean, sent to Vincent; the other half of the exchange. Swatch chips too. |
| 4 | `gauguin-christ-garden-of-olives` | Paul Gauguin, *Christ in the Garden of Olives* | 1889 | Norton Museum of Art, West Palm Beach | Ch4 third panel | Gauguin paints himself as Christ after Arles. Swatch chips (the red hair is checked by colour, since no text source mentions it). |
| 5 | `japonaiserie-flowering-plum-tree` | *Japonaiserie: Flowering Plum Tree (after Hiroshige)* | 1887 | Van Gogh Museum | Ch3 plate, with a zoom on the border characters | His copy of a Japanese print; the border characters were copied from other prints and don't make sense. |
| 6 | `hiroshige-plum-park-kameido` | Utagawa Hiroshige, *Plum Park in Kameido* (from *One Hundred Famous Views of Edo*) | 1857 | Several museums hold impressions: try the Van Gogh Museum (Vincent's own copy, if it holds one), Rijksmuseum, Brooklyn Museum | Ch3, beside no. 5 | The original next to the copy, in one plate. |
| 7 | `red-vineyard` | *The Red Vineyard* | Nov 1888 | Pushkin State Museum of Fine Arts, Moscow | Ch1 and Ch6, the "gold dot" | The one documented sale in his life: 400 F to Anna Boch, 1890. |
| 8 | `yellow-house` | *The Yellow House (The Street)* | Sept 1888 | Van Gogh Museum | Ch4 | The house he rented for the Studio of the South. |
| 9 | `self-portrait-bandaged-ear` | *Self-Portrait with Bandaged Ear* | Jan 1889 | Courtauld, London | Ch5 claims plate | After the ear. **Check:** the brief calls it "with Bandaged Ear and Pipe" at the Courtauld; the Courtauld's version has no pipe, and the pipe version is in a private collection. Get the Courtauld one; list the pipe version as optional. |
| 10 | `starry-night` | *The Starry Night* | June 1889 | MoMA, New York | Ch3 or Ch7 | The painting readers know, painted at the Saint-Rémy asylum. |
| 11 | `sunflowers-national-gallery` | *Sunflowers* | Aug 1888 | National Gallery, London | Ch2, the ochre field | Painted to decorate the Yellow House for Gauguin. |
| 12 | `dr-felix-rey` | *Portrait of Dr Félix Rey* | Jan 1889 | Pushkin State Museum of Fine Arts, Moscow | Ch5 vignette | The doctor who treated him after the ear; the "chicken coop" painting. Research found it entered the Pushkin in 1948, not 1960. |
| 13 | `johanna-and-vincent-willem` | Photograph of Johanna van Gogh-Bonger with her son Vincent Willem | c. 1890 | Van Gogh Museum (Vincent van Gogh Foundation) holds the original; Commons has copies | Ch6 | Theo's widow, who built the reputation. **Check** the date, photographer and PD status on the museum or Commons page. |

## Recommended (the outline or the brief's "others welcome")

| # | Slug | Title | Date | Holding institution | For | Why it's needed |
|---|---|---|---|---|---|---|
| 14 | `portrait-dr-gachet-orsay` | *Portrait of Dr Gachet* (second version) | 1890 | Musée d'Orsay, Paris | Ch6 price curve, end | Stand-in for the first version, which sold for $82.5m in 1990 and hasn't been seen publicly since. |
| 15 | `irises` | *Irises* | 1889 | J. Paul Getty Museum, Los Angeles | Ch6 price curve | $53.9m in 1987. |
| 16 | `potato-eaters` | *The Potato Eaters* | 1885 | Van Gogh Museum | Ch1, the early years | The Nuenen period, before the colour. |
| 17 | `van-goghs-chair` | *Van Gogh's Chair* | 1888 | National Gallery, London | Ch4, a quiet pair with no. 18 | Two empty chairs as the two men in the Yellow House. |
| 18 | `gauguins-chair` | *Gauguin's Chair* | 1888 | Van Gogh Museum | Ch4, with no. 17 | As above. |
| 19 | `rey-ear-sketch` | Dr Félix Rey's sketch of the ear wound, in a 1930 letter to Irving Stone | 1930 | Bancroft Library, University of California, Berkeley | Ch5, the ear verdict | The drawing that shows the whole ear cut off. **Check** the rights: it may not be public domain; if it isn't, record that and don't download. |
| 20 | `arles-petition` | The petition of Arles residents against Vincent | Feb 1889 | Archives municipales d'Arles | Ch5 vignette | About 30 names asking for him to be locked up or sent home. **Check** whether the archive publishes an image and on what terms. |

## When you're done

Report: which rows have files, their pixel sizes, each licence, and every row you couldn't fill and why. Don't
change any other file in the repo.
