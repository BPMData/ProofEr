# STATUS.md: the index (read at session start; keep it short)

> **Visitors:** this is the project's working log. For what ProofEr is and how to use it, start with
> [README.md](README.md).

_Last updated: Oct 26, 2026 (tentative skeleton: rules, interview, research step, craft, taste, skills, tools, CI)._

## Pieces
- **holocaust-by-country**, **nazi-victims-all-groups**: Bryan's pre-ProofEr pages, published in `pieces/`.
- **pomewawa** (Pomeranians, Chihuahuas and the mix; for family and online): **published** to `pieces/pomewawa.html`; live once merged to main. `proj/pomewawa/STATUS.md`.

## Across the repo
- **Scope:** infographics only for now. Recipe cards may come later as a second kind of piece.
- **License:** AGPLv3 (Oct 26); pieces people make are theirs.
- **Toolbox:** small: `tools/embed_fonts.py` (tested on two of Bryan's example pages: the same fonts load with the
  network blocked), `tools/check_offline.py`, the choice panel. Until it holds earlier work, every piece is made from
  scratch and the interview skips the mode question.
- **CI:** offline check on `pieces/` (fails on a remote load) and the stage-read audit (warnings only). The
  first-question eval runs by hand (Bryan: no API key secret for now).
- **Peeking audit:** 0 new pieces so far. Decision rule in `notes/architecture.md`.

## Next
1. **First piece (Pomewawa) done.** Lessons: the network policy blocked opening papers (allow nature.com, PMC, akc.org); the stage-read log needs a commit after every turn.
2. **Run `tools/eval_new_piece.py` by hand once** to measure the first-question budget for this repo.
3. **Bryan's two Holocaust pages** are published in `pieces/` (fonts embedded, companion links made local). Made just before ProofEr with the same method and fact-checking; their figures tables aren't in the repo yet (`proj/` folders for them would be the next step).
4. **GitHub Pages** is on (deploy from `main`, root); add the first card to `index.html` when a piece is published.
