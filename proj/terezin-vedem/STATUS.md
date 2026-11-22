# STATUS: terezin-vedem

- **Stage:** done (`pieces/terezin-vedem.html` built, embedded offline, and QA'd; `index.html` & root `STATUS.md` updated)
- **Format:** Scrolling interactive data essay (English-only; dark-slate mode matching `:root[data-theme="dark"]` of `nazi-victims-all-groups.html` and `holocaust-by-country.html` + clean light `@media print`)
- **Budget:** deep (`pass1` 5 workers + `gap_fill` 4 workers -> 28 checked entries in `figures.md`)
- **QA verified:**
  - `python3 tools/check_offline.py` -> 6 files checked, 0 remote loads (`1.67 MB` self-contained HTML with 16 font faces + 7 licensed PD/CC BY-SA archival images inlined)
  - Chromium QA (`proj/terezin-vedem/qa/`): `desktop.png` (1280px, 0 overflow), `phone.png` (390px, 0 overflow), `interactive-sheet.png` (toggle, tab switch, and `dialog#sheet` verified), `print.png` (`@media print` verified), 0 console/page errors.
- **Nov 22 edit:** inline glosses for *casemates* (crowding paragraph + Fritta caption) and a *Madrich* note under the *Vedem* editorial; `check_offline.py` OK, 0 overflow at 1280/390. **Open:** follow-up research on the Birkenau family camp thread (prompt given in chat; reports go in `research/`).
- **Nov 22 family-camp update (published):** four research reports (`research/report-*-family-camp.*`) cross-checked into F29–F37; unsourced von Thadden line replaced; new "Where the 7,503 went" passage + range bar chart; About/sources updated. `check_offline.py` OK, view counter present, 0 overflow / 0 errors at 1280, 390 and print; chart shots in `qa/family-camp-chart*.png`.
