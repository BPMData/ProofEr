# Brief: Terezín, *I Never Saw Another Butterfly*, and *Vedem* (`terezin-vedem`)

Status: APPROVED 2026-11-22 by Bryan Murphy · Stage: done · Mode: from scratch · Budget: deep · Client: Bryan Murphy · Sign-off: Bryan Murphy
Usage: Antigravity (Gemini 4 Hydrogen High) · All 4 stages complete (9 research workers, 28 checked rows, 3 stills, full offline build & Chromium QA)

## 1. The ask
A scrolling **interactive data essay** accompanying `nazi-victims-all-groups.html` and `holocaust-by-country.html`, focused on **Terezín (Theresienstadt)**, the children's poetry and artwork preserved in ***I Never Saw Another Butterfly***, and ***Vedem***, the secret boys' literary magazine from Home L417. Built for **high school students** (Danbury High School, usable in class) as well as the **general public** online (shared to Facebook groups and social media).

## 2. Purpose and tone
- **Know:** The scale of what happened inside Terezín beneath the Nazi "model ghetto" facade—how many children and adults passed through, starved, were deported, and died; how the June 1944 Red Cross walkthrough and propaganda film were staged; and what the children and teenagers recorded in *I Never Saw Another Butterfly* and *Vedem* while living through it.
- **Feel:** That genocide is a reprehensible crime for which there can be no forgiveness, and that a single curated video, photograph, or walkthrough tour in person is never enough to verify what is actually happening on the ground—with a heavy, **not directly stated** resonance with the current Israeli genocide in Gaza.
- **Do:** Question single-tour, single-video, or single-photo "proof" when powerful institutions curate what outsiders are allowed to see, and look for primary voices and full ground-level data instead.
- **Tone:** Heavy, sober, unsparing, respectful—explicitly "not something for fun." Must never feel gamified, cute, sensational, or like homework.

## 3. How it's read
Scrolling interactive data essay read on laptops/desktops and phones (social media links and classroom use), both **read alone** online and potentially **walked through in class**. Must read clearly up close on a screen and remain readable if projected in class.

## 4. The subject
- **The story behind the numbers:** Terezín was presented to the world (and to the June 1944 International Committee of the Red Cross inspection and propaganda film) as a humane "model settlement" and "spa town," even as overcrowding, starvation, disease, and systematic transports to extermination camps killed the vast majority of those sent there—including almost all of the children. Meanwhile, inside Barracks L417 and across the ghetto, young people documented the truth in *Vedem* and in the poems and drawings later collected as *I Never Saw Another Butterfly*.
- **Common misconceptions:** That Terezín was a "benign" or "privileged" camp where people lived comfortably (a Nazi propaganda lie amplified by the staged 1944 Red Cross walkthrough), or that a single external inspection/film proves humane treatment.
- **What it must never say, compare, rank, or show:**
  - Never state the Gaza connection explicitly; let the indictment of curated tours, single photographs, and single videos carry the weight cleanly without breaking the historical frame.
  - Never rank suffering across groups or treat victims as numbers without humanity.

