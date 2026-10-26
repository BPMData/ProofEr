# Brief: <piece name>

Status: DRAFT | APPROVED <date> by <name> · Stage: interview | brief | research | figures | concepts | layout | build · Mode: quicker | from scratch · Client: <name> · Sign-off: <names>
Usage: <model, effort> · <share of a 5-hour limit, per stage, as the Claude app or Claude Code shows it>

_Copy to `proj/<name>/brief.md` once round 1 of the interview (`INTERVIEW.md`) is answered, and update `Stage:` at
each gate. Write it in the client's words and keep the reasons. **ASK** = missing, **DRAFT** = Claude's draft,
**Claude's call** = delegated by the client._

## 1. The ask
_Topic, audience, where it's seen, by when._

## 2. Purpose and tone
_What readers should know, feel and do afterwards; three tone words; what it must not feel like._

## 3. How it's read
_Medium (phone, laptop, projector, print, poster), distance, time spent, read alone or presented. This decides type
sizes, density and whether it can scroll._

## 4. The subject
_The story behind the numbers; common misconceptions; what it must never say, compare, rank or show, and why._

## 5. The questions the numbers must answer
_Each question becomes research. Figures the client already has go here with their origin; they still get checked._

| # | Question | Why it matters to the reader |
|---|---|---|
| Q1 | | |

## 6. Research plan
_Which tools the client will run (two or more), which prompts (`proj/<name>/research/prompts.md`), and any sources the
client trusts or distrusts. Checked figures live in `proj/<name>/figures.md`, never here._

## 7. Structure and reading order
_Sections, what the eye hits first, what's hero and what's support._

## 8. Brand and contrast
_Colors (hex and role), fonts, logos; contrast rules._

## 9. Language
_Languages, which lines, who checks translations._

## 10. Call to action and credit
_The reader's next step; author and publisher credit. Nothing invented._

## 11. Hard limits
_Images, claims, likenesses, anything an institution won't allow._

## 12. Taste
`Taste: house. Applies: <IDs from brief/taste/house.md whose condition this brief meets>. Overrides: <ID off or
changed, with the reason>.`
_Then the client's own loves and hates, with why._

## 13. Craft bar
Default (`CRAFT.md`); this piece adds or relaxes: _..._
- One message a reader could repeat after five seconds; everything else supports it.
- The chart form chosen for the question, not for novelty; honest scales; direct labels over legends.
- One visual idea grown from this subject that makes the numbers felt, not just shown.
- Uncertainty shown honestly (ranges, "about", notes), never hidden for a cleaner look.
- Dignity on human subjects: people are never decoration, never gamified.

## 14. Technical
Repo defaults (CLAUDE.md "Rules for every piece"): one offline HTML file, embedded open-licensed fonts, text
alternatives, prints cleanly. Exceptions: _..._

## 15. Deliverables
_Files (web page, print PDF, social image), sizes, where it's published (`pieces/`, the Pages site)._

## 16. QA
Default checks; add the piece's own:
- Facts: every number, name and date on the page has a row in `figures.md` with status `checked`.
- Sources: the page's sources section lists every source used, and "About these numbers" explains disagreements.
- Charts: zero baselines on bars and areas, proportional areas, labeled units and scales.
- Legibility: readable at the brief's distance; at 25% scale the headline still reads.
- Contrast: every text/background pair meets WCAG AA, reported honestly; color isn't the only cue.
- Offline: opens with the network off (`tools/check_offline.py`); fonts embedded.
- Accessibility: chart text alternatives; reading order makes sense to a screen reader; reduced motion respected.
- Print: one clean print preview (no cut-off sections, no dark-background ink flood unless intended).
- Taste: every applicable `strong` item in `brief/taste/house.md` is honored, or overridden in §12 with a reason.
- A short report: what was verified, what wasn't, known limits.

## 17. Approval and success
_Who signs off; what makes them say "that's it"._

## 18. Open questions
_Every ASK above, in one list._

## Decisions log
_Date · the decision or verdict, in the client's words · what changed._
