# Brief: Sicilian folk magic (working title)

Status: APPROVED Nov 22, 2026 by Bryan (with amendments) · Stage: research · Mode: from scratch · Budget: standard to deep · Client: Bryan Murphy · Sign-off: Bryan
Usage: Opus 5.5 (Claude Duet thread) · interview: not measured (the Duet app shows no per-stage share)

_Made from `brief/TEMPLATE.md`. **ASK** = missing, **DRAFT** = Claude's draft, **Claude's call** = delegated by the
client. Quotes are Bryan's own words, Nov 22, 2026._

## 1. The ask
- **Topic:** "An upbeat, dynamic, ecletic, erudite but fun and occultist piece about the intersection and syncretism
  of sicilian catholicism with pagan and folk magical traditions."
- **Format:** "medium to long scrolling interactive essay", published on the ProofEr site (`pieces/`, linked from
  `index.html`).
- **Audience:** "bored history nerds on mobile or pc"; "educated, clever, witty adults".
- **By when:** no deadline (Bryan). Byline date: Nov 22, 2026 ("todays date").

## 2. Purpose and tone
- **Know:** "how italian catholicism absorbed local pre extant indigenous traditions, and what sicilian catholics
  practice that the rest of catholicism does not."
- **Feel:** "edified, amused and edutained."
- **Do:** nothing asked for (**DRAFT**: a sources and further-reading list is the next step for the curious).
- **Stance:** "No need to be disrespectful but no need to pretend this shit is 100% real. More like a cultural
  anthropologist analyzing the mechanism of transfer and syncretism respectfully but without ascribing to it. Just a
  hint of Barnes and noble white girl tarot card self help mysticism energy."
- **Amended at approval:** "Not that doesnt believe a word of it. More like scully and mulder from xfiles combined:
  acknowledge the optics of it but secretly DL "i want to believe." I mean, some sicilians think the charms work
  magic so the belief should be clearly defined." So: Scully's eye for the evidence and the optics, Mulder's quiet
  wish that it's true. The piece never claims the magic works and never sneers that it doesn't; where people believe
  a charm works, it says so plainly, as their belief, with what they believe it does. The tarot-shop mysticism is a
  hint of flavor, not the voice.
- **Tone words:** upbeat, dynamic, eclectic, erudite, fun, occultist. **Must not feel like:** homework, a sneer at
  believers, or a sincere spellbook.

## 3. How it's read
- Phone, PC and tablet: "Should also work on tablet." "Probably not gonna be projected."
- Read alone, scrolling, for as long as the reader likes. Long read: drill-downs carry the depth (T15).

## 4. The subject
- **Client's starting idea, not yet a fact:** Sicilian (and Italian) Catholicism absorbed older local traditions,
  and Sicily keeps practices the rest of Catholicism doesn't. Research tests each claim; when the reports come back,
  say in one line where they support, complicate or overturn it, and ask before building on a flipped version.
- **Primer needed:** readers need the mechanism (what syncretism, folk Catholicism and "pagan survival" mean, and
  why scholars argue about them) before the examples make sense. Its questions are in the first research pass (Q5).
- **Landmines.** Bryan: "yeah neither of those examples. Tbh i trust your judgement on this one be normal about it."
  His two: never "Sicilians are superstitious peasants"; never treat living practitioners as a museum exhibit. The
  rest Claude drafted and Bryan approved ("yes with my amendments above"):
  - No mafia, *Godfather* or crime framing; organized crime appears only if research ties it to a specific
    practice, and then as a sourced fact, not flavor.
  - No claim that a practice "survived unbroken from pagan antiquity" unless the sources trace it; legends
    the research can't back get a myth-check label (T10).
  - Jokes aim at relic markets, institutions, marketing and myths (`clients/bryan.md`), never at the faith
    of living Catholics or practitioners.
  - The piece doesn't present a charm as working magic in its own voice, and doesn't dismiss it either: belief is
    defined clearly as belief ("practitioners hold that ..."), with what it is for and who holds it; charms are quoted
    as recorded texts, with their source.
  - No "backward South" or North/South Italy ranking.
  - Inquisition and witch-trial defendants are people, not punchlines.
  - No photos of identifiable living people at rituals unless the license allows it.

## 5. The questions the numbers must answer
Bryan: "we can downplay the numbers and strict figures for this one. Dates in history, counts of saints and feast
days, number of churches with reliquaries, number of churches claiming to all have the same relic (how many
fingerbones can one dead saint have?) are all fair game." Numbers are supporting cast; dates and counts carry the
essay, and the stories carry the reader. Every date, name, count and quoted charm still needs two sources.

| # | Question | Weight | Why it matters to the reader |
|---|---|---|---|
| Q1 | When does each practice or belief first show up in the record, and how do those dates line up with Sicily's successive rulers and peoples? | main | The timeline is the spine: it shows what could have blended with what. |
| Q2 | Which practices are distinctly Sicilian, kept there and not in Catholicism at large (saint cults, feasts, healers, charms, votive customs), and what does each one involve? | main | Bryan's "know" line: "what sicilian catholics practice that the rest of catholicism does not." |
| Q3 | How many saints, feast days and processions does Sicily keep, and which are said to sit on older cults, with what evidence? | main | Shows the scale of the saint calendar and where the syncretism claims cluster. |
| Q4 | How many churches hold reliquaries, and how many claim the same relic? ("how many fingerbones can one dead saint have?") | main | The essay's best running joke, and a real story about relic markets. |
| Q5 | Primer: what do "syncretism", "folk Catholicism" and "pagan survival" mean, and where do scholars disagree? | main (primer) | Readers need the mechanism before the examples. |
| Q6 | What do Inquisition records and ethnography say about folk healers, the evil eye and the *donne di fuora*, and how many cases are recorded? | main | Bryan: "main point, how could they not be?" The best-documented meeting point of Church and folk magic. |
| Q7 | Is there a real connection between Sicilian and Latin American Catholicism ("They both love hella candles and gaudy shit")? Shared Spanish rule, baroque, saints? | main if the research shows substance, otherwise side | Bryan: "maybe a main point towards the end of the piece, if there's substance there as shown by the research. Otherwise side note." |

