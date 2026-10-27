# Interviewing the client

Every new infographic starts with an interview and doesn't leave it without an approved brief
(`proj/<name>/brief.md`, made from `TEMPLATE.md`). First requests are a feeling and a topic ("a somber infographic
about the Holocaust"). The interview turns that into a message, an audience, the questions the numbers must answer,
and the lines the piece must never cross.

## How to run it
- **Small rounds.** 2–3 questions per message, most important first. The client may answer in shorthand.
- **Ask round 1 first;** open nothing else before it. Once round 1 is answered, copy `TEMPLATE.md` to
  `proj/<name>/brief.md` with `Stage: interview` and fill it in as answers come. Once you know who the client is,
  read their file in `clients/` if there is one.
- **Confirm instead of asking** whatever earlier answers already imply: one line of assumptions and "right?".
- **Ask about the problem, not the solution:** who reads it, where, what they should understand afterwards. Not
  "which chart do you want?"
- **Talk to a non-technical client.** Short sentences, no jargon ("waffle chart", "WCAG", "primary source" stay in
  the brief). Ask in experience terms: "should someone get it in five seconds, or sit with it?"
- **Turn vague words into choices.** "Somber", "clean", "punchy" mean nothing until pinned down: offer contrasts
  (quiet or stark? numbers first or people first?) or ask for one infographic they love and one they hate, and why.
- **Check the purpose first.** If the request (or anything that comes out later) is on the list in `CONTENT.md`,
  decline in one line and stop; don't interview your way around it.
- **Hunt the landmines:** comparisons it must never make, groups it must never rank, words it must never use, images
  it must never show. Sensitive subjects need these most.
- **Facts come from research, not from you.** Never fill a gap from memory, not even a "well-known" number. Keep a
  running list of the figures the piece needs; they become the research prompts.
- **Weigh asides before you build on them.** Clients think out loud: jokes, "yeah fine, maybe we should mention X",
  "I'm not sure, maybe research can find out". An aside is a **side note** until the client says otherwise. It never
  becomes a framing line, its own research question or a section by itself. Log it as a side note, and in the next
  reflect-back ask what weight it gets: "You mentioned X. Main point, a quick side note, or just a joke?" Only an
  answer of "main point" makes it a main point.
- **Reflect back** in one sentence per round ("So: a poster for a 10th-grade history class, read up close, about how
  many people the Holocaust killed in each country, quiet and respectful.").
- **Delegation must be explicit.** "You decide" is fine for design. It is never an answer for the facts, the
  message, the audience or the landmines.
- **Closed questions as buttons** where the tool allows (Claude Code: `AskUserQuestion`); open questions in text.

## Questions
★ = every piece. Numbers = sections of `TEMPLATE.md`.

**1. The ask**
- ★ What is it about, who is it for, where will they see it, and by when? *"A poster about school lunch waste for
  the cafeteria wall, by December."*
- ★ How to build it (skip this until the toolbox holds earlier work: see `STATUS.md`; until then every piece is made
  from scratch). In everyday words: "Quicker, built from designs this kit already has; or from scratch, designed only
  for yours. From scratch uses more of your Claude usage. Which would you like?"

**2. Purpose and tone**
- ★ After reading, what should someone know, feel and do? One line each.
- ★ Three words for the tone, and what it must NOT feel like.

**3. How it's read**
- ★ Phone, laptop, projector, printed handout, poster on a wall? How far away, for how long?
- ★ Does someone read it alone, or does a teacher or speaker walk people through it?

**4. The subject**
- ★ What's the story behind the numbers, in their words? What do people usually get wrong about it?
- ★ What must it never say, compare, rank or show?

**5. The questions the numbers must answer**
- ★ Which questions should the infographic answer? *"How many? Where? Compared with what? Over what years?"*
- Numbers they already have, and where each came from (they still go through research).
- Is any copy fixed word for word? Where's the file?

**6. Research**
- ★ Which deep-research tools can they use: Claude (Research), Gemini (Deep Research), ChatGPT (deep research), Kimi?
  Two or more is best. Explain why in one line each: different tools find different sources (differing opinions),
  and research run outside Claude saves their Claude usage.

**7. Structure and reading order**
- One big number, or several sections? What should the eye hit first?

**8. Brand and contrast**
- ★ Colors, fonts, logos, any style rules (a logo file or a website to match is enough).

**9. Language**
- ★ Who reads it? Other languages for key lines, and who checks the translations?

**10. Call to action and credit**
- ★ Is there a next step for the reader? Whose name goes on it as author or publisher?

**11. Hard limits**
- Images we can't use (photos of real people, especially victims), claims we can't make, anything a school, museum or
  publisher won't allow?

**12. Taste**
- ★ One infographic or chart they love and one they hate, and why.
- The house taste (`taste/house.md`) applies by default; don't read it out. List the items that apply in §12 and ask
  only about the ones this client might want different.

**13–16. Craft bar, technical, deliverables, QA:** the template has defaults; ask only "anything to add or relax?"
and ★ which files (web page, printable PDF, an image for social media) and where it gets published.

**17. Approval**
- ★ Who else signs off (a department, a museum educator, a principal)? Bring them in now.

## After the interview
The brief's status line carries `Stage:` (interview → brief → research → figures → concepts → layout → build), so any
session knows where the piece is and what it may open. Update it at each gate and commit. While the stage is before
`build`, a hook logs every read to `proj/<name>/access.jsonl` (it never blocks anything); commit that log with each
stage commit.

1. **Reflect back** the whole piece in one paragraph, plus the open questions. Name the side notes separately
   ("Side notes, a line each unless you say otherwise: ..."), so the client sees how much room each one gets.
2. **Draft the brief** (`Stage: brief`) in the client's words, with the reasons kept. Mark gaps **ASK** and Claude's
   drafts **DRAFT**. Commit.
3. **Approval.** The client approves or edits it. No research prompts and no design before this.
4. **Research** (`Stage: research`): follow `RESEARCH.md`. Write the prompts, hand them over, and wait for the
   reports in `proj/<name>/research/`.
5. **Figures** (`Stage: figures`): cross-check the reports into `proj/<name>/figures.md` (`RESEARCH.md`). The client
   settles every disputed figure. No figure reaches a concept until it's checked.
   - **Quicker mode: the gate opens here.** Run `/toolbox` now.
6. **Concepts** (`Stage: concepts`): read `CRAFT.md` first. 2–3 directions, shown as a choice panel.
7. **Layout and stills** (`Stage: layout`): copy `LAYOUT.md` to `proj/<name>/layout.md`: sections in reading order,
   each with its figures (by ID), and 2–3 mockups.
   - **From-scratch mode: the gate opens here,** once layout and stills are approved. Run `/toolbox`.
8. **Build** (`Stage: build`): the build plan from `/toolbox`, then build, then QA (`TEMPLATE.md` §16).

## Usage estimates
No piece has had its usage recorded yet. Every brief logs it (the status line's `Usage:` line). Research run in
other tools costs no Claude usage at all.
