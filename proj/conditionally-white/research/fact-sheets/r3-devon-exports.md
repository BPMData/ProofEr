# Round 3: Devon *Digest* Table 95 pages and digits (F37/M3), the commissioners (F38), exports (F43)

Round-3 worker, 2026-11-24. Earlier sheets: `q05-devon-mitchel-text.md`, `q06-exports.md`,
`gap-q05-q06-devon-exports.md`, `r2-devon-exports-oconnell-douglass.md`.

**Access this round:** `curl` to archive.org is still refused by the proxy (CONNECT 403). The page-image URL
(`archive.org/download/digestevidencet01kenngoog/page/n580.jpg`) failed in WebFetch ("error while fetching"), and the
`_djvu.txt` stream still serves only 109,023 characters, so the `offset` parameter can't reach p. 564. **No page image
was seen.** Every *Digest* finding below comes from Internet Archive's full-text search inside the book
(`ia601505.us.archive.org/fulltext/inside.php?item_id=digestevidencet01kenngoog&…&q=…`). That search returns each
hit's scan page and its box position on the page. A hit that is only a number in a box near the top of the page
(t ≈ 160–240 of ~4,790) is that page's **printed running head**. That is how the printed page numbers were pinned
down this round. About 24 fetches used; I stopped there for the shared limit.

## Results

