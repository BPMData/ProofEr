# Layout plan: The Pomewawa

Stage: layout · APPROVED Oct 26, 2026 by Bryan Murphy

Format: phone scroll, one column, designed at 390 px wide (works 320–480; widens to a centered 560 px column on
laptops) · Paper concept (cream ground, near-black ink, one red-orange accent; heavy condensed headlines, serif notes,
rubber-stamp myth checks).

The one sentence: **Pomeranians and Chihuahuas are tiny dogs with a big, strange, checkable history, and they outlast
the big guys, even if they'd lose the fight.**

The visual idea: **field-guide plates, drawn to scale.** Each section is a numbered plate; sizes and lifespans are
drawn true to scale from a zero line, and every legend the internet repeats gets a stamped verdict. The "plate" frame
fits this subject (natural history of two breeds); the stamps carry the punch.

Headlines marked DRAFT are Claude's wording until Bryan approves them.

| # | Section | What the reader learns | Figures (IDs) | Chart and why | Eye hits first |
|---|---|---|---|---|---|
| 0 | **Hero.** "TINY. ANCIENT. UNBOTHERED." (DRAFT) + "The Pomewawa: Pomeranian × Chihuahua. Every number checked." | What this is and its tone | none | Type only: the promise of checked facts is the hook | The headline, accent on UNBOTHERED |
| 1 | **Plate I: Aztec roots.** "ON THE MENU SINCE 1520." (DRAFT) | Cortés saw little dogs sold for eating in Tenochtitlan; Maya dogs were fed corn and carried in alive from the highlands; some Chihuahuas still carry ancient Mexican mother-line DNA | F03, F04, F02 (F01's ~4% only if the paper check passes) | A short three-stop timeline (1100 BCE → 1520 → today): events in time, nothing to compare | Big "1520" in accent |
| 1b | **Myth checks** under Plate I | Two legends with verdicts: the dog that carries souls across the river of the dead (documented belief, colors = later retellings); "hot-water-bottle dogs" (no old record backs it) | F06, F07 | Stamps, not charts: the verdict is the content | The stamp words |
| 2 | **Plate II: Shrunk on purpose.** "A BIG DOG, MADE SMALL." (DRAFT) | Same breed standard: Wolfspitz 49 cm vs Pomeranian 22 cm; Queen Victoria's Marco ~12 lb vs today's 3–7 lb; Gainsborough painted one c. 1777; AKC recognized it in 1900 | F11a, F10, F26 (Pom), F12, F09 | To-scale bars from a zero line (heights in cm), then a second pair for weight (lb), each with its own labeled scale. Both questions are "how big?", so bars | The 49 vs 22 bars |
| 3 | **Plate III: Attitude.** "SMALL. ARMED. DOCUMENTED." (DRAFT) | Chihuahuas rank among the breeds most likely to bite (or try) with strangers; shorter breeds show more problem behavior | F19, F20 | Type and source cards, no chart: the studies give rankings and correlations, not one number per breed; drawing fake bars would invent precision | "Top tier" in accent |
| 4 | **Plate IV: How long they last.** "OUTLIVES THE BIG GUY." | Chihuahua 11.8 years vs Cane Corso 8.1 (median age at death, 584,734 UK dogs); the fight line; the "700 PSI" myth and the real record (1,394 N, about 313 lb of force, measured in a pet dog) | F14, F15, F17 (F16 Pom 12.2 if verified), F22, F23 | Horizontal bars from 0 years, labeled; bite force as a stamped myth + one plain number. The Corso's only appearance | The 11.8 bar |
| 5 | **Plate V: Firsts.** "PAPERWORK." (DRAFT) | 1900 AKC Pomeranian, 1904 AKC Chihuahua ("Midget", of Texas), 1912 Titanic: 2 of the 3 dogs that survived were Pomeranians | F09, F08, F13 | Timeline (events in time), with "2 of 3" as a big number | "2 of 3" |
| 6 | **Plate VI: Wrong dog, wrong house.** Bryan's Kangal story, his words, breeder unnamed | Kangals are Turkish flock guardians against wolves, males 48–60 kg; a Kangal breeder told Bryan not so many people should own one | F24; Bryan's anecdote (brief §4) | To-scale silhouette-free bar: Kangal weight range vs a Pomeranian's 3–7 lb, same kg scale from 0, so the gap is felt | The weight bar's length |
| 7 | **Drill-down: "Everyone eats the dog eventually."** (DRAFT, from Bryan's "everyone would eat a dog like a cinnabon if they had to") | Documented times people ate dogs, told the same plain way for every place: Mesoamerica, Hawaiʻi, Jamestown, Lewis and Clark, Paris 1870, Amundsen, Switzerland (still legal at home), Germany (banned 1986), South Korea (ban from 2027) | F03, F04, F35, F31, F32, F30, F33, F28, F29, F34 | A list of tap-to-open entries (`<details>`): works without scripts, prints fully open. Order: by date, never by "strangeness" | The intro line, then the list |
| 8 | **Sources and "About these numbers"** | Where every number came from, and the caveats | all used | — | — |

## Sources and "About these numbers"
At the end, same type size as the body (not fine print). The note explains, in plain words:
- **Lifespans** are median age at death from one big UK study (McMillan et al. 2024). Other studies count
  differently (one gives 7.9 years "at birth" because it counts puppies who die young); we used the typical age at
  death.
- **Attitude** studies are owner surveys (Duffy 2008, McGreevy 2013): rankings and patterns, not lab measurements;
  one later study found lower Chihuahua scores.
- **Sizes** are breed standards (FCI, AKC), not every dog. The Wolfspitz is a cousin in the same standard, not a
  proven ancestor.
- **Bite force:** no study has measured Kangals or Cane Corsos; the "PSI" numbers online have no source.
- **Myth checks** mark stories we couldn't find in old records; that's "unproven", not "disproven".
- **Pomewawa** facts come from the parent breeds; nobody has studied the mix itself.
- How it was checked: research by Gemini and ChatGPT deep research, cross-checked against the sources listed.
Each source: author or body, title, year, link.

## Open before build
- F01 (4% DNA), F16 (Pom 12.2 years): need the network opened to confirm; off the page until then.
- Plate VI wording: Bryan's own words for the Kangal story (ASK).
- Headlines marked DRAFT: Bryan approves or rewrites.
- Fonts (open-licensed, inlined): a heavy condensed sans for headlines, a readable serif for notes. Chosen at build.

## Stills
In `stills/`, 390 px wide, real type sizes (system stand-in fonts):
- `still-1-hero.png`: hero + Plate I + myth stamps (proves the tone and the headline at 25%).
- `still-2-plates.png`: Plates II and IV (proves the to-scale bars and zero lines, the dense sections).
- `still-3-menu.png`: the dog-food drill-down, one entry open (proves the menu reads plainly, not as a freak show).
