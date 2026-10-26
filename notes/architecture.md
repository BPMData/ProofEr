# Why ProofEr is built this way

ProofEr copies the architecture of its sister repo EOMD (`notes/context-plan.md` there), adapted for infographics.

## Context follows the stage
Whatever is in the model's context first becomes the answer. If a session opens on earlier pieces and tools, every
new piece comes out looking like them. So each stage loads only what its decisions need:

| Tier | Loaded | Holds |
|---|---|---|
| 0 Always | Session start | `CLAUDE.md` (rules, gates, routing) and the `STATUS.md` index |
| 1 Design | Interview → layout | `brief/`: interview, template, research, craft, layout, taste, client files |
| 2 Toolbox | At the gate, via `/toolbox` | What exists, by need, and the build-plan step |
| 3 Detail | When a folder is opened | That folder's `CLAUDE.md` (e.g. `tools/CLAUDE.md`) |
| Piece | Working on a piece | `proj/<name>/`: brief, figures, research, layout, status |

**The mode decides when the toolbox opens:** quicker mode once the figures are checked; from scratch only after the
layout and stills are approved.

## Research is a separate, client-run step
Facts are the product. The model never supplies a number from memory: the client runs deep-research prompts in two
or more tools (differing opinions; saves Claude usage), and the model cross-checks the reports into a figures table
(`brief/RESEARCH.md`). Only checked figures reach the design.

## The restricted list (design stages)
Until the toolbox gate: `pieces/`, `examples/`, `players/`, `dist/`, `tools/`, and every `proj/<piece>/` except the
new piece's own. Open during design: `CLAUDE.md`, `STATUS.md`, `brief/`, `.claude/skills/new-piece/`, the new piece's
`proj/<name>/`, files the client supplied, and the web (for checking sources).

## Checks
- **Stage-read log:** a non-blocking hook (`.claude/settings.json`) records reads during design stages to
  `proj/<name>/access.jsonl`; `tools/check_stage_reads.py` (CI) reports restricted reads as warnings. Decision rule
  (from EOMD): if peeks show up in 2 of 3 new pieces, or once in a way that shaped a design, make the hook blocking.
- **Offline check:** `tools/check_offline.py` (CI) fails if a published piece loads anything from the internet.
- **First-question eval:** `tools/eval_new_piece.py` asks for a new piece in one sentence and checks that the model
  asks before it designs, opens only `brief/` and the skills, and stays within a context and cost budget.
