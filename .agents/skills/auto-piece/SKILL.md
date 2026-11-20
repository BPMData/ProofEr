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
3. Execute parallel isolated workers:
   - **Antigravity:** run `run_workflow(ScriptPath=".agents/workflows/research_piece.py", Args={"piece": "<name>"})`.
   - **Claude Code:** launch isolated `Agent` workers in parallel writing outputs to `proj/<name>/research/workers/<id>.json`.
   - **Codex CLI:** launch isolated subagents / worker scripts writing outputs to `proj/<name>/research/workers/<id>.json`.
4. Synthesize worker outputs into `proj/<name>/figures.md` (`>= 2` independent sources per `checked` figure,
   disagreements preserved as explicit ranges/notes, odd units explained, myths tagged per `T10`). Set `Stage: concepts`.

## Stage 3 — 3 Visual Stills + Multimodal Self-Critique (`Stage: concepts` -> `layout`)
Still staying out of `pieces/`, `examples/`, and `tools/`:
1. Draft `proj/<name>/layout.md` citing figure IDs from `figures.md`.
2. Build **3 genuinely distinct** HTML/SVG concept stills in `proj/<name>/stills/` (`concept-a.html`, `concept-b.html`, `concept-c.html`).
3. Render all 3 stills over localhost and save full-page PNG screenshots (`concept-a.png`, `concept-b.png`, `concept-c.png`)
   at phone (~390px) and/or desktop (~1200px) widths.
4. **Visually inspect every PNG** directly using `read_file` / `Read` / `view_image` (or an isolated critic subagent)
   and write `proj/<name>/stills/critique.md` scoring each on focal clarity, `390px` legibility, WCAG AA contrast (`T07`),
   `T01`/`T02`/`T06`/`T08`/`T12`, zero overlapping labels, and zero-baseline honest charts.
5. Pick the winning concept, log the verdict in `brief.md` Decisions, mark `proj/<name>/layout.md` with `APPROVED`,
   and set `Stage: build`.

## Stage 4 — Build, Font Embedding & Final Visual QA (`Stage: build`)
1. Open `tools/CLAUDE.md`, build `pieces/<name>.html`, and run `tools/embed_fonts.py` if fonts were linked.
2. Update `index.html`, `proj/<name>/STATUS.md`, and root `STATUS.md`.
3. Render final desktop + phone PNGs of `pieces/<name>.html` into `proj/<name>/qa/` (`desktop.png`, `phone.png`) and
   inspect both via `read_file` / `Read` / `view_image`. Fix any visual defect and re-inspect after the last edit.
4. Run `python3 tools/check_offline.py` and `python3 tools/check_stage_reads.py`, and commit on a branch.
