# Stills Visual Self-Critique (`proj/clay-cookware/stills/`)

Inspected rendered PNGs in Chromium (`still-01-hero-and-primer.png`, `still-02-charts-and-stovetop.png`, `still-03-phone-and-benchmark.png`).

## Defects Caught & Fixed (Pass 1 -> Pass 2)
1. **`still-01` running bar collision:** Left label (`CLAY COOKWARE PHYSICS`) and right benchmark chips collided with zero gap (`PHYSICSBENCHMARKS:`). Fixed with `gap: 16px; flex-wrap: wrap;` on `.running-bar`.
2. **`still-01` cross-section vertical misalignment:** `Glazed Kaolin Stoneware` subtitle wrapped onto two lines, pushing its SVG cross-section 16px lower than its three neighbors. Fixed with `min-height: 28px` on `.sub` so all four cross-sections align across the grid.
3. **`still-02` metric-box mid-range wrap:** `+10–30m` broke awkwardly across lines (`+10–` / `30m`). Reduced `.num-cell .big` to `20px` with `white-space: nowrap` and formatted as `10–30 min`.
4. **`still-03` mobile badge orphan:** `500–600 W · 3–6.5 qt` wrapped `qt` alone onto a second line next to `VitaClay VM7900 / VM7800`. Added `flex-wrap: wrap; gap: 6px;` and `white-space: nowrap` on the spec badge.

## Notes for Stage 4 Full Build
- Keep `0–200 W/(m·K)` zero-baseline bar scale for honest metal-vs-clay comparison, and add a **0–5 W/(m·K) zoomed clay-only sub-panel** directly underneath so differences between terracotta (`0.5–1.3`), Zisha (`1.3` single source), and stoneware (`1.0–4.0`) remain legible alongside the 100× gulf vs. aluminum.
- Ensure section headings use Bryan's clause-heavy voice (colons/semicolons, dry humor), maintain strong contrast (`#1A1815` on `#F7F3EA` / `#FCF9F2`), and keep interactive selectors progressive-enhanced so the static page reads completely on its own.

## Pass 3 (Client Feedback Refinements)
- Replaced the confusing Römertopf offset trivia box in `still-02` with a clear, actionable **Do / Don't rule for ALL unglazed, water-soaked clay bakers** (`10–20 min` soak, cold oven start, `+100°F` / `400–450°F` dial, uncover final `15–20 min`), moving the `+50°F` vs. `+100°F` (`+50°C`) unit confusion into an optional `<details>` drill-down.
- Added the `0–5 W/(m·K)` clay-only zoom sub-panel underneath the `0–200` thermal conductivity bar chart.
- Updated `layout.md` with 5 hands-on interactive demonstrations/simulators + pervasive `<details>` drill-downs (`knife-country` mechanism pattern) while preserving the test-kitchen notebook aesthetic.
