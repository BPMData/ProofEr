---
name: new-piece
description: Start any new ProofEr piece (short infographic or interactive data essay) by interviewing the client, getting a brief approved, then running automated multi-pass research and outline/mockup review before building. Use whenever someone asks for a new piece, infographic, interactive data essay, chart page or data poster, however short the request. Not for changes to an existing piece.
---
Follow `brief/INTERVIEW.md` from the top: ask round 1 first (open nothing else before it), then start `proj/<name>/brief.md` from `brief/TEMPLATE.md` with `Stage: interview`; interview in rounds (showing quick visual samples if helpful or asked) until tone, aesthetic, audience, and detail level are confirmed, then run automated multi-pass research (`proj/<name>/research/`), show a self-critiqued quick outline/mockup for user refinement (`layout.md` APPROVED), and build + QA the final interactive piece.

Gates (update `Stage:` in the brief's status line at each one):
- interview → brief (approved by user) → research (automated parallel deep research + gap-fill passes, enforced by `.agents/hooks/stage_gate.py`) → figures (checked) → concepts & mockup (self-critique PNGs, then present quick outline/mockup to user) → layout (APPROVED by user) → build & final visual/offline QA.
- **Quicker mode:** run `/toolbox` once the figures are checked.
- **From scratch:** run `/toolbox` only after the layout and mockup/stills are approved. Until then, read only `brief/`, this skill, the root `STATUS.md` index, the piece's own `proj/<name>/` and what the client supplied.
