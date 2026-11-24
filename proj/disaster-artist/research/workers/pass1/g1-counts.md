# G1 counts: Van Gogh paintings, letters, self-portraits, per-period (pass 1)

Method note: only WebFetch/WebSearch were usable. Bash/curl to vangoghletters.org, vangoghmuseum.nl and vggallery.com is blocked by the proxy. vangoghletters.org and many VGM pages render with JavaScript, so their count pages could NOT be opened directly. Letter figures below are therefore traced via two secondary-but-quoting sources (Grant, AU Press 2014; Museo Van Gogh guide quoting vangoghletters.org) plus the TEI project page. Anything not opened is marked.

## 1. Total paintings / drawings

| Source | Figure | Wording / locator | Checked? |
|---|---|---|---|
| Metropolitan Museum, Dept. of European Paintings, "Vincent van Gogh (1853-1890)", Heilbrunn Timeline essay, 2004 rev. 2010, metmuseum.org/essays/vincent-van-gogh-1853-1890 | "nearly 900 paintings and more than 1,100 works on paper" (1880-90) | Opened; number present | yes |
| Van Gogh Museum, gallery text (permanent collection) | "hundreds of paintings and drawings ... in a mere decade (1880-1890)"; VGM owns "around 200 paintings" and 500+ drawings | Opened. VGM gives NO exact total on pages I could open | yes |
| VGM General Factsheet | museum "owns more than 200 paintings, 500 drawings and almost all of his letters" | Opened (holdings only, not lifetime total) | yes |
| Wikipedia, Vincent van Gogh (LEAD ONLY, no inline cite) | "about 2,100 artworks, including around 860 oil paintings" | Lead; commonly attributed to VGM but I could not find the VGM page that says it | lead only |
| Wikipedia, List of works | "more than 2,000 artworks ... around 900 paintings and 1,100 drawings and sketches" | lead only | lead only |
| vggallery.com (private hobby site, follows F/JH numbering) | 861 paintings listed | Home page "861 paintings online"; the six period pages sum to 861 (36+188+8+226+184+143+76 = 861) | yes, but not institutional |
| de la Faille 1970 | NOT SOURCED. Wikipedia (Jacob Baart de la Faille) only says 1928 edition reproduced "plus de 1.600 tableaux, dessins, aquarelles et gravures" (combined). No 1970 count found | | LOW / unsourced |
| Hulsker 1996 | vggallery bibliography: "over 2,185 reproductions"; JH numbers run to about 2,150 across paintings+drawings+sketches in one chronological sequence (highest JH seen in the Auvers list: 2125). No separate painting count found | | LOW |
| Globe and Mail (Van Gogh canon has long history of disputes) | 1928 de la Faille: "roughly 2,200 paintings, sketches and drawings"; Hulsker 1996 doubted 45 paintings | Opened | yes (journalism) |

Reading: oil paintings range "about 860" (Wikipedia lead, vggallery 861) to "nearly 900" (Met). The gap is attributions and whether oil sketches/studies count. Works on paper "more than 1,100" (Met) or "about 1,100" (Wikipedia). I could not get VGM's own exact sentence; the essay should either cite the Met ("nearly 900 paintings, more than 1,100 works on paper") or say "about 860 oil paintings and about 1,100 works on paper" tagged to the catalogue-based lists, and flag VGM wording as unverified.

## 2. Letters (2009 VGM/Huygens ING edition, Jansen, Luijten, Bakker eds.)

Figures traced:
- Total surviving: **903**. TEI page (tei-c.org/activities/projects/vincent-van-gogh-the-letters/, opened): "The 903 letters and 25 related manuscripts were published both online and in a six-volume printed edition."
- Grant, *Reading Vincent van Gogh* (AU Press 2014), Appendix One "Some Facts About the Letters" (opened): "Total number of letters surviving: 903"; "Number written by Van Gogh: 820"; "Number written to Van Gogh: 83". To Theo alone 651 (659 incl. to Theo and Jo jointly or Jo alone). From Theo alone 39 (46 incl. joint or Jo alone).
- Museo Van Gogh guide (museovangogh.org/en/van-gogh-letters/, opened; it attributes to vangoghletters.org "Van Gogh as a letter-writer"): 903 total, 820 by Vincent, 83 received; 651 to Theo, 7 to Theo+Jo, 162 to others; 39 from Theo, 2 from Theo+Jo; estimated lost: at least 550 to him, at least 290 by him.

