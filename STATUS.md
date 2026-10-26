# STATUS.md: the index (read at session start; keep it short)

> **Visitors:** this is the project's working log. For what ProofEr is and how to use it, start with
> [README.md](README.md).

_Last updated: Oct 26, 2026 (tentative skeleton: rules, interview, research step, craft, taste, skills, tools, CI)._

## Pieces
- **pomewawa** (Pomeranians, Chihuahuas and the mix; for family and online): interview. `proj/pomewawa/STATUS.md`.

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
1. **First real piece through `/new-piece`.** It's the test of the setup, including the research step.
2. **Run `tools/eval_new_piece.py` by hand once** to measure the first-question budget for this repo.
3. **Bryan's example pages** (two Holocaust infographics): candidates for `examples/` once their fonts are embedded
   and their figures have a checked `figures.md`. Not added yet.
4. **GitHub Pages** is on (deploy from `main`, root); add the first card to `index.html` when a piece is published.
