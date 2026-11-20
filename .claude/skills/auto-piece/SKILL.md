---
name: auto-piece
description: >-
  Run ProofEr's full infographic pipeline autonomously from a one-sentence request to a finished, offline-checked,
  visually self-critiqued page in pieces/<name>.html. Use ONLY when the user explicitly asks for autonomous,
  end-to-end, or self-judged execution without interactive interview/still-selection pauses.
---

# Autonomous End-to-End Infographic Workflow (`auto-piece`)

Follow ProofEr's stage gates (`CLAUDE.md`, `STATUS.md`, `brief/`) while acting as both researcher/builder and
critical client/art director. Programmatic hooks (`.agents/hooks/stage_gate.py`) enforce each gate.

## Stage 0 — Read Rules (Stay Out of Restricted Paths)
1. Read `CLAUDE.md`, `STATUS.md`, `brief/CONTENT.md`, `brief/CRAFT.md`, `brief/TEMPLATE.md`, `brief/RESEARCH.md`,
   `brief/LAYOUT.md`, and `brief/taste/house.md`.
2. Do NOT read `pieces/`, `examples/`, `tools/`, or other `proj/` folders until `proj/<name>/layout.md` is `APPROVED`.

## Stage 1 — Brief (`proj/<name>/brief.md`)
1. Create `proj/<name>/brief.md` from `brief/TEMPLATE.md`.
2. Include `Stage: research` and `Mode: autonomous` in the header so stage hooks enforce autonomous checks.
3. Choose sensible defaults (curious reader, phone + desktop scroll, `T12` light ground unless topic demands otherwise)
   and log those assumptions in Decisions.

## Stage 2 — Self-Prompted Parallel Deep Research (`Stage: research` -> `figures`)
Do NOT perform deep web research inline in the coordinator context window.
1. Inspect what claims, physics, data, or popular myths an LLM usually gets wrong or conflates on this topic.
2. Write `proj/<name>/research/prompts.md` (and `proj/<name>/research/prompts.json`) with **>= 2 independent prompts/angles per topic**
   requiring primary/peer-reviewed/official sources and forbidding SEO blogs.
3. Launch isolated parallel `Agent` workers (each with no shared conversation baggage, using `WebSearch`/`WebFetch`)
   that write structured findings to `proj/<name>/research/workers/<id>.json`.
4. Synthesize worker outputs into `proj/<name>/figures.md` (`>= 2` independent sources per `checked` figure,
   disagreements preserved as explicit ranges/notes, odd units explained, myths tagged per `T10`). Set `Stage: concepts`.

## Stage 3 — 3 Visual Stills + Multimodal Visual Self-Critique (`Stage: concepts` -> `layout`)
Still staying out of `pieces/`, `examples/`, and `tools/`:
1. Draft `proj/<name>/layout.md` citing figure IDs from `figures.md`.
2. Build **3 genuinely distinct** HTML/SVG concept stills in `proj/<name>/stills/` (`concept-a.html`, `concept-b.html`, `concept-c.html`).
3. Render all 3 stills in headless Chromium/Playwright and capture PNG screenshots (`concept-a.png`, `concept-b.png`, `concept-c.png`).
4. Open and visually inspect every PNG via `Read` and write `proj/<name>/stills/critique.md` scoring each against
   `brief/CRAFT.md`, `brief/taste/house.md` (`T01`–`T13`), WCAG AA contrast (`T07`), `390px` phone legibility, and zero-baseline charts.
5. Pick the winner, record the decision in `brief.md`, mark `proj/<name>/layout.md` with `APPROVED`, and set `Stage: build`.

## Stage 4 — Build, Font Embedding & Final Visual QA (`Stage: build`)
1. Read `tools/CLAUDE.md`, build `pieces/<name>.html`, and run `tools/embed_fonts.py` if fonts were linked.
2. Update `index.html`, `proj/<name>/STATUS.md`, and root `STATUS.md`.
3. Render final desktop + phone PNGs of `pieces/<name>.html` into `proj/<name>/qa/` (`desktop.png`, `phone.png`) and
   inspect both via `Read`. Fix any visual defect and re-inspect after the last edit.
4. Run `python3 tools/check_offline.py` and `python3 tools/check_stage_reads.py`, and commit on a branch.
