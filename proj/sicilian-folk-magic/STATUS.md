# STATUS: Sicilian folk magic

_Last updated: Nov 23, 2026 (late)._

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
  drawn for this page" tooltip removed. **Waiting on Bryan:** photo files for the real Agatha bust (to replace the
  Juliana stand-in) and for each cabinet relic; the proxy blocks Commons downloads. Then Act 8.