## 5. The questions the numbers must answer
| # | Question | Weight | Why it matters to the reader |
|---|---|---|---|
| Q1 | **Terezín scale & fate:** How many total prisoners (and specifically how many children under 15) were sent to Terezín (1941–1945), how crowded was the town (pre-war population vs. peak ghetto population), how many died inside Terezín vs. were deported east, and how many survived? | main | Grounds the real human scale behind the "model ghetto" facade. |
| Q2 | **The staged walkthrough & film:** What happened before and during the June 23, 1944 Red Cross visit (*Stadtverschönerung* / "beautification," deportations right before the visit to lower headcount, duration/route of Maurice Rossel's tour) and the 1944 propaganda film (*Theresienstadt*)—and what happened to the participants afterwards? | main | Proves concretely why one walkthrough tour, one photograph, or one video cannot verify conditions on the ground. |
| Q3 | ***I Never Saw Another Butterfly* & the children:** How many drawings/poems survived, who taught and hid them (Friedl Dicker-Brandeis, suitcases), what do the survival rates of Terezín's children look like, and what are the verified facts of Pavel Friedmann and *"The Butterfly"* (4. 6. 1942)? | main | Connects the statistical scale directly to the children's creative witness. |
| Q4 | ***Vedem* (Home L417):** When was *Vedem* produced, how many issues/pages survived, how many boys lived in L417 and how many survived, who were the key editors/writers (Petr Ginz, Kurt Kotouč, Josef "Pepek" Stiassny, Hanuš Hachenburg, Valtr Eisinger), and how was it hidden and recovered? | main | Shows teenagers consciously acting as journalists and moral witnesses inside the ghetto. |
| Q5 | **Text, copyright & licensed photography:** Exact wording, translators, dates, and copyright/licensing status for Pavel Friedmann's *"The Butterfly"*, Pepek's *Vedem* editorial, and verified public-domain / CC-licensed historical photographs of Terezín. | main | Ensures full attribution, legal clarity, and properly licensed historical photography (client confirmed photographs are important where licensed). |

**Client-supplied copy (verbatim):**
1. **Pavel Friedmann, *"The Butterfly"* (4. 6. 1942)** — supplied as screenshot (p. 39 of *I Never Saw Another Butterfly*):
   - Text visible in screenshot: *"The last, the very last, / So richly, brightly, dazzlingly yellow. / Perhaps if the sun's tears would sing / against a white stone. . . . / Such, such a yellow / Is carried lightly 'way up high. / It went away I'm sure because it wished to / kiss the world good-bye. / For seven weeks I've lived in here, / Penned up inside this ghetto. / But I have found what I love here. / The dandelions call to me / And the white chestnut branches in the court. / Only I never saw another butterfly. / That butterfly was the last one. / Butterflies don't live in here, / in the ghetto. / 4. 6. 1942 Pavel Friedmann"*
2. **Pepek (Josef Stiassny), *Vedem* Editorial** — supplied from `https://www.vedem-terezin.cz/en/rambles/22.html` (on "Loonie" and "idiot," the mother behind the barred windows selling crumpled paper slippers, and *"Boys, respect your comrades, respect yourselves. You are responsible not only for your actions, but also for your words."*).

## 6. Research plan
- **Autonomous multi-pass Deep Research (`auto-piece`, `Budget: deep`):** Run isolated parallel Pass 1 research workers via `.agents/workflows/research_piece.py` across primary/authoritative Holocaust archives and scholarship (USHMM, Yad Vashem, Památník Terezín / Terezín Initiative, Jewish Museum in Prague, `vedem-terezin.cz`, ICRC archives, Wikimedia Commons / Bundesarchiv for licensed photos), followed by Pass 2 gap-fill and primary-source verification before synthesizing `proj/terezin-vedem/figures.md`.

## 7. Structure and reading order
**DRAFT** (to be finalized after research & mockup review):
1. Opening hook: the discrepancy between the "model town" the outside world was shown and the lived reality inside the fortress walls.
2. Spatial & demographic reality: pre-war garrison town vs. ghetto overcrowding, deaths inside Terezín, and deportations east.
3. The anatomy of a staged truth: the 1944 Red Cross walkthrough ("beautification," pre-visit deportations, curated route) and the propaganda film—why one tour/photo/video fails.
4. Through the children's eyes: *I Never Saw Another Butterfly* (Friedl Dicker-Brandeis, the preserved suitcases, Pavel Friedmann's *"The Butterfly"* prominently featured with full attribution, and child survival figures).
5. The boys of L417 and *Vedem*: weekly journalism in secret, Pepek's editorial on language and human dignity prominently featured with full attribution, how the pages survived, and the fate of the boys.
6. Closing synthesis, full Sources, Attribution & Licensing notes, and "About these numbers."

## 8. Brand and contrast
Aesthetic must **pair** with Bryan's two companion Holocaust interactive data essays (`nazi-victims-all-groups.html` and `holocaust-by-country.html`)—restrained, quiet, high-contrast archival typography and palette—inspected only once the layout/build gate opens (`CLAUDE.md` / `notes/architecture.md`).

## 9. Language
**English only** (client confirmed: match the two companion Holocaust pages).

## 10. Call to action and credit
- **Reader next step:** Reflect on how propaganda works and seek primary-source, multi-angle documentation before accepting curated official narratives.
- **Credit:** Bryan Murphy / ProofEr, with full attribution and licensing credits for *I Never Saw Another Butterfly*, *Vedem*, and any licensed historical photographs used.

