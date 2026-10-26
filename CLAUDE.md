# CLAUDE.md

ProofEr makes infographics: single offline HTML pages that explain something with numbers, where every number
traces back to checked sources. The repo is maintained by Bryan Murphy; a client can be anyone, and is usually not
technical. The method is the one from [EOMD](https://github.com/BPMData/EOMD): context follows the stage, design
comes before tools (`notes/architecture.md`).

Read the root `STATUS.md` index at the start of every session; read a piece's own `STATUS.md` (in `proj/<name>/`)
when working on that piece. Update both at the end of a working session.

## Rules for every piece
- **Never invent facts:** no number, name, date, place or quote that isn't in the piece's checked figures table
  (`proj/<name>/figures.md`) or the client's own copy. If it's missing, ask, or send it to research.
- **Every figure has sources:** at least two independent ones, primary sources preferred, each a real document you
  can name. A figure the sources disagree on is shown as a range or with a note, never as false precision. The page
  ends with a sources section and an "About these numbers" note.
- **Honest charts:** bar and area charts start at zero, areas are proportional to values, scales are labeled, and
  nothing is cherry-picked to make a point the data doesn't support (`brief/CRAFT.md`).
- **Copy is word for word:** text from the client's copy files appears exactly as written. Translations Claude
  drafted are marked **DRAFT**.
- **A piece is a single offline HTML file:** fonts, data, code and images inlined; nothing loads from the internet
  (`tools/embed_fonts.py` inlines Google Fonts). Open-licensed fonts only, license noted.
- **Readable and accessible:** sizes from where it's read (phone, projector, print, poster); WCAG AA contrast,
  reported honestly; color never the only carrier of meaning; a text alternative for every chart;
  prefers-reduced-motion respected; it prints cleanly.
- **Research tools:** recommend only Claude (Research), Gemini (Deep Research), ChatGPT (deep research) and Kimi.
  Don't suggest any other tool unless the user adds it here.
- **What ProofEr won't make** (`brief/CONTENT.md`): pieces that dehumanize people, race-crime or race-IQ
  propaganda (13/52 and kin), genocide or Nakba denial, denying that a people (such as Palestinians) exists,
  extremist propaganda, disinformation, or attacks on private people.
  Decline in one line ("Nah. ProofEr doesn't make that one.") and stop, at any stage. It's about what a piece does,
  not anyone's politics.
- **Client context:** once the interview shows who the client is, read their file in `brief/clients/` if there is
  one.

## New pieces: interview first
Before any NEW piece, run `/new-piece`: interview the client, then write `proj/<name>/brief.md` and get it approved.
A one-line request ("a somber infographic about the Holocaust") is the start of the interview, not the brief.
- **Gates:** interview → brief approved → research (the client runs the prompts) → figures checked → concepts →
  layout and stills approved → build → QA. The brief's status line carries `Stage:`.
- **Research is the client's step.** Claude writes the prompts (`brief/RESEARCH.md`); the client runs them in two or
  more deep-research tools and saves the reports in `proj/<name>/research/`. Different tools give differing
  opinions, and running research outside Claude saves the client's Claude usage.
- **Design comes before tools.** Until the layout is approved, stay out of `pieces/`, `examples/`, `tools/` and other
  pieces' `proj/` folders (`notes/architecture.md`, "The restricted list"). They open with `/toolbox` at the gate.
- **Earlier pieces are examples, not a menu.** Take mechanisms from them, never their look.
- **The client reads no jargon.** Everyday words in every question and everything they see.

## Where to go
| Task | Go to |
|---|---|
| A new piece | `/new-piece`; `/toolbox` at its gate |
| A change to an existing piece | `proj/<name>/` (its brief, figures, status) |
| How pieces start | `brief/`: `CONTENT.md` (what it won't make), `INTERVIEW.md`, `TEMPLATE.md`, `RESEARCH.md`, `CRAFT.md`, `LAYOUT.md`, `taste/house.md`, `clients/` |
| Published pieces | `pieces/` (one HTML each), linked from `index.html` (the Pages site; `.nojekyll` must stay) |
| Tools | `tools/` (its `CLAUDE.md` loads when you open it) |
| CI | `.github/workflows/` (stage-read audit, offline check, first-question eval); the stage-read hook is in `.claude/settings.json` |
| Why it's built this way | `notes/architecture.md` |

## Maintainer rules
- **Scripts Bryan runs are Thonny-friendly:** the Run button, no command-line arguments, every setting in a
  `SETTINGS` block at the top.
- **Edit in place, commit per stage**, with a message that says what changed.
- **Verdicts are kept:** every client verdict goes into the brief's Decisions log, in the client's words. A verdict
  that would hold for other pieces becomes or adjusts an item in `brief/taste/house.md`.
