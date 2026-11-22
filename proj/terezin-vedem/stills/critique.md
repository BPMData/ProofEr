# Visual Self-Critique: `terezin-vedem` Stills

## Revision 3 — Dark-Slate Default (Client-Approved Companion Mode)
Updated all 3 stills to dark-slate mode (`--bg:#15171A; --surface:#1C1F23; --ink:#E7E4DD; --muted:#A2A6AD; --rule:#34383E; --killed:#B5475A; --survived:#5B5750; --ally:#79AFCF; --reich:#D4A650;`) matching `:root[data-theme="dark"]` of `pieces/nazi-victims-all-groups.html` and `pieces/holocaust-by-country.html`.

## Defects caught & fixed during dark-slate PNG inspection
1. **Surface variable collision (`still-01/02/03`):** Caught `.surface-panel` and `.quote-block.vedem` inadvertently rendering `#E7E4DD` instead of `#1C1F23`; restored `--surface: #1C1F23` and `#1C1F23` SVG label halos.
2. **Dark ink on light accent bars (`still-03`):** Switched `.mbar .o` (`#79AFCF` slate-blue) text color to `#15171A` (high contrast ~8.3:1 vs. low white-on-sky-blue contrast). Also flagged `.mbar .j` (`#B5475A`) for final build contrast tuning (`#15171A` dark text or `#9C3548` fill with `#FFF3F4` so WCAG AA >= 4.5:1 passes cleanly).

Inspected all updated PNGs (`still-01-hero-and-crowding.png`, `still-02-redcross-facade.png`, `still-03-butterfly-vedem.png`) in Chromium at `2×` scale.
