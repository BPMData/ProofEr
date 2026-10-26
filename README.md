# ProofEr

![status: beta](https://img.shields.io/badge/status-beta-ff69b4)

A repo to help you make better, better-sourced infographics to share with the world.

ProofEr is built to be worked on with an AI coding assistant (Claude Code). You bring a topic and a feeling
("a somber infographic about the Holocaust"); it interviews you, sends you off to gather research, checks the
sources against each other, shows you options, and builds a single HTML file that works offline and can be shared
anywhere. Every number on the page traces back to a source.

It uses the same working method as its sister repo, [EOMD](https://github.com/BPMData/EOMD) (motion design):
design from the brief first, open the toolbox later.

## How a piece gets made
1. **Interview.** You describe what you want in a sentence. The assistant asks short rounds of plain-English
   questions: who it's for, where it'll be seen (phone, projector, print), the tone, what it must never say.
2. **Brief.** It writes down what you agreed. Nothing gets designed until you approve it.
3. **Research (you run this step).** The assistant writes deep-research prompts for the facts the piece needs. You
   run them in one or more deep-research tools and save the reports into the piece's `research/` folder:
   - Claude (the Research mode in the Claude app),
   - Google Gemini (Deep Research),
   - ChatGPT (deep research),
   - Kimi (Moonshot AI).

   Running the same prompt in two or three of them is the point:
   - **Differing opinions.** Different tools find different sources and make different mistakes. Where they
     disagree, that's exactly the number that needs a closer look.
   - **Saving your Claude usage.** Deep research is long and expensive. Running it in tools you already have leaves
     your Claude usage for the design and build.
4. **Cross-check.** The assistant compares the reports, lists every figure with its sources, flags the ones that
   disagree or rest on a single weak source, and asks you to settle them. Only checked figures go on the page.
5. **Concepts.** Two or three directions, shown as a picker page: you answer with a letter ("B, but calmer").
6. **Layout and stills.** The page in reading order, with mockups, before any building tools are opened.
7. **Build.** A single offline HTML file, with a sources section and an "About these numbers" note.

## Status
Just started. The working rules, interview, brief template, research templates and toolbox come next, adapted from
EOMD. Recipe cards (history-themed, like a 1915 war bread) are planned as a second kind of piece.

## License
Copyright (C) 2026 Bryan Patrick Murphy. The code is licensed under the
[GNU Affero General Public License v3.0](LICENSE) (AGPLv3): you may use, change and share it, but if you share a
changed version, or run one as a website or online service, you must share its source code under AGPLv3 too.

Pieces you make with this (their words, data, pictures and music) are yours to license however you like; the code
inside stays AGPLv3.