| ID | Claimed | What the source actually says (exact wording read) | Source, page, date | Status | Note |
|---|---|---|---|---|---|
| F37 (pages) | R2 inferred: removal sentence on ~p. 397; Table 95 on p. 564; its conclusion ~p. 565; Canada passage ~p. 568 (scan + 16) | Running heads found by OCR: scan 410 = "396" (head garbled "BTCE OF TAKMBi"); scan 411 = "397" ("6I2S OF PARtfd"); scan 414 = "400" ("S12E OF FABM8", i.e. SIZE OF FARMS); scan 580 = "564" (number alone); scan 582 = "566" ("WA8TB LANDS", i.e. WASTE LANDS). | Kennedy (ed.), *Digest*, Part I (Dublin: Thom, 1847), IA `digestevidencet01kenngoog` | **VERIFIED (running heads, OCR)** for 396, 397, 400, 564, 566 | **Correction: the offset is not a steady +16.** Around scans 410–414 it is +14; by scan 580 it is +16 (two unnumbered leaves, probably plates or folding tables, fall between pp. 400 and 564). So: **the "192,368 families" sentence and the "320,084 occupiers" sentence (scan 413) are on printed p. 399, not p. 397.** Scans 411 = 397 and 414 = 400 leave 412 = 398 and 413 = 399 with no room for a plate. The 135,314 sentence (scan 410) is on **p. 396**, not 394. **Table 95 is on p. 564 (VERIFIED).** Its conclusion (scan 581) is on **p. 565 (VERIFIED: it sits between 564 and 566).** The Canada passage (scan 584) is **p. 568, PROBABLE**: no running head for 567 or 568 came back from the OCR, so a plate after p. 566 can't be ruled out. The table sits in the "Waste Lands" chapter (running head p. 566). The two p. 399 sentences sit under "Size of Farms". |
| F37 (digits) | "192,368" (one scan read "192,868") | p. 399 (OCR): "would require the removal of about 192.368 families". p. 565 (OCR): "The above table 95 (2) shows that 192,868 families might be permanently provided for upon lots about eight acres in extent". p. 568 (OCR): "supposing that 192,368 of the best labouring families be selected and sent there … a certain loss of £5,771,040 for their removal" | same; pp. 399, 565, 568 | **VERIFIED: 192,368** (by the book's own arithmetic; no page image seen) | **£5,771,040 ÷ 192,368 = exactly £30.0 a family. 192,868 × £30 would be £5,786,040.** So the *Digest*'s own cost figure confirms 192,368, and "192,868" at p. 565 is an OCR misreading of 3 as 8. Two of three OCR reads also give 368. The Mitchel figure (p. 72, "one hundred and ninety-two thousand three hundred and sixty-eight") matches. |
| F37 (what the table is) | "Table 95" | p. 565 calls it "**table 95 (2)**". p. 399 cites "Appendix, No. 95 (see page 564)". p. 396 cites "Appendix, No. 95" for the 135,314 holdings of one acre and under. | same | VERIFIED (wording, OCR) | So "No. 95" is an appendix (the classification of holdings), and the p. 564 grid is its **second part, "95 (2)"**: the Digest's own scale of how far improvable waste land would go. Cite it as "Appendix No. 95 (2), p. 564". |
| F37 (title, columns, acres) | table title; columns incl. "col. e"; Irish or statute acres | **Not read.** Searches for phrases likely to sit in the grid ("Irish acres", "statute measure", "first quality", "acres each") returned no hit on scans 576–580. Only the prose under it (p. 565) matched. The table's OCR is probably too broken to be searched. | — | **UNVERIFIED** | Context only, not a finding: elsewhere the *Digest* writes "Irish acres" whenever it means them (35 hits, e.g. p. 691 for scan 691: "about 3,000,000 of Irish acres of waste land, equal to 5,000,000 of English acres"). But p. 565 speaks of "3,755,000 acres" of waste land, which matches neither figure. Don't print "eight Irish acres" or "≈13 statute acres" from the *Digest* until the grid is seen. Mitchel's own footnote (Irish acres) can be cited as Mitchel's. |
| F38 | The five commissioners: Devon, Ferguson, Hamilton, Redington, Wynne; "composed entirely of landlords" (Mitchel p. 68) | (1) *The Spectator*, 4 Nov 1843, p. 4 ("Ireland"), quoting the Dublin *Monitor*: "The Commission consists of five persons— two Tories and two Whigs, with the Earl of Devon as Chairman," [Devon] "of Tory politics, but, we believe, a just and excellent landlord." A later report there names "Mr. George Alexander Hamilton, M.P., and Mr. Wynne, of Hazlewood, both Tories;" and "Mr. William Tighe, of Woodstock, and Mr. More O'Ferrall, M.P., both Liberals." It adds: "Mr. O'Ferrall had declined to act, principally on account of delicate health; and his substitute had not been named". (2) HC Deb 6 Feb 1844 vol 72 cc326–30: Peel, "The first person he applied to to be a member of the Commission was Mr. More O'Ferrall", and he "had also applied to Sir Patrick Bellew". Wakley: "the Commission was entirely composed of Irish landlords." Sharman Crawford: "there was a general feeling in Ireland of dissatisfaction that the Commission was wholly composed of landlords." (3) HL Deb 1 Mar 1844 vol 73 cc433–4 names only Devon. | *Spectator* archive (4 Nov 1843); Hansard (6 Feb 1844; 1 Mar 1844). *Digest* Part I full-text search for "Redington": no hits. | **Devon, Hamilton, Wynne: PROBABLE** (one contemporary press report of the announced members). **Ferguson, Redington: UNVERIFIED.** The usual five-name list is **not confirmed and may be wrong**: the announced Liberal members were Tighe and More O'Ferrall. **"Composed of landlords": VERIFIED as a contemporary charge** made in the Commons, Feb 1844. | Ferguson and Redington are probably later appointments (O'Ferrall's substitute, and perhaps Tighe's), but that's an inference, not something I read. Print no names beyond the Earl of Devon until the Report's title page or signatures are read (HC 1845 [605] xix; the *Digest* prints the Report at pp. [1103]–1172, in Part II, whose IA search index is nearly empty). **Mitchel's "entirely of landlords" echoes what MPs said in 1844**, so the essay can attribute it to them too. Peel's approach to More O'Ferrall and Bellew (both Catholic gentry, from general knowledge, not read) bears on fairness: he says he had looked for Liberal members. |
| F43 | one verified Irish food-export figure, 1846–47 or 1846–50 (Kinealy, Ó Gráda, Solar or Bourke), read in the text | Not read. `historyireland.com/?p=1228` now opens (R2 was refused) but it shows only the teaser: no byline, no volume, issue or year, and no figures. "Read more" leads to the paywall. | — | **UNVERIFIED (unchanged)** | No exports row for the ledger this round. Budget went to F37 first, per the priority order. |

