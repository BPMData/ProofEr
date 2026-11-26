---
name: auto-piece
description: >-
  Run ProofEr's automated multi-pass Deep Research, fact-checking, isolated fresh-eyes visual review, and build pipeline
  after the client interview locks in audience, tone, aesthetic, and detail level (or fully headless if explicitly asked).
---

# Guided-Brief + Autonomous Research & Build Pipeline (`auto-piece`)

## Stage 1 — Always Align With the User First (`Stage: interview -> brief`)
1. Unless the user explicitly instructed to skip questions, **always interview first** (`brief/INTERVIEW.md`, Round 1+): clarify format (**infographic** vs. **interactive data essay**), audience, tone, visual aesthetic (showing rough templates/style options if the conversation calls for it or the user asks), and target level of detail.
2. Lock those decisions into `proj/<name>/brief.md` and advance to `Stage: research`.

## Stage 2 — Autonomous Multi-Pass Deep Research & Fact-Checking (`Stage: research -> figures`)
Once tone, aesthetic, audience, budget (`Budget: light | standard | deep`), and detail are set, take over the research loop:
- **Budget & model rules:**
  - **Antigravity:** Run the coordinator on **Hydrogen High**; keep `research_piece.py` inheriting the session model (leave Antigravity subagent tier overrides out until model tiers are clearer).
  - **Claude Code / Codex:** Never use `fable`, `turbo`, or effort above `high` (`max`, `xhigh`, `extra`). On `Budget: light`, route Pass 1 workers to `sonnet` (`haiku` only for narrow, clearly defined lookups) and ask the user before spawning `>3` workers or a second pass (`Budget-Override: approved`). On `Budget: standard`, Opus (`medium` effort) is fine for coordinator/synthesis with `sonnet` Pass 1 workers. On `Budget: deep`, full multi-pass fan-out is enabled while still banning `fable` and `>high`.
1. Identify what facts, numbers, definitions, and myths the brief needs, writing `proj/<name>/research/prompts.md` and `prompts.json`.
2. Launch **Pass 1** parallel isolated search workers:
   - **Antigravity:** `run_workflow(ScriptPath=".agents/workflows/research_piece.py", Args={"piece": "<name>", "round": "pass1"})`
   - **Claude Code / Codex:** parallel isolated `Agent` (`.claude/agents/research-worker.md`) / `spawn_agent` (`research_worker`) workers writing into `proj/<name>/research/workers/pass1/`.
3. **Evaluate & Gap-Fill (Pass 2+):** Read the deterministic `<round>_digest.md` produced by `research_piece.py` (spot-checking raw JSONs for gaps/contradictions) and launch follow-up worker prompts (`round="gap_fill"`) when budget permits to verify primary sources and resolve disagreements.
4. Synthesize verified numbers into `proj/<name>/figures.md` (`>= 2` independent sources per `checked` figure, disagreements recorded as honest ranges/notes, odd units explained, myths tagged per `T10`). Set `Stage: concepts`.

## Stage 3 — Fresh-Eyes Subagent Review -> Quick Outline/Mockup for User Review (`Stage: concepts -> layout`)
Still staying out of `pieces/`, `examples/`, and `tools/`:
1. Draft `proj/<name>/layout.md` and build visual mockup/stills in `proj/<name>/stills/`.
2. Render `.png` screenshots, inspect them via `read_file`/`Read`/`view_image`, and launch an **isolated fresh-eyes reviewer subagent** (`brief/CRAFT.md` §12; `fresh-eyes-reviewer` in Claude Code, `invoke_subagent` in Antigravity, `spawn_agent` in Codex) seeing ONLY `brief.md`, `figures.md`, and `stills/*.png` to write `proj/<name>/stills/review.md`. Fix clear defects before showing the user.
3. **Present the concise outline + visual mockup** to the user for feedback/refinements. Once approved, mark `proj/<name>/layout.md` `APPROVED` and advance to `Stage: build`.

## Stage 4 — Interactive Data Essay Build & Final Fresh-Eyes/Offline QA (`Stage: build`)
1. Read `tools/CLAUDE.md`, generate `pieces/<name>.html`, run `tools/embed_fonts.py` + `tools/add_view_counter.py`, and update `index.html` + `STATUS.md`.
2. Render final desktop + phone PNGs into `proj/<name>/qa/` (`desktop.png`, `phone.png`), inspect both via `read_file`/`Read`/`view_image`, run an **isolated fresh-eyes reviewer subagent** (`proj/<name>/qa/review.md`), fix any visual/fact defect, and run `python3 tools/check_offline.py` + `python3 tools/check_stage_reads.py`.
