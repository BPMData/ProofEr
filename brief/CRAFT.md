# Craft: from checked figures to an approved layout

Read this once the figures are checked and before the first concept. It's for the model, not the client, and no
tool is in view yet. The interview, template and research steps are `INTERVIEW.md`, `TEMPLATE.md` (craft bar §13,
QA §16) and `RESEARCH.md`.

## 1. From figures to concept
- **One sentence first:** what a reader who gives it five seconds must take away. Every section serves it or goes.
- **Reading context first:** a phone held close, a projector across a room and a printed poster are three
  different pieces. Distance and time decide type size, density and how many numbers fit.
- **Find the visual idea in the subject,** not in a chart library: a unit that makes the number felt (one square =
  10,000 people), a map that carries the "where", a timeline that carries the "when". Test: would it be wrong for any
  other topic? If not, keep looking.
- **A system with variations:** one grid, one type scale, one palette with roles, one way of labeling, used in every
  section; each section varies the content, not the style.
- **The subject's clichés are off the table:** list them (barbed wire for war, red splatter for violence,
  thermometers for climate, gears for industry) and avoid every one.

## 2. Pitching concepts
2–3 directions that differ in idea, each a few lines in everyday words: **the idea** in one sentence; **what they'd
see first**; **how it feels** in three words and what it steers away from; one sketch or still each. Say which you
recommend and why.

**Choice panels:** whenever the client chooses (a concept, a chart form, a palette, a headline), show, don't
describe: one offline page, up to six options in a 3 × 2 grid, each a still or a live sketch, a short label and a
letter to answer with ("B, but calmer"). Template: `.claude/skills/toolbox/choice-panel.html` (open only that file,
not the toolbox).

## 3. Choosing the chart
Pick the form from the question, not the other way round:
- **How many / how big?** A big number in words and digits; a unit chart (squares, dots) when the scale must be felt.
- **Compared with what?** Bars (horizontal when labels are long), sorted unless the order means something.
- **Part of a whole?** A stacked bar or unit chart; a pie only for two or three parts, never in 3D.
- **Over time?** A line for continuous change, columns for counts per period, a timeline for events.
- **Where?** A map only when location is the point; otherwise a sorted list or bars beats a map of blobs.
- **How sure?** Ranges, error bars or "about"; shade estimates differently from counts.
Two or three chart forms per piece at most; ten read as a demo.

## 4. Honesty
- Bars and areas start at zero. A line chart may zoom, with the axis clearly labeled.
- Area and size are proportional to value; never scale an icon in two dimensions for a one-dimensional number.
- Same unit, same scale across sections that will be compared.
- Per capita when sizes differ; absolute numbers when the count is the point; say which.
- No cherry-picked years or baselines; show the context that changes the reading.
- Uncertainty stays visible. False precision ("5,931,956") is shown only when the source really counts that exactly,
  and the note says so.
- The sources section and "About these numbers" are part of the design, not fine print to hide.

## 5. Type and layout
- **Hierarchy at a glance:** one headline (often the key number in words), one level of support, then detail. Two
  type families at most.
- **Direct labels** on the data beat a legend; numbers next to what they count.
- **Reading path:** top to bottom, one column on a phone; nothing important in a corner the eye never reaches.
- **Sizes from the brief:** heavy weights and short lines for a projector or wall; generous line height for reading
  close.
- **Contrast:** WCAG AA at least; stronger for projectors and bright rooms; dark text on light brights.
- **Copy is sacred:** fixed copy word for word; nothing invented to fill a layout.
- **More than one language** when the audience needs it; fit the layout to the longest version.

## 6. Color
- Color carries meaning (a category, a highlight), not decoration. One accent for what matters most.
- Colorblind-safe pairs; never red against green as the only difference.
- Sequential for amounts, diverging only around a meaningful middle, categorical for groups.
- On sensitive subjects, restraint: muted neutrals, one deep accent, no alarm reds unless the brief asks.

## 7. Motion and interaction (only when they help)
- Interaction reveals detail on demand (select a square, a country); the static page must already tell the story.
- Motion builds a number in reading order or shows change over time; never decoration. Respect reduced motion.
- Nothing flashes more than three times a second. It must print and read with scripts off.

## 8. Human subjects
- People are never decoration: no icons of victims as cute figures, no gamified counters, no "fun" transitions.
- Name groups the way the groups and recognized scholarly and memorial institutions name them.
- A number of people is a number of lives: let the scale be felt (units, a moment of white space) without
  sensationalism.

## 9. The layout plan and stills
**The layout plan** lives in `proj/<name>/layout.md` (template: `LAYOUT.md`): one row per section in reading order,
each naming the figures it uses by ID from `figures.md`. Each row must prove: what the reader learns there, what the
eye hits first, which chart and why, and how it connects to the next section.

**Stills** (2–3 mockups at the real size and shape: phone, slide or page) prove the look: type at its real size, the
palette with its roles, the visual idea at its strongest, one dense section. At 25% scale the headline still reads.

## 10. Anti-patterns
- Chart junk: 3D, shadows, gradients and icons that don't carry data.
- Decorative charts: a chart chosen because it looks clever, not because it answers the question.
- Dual axes, truncated bars, area-scaled icons, unlabeled units.
- Wallpaper text: captions laid over unrelated imagery.
- Template feel: a look that could belong to any topic.
- False precision, hidden uncertainty, sources in grey 6-pt type.
- The subject's clichés.

## 11. Self-check before the client sees anything
- Could someone who looked for five seconds say what it's about?
- Is every number on it in `figures.md`, checked, with its source in the sources section?
- Does each chart answer a question from brief §5, and is it honest (baselines, areas, units)?
- Is uncertainty visible where the sources disagree?
- Is the headline readable at 25% scale and at the brief's distance? Does every pair pass contrast?
- Does it work in grayscale, in print and with scripts off?
- Is it free of the subject's clichés and of anything the landmines in brief §4 rule out?
