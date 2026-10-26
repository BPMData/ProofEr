# House taste profile

The default taste for every piece. It starts small: most items come from verdicts in EOMD, ProofEr's sister repo,
that hold for infographics too; new verdicts are added as pieces are made. Hard rules live in `CLAUDE.md`, not here.

**How to use it**
- One line per item: `ID · strength · area · [condition ·] the preference — the verdict it came from`.
- **strength:** `strong` = the default; overriding it needs a reason in the brief. `soft` = a lean.
- **area:** layout, type, color, chart, data, motion, process.
- **condition** (from "How it's read"): `phone` / `screen` / `projector` / `print` / `poster`, `read alone` /
  `presented`, `more than one language`, `human subject`. No condition = every piece.
- **In the brief (§12):** `Taste: house. Applies: T01–T08, T09 (more than one language). Overrides: ...`
- **New verdicts flow in:** a verdict in a brief's Decisions log that would hold for other pieces becomes an item
  (next free ID) or adjusts one. IDs are never reused.
- Parse with `^T\d+ · (strong|soft) ·`.

## Items
T01 · strong · layout · Words and picture belong to one idea: no captions laid over unrelated imagery. — EOMD, PLTW r1 (Oct 20): "words on top of unconnected visuals ... looks bad"
T02 · strong · chart · Every effect and ornament is there because the reader needs it, not because the tool can do it. — EOMD, PLTW r2 (Oct 20): "looks cheesy as hell, but it's exactly what I asked for"
T03 · strong · process · Let the client choose by looking: a page of options (choice panel), not descriptions. — EOMD, Academies hero marks: the demo-sheet pickers "were a great methodology" (Oct 25)
T04 · strong · process · Show something rough early; rough and early beats polished and lost. — EOMD Process (Bryan's rule)
T05 · strong · data · Research runs in two or more tools, so differing opinions surface. — Bryan, Oct 26 (ProofEr setup)
T06 · strong · layout · Avoid the subject's clichés and stock-corporate energy. — EOMD, Academies brief
T07 · strong · color · Dark text on yellow and other light brights, never white; tint a brand color that fails contrast rather than use it for text. — EOMD, Academies brief; PLTW r2
T08 · strong · layout · Check every shape for unintended readings before showing it. — EOMD, SSR poster: a shape read as something it wasn't
T09 · soft · layout · when more than one language · Key lines in the readers' languages, as a flourish or in full, with the checker named. — EOMD, Academies brief
T10 · soft · data · A popular legend the research can't back is shown with a visible myth-check label and an honest verdict, not quietly cut. — ProofEr, Pomewawa (Oct 26): "include it but label it as a myth busted"
T11 · soft · data · Lifespans as median age at death; leave "life expectancy at birth" off pop pieces, where it reads as absurd. — ProofEr, Pomewawa (Oct 26): "by that puppies die metric thr average lifespan of an old English bulldog would ve like half an hour"
T12 · soft · color · Light "paper" grounds over dark mode by default; the dark, neon-accent look reads as every other infographic. — ProofEr, Pomewawa (Oct 26): "night looks a little bit too much like every other infographic"
