# Pomewawa: status
Stage: build, done and published to `pieces/pomewawa.html` (card in `index.html`). Goes live on GitHub Pages once
the branch `claude/wonderful-tesla-l3dhpf` is merged to `main`.

## QA report (Oct 26, 2026)
Verified:
- **Facts:** every number, name and date on the page is a `checked` or `checked*` row in `figures.md`; unverified
  rows (F25, F26 Chi, F27, F36, F37) are not on the page. The 7.9-year figure appears
  only in "About these numbers" as the explanation Bryan asked to leave off the charts.
- **Sources:** 27-item sources list at the end, body-size type; "About these numbers" explains lifespans, surveys,
  standards, bite force, myth checks and what was left out.
- **Charts:** all bars start at 0 with labeled units (cm, lb, years, kg); same scale within each chart; ranges drawn
  as ranges.
- **Offline:** `tools/check_offline.py` passes; Playwright with every network request blocked loads both fonts
  (Barlow Condensed, Source Serif 4, SIL OFL) and makes zero remote calls.
- **Contrast (WCAG AA):** ink/paper 14.4:1, accent/paper 5.1:1, dim/paper 6.6:1, accent/card 4.7:1, dim/card 6.2:1.
- **Phone:** 390 px wide, no sideways scroll; the headline reads at a glance.
- **Accessibility:** each chart has a text alternative (role="img" + aria-label); headings in order; no motion.
- **Print:** 12 Letter pages, menu entries print open, bar colors kept, sections don't split.
Not verified / known limits:
- Sources were confirmed through search results, not by opening the papers (network policy blocked nature.com,
  PMC, akc.org). `checked*` rows rely on secondary sources.
- Screen-reader pass with a real reader not done; checked by structure only.
- Usage not recorded (brief `Usage:` line).
