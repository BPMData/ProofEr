# ProofEr: notes for AI agents (Antigravity, Codex, and others)

Read `CLAUDE.md` and `STATUS.md` first: all ground rules apply to every agent (`never invent facts`,
`>= 2 independent sources`, honest charts, `brief/CONTENT.md` refusal policy, single offline HTML pieces,
restricted-path stage order).

- **Standard hybrid flow (`new-piece` + `auto-piece`):**
  1. **Interview first** (`brief/INTERVIEW.md`, showing optional style/template options if helpful or requested) until the user confirms format (**infographic** vs. **interactive data essay**), audience, tone, aesthetic, and level of detail.
  2. **Autonomous multi-pass research:** run isolated parallel deep-research workers (`.agents/workflows/research_piece.py` or subagents) + gap-fill/fact-check passes into `proj/<name>/research/`, then synthesize `figures.md`.
  3. **Outline & mockup review:** run an isolated fresh-eyes subagent review (`brief/CRAFT.md` §12) on rendered mockup `.png`s first, then present the quick outline/mockup to the user until `layout.md` is `APPROVED`.
  4. **Autonomous build & QA:** generate `pieces/<name>.html`, embed fonts, run `tools/add_view_counter.py`, verify `tools/check_offline.py` + final desktop/phone PNGs + isolated fresh-eyes QA review.
- **Programmatic gates:** `.agents/hooks/stage_gate.py` (wired in `.agents/hooks.json`, `.claude/settings.json`, and `.codex/hooks.json`) enforces stage order and QA receipts.
- **Fast ops & bookkeeping:** For file moves, URL switches, or non-visual tweaks (unless the user asks), skip Playwright screenshots, `STATUS.md` updates, and PR-body rewrites. Batch `git` write/push commands into minimal turns rather than running each step sequentially.
- **Formatting:** run `npx prettier --write` on changed files before committing (JS, CSS, JSON, YAML; Markdown, HTML pieces and research output are ignored via `.prettierignore`). CI runs `prettier --check .`.
