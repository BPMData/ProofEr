# R6: Bryan's NotebookLM pass over six print books

Round 6, 2026-11-25. Bryan loaded six books into NotebookLM and ran fixed questions (one per open item), with a
role prompt requiring word-for-word quotes, page numbers and "Not found in the sources" for misses. Answers are
NotebookLM's reading of the books, pasted back by Bryan; wording below is as NotebookLM returned it. Status key as
in `research/quote-verification.md`.

Books in the notebook: Killen (ed.), *The Famine Decade: Contemporary Accounts 1841–1851* (Belfast: Blackstaff,
1995); Woodham-Smith, *The Great Hunger* (1962); Allen, *The Invention of the White Race*, vols 1–2; Ignatiev,
*How the Irish Became White* (1995); Roediger, *The Wages of Whiteness*.

| ID | Question | Finding | Status |
|---|---|---|---|
| B13 | *Waterford Freeman*, Aug 1846, "men in trade" | Not found in any of the six books. Woodham-Smith has the Aug 1846 decision to leave grain to private trade and Fr Mathew/Routh on "capitalists in the corn and flour trade" (pp. 86, 113–114), but no *Waterford Freeman*. | UNVERIFIED → **retire** (Killen, the best lead, doesn't have it) |
| B16 | *Sligo Champion*, Jan 1847, McManus inquest, pig | **Found.** Killen p. 99 (and editor's intro p. 6) reprints the *Illustrated London News*, 16 Jan 1847, which copies the *Sligo Champion* (credited "—Champion."). Inquest 12 Jan 1847. Names as printed: **Thomas M'Manus, of Kilmactranny**; **Thomas Burrows, Esq., M.D.** (not "Burroughs"). | **VERIFIED (contemporary reprint, via Killen)** |
| B23 | *Newry Telegraph*, Mar 1849, "failed in Connaught and Munster" / "painstaking, industrious, laborious people" | Not found in any of the six books. Killen's only *Newry Telegraph* item is an Armagh blight report via the *ILN*, 18 Aug 1849 (p. 227). Killen p. 221 has a Mar 1849 "EMIGRATION FROM DOWN" piece on the rate-in-aid (credited by NotebookLM to the *Dublin University Magazine*; unchecked). | UNVERIFIED → **retire** |
| B6 | Duke of Cambridge, 1846, potatoes/seaweed/grass | Not found. No Cambridge diet remark in any book (only Prince George at Carton, Aug 1849, Killen p. 226). | UNVERIFIED → **retire** the Duke's words; O'Connell's charge (*Northern Star*, 24 Jan 1846) stays PROBABLE if wanted |

## B16 text (Killen, p. 99, under "DEATHS FROM STARVATION / AWFUL STATE OF SLIGO")

> HORRIBLE!—An inquest was held on the 12th instant, upon the body of Thomas M'Manus, of Kilmactranny—verdict.
> "Deceased came to his death by hunger and cold." This wretched creature was observed by a man lying in a muddy
> ditch; he was raised up, and the man went to two or three houses in the neighbourhood, and asked the people to
> admit deceased, but they refused, alleging that he had typhus fever. He then carried deceased to a haggard and
> placed him upon some straw, where he was found dead on the following morning, and dreadfully mutilated. We copy
> the evidence of Thomas Burrows, Esq., M.D.— "Examined the body of Thomas M'Manus; both the legs, as far as the
> buttocks, appeared to have been eaten off by a pig; is of opinion his death was caused by hunger and cold."
> There was not a particle of food found in deceased's stomach or intestines. Those who saw the body were of
> opinion, from the agonized expression of M'Manus's countenance, that he was alive when the pig attacked him.
>
> Let Lord John Russell read the above, and then say, if he can, that he is justified in keeping the government
> stores closed against the people.—Champion.

(NotebookLM's paste had stray doubled quote marks around the verdict; they're normalised above.)

**Notes for the essay.**
- The pack's wording is close but wrong in three places: "Burroughs" → **Burrows**, "both of the legs" → **both
  the legs**, "McManus" → **M'Manus** (keep the period spelling in the quote; "McManus" is fine in narration).
- Cite as: *Sligo Champion*, as reprinted in *Illustrated London News*, 16 Jan 1847; in Killen (1995), p. 99.
- The closing line ties the inquest straight to Russell's refusal to open the depots (B10), so the card can sit
  beside Russell on the wall, in the newspaper's own words.
- High-gravity item: the card states the evidence and stops. No garnish.
- "Those who saw the body were of opinion … he was alive" is the paper's report of bystanders' opinion, not the
  doctor's finding. Keep that attribution if the line is used.

## Answers 3–4: substitutes the books did turn up

- **Duke of Norfolk's curry powder (new, SECONDARY):** Woodham-Smith, p. 43: "More far-reaching was a suggestion
  made by the Duke of Norfolk, that in place of the potato the Irish should learn to consume curry powder, on which,
  mixed with water, he appeared to believe the population of India was nourished." Her wording, not the Duke's; date
  and primary not given in the answer. A candidate to replace B6's "aristocrat's diet tip" slot if its primary can be
  found.
- ***Dublin Evening Post*, 9 Sept 1845 (Killen p. 35):** "The Irish peasantry rely almost exclusively upon potatoes
  for their subsistence; and when the crop fails, they have nothing to fall back upon but grass, nettles, and
  seaweed." Contemporary reprint; usable for Ch4's opening.
- **1851 Census (Killen p. 249):** "…principally on the herbs of the field, nettle tops, wild mustard, and
  watercresses, and even in some places dead bodies were found with grass in their mouths… but along the coast every
  description of sea-weed was greedily devoured, often with fatal consequences…" Ellipses as NotebookLM returned
  them; read the full passage before quoting.
