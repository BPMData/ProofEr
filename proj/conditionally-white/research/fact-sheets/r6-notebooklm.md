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
| F29 | Allen's chronology and motive | **Found.** No official "white" status before a 1691 Virginia law (vol. 1 p. 195 n. 15); Bacon's Rebellion 1676 and the 1705 Act as the pivot (vol. 1 pp. 24–25); "beginning of the eighteenth century" (vol. 2 p. 115); why (vol. 2 pp. 239–240). | **VERIFIED (via NotebookLM)** → AL4–AL6; replaces the "from memory" note in Q9-1 |
| F29 | Ignatiev's thesis | **Found.** Pp. 1, 2–3, 59, 69. | **VERIFIED (via NotebookLM)** → IG1–IG4 |
| F30 | 1841 Address and the Irish-American response | **Found** in Ignatiev ch. 1: Address pp. 6, 9–10; Hughes p. 12; *Pilot* 5 Feb 1842 p. 13; Pottsville pp. 13–14; Garrison pp. 22–23; O'Connell 9 May 1843 p. 23, 11 Oct 1843 p. 29. | **SECONDARY (via Ignatiev)** → IA1–IA5, O2; O1 unchanged |
| F97 | Du Bois's "public and psychological wage" vs "wages of whiteness" | **Found.** Roediger pp. 12–13 (quoting *Black Reconstruction*), 60, 137; "wages of whiteness" is Roediger's own phrase (title, p. 13). | Du Bois **SECONDARY (via Roediger)** → DB1; Roediger **VERIFIED** → RG1 |
| F47 | Draft Riots death toll | Total **not found** in any of the six books. Allen vol. 1 p. 320 n. 77: five days, "eleven African-Americans were lynched" (cites Cook 1974, Bernstein 1990). Ignatiev and Roediger give no figures. | total unchanged (from Q10, not R6); lynching count **SECONDARY (via Allen)** |

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

## Answer 8: Allen's chronology and motive (F29, AL4–AL6)

As NotebookLM returned it (curly quotes shown straight):

- **Vol. 1, notes to ch. 1, p. 195, n. 15 (AL4):** "During my own study of page after page of Virginia county
  records, reel after reel of microfilm prepared by the Virginia Colonial Records Project, and other
  seventeenth-century sources, I have found no instance of the official use of the word 'white' as a token of social
  status before its appearance in a Virginia law passed in 1691, referring to 'English or other white women.'"
- **Vol. 2, ch. 11, p. 214:** "Grantham's testament has a significance that is beyond exaggeration: in Virginia, 128
  years before William Lloyd Garrison was born, laboring-class African-Americans and European-Americans fought side by
  side for the abolition of slavery. In so doing they provided the supreme proof that the white race did not then
  exist."
- **Vol. 2, ch. 8, p. 115:** "Two fair conclusions would seem to follow: First, "the white race" – supra-class unity
  of European-Americans in opposition to African-Americans – did not and could not have then existed. Second, the
  invention of the white race at the beginning of the eighteenth century can in no part be ascribed to demands by
  European-American laboring people for privileges vis-à-vis African-Americans."
- **Vol. 1, Introduction, pp. 24–25 (AL5):** "The pivotal events are seen to be Bacon's Rebellion in 1676 and the
  1705 revision of the Virginia laws, in particular, the "Act concerning Servants and Slaves." ... the problem of
  social control reconsidered; the invention of the "white race" – the truly Peculiar Institution – as the solution
  to the problem of social control, its failure in the West Indies, its establishment in the continental plantation
  colonies, signaled by the enactment of the "Act concerning Servants and Slaves," which formally instituted the
  system of privileges for European-Americans, of even the lowest social status, vis-à-vis any person of any degree
  of African ancestry, not only bond-laborers but free Negroes as well, however possessed of property they might
  be..." (the "..." are NotebookLM's; the passage reads like a chapter summary, so check the page.)
