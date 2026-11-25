# R3: Trevelyan, Wood, Clarendon (B21, B17, B15, B8, B14, B12, T2)

Round-3 worker, 2026-11-24. I worked the items in the order given and stopped at about 21 page reads, the round-3
budget. Status key as in `research/quote-verification.md`.

**Routes that failed this pass**, so the next pass doesn't repeat them:
- **Google Books:** `books.google.com` and `google.com/search?tbm=bks` are both `robots_disallowed` for WebFetch. The
  curl proxy refuses them (403), and the Books API (`googleapis.com/books/v1`) answers 429 with a zero daily quota.
- **curl:** the proxy refuses archive.org, HathiTrust and sarkoups.free.fr.
- **archive.org "search inside":** `ia801001.us.archive.org/fulltext/inside.php?...` returns `client_error`.
- **Long archive.org URLs:** the WebFetch proxy refuses URLs of about 250 characters or more ("url exceeds the maximum
  fetchable length"). That rules out the one open full-text copy of Woodham-Smith found (see leads).
- **Whole-file reads with an offset:** `offset` does not get past the fetch cap. For `op1246627-1001_djvu.txt` (2.39 MB)
  the fetched text is only 81,235 characters, so offset 1,950,000 returned nothing.

## Results

| ID | Claimed | What the source actually says (exact wording read) | Source, page, date | Status | Note |
|---|---|---|---|---|---|
| B21 (1849) | Clarendon to Russell, 26 Apr 1849: "…coldly persist in a policy of extermination" | Not re-read this pass. The wording stays as R2 read it through the ERIC curriculum. | Woodham-Smith, *The Great Hunger*, p. 381 (per ERIC ED 439 056 p. 13). Not opened. | **PROBABLE (unchanged)** | Every route to p. 381 failed (see above). The archive.org copies found are lending items: `greathungerirela00wood` (NAL Signet 1964, different pagination), `greathungerirel00wood`, `greathungerirela0000wood` and others. There is also one open upload (see leads). Keep the caption warning: Clarendon was **attacking** the policy, not proposing it. |
| B21 (1847) | Clarendon, Sept 1847: "They are always in the mud…" | not reached | — | UNVERIFIED (unchanged) | Only carrier is still IrishCentral. Keep it off the wall. |
| B17 | Trevelyan, "January 1847": "However serious and painful it may be, it is indispensable that the prices at our depots should keep pace with the Cork prices..." | The **Contents** list of the Jan–Mar 1847 Commissariat volume has an entry for **"Mr. Trevelyan to Sir R. Routh", dated 22 January 1847**. Its summary includes the words "the prices at our depots should keep pace with the Cork prices". The same entry also concerns store-room for the London (British) Relief Association. The entry before it is Mr. Ball to Mr. Trevelyan, 19 Jan; the one after is Mr. Trevelyan to Lieut.-Col. Jones, 23 Jan (Government depots open at Skibbereen and Berehaven, another to be set up near Skull). | *Correspondence from January to March, 1847, relating to the measures adopted for the relief of the distress in Ireland. Commissariat Series. [Second Part.]* (London: W. Clowes for HMSO, 1847), Contents. Read as a scan at http://sarkoups.free.fr/relief1847.pdf (a private site's copy of the official paper; cite the paper, not the host). No page number was legible on that line. | **PROBABLE** (was UNVERIFIED). **Date and volume corrected.** | **Correction:** the letter is dated **22 Jan 1847** and sits in the **Second Part (Jan–Mar 1847)**. R2 had it as 2 Jan 1847, First Part, BPP 1847 LI p. 443; that was wrong. The R2 sheet gives the Second Part as BPP 1847 LII, IA `op1246629-1001`. What I read is the Contents summary, which the clerks wrote, not the letter itself, and the tool's reader would only quote the phrase, not the whole Contents line. "However serious and painful it may be, it is indispensable that…" is **still unread**. The body text in that PDF stops partway through a letter of 23 Jan, and the 22 Jan letter was not in the part I could read. Not for the wall until the letter itself is read. |
| B15 | Trevelyan, Dec 1846: "…pledge not to send orders abroad… a thing unheard of" | not read | Expected in the First Part (Jul 1846–Jan 1847, BPP 1847 LI, IA `op1246627-1001`), Dec 1846 letters. Past the fetch cap. | UNVERIFIED (unchanged) | Use T4 (*Irish Crisis* pp. 53–54, VERIFIED). |
| B8 | Trevelyan to Routh, "July 1847": "habitually dependent… food depots to a close" | not found | One phrase search ("becoming habitually dependent on Government" Trevelyan depots) found nothing relevant. | UNVERIFIED (unchanged) | Misdating to summer 1846 is still likely. |
| B14 / B12 | Wood, Dec 1846 / Aug 1846 | not reached (budget) | — | B14 UNVERIFIED, B12 PROBABLE (both unchanged) | Gray (1999) not opened. |
| T2 | *Irish Crisis* closing: "all-wise and all-merciful Providence" | not reached (budget) | — | SECONDARY in fragments (unchanged) | |

Counts this pass: VERIFIED 0 · SECONDARY 0 · WRONG 0 · moved to PROBABLE 1 (B17, with its date and volume corrected) ·
unchanged 6.

## Leads for the next pass
1. **B17, the letter itself.** Trevelyan to Routh, 22 Jan 1847, Commissariat Series Second Part (Jan–Mar 1847).
   - Find its number and page in the body. Try the IA item `op1246629-1001` with a page-level view (BookReader page
     URL), not the whole `_djvu.txt`.
   - Or try the sarkoups.free.fr PDF from a browser, not WebFetch. The text WebFetch got ran out partway through the
     23 Jan letters.
   - Search the body for "serious and painful" and "keep pace".
2. **B21 (1849), Woodham-Smith p. 381.** One archive.org copy is an open upload, not a lending copy:
   `the-great-hunger-ireland-1845-1849-cecil-woodham-smith-cecil-w.-smith-cecil-blanche-fitz` (server ia601009, dir
   `/3/items/…`).
   - Its text file is named `The great hunger- Ireland 1845-1849 - Cecil Woodham Smith, Cecil W. Smith, Cecil Blanche Fitz -_djvu.txt`.
     The URL is too long for WebFetch's proxy.
   - It needs a browser, or the client opening it. The upload is labelled public domain, but the book is in copyright,
     so cite the book and page, never the upload.
   - The edition of that upload is not known, so check that its page numbers match the 1962 Hamish Hamilton edition
     before giving "p. 381".
   - The lending copies (`greathungerirel00wood`, `greathungerirela0000wood`) can be searched inside from a
     browser BookReader.
   - Or put it to the client's deep-research run: "Woodham-Smith, *The Great Hunger*, p. 381, Clarendon to Russell
     26 April 1849, exact wording".
3. **B15.** The First Part (`op1246627-1001`), Dec 1846, page-level only. The index item `op1246628-1001` should give
   the page for "orders abroad" and "unheard of".
4. **B8.** HathiTrust catalogue Record 001119839: *Correspondence explanatory of the measures adopted… for the relief
   of distress arising from the failure of the potato crop* (the 1846 paper, Nov 1845–Aug 1846). It is full view
   (University of Michigan), but the catalogue page shows no volume id. Find the babel id, then read the plain-text view
   page by page for "habitually dependent", likely July–Aug 1846.
5. **B12 / B14.** Gray, *Famine, Land and Politics* (1999), index under Wood (Hickleton Papers). Not opened.
6. **T2.** As in the R2 leads (the closing paragraph of *The Irish Crisis*, Edinburgh Review vol. 87 last page). Not
   opened.

## Sources read this pass
- *Correspondence from January to March, 1847, relating to the measures adopted for the relief of the distress in
  Ireland. Commissariat Series [Second Part]* (HMSO, 1847): title page and Contents, from the scan at
  http://sarkoups.free.fr/relief1847.pdf (about 110k characters of text reached, body to 23 Jan 1847).
- archive.org metadata and file listings for the Woodham-Smith items named above, and for `greathungerirela00wood`
  (NAL 1964, lending). No book text was read.
- HathiTrust catalogue Record 001119839 (catalogue page only).
