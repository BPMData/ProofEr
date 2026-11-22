---
name: auto-piece
description: >-
  Run ProofEr's automated multi-pass Deep Research, fact-checking, visual self-critique, and build pipeline after
  the client interview locks in audience, tone, aesthetic, and detail level (or fully headless if explicitly asked).
---

# Guided-Brief + Autonomous Research & Build Pipeline (`auto-piece`)

## Stage 1 — Always Align With the User First (`Stage: interview -> brief`)
1. Unless the user explicitly instructed to skip questions, **always interview first** (`brief/INTERVIEW.md`, Round 1+): clarify format (**infographic** vs. **interactive data essay**), audience, tone, visual aesthetic (showing rough templates/style options if helpful or requested), and target level of detail.
2. Lock those decisions into `proj/<name>/brief.md` and advance to `Stage: research`.

## Stage 2 — Autonomous Multi-Pass Deep Research & Fact-Checking (`Stage: research -> figures`)
Once tone, aesthetic, audience, budget (`Budget: light | standard | deep`), and detail are set, take over the research loop:
- **Budget & model rules (Claude Code):** Never invoke `fable`, `turbo`, or effort above `high` (`max`). On `Budget: light`, route Pass 1 workers to `sonnet` (via `.claude/agents/research-worker.md`; `haiku` is fine for narrow, clearly defined lookups) and ask the user before spawning `>3` workers or a second pass (`Budget-Override: approved`). On `Budget: standard`, Opus (`medium` effort) is fine for coordination/synthesis with `sonnet` Pass 1 workers. On `Budget: deep`, run full multi-pass fan-out while still banning `fable` and `>high`.
1. Write `proj/<name>/research/prompts.md` and `prompts.json` targeting brief questions, primary sources, and likely LLM blind spots.
2. Launch **Pass 1** isolated parallel `Agent` workers (`subagent_type: "research-worker"` / `model: "sonnet"`) writing structured findings to `proj/<name>/research/workers/pass1/`.
3. **Evaluate & Gap-Fill (Pass 2+):** Inspect Pass 1 outputs for missing metrics, single-source claims, or contradictions; launch follow-up `Agent` workers (`gap_fill`) when budget permits to fact-check primary sources.
4. Synthesize into `proj/<name>/figures.md` (`>= 2` independent sources per `checked` figure, disagreements recorded as honest ranges/notes, myths tagged per `T10`). Set `Stage: concepts`.

## Stage 3 — Visual Self-Critique -> Quick Outline/Mockup for User Review (`Stage: concepts -> layout`)
Still staying out of `pieces/`, `examples/`, and `tools/`:
1. Draft `proj/<name>/layout.md` and build visual mockup/stills in `proj/<name>/stills/`.
2. Capture `.png` screenshots, inspect them via `Read`, and write `proj/<name>/stills/critique.md`.
3. **Present the concise outline + visual mockup** to the user for refinement. Once approved, mark `proj/<name>/layout.md` `APPROVED` and advance to `Stage: build`.

## Stage 4 — Interactive Data Essay Build & Final Visual/Offline QA (`Stage: build`)
1. Read `tools/CLAUDE.md`, generate `pieces/<name>.html`, run `tools/embed_fonts.py`, and update `index.html` + `STATUS.md`.
2. Capture final desktop + phone PNGs into `proj/<name>/qa/` (`desktop.png`, `phone.png`), inspect both via `Read`, fix any defect, and run `python3 tools/check_offline.py` + `python3 tools/check_stage_reads.py`.