- **Vol. 2, ch. 13, p. 240 (AL6; the follow-up gives the same passage as p. 250, so the page is unsettled):** "Thus was the "white race" invented as the social control formation whose
  distinguishing characteristic was not the participation of the slaveholding class, nor even of other elements of
  the propertied classes; that alone would have been merely a form of the "beautiful gradation" of class
  differentiation prescribed by Edmund Burke. What distinguished this system of social control, what made it "the
  white race", was the participation of the laboring classes: non-slaveholders, self-employed smallholders, tenants,
  and laborers. In time this "white race" social control system begun in Virginia and Maryland would serve as the
  model of social order to each succeeding plantation region of settlement."
- **Vol. 2, ch. 13, pp. 239–240 (the motive):** "…The solution was to establish a new birthright not only for Anglos
  but for every Euro-American, the "white" identity that "set them at a distance," to use Sir Francis's phrase, from
  the laboring-class African-Americans, and enlisted them as active, or at least passive, supporters of lifetime
  bondage of African-Americans." Full passage, including the "counterfeit of social mobility" sentence, in Bryan's
  pasted answer; "Sir Francis" is not identified in the answer; check the page before naming him.

**Notes.** This replaces Q9-1's "from memory" chronology: 1676 → 1691 (first official "white") → 1705 Act →
"beginning of the eighteenth century". Still Allen's argument; the origins-debate critics (Jordan, Vaughan) date
anti-Black prejudice earlier.

## Answer 9: Ignatiev in his own words (F29, IG1–IG4)

- **Introduction, p. 1 (IG1):** "This book looks at how one group of people became white. Put another way, it asks
  how the Catholic Irish, an oppressed race in Ireland, became part of an oppressing race in America. It is an
  attempt to reassess immigrant assimilation and the formation (or non-formation) of an American working class."
- **Introduction, pp. 2–3 (IG2):** "…The outcome was not the inevitable consequence of blind historic forces, still
  less of biology, but the result of choices made, by the Irish and others, from among available alternatives. To
  enter the white race was a strategy to secure an advantage in a competitive society." Then, after the passage on
  what becoming white meant (selling themselves "piecemeal instead of being sold for life", juries, voting, living
  "wherever they could afford"): "In becoming white the Irish ceased to be Green."
- **Introduction, p. 3:** "In viewing entry into the white race as something the Irish did "on" (though not by)
  themselves, this book seeks to make them the actors in their own history."
- **Ch. 2, p. 59 (IG3):** "In this chapter I have tried to suggest that, while the white skin made the Irish eligible
  for membership in the white race, it did not guarantee their admission; they had to earn it. The following chapters
  will examine how they did so."
- **Ch. 3, p. 69 (IG4):** "The truth is not, as some historians would have it, that slavery made it possible to
  extend to the Irish the privileges of citizenship, by providing another group for them to stand on, but the
  reverse, that the assimilation of the Irish into the white race made it possible to maintain slavery. The need to
  gain the loyalty of the Irish explains why the Democratic Party, on the whole, rejected nativism. It also explains
  why not merely slavery but the color line became so important to it."

**Notes.** Ch5 claim 5 quotes IG1 and IG3 at full strength, then the pushback (Q9-2). IG4 is the boldest claim and
the most disputed; if used, say so. p. 3's "on (though not by)" shows Ignatiev giving the Irish agency, which is the
essay's own diaspora argument (Ch7).

## Answer 10: the 1841 Address and the replies (F30, IA1–IA5, O2)

All via Ignatiev, *How the Irish Became White*, ch. 1 ("Something in the Air"), so SECONDARY.

- **p. 6:** "In 1841 sixty thousand Irish issued an Address to their compatriots in America calling upon them to join
  with the abolitionists in the struggle against slavery. Heading the list of signers was the name of Daniel
  O'Connell, known throughout Ireland as the Liberator."
