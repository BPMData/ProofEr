# Refinement Plan: *Saints & Spells* (`sicilian-folk-magic`)

**Purpose:** Hand-off execution blueprint for **non-Neon (Hydrogen / Flash) sub-agents** to elevate *Saints & Spells* from a patched draft into a cohesive, deeply engaging, historically vivid long-form infoessay—after the immediate UI/animation/cabinet/map bug fixes landed on `fix/sicilian-bugfixes-and-cabinet`.

---

## 0. Open Decisions for Bryan (Settle Before Wave 1/2 Starts)

1. **Relic cabinet behavior when scrolling back up:** Right now the cabinet is strictly synced to your current scroll position (scroll down through Act 7 → `5 of 5`; jump back to Overture → `0 of 5` so it can never desync). Would you prefer it to stay **strictly synced to scroll position**, or **sticky/cumulative once discovered** (stays `5 of 5` once you've scrolled past Act 7, with a subtle reset only at top)?
2. **File size vs. offline rule:** Currently `pieces/sicilian-folk-magic.html` is ~3.6 MB because ProofEr's `check_offline.py` and CI strictly forbid hotlinking external images (everything—fonts, WebP cutouts, zoom photos, relic photos—is base64-inlined). Are you happy keeping it single-file offline around 3.5–4.0 MB, or should we cap zoom/cutout resolution slightly to trim closer to ~2.5 MB?
3. **Missing/unattributed images:**
   - **Act 8 (*To the Americas*):** Currently has only a drawn ship because no open-licensed image of Benedict the Moor or Antonio of Noto turned up in Pass F. Should a Hydrogen art-scout worker hunt Wikimedia Commons / Met / Europeana for a public-domain painting or statue of St. Benedict the Moor?
   - **Act 6 (`13-gratteri-portrait.jpg`):** Sourced from `visitgratteri.com` with unknown photographer/sitter/date (`19th century` by look). Keep it as-is, or swap/remove if provenance feels thin?
4. **Targeted context research:** Acts 3 (*Messina*), 4 (*St Joseph's tables*), and 8 (*To the Americas*) are thin partly because earlier drafts trimmed them down and partly because a few connecting facts (e.g., why Messina and Palermo rivaled each other, why emigrants told the fava-bean famine legend, what a *vara* or *cimaruta* physically looks like) aren't in `figures.md` yet. Should we run one quick Hydrogen research pass (`Wave 1`) for those specific context hooks, or stay strictly inside existing `figures.md`?
5. **Myth-check stamps & stage slam:** Should we trim the remaining mid-prose Myth-Check boxes down to only the big load-bearing myths (tarot, Agatha/goddess, Inquisition witches, Americas migration) and drop the giant tilted red stamp from the puppet canvas (or keep the canvas slam)?

---

## 1. North Star: Voice, Narrative & Editorial Diagnosis

### The Two Pillars of the Voice
1. **Barbara Tuchman's *A Distant Mirror* (slightly warmer and less technical/intimidating, never dumbed down):**
   - **Panoramic history grounded in human portraits:** Tuchman makes a foreign century feel habitable by anchoring big institutional forces in named people caught inside them. We already have remarkable human anchors in `figures.md`—Geronima La Gattuta of Ciminna, the despairing soap-maker Vincenzo Bonelli climbing Monte Pellegrino in February 1625, Lauria de Pavia telling Palermo inquisitors she flew six palms above the ground to Benevento, Catarina Calandrino shut away in Palermo's great hospital, the farmer Francesco Frusteri beheaded at Paceco in 1817, the tireless doctor Giuseppe Pitrè filling 25 volumes while barely leaving Palermo, and Benedict of San Fratello born to enslaved African parents. Let them breathe as human scenes, not bullet-point citations.
   - **Sympathetic interiority without credulity:** Show *why* a belief made urgent, rational emotional sense in its own world—why a city facing lava or bubonic plague wanted its patron saint physically present in gilded silver, why an anxious parent turned to a *ciarmavermi* healer, why a condemned prisoner who repented at the scaffold looked like a brother to the Good Thief—without either pretending the magic works or sneering at the people who practiced it.
   - **Unhurried, clause-rich prose (`T14`):** Use colons, semicolons, and balanced subordinate clauses that pull the reader forward; eliminate clipped AI staccato fragments ("Not leftovers of someone else's religion. Sicilians' own.") and breathless "Snopes on cocaine" gotchas.
2. **A wry, deeply knowledgeable Sicilian friend & folklorist:**
   - Warm, conversational connective tissue between acts so each chapter feels like the next turn in a long evening's story, not a disconnected museum placard.
   - Debunk the faintly Orientalist exoticisms—tarot's fake Egyptian/Romani pedigree, northern Italian race-science caricatures, "goddess in disguise" Victoriana, "thousands of witches burned"—with dry irony aimed at the myth-makers, institutions, and relic merchants, never at ordinary Sicilians.

### Concrete Before → After Rewrite Benchmarks

#### Example 1: Replacing Snopes-cadence & abrupt transition (Act 5)
- **Current `copy.md`:**
  > Are they saints? Not to the Church: they were never listed among its saints or blessed. They were saints of the street, "popular, though not officially recognised", as the historians Davies and Matteoni put it, and other towns had their own.
  >
  > Francesco Frusteri of Paceco, near Trapani, is one. He was a farmer who killed his own mother and was beheaded at Paceco on 5 November 1817...
  >
  > The dead visit children too. On 2 November, the Day of the Dead, many Sicilian families tell children that their dead relatives come back in the night and leave presents: *pupi di zùccaru*, sugar dolls, with fruit and nuts in a basket. You'll read that the custom carries on Roman offerings to the dead, but nobody we found names a document for that.
- **Target Voice (Tuchman + Sicilian friend):**
  > By the Church's own rulebook, none of these men could be saints: their names never entered the official lists of the blessed or canonized, and Rome forbids public veneration of anyone left outside them [X2-124, X1-234]. On Palermo's streets, however, official lists were beside the point; what mattered was a reputation for holiness won on the scaffold. Other towns kept their own gallows patrons, and in Paceco, near Trapani, one of the most vivid was a farmer named Francesco Frusteri, beheaded on 5 November 1817 for murdering his own mother [X1-234, X1-235, X1-159]. An inscription in the church of San Francesco di Paola recorded only that he died "resigned and contrite"—yet seventy years later Giuseppe Pitrè found him spoken of "in fame of sanctity," with miracles credited to his name across Trapani, Paceco, and the Isola Grande [X1-159].
  >
  > The Sicilian dead did not return only on dark roads by the Oreto; once a year, on 2 November, they came through the front door carrying sweets for the children [X1-162]. On the Day of the Dead, families set out baskets of fruit, nuts, and *pupi di zùccaru*—painted sugar dolls—and told the young ones that departed relatives had slipped in during the night to leave them [X1-162, X1-212, X1-163]. Outsiders regularly trace the custom straight back to Roman offerings at family tombs, though when you go looking for an unbroken documentary chain from antiquity to Palermo's sugar-casters, the paper trail simply isn't there [X1-167].

#### Example 2: Expanding an unwritten stub into lived history (Act 8)
- **Current `copy.md`:**
  > **Benedict the Moor.** Born at San Fratello to African parents who had been enslaved, he died at a convent in Palermo on 4 April 1589. He was beatified in 1743 and made a saint in 1807.
- **Target Voice (Tuchman + Sicilian friend):**
  > Long before nineteenth-century steamers carried Sicilian families to Buenos Aires or New Orleans, Sicilian saints were already crossing the Atlantic inside the devotional networks of the Spanish Empire, which ruled Sicily from 1516 to 1713 [X1-71, X3-211]. Consider Benedict of San Fratello, known across the Catholic world as Benedict the Moor: born in a Sicilian hill town to African parents who had been enslaved, he spent his religious life in Palermo and died there in a Franciscan convent on 4 April 1589 [X3-122, X3-123, X3-124]. Rome did not beatify him until 1743 or canonize him until 1807, yet popular devotion refused to wait for Vatican paperwork [X3-126, X3-127, X3-128]: by 1609 a Black Catholic brotherhood in Lisbon had already taken him as patron, and from there his cult traveled down the sea lanes to Brazil and across the Spanish and Portuguese Americas, where in Venezuela his feast is still danced to the beat of *chimbangueles* drums [X3-134, X3-136, X3-158].

#### Example 3: Fixing the clipped AI closer (Curtain call)
- **Current `copy.md`:**
  > So, no goddesses under the robes, and no ancient Egyptian cards. What Sicily has is better and stranger: a city that carried a veil against lava, a hermit elected patron before her bones were checked, a letter from Mary written 1,500 years late, tables for the poor, executed men prayed to as protectors, and healers the Inquisition couldn't quite bring itself to burn. Not leftovers of someone else's religion. Sicilians' own.
- **Target Voice (Tuchman + Sicilian friend):**
  > Put away the Egyptian tarot and the Victorian goddesses, then, because the island left behind in the archives is far richer—and far more human—than the exotic mirage outsiders invented for it. Under an unbroken succession of foreign crowns, from Byzantines and Arabs to Normans and Spaniards, Sicilians did not quietly preserve someone else's paganism under Catholic robes; they took the liturgy, saints, relics, and feast days of an empire-spanning Church and bent them to the immediate urgencies of their own streets—halting Etna's lava with a martyr's veil, voting an unverified hermit onto Palermo's civic throne in the middle of a plague, turning condemned criminals into compassionate night-watchmen, and bargaining with fairies and saints alike when a child fell ill. What looks from afar like ancient superstition turns out, up close, to be something much closer to craft: the work of an island making a universal religion answer in its own dialect.

### Concrete Editorial & Structural Gaps to Fix
1. **Unwritten / thin acts:**
   - **Act 8 (`To the Americas`)** was never rewritten in the friend-and-folklorist voice (`STATUS.md` stopped at Act 7) and reads like raw notes (~200 words).
   - **Act 3 (`Messina`)** and **Act 4 (`St Joseph's tables`)** are ~200-word stubs that speed past the human, architectural, and culinary life of the feasts.
   - **Curtain call** is a 4-line staccato list rather than a satisfying historical synthesis.
2. **Cold act starts & missing transitions:** Every act currently starts abruptly (`In May 1624 the plague reached Palermo`, `Messina has a feast on 3 June`, `Joseph, in the Gospels...`). Add 1–2-sentence conversational bridges linking each act to the preceding one so the whole piece reads as a single continuous story.
3. **Context gaps for readers unfamiliar with Sicily or Catholicism:**
   - `Sicily 101` lists 11 dynasties in 8 rapid bullets without explaining *what* that endless turnover meant for ordinary towns (why local civic saints became steady anchors when kings kept changing).
   - Act 1 mentions "under the Roman emperor Decius" without briefly explaining what Roman persecution of Christians actually meant; "Catania's own daily paper" appears suddenly; "the veil" isn't introduced before 1669.
   - Act 2 jumps straight into the plague without noting why Palermo's Senate had the civic muscle to elect a patron saint by vote.
   - Act 5 jumps abruptly from *decollati* & Frusteri → *pupi di zùccaru* (Day of the Dead) → an orphaned final ex-voto paragraph that belongs organically inside the *decollati* / sanctuary section (where Pitrè counted ~100 painted tablets!).
   - Several glosses (`*vampata*`, `*sacco*`, `*cimaruta*`, `*pupi di zùccaru*`, `*miraculu*`) are still thin one-liners that repeat or barely extend the body; key institutions (`Compagnia dei Bianchi`, `Steri palace`, `Council of Trent`, `furta sacra`) lack clickable call-outs.
4. **Stage pacing & visual polish:**
   - **Act 6** is ~7,566 px tall on desktop while the stage stays frozen on `albarello + eye + horn` even during the Spanish Inquisition archive fire and the *donne di fuora* fairy trials! Needs 3 distinct `_scene N_` beats (`6a` Inquisition/Steri & unit chart, `6b` *donne di fuora* / Bosch or Guidobono, `6c` Gratteri healers + evil eye).
   - **Acts 1, 5, 7, 8** can also benefit from 1–2 mid-act `_scene N_` beats (e.g., Act 1: bronze Agatha → bust returning on boat → veil/Etna; Act 5: night candles + ex-voto → sugar-doll/cemetery note; Act 7: Lucy & Agatha → Louis IX / Calvin boat; Act 8: Benedict's Atlantic ship → Americas route).
   - **Visual cleanup:** Clean up white halo/fringe pixels on `art/cut/agathabust.png` via `make_cutouts.py`; deduplicate the hero "Saints & Spells" title appearing identically in both the stage ribbon and the right-hand card banner; upgrade drawn props (`teller`, `occultist`, `ship`, `letter`) with subtle cut-paper shading/engraving lines.

---

## 2. Hard Guardrails for Every Hydrogen Sub-Agent

Every sub-agent prompt MUST enforce these rules:
1. **Zero invented facts (`CLAUDE.md`):** Every date, count, place, quote, name, and scholarly claim MUST come from `proj/sicilian-folk-magic/figures.md` and carry its exact row tag (`[X1-...]`, `[X2-...]`, `[X3-...]`) inline in draft prose. Do NOT use `unverified` rows as fact; mark single-source counts with the document named in the sentence (`D3`); write beliefs explicitly as beliefs ("devotees held…", "families told children…").
2. **Flag missing context instead of guessing:** If a smooth narrative bridge needs a historical fact not in `figures.md`, insert `[NEEDS-RESEARCH: <exact question>]` in the draft rather than making it up.
3. **Strict file isolation during parallel work:**
   - Wave 2 writing workers write ONLY to `proj/sicilian-folk-magic/drafts/<slug>.md`—NEVER edit `copy.md`, `figures.md`, or `build_piece.py` concurrently.
   - Only Wave 3's single Integration worker writes `proj/sicilian-folk-magic/copy.md`.
4. **Preserve every chart anchor, beat anchor, and figure anchor** (`_figure ..._`, `_cabinet ..._`, `_scene ..._`, `_[Unit chart...]_`, `**Stamp:** MYTH-CHECK · ...`, `[[...|...]]` call-outs, `*term*` glosses) unless explicitly tasked with adding/moving one.

---

## 3. Four-Wave Hydrogen Sub-Agent Execution Plan

> **Model selection:** Invoke every worker below with `Model: "flash"` (Hydrogen) unless Bryan requests otherwise.

### Wave 1 — Optional Targeted Context & PD Artwork Hunt (2 parallel workers; run ONLY if Bryan approves Q3/Q4)

#### Worker 1A: Context-Gap Researcher
- **TypeName / Model:** `research` / `flash`
- **Role:** `Sicilian Context Gap Researcher`
- **Inputs:** `proj/sicilian-folk-magic/figures.md`, `proj/sicilian-folk-magic/copy.md`
- **Output:** `proj/sicilian-folk-magic/research/I-context-gaps.md`
- **Task:** Find >=2 independent primary/scholarly sources (per ProofEr's `figures.md` rules—no wikis/blogs/tourism portals) for:
  1. Messina's civic rivalry with Palermo & physical description of the *vara* float (Act 3 context).
  2. Why Sicilian emigrants told the fava-bean famine legend & what foods/breads appear on St Joseph's tables (Act 4 context).
  3. Physical form of the *cimaruta* charm & a second scholarly source for the Sicilian oil-in-water evil-eye test (Act 6 context).
  4. Brief biographical facts on Benedict the Moor (life in Palermo, reputation for charity/humility) & Antonio of Noto (Act 8 context).
  5. Brief context on Decius's 250 CE persecution edict & Palermo's Steri palace / Spanish Viceroy archive (Acts 1 & 6).
- **Done criteria:** Clean table of candidate `X1-254+` / `X3-214+` rows with exact quotes, page numbers, and URLs/citations ready for cross-check into `figures.md`.

#### Worker 1B: Public-Domain Artwork Scout
- **TypeName / Model:** `research` / `flash`
- **Role:** `Open-Licensed Art Scout`
- **Inputs:** `proj/sicilian-folk-magic/research/F-images.md`, `proj/sicilian-folk-magic/art/originals/`
- **Output:** `proj/sicilian-folk-magic/research/I-art-candidates.md`
- **Task:** Search Wikimedia Commons, The Met Open Access, Wellcome Collection, Rijksmuseum, and NGA for public-domain or CC-BY/CC-BY-SA images (with exact file URL, museum/archive ID, date, artist, and license) for:
  1. St. Benedict the Moor (17th–19th c. painting, engraving, or statue) for Act 8.
  2. Palermo's Palazzo Chiaramonte-Steri or an early modern Sicilian/Spanish Inquisition engraving for Act 6a.
  3. A clearly licensed archival photo/print of a *ciarmavermi* or Sicilian folk healer / amulets if one exists to supplement or replace `13-gratteri-portrait.jpg`.
- **Done criteria:** Candidate list with verifiable license strings and dimensions; nothing downloaded or modified yet until Bryan approves.

---

### Wave 2 — Parallel Narrative & Voice Rewrites (4 parallel `self` / `flash` workers)

Each Wave 2 worker reads:
- `proj/sicilian-folk-magic/brief.md` (especially §2, §4, §12, Decisions log)
- `brief/taste/house.md` (`T10`, `T13`–`T21`, `T23`)
- `proj/sicilian-folk-magic/REFINEMENT-PLAN.md` (§1 Voice Guide & Before/After examples)
- `proj/sicilian-folk-magic/copy.md` (for existing anchors and structure)
- Their assigned slice of `proj/sicilian-folk-magic/figures.md`

#### Worker 2A: Overture, Orientalism & Sicily 101 (Sections 0–3)
- **Role:** `Opening & Framing Writer` (`self`, `Model: "flash"`)
- **Figures rows:** `X1-01`–`X1-81`, `X1-122a`, `X1-183`–`X1-184`, `X1-214`–`X1-225`, `X1-239`–`X1-246`, `X2-124`, `X2-126`, `X3-01`
- **Output:** `proj/sicilian-folk-magic/drafts/part1-opening.md`
- **Task:** Rewrite Sections 0–3 in the *A Distant Mirror* + wry Sicilian friend voice:
  - Keep Section 0 metadata/title, tightening the hero `dek` so it feels inviting rather than textbook-ish.
  - Smooth Section 1 (`Overture: the cards on the table`) from the tarot table scene into Court de Gébelin's Paris parlor, then seamlessly bridge to Sicily's "spooky treatment."
  - In Section 2 (`Where the goddess story came from`), weave Pitrè, Gramsci, de Martino, and the "Southern Question" (Farini, Lombroso, 1891 New Orleans) into a gripping, cohesive historical narrative explaining *why* outsiders needed Sicily to look ancient and magical.
  - In Section 3 (`Sicily 101`), keep the non-Catholic primer crystal clear, explain *why* revolving rulers (Byzantines, Arabs, Normans, Aragon, Spain) made local civic patron saints vital anchors, and transition smoothly into Act 1.
- **Done criteria:** Preserves `_scene 14_` and `_scene 15_`, all `[X...]` IDs, and `[[...|...]]` call-outs; zero clipped staccato prose.

#### Worker 2B: Three Cities & St Joseph's Table (Acts 1–4, Sections 4–7)
- **Role:** `Acts 1-4 Narrative Writer` (`self`, `Model: "flash"`)
- **Figures rows:** `X1-82`–`X1-150`, `X1-186`–`X1-206`, `X1-237`, `X2-02`–`X2-43`, `X2-67`–`X2-93`, `X2-98`–`X2-113`, `X2-150`–`X2-159` (+ Wave 1A additions if run)
- **Output:** `proj/sicilian-folk-magic/drafts/part2-acts1-4.md`
- **Task:**
  - **Act 1 (Catania):** Briefly contextualize Roman persecution under Decius so non-Catholic readers grasp *why* martyrdom mattered; introduce Agatha's veil *before* 1669; deepen the contrast between the jewel-crusted 1376 bust and 19th-century goddess theories; add a conversational bridge from Catania to Palermo.
  - **Act 2 (Palermo):** Give the 1624 plague narrative Tuchman-like immediacy—palace politics of Palermo's Senate electing Rosalia seven months before proof, Geronima La Gattuta's visions, Vincenzo Bonelli's despair on Monte Pellegrino—without losing the dry timing joke; bridge from Palermo to Messina.
  - **Act 3 (Messina):** Expand from stub into a vivid scene (the strait, the silver *vara*, how a 16th-century forged letter of AD 42 survived Vatican censorship, and why Messina shared a single hair with Palmi across the water in plague-time gratitude). Keep `_figure lettera_` and `_cabinet..._`.
  - **Act 4 (St Joseph's tables):** Expand from stub with sensory detail of the tables, the *virgineddi*, the *vampata* bonfires, the emigrant fava-bean famine legend, and the REIS tally; bridge smoothly into nightfall and Act 5.
- **Done criteria:** Every claim tagged `[X...]`, preserves `_figure lettera_`, `_cabinet..._`, timeline/strip anchor paragraphs (`Then the island changed hands...`, `Here is the timeline...`).

#### Worker 2C: The Night Acts (Acts 5–6, Sections 8–9)
- **Role:** `Night Acts Narrative Writer` (`self`, `Model: "flash"`)
- **Figures rows:** `X1-151`–`X1-182`, `X1-207`–`X1-212`, `X1-227`–`X1-236`, `X1-247`–`X1-249`, `X2-124`, `X3-01`–`X3-117` (+ Wave 1A additions if run)
- **Output:** `proj/sicilian-folk-magic/drafts/part3-acts5-6.md`
- **Task:**
  - **Act 5 (*The dead who help*):** Deepen the *Compagnia dei Bianchi* and the theological logic of the *good thief* and purgatory so any reader grasps *why* executed murderers became street intercessors; connect Pitrè's ~100 painted ex-voto tablets directly into the *decollati* church narrative (removing the orphaned final paragraph!), then bridge organically into 2 November (*Festa dei Morti*) and *pupi di zùccaru* so there is no tonal whiplash.
  - **Act 6 (*Witches, healers and the evil eye*):** Structure cleanly into three paced movements with explicit stage-beat comments/placeholders (`_scene 16_` Steri/Inquisition, `_scene 17_` *donne di fuora*, `_scene 9_` Gratteri healers & amulets—final numbers assigned by Worker 3B):
    - 6a: 1487–1782 Spanish Inquisition in Palermo's Steri palace, the 1783 archive bonfire ("reasons of state"), who actually died (200–440 conversos early, 25–52 later including Abbate's 36 Protestants, only 2 men for witchcraft), keeping `_[Unit chart...]_` anchor exact.
    - 6b: The *donne di fuora*—give Lauria de Pavia, Catarina Calandrino, and Gracia la Chiaczisa room to breathe as real people caught between village healing and inquisitors' demonology; preserve `_figure bosch_` and `_figure guidobono_`.
    - 6c: The evil eye (*malocchiu* / *l'ucchiatura*) and Gratteri's *ciarmavermi* & *scantu* healers; preserve `_figure gratteri_`; bridge cleanly to morning and Act 7's relic cabinet.
- **Done criteria:** Zero invented facts, every `[X...]` preserved, `_[Unit chart...]_` and `_figure ..._` anchors intact.

#### Worker 2D: Relics, Americas, Curtain Call & Reference Notes (Acts 7–8, Curtain Call, Call-outs & Glosses)
- **Role:** `Acts 7-8 & Apparatus Writer` (`self`, `Model: "flash"`)
- **Figures rows:** `X2-41`–`X2-66`, `X2-91`–`X2-159`, `X1-71`, `X1-251`, `X3-115`, `X3-122`–`X3-213` (+ Wave 1A additions)
- **Output:** `proj/sicilian-folk-magic/drafts/part4-acts7-8-end.md`
- **Task:**
  - **Act 7:** Smooth prose transitions around Lucy of Syracuse, Agatha's scattered limbs, Louis IX's boiled remains (keeping `Palermo Cathedral says its Chapel of the Relics...` paragraph intact as the `cabinet_html()` hook and `_cabinet louis_` intact), Gregory the Great's 594 refusal, Nicaea 787, *furta sacra*, Calvin's 1543 *Treatise* + Krasinski's footnote, and 2017 canon law.
  - **Act 8 (*To the Americas*):** Complete rewrite from scratch in the *A Distant Mirror* + Sicilian friend voice—shared Spanish crown (1516–1713), Benedict the Moor's story and Black Catholic brotherhoods (Lisbon 1609 → Brazil → Venezuela's *chimbangueles* drums), Antonio of Noto, Rosalia in New Spain, Joseph as patron in 1555, debunking the 19th-century-emigrant myth, and explaining why shared baroque candles/gold and 2 November customs are parallel Catholic evolutions rather than Sicilian exports.
  - **Curtain call:** Replace the 4-line staccato closer with a resonant, reflective 2-paragraph finale (modeled on Example 3 above).
  - **Call-outs & Glosses:** Deepen thin glosses (*vampata*, *sacco*, *pupi di zùccaru*, *miraculu*, *cimaruta*) so EVERY click teaches something genuinely interesting (`T15`), and draft 4 new call-outs (`Compagnia dei Bianchi`, `Steri palace`, `Council of Trent`, `furta sacra`) using only verified `figures.md` facts.
- **Done criteria:** Preserves all required hooks (`_cabinet louis_`, `**Rosalia** crossed to New Spain...` for `route_svg()`), zero invented facts.

---

### Wave 3 — Integration, Citation Audit & Stage/Cutout Polish (2 sequential `self` / `flash` workers)

#### Worker 3A: Copy Integrator & Citation Auditor
- **Role:** `Lead Copy Editor & Auditor` (`self`, `Model: "flash"`)
- **Inputs:** `proj/sicilian-folk-magic/drafts/part1-opening.md` through `part4-acts7-8-end.md`, `proj/sicilian-folk-magic/figures.md`, `proj/sicilian-folk-magic/copy.md`
- **Output:** Updated `proj/sicilian-folk-magic/copy.md`
- **Task:**
  1. Merge the four drafts cleanly into `proj/sicilian-folk-magic/copy.md` (preserving header/format conventions expected by `build_piece.py`: `## N · ...`, `**Stamp:**`, `## Call-outs`, `## Glosses`).
  2. Smooth all Act-to-Act transitions and eliminate any repetitive phrasing, leftover Snopes-y quips, or staccato triplets (`T14`).
  3. Run a Python verification script checking: (a) every `[X...]` ID in `copy.md` exists in `figures.md`, (b) zero `unverified` rows are used, (c) zero `[NEEDS-RESEARCH]` tags remain unresolved, (d) every `build_piece.py` anchor (`Then the island changed hands`, `Here is the timeline`, `_[Unit chart`, `Palermo Cathedral says its Chapel of the Relics`, `**Rosalia** crossed to New Spain`) matches verbatim, (e) every `*term*` gloss in `## Glosses` actually appears in the prose.

#### Worker 3B: Stage Beats, Cutouts & Visual Builder
- **Role:** `Stage Choreographer & Builder` (`self`, `Model: "flash"`)
- **Inputs:** Updated `proj/sicilian-folk-magic/copy.md`, `proj/sicilian-folk-magic/build/build_piece.py`, `proj/sicilian-folk-magic/build/make_cutouts.py`, `proj/sicilian-folk-magic/build/template.html`
- **Outputs:** Updated `make_cutouts.py` / `art/cut/agathabust.png`, `build_piece.py`, `template.html`, rebuilt `pieces/sicilian-folk-magic.html`
- **Task:**
  1. Add new stage scenes in `SCENES` (and matching `_scene N_` beats in `copy.md`) so long acts don't stall on one frozen puppet setup—especially **Act 6** (`6a` Steri/Inquisition placard, `6b` *donne di fuora* / Bosch or Guidobono print, `6c` `albarello + eye + horn`), plus beats in **Act 1** (bronze Agatha → bust on boat), **Act 7** (Lucy + bust → Louis IX / Calvin boat), and **Act 8** (ship + Benedict card/artwork if cleared in Wave 1B).
  2. Clean up white edge-matte pixels on `art/cut/agathabust.png` in `make_cutouts.py` (feather/erode alpha border 1–2 px before white cutout outline).
  3. Eliminate the duplicate "Saints & Spells" title ribbon in Hero (keep the stage ribbon as the hero banner OR replace the right card's duplicate `.ribbon` with a clean kicker/rule so "Saints & Spells" doesn't repeat side-by-side on desktop or stacked on mobile).
  4. Add subtle cut-paper shading/engraving detail to drawn props (`teller`, `occultist`, `ship`, `letter`).
  5. Rebuild via `build_piece.py`, copy to `pieces/sicilian-folk-magic.html`, run `tools/add_view_counter.py` and `tools/check_offline.py`.

---

### Wave 4 — Full Browser QA & PR Submission (1 `self` / `flash` worker)

- **Role:** `Browser QA & PR Verifier` (`self`, `Model: "flash"`)
- **Inputs:** Rebuilt `pieces/sicilian-folk-magic.html`, `tools/check_offline.py`
- **Outputs:** Fresh PNGs in `proj/sicilian-folk-magic/qa/`, updated `proj/sicilian-folk-magic/STATUS.md` & root `STATUS.md`, PR against `main` (never merge)
- **Task:**
  1. Run `python3 tools/check_offline.py pieces/sicilian-folk-magic.html`.
  2. Run Playwright across **Desktop (1440×900)**, **Tablet (768×1024)**, **Phone (390×844)**, and **Print (`@media print`)**:
     - Verify 0 console/page errors, 0 horizontal overflow at all 3 widths, all images (`naturalWidth > 0`) and embedded fonts loaded.
     - Test every gloss, call-out, figure zoom, relic cabinet drawer & thumbnail, fast scroll down/up, `prefers-reduced-motion`, and keyboard (`Tab` / `Escape`) navigation.
     - Capture & visually inspect screenshots for every act and interactive state via `read_file`.
  3. Update `STATUS.md` logs, commit cleanly on a dedicated PR branch, push, and open a PR against `main`.
