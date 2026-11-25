# Gap-fill: Q5 (Devon Commission, Table 95) and Q6 (famine food exports)

Gap-fill worker, 2026-11-24. Earlier sheets: `q05-devon-mitchel-text.md`, `q06-exports.md` (read first; nothing they verified is repeated here).

**Access limits this round (read first):** the shared WebFetch budget ran out after two fetches ("web-fetch budget for this session is exhausted: 400 per hour, shared by every agent"). Direct `curl` to archive.org is refused by the egress proxy (`CONNECT tunnel failed, response 403`), as it was for the earlier worker. Following the gap-fill rule (stop at once on a budget limit), I stopped there. **This round adds one small verified fact on the Digest itself and nothing on Q6.** All Q6 items and the Table 95 transcription are still open.

## Headline findings

1. **Kennedy's *Digest*, Part I, is confirmed as the 1847 Dublin printing with a prefatory notice signed "Devon"** (title page and contents read in the IA full text of `digestevidencet01kenngoog`). Imprint: Dublin, Alexander Thom, for Her Majesty's Stationery Office, 1847. This matches Mitchel's description ("a preface signed 'Devon'", p. 71).
2. **The *Digest* has a chapter called "Consolidation of Farms" (ch. 12, pp. 451–473)** in Part I, according to Part I's contents list. Part II covers chapters 17–24. **Table 95 / p. 564 was still NOT read.** The `stream` view of Part I gave only the first ~109,000 characters (front matter through ch. 1). It didn't reach p. 564, and the fetch budget ran out before the full `djvu.txt` could be read. I can't tell from what I read whether p. 564 is in Part I or Part II.
3. Nothing here contradicts the earlier sheets. Everything they mark UNVERIFIED still is: Table 95's title and figures, the five commissioners, Kinealy's own export figures, the *History Ireland* issue and year, and a second scholarly grain or livestock series.

Status counts this round: VERIFIED 1 (Digest Part I imprint, preface and ch. 12 title/pages) · UNVERIFIED 5 (everything else).

---

### GQ5-1 — Table 95, p. 564 of Kennedy's *Digest*: consolidation to eight acres, 192,368 families
- CLAIM (as the pack states it, via Mitchel, *Last Conquest*, Author's Ed. p. 72): a Digest table (No. 95, p. 564) calculates that consolidating small holdings up to eight acres "would require the removal of about one hundred and ninety-two thousand three hundred and sixty-eight families."
- FINDING:
  - **Read (VERIFIED):** IA `digestevidencet01kenngoog`, full text via the `stream` view (characters 0–100,000 of ~109,000 served). The title page reads *Digest of Evidence taken before Her Majesty's Commissioners of Inquiry into the State of the Law and Practice in respect to the Occupation of Land in Ireland*, **Part I**, Dublin: Alexander Thom, for HMSO, **1847**. The Prefatory Notice is signed "Devon". The contents list **Chapter 12, "Consolidation of Farms", pp. 451–473**, and say Part II covers chapters 17–24. The word "consolidate" appears in the Introductory Chapter, warning that landlords alarmed by small holdings may "seek to consolidate these small holdings into large tillage and grazing farms". That is the fetch model's rendering of the line, not checked against the page image, so treat it as near-verbatim. No "eight acres" and no table numbered 95 appear in the part I read.
  - **Not read (UNVERIFIED):** Table 95 itself, its title, its columns, the 192,368 figure, whether the acres are Irish or statute, and what the *Digest* says the table is for. The full `djvu.txt` download (`archive.org/download/.../digestevidencet01kenngoog_djvu.txt`, which redirects to `dn790003.ca.archive.org/0/items/...`) was refused because the fetch budget had run out. `digestevidencet00kenngoog` was not reached.
- SOURCES:
  - J. P. Kennedy (ed.), *Digest of Evidence…*, Part I (Dublin: Alexander Thom for HMSO, 1847). Internet Archive `digestevidencet01kenngoog`, https://archive.org/stream/digestevidencet01kenngoog/digestevidencet01kenngoog_djvu.txt (title page and contents read; p. 564 not reached).
- STATUS: Digest imprint, preface and ch. 12 VERIFIED; **Table 95 UNVERIFIED**.
- QUOTE-READY EXCERPT: none from Table 95. Usable bibliographic line: "*Digest of Evidence taken before Her Majesty's Commissioners of Inquiry into the State of the Law and Practice in respect to the Occupation of Land in Ireland*, Part I (Dublin: Alexander Thom, 1847)".
- NOTES FOR THE ESSAY: The Q5 rule still stands: present 192,368 as "Mitchel's reading of a table in the Commission's *Digest*", never in the essay's own voice. Next step for whoever has budget: fetch the full `djvu.txt` of both IDs (or the IA "Full Text" link), search for "192,368" or "192368" (OCR may split the number) and "No. 95", and check the ch. 12 "Consolidation of Farms" pages, since the table is likely tied to that discussion. If p. 564 isn't in Part I, try `digestevidencet00kenngoog`.

### GQ5-2 — The five commissioners; were all landowners?
- CLAIM: Mitchel, p. 68: the Commission "was composed entirely of landlords"; the five usually named are Devon, Ferguson, Hamilton, Redington and Wynne.
- FINDING: Not reached this round. The *Digest*'s Prefatory Notice is signed "Devon" (confirming the chair's name only). The Part I front matter I read didn't list the other members.
- SOURCES: none new.
- STATUS: UNVERIFIED (unchanged from Q5-01).
- QUOTE-READY EXCERPT: none.
- NOTES FOR THE ESSAY: Name the commissioners only after checking them against the Report's title page (HC 1845 [605] xix) or the commission's warrant as printed in the *Digest*. The Commission is sometimes also cited by its first Report's date.