Disagreements:
- 903 vs **902**: Art Newspaper (2019) and horscadre.paris say 902 "in the annotated edition" (letter numbering runs to 902; the 903 total counts one letter with a doubled number/addition). TEI/Grant say 903. Use 903.
- 83 vs **84** letters to Vincent: Wikipedia cites vangoghletters.org searches as 84 (39 from Theo). Grant and Museo say 83. Because 820 + 83 = 903, use 83. 84 is a likely one-off in a database listing; LOW confidence on why.
- To Theo: 651 alone / 658-659 incl. Jo (Art Newspaper says "658"; horscadre "about 660"; Wikipedia 663 uncited). Use "about 650 to Theo alone (651); 659 with letters to Theo and Jo".
- Theo's letters to Vincent that survive: **39** (46 with Jo's/joint). Few survive because Vincent kept little and moved a lot. Not opened on vangoghletters.org directly (JS), but Grant and Museo agree.
- 844 figure in Wikipedia is internally inconsistent; ignore.

Statement: Van Gogh wrote 820 surviving letters, over 650 of them to Theo; only 83 letters to him survive, 39 from Theo.

## 3. Self-portraits

- VGM collection page (vangoghmuseum.nl/en/collection/s0065V1962, opened): "Vincent van Gogh painted about 35 self-portraits in total, most of them in Paris." (the fetch tool returned this sentence; I could not re-verify wording beyond that.)
- Martin Bailey, Art Fund, "The many faces of Vincent van Gogh" (opened): "Of the 35 surviving painted self-portraits, 18 are at the Van Gogh Museum." Hmm: the tool's quote; treat the 18 as LOW CONFIDENCE (VGM holds fewer by its own listing).
- Met essay: "more than twenty self-portraits" in Paris (1886-88).
- Wikipedia Portraits list: my count 35-37 depending on drawings, etc. (lead only).
Verdict: "about 35" holds (two independent sources: VGM and Bailey). Includes oil self-portraits only.

## 4. Paintings per period / per year

### Period statements from institutions
| Period | Statement | Source |
|---|---|---|
| Paris 1886-88 | "more than 200 paintings during his two years there" (Wikipedia, citing letter 640 note); Met: "more than twenty self-portraits" | Wikipedia (lead-ish, cited to Van Gogh 2009 letters 640) |
| Arles | "completed 200 paintings and more than 100 drawings and watercolours" (Wikipedia citing Pickvance 1984 p.11). I could not confirm "187". vggallery: 184 (Feb 1888-Apr 1889) | Pickvance via Wikipedia; vggallery |
| Saint-Rémy | VGM Hospitalization page meta: "He completed around 150 paintings in one year"; Met: "some 150 canvases". vggallery: 143 (May 1889-May 1890) | VGM page (opened), Met (opened), vggallery |
| Auvers | Wikipedia citing Rosenblum 1975 pp.98-100: "approximately 70 oils, painted during as many days"; Met: "In just over two months, Van Gogh averaged a painting a day"; vggallery: 76 (May-July 1890) | as stated |
| Nuenen 1883-85 | "nearly 200 oil paintings" (Wikipedia citing Tralbaut 1981); vggallery 188 | |

### Computed from vggallery.com period tables (private site using F/JH dating; counts via page tables, entries by the date column; not an institution, MEDIUM-LOW)
Period lists: 1881-83: 36; Nuenen Dec 1883-Nov 1885: 188 (table has 187 rows); Antwerp Dec 1885-Feb 1886: 8; Paris Mar 1886-Feb 1888: 226; Arles Feb 1888-Apr 1889: 184; Saint-Rémy May 1889-May 1890: 143; Auvers May-Jul 1890: 76. Sum 861.

Derived per-year (approximate; a few entries span years or are dated loosely):
| Year | Count | How |
|---|---|---|
| 1881 | 3 | early.htm date column |
| 1882 | 14 | same |
| 1883 | 19 (+0 from Nuenen list) | same |
| 1884 | about 50-56 | 50 solely 1884 + 6 spanning 1884-85 |
| 1885 | about 130-137 (+6-7 Antwerp) | 130 solely 1885 + spanning |
| 1886 | about 103 (Paris, + small Antwerp Jan-Feb 1886) | Paris date column; 8 entries "1886-87" double counted |
| 1887 | about 130 | Paris date column |
| 1888 | about 153 Arles + 1 Paris (Feb) = about 154 | Arles table: 153 in 1888, 1 ambiguous |
| 1889 | about 140 | 30 Arles Jan-Apr + about 110 Saint-Rémy |
| 1890 | about 109 | about 33 Saint-Rémy Jan-May + 76 Auvers |
Sum approx 860. Caveats: dates of many Nuenen, Paris and Antwerp works are uncertain; year totals can shift by several. I could not open the underlying Hulsker/de la Faille catalogues, so this stands on vggallery's dating alone. Treat as LOW-MEDIUM; the essay should say "about" and cite periods, not single years.

