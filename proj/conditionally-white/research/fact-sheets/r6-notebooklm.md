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
| B2 | Trevelyan, "real/great evil … moral evil" | **Found.** Woodham-Smith p. 151 (other printings p. 156): to **Colonel Jones** (Harry Jones, Board of Works chairman), "on December 2"; opening word **"great"**. Year not in the answer; the chapter's context makes it 1846. Endnote 16 is missing from the scan. | **SECONDARY** (date, recipient, wording settled; primary letter unread) |
| F29 | Allen's definition of racial oppression | **Found.** Vol. 1 p. 32 (restated vol. 2 p. 239); racial vs national oppression, vol. 1 p. 273 n. 11. | **VERIFIED (Allen's own text, via NotebookLM)** → AL1, AL2 |
| F29 | Allen on Ireland as racial oppression without a colour line | **Found.** Vol. 1 p. 22; also pp. 27–28, 30, 71, 92. | **VERIFIED (via NotebookLM)** → AL3 |

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

## Answer 5: Trevelyan's "great evil" (B2)

Woodham-Smith, *The Great Hunger*, p. 151, as NotebookLM returned it (the stray "16" is her endnote mark):

> These complications confirmed Trevelyan in his 16 opinion of the Irish. "The great evil with which we have to
> contend," he wrote to Colonel Jones, on December 2, is "not the physical evil of the famine, but the moral evil of
> the selfish, perverse and turbulent character of the people."

**Notes for the essay.**
- Settles three things: the opening is **"great"**, not "real"; the recipient is **Colonel Harry Jones**, not
  Monteagle; the date is **2 December** (1846 by the chapter's context; the answer itself gave no year, so confirm
  from her page before printing the year).
- Her quote marks split it: "The great evil with which we have to contend" and "not the physical evil … people" are
  two quoted pieces with her words between. Quote them as two pieces, or quote only the second.
- Still SECONDARY: endnote 16 isn't in the scan, so the letter itself (likely Trevelyan's letter books) is unread.
- Page: p. 151 in this copy; the earlier p. 156 came from a review of a Penguin printing. Cite the edition used.

## Answers 6–7: Allen's own wording (F29)

From Theodore W. Allen, *The Invention of the White Race*, as NotebookLM returned it. Edition not stated (Verso 1994
and 1997, or the 2012 second edition); check page numbers against the edition cited.

- **Vol. 1, ch. 1 ("The Hallmark of Racial Oppression"), p. 32 (AL1):** "The assault upon the tribal affinities,
  customs, laws and institutions of the Africans, the American Indians and the Irish by English/British and
  Anglo-American colonialism reduced all members of the oppressed group to one undifferentiated social status, a
  status beneath that of any member of any social class within the colonizing population. This is the hallmark of
  racial oppression in its colonial origins, and as it has persisted in subsequent historical contexts."
- **Vol. 2, ch. 10 ("The Status of African-Americans"), p. 239:** "The hallmark of racial oppression in its colonial
  origins and as it has persisted in subsequent historical contexts is the reduction of all members of the oppressed
  group to one undifferentiated social status, a status beneath that of any member of any social class within the
  oppressor group. It is a system of rule designed to deny, disregard, delegitimate previous or potential social
  distinctions that may have existed or that might tend to emerge in the normal course of development of a class
  society."
- **Vol. 1, ch. 4, p. 273, note 11 (AL2):** "The essential difference between racial and national oppression is the
  following. In the system of racial oppression, social control depends upon the denial of the legitimacy of social
  distinctions within the oppressed group. In the system of national oppression, social control depends upon the
  acceptance and fostering of social distinctions within the oppressed group."
- **Vol. 1, Introduction ("The Irish Mirror"), p. 22 (AL3):** "Irish history presents a case of racial oppression
  without reference to alleged skin color or, as the jargon goes, "phenotype.""
- **Vol. 1, ch. 1 ("The Irish Analogy"), pp. 27–28:** "To our conditioned minds, the attitude and behavior of
  Anglo-Americans toward African-Americans and American Indians have the readily recognizable character of racial
  oppression. But when racial oppression is defined in terms of its operational principles, the exclusion of the
  Irish case is seen to be wholly arbitrary. The exclusion is especially deplorable when practiced by
  European-American scholars, because it ignores a case where "white" consciousness on the part of the observer is
  least likely to affect the drawing of conclusions. A "need to know they were white" cannot possibly serve to
  explain the attitude of the English toward the Irish."
- **Vol. 1, ch. 1 ("The Analogy as Practice"), p. 30:** "In its sameness with respect to the Irish and to American
  Indians and African-Americans, this ideology and practice was not concerned with "phenotype," color, etcetera, but
  rather with the "uncivilized ways" of the victims."
- **Vol. 1, ch. 3 ("Protestant Ascendancy and White Supremacy"), p. 71:** "Students of American history, however,
  have almost completely neglected this field of investigation for insights into the system of racial oppression
  which, more than any other force or factor, has controlled the flow of United States history. This neglect is due,
  no doubt, to the fact that they mistake the chattel form of labor, along with perceived variations in physical
  appearance, for the essential substance of racial oppression."
- **Vol. 1, ch. 3, p. 92:** "When the historian W. F. T. Butler concluded that "A common misfortune had welded all
  these [Catholics – Old English and native Irish] into one race," he was not referring to a genetic "merger" of Old
  English and Irish Catholics, nor to the appearance of some new Irish phenotype. He was affirming, rather, that that
  which in Ireland took the form of anti-Popery, and in time would be officially known as the Protestant Ascendancy,
  was a classic system of racial oppression."

(Curly quotes in NotebookLM's paste are shown straight here; the quote sheet keeps them as returned.)

**Notes for the essay.**
- Ch3 can now quote Allen in his own words: AL3 as the thesis line, AL1 as the definition, AL2 to meet the "that's
  just national oppression" reply.
- These are Allen's argument, not settled fact (F29). Keep the critics beside him (Q9-1: Kolchin, Arnesen, the
  origins debate, the religion-not-race objection). AL2 sharpens that objection: Penal-era Catholics who conformed
  escaped, which reads more like the "fostering of social distinctions" he assigns to national oppression.
- The p. 92 Butler quotation is Allen quoting Butler; credit it that way if used.
