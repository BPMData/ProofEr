# ProofEr ↔ EOMD merge map

EOMD inventory read from the sibling checkout on `claude/html-tricks-eomd-aa1cb6` at
`aa55cd706674ea8eab4ac7fa2740cefc7860a9fa`. The boundary and kit plan are in that branch’s
`TODO.md` §0, which began in [EOMD PR #18](https://github.com/BPMData/EOMD/pull/18).

The table covers every Git-managed ProofEr file and its parent folders, plus the reserved vendor paths. A
trailing slash means a directory. Local caches, worktrees, and ignored build products are outside the inventory.
`none` means no current path counterpart. When moving a project, keep its entire subtree with its slug.

## Shared conventions and deliberate differences

- Both repos use a root `STATUS.md` index and `proj/<name>/brief.md` with a `Stage:` line. Individual project
  briefs, status files and artifacts belong to their own slugs. The shared convention is a path pattern,
  independent of which pieces exist.
- Maintainer scripts run from Thonny with no arguments and a top-level `SETTINGS` block. Both repos pin Prettier
  3.3.3 and use the same `.prettierrc`. Their ignore lists reflect their own output.
- The hooks use the same receipt record shapes. Subagent JSONL records use `ts`, `tool`, `review`. Review JSONL
  records use `ts`, `tool`, `stage`, `html_sha256`. PNG inspection JSON uses relative PNG keys with timestamps
  and `_sha256_pngs`. The final check uses JSON with `ts`, `sha256`, `cmd`.
- Receipt placement and triggers differ. ProofEr puts `.subagent_receipts.jsonl` under
  `proj/<name>/research/` and writes `.offline_checked.json` after its offline check. EOMD puts the subagent
  receipt at the project root and writes `.qa_checked.json` for its audio/render/player checks. Both keep
  `.review_receipts.jsonl` and `.inspected_pngs.json` at the project root. They hash their own published HTML.
  Preserve these distinctions when merging the hook implementations.
- Both checked-in root licenses are AGPLv3. EOMD’s plan specifies a separately MIT-licensed kit. The kit is
  the one-way code path from EOMD into ProofEr.
- `tools/check_drift.py` compares the same-purpose rows and selected collisions with a shared implementation.
  File rows compare bytes and folder rows compare their tracked path inventories. The script pins known
  differences so later edits surface as drift. It reads the current EOMD working tree and produces warnings only.

## Path inventory

| ProofEr | EOMD | Relationship | Merge notes |
|---|---|---|---|
| `.agents/` | `.agents/` | same purpose, same name | Cross-harness automation. ProofEr adds a research workflow. |
| `.agents/hooks.json` | `.agents/hooks.json` | same purpose, same name | Same harness and core hook. ProofEr includes events for the research workflow. |
| `.agents/hooks/` | `.agents/hooks/` | same purpose, same name | Gate scripts and tests. Gate logic differs. See the receipt notes below. |
| `.agents/hooks/stage_gate.py` | `.agents/hooks/stage_gate.py` | name collision with a different meaning | Shared origin and receipt schema. ProofEr gates research, checked figures, layout and offline QA. EOMD gates storyboard, sound and player QA. |
| `.agents/hooks/test_stage_gate.py` | `.agents/hooks/test_stage_gate.py` | name collision with a different meaning | Tests the different gate contracts. |
| `.agents/skills/` | `.agents/skills/` | name collision with a different meaning | ProofEr workflow skills combine research and visual QA. EOMD skills coordinate motion design and audio. |
| `.agents/skills/auto-piece/` | `.agents/skills/auto-piece/` | name collision with a different meaning | ProofEr researches and verifies claims before building. EOMD builds motion and calibrates audio. |
| `.agents/skills/auto-piece/SKILL.md` | `.agents/skills/auto-piece/SKILL.md` | name collision with a different meaning | ProofEr research, figures, layout and offline QA versus EOMD storyboard, audio and frame QA. |
| `.agents/skills/new-piece/` | `.agents/skills/new-piece/` | name collision with a different meaning | Both interview first. ProofEr prepares sourced pieces and EOMD prepares screen motion pieces. |
| `.agents/skills/new-piece/SKILL.md` | `.agents/skills/new-piece/SKILL.md` | name collision with a different meaning | Different formats and gates after the shared interview. |
| `.agents/workflows/` | none | ProofEr-only | |
| `.agents/workflows/research_piece.py` | none | ProofEr-only | Multi-pass research and figures workflow. |
| `.claude/` | `.claude/` | same purpose, same name | Claude Code integration. Agent and settings inventories follow each repo. |
| `.claude/agents/` | `.claude/agents/` | same purpose, same name | Isolated reviewers and workers. ProofEr adds a research worker. |
| `.claude/agents/fresh-eyes-reviewer.md` | `.claude/agents/fresh-eyes-reviewer.md` | same purpose, same name | Same isolated review. ProofEr checks sourced figures, charts and reading layout. EOMD checks timed frames and audio QA. |
| `.claude/agents/research-worker.md` | none | ProofEr-only | Isolated deep research worker. |
| `.claude/hooks/` | `.claude/hooks/` | same purpose, same name | Stage-read logging. |
| `.claude/hooks/stage_log.py` | `.claude/hooks/stage_log.py` | same purpose, same name | Same read-log contract. Project paths and gates differ. |
| `.claude/settings.json` | `.claude/settings.json` | same purpose, same name | Same stage-gate wiring. |
| `.claude/skills/` | `.claude/skills/` | name collision with a different meaning | Repo-specific workflow skills share names and entry points. |
| `.claude/skills/auto-piece/` | `.claude/skills/auto-piece/` | name collision with a different meaning | Claude Code entry point to each repo’s autonomous workflow. |
| `.claude/skills/auto-piece/SKILL.md` | `.claude/skills/auto-piece/SKILL.md` | name collision with a different meaning | ProofEr research and offline QA versus EOMD calibrated audio and frame QA. |
| `.claude/skills/new-piece/` | `.claude/skills/new-piece/` | name collision with a different meaning | Claude Code entry point for each repo’s new-piece flow. |
| `.claude/skills/new-piece/SKILL.md` | `.claude/skills/new-piece/SKILL.md` | name collision with a different meaning | Different formats and gates after the shared interview. |
| `.claude/skills/toolbox/` | `.claude/skills/toolbox/` | same purpose, same name | Toolbox entry point. There are different gates and tools. |
| `.claude/skills/toolbox/SKILL.md` | `.claude/skills/toolbox/SKILL.md` | name collision with a different meaning | ProofEr opens tooling around checked figures or approved layout. EOMD opens it around the approved brief or storyboard. |
| `.claude/skills/toolbox/choice-panel.html` | `.claude/skills/toolbox/choice-panel.html` | same purpose, same name | Same client-choice UI. Labels and choices fit each workflow. |
| `.codex/` | `.codex/` | same purpose, same name | Codex integration. |
| `.codex/config.toml` | `.codex/config.toml` | same purpose, same name | Codex project configuration. Agent setup follows each repo. |
| `.codex/hooks.json` | `.codex/hooks.json` | same purpose, same name | Same stage-gate wiring. |
| `.git-blame-ignore-revs` | `.git-blame-ignore-revs` | same purpose, same name | Formatting revisions are specific to each Git history. |
| `.gitattributes` | none | ProofEr-only | Git preserves the exact vendored kit bytes. |
| `.github/` | `.github/` | same purpose, same name | GitHub configuration. EOMD also has issue templates. |
| `.github/workflows/` | `.github/workflows/` | same purpose, same name | CI and first-question eval. |
| `.github/workflows/ci.yml` | `.github/workflows/ci.yml` | same purpose, same name | ProofEr checks offline pages, hook behavior and the vendored kit. EOMD checks engine builds and audio. Both run Prettier and audit stage reads. |
| `.github/workflows/eval.yml` | `.github/workflows/eval.yml` | same purpose, same name | Same first-question eval workflow. The fixture and paths belong to each repo. |
| `.gitignore` | `.gitignore` | same purpose, same name | Local files, generated output and receipts differ by repo. |
| `.nojekyll` | `.nojekyll` | same purpose, same name | Publish the Pages tree as-is. |
| `.prettierignore` | `.prettierignore` | same purpose, same name | Exclusions follow each repo. ProofEr also protects the vendored kit bytes. |
| `.prettierrc` | `.prettierrc` | same purpose, same name | Identical config. Both pin Prettier 3.3.3. |
| `AGENTS.md` | `AGENTS.md` | same purpose, same name | Agent entry point, with repo-specific gates. |
| `CLAUDE.md` | `CLAUDE.md` | same purpose, same name | Rules, stage order and routing. ProofEr has research, figures and offline publication rules. |
| `LICENSE` | `LICENSE` | same purpose, same name | Identical AGPLv3 root license texts. The planned EOMD kit has a separate MIT grant. |
| `README.md` | `README.md` | same purpose, same name | Public overview for each repo and its output. |
| `STATUS.md` | `STATUS.md` | same purpose, same name | Session-start index linking to individual status files. ProofEr uses bullets for pieces and EOMD uses a table. |
| `brief/` | `brief/` | name collision with a different meaning | ProofEr’s claims, research and layout guidance versus EOMD’s screen motion, sound and storyboard guidance. |
| `brief/CONTENT.md` | none | ProofEr-only | Content policy for sourced pieces. |
| `brief/CRAFT.md` | `brief/CRAFT.md` | same purpose, same name | Shared design-before-tools and fresh-eyes principles. ProofEr adds honest charts, uncertainty and motion-essay craft. EOMD covers sound and screen design. |
| `brief/INTERVIEW.md` | `brief/INTERVIEW.md` | same purpose, same name | Shared interview core. ProofEr adds sources, claims, format depth and the planned motion essay. EOMD covers screen pieces and engine-led options. |
| `brief/LAYOUT.md` | `brief/STORYBOARD.md` | same purpose, different name | Prebuild approval template. ProofEr plans reading order and Figure IDs. EOMD plans timing, picture and sound. |
| `brief/RESEARCH.md` | none | ProofEr-only | Research and figures-table instructions. |
| `brief/TEMPLATE.md` | `brief/TEMPLATE.md` | same purpose, same name | Both copy to proj/<name>/brief.md with a Stage: line. ProofEr adds research and figures stages and uses layout where EOMD uses storyboard. |
| `brief/clients/` | `brief/clients/` | same purpose, same name | Client profiles. |
| `brief/clients/bryan.md` | `brief/clients/bryan.md` | same purpose, same name | Same client. Each profile selects the context relevant to its repo. |
| `brief/taste/` | `brief/taste/` | same purpose, same name | House taste guidance. |
| `brief/taste/house.md` | `brief/taste/house.md` | same purpose, same name | Shared approach to recording verdicts. Rules and IDs follow each repo. |
| `index.html` | `index.html` | same purpose, same name | Pages landing page and publication index. Each lists its own output. |
| `notes/` | `notes/` | same purpose, same name | Architecture and maintenance notes. Each repo has its own files. |
| `notes/architecture.md` | `notes/context-plan.md` | same purpose, different name | Progressive disclosure and stage order, adapted for sourced pieces. |
| `notes/merge-map.md` | none | ProofEr-only | Sister-repo path and divergence inventory. |
| `package-lock.json` | `package-lock.json` | same purpose, same name | Same Prettier version. Package metadata is repo-specific. |
| `package.json` | `package.json` | same purpose, same name | Dev tooling with identical Prettier pin. Package names and descriptions differ. |
| `pieces/` | `players/` | same purpose, different name | Published HTML outputs. ProofEr publishes sourced offline pages. EOMD publishes motion players. Individual pieces have separate identities. |
| `pieces/README.md` | none | ProofEr-only | |
| `pieces/assets/` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/agatha.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/albarello.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/angel1.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/benedict.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/bosch.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/bust.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/capello.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/exvoto.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/float.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/goddess.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/gratteri.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/guidobono.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/isis.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/joseph.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/lettera.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/louis.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/lucy.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/lucybody.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/rosalia.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/steri.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/urn.webp` | none | ProofEr-only | |
| `pieces/assets/sicilian-folk-magic/woodcut.webp` | none | ProofEr-only | |
| `pieces/clay-cookware-v2.html` | none | ProofEr-only | |
| `pieces/clay-cookware.html` | none | ProofEr-only | |
| `pieces/holocaust-by-country.html` | none | ProofEr-only | |
| `pieces/knife-country.html` | none | ProofEr-only | |
| `pieces/nazi-victims-all-groups.html` | none | ProofEr-only | |
| `pieces/pomewawa.html` | none | ProofEr-only | |
| `pieces/sicilian-folk-magic-rebuild.html` | none | ProofEr-only | |
| `pieces/sicilian-folk-magic.html` | none | ProofEr-only | |
| `pieces/terezin-vedem.html` | none | ProofEr-only | |
| `proj/` | `proj/` | name collision with a different meaning | Sourced-piece workspaces and research versus screen-piece workspaces. Each keeps its own slugs. |
| `proj/clay-cookware/` | none | ProofEr-only | |
| `proj/clay-cookware/.inspected_pngs.json` | none | ProofEr-only | |
| `proj/clay-cookware/.offline_checked.json` | none | ProofEr-only | |
| `proj/clay-cookware/STATUS.md` | none | ProofEr-only | |
| `proj/clay-cookware/access.jsonl` | none | ProofEr-only | |
| `proj/clay-cookware/brief.md` | none | ProofEr-only | |
| `proj/clay-cookware/figures.md` | none | ProofEr-only | Checked figures table. |
| `proj/clay-cookware/layout.md` | none | ProofEr-only | |
| `proj/clay-cookware/qa/` | none | ProofEr-only | |
| `proj/clay-cookware/qa/desktop.png` | none | ProofEr-only | |
| `proj/clay-cookware/qa/phone.png` | none | ProofEr-only | |
| `proj/clay-cookware/qa/v2-desktop-names.png` | none | ProofEr-only | |
| `proj/clay-cookware/qa/v2-desktop.png` | none | ProofEr-only | |
| `proj/clay-cookware/qa/v2-phone-names.png` | none | ProofEr-only | |
| `proj/clay-cookware/qa/v2-phone.png` | none | ProofEr-only | |
| `proj/clay-cookware/research/` | none | ProofEr-only | Sourced-piece research. |
| `proj/clay-cookware/research/.subagent_receipts.jsonl` | none | ProofEr-only | |
| `proj/clay-cookware/research/prompts.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/prompts.md` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/gap_fill/` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/gap_fill/induction-diffusers-and-lachamba-care.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/gap_fill/magnifique-vitaclay-specs.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/gap_fill/romertopf-temp-and-water.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/gap_fill/zisha-cte-and-vitrification.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/pass1/` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/pass1/browning-surface-flavor.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/pass1/multicooker-inserts.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/pass1/porosity-water-loss.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/pass1/stovetop-la-chamba-glaze-safety.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/pass1/thermal-physics.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/pass1/thermal-shock.json` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/pass2_primer/` | none | ProofEr-only | |
| `proj/clay-cookware/research/workers/pass2_primer/clay-types-primer.json` | none | ProofEr-only | |
| `proj/clay-cookware/stills/` | none | ProofEr-only | |
| `proj/clay-cookware/stills/critique.md` | none | ProofEr-only | |
| `proj/clay-cookware/stills/still-01-hero-and-primer.html` | none | ProofEr-only | |
| `proj/clay-cookware/stills/still-01-hero-and-primer.png` | none | ProofEr-only | |
| `proj/clay-cookware/stills/still-02-charts-and-stovetop.html` | none | ProofEr-only | |
| `proj/clay-cookware/stills/still-02-charts-and-stovetop.png` | none | ProofEr-only | |
| `proj/clay-cookware/stills/still-03-phone-and-benchmark.html` | none | ProofEr-only | |
| `proj/clay-cookware/stills/still-03-phone-and-benchmark.png` | none | ProofEr-only | |
| `proj/clay-cookware/v2/` | none | ProofEr-only | |
| `proj/clay-cookware/v2/build.py` | none | ProofEr-only | |
| `proj/clay-cookware/v2/src/` | none | ProofEr-only | |
| `proj/clay-cookware/v2/src/page.css` | none | ProofEr-only | |
| `proj/clay-cookware/v2/src/page.html` | none | ProofEr-only | |
| `proj/clay-cookware/v2/src/page.js` | none | ProofEr-only | |
| `proj/conditionally-white/` | none | ProofEr-only | |
| `proj/conditionally-white/.inspected_pngs.json` | none | ProofEr-only | |
| `proj/conditionally-white/.review_receipts.jsonl` | none | ProofEr-only | |
| `proj/conditionally-white/STATUS.md` | none | ProofEr-only | |
| `proj/conditionally-white/brief.md` | none | ProofEr-only | |
| `proj/conditionally-white/figures.md` | none | ProofEr-only | Checked figures table. |
| `proj/conditionally-white/img/` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/bacons-rebellion-engraving.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/beddoe-headbreadth-diagram-1885.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/beddoe-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/beddoe-races-of-britain-map-1885.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/biden-ballina-2023.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/castle-hill-1804-watercolour.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/census-1851-satisfactory-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/cesaire-photo.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/constable-iberian-negro-1899.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/convict-ship-or-hulk.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/devon-digest-table-95.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/douglass-daguerreotype-c1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/douglass-narrative-frontispiece-1845.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/down-survey-barony-map.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/draft-riots-lynching-clarkson-1863.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/draft-riots-orphan-asylum-1863.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/eureka-flag.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/famine-emigrant-ship-departure-cork.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/faneuil-hall-1840s.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/fanon-photo.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/garrison-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/hening-1705-act-page-p81-title.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/hening-1705-act-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/henry-doyle-emigrants-1868.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/iln-ejectment-1848.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/iln-emigrants-between-decks-1851.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/iln-food-riots-1846.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/iln-searching-for-potatoes-1849.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/kelly-jerilderie-letter-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/lambing-flat-roll-up-banner.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/liberator-masthead-1842.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/macdonald-discovery-of-blight-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/mahony-boy-and-girl-cahera-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/mahony-funeral-skibbereen-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/mahony-mullins-hut-scull-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/mahony-woman-begging-clonakilty-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/mitchel-jail-journal-title.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/mitchel-last-conquest-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/mitchel-photograph.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/nast-day-we-celebrate-1867.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/nicholson-annals-widow-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/nicholson-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/nina-newspaper-ad.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/northern-star-1846-01-03-curry-crop.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/northern-star-1846-01-03.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/nott-gliddon-types-of-mankind-1854.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/oconnell-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/puck-king-of-a-shantee-1882.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/punch-fenian-pest-1866.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/punch-irish-frankenstein-1882.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/punch-irish-tempest-1870.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/punch-missing-link-1862-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/punch-norfolk-curry-1845.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/punch-two-forces-1881.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/reagan-ballyporeen-1984.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/sheet-music-no-irish-need-apply-1862.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/spenser-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/spenser-view-1633-title.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/trevelyan-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/ulster-plantation-map-1609.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/vandeleur-eviction-battering-ram-1888.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/wells-contrasted-faces-1866.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/full/young-ireland-1848-or-mitchel-trial.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/rights.md` | none | ProofEr-only | |
| `proj/conditionally-white/img/sizes.json` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/bacons-rebellion-engraving.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/beddoe-headbreadth-diagram-1885.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/beddoe-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/beddoe-races-of-britain-map-1885.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/biden-ballina-2023.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/castle-hill-1804-watercolour.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/census-1851-satisfactory-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/cesaire-photo.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/constable-iberian-negro-1899.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/convict-ship-or-hulk.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/devon-digest-table-95.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/douglass-daguerreotype-c1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/douglass-narrative-frontispiece-1845.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/down-survey-barony-map.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/draft-riots-lynching-clarkson-1863.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/draft-riots-orphan-asylum-1863.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/eureka-flag.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/famine-emigrant-ship-departure-cork.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/faneuil-hall-1840s.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/fanon-photo.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/garrison-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/hening-1705-act-page-p81-title.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/hening-1705-act-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/henry-doyle-emigrants-1868.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/iln-ejectment-1848.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/iln-emigrants-between-decks-1851.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/iln-food-riots-1846.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/iln-searching-for-potatoes-1849.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/kelly-jerilderie-letter-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/lambing-flat-roll-up-banner.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/liberator-masthead-1842.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/macdonald-discovery-of-blight-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/mahony-boy-and-girl-cahera-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/mahony-funeral-skibbereen-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/mahony-mullins-hut-scull-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/mahony-woman-begging-clonakilty-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/mitchel-jail-journal-title.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/mitchel-last-conquest-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/mitchel-photograph.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/nast-day-we-celebrate-1867.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/nicholson-annals-widow-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/nicholson-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/nina-newspaper-ad.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/northern-star-1846-01-03-curry-crop.png` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/northern-star-1846-01-03.png` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/nott-gliddon-types-of-mankind-1854.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/oconnell-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/puck-king-of-a-shantee-1882.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/punch-fenian-pest-1866.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/punch-irish-frankenstein-1882.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/punch-irish-tempest-1870.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/punch-missing-link-1862-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/punch-norfolk-curry-1845.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/punch-two-forces-1881.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/reagan-ballyporeen-1984.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/sheet-music-no-irish-need-apply-1862.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/spenser-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/spenser-view-1633-title.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/trevelyan-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/ulster-plantation-map-1609.png` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/vandeleur-eviction-battering-ram-1888.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/wells-contrasted-faces-1866.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/src/young-ireland-1848-or-mitchel-trial.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/bacons-rebellion-engraving.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/beddoe-headbreadth-diagram-1885.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/beddoe-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/beddoe-races-of-britain-map-1885.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/biden-ballina-2023.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/castle-hill-1804-watercolour.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/census-1851-satisfactory-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/cesaire-photo.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/constable-iberian-negro-1899.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/convict-ship-or-hulk.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/devon-digest-table-95.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/douglass-daguerreotype-c1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/douglass-narrative-frontispiece-1845.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/down-survey-barony-map.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/draft-riots-lynching-clarkson-1863.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/draft-riots-orphan-asylum-1863.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/eureka-flag.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/famine-emigrant-ship-departure-cork.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/faneuil-hall-1840s.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/fanon-photo.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/garrison-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/hening-1705-act-page-p81-title.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/hening-1705-act-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/henry-doyle-emigrants-1868.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/iln-ejectment-1848.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/iln-emigrants-between-decks-1851.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/iln-food-riots-1846.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/iln-searching-for-potatoes-1849.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/kelly-jerilderie-letter-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/lambing-flat-roll-up-banner.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/liberator-masthead-1842.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/macdonald-discovery-of-blight-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/mahony-boy-and-girl-cahera-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/mahony-funeral-skibbereen-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/mahony-mullins-hut-scull-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/mahony-woman-begging-clonakilty-1847.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/mitchel-jail-journal-title.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/mitchel-last-conquest-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/mitchel-photograph.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/nast-day-we-celebrate-1867.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/nicholson-annals-widow-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/nicholson-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/nina-newspaper-ad.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/northern-star-1846-01-03-curry-crop.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/northern-star-1846-01-03.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/nott-gliddon-types-of-mankind-1854.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/oconnell-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/puck-king-of-a-shantee-1882.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/punch-fenian-pest-1866.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/punch-irish-frankenstein-1882.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/punch-irish-tempest-1870.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/punch-missing-link-1862-page.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/punch-norfolk-curry-1845.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/punch-two-forces-1881.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/reagan-ballyporeen-1984.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/sheet-music-no-irish-need-apply-1862.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/spenser-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/spenser-view-1633-title.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/trevelyan-portrait.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/ulster-plantation-map-1609.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/vandeleur-eviction-battering-ram-1888.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/wells-contrasted-faces-1866.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/img/thumb/young-ireland-1848-or-mitchel-trial.jpg` | none | ProofEr-only | |
| `proj/conditionally-white/layout.md` | none | ProofEr-only | |
| `proj/conditionally-white/outline.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/` | none | ProofEr-only | Sourced-piece research. |
| `proj/conditionally-white/research/.subagent_receipts.jsonl` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/gap-q01-trevelyan.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/gap-q02-press.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/gap-q03-ministers-officials.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/gap-q05-q06-devon-exports.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/gap-q08-q13-historians-mitchel.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/gap-q09-q16c-oconnell-douglass-scotland.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/gap-q11-q12-australia.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/gap-q14-reagan-biden.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q01-trevelyan.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q02-press.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q03a-ministers.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q03b-officials.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q04-flagged-census.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q05-devon-mitchel-text.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q06-exports.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q07-land.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q08-genocide-mortality.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q09-whiteness.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q10-nina-draft-riots.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q11-transportation.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q12-australia.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q13-mitchel.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q14-memory-ballina.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q14b-biden-record.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q14r-reagan-record.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q15-spenser.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q16a-enclosure.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q16bcd-hickel-scotland-haafner.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/q17a-nicholson-anchors.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r2-devon-exports-oconnell-douglass.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r2-malthus-clarendon-nangle.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r2-press.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r2-reagan-biden-clan.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r2-scotland-australia.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r2-trevelyan-wood.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r3-australia-oconnell-mitchel.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r3-devon-exports.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r3-press-scotland.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r3-transportation.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r3-trevelyan-wood-clarendon.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r4-australia.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r4-clarendon-nangle-jowett.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r4-exports-devon.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r4-press-oconnell.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r4-scotland.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r4-trevelyan-wood.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r5-australia.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r5-exports.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r5-nangle-press.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r5-trevelyan-clarendon.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r6-notebooklm.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r7-notebooklm.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/fact-sheets/r8-notebooklm.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/image-hunt.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/master-fact-sheet.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/original-prompts.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/prompts.md` | none | ProofEr-only | |
| `proj/conditionally-white/research/quote-verification.md` | none | ProofEr-only | |
| `proj/conditionally-white/scripts/` | none | ProofEr-only | |
| `proj/conditionally-white/scripts/make_image_tiers.py` | none | ProofEr-only | |
| `proj/conditionally-white/sources/` | none | ProofEr-only | |
| `proj/conditionally-white/sources/primary-source-pack.md` | none | ProofEr-only | |
| `proj/conditionally-white/stills/` | none | ProofEr-only | |
| `proj/conditionally-white/stills/desktop-ch1.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/desktop-ch2.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/desktop-ch4.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/desktop-ch6.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/desktop-cw-100pct.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/desktop-low.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/desktop-mid.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/desktop-top.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/desktop-tx-open.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/mockup.html` | none | ProofEr-only | |
| `proj/conditionally-white/stills/phone-cw-100pct.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/phone-mid.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/phone-top.png` | none | ProofEr-only | |
| `proj/conditionally-white/stills/review.md` | none | ProofEr-only | |
| `proj/disaster-artist/` | none | ProofEr-only | |
| `proj/disaster-artist/.inspected_pngs.json` | none | ProofEr-only | |
| `proj/disaster-artist/STATUS.md` | none | ProofEr-only | |
| `proj/disaster-artist/access.jsonl` | none | ProofEr-only | |
| `proj/disaster-artist/brief.md` | none | ProofEr-only | |
| `proj/disaster-artist/data/` | none | ProofEr-only | |
| `proj/disaster-artist/data/chart-data.json` | none | ProofEr-only | |
| `proj/disaster-artist/figures.md` | none | ProofEr-only | Checked figures table. |
| `proj/disaster-artist/img/` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/arles-petition.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/dr-felix-rey.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/gauguin-christ-garden-of-olives.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/gauguin-les-miserables.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/gauguins-chair.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/hiroshige-plum-park-kameido.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/irises.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/japonaiserie-flowering-plum-tree.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/johanna-and-vincent-willem.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/pere-tanguy.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/portrait-dr-gachet-orsay.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/potato-eaters.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/red-vineyard.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/rey-ear-sketch.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/self-portrait-bandaged-ear.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/self-portrait-dedicated-to-gauguin.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/starry-night.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/sunflowers-national-gallery.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/van-goghs-chair.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/full/yellow-house.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/rights.md` | none | ProofEr-only | |
| `proj/disaster-artist/img/sizes.json` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/arles-petition.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/dr-felix-rey.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/gauguin-christ-garden-of-olives.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/gauguin-les-miserables.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/gauguins-chair.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/hiroshige-plum-park-kameido.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/irises.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/japonaiserie-flowering-plum-tree.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/johanna-and-vincent-willem.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/pere-tanguy.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/portrait-dr-gachet-orsay.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/potato-eaters.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/red-vineyard.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/rey-ear-sketch.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/self-portrait-bandaged-ear.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/self-portrait-dedicated-to-gauguin.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/starry-night.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/sunflowers-national-gallery.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/van-goghs-chair.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/src/yellow-house.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/swatches.json` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/arles-petition.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/dr-felix-rey.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/gauguin-christ-garden-of-olives.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/gauguin-les-miserables.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/gauguins-chair.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/hiroshige-plum-park-kameido.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/irises.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/japonaiserie-flowering-plum-tree.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/johanna-and-vincent-willem.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/pere-tanguy.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/portrait-dr-gachet-orsay.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/potato-eaters.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/red-vineyard.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/rey-ear-sketch.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/self-portrait-bandaged-ear.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/self-portrait-dedicated-to-gauguin.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/starry-night.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/sunflowers-national-gallery.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/van-goghs-chair.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/img/thumb/yellow-house.jpg` | none | ProofEr-only | |
| `proj/disaster-artist/layout.md` | none | ProofEr-only | |
| `proj/disaster-artist/outline.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/` | none | ProofEr-only | Sourced-piece research. |
| `proj/disaster-artist/research/gemini-prompts.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/image-hunt.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/prompts.json` | none | ProofEr-only | |
| `proj/disaster-artist/research/prompts.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/round2/` | none | ProofEr-only | |
| `proj/disaster-artist/research/round2/README.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/round2/gauguin.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/round2/johanna.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/round2/rey-chicken-coop.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/round2/three-claims.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/stipend-model.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/workers/` | none | ProofEr-only | |
| `proj/disaster-artist/research/workers/pass1/` | none | ProofEr-only | |
| `proj/disaster-artist/research/workers/pass1/g1-counts.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/workers/pass1/g2-money.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/workers/pass1/g3-arles.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/workers/pass1/g4-afterlife.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/workers/pass1/g5-life.md` | none | ProofEr-only | |
| `proj/disaster-artist/research/workers/pass2/` | none | ProofEr-only | |
| `proj/disaster-artist/research/workers/pass2/gap-fill.md` | none | ProofEr-only | |
| `proj/disaster-artist/scripts/` | none | ProofEr-only | |
| `proj/disaster-artist/scripts/extract_swatches.py` | none | ProofEr-only | |
| `proj/disaster-artist/scripts/make_image_tiers.py` | none | ProofEr-only | |
| `proj/disaster-artist/stills/` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-ch1.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-ch2.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-ch3.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-ch4-swatches.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-ch4.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-ch6.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-low.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-top.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-vg-100pct.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/desktop-vg-lightbox.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/mockup.html` | none | ProofEr-only | |
| `proj/disaster-artist/stills/phone-mid.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/phone-top.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/phone-vg-100pct.png` | none | ProofEr-only | |
| `proj/disaster-artist/stills/review.md` | none | ProofEr-only | |
| `proj/knife-country/` | none | ProofEr-only | |
| `proj/knife-country/.offline_checked.json` | none | ProofEr-only | |
| `proj/knife-country/QA.md` | none | ProofEr-only | |
| `proj/knife-country/STATUS.md` | none | ProofEr-only | |
| `proj/knife-country/brief.md` | none | ProofEr-only | |
| `proj/knife-country/build.py` | none | ProofEr-only | |
| `proj/knife-country/concepts.md` | none | ProofEr-only | |
| `proj/knife-country/eomd-access.jsonl` | none | ProofEr-only | |
| `proj/knife-country/figures.md` | none | ProofEr-only | Checked figures table. |
| `proj/knife-country/fonts/` | none | ProofEr-only | |
| `proj/knife-country/fonts/OFL-Archivo.txt` | none | ProofEr-only | |
| `proj/knife-country/fonts/OFL-NotoSerifSC.txt` | none | ProofEr-only | |
| `proj/knife-country/fonts/OFL-SourceSerif4.txt` | none | ProofEr-only | |
| `proj/knife-country/knife-country.html` | none | ProofEr-only | |
| `proj/knife-country/research-notes.md` | none | ProofEr-only | |
| `proj/knife-country/research/` | none | ProofEr-only | Sourced-piece research. |
| `proj/knife-country/research/prompts.md` | none | ProofEr-only | |
| `proj/knife-country/research/q1-yangjiang-origins-to-1990.md` | none | ProofEr-only | |
| `proj/knife-country/research/q2-germany-japan-india-china.md` | none | ProofEr-only | |
| `proj/knife-country/research/q3a-yangjiang-1990-2026-claude.md` | none | ProofEr-only | |
| `proj/knife-country/research/q3b-yangjiang-1990-2026.md` | none | ProofEr-only | |
| `proj/knife-country/research/q4-knife-primer.md` | none | ProofEr-only | |
| `proj/knife-country/research/q5a-gaps.md` | none | ProofEr-only | |
| `proj/knife-country/research/q5b-gaps.md` | none | ProofEr-only | |
| `proj/knife-country/src/` | none | ProofEr-only | |
| `proj/knife-country/src/page.css` | none | ProofEr-only | |
| `proj/knife-country/src/page.html` | none | ProofEr-only | |
| `proj/knife-country/src/page.js` | none | ProofEr-only | |
| `proj/knife-country/src/sources.json` | none | ProofEr-only | |
| `proj/knife-country/stills/` | none | ProofEr-only | |
| `proj/knife-country/stills/render.js` | none | ProofEr-only | |
| `proj/knife-country/stills/still1-phone-open.html` | none | ProofEr-only | |
| `proj/knife-country/stills/still1-phone-open.png` | none | ProofEr-only | |
| `proj/knife-country/stills/still2-laptop-japan.html` | none | ProofEr-only | |
| `proj/knife-country/stills/still2-laptop-japan.png` | none | ProofEr-only | |
| `proj/knife-country/stills/still3-phone-plate.html` | none | ProofEr-only | |
| `proj/knife-country/stills/still3-phone-plate.png` | none | ProofEr-only | |
| `proj/knife-country/storyboard.md` | none | ProofEr-only | |
| `proj/pomewawa/` | none | ProofEr-only | |
| `proj/pomewawa/.inspected_pngs.json` | none | ProofEr-only | |
| `proj/pomewawa/.offline_checked.json` | none | ProofEr-only | |
| `proj/pomewawa/STATUS.md` | none | ProofEr-only | |
| `proj/pomewawa/access.jsonl` | none | ProofEr-only | |
| `proj/pomewawa/brief.md` | none | ProofEr-only | |
| `proj/pomewawa/choices-concept-2.html` | none | ProofEr-only | |
| `proj/pomewawa/choices-concept.html` | none | ProofEr-only | |
| `proj/pomewawa/concepts/` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-A.png` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-A.svg` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-B.png` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-B.svg` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-B2a.png` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-B2a.svg` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-B2b.png` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-B2b.svg` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-C.png` | none | ProofEr-only | |
| `proj/pomewawa/concepts/concept-C.svg` | none | ProofEr-only | |
| `proj/pomewawa/concepts/stills.py` | none | ProofEr-only | |
| `proj/pomewawa/concepts/stills2.py` | none | ProofEr-only | |
| `proj/pomewawa/figures.md` | none | ProofEr-only | Checked figures table. |
| `proj/pomewawa/images/` | none | ProofEr-only | |
| `proj/pomewawa/images/cugat-cavalcade.webp` | none | ProofEr-only | |
| `proj/pomewawa/images/pomewawa.webp` | none | ProofEr-only | |
| `proj/pomewawa/images/victoria-pomeranian.webp` | none | ProofEr-only | |
| `proj/pomewawa/layout.md` | none | ProofEr-only | |
| `proj/pomewawa/pomewawa.html` | none | ProofEr-only | |
| `proj/pomewawa/research/` | none | ProofEr-only | Sourced-piece research. |
| `proj/pomewawa/research/chatgpt-AB.md` | none | ProofEr-only | |
| `proj/pomewawa/research/gemini-A-v1.md` | none | ProofEr-only | |
| `proj/pomewawa/research/gemini-A-v2.md` | none | ProofEr-only | |
| `proj/pomewawa/research/gemini-B-v1.md` | none | ProofEr-only | |
| `proj/pomewawa/research/gemini-B-v2.md` | none | ProofEr-only | |
| `proj/pomewawa/research/gemini-C.md` | none | ProofEr-only | |
| `proj/pomewawa/research/prompts.md` | none | ProofEr-only | |
| `proj/pomewawa/stills/` | none | ProofEr-only | |
| `proj/pomewawa/stills/mock.html` | none | ProofEr-only | |
| `proj/pomewawa/stills/still-1-hero.png` | none | ProofEr-only | |
| `proj/pomewawa/stills/still-2-plates.png` | none | ProofEr-only | |
| `proj/pomewawa/stills/still-3-menu.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/.inspected_pngs.json` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/.offline_checked.json` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/REFINEMENT-PLAN.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/STATUS.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/agatha.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/agathabust.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/albarello.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/angel1.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/benedict.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/bust.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/demartino.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/exvoto.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/float.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/frame.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/goddess.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/gramsci.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/isis.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/joseph.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/lettera.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/lucy.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/pitre.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/rosalia.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/steri.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/cut/tile.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/01-rosalia-vandyck.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/02-houel-car-rosalia.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/03-agatha-bronze-back.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/03-agatha-bronze.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/04-bust-34.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/04-bust-back.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/04-bust-front.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/04-bust-side.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/05-lucy-zurbaran.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/06-joseph-back.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/06-joseph.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/07-goddesses-back1.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/07-goddesses-back2.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/07-goddesses-front.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/07-goddesses-side.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/08-isis-front.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/08-isis-side.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/09-albarello-back.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/09-albarello-front.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/10-frame.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/11-exvoto.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/12-angel-1.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/12-angel-2.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/12-angel-3.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/12-angel-4.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/13-gratteri-portrait.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/14-bosch-fish.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/15-guidobono-sorceress.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/16-benedict-moor.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/17-steri-inquisition.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/18-pitre.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/19-gramsci.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/20-demartino.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/Busto_di_Sant'Agata.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/Messina-Letter-plate_Quingles-Aglioti_1740_pp168-169.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/Reliquia_del_Sacro_Capello_di_Palmi_-_002.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/The_relics_of_Santa_Lucia,_Chiesa_di_San_Geremia,_Venice_(37060531904).jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/Tomb_of_Louis_IX_of_France_-_Cathedral_of_Monreale_-_Italy_2015_(2).jpeg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/Urna_Santa_Rosalia_PA_14_07_2019_01.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/originals/Virgin-to-Messina-1674-78_Bibliotheca_Fictiva_nr._8699204.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/crowley.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/demartino.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/etteilla.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/gebelin.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/gramsci.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/papus.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/pitre.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/smith.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/art/portraits/waite.jpg` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/brief.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/build/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/build/build_piece.py` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/build/make_cutouts.py` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/build/make_mockup.py` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/build/make_tile.py` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/build/template.html` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/choices-hero.html` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/copy.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/drafts/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/drafts/part1-opening.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/drafts/part2-acts1-4.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/drafts/part3-acts5-6.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/drafts/part4-acts7-8-end.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/figures.md` | none | ProofEr-only | Checked figures table. |
| `proj/sicilian-folk-magic/image-shortlist.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/layout.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/desktop-act1-boat.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/desktop-act6a-steri.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/desktop-act7-check-and-cab.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/desktop-act7-relics.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/desktop-act8-benedict.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/desktop-act8-route-and-cab.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/desktop-hero-overture.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/desktop-tarot-callout.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/phone-cabpop.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/phone-gloss-closed-after-scroll.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/phone-hero.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/rebuild-desktop.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/rebuild-phone.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/qa/tablet-act2.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/` | none | ProofEr-only | Sourced-piece research. |
| `proj/sicilian-folk-magic/research/.subagent_receipts.jsonl` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/A-pass1.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/A-pass2.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/B-pass1.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/B-pass2.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/C-pass1.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/C-pass2.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/D-pass1.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/D-pass2.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/E-pass1.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/E-pass2.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/F-images.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/G1-gapfill.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/G2-gapfill.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/G3-factcheck.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/H-revision-reads.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/I-art-candidates.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/I-context-gaps.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/NOTES.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/prompts.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/xcheck/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/xcheck/X1.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/xcheck/X2.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/research/xcheck/X3.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/stills/` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/stills/bryan-screenshot-1.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/stills/bryan-screenshot-2.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/stills/critique.md` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/stills/hero-phone.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/stills/qa-stage-fix-rosalia.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/stills/qa-stage-phone.png` | none | ProofEr-only | |
| `proj/sicilian-folk-magic/stills/stills.html` | none | ProofEr-only | |
| `proj/terezin-vedem/` | none | ProofEr-only | |
| `proj/terezin-vedem/.inspected_pngs.json` | none | ProofEr-only | |
| `proj/terezin-vedem/.offline_checked.json` | none | ProofEr-only | |
| `proj/terezin-vedem/STATUS.md` | none | ProofEr-only | |
| `proj/terezin-vedem/brief.md` | none | ProofEr-only | |
| `proj/terezin-vedem/figures.md` | none | ProofEr-only | Checked figures table. |
| `proj/terezin-vedem/layout.md` | none | ProofEr-only | |
| `proj/terezin-vedem/qa/` | none | ProofEr-only | |
| `proj/terezin-vedem/qa/desktop.png` | none | ProofEr-only | |
| `proj/terezin-vedem/qa/family-camp-chart-print.png` | none | ProofEr-only | |
| `proj/terezin-vedem/qa/family-camp-chart.png` | none | ProofEr-only | |
| `proj/terezin-vedem/qa/interactive-sheet.png` | none | ProofEr-only | |
| `proj/terezin-vedem/qa/phone.png` | none | ProofEr-only | |
| `proj/terezin-vedem/qa/print.png` | none | ProofEr-only | |
| `proj/terezin-vedem/research/` | none | ProofEr-only | Sourced-piece research. |
| `proj/terezin-vedem/research/.subagent_receipts.jsonl` | none | ProofEr-only | |
| `proj/terezin-vedem/research/gap_fill_prompts.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/prompts.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/prompts.md` | none | ProofEr-only | |
| `proj/terezin-vedem/research/report-a-family-camp.md` | none | ProofEr-only | |
| `proj/terezin-vedem/research/report-b-family-camp.md` | none | ProofEr-only | |
| `proj/terezin-vedem/research/report-c-family-camp.txt` | none | ProofEr-only | |
| `proj/terezin-vedem/research/report-d-family-camp.md` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/gap_fill/` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/gap_fill/gap_fill_digest.md` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/gap_fill/p2_gap_butterfly_vedem.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/gap_fill/p2_gap_demographics_urls.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/gap_fill/p2_gap_pd_photos.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/gap_fill/p2_gap_redcross_rossel.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/pass1/` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/pass1/p1_terezin_demographics.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/pass1/p2_redcross_and_film.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/pass1/p3_butterfly_and_friedmann.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/pass1/p4_vedem_l417.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/pass1/p5_licensed_photos_and_archives.json` | none | ProofEr-only | |
| `proj/terezin-vedem/research/workers/pass1/pass1_digest.md` | none | ProofEr-only | |
| `proj/terezin-vedem/stills/` | none | ProofEr-only | |
| `proj/terezin-vedem/stills/critique.md` | none | ProofEr-only | |
| `proj/terezin-vedem/stills/still-01-hero-and-crowding.html` | none | ProofEr-only | |
| `proj/terezin-vedem/stills/still-01-hero-and-crowding.png` | none | ProofEr-only | |
| `proj/terezin-vedem/stills/still-01-phone.png` | none | ProofEr-only | |
| `proj/terezin-vedem/stills/still-02-redcross-facade.html` | none | ProofEr-only | |
| `proj/terezin-vedem/stills/still-02-redcross-facade.png` | none | ProofEr-only | |
| `proj/terezin-vedem/stills/still-03-butterfly-vedem.html` | none | ProofEr-only | |
| `proj/terezin-vedem/stills/still-03-butterfly-vedem.png` | none | ProofEr-only | |
| `tools/` | `tools/` | name collision with a different meaning | Sourced publication and validation tooling versus engine build, audio and render tooling. |
| `tools/CLAUDE.md` | `tools/CLAUDE.md` | same purpose, same name | Thonny-friendly tool index. Tools differ by repo. |
| `tools/add_view_counter.py` | none | ProofEr-only | Adds ProofEr’s publication view counter. |
| `tools/check_drift.py` | none | ProofEr-only | ProofEr-side sister-repo comparison. |
| `tools/check_offline.py` | none | ProofEr-only | Offline publication and view-counter validation. |
| `tools/check_stage_reads.py` | `tools/check_stage_reads.py` | same purpose, same name | Same stage-read audit. Restricted paths and stage expectations follow each workflow. |
| `tools/check_vendor.py` | none | ProofEr-only | ProofEr-side kit integrity check. |
| `tools/embed_fonts.py` | none | ProofEr-only | Inline fonts into the standalone essay HTML. |
| `tools/eval_new_piece.py` | `tools/eval_new_piece.py` | same purpose, same name | Same interview eval. Prompt, budget and expected reads follow each workflow. |
| `tools/sync_eomd_kit.py` | none | ProofEr-only | One-way install of the released MIT kit. |
| `vendor/` | none | ProofEr-only | Reserved for vendored dependencies. |
| `vendor/eomd-kit/` | none | ProofEr-only | Reserved for future MIT kit imports from kit/ once EOMD publishes it. |