- **pp. 9–10, the Address (IA1), brought by Charles Lenox Remond, Dec 1841:** "America is cursed by slavery! WE CALL
  UPON YOU TO UNITE WITH THE ABOLITIONISTS, and never to cease your efforts until perfect liberty be granted to
  everyone of her inhabitants, the black man as well as the white man.... JOIN WITH THE ABOLITIONISTS EVERYWHERE.
  *They are the only consistent advocates of liberty.* Tell every man that you do not understand liberty for the
  white man, and *slavery for the black man;* that you are for LIBERTY FOR ALL, of every color, creed, and
  country.... Irishmen and Irishwomen! *Treat the colored people as your equals, as brethren.* By your memories of
  Ireland, continue to love liberty—hate slavery—CLING BY THE ABOLITIONISTS—and *in America you will do honor to
  the name of Ireland.*"
- **p. 12, Bishop John J. Hughes (IA2):** "the duty of every naturalized Irishman to resist and repudiate the address
  with indignation. Not precisely because of the doctrines it contains, but because of their having emanated from a
  foreign source, and of their tendency to operate on questions of domestic and national policy. I am no friend of
  slavery, but I am still less friendly to any attempt of foreign origin to abolish."
- **p. 13, the *Pilot*, 5 Feb 1842 (IA3):** abolitionist doctrines would "bathe the whole South in blood"; the Irish
  would never be drawn into "the vortex of abolitionism".
- **pp. 13–14, Pottsville miners (IA4):** "We do not form a distinct class of the community, but consider ourselves
  in every respect as CITIZENS of this great and glorious republic—that we look upon every attempt to address us,
  otherwise than as CITIZENS, upon the subject of the abolition of slavery, or any subject whatsoever, as base and
  iniquitous, no matter from what quarter it may proceed."
- **pp. 22–23, Garrison (IA5):** "It is now quite apparent that they will go *en masse* with Southern men-stealers,
  and in opposition to the anti-slavery movement…" and "Even to this hour, not a single Irishman has come forward,
  either publicly or privately, to express his approval of the Address, or to avow his determination to abide by its
  sentiments." Ignatiev calls the second "what may be the saddest words ever written about the Irish diaspora"
  (his words, not Garrison's).
- **p. 23, O'Connell, 9 May 1843:** "Over the broad Atlantic I pour forth my voice, saying, Come out of such a land,
  you Irishmen; or, if you remain, and dare countenance the system of slavery that is supported there, we will
  recognize you as Irishmen no longer." **Compared with O1:** the words match the *Signal of Liberty* (17 July 1843)
  exactly; Ignatiev drops the inner quotation marks around "Come out … no longer". Keep O1's newspaper wording.
- **p. 29, O'Connell's reply to the Cincinnati Repealers, 11 Oct 1843 (O2, new):** "It was not in Ireland you
  learned this cruelty," … "Your mothers were gentle, kind, and humane.... How can your souls have become stained
  with a darkness blacker than the negro's skin?" … and "never cease [their] efforts, until the crime... of being the
  worst enemies of the men of color shall be atoned for, and blotted out, and effaced forever." (Ellipses and
  brackets as returned.)

**Notes.** The Ch3 counter-quotation beat now has its full arc: the Address (IA1), the refusal (IA2–IA4), Garrison's
verdict (IA5), O'Connell's threat (O1) and his Cincinnati rebuke (O2). It also carries the Ch6 hand-off from
Ireland to America. Faneuil Hall (Jan 1842) isn't in the answer; it stays on Q9-7 alone.

## Answer 11: Du Bois's wage and Roediger's phrase (F97, DB1, RG1)

Roediger, *The Wages of Whiteness*, as NotebookLM returned it:

- **Ch. 1, pp. 12–13:** "…But vital for the white workers Du Bois studied most closely was, as he puts it in a
  brilliant, indispensable formulation, that even when they 'received a low wage [they were] compensated in part by
  a ... public and psychological wage.' … the idea that the pleasures of whiteness could function as a 'wage' for
  white workers. That is, status and privileges conferred by race could be used to make up for alienating and
  exploitative class relationships, North and South. White workers could, and did, define and accept their class
  positions by fashioning identities as 'not slaves' and as 'not Blacks'. When they did so, Du Bois argued, the wages
  of whiteness often turned out to be spurious…" (NotebookLM elided Roediger's long Du Bois block quote.)
