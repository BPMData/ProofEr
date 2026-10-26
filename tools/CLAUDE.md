# tools/: the Python scripts

Every script is Thonny-friendly: the Run button, no command-line arguments, every setting in a `SETTINGS` block at
the top. Each resolves paths from the repo root (its parent folder).

| Script | What it does |
|---|---|
| `embed_fonts.py` | Makes a page work offline: downloads the Google Fonts it links to and puts them inside the page (only the `KEEP_SUBSETS` character sets). Set `HTML_IN`, optionally `HTML_OUT` |
| `check_offline.py` | Lists anything a page loads from the internet (stylesheets, scripts, images, fonts, CSS imports). Links readers click are fine. CI runs it on `pieces/` and fails on a hit |
| `check_stage_reads.py` | The peeking audit: reads of restricted paths before a new piece's toolbox gate, from `proj/*/access.jsonl` (written by `.claude/hooks/stage_log.py`). Warnings only; CI runs it |
| `eval_new_piece.py` | The first-question eval: a one-sentence request on a copy of the repo (Sonnet, read-only, capped at $0.50), checking files opened, context and cost before the first question; PASS/FAIL. Run by hand (it uses your Claude login); CI runs it only if an `ANTHROPIC_API_KEY` secret exists |

Publishing: copy a finished, QA'd piece to `pieces/<name>.html`, run `check_offline.py`, add a card to `index.html`.
