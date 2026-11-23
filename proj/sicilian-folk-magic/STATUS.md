# STATUS: Sicilian folk magic

_Last updated: Nov 23, 2026._

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
- **Next:** Bryan looks at the page on his phone. Then, on his yes: merge to main (publishes the page and the hub card).
- **Repo note for Bryan:** `.agents/hooks/stage_gate.py` checks figures.md for `| F01 |` rows; this piece's rows are
  `X1-01` style, so the design gate's row check doesn't match them. The repo-wide `build/` ignore rule also catches
  piece build scripts.
