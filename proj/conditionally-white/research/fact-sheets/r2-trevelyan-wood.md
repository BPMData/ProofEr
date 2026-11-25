# R2: Trevelyan and Wood quotes (B8, B12, B14, B15, B17, B20, T1–T4)

Round-2 worker, 2026-11-24. **Budget note:** the shared WebFetch budget (400 an hour) ran out after about 20 fetches,
and I stopped there as the rules say. `curl` to archive.org is refused by the proxy (CONNECT 403, a policy denial), so
the full-text downloads could not be pulled to disk either.

**Why the end of *The Irish Crisis* is still unread:** the fetch tool stops reading every copy of the book at about
120–130k characters:
- Gutenberg HTML reaches p. 131.
- CELT text001 reaches p. 136.
- The IA PDF reaches p. 93.
- The IA `_djvu.txt` download reaches about p. 54.

The closing pages (about pp. 180–201) cannot be reached this way. The Gutenberg plain-text file and the IA "search
inside" endpoint both returned "robots.txt unreachable".

Status key as in `research/quote-verification.md`.

## Results

| ID | Claimed | What the source actually says (exact wording read) | Source, page, date | Status | Note |
|---|---|---|---|---|---|
| T1 | "Supreme Wisdom has educed permanent good out of transient evil." (*Irish Crisis*, p. 1) | "Unless we are much deceived, posterity will trace up to that famine the commencement of a salutary revolution in the habits of a nation long singularly unfortunate, and will acknowledge that on this, as on many other occasions, Supreme Wisdom has educed permanent good out of transient evil." | Trevelyan, *The Irish Crisis* (London: Longman, 1848), opening paragraph, before the first page marker, so p. 1. Gutenberg #56727 HTML. | VERIFIED (re-read) | The full sentence is a prediction about "posterity". Quote from "on this, as on many other occasions" if space allows. |
| T2 (b) | "all-wise **and all-merciful** Providence" form, in *The Irish Crisis* | Read only as fragments in a historian's article. Donnelly says these come from *The Irish Crisis*'s **closing paragraph**: "a direct stroke of an all-wise and all-merciful Providence," / "the deep and inveterate root of social evil" / "the sharp but effectual remedy by which the cure is likely to be effected…." / "God grant that the generation to which this opportunity has been offered may rightly perform its part" | James S. Donnelly Jr., "The Great Famine and its interpreters, old and new", *History Ireland* (issue and year not shown on the web page), https://historyireland.com/?p=318 | **SECONDARY** (was UNVERIFIED) | It does exist and it is in *The Irish Crisis*: the closing paragraph, about p. 201, page not read. Donnelly gives **fragments**, so don't join them into one sentence; the words between them are unseen. Keep it apart from the Oct 1846 Monteagle letter ("direct stroke of an all-wise Providence", no "all-merciful"). These are two documents, 15 months apart. A search for the joined form "direct stroke of an all-wise and all-merciful Providence" found no copy, so quote the fragment as Donnelly gives it. |
| T3 | "…to promote their moral advancement, by awakening and encouraging a spirit of independent exertion." (*Irish Crisis* p. 129), offered as a substitute for B20 | "…to promote their moral advancement, by awakening and encouraging a spirit of independent exertion, and fostering habits of industry and self-reliance." | *The Irish Crisis* (1848), p. 129 (Gutenberg HTML and CELT text001, both read; between the 129 and 130 markers) | VERIFIED, **but context correction** | Both copies place it in the passage on the **Ladies' Relief Association for Ireland**: it states that charity's aims, among Trevelyan's accounts of private relief, next to the Owenmore committee on p. 131. **It is not Trevelyan stating government policy.** It cannot stand in for B20 as "Trevelyan says relief must give way to self-reliance". If used, the caption must say it describes a ladies' charity's aims. Whether these are Trevelyan's words or his quotation of the Association's own prospectus was not settled. |
| T4 | "no orders for supplies of food would be sent by the Government to foreign countries" (page to add) | "1st. That no orders for supplies of food would be sent by the Government to foreign countries." (the p. 54 marker falls inside the sentence, after "supplies") | *The Irish Crisis* (1848), **pp. 53–54**, Gutenberg HTML | VERIFIED (page added) | It is the first of three measures listed for the 1846–7 season. The IA OCR of pp. 53–54 also has the reason nearby: purchases "in the local markets of Ireland, where the appearance of the Government as a buyer must have had the effect of keeping up prices and encourag[ing]…" (cut off where the tool stopped reading). |
| T2 (a) | Monteagle letter, Oct 1846, "direct stroke of an all-wise Providence" | not re-read | — | SECONDARY (unchanged) | No budget left. |
| B12 | Charles Wood, Aug 1846: "A want of food and employment is a calamity sent by providence; except through a purgatory of misery and starvation, I cannot see how Ireland is to emerge..." | Two separate quoted pieces, both credited to Wood: "A want of food and employment is a calamity sent by providence" and "Except through a purgatory of misery and starvation, I cannot see how Ireland is to emerge…" | Brendan Ó Cathaoir, "Food depots close to teach Irish a lesson", *The Irish Times* ("Famine Diary" column), 24 Aug 1996. The column covers the week of 24 Aug 1846. No recipient, date or archive reference given. | **PROBABLE** (was UNVERIFIED) | A newspaper column, not a scholarly source, so it is not SECONDARY under our rule. It supports **Wood, Aug 1846** and the wording of each piece. **The pack's semicolon joins two pieces that the column quotes apart, and the words between them are unknown.** The pack also lower-cases "except". Ó Cathaoir's 1997 *Irish Times* piece names Gray, Kinealy, Ó Gráda and Kerr as his sources. The likely scholarly home is Gray, *Famine, Land and Politics* (1999), citing the Hickleton Papers. |
| B14 | Wood, Dec 1846: "What has brought them… to their present state of helplessness? Their habit of depending on government..." | not found | Searches return only IrishCentral's "Was it genocide?" compilation and blog copies (leads only). Ó Cathaoir's two *Irish Times* pieces don't have it. | UNVERIFIED | Searches found no scholarly copy. Keep it off the wall. |
| B8 | Trevelyan to Routh, "July 1847": "habitually dependent… bring the food depots to a close" | not found | The *Irish Times* 24 Aug 1996 column on the depots closing does **not** use "habitually dependent". | UNVERIFIED (misdating still likely) | The column dates the depot closures to Aug 1846, which fits the earlier view: the letter belongs to summer 1846, not July 1847. |
| B15 | Trevelyan, Dec 1846: "…not to send orders abroad… a thing unheard of" | not read | — | UNVERIFIED (letter wording) | Use T4, now paged at pp. 53–54. |
| B17 | Trevelyan, Jan 1847: "…keep pace with the Cork prices…" | not read | The exact-phrase search found nothing. | UNVERIFIED (wording); document PROBABLE (Trevelyan to Routh, 2 Jan 1847, BPP 1847 LI, contents p. 443) | Needs the BPP scan. |
| B20 | "too much has been done for the people… independent exertion" (Trevelyan or Wood) | not found | Search returns only IrishCentral, Schiller Institute / *American Almanac* (LaRouche-movement sites) and blogs. | UNVERIFIED; **provenance poor** | No scholarly or primary copy found, and its main web carriers are not citable. **The T3 substitute does not carry the same meaning (see T3)**, so drop B20 rather than substitute. |

