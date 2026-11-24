# STATUS: Sicilian folk magic

_Last updated: Nov 23, 2026 (evening)._

- **Stage:** build done, on branch `claude/project-thread-gi5ppk` (not merged, not published). Brief approved Nov 22
  (Bryan, with amendments); layout approved Nov 23 ("Lock it in").
- **Page:** `pieces/sicilian-folk-magic.html` (1.1 MB, one offline file, fonts and pictures inside, view counter
  added, `check_offline.py` passes). Built by `build/build_piece.py` from `copy.md`, `figures.md` and
  `build/template.html` (the `build/` scripts are force-added; `build/out/` stays ignored). Cutouts by
  `build/make_cutouts.py` into `art/cut/`; originals in `art/originals/`.
- **Charts:** rulers timeline (Inquisition dates in blue), Rosalia day strip, Inquisition chart (penitent's hats, one
  = 10 people tried; stakes, one = one person executed, any charge; Bryan, Nov 23), relic cabinet drawers, routes
  map (not to scale). Each has a caption; the timeline and strip have "Read it as a list".
- **QA done:** HTML nesting, ids, heading order; WCAG AA contrast for every text and chart color (all pass); no
  leftover markers; the page script runs without errors through all 14 scenes; every stage scene redrawn and looked
  at (`stills/qa-stage-phone.png`). **Not done:** a look in a real browser (none here; installing one was refused),
  so the text column, glosses, scrolling and print are checked in code only.
- **Pictures:** all 12 used. Stand-ins and caveats in the credits: the bust is Saint Juliana's (Agatha's own is not
  open-licensed); the ex-voto is Roman, 1851; the angel is credited to the Met's crèche angels (64.164) since which
  of the four photos is .16 is unclear. The eye charm and coral horn are drawn; shop photos were reference only.
- **Merged** to main Nov 23 (Bryan: "Merge it"). Credit tooltips on the stage and red stakes added after, also on main.
- **Nov 23, Bryan's read-through (Acts 1–4):** Mulder/Scully cut; call-outs for Pitrè, Gramsci, de Martino and the
  first peoples (portraits for Pitrè and Gramsci only); Act 1 rewritten for readers new to Sicily; Act 2 fixes (timeline
  labels, the *Life*, the Roman Martyrology, "Why the floats?", the REIS link). New rows at the end of figures.md
  ("Added Nov 23"). **Waiting on Bryan:** the thesis, act-by-act line and new opening (sent Nov 23); then rewrite the
  body around it, and his notes on Acts 5–8.
- **Repo note for Bryan:** `.agents/hooks/stage_gate.py` checks figures.md for `| F01 |` rows; this piece's rows are
  `X1-01` style, so the design gate's row check doesn't match them. The repo-wide `build/` ignore rule also catches
  piece build scripts.
