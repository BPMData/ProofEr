# Brief: Glazed vs. Unglazed Clay Cookware

Status: APPROVED 2026-11-20 by Bryan Murphy · Stage: done · Mode: from scratch · Client: Bryan Murphy · Sign-off: Bryan Murphy
Usage: Gemini 4 Hydrogen (High) · ~36% of 5-hr window / ~8% weekly on $20/mo plan (entire end-to-end run incl. 11 workers, 3 stills, build/QA, and 3 PRs)

## 1. The ask
- **Topic:** Differences between glazed and unglazed clay in clay cookware during cooking—comparing thermal behavior, moisture retention, thermal shock, browning, flavor memory, and stovetop compatibility across classic clay pots (glazed clay, soaked unglazed Römertopf, burnished La Chamba) and electronic multi-cooker clay inserts.
- **Format:** Deep interactive data essay — substantive, well-paced, zero fluff or unnecessary padding.
- **Audience:** General-purpose cookware and food-science enthusiasts (anchored by Bryan's real-world comparison of clay multi-cooker inserts).
- **Where it's seen:** ProofEr site (`pieces/clay-cookware.html`, linked from `index.html`), read alone on desktop/laptop and phone.
- **By when:** No deadline.

## 2. Purpose and tone
- **Know / feel / do:** Readers should understand *physically* why glazed and unglazed clay behave differently in the oven, on the stove, and inside an electric multi-cooker—when unglazed clay is worth the fuss (and when it breaks or ghosts yesterday's garlic), why shiny La Chamba isn't glazed, and what actually separates a glazed clay multi-cooker insert (Magnifique) from an unglazed one (VitaClay) or standard metal inserts.
- **Tone & visual feel:** Clean test-kitchen notebook — crisp diagrams, calm, analytical, with Bryan's dry humor and clause-heavy prose (`brief/clients/bryan.md`, T14). Must NOT feel like rounded-card AI web slop, homework, or a cookware-blog toxin panic piece.

## 3. How it's read
- Desktop/laptop primary and mobile phone; scrolled alone at the reader's own pace.

## 4. The subject
- **The story behind the numbers:** Classic home-cook clay lore mixes together wildly different materials—soaked porous terracotta bakers (Römertopf), glazed stoneware, burnished micaceous earthenware (La Chamba), and modern electric multi-cooker clay inserts (Magnifique glazed vs. VitaClay unglazed Zisha)—all while comparing them implicitly against aluminum non-stick and cast-iron multi-cooker inserts.
- **Client's working observations to test in research:**
  - Amateurs destroy clay pots most often via thermal shock.
  - Clay's thermal mass & insulation noticeably change cooking temps (Bryan's experience: lidded Römertopf often runs ~50°F hotter than published recipe temps).
  - La Chamba looks shiny even though it is unglazed, and is stovetop-safe even though putting clay on a burner feels nerve-wracking.
  - None work directly on induction without a steel induction plate, and it's unclear whether a diffuser plate harms clay.
- **Landmines (never say, compare, rank, or show):**
  - **Do NOT** turn this into a weird moral panic about toxins or lead glazes. Only include a brief, strictly factual note on glaze safety if research shows a genuine modern concern (e.g., unverified artisanal low-fire glazes vs. modern commercial food-contact standards).

## 5. The questions the numbers must answer
| # | Question | Weight | Why it matters to the reader |
|---|---|---|---|
| Q1 | Thermal mass, thermal conductivity, and cooking temperatures across glazed clay, unglazed clay, aluminum, and cast iron—including whether lidded Römertopf recipes really run ~50°F hotter | main | Explains why clay heats slowly, buffers temperature swings, and changes oven setpoints |
| Q2 | Porosity and water/steam loss over 2, 4, and 8-hour slow cooks (soaked unglazed Römertopf vs. dry unglazed insert vs. glazed clay vs. metal)—do you need to top up water? | main | Directly answers how much moisture escapes and when clay self-bastes vs. dries out |
| Q3 | Thermal shock mechanics (thermal expansion, $\Delta T$ limits, wet vs. dry clay, oven vs. electric multi-cooker heating ramp) | main | Shows why amateurs crack pots and how electric jackets reduce the hazard |
| Q4 | Browning / Maillard behavior and surface sticking on glazed vs. unglazed clay vs. aluminum non-stick and cast iron | main | Explains sear vs. steam trade-offs at the food contact surface |
| Q5 | Flavor memory (oil & aromatic absorption in unglazed pores): when seasoning helps vs. hurts | main | Clarifies the real cost and benefit of cooking strongly flavored foods in unglazed clay |
| Q6 | Stovetop compatibility (gas, electric coil, radiant glass, induction + steel diffuser plate hotspots) and why La Chamba is stovetop-safe | main | Prevents cracked pots and answers what actually works on modern ranges |
| Q7 | Supporting benchmark: Magnifique (glazed clay) vs. VitaClay (unglazed Zisha) vs. aluminum non-stick and cast-iron multi-cooker inserts | main (supporting) | Grounds the material physics in real hardware buyers actually compare |
| Q8 | Primer: Major clay cookware families (red earthenware/terracotta, La Chamba micaceous clay, Chinese Zisha, kaolin stoneware/porcelain, petalite/cordierite flameware, and "volcanic clay")—and how much the clay name matters vs. firing temp, porosity, and thermal expansion | main (primer) | Anchors all the unfamiliar clay names and explains why physics, not marketing geology, drives cooking behavior |
| Q9 | Glaze safety (modern commercial food-safe ceramics vs. low-fire artisanal lead glazes) | side | Brief factual check only; explicitly no moral panic |

## 6. Research plan
- **Mode:** Automated multi-pass deep research (`auto-piece` / `.agents/workflows/research_piece.py`) into `proj/clay-cookware/research/`.
- **Standards:** `>= 2` independent authoritative sources per checked figure (materials science / ceramic engineering texts, university food-science / extension guides, FDA/ISO standards, manufacturer engineering specs); explicit ranges/notes where sources disagree; myths labeled per T10.

## 7. Structure and reading order
- Pending `Stage: figures` → `Stage: concepts` & `proj/clay-cookware/layout.md`.

## 8. Brand and contrast
- Light "test-kitchen notebook" paper grounds (T12), crisp technical ink/rule hierarchy, WCAG AA contrast (T07), no rounded-card AI cliché. Exact palette/type chosen in `Stage: concepts`.

## 9. Language
- English only.

## 10. Call to action and credit
- Credit: Bryan Murphy / ProofEr.

## 11. Hard limits
- No toxin moral panic; no unverified single-source claims presented as settled fact; no brand shilling.

## 12. Taste
`Taste: house. Applies: T01–T08, T10, T12–T21. Overrides: none.`
- **Client's voice & taste (`brief/clients/bryan.md`):** Clause-heavy sentences with colons and semicolons, dry humor aimed at myths and marketing; NYT *Untold Story of Sushi* scrollytelling and DK-style illustrated reference books; hates generic AI rounded cards and homework tone.

## 13. Craft bar
Default (`CRAFT.md`).

## 14. Technical
Repo defaults: single offline HTML file (`pieces/clay-cookware.html`), embedded open-licensed fonts, text alternatives, clean print view. Primary testing in Chromium.

## 15. Deliverables
- `pieces/clay-cookware.html` + `index.html` card + `STATUS.md` updates. No PDF or social image extras.

## 16. QA
Default (`TEMPLATE.md` §16) + desktop and phone PNG verification in Chromium + `tools/check_offline.py`.

## 17. Approval and success
- **Sign-off:** Bryan Murphy.

## 18. Open questions
- None — brief approved to start `Stage: research`.

## Decisions log
- 2026-11-20 · Round 1: Deep interactive data essay, food-science/cookware audience, clean test-kitchen notebook aesthetic.
- 2026-11-20 · Round 2: Anchored by clay multi-cooker insert decision vs. classic clay (glazed, Römertopf, La Chamba); cover thermal shock, thermal mass (+50°F premise), 2/4/8-hr slow-cook water loss, browning, flavor memory; explicitly avoid toxin moral panic.
- 2026-11-20 · Round 3: Add stovetop/induction-plate compatibility and La Chamba stovetop safety; use Magnifique vs. VitaClay (+ aluminum non-stick & cast-iron) as supporting benchmark for a general audience; run automated multi-pass research (`auto-piece`); brief approved ("I think the brief looks fine, let's go").
- 2026-11-20 · Follow-up: Added a concise primer on the major clay cookware types (terracotta, La Chamba, Zisha, kaolin stoneware, petalite/cordierite flameware, and "volcanic clay" marketing vs. mineralogy) and how much they matter.