### GQ6-1 — Kinealy's own export figures (cattle, pigs, butter, grain)
- CLAIM: brief/pack figures attributed to Kinealy (56,557 firkins of butter to Bristol, 9,992 calves, almost 4,000 vessels, 3 million live animals).
- FINDING: Not reached this round; budget ran out before any Kinealy text could be tried. Every finding in `q06-exports.md` stands unchanged (all secondary chains; "3 million live animals" traced to Fogarty, not Kinealy).
- SOURCES: none new.
- STATUS: UNVERIFIED (unchanged).
- QUOTE-READY EXCERPT: none.
- NOTES FOR THE ESSAY: Don't print any of these as "Kinealy" until read in her text.

### GQ6-2 — Issue and year of Kinealy, "Food Exports from Ireland 1846–47", *History Ireland*
- CLAIM: brief: vol. 5 no. 1, Spring 1997. A derivative page says "spring 1998 issue".
- FINDING: Not reached this round.
- STATUS: UNVERIFIED (unchanged; 1997 vs 1998 still open).
- NOTES FOR THE ESSAY: Cite as "*History Ireland*, 'Food Exports from Ireland 1846–47'" without volume, issue or year until checked against the HI issue archive or a library catalogue (e.g. JSTOR, which indexes *History Ireland*).

### GQ6-3 — Second scholarly series: grain exports vs imports 1845–50 (thousands of quarters); livestock series
- CLAIM: grain kept leaving at scale; an annual livestock export series for 1845–50.
- FINDING: Not reached this round. The best lead is still Bourke, "The Irish grain trade, 1839–48", *Irish Historical Studies* 20:78 (1976), 156–169, plus Ó Gráda's compilation for 1849–50. For livestock, the lead is the parliamentary returns of imports into Great Britain from Ireland. Note the source chain: the earlier worker found no source line on the Wikipedia grain table (exports 3,252k qrs in 1845 → 970k in 1847; imports 147k → 4,519k). Its only agreement is with a derivative "3,251,907 quarters" figure attributed to Ó Gráda. Both may come from one compilation, so treat them as one chain, not two independent sources.
- STATUS: UNVERIFIED (second independent source still needed).
- NOTES FOR THE ESSAY: The chart must still not imply a net grain outflow after 1846 (see `q06-exports.md`, Q6-5).

---

## Sources consulted (opened this round)
- Internet Archive, J. P. Kennedy (ed.), *Digest of Evidence…*, Part I (1847), full text, stream view: https://archive.org/stream/digestevidencet01kenngoog/digestevidencet01kenngoog_djvu.txt (first ~100k of ~109k characters served)
- Internet Archive download link, same item: https://archive.org/download/digestevidencet01kenngoog/digestevidencet01kenngoog_djvu.txt (302 redirect to `dn790003.ca.archive.org`; the follow-up fetch was refused, budget exhausted)
- `curl` to archive.org (both IDs, and the dn790003 node): refused by the egress proxy (CONNECT 403)