Status counts this round: **VERIFIED**: F37 printed pages (396, 397, 399, 400, 564, 565, 566), the digits 192,368
(by arithmetic), and "Appendix No. 95 (2)" as the table's name; the "landlords" charge as an 1844 Commons complaint.
**PROBABLE**: p. 568; Devon, Hamilton and Wynne as members. **WRONG**: R2's inferred p. 397 (it's **p. 399**) and
p. 394 (it's **p. 396**). The standard five-name list is unconfirmed: a contemporary report names Tighe and More O'Ferrall
among the first members. **UNVERIFIED**: the table's title and columns, Irish vs statute acres, Ferguson, Redington, F43.

## What changes in the master sheet
- F37: change "~p. 397" to **p. 399** (removal and 320,084 sentences), "~p. 565" to **p. 565**, "~p. 568" to
  **p. 568 (probable)**; call the table **"Appendix No. 95 (2)", p. 564**; 192,368 confirmed by the *Digest*'s own
  £30-a-family arithmetic (£5,771,040). Table title, columns and acre measure still open.
- F38: don't print the five-name list. The 1843 announced membership was Devon (chair), G. A. Hamilton MP, Wynne of
  Hazlewood, William Tighe of Woodstock and More O'Ferrall MP, and O'Ferrall declined. The "all landlords" complaint
  can be cited to Wakley and Sharman Crawford in the Commons on 6 Feb 1844.

## Leads for next pass
1. **Table grid, p. 564 (scan 580):** page images only. Try `https://archive.org/details/digestevidencet01kenngoog/page/n580/mode/1up`
   in a real browser, or the HathiTrust copy of the same Michigan volume (full view, public domain; search HathiTrust for
   "Digest of evidence taken before Her Majesty's commissioners of inquiry" 1847). HathiTrust's page-text view
   (`babel.hathitrust.org/cgi/pt?id=…;seq=…`) can give the single page's OCR. Also check whether scan 567/568 holds a plate.
2. **Commissioners:** the Report's title page or signatures in HC 1845 [605] xix (ProQuest UK Parliamentary Papers; or
   the *Digest* Part II, IA `digestevidencet02kenngoog`, pp. [1103]–1172, page images). The Spectator archive's later
   issues (Nov–Dec 1843) for O'Ferrall's substitute. Hansard HC 12 Feb 1844 vol 72 cc517–8 ("Land Tenure Commission
   (Ireland)") and HL 5 Mar 1844 vol 73 cc570–80, not yet opened, may name members.
3. **F43:** the HI article is paywalled (no byline or issue on the page). Routes: JSTOR's *History Ireland* table of
   contents (vol. 5, 1997) for the citation; Bourke, "The Irish grain trade, 1839–48", *IHS* 20:78 (1976), 156–169
   (Cambridge Core; abstract only so far) for an oats/grain export figure for 1846; Kinealy, *A Death-Dealing Famine*
   (Pluto, 1997), on Everand/Scribd (lead only: search result
   `everand.com/book/315897011/A-Death-Dealing-Famine-The-Great-Hunger-in-Ireland`, needs an account, so not for this
   worker); Ó Gráda, *Black '47 and Beyond* (1999), ch. 4, in a library copy. Ignore usbornefamilytree.com (derivative).

## Sources consulted (opened this round)
- IA full-text search in `digestevidencet01kenngoog`: q = "Irish acres" · 192,368 · 564 · 397 · 399 · 398 · 400 · 396 ·
  568 · 566 · "statute measure" · eight acres · "first quality" · "acres each" · Redington
- `https://archive.org/download/digestevidencet01kenngoog/page/n580.jpg` (fetch error)
- `https://archive.org/stream/digestevidencet01kenngoog/digestevidencet01kenngoog_djvu.txt` at offset 2,800,000 (text is only 109,023 characters)
- *The Spectator*, 4 Nov 1843, p. 4: https://archive.spectator.co.uk/article/4th-november-1843/4/ireland
- HC Deb 6 Feb 1844 vol 72 cc326–30: https://api.parliament.uk/historic-hansard/commons/1844/feb/06/landlord-and-tenant-commission-ireland
- HL Deb 1 Mar 1844 vol 73 cc433–4: https://api.parliament.uk/historic-hansard/lords/1844/mar/01/tenure-of-land-ireland-commission
- Collinge (ed.), *Office-Holders in Modern Britain* vol. 9 (1984), BHO list 1840–49: https://prod.british-history.ac.uk/node/10227 (no Devon Commission entry)
- *History Ireland*, "Food Exports from Ireland 1846-47": https://historyireland.com/?p=1228 (teaser only)
