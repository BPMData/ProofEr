# STATUS: Disaster Artist (Van Gogh)

_Last updated: Nov 24, 2026._

- **Stage:** outline waiting for Bryan's read and approval. Meanwhile he runs the four Gemini Deep Research prompts in
  `research/gemini-prompts.md` (Gauguin in Arles; Johanna's 1914 editing and remarriage; the chicken-coop
  provenance; three suspected AI-invented claims), reports go in `research/gemini/`, then figures update and prose. Brief = Bryan's own uploaded
  build brief (`brief.md`). Prose will be written with Gemini; this pass stops at the outline (Bryan, Nov 24).
- **Research:** five pass-1 workers (counts, money, Arles, afterlife, early life) and one gap-fill pass, in
  `research/workers/`. vangoghletters.org and most vangoghmuseum.nl pages wouldn't load for the workers, so several
  letter quotes come from older translations and need a recheck.
- **Figures:** `figures.md` (F01–F99, with status). `research/stipend-model.md` models Theo's support (about
  16,000 F, range 13,000–19,000) because no published total was found.
- **Outline:** `outline.md`, chapter by chapter, plus 28 brief claims the research contradicts or can't support
  (biggest: per-year painting counts unsourced; ear verdict flips to CONFIRMED; Gauguin's "unsalable" letter isn't
  real; Johanna remarried in 1901; Tanguy was never deported).
- **Images:** Bryan is having Gemini (Antigravity) find and licence-check the paintings. `scripts/make_image_tiers.py`
  (src → full/thumb + sizes.json) and `scripts/extract_swatches.py` (measured colour chips for the compare plate)
  are ready for them; both run from Thonny.
- **Chart data:** `data/chart-data.json`, every number tied to a figures.md row.
- **Open:** Bryan's approval of the outline; the four Gemini reports; letter quotes to recheck; *The Account Book of Theo van Gogh and Jo van
  Gogh-Bonger* (2002) would replace the stipend model with real numbers.