- **Ch. 3, p. 60:** "Avoidance of connections to dependency and to blackness paid, in Du Bois's language, 'public and
  psychological' wages. But there were costs as well, not only in terms of race relations but also the wedding of
  labor to a debased republicanism."
- **Ch. 7, p. 137 (RG1):** "The imperative to define themselves as white came but from the particular 'public and
  psychological wages' whiteness offered to a desperate rural and often preindustrial Irish population coming to
  labor in industrializing American cities."

**Notes.** Settles the brief's "whiteness as wages ✱ cite carefully": credit Du Bois with "a sort of public and
psychological wage" (*Black Reconstruction*, 1935) and Roediger with "the wages of whiteness" (1991). p. 137's "came
but from" reads oddly; check the page before quoting.

## Answer 12: the Draft Riots death toll (F47)

Not found as a total in any of the six books. Allen, vol. 1, notes to ch. 8, p. 320, n. 77:

> "That blow took the form of the Draft Riot (sometimes described as a succession of riots) which lasted five days,
> during which eleven African-Americans were lynched in an atmosphere of bloodthirsty white-supremacism. The rioting
> was finally ended by Federal troops. (See: Adrian Cook, The Armies of the Street; the New York City Draft Riots of
> 1863 [Lexington, Kentucky, 1974]; Iver Bernstein, The New York City Draft Riots: Their Significance for American
> Society and Politics in the Age of the Civil War [New York, 1990].)"

**Notes.** F47's "at least 105 … about 119 documented" stands on its earlier sources (Q10), not on these books.
"Eleven lynched" is usable as SECONDARY via Allen; for a total, Cook (1974) is the standard count. Ignatiev (pp. 84,
88, 121) and Roediger (p. 172: "working class racism to new depths") give no figures.

## Follow-up A: Allen's Penal Laws / Virginia parallel (vol. 1, ch. 3, "Penal Laws and 'Race' Laws", pp. 81–90)

Asked because NotebookLM offered it after answer 7. Not a printed table: Allen runs the comparison in prose under
four heads he calls the defining characteristics of racial oppression (pp. 82–83): "(1) declassing legislation,
directed at property-holding members of the oppressed group; (2) deprivation of civil rights; (3) illegalization of
literacy; and (4) displacement of family rights and authorities."

Paired measures as Allen gives them (dates and statute references are his, unchecked against the statutes):

| Head | Ireland (Penal Laws) | Virginia / Anglo-America | Allen, page |
|---|---|---|---|
| Property | Catholics "by law forbidden to acquire land (except as short-term tenants)" | 1670: Black colonists barred from acquiring "any bond-laborers except those of African ancestry"; after 1691 the newly freed may not stay without leave | 83–84 |
| Legal existence | "the law does not suppose any such person to exist as an Irish Roman Catholic" (Chancellor and Chief Justice) | Taney, *Dred Scott* (1857): "there are no rights which negroes have that white men are bound to respect" | 83–85 |
| Witnesses | — | 1705 court law: "popish recusants convict, negroes, mulattoes and Indian servants" incapable as witnesses (AL7) | 85 |
| Juries | juries "could be limited to Protestants only" when the defendant was Catholic | 1705: Black bond-laborers lose jury trial; 1832: free Black people too, except capital cases | 85–86 |
| Vote | 1727: "[n]o papist, though not convict, shall be entitled or admitted to vote" | 1723: Black freeholders lose the vote for the first time | 86 |
| Literacy | 1692 (4 W & M c. 2): crime to go abroad for schooling; 1695 (7 Will. III c. 4): crime to teach "Papists"; 8 Anne c. 3 raises it to perpetual imprisonment and forfeiture | 1832, after Nat Turner: crime to teach a free Black person to read and write | 86–87 |
| Marriage | 1697 re-enactment of the bar on English–Irish intermarriage; "corruption and perversion", "dishonour to Almighty God" | 1691: first penalties on marriage between Europeans and Black or Indian people; "abominable mixture" | 87–88 |

Key passages as returned:

