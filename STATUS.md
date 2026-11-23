# STATUS.md: the index (read at session start; keep it short)

> **Visitors:** this is the project's working log. For what ProofEr is and how to use it, start with
> [README.md](README.md).

_Last updated: Nov 22, 2026 (terezin-vedem glosses + family-camp section; clay-cookware v2 remake published unlinked for comparison; invisible GoatCounter view
counter on all published pieces)._

## Pieces
- **holocaust-by-country**, **nazi-victims-all-groups**: Bryan's pre-ProofEr pages, published in `pieces/`.
- **terezin-vedem** (Terezín/Theresienstadt, *I Never Saw Another Butterfly*, and *Vedem*; for HS students and online): **published** to `pieces/terezin-vedem.html` (`index.html` updated; dark-slate mode matching companion pieces' `:root[data-theme="dark"]`; full offline fonts + 7 licensed PD / CC BY-SA archival images inlined; `check_offline.py` passed; desktop, phone, interactive `dialog#sheet`, and `@media print` Chromium QA verified with 0 errors and 0 overflow; 0 restricted reads before gate). `proj/terezin-vedem/STATUS.md`.
- **pomewawa** (Pomeranians, Chihuahuas and the mix; for family and online): **published** to `pieces/pomewawa.html`; live once merged to main. `proj/pomewawa/STATUS.md`.
- **knife-country** (Yangjiang and the "City of Knives" title; a long scrolling piece for knife nerds online): **published** to `pieces/knife-country.html`; live once merged. Built in EOMD by mistake, then moved here; Bryan accepted its single-source figures as shown. `proj/knife-country/STATUS.md`.
- **clay-cookware** (Glazed vs. unglazed clay in cookware & multi-cooker inserts; interactive data essay for food-science/cookware enthusiasts): **published** to `pieces/clay-cookware.html` (`index.html` updated; `0` restricted reads before gate; `check_offline.py` passed; desktop/phone Chromium QA verified; usage on \$20/mo plan all on Gemini 4 Hydrogen High incl. 11 workers + 3 PRs: ~36% of 5-hr window, ~8% weekly—indicating Antigravity has comfortable headroom before needing aggressive Medium/light throttling). `proj/clay-cookware/STATUS.md`. **v2 remake** ("It's All in the Wall": scannable, pot picker, interactive plates) at `pieces/clay-cookware-v2.html`, live but **not on the hub** until Bryan picks a version.

- **sicilian-folk-magic** (Sicilian Catholicism and folk magic; long scrolling essay for witty history nerds;
  baroque x cut-paper puppets): **built** Nov 23 at `pieces/sicilian-folk-magic.html` on branch
  `claude/project-thread-gi5ppk` (view counter added, `check_offline.py` passed, card added to `index.html` on the
  branch). No browser in this environment: the stage was checked by redrawing every scene from the page's own drawing
  code; the text column still needs one look on a real phone. Merged to main Nov 23. Bryan's Acts 1–4 notes partly done
  (Act 1, Act 2 fixes, call-outs, Mulder/Scully cut); thesis approved; body rewritten through Act 7 (Nov 23 late); waiting on relic photos, then Act 8. `proj/sicilian-folk-magic/STATUS.md`.

## Across the repo
- **Scope:** sourced visual pieces—short **infographics** and long-form **interactive data essays**. Recipe cards may come later.
- **License:** AGPLv3 (Oct 26); pieces people make are theirs.
- **Toolbox:** small: `tools/embed_fonts.py` (tested on two of Bryan's example pages: the same fonts load with the
  network blocked), `tools/check_offline.py`, the choice panel. Until it holds earlier work, every piece is made from
  scratch and the interview skips the mode question.
- **CI:** offline check on `pieces/` (fails on a remote load) and the stage-read audit (warnings only). The
  first-question eval runs by hand (Bryan: no API key secret for now).
- **Multi-harness gates:** `.agents/hooks/stage_gate.py` enforces research/figures/stills/QA gates across
  Antigravity (`.agents/hooks.json`), Claude Code (`.claude/settings.json`), and Codex (`.codex/hooks.json`), with
  the `auto-piece` skill and `.agents/workflows/research_piece.py` for explicit autonomous end-to-end runs.
- **View counts:** every piece in `pieces/` has an invisible GoatCounter ping (no cookies, nothing shown, skipped
  offline/localhost); Bryan's private dashboard is https://bpmdata.goatcounter.com. New pieces: run
  `tools/add_view_counter.py` when publishing or rebuilding (root `CLAUDE.md` rule); `check_offline.py` and CI
  fail a piece without it and allow only that ping. Counting began Nov 22, 2026;
  earlier site visits were never recorded (GitHub's Insights → Traffic counts only the repo page, not the site).
- **Peeking audit:** 0 new pieces so far. Decision rule in `notes/architecture.md`.

## Next
0. **Knife Country lessons (Nov 3)** are folded in:
   - Confirm it's a ProofEr piece first (it was built in EOMD by mistake).
   - Ask for the client's voice early.
   - Say when the research overturns the premise, and plan a primer.
   - Explain odd units; ask Bryan for primary documents.
   - Taste items T14–T21.

1. **First piece (Pomewawa) done.** Lessons: the network policy blocked opening papers (allow nature.com, PMC, akc.org); the stage-read log needs a commit after every turn; the interview took an aside (the Cane Corso joke) as a main point, so asides now stay side notes until the client says otherwise (`INTERVIEW.md`, T13).
2. **First-question eval run by hand (Oct 27):** repo share 9,428 of 12,000 tokens, $0.09 (budget $0.35); it asked before designing and opened only the skill, `brief/INTERVIEW.md` and `STATUS.md`. Its FAIL was a path bug in the script (macOS `/private/var`), now fixed; one rerun should show PASS.
3. **Bryan's two Holocaust pages** are published in `pieces/` (fonts embedded, companion links made local). Made just before ProofEr with the same method and fact-checking; their figures tables aren't in the repo yet (`proj/` folders for them would be the next step).
4. **GitHub Pages** is on (deploy from `main`, root); add the first card to `index.html` when a piece is published.
