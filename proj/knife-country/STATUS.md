# STATUS: Knife Country (Yangjiang knives scrolling infographic)

_Last updated: Nov 3, 2026._

**Published:** `pieces/knife-country.html`, linked from `index.html`. It goes live on Pages once merged to main.

## How it got here
Built Nov 2–3, 2026 in the sister repo EOMD by mistake (BPMData/EOMD, `proj/yangjiang-knives/`), following EOMD's
gates (interview → brief → concepts → storyboard → build), then moved here. So:
- The brief is in EOMD's template, not ProofEr's.
- The layout lives in `storyboard.md`, not `layout.md`.
- `figures.md` was made after the build, not before the concepts.
- The read log `eomd-access.jsonl` is EOMD's. It shows no reads of EOMD's restricted folders before its gate; this
  repo's peeking audit doesn't apply.

## Files
- **Brief:** `brief.md` (approved, with the full Decisions log in Bryan's words).
- **Design:** `concepts.md`, `storyboard.md`, `stills/`.
- **Research:** `research/` (the reports and `prompts.md`), `research-notes.md` (cross-check and conflicts),
  `figures.md` (72 figures, with status).
- **Build:** `build.py` (Thonny Run; needs `pip install fonttools brotli`) turns `src/` into `knife-country.html`
  and copies it to `pieces/`.
  - Sources: `page.html`, `page.css`, `page.js`, `sources.json`.
  - Fonts: Source Serif 4, Archivo and Noto Serif SC (subset), downloaded into `font_cache/`; OFL licenses in
    `fonts/`.
- **QA:** `QA.md`.

## Checked
- `tools/check_offline.py`: offline OK.
- No script errors in Chromium at phone and laptop sizes; every interaction exercised; keyboard pass.
- Contrast AA (lowest 4.67:1).
- Print styles: belts hidden, scenes laid flat, marks shown struck.

## Open
- **Figures against ProofEr's two-source rule:**
  - 21 checked (2 against primary sources)
  - 41 single source
  - 6 single source from an encyclopedia
  - 4 accepted with a note

  Bryan to accept them as shown (each with its visible confidence on the page) or name rows to upgrade.
- Not tested on iPhone/Safari or with reduced motion (Bryan has neither).
- "Knife Country" is a working title.