- p. 81: "At the threshold of the eighteenth century, it was Virginia that led the way among Anglo-American
  continental colonies in codifying the concept that, "race, not class … [is] the great distinction in society." It
  was then, too, that the Protestant Ascendancy instituted its system of Penal Laws, designed to "put an end to all
  other distinctions in Ireland, but that of Protestant and Papist.""
- p. 85: "The kinship of spirit between the Protestant Ascendancy and white supremacy was put on record at the outset
  of the "white race" era in a 1705 Virginia law reconstituting the Virginia Court system: "popish recusants convict,
  negroes, mulattoes and Indian servants, and others not being christians, shall be deemed and taken to be persons
  incapable in law, to be witnesses in any case whatsoever.""
- pp. 86–87: "…the first of the Penal Laws (7 Will. III c. 4, Irish Statutes), passed in 1695, made it a criminal
  offense for any person (except within one's immediate family) to teach "Papists" to read or write, or otherwise
  school them. "No person whatsoever of the popish religion," it said, "shall publickly or in private houses teach
  school or instruct youth in learning within this realm.""

**Checks.**
- p. 83 as returned reads "by virtue of the headlight system": almost certainly an OCR error for **headright** (the
  land grant per imported laborer). Quote it as "[headright]" or avoid the sentence.
- Allen cites 7 Will. III c. 4 for both the 1695 teaching ban and the ban on going abroad for schooling (p. 87),
  having given the latter as 4 W & M c. 2 (1692) a page earlier. Check before printing a chapter number.
- Allen quotes Sigerson, Scully and the Irish judges; credit those lines "as quoted by Allen".

**Use in the essay.** This is the source spine for Ch3's ladder annotations ("what whiteness excluded"): each rung can
carry an Irish and a Virginian date. It is **Allen's framing**, not a neutral table: the pairing is his argument (F29),
and the religion-not-race objection (Q9-1 (c)) still applies, since a Catholic who conformed escaped every Irish
column.

## Follow-up B: the 1705 "Act concerning Servants and Slaves" (vol. 2, ch. 13, pp. 248–250; App. II-F, p. 261)

Allen's five areas of "white-skin privilege" in the act (3 Hening 447–462), as returned:

- **pp. 248–249:** "the revised Virginia code of 1705 took pains to specify unprecedented guarantees for the European
  "christian white" limited-term bond-laborers. … The new code forbade the master to "whip a christian white servant
  naked, without an order from the justice of the peace," the offending master to be fined forty shillings payable
  to the servant."
- **p. 249, freedom dues:** "to every male servant, ten bushels of corn, thirty shillings in money (or the equivalent
  in goods), a gun worth at least twenty shillings; and to every woman servant, fifteen bushels of corn, forty
  shillings in money (or the equivalent in goods)." Livestock raised by Black bond-laborers "in 1692, and again in
  1705 with greater emphasis … were ordered to be confiscated."
- **p. 249, against free Black people:** no office of public trust; no witness "against a "white" person"; "thirty
  lashes at the public whipping post for "lift[ing] his or her hand" against any European-American"; no militia; no
  "gun, powder, shot, or any club, or any other weapon whatsoever, offensive or defensive."
- **pp. 249–250, read aloud:** parish clerks or churchwardens, "once each spring and fall at the close of Sunday
  service, should read ("publish") these laws in full to the congregants"; sheriffs at the courthouse door. Allen:
  "the general public was regularly and systematically subjected to officiai [official] white-supremacist agitation."
- **p. 250:** the "Thus was the "white race" invented…" passage, also given as p. 240 in answer 8. Page unsettled.

**Use in the essay.** A concrete list for Ch3 or Ch5 claim 5 of what "white" bought a poor European in 1705: a whip
needing a magistrate, a gun at the end of service, a law that let him strike a free Black neighbour who couldn't
strike back. The statute wording is via Allen (SECONDARY); Hening vol. 3 is online and would make it VERIFIED.

## Follow-ups 13, 14, 16 (asked from the list sent 2026-11-26)

**13. Food exported under armed guard (F41, WS1, WS2): found.** Woodham-Smith, *The Great Hunger*:

