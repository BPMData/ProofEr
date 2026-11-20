---
name: new-piece
description: Start any new ProofEr piece (short infographic or interactive data essay) by interviewing the client, getting a brief approved, then running the research step before any design or build. Use whenever someone asks for a new piece, infographic, interactive data essay, chart page or data poster, however short the request. Not for changes to an existing piece.
---
Follow `brief/INTERVIEW.md` from the top: ask round 1 first (open nothing else before it), then start `proj/<name>/brief.md` from `brief/TEMPLATE.md` with `Stage: interview`; interview in rounds (the ★ questions every time), get the brief approved, then research and figures (`brief/RESEARCH.md`), then concepts and layout (`brief/CRAFT.md`, `brief/LAYOUT.md`).

Gates (update `Stage:` in the brief's status line at each one):
- interview → brief (approved by user: audience, tone, aesthetic, depth) → research (run automated parallel deep research + gap-fill rounds in `proj/<name>/research/`, never manual client prompt-pasting unless primary scan is paywalled) → figures (checked) → concepts & mockup (self-critique stills, then show quick outline/mockup to user for refinement) → layout (APPROVED by user) → build & final visual/offline QA.
- **Quicker mode:** run `/toolbox` once the figures are checked.
- **From scratch:** run `/toolbox` only after the layout and mockup/stills are approved. Until then, read only `brief/`, this skill, the root `STATUS.md` index, the piece's own `proj/<name>/` and what the client supplied.