- **Nov 23 night:** body rewritten in the friend-and-folklorist voice with far fewer stamps; new tarot opening on the
  stage (the costume comes off to show a Paris occultist of 1781); "why it's in acts" and "Why Sicily gets the spooky
  treatment" (Southern Question, race science, New Orleans 1891); Act 5 (intercession, decollati, frusteri); Act 6
  (archive fire, who was executed, the ladies from outside, Gratteri's healers, three captioned pictures); click any
  painting or statue to zoom (embedded, about +0.8 MB; page now 2.5 MB). Scenes are picked by scroll position so beats
  inside a section work.
- **Nov 23 late:** Act 1 "Inside the silver woman" (what the bust holds, jewels, the breast legend, why bodies matter);
  Act 7 rewritten (Lucy introduced; Venice vs Metz as the lead duplicate; Louis IX; why Europe wanted bones: altars,
  Nicaea 787, pilgrimage, the trade, *furta sacra*; Lateran 1215, Trent 1563; Calvin 1543 and Krasinski's footnote;
  2017 rules; one stamp on "first/second/third-class"). Relic cabinet: one drawer per relic (4), no empty slots, fill
  read from scroll position so fast scrolling can't desync it; tap it for a list with a note per relic. "The boat:
  drawn for this page" tooltip removed.
- **Nov 23 evening:** Bryan's relic photos (art/originals, licences in figures X1-252). The real Agatha bust replaces the
  Juliana stand-in on the stage (`make_cutouts.py`, `agathabust`); cabinet drawers open photos of the bust, the Messina
  Letter manuscript (no photo of the hair exists), Lucy in Venice (her feet show) and Louis IX's tomb, which gets a
  fifth drawer (copy `_cabinet louis_`). Page now 3.2 MB. Research reports behind today's revisions saved as
  `research/H-revision-reads.md`. Rosalia's urn photo (Effems, CC BY-SA 4.0) added after Bryan sent the author. **Next:** Act 8.
- **Nov 23 bugfix & refinement-plan pass (`fix/sicilian-bugfixes-and-cabinet`):**
  - Fixed `#cabpop` off-screen positioning on mobile (`position:fixed`, scrollable, close button), added `64×64` clickable
    relic photo thumbnails, made the drawn stage cabinet clickable (`ui:cabinet`) and hid it on compact mobile stages so
    `.cabbtn` doesn't cover it; made Act 7's opened cabinet drawers clickable (`data-z`) and moved the grid after Louis IX.
  - Fixed puppet `setCast`/`drawCast` popping & duplicate Overture pop-down/pop-up (kept matching props in place across
    consecutive scenes, skipped `leaving` for un-entered props, disabled hitboxes on leaving props, clipped stage cast
    to proscenium/floor slot, shortened `boat` stick, clamped `stampOn` width and cleared stale stamps on scene change).
  - Fixed mobile `pickScene` trigger line, `cabKey` sync, empty `#oncap` stray box (`.oncap:empty`), `#glosspop` scroll
    dismissal & flip, `Escape` modal priority (`zoom` → `cabpop` → `glosspop`), and Act 8 `route_svg()` geography.
  - Added offline font fallback in `build_piece.py`; rebuilt `pieces/sicilian-folk-magic.html` (3.60 MB), ran
    `add_view_counter.py` and `check_offline.py` (0 problems), and verified in headless Chromium at 1440×900 and 390×844
    (`proj/sicilian-folk-magic/qa/`).
  - Logged Bryan's *A Distant Mirror* tone benchmark in `brief.md` and wrote the 4-wave Hydrogen sub-agent refinement
    plan at `proj/sicilian-folk-magic/REFINEMENT-PLAN.md`. **Next:** Bryan's answers on the 5 open questions, then run Wave 1–4.
- **Nov 23 evening — Full 4-wave Hydrogen refinement (`feat/sicilian-refinement-tuchman`, stacked on `fix/sicilian-bugfixes-and-cabinet`):**
  - **Wave 1 (`research/I-context-gaps.md`, `research/I-art-candidates.md`):** Added `X1-254`–`X1-270` and `X3-214`–`X3-219` to `figures.md` (Decius 250 CE edict, Messina–Palermo rivalry & *Vara* float mechanics, St Joseph's table foods & diaspora hunger reading, Palazzo Chiaramonte-Steri pre-1601, *cimaruta* & Sicilian oil-in-water test, Benedict the Moor & Antonio of Noto biographies, and tarot occultist bios). Downloaded & verified Wikimedia PD portraits (`gebelin`, `etteilla`, `papus`, `waite`, `smith`, `crowley` at 168 px) plus St. Benedict the Moor (`16-benedict-moor.jpg`, NGA photo of Mia 2010.27.2, CC BY-SA 4.0) and Picart's *Auto-da-Fé* (`17-steri-inquisition.jpg`, Wellcome V0041640, CC BY 4.0).
  - **Wave 2 & 3 (`copy.md`, `make_cutouts.py`, `build_piece.py`, `template.html`):** Four parallel Hydrogen drafts integrated & audited (`416` unique `[X...]` IDs, `0` missing, `0` unverified) and polished end-to-end by a single-voice continuity editor in the *A Distant Mirror* + wry Sicilian friend voice. Implemented 3-tier myth checks (`3` Tier-1 canvas stamps, `2` Tier-2 scroll-lit `.myth-sm` inline checks, obscure claims folded into prose), `14` call-outs (incl. the 6 tarot occultists + 4 new historical entries), `18` deepened glosses, Act 6 three-beat stage (`16` → `17` → `9`), Act 8 Benedict + ship stage, `agathabust` 1 px fringe cleanup, and hero single-title `.herotitle`.
  - **Same-repo zoom assets & QA:** Moved 21 zoomed WebPs into `pieces/assets/sicilian-folk-magic/*.webp` with inline `THUMBS` & fallback, cutting the rebuilt HTML from **3.60 MB → 1.75 MB** while passing `add_view_counter.py` and `check_offline.py` (`0` problems). Published unlinked at `pieces/sicilian-folk-magic-rebuild.html` (keeping `pieces/sicilian-folk-magic.html` as `main`'s original for side-by-side comparison, matching `clay-cookware-v2.html`). Verified in headless Chromium at 1440×900, 768×1024, 390×844, and `@media print` (`0` errors, `0` overflow; screenshots in `proj/sicilian-folk-magic/qa/`). **Next:** Bryan compares side-by-side and reviews PRs against `main`.