- **p. 75:** "…Forced by economic necessity to sell his produce he was furiously resentful when food left the market
  towns under the eyes of the hungry populace, protected by a military escort of overwhelming strength. From
  Waterford, the Commissariat officer wrote to Trevelyan, on April 24, 1846, "The barges leave Clonmel once a week for
  this place, with the[-]export supplies under convoy which, last Tuesday, consisted of 2 guns, 50 cavalry and 80
  infantry escorting them on the banks of the Suir as far as Carrick.""
- **p. 71:** "Coffin wrote to Routh from Limerick pointing out "the inconsistency of importing supplies into[.]a
  country which is at the same time exporting its own resources." Limerick was an export centre, and no doubt Coffin
  had seen ship after ship laden with wheat, oats, cattle, pigs, eggs and butter, sailing away down the Shannon…"
- **pp. 120–121 (autumn 1846):** four companies of the 47th Foot sent to Dungarvan; on 1 October grain ships there
  couldn't be loaded because the hired labourers feared the crowds. "…Trevelyan arranged for the provisioning, with
  beef, pork and biscuit, of 2,000 troops, formed into mobile columns "to be directed on particular points at very
  short notice."" Trevelyan: "food riots are quite different from [a] rebellion and are not likely to be of long
  duration" (NotebookLM: "ease rebellion", a scan error). "…all vessels loaded with grain or meal passing up the
  river Fergus were to have a naval escort", Admiral Pigot at Cork proposed a "vessel of war" with marines off Bantry
  and Berehaven, depots were guarded by police and troops, and Hewetson reported from Limerick on 10 October that
  troops went out daily to guard the corn harvest.
- **Killen p. 115 (*ILN*, 13 Feb 1847):** a Government steamship guarding a sloop's 50-ton cargo being sold "at
  'famine prices'" to a population of 27,000. This is **food arriving for relief sale**, not food leaving; don't use
  it as export evidence.

**Notes.** This reverses F41's "no source says under military escort" for 1846, at SECONDARY strength: the
Commissariat letter is quoted by Woodham-Smith, not read. It's one dated convoy plus an autumn policy of escorts,
not proof that every shipment was guarded. Ch5 claim 2's verdict is reopened for Bryan (see the outline). Scan
artefacts ("the-export", "into.a", "ease rebellion") are corrected in brackets above; check the page before quoting
any of them.

**14. The Duke of Norfolk's curry powder (NF1): partly found.** Woodham-Smith p. 43 gives it only in her own words,
with no date and nothing quoted from the Duke; the paragraph before is Lord Clare's warning of 5 Nov 1845, so the
context is late 1845. The same paragraph has the plan to cut the 12,000 police and army horses' corn from ten to five
pounds a day ("an extra 60,000 pounds a day"). Use only as "Woodham-Smith records a suggestion by the Duke of
Norfolk…", undated.