## 11. Hard limits
- Historical photographs are important and **should be used where license permits** (Public Domain, CC0, CC BY, CC BY-SA, or verified open archival licenses; full attribution given, embedded offline).
- Check copyright/licensing status carefully for Pavel Friedmann's *"The Butterfly"* and Pepek's *Vedem* editorial; give full attribution and verify legal permissions/fair-use framing if still under copyright (e.g., 1959/1964 translation).
- No unverified numbers, no invented quotes, no gamification of deaths, and keep the Gaza connection strictly unstated.

## 12. Taste
`Taste: house. Applies: T01–T08, T10 (myths checked: Nazi "model ghetto" propaganda & child-survival approximations), T13 (asides stay side notes), T14 (Bryan's voice: clause-heavy sentences with colons and semicolons, zero clipped AI cadence), T15 (explain name-drops behind drill-downs), T16 (noticeable section question titles), T17 (explain unusual units), T18–T21 (scroll-driven where physical/temporal, persistent frame). Overrides: T12 OFF by explicit client request — dark slate ground (`#15171A` / `#1C1F23` / `#E7E4DD` matching `:root[data-theme="dark"]` of `nazi-victims-all-groups.html` and `holocaust-by-country.html`) to evoke the weight and back-breaking labor of stone, with light print styles preserved via `@media print`.`
- **Client taste (`bryan.md`):** Loves NYT scrollytelling and big illustrated DK-style reference books; hates generic AI web templates, rounded cards everywhere, and anything that reads like homework.

## 13. Craft bar
Default (`brief/CRAFT.md`): one five-second message, honest zero-baseline/proportional charts, visual idea grown from the subject, uncertainty shown honestly, dignity on human subjects.

## 14. Technical
Single offline HTML file (`pieces/terezin-vedem.html`), Google Fonts embedded locally via `tools/embed_fonts.py`, licensed photos embedded as inline data URIs (sized cleanly), text alternatives for every chart, keyboard/screen-reader accessible, clean print view, tested in Chromium (`bryan.md`).

## 15. Deliverables
- `pieces/terezin-vedem.html`
- Updated `index.html` card linking alongside `nazi-victims-all-groups.html` and `holocaust-by-country.html`
- Updated `STATUS.md` and `proj/terezin-vedem/STATUS.md`

## 16. QA
Default checks (`TEMPLATE.md` §16): every fact in `figures.md` with status `checked`, sources + "About these numbers," honest scales, WCAG AA contrast, `tools/check_offline.py` pass, desktop + phone Chromium screenshots (`proj/terezin-vedem/qa/`) visually inspected, print preview verified.

## 17. Approval and success
Sign-off by **Bryan Murphy** at two gates:
1. Brief (`APPROVED 2026-11-22` -> `Stage: research`)
2. Concise outline + self-critiqued visual mockups (`proj/terezin-vedem/layout.md` -> `APPROVED`, unlocking `Stage: build`).

## 18. Open questions
None (all interview questions resolved; copyright/licensing and exact numbers assigned to Stage 2 research).

## Decisions log
- `2026-11-22` · Scrolling interactive data essay (heavy, not for fun); audience HS students (class) + general public (Facebook/social media); takeaway: genocide is unforgivable and one video/photo/walkthrough tour cannot verify conditions on the ground (heavy, unstated resonance with Gaza); `Deep` research budget; focus on *I Never Saw Another Butterfly* (Pavel Friedmann screenshot) and *Vedem* (Pepek editorial supplied). · Captured in §1–§5.
- `2026-11-22` · Approved brief; confirmed slug `terezin-vedem`, English-only, include licensed historical photographs with attribution, emphasize and attribute Friedmann's *"The Butterfly"* and Pepek's *Vedem* editorial (verify copyright status during research). · Status set to `APPROVED`, `Stage: research`.
- `2026-11-22` · Chose Option B (include full English poem & editorial under non-commercial educational commentary with full attribution) and rejected boxed parchment still aesthetic in favor of matching `pieces/nazi-victims-all-groups.html` and `pieces/holocaust-by-country.html`. · Rebuilt `layout.md` and `stills/` to match the companion pieces' exact stone palette (`#E4E3DF`/`#EFEEEB`/`#7B1D2A`), `Spectral` + `Public Sans` typography, unit grids, borderless rows, and `.factors` columns.
- `2026-11-22` · Approved companion aesthetic, requesting the companion pieces' dark-slate mode (`#15171A` / `#1C1F23` / `#E7E4DD`) as the default look to evoke the heaviness of stone and back-breaking labor. · Overrode `T12` in §12, updated `layout.md` to `APPROVED` (`Stage: build`), and switched dark-slate tokens to default.