### Draft guess check
- 1881: 1 -> adjust: about 3 (vggallery). Etten drawings dominated 1881; oils begin late 1881.
- 1882: 30 -> wrong-ish: about 14 on the list.
- 1883: 80 -> wrong: about 19 (1881-83 total is 36). Nuenen oils begin Dec 1883.
- 1884: 100 -> adjust: about 50-56.
- 1885: 120 -> adjust: about 130-137 (Nuenen peaks, Potato Eaters year).
- 1886: 60 -> wrong: about 103 (Paris from March 1886).
- 1887: 75 -> wrong: about 130.
- 1888: 200 -> wrong for the calendar year: about 154; "200" is the often-quoted whole-Arles figure (Pickvance) while vggallery has 184 for Feb 1888-Apr 1889.
- 1889: 140 -> holds (about 140), by this computation only.
- 1890: 65 -> wrong: about 109 (76 Auvers + about 33 Saint-Rémy Jan-May). Auvers alone ~70 (Rosenblum) to 76.

## 5. Career length and rates
- VGM gallery text: "Decides at the age of 27, to become an artist" (1880); practised drawing in the Borinage 1878-80 (opened). Died 29 July 1890 (VGM page).
- Artist career 1880-July 1890 about 10 years (VGM "a mere decade"). First paintings: vggallery shows 3 in 1881 (late 1881); I did not verify the first oil with a primary source. So painting career about 8.5-9 years (late 1881-July 1890).
- Averages (computed): 860 paintings / about 9 years (about 470 weeks) = about 1.8 per week; if "nearly 900" and 9 years = about 1.9/week; across a 10-year career about 1.65-1.7/week. "About two paintings a week" holds as a loose, slightly generous career average.
- Peak rates: Paris 226 in about 23 months = about 2.3 a week; Arles 184 in about 14.5 months (Feb 1888-Apr 1889) = about 2.9 a week (or 200/65 weeks about 3.1); Saint-Rémy 143-150 in about 12.5 months = about 2.7 a week; Auvers 70-76 in about 70 days = about 7-7.5 a week (about one a day, which matches the Met).

## Summary table
| ID | Claim | Value | Sources | Agreement | Confidence | Verdict on draft |
|---|---|---|---|---|---|---|
| C1 | Total oil paintings | about 860 (to nearly 900) | Wikipedia lead; vggallery 861; Met "nearly 900" | close | medium | not stated in draft; use "about 860" |
| C2 | Works on paper | about 1,100 (more than 1,100) | Met; Wikipedia lead | agree | medium | can't verify VGM wording |
| C3 | de la Faille 1970 / Hulsker totals | not found | n/a | n/a | LOW | can't verify |
| C4 | Surviving letters | 903 (902 numbered) | TEI page; Grant 2014; Museo | agree (902 outlier) | high | holds |
| C5 | Letters by Vincent | 820 | Grant; Museo | agree | high | holds |
| C6 | Letters to Vincent | 83 (84 in one count) | Grant; Museo vs Wikipedia | minor conflict | medium | holds as 83 |
| C7 | Letters to Theo | 651 alone, 659 with Jo | Grant; Museo | agree | medium-high | use "over 650" |
| C8 | Theo's letters surviving | 39 (46 incl. Jo) | Grant; Museo | agree | medium-high | holds |
| C9 | Self-portraits | about 35 | VGM collection page; Bailey (Art Fund) | agree | medium-high | holds |
| C10 | Paris | 200+ (vggallery 226) | Wikipedia/letter 640; vggallery | agree | medium | holds |
| C11 | Arles | 184 to 200 | vggallery; Pickvance via Wikipedia | close | medium | 200 holds as a period figure; "187" not found |
| C12 | Saint-Rémy | about 150 (143) | VGM; Met; vggallery | agree | high | holds |
| C13 | Auvers | about 70 (76) in about 70 days | Rosenblum via Wikipedia; Met; vggallery | close | medium | holds |
| C14 | Per-year 1881-1890 | see section 4 | vggallery only | n/a | LOW | draft numbers mostly wrong or unsourced |
| C15 | Career length | 1880 decision; painting from late 1881; died July 1890 | VGM gallery text; vggallery | | medium | holds |
| C16 | Average painting rate | about 1.7-1.9 per week | computed from C1 | | derived | "nearly two a week" holds |