**16. The Draft Riots (F47, F48): not found.** No total death toll, no Cook or Bernstein figure, and no Colored
Orphan Asylum in any loaded book; Allen's "eleven African-Americans were lynched" (vol. 1 p. 320 n. 77) is the only
number. This changes nothing: F47's range and F48's asylum facts rest on other sources (Bernstein; Adelman,
*Commonplace*, 2017). Related: Philadelphia mobs attacked Black orphan asylums earlier: Ignatiev p. 133 (1838: "a mob
attacked the still-unoccupied, Quaker-sponsored Shelter for Colored Orphans"), Ignatiev p. 124 (Lippard's 1844 novel
*The Quaker City*: a rioter who "helped to burn a nigger church, two orphans' asylums and a school-house"; fiction,
and the slur is the novel's), and Roediger p. 108 (Grimsted: "the tendency to riot against asylums for Black orphans
carried the singling out of the defenseless for attack to a chilling extreme"). These could set up the 1863 asylum
as part of a pattern.

NotebookLM's answer to 16 lists Fanon, *The Wretched of the Earth*, among the loaded books, so the notebook holds a
seventh title.

Still out with Bryan (as of answer 16): follow-ups 15 (the year of Trevelyan's "December 2"), 17 (Garrison's date and paper; the
Pottsville meeting), 18 (Faneuil Hall, Jan 1842), 19 (Roediger p. 137's exact sentence).

## Follow-up: the autumn 1846 food riots (asked from NotebookLM's own offer)

Killen has **no** Youghal or Dungarvan account; the 1846 riots are in Woodham-Smith pp. 120–121. Killen has three
other crowd scenes.

**Woodham-Smith, pp. 120–121 (SECONDARY, her narrative):**
- **Youghal, 25 Sept 1846:** "To people desperate with hunger the sight of food streaming out of the country was once
  more unbearable, and serious riots took place—more serious than any riots of the previous years. At Youghal, near
  Cork, a small port much used for export, an outbreak took place on September 25. A large crowd of country people,
  described by the police as "enraged," attempted to hold up a boat laden with export oats—the police sent for
  troops, and the crowd was checked, with difficulty, at Youghal bridge." Under-Secretary T. N. Redington was sent to
  London "by the next boat to explain to the Government."
- **Dungarvan, 29 Sept 1846 (WS3):** "A crowd of starving unemployed entered the town, threatened merchants and
  shopkeepers, ordering them not to export grain, and plundered shops." After arrests, police failure and the Riot
  Act, "the officer commanding the Dragoons, Captain Sibthorp, gave the order to fire, and twenty-six shots were fired
  into the crowd, which then retreated. Several men were wounded and two were left lying on the ground, dead." The
  regiment is the 1st Royal Dragoons (the paste reads "Ist").
- **1 Oct 1846:** grain ships at Dungarvan couldn't be loaded because the hired labourers "were afraid of the
  crowds"; then Trevelyan's 2,000 troops in mobile columns (see follow-up 13).

(Scan dots and slips in the paste, "was. once", "police-as", "woul", "stcne-throwing", "men were. wounded", are
normalised above.)

**Killen, contemporary reprints (VERIFIED as reprints):**
- **Clonmel flour mills, *ILN* 4 Apr 1846 quoting the *Freeman* (pp. 59–60; K1):** headed "THE FAMINE WAR COMMENCED /
  INCREASE OF DISTRESS—OUTBREAK AT CLONMEL". Several hundred people, "whose bones protruded through the skin which
  covered them—staring through hollow eyes as if they had just risen from their shrouds", attacked the mills of
  "several Quaker gentlemen named Grubb, Malcomson, and Hughes"; "the army, consisting of artillery and dragoons"
  dispersed them "without loss of property, and happily without loss of life".
- **Dublin bread carts, *Downpatrick Recorder* 9 Jan 1847 (p. 93):** forty or fifty countrymen "surrounded a bread
  cart belonging to Mr. Walsh, baker, of No. 3, Dorset-street" and took "twenty loaves of bread and about a dozen
  rolls, value about ten or eleven shillings… some devouring the bread with evident voracity." Elsewhere bakers gave
  bread when asked, and "Several bread-carts were stopped in the outlets of the city, and their contents taken."
- **Kanturk workhouse, *Cork Examiner* via Killen, Oct 1847 (pp. 161–162):** about two thousand people from
  Kilbolane and Shandum at the workhouse gate demanding out-door relief; the military at first "refused to act";
  bayonets, a threat of the Riot Act; and "A strange fact—more powder was purchased by these out-door relief folks on
  that day than was sold for the previous year in the town of Kanturk." The 2l. the magistrates gave them for bread
  went mostly on "powder and ball".

**Use in the essay.** The crowd's side of the export story, beside the convoy (WS1): April 1846 at Clonmel the
army guards the mills and the barges; September 1846 at Youghal and Dungarvan crowds try to stop export grain and two
men are shot dead. Two cautions:
- **Nicholson's N2** ("so little plundering was never known in any famine as this; scarcely ever was a bread shop
  disturbed") sits uneasily beside the Dublin bread carts. Both can stand (hers is a general impression, these are
  incidents), but don't let the essay say there was no unrest.
- **Kanturk** is an Examiner report with an edge (the "troublesome mob" buying powder). Quote it as the paper's view,
  not as fact about the crowd.
