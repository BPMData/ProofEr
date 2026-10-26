---
name: toolbox
description: Opens the ProofEr toolbox (what already exists to build an infographic with, by need). Use only after the figures are checked (quicker mode) or the layout and stills are approved (from scratch). Never during the interview, research, concepts or layout of a from-scratch piece.
---
# Toolbox: what exists, by need

**Check the gate first.** Read `proj/<name>/brief.md`. Quicker mode: `Stage:` is past `figures`. From scratch:
`layout.md` is APPROVED. If not, stop and go back to `/new-piece`. When the gate is open, set `Stage: build` once
the build plan below is approved.

**The rule:** earlier pieces are consulted for mechanisms and lessons, never for their look. The toolbox is small
for now; most of a new piece is built new, and what proves reusable is added here.

| Need | What exists | Where |
|---|---|---|
| Make a page offline: inline the Google Fonts it links to | `tools/embed_fonts.py` (Thonny: set `HTML_IN`, `HTML_OUT`) | `tools/CLAUDE.md` |
| Check a page loads nothing from the internet | `tools/check_offline.py` (CI runs it on `pieces/`) | `tools/CLAUDE.md` |
| Let the client choose between finished options | `choice-panel.html` in this folder | below |
| Publish | Copy the finished HTML to `pieces/<name>.html`, add a card to `index.html`, keep `README.md` true | — |
| Anything else (charts, unit grids, maps, timelines) | Build it in the piece, plain HTML/SVG/Canvas, no libraries loaded from the web | — |

## The build plan (before building)
1. For every row of `layout.md` (or every section of the chosen concept in quicker mode), write one line in the
   brief under **Build plan**: **reuse** (which tool), **adapt** (what changes) or **build new** (what, roughly).
2. Show the client the plan in everyday words with what they'll see first. Their answer goes in the Decisions log.
3. Build, then run QA (`brief/TEMPLATE.md` §16), then publish.

## Choice panels
Copy `choice-panel.html` to `proj/<name>/choices-<topic>.html`, fill in `PANEL` at the top (up to six options: a
still or a live `draw` sketch), and send it. The client answers with a letter; the answer goes in the Decisions log.
