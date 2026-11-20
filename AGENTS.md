# ProofEr: notes for AI agents (Antigravity, Codex, and others)

Read `CLAUDE.md` and `STATUS.md` first: all ground rules apply to every agent (`never invent facts`,
`>= 2 independent sources`, honest charts, `brief/CONTENT.md` refusal policy, single offline HTML pieces,
restricted-path stage order).

- **Interactive new piece (default):** follow `.claude/skills/new-piece/SKILL.md` and `brief/INTERVIEW.md` (ask round 1 first; do not design before the brief).
- **Autonomous end-to-end piece** (only when explicitly requested): activate the `auto-piece` skill (`.agents/skills/auto-piece/SKILL.md`), set `Mode: autonomous` in `proj/<name>/brief.md`, run isolated parallel research workers via `.agents/workflows/research_piece.py` (or subagents), render and visually inspect 3 concept PNGs before `pieces/<name>.html`, and run `tools/check_offline.py` + final PNG QA before finishing.
- **Programmatic gates:** `.agents/hooks/stage_gate.py` (wired in `.agents/hooks.json`, `.claude/settings.json`, and `.codex/hooks.json`) enforces stage order and QA receipts.