## 6. Research plan
- **Changed from the repo default (Bryan):** "You run the research tasks yourself via yourself or subagents, I want to
  see how Duet handles this." Claude runs at least two independent research passes per question group (separate
  subagents with web search, so they don't share mistakes), then a gap-fill and fact-check pass, all saved to
  `proj/sicilian-folk-magic/research/`; then cross-checks them into `figures.md`. Disagreements and single-source
  figures go to Bryan to settle. "we have api usage to burn." T05 (two or more tools) is met by independent passes,
  not separate products; noted as an override in §12.
- **Sourcing rules (Bryan's standing rules):** never cite Holocaust deniers or revisionist sites, or wikis and
  aggregators like Fandom or Kiddle; Medium and Reddit are leads only, never the citation for a figure; trace every
  figure to the original institution, book or journal. For this topic, favor academic folklore, anthropology and
  religious-history sources, primary ethnography, published Inquisition records and diocesan or church records.
- **Images** are research too: public-domain or open-licensed artworks (baroque and classical paintings, saints'
  images, ex-votos) with their license and source, for the cutout look in §8.

## 7. Structure and reading order
Decided at concepts and layout. **DRAFT** idea to show then: the primer first, then a tour of practices in timeline
order, with a running relic tally visible the whole way (T20).

## 8. Brand and contrast
- **Look:** "let's go baroque sicilian x the video game franchise "rock of ages" (i.e. papercraft cutouts of classical
  artworks staged or animated as puppets. Google rock of ages)". So: baroque Sicilian color and ornament (painted
  tiles, gold, votive candles) with cut-paper puppets made from public-domain paintings, staged and moved on scroll.
- **Original look only:** the game is a style cue; no game assets, characters, names or branding appear. Every
  cutout comes from a public-domain or open-licensed artwork, license noted.
- Colors and fonts: **Claude's call**, shown as a choice panel at concepts (T03). Open-licensed fonts only.
  Contrast: WCAG AA, reported honestly; dark text on gold and other light brights (T07).

## 9. Language
"English only, sicilian where appropriate but each term is defined inline or with a clickable drilldown, etc."

## 10. Call to action and credit
- **Credit:** "bryan murphy", dated Nov 22, 2026.
- **Next step:** **DRAFT** sources and further reading.

## 11. Hard limits
- Images: public-domain or open-licensed only; nothing from the game; no identifiable living people without a
  license that allows it.
- Claims: nothing about magic presented as working; no "pagan survival" stated as fact without sources.

## 12. Taste
`Taste: house. Applies: T01–T08, T10, T13–T21 (screen, read alone). Overrides: T05 (research runs as independent
Claude passes, at Bryan's ask); T12 (light paper ground) to be decided at concepts, since the baroque candlelit look
may want darker grounds.`
Bryan's named loves and hates (`brief/clients/bryan.md`) carry over: loves the NYT "The Untold Story of Sushi in
America" scrollytelling and DK-style illustrated reference books; hates the homogeneous default AI web look, rounded
cards everywhere, anything that reads like homework.

## 13. Craft bar
Default (`CRAFT.md`); this piece adds:
- The cutout puppets move because the story moves (a saint slides over an older goddess, a relic multiplies), never
  as decoration (T02, T18); reduced motion still respected (repo rule).
- Every Sicilian term has a plain-English gloss at first use (T15, T17).

## 14. Technical
Repo defaults. Images inlined, compressed for phone.

## 15. Deliverables
One web page, `pieces/sicilian-folk-magic.html` (final slug can follow the title), linked from `index.html`.

## 16. QA
Defaults, plus: every image has its license and source in the sources section; tested in Chromium at desktop, phone
and tablet widths.

## 17. Approval and success
Bryan signs off. Success: readers leave "edified, amused and edutained".

## 18. Open questions
None at approval. Research may raise disputed figures for Bryan to settle.

## Decisions log
- Nov 22 · "medium to long scrolling interactive essay"; "bored history nerds on mobile or pc ... Should also work on
  tablet ... educated, clever, witty adults"; "standard to deep, we have api usage to burn. You run the research tasks
  yourself via yourself or subagents" · format, audience and budget set; research moves from the client to Claude.
- Nov 22 · tone: "Both ... a cultural anthropologist analyzing the mechanism of transfer and syncretism respectfully
  but without ascribing to it"; numbers: "we can downplay the numbers and strict figures for this one"; landmines:
  "i trust your judgement on this one be normal about it" · stance set; Q1–Q4 from his list; landmines drafted for
  his approval.
- Nov 22 · know/feel, look ("baroque sicilian x ... rock of ages"), credit ("bryan murphy, todays date"), language
  ("English only, sicilian where appropriate but each term is defined") · brief drafted, Stage: brief.
- Nov 22 · approved: "yes with my amendments above"; voice "scully and mulder from xfiles combined: acknowledge the
  optics of it but secretly DL "i want to believe""; "some sicilians think the charms work magic so the belief
  should be clearly defined"; "no deadline"; trials and healers "main point, how could they not be?"; Latino link
  "maybe a main point towards the end of the piece, if there's substance there" · Status APPROVED, Stage: research.
