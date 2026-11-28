# ProofEr

![status: beta](https://img.shields.io/badge/status-beta-ff69b4)

A repo to help you make better, better-sourced visual pieces—short **infographics** and deep **interactive data essays**—to share with the world.

ProofEr is built to be worked on with an AI coding assistant (Antigravity, Claude Code, or Codex). You bring a topic and a feeling
("a somber piece about the Holocaust"); it interviews you on format, audience, tone, and depth, runs multi-pass research and checks the
sources against each other, shows you an outline/mockup to refine, and builds a single HTML file that works offline and can be shared
anywhere. Every number on the page traces back to a source.

It uses the same working method as its sister repo, [EOMD](https://github.com/BPMData/EOMD) (motion design):
design from the brief first, open the toolbox later.

## How a piece gets made
1. **Interview (`/new-piece`).** You describe what you want in a sentence. After Round 1, the assistant checks what the
   repo already has for your piece or client profile (so you confirm instead of re-typing), asks short rounds of
   plain-English questions (format, audience, viewing context, your writing voice, landmines, and usage budget
   `light | standard | deep`), and keeps offhand jokes/asides as side notes until you call them main. No deadlines
   are asked or set.
2. **Brief.** It writes down what you agreed (`proj/<name>/brief.md`). Nothing gets designed until you approve it.
3. **Research (`auto-piece` or external tools).** By default, the assistant runs automated multi-pass parallel deep
   research + gap-fill passes into `proj/<name>/research/`. If you want to save session usage (e.g., `Budget: light`)
   or cross-check further, you can also run the prompts in two or more tools and save the reports there:
   - Claude (Research), Google Gemini (Deep Research), ChatGPT (deep research), or Kimi (Moonshot AI).
4. **Cross-check.** The assistant compares the reports into `proj/<name>/figures.md` (≥ 2 independent sources per
   checked figure), flags disagreements or weak single sources, and asks you to settle them. Only checked figures go
   on the page.
5. **Concepts, layout, and fresh-eyes review.** Two or three directions (or a picker page), followed by a section-by-section
   layout and rendered mockup stills—inspected cold by an **isolated fresh-eyes reviewer subagent** (`brief/CRAFT.md` §12,
   `stills/review.md`) before reaching you for refinement and approval.
6. **Build and QA.** Once `layout.md` is `APPROVED`, `/toolbox` opens to build a single offline HTML file (embedded fonts,
   sources section, "About these numbers" note, view counter), verified via `tools/check_offline.py`, desktop + phone
   screenshots, and a final isolated fresh-eyes QA review (`qa/review.md`), enforced by `.agents/hooks/stage_gate.py`.

## What ProofEr won't make
Pieces that dehumanize people, race-crime or race-IQ propaganda (13/52 and the like), genocide or Nakba
denial, denying or dehumanizing the Palestinian people or erasing their dead, extremist propaganda, deliberate disinformation, or attacks on private people. It's about what a piece does, not
anyone's politics: an honest, sourced piece on any contested topic is welcome. Details: `brief/CONTENT.md`.

## Try it
Open the repo in Antigravity, Claude Code, or Codex and ask for a piece in one sentence ("an interactive data essay about
clay cookware" or "an infographic about how much food school cafeterias throw away"). The `/new-piece` skill starts the
interview. Finished pieces are published in `pieces/` and on the site: https://bpmdata.github.io/ProofEr/

## Where things are
| Folder | What's in it |
|---|---|
| `brief/` | How a piece starts: the interview, the brief template, the research guide (prompts and the cross-check), the craft guide, the layout template, the house taste, client notes |
| `proj/<name>/` | One piece: its brief, research reports, checked figures, layout, stills and status |
| `pieces/` | Published pieces (infographics and interactive data essays), one offline HTML file each |
| `tools/` | Python scripts (Thonny-friendly): inline Google Fonts for offline use, check a page is offline, the reading audit, the first-question eval |
| `.claude/`, `.agents/`, `.codex/` | Skills (`new-piece`, `auto-piece`, `toolbox`), workflow runners, and stage-gate hooks across harnesses |
| `notes/` | Why it's built this way (`notes/architecture.md`) |

## Status
Published pieces live in `pieces/` (including two Holocaust pages, *The Pomewawa*, and *Knife Country*). Scope: sourced
infographics and interactive data essays (`STATUS.md`).

## License
Copyright (C) 2026 Bryan Patrick Murphy. The code is licensed under the
[GNU Affero General Public License v3.0](LICENSE) (AGPLv3): you may use, change and share it, but if you share a
changed version, or run one as a website or online service, you must share its source code under AGPLv3 too.

Pieces you make with this (their words, data, pictures and music) are yours to license however you like.
The ProofEr code inside stays AGPLv3.

When the EOMD kit ships, `vendor/eomd-kit/` will contain MIT-licensed code from EOMD included in this AGPLv3
project. The kit keeps its upstream copyright and license notices. Code moves one way, from EOMD into ProofEr.