## Leads for the next pass
1. **Closing paragraph of *The Irish Crisis*, about pp. 195–201 (T2 b).** The fetch tool cannot read past about p. 136
   of any whole-book copy. Ways around that:
   - Gutenberg plain text `https://www.gutenberg.org/ebooks/56727.txt.utf-8`, read with an offset of 200,000+ (robots.txt timed out today; retry).
   - IA search inside: `ia600304.us.archive.org/fulltext/inside.php?item_id=irishcrisis00trev&doc=irishcrisis00trev&path=/13/items/irishcrisis00trev&q=merciful` (robots.txt timed out).
   - The *Edinburgh Review* vol. 87 (Jan 1848), the article's last page (about p. 320), on HathiTrust page view.
   - Or a deep-research run asked for "the final paragraph of Trevelyan's *The Irish Crisis* (1848) with page number".
2. **Donnelly article details:** read the *History Ireland* issue and year off the print or PDF (historyireland.com/?p=318 shows no issue). It is the chain for T2(b).
3. **B12:** Peter Gray, *Famine, Land and Politics* (1999), index under Wood, for the Hickleton Papers reference (recipient and date, Aug 1846). Also check Gray, "Potatoes and providence", *Bullán* 1:1 (1994).
4. **T3 context:** read pp. 128–130 of *The Irish Crisis* whole, to see whether the "independent exertion" words are the Ladies' Relief Association's own statement quoted by Trevelyan.
5. **B15, B17:** Commissariat Series BPP 1847 vol. LI (IA op1246627-1001). It needs a page-level view, because the fetch tool caps whole-file reads at about 120k characters. Use IA BookReader page URLs or HathiTrust; the contents give p. 443 for B17.
6. **B8:** the 1846 Commissariat paper (Nov 1845 to Aug 1846). Also Woodham-Smith, *The Great Hunger*, ch. 5, for the "habitually dependent" letter (expected to be July 1846, Trevelyan to Routh).
7. **B14, B20:** Woodham-Smith and Gray (1999) indexes. If no scholarly page turns up, retire both.

## Sources read this pass
- Trevelyan, *The Irish Crisis* (1848). Read in four copies, each cut short by the fetch tool:
  - Gutenberg #56727 HTML, https://gutenberg.org/cache/epub/56727/pg56727-images.html (read to p. 131);
  - CELT E840001-002, https://celt.ucc.ie/published/E840001-002/text001.html (read to p. 136);
  - IA irishcrisis00trev, the PDF (to p. 93) and the `_djvu.txt` (to about p. 54).
- J. S. Donnelly Jr., "The Great Famine and its interpreters, old and new", *History Ireland*, https://historyireland.com/?p=318
- B. Ó Cathaoir, "Food depots close to teach Irish a lesson", *Irish Times*, 24 Aug 1996, https://www.irishtimes.com/news/food-depots-close-to-teach-irish-a-lesson-1.79616
- B. Ó Cathaoir, "Research points finger at dogma and neglect", *Irish Times*, 27 Dec 1997, https://www.irishtimes.com/news/research-points-finger-at-dogma-and-neglect-1.140713 (no Wood wording).
