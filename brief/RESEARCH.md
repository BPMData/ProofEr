# Research: prompts out, reports in, figures checked

The client runs the research. Claude writes the prompts, then cross-checks what comes back. Two reasons, worth
telling the client in one line each:
- **Differing opinions.** Different tools search differently, find different sources and make different mistakes.
  Where two reports disagree is exactly where a figure needs a closer look.
- **Saving Claude usage.** Deep research is long and expensive. Running it in tools the client already has leaves
  their Claude usage for checking, design and build.

**Tools to suggest:** Claude (the Research mode in the Claude app), Google Gemini (Deep Research), ChatGPT (deep
research), Kimi. Two or more per piece; the same prompt in each. Suggest no other tool unless it's added here.

Claude Code can search the web and read pages itself, so it can open a cited source to check one figure. It doesn't
replace a deep-research run: use it to verify, not to gather.

## 1. Write the prompts (`Stage: research`)
One prompt per group of related questions from brief §5, saved in `proj/<name>/research/prompts.md`. Each prompt:
- **States the questions exactly,** with the place, the years and the unit ("number of Jewish people killed,
  1939–1945, by country, using pre-war 1939 borders").
- **Asks for sources:** for every figure, the source's title, author or institution, year, page or table, and a
  link; primary sources (official records, scholarly works, archives, statistical agencies) before secondary.
- **Asks for disagreement:** "Where reputable sources give different figures, list each figure with its source and
  explain why they differ (definitions, borders, years, methods)." Never "give me the number".
- **Asks for a table** (figure, value or range, unit, source, year, notes), so reports can be compared.
- **Says what not to do:** no figures without a source; no unsourced round numbers; flag estimates as estimates.
- Fits the subject's sensitivity: for atrocities, ask for the recognized scholarly and memorial institutions'
  figures and how they were estimated.

Hand them to the client in everyday words: which tool, paste this, save the full report (with its links) as
`proj/<name>/research/<tool>-<question group>.md` (or send it in the chat and Claude saves it).

## 2. Cross-check into `figures.md` (`Stage: figures`)
Make `proj/<name>/figures.md`: one row per figure the piece may show.

| ID | Figure (what exactly) | Value used | Sources (title, year, where) | Reports that agree | Disagreement | Status |
|---|---|---|---|---|---|---|
| F01 | | | | | | checked / disputed / single source / unverified |

Rules:
- **Two independent sources** for `checked`, at least one primary. Two reports citing the same source count once.
- **Open the source** when you can (Claude Code can fetch pages): confirm the number is really there, in that unit,
  for that place and year. A citation that doesn't exist or doesn't say it is a red flag on the whole report; note it.
- **Disagreement is information:** record each value with its source and the reason they differ. Decide nothing
  alone: show the client the options in plain words ("Source A counts by 1939 borders, B by today's; A says X, B
  says Y. Show X, show a range, or show both with a note?"). Their call goes in the Decisions log.
- **Single source or unverified** figures don't go on the page, unless the client accepts them with a visible note.
- **Rounding** is stated ("about 6 million"); the exact value and its source stay in the table.
- Every source used ends up in the page's sources section.

When every figure the layout will need is `checked` (or accepted with a note), move the brief to `Stage: concepts`.
