# Conditionally White: image hunt (brief for Gemini Antigravity)

Bryan runs this himself in Gemini Antigravity, as a separate task. Paste everything below the line into a new
Antigravity session opened on the ProofEr repo.

Built from the piece's brief (§12 imagery directive, and the images each chapter calls for), the draft outline
(`outline.md`) and the research fact sheets (`research/fact-sheets/`). Claude did not search for or open any image:
every title, date, artist and holder below is a **lead to confirm**, not a checked fact. Rows marked **check** carry a
specific doubt.

---

## Task

Find, licence-check and download the images below for the data essay "Conditionally White" (the Irish, whiteness
and the Great Famine), in the repo `bpmdata/proofer`, piece folder `proj/conditionally-white/`.

For every image:
1. Find the **highest-resolution file the holding institution itself offers** (its open-access download or IIIF
   image): National Library of Ireland (catalogue.nli.ie), Library of Congress (loc.gov), British Library, National
   Portrait Gallery London, National Gallery of Ireland, Trinity College Dublin (Down Survey), National Library of
   Australia (Trove), State Library of NSW, New York Public Library Digital Collections, HathiTrust, Internet Archive.
   Use Wikimedia Commons only where the institution offers nothing, and then pick the largest file whose own Commons
   page shows a public-domain or open licence tag.
2. Open the file's own page and record its licence or public-domain status as written. Never assume.
3. Save the original download, unchanged, to `proj/conditionally-white/img/src/<slug>.<ext>` (slug given below).
4. Add a row to `proj/conditionally-white/img/rights.md`: slug · title (as the holder gives it) · date · artist or
   photographer · publication and issue (for cartoons and engravings: magazine, date, page) · holding institution ·
   source page URL · file URL · pixel size · licence or PD tag, as written on the page.
5. Don't make the full/thumb copies yet; the build step will add the tier script (`img/src|full|thumb`, ~2000px q82
   masters, ~640px q72 thumbs).

Rules:
- Captions cite the holding institution and the original publication, never a search engine. Don't use Google
  Lens or any reverse-image search to identify or caption anything.
- Don't download from stock-photo, print-on-demand or poster sites (Alamy, Getty Images, Bridgeman resale pages,
  Etsy, Fine Art America, etc.), and don't use AI-upscaled, colourised or recoloured copies.
- Never use Fandom, Kiddle or IrishCentral image pages as the source or the caption authority. Commons is fine
  only with the file's own licence tag; prefer the institution.
- Cartoons are exhibits: record the exact magazine, date and page so the caption can say where and when it ran.
  If the title or date below is wrong, write what the scan or the holder says.
- Modern photographs (memorials, 1984 and 2023 presidential visits) are not public domain by default. US federal
  government photos (White House photographers) usually are; record the tag. Anything else needs a CC licence and
  an attribution line, or it's left out.
- Famine images are never decorative. For each Mahony sketch, also copy the sentence of his ILN text that says
  where he stood (into `rights.md`, column "artist's note").

---

## Required

| # | Slug | Title | Date | Artist / publication | Likely holder | For | Why it's needed |
|---|---|---|---|---|---|---|---|
| 1 | `punch-irish-frankenstein-1882` | "The Irish Frankenstein" | 20 May 1882 | John Tenniel, *Punch* | Commons / Internet Archive scans of *Punch* vol. 82 | Ch3 bestiary plate | The simianized Irish "monster" after the Phoenix Park murders. **Check:** there is also an 1843 *Punch* "Irish Frankenstein" (O'Connell); get both if you can and record which is which. |
| 2 | `punch-two-forces-1881` | "Two Forces" | 29 Oct 1881 | John Tenniel, *Punch* | Commons / *Punch* vol. 81 scan | Ch3 bestiary plate | Britannia shields Hibernia from an ape-faced Irish "anarchy". The clearest single image of the genre. |
| 3 | `punch-fenian-pest-1866` | "The Fenian-Pest" | 3 Mar 1866 | John Tenniel, *Punch* | Commons / *Punch* vol. 50 scan | Ch3 bestiary plate | Hibernia appeals to Britannia against an apelike Fenian. Early date for the genre. |
| 4 | `punch-irish-tempest-1870` | "The Irish 'Tempest'" (Caliban) | 19 Mar 1870 | John Tenniel, *Punch* | Commons / *Punch* vol. 58 scan | Ch3 bestiary plate | The Irish peasant as Shakespeare's Caliban: the "savage" frame. **Check** the date. |
| 5 | `puck-king-of-a-shantee-1882` | "The King of A-Shantee" | 15 Feb 1882 | Frederick Opper, *Puck* (New York) | Library of Congress (Prints & Photographs, *Puck* cartoons) | Ch3 bestiary plate, the American side | The Irish shanty-dweller drawn as an ape; the pun ties the Irish to Africa (Ashanti). Shows the genre crossed the Atlantic. **Check** artist and date on the LoC record. |
| 6 | `nast-day-we-celebrate-1867` | "The Day We Celebrate" | 6 Apr 1867 | Thomas Nast, *Harper's Weekly* | Library of Congress / HathiTrust *Harper's Weekly* scans | Ch3 bestiary plate, or Ch7 (St Patrick's Day) | Simianized Irish rioters on St Patrick's Day. Links the cartoon genre to the parade beat. |
| 7 | `constable-iberian-negro-1899` | Comparative heads: "Irish Iberian", "Anglo-Teutonic", "Negro" | 1899 | H. Strickland Constable, *Ireland from One or Two Neglected Points of View* (London, 1899) | Internet Archive / HathiTrust scan of the book; Commons | Ch3, the ladder scene | The racial-science "ladder" drawn as faces, with the Irish placed next to the African. The essay's key evidence that the hierarchy was graded, not binary. |
| 8 | `beddoe-races-of-britain-map-1885` | Map or table of the "index of nigrescence" | 1885 | John Beddoe, *The Races of Britain* (Bristol/London, 1885) | Internet Archive / HathiTrust / Wellcome Collection | Ch3 measurement plate | The instrument itself: Beddoe scored the peoples of Britain and Ireland by hair and eye darkness. Get the map plate if the book has one, and the page that defines the index. |
| 9 | `nott-gliddon-types-of-mankind-1854` | Plate comparing "Apollo Belvidere", "Negro" and "Young Chimpanzee" skulls/profiles | 1854 / 1857 | Josiah Nott & George Gliddon, *Types of Mankind* (1854) or *Indigenous Races of the Earth* (1857) | Internet Archive / Wellcome Collection / LoC | Ch3, the ladder scene (context) | The American racial-science ladder the Irish caricatures borrowed from. Used as an exhibit, with its date. **Check** which book has the plate. |
| 10 | `mahony-boy-and-girl-cahera-1847` | "Boy and girl at Cahera" | 20 Feb 1847 | James Mahony, *Illustrated London News* | Commons / NLI / Internet Archive ILN vol. 10 | Ch4 eyewitness plate | Two children digging for potatoes near Skibbereen. The best-known Mahony image. |
| 11 | `mahony-funeral-skibbereen-1847` | "Funeral at Skibbereen" | 20 Feb 1847 | James Mahony, *Illustrated London News* | as above | Ch4 eyewitness plate | A coffinless burial: the scale of death in one frame. |
| 12 | `mahony-woman-begging-clonakilty-1847` | "Woman begging at Clonakilty" | 13 Feb 1847 | James Mahony, *Illustrated London News* | as above | Ch4 eyewitness plate | Mother with a dead infant; Mahony's text says what he saw. Handle with the gravity rules. |
| 13 | `mahony-mullins-hut-scull-1847` | "Mullins's hut at Scull" | probably 20 Feb 1847 (the 13 Feb text has "Harrington's hut" at "Skull"): **check** | James Mahony, *Illustrated London News* | as above | Ch4 eyewitness plate | The cabin interior; pairs with Nicholson's widow-and-dog scene. |
| 14 | `iln-searching-for-potatoes-1849` | "Searching for potatoes in a stubble field" | 22 Dec 1849 | *Illustrated London News* (artist **check**) | Commons / ILN vol. 15 scan | Ch4 (beside the Nicholson widow scene) | The gleaning that the widow in Nicholson's account was doing. |
| 15 | `iln-ejectment-1848` | "The Ejectment" (eviction scene) | 16 Dec 1848 | *Illustrated London News* | Commons / ILN scan | Ch1 conveyor (the ejectment act), or Ch4 | An eviction as the cheap-ejectment acts made routine. **Check** title and date. |
| 16 | `vandeleur-eviction-battering-ram-1888` | Eviction on the Vandeleur estate, Moyasta, Co. Clare (battering ram) | 1888 | Robert French / Lawrence Collection photograph | National Library of Ireland (Lawrence Collection) | Ch1 or Ch6 (eviction/emigration imagery) | The brief's "battering-ram genre": a real photograph of the ram in use. Later than the famine; caption must say 1888. |
| 17 | `iln-emigrants-between-decks-1851` | "Emigration vessel: between decks" | 10 May 1851 | *Illustrated London News* | Commons / ILN scan | Ch6 (the passage) | The coffin-ship interior. **Check** the date. |
| 18 | `down-survey-barony-map` | One Down Survey barony or county map (choose one with clear plantation boundaries, e.g. Co. Tipperary or Co. Louth) | 1655–58 | William Petty's Down Survey | Trinity College Dublin, "The Down Survey of Ireland" project (downsurvey.tcd.ie); Bibliothèque nationale de France holds many originals | Ch1 strip end / Ch2 ledger | The surveying instrument of the Cromwellian confiscation, in its own hand. The essay draws its own modern SVG map; this is the period exhibit. Record the project's reuse terms. |
| 19 | `ulster-plantation-map-1609` | A 1609 escheated-counties map of Ulster (the "Bodley" barony maps) or a period plantation map | 1609–10 | Sir Josias Bodley's survey | The National Archives (UK), MPF series; or PRONI | Ch1 gyre, stop 3 (1609) | A period map of the Ulster plantation. **Check** the holder's reuse terms; if not open, find a PD scan of a 17th-century plantation map instead and record it. |
| 20 | `douglass-daguerreotype-c1847` | Frederick Douglass, earliest daguerreotype | c. 1847–52 (**check**; the brief wants c. 1845) | Unidentified photographer | National Portrait Gallery (Smithsonian), Washington; or LoC; also the 1845 *Narrative* frontispiece engraving | Ch3 counter-quotation / Ch6 close | Douglass at about the age of his 1845–46 Irish tour. If no image from 1845 exists, use the earliest the holder dates, and note the gap. |
| 21 | `oconnell-portrait` | Daniel O'Connell, portrait engraving or painting | 1830s–1840s | e.g. after George Mulvany or Bernard Mulrenin | National Gallery of Ireland / NLI / NPG London | Ch3 and Ch6 (O'Connell–Douglass) | The Liberator who told Irish America "come out of such a land". |
| 22 | `mitchel-photograph` | John Mitchel, photographic portrait | c. 1860s–1870s | e.g. Brady or Brady-Handy studio | Library of Congress (Brady-Handy collection) or NLI | Ch6 route paragraph and Ch7 spine | The essay's exhibit zero. **Check** the LoC record's sitter and date. |
| 23 | `mitchel-last-conquest-page` | Page facsimile: *The Last Conquest of Ireland (Perhaps)*, the page with "The Almighty, indeed, sent the potato blight, but the English created the famine" | Author's Edition, ch. XXIV, **p. 219** (Internet Archive scan `lastconquestofir00mitc`, which matches these page numbers) | John Mitchel | Internet Archive / HathiTrust scan | Ch4 aphorism, Ch7 | The essay quotes it only from a verified edition and page; the facsimile is the receipt. Use the edition and page the fact sheet settles. |
| 24 | `nicholson-annals-widow-page` | Page facsimile: Asenath Nicholson, *Annals of the Famine in Ireland* (New York, 1851), the widow, dog and pot page | 1851 | Asenath Nicholson | Internet Archive / HathiTrust / Google Books scan | Ch4 eyewitness spine | The passage the essay reproduces at length; the page itself is the citation. Page number per `fact-sheets/q17a-nicholson-anchors.md` if present. |
| 25 | `census-1851-satisfactory-page` | Page facsimile: *The Census of Ireland for the Year 1851*, General Report, the page with "on the whole, satisfactory" | 1856 (published) | Census Commissioners | Internet Archive / histpop.org / EPPI (Southampton) | Ch4 quotes wall | The bureaucratic-horror centerpiece; a facsimile makes it undeniable. Page per `fact-sheets/q04-flagged-census.md`. |
| 26 | `devon-digest-table-95` | Page facsimile: the Devon Commission Digest, Table 95 (p. 564), or the page Mitchel cites. Part I is Internet Archive `digestevidencet01kenngoog` (Dublin: Thom, 1847; ch. 12 "Consolidation of Farms", pp. 451–473); p. 564 may be in Part II (`digestevidencet00kenngoog`). Fallback: Mitchel's own p. 72, where he quotes it | 1847–48 | J.P. Kennedy (ed.), *Digest of Evidence taken before Her Majesty's Commissioners of Inquiry into the State of the Law and Practice in respect to the Occupation of Land in Ireland* | Internet Archive / Google Books / HathiTrust | Ch4 (Mitchel's arithmetic) | Only if the fact sheet (`q05`) finds the table. If it doesn't exist as Mitchel describes, skip this row. |
| 27 | `spenser-view-1633-title` | Title page and the starvation passage of *A View of the State of Ireland* in James Ware's edition | 1633 | Edmund Spenser, ed. James Ware (Dublin, 1633) | Internet Archive / EEBO-TCP page images / British Library | Ch1 gyre, stop 2 | The proposal in print, 250 years before 1846. |
| 28 | `spenser-portrait` | Edmund Spenser, portrait | 17th-c. copy of a lost original | unknown artist | Pembroke College Cambridge / NPG London / Commons | Ch1 gyre, stop 2 | The poet-planter. |
| 29 | `trevelyan-portrait` | Sir Charles Edward Trevelyan, photograph or engraving | 1850s–1860s | e.g. Camille Silvy (1860s) | National Portrait Gallery London | Ch4 quotes wall | The Treasury man's face for the wall's lead quote. |
| 30 | `draft-riots-orphan-asylum-1863` | "The riots at New York: the rioters burning and sacking the Colored Orphan Asylum" | 1 Aug 1863 | *Harper's Weekly* | Library of Congress / NYPL / HathiTrust | Ch6 America side | The first installment, collected from children. State plainly in the caption. |
| 31 | `draft-riots-lynching-clarkson-1863` | "Hanging and burning a Negro in Clarkson Street" (or the holder's title) | 8 Aug 1863 | *Illustrated London News* | Commons / ILN vol. 43 scan / NYPL | Ch6 America side | The lynchings, as the period press drew them. Gravity zone: caption states what happened, no adjectives. **Check** title and date. |
| 32 | `castle-hill-1804-watercolour` | "Major Johnston with Quartermaster Laycock, One Sergeant and Twenty-five Privates of the New South Wales Corps defeats two hundred and sixty six armed rebels, 5th March 1804" | 1804 | unknown artist (watercolour) | National Library of Australia | Ch6 Australia side | The Castle Hill rising of Irish convicts. **Settled by research:** no 1804 flag exists in any account (NMA, Dictionary of Sydney, NSW State Archives); "Death or Liberty" was a slogan. This watercolour is the image. |
| 33 | `lambing-flat-roll-up-banner` | The "Roll Up" banner (anti-Chinese, Lambing Flat goldfield) | 1861 | unknown | Lambing Flat Folk Museum, Young, NSW | Ch6 Australia side | The riot's own banner ("Roll Up, Roll Up, No Chinese"), first recorded 18 June 1861. Held by the Young Historical Society Inc., shown at the Lambing Flat Folk Museum (also called Young Historical Museum); two accounts disagree on its maker and size. **Check** whether the museum or an institution (NLA, State Library NSW) publishes an image and on what terms; if not open, skip and record why. |
| 34 | `convict-ship-or-hulk` | A period engraving of a convict ship or prison hulk (e.g. Bermuda or Woolwich hulks, or a VDL convict transport) | 1840s–1850s | e.g. *Illustrated London News* | Commons / State Library NSW / Libraries Tasmania / NLA | Ch6 horse-thief timeline | The ship the family legend ends on. Prefer an Irish or Van Diemen's Land transport of the 1840s. |
| 35 | `reagan-ballyporeen-1984` | President Reagan in Ballyporeen, Co. Tipperary | 3 Jun 1984 | White House photographer | Ronald Reagan Presidential Library (photo archive) | Ch7 diptych, left | The homecoming. US federal government photo: record the PD tag. |
| 36 | `biden-ballina-2023` | President Biden at St Muredach's Cathedral, Ballina, Co. Mayo | 14 Apr 2023 | White House photographer (e.g. Adam Schultz) | White House photo archive (Flickr "The White House", archived) / National Archives (Biden Library) | Ch7 diptych, right | Same script, forty years on. Record the exact licence tag as given (US Government Work / PD). |

## Recommended

| # | Slug | Title | Date | Artist / publication | Likely holder | For | Why it's needed |
|---|---|---|---|---|---|---|---|
| 37 | `punch-missing-link-1862-page` | Page facsimile of *Punch*, "The Missing Link" (text satire: "A creature manifestly between the Gorilla and the Negro... It comes from Ireland") | 18 Oct 1862 | *Punch* | Internet Archive scan of *Punch* vol. 43 | Ch3 bestiary plate | The "missing link" genre in the magazine's own words. **Check** the date and that the wording matches. |
| 38 | `wells-contrasted-faces-1866` | "Contrasted Faces" (Florence Nightingale vs "Bridget McBruiser") | 1866 | Samuel R. Wells, *New Physiognomy* (New York) | Internet Archive / LoC | Ch3 measurement plate | American physiognomy placing the Irish woman below. **Check** source book and date. |
| 39 | `macdonald-discovery-of-blight-1847` | Daniel MacDonald, "An Irish Peasant Family Discovering the Blight of their Store" | 1847 | Daniel MacDonald (painting) | National Folklore Collection, University College Dublin | Ch4 opening | The only painting made during the famine of its arrival. **Check** rights: probably not open; record the terms and skip if not. |
| 40 | `henry-doyle-emigrants-1868` | "Emigrants Leave Ireland" | 1868 | Henry Doyle, in M.F. Cusack, *An Illustrated History of Ireland* | Internet Archive / Commons | Ch6 or Ch7 | The departure scene, as the diaspora later drew it. |
| 41 | `sheet-music-no-irish-need-apply-1862` | Sheet music cover, "No Irish Need Apply" (song) | 1862 | e.g. John F. Poole (words) | Library of Congress (Music Division) | Ch5 NINA claim | The phrase as popular culture in the 1860s, beside the ads count. **Check** title, date and holder. |
| 42 | `nina-newspaper-ad` | A newspaper "No Irish need apply" classified ad, as cited in Fried (2015) or Jensen (2002) | 1850s–1860s | e.g. *New York Sun*, *New York Times* | Chronicling America (LoC) / NYT TimesMachine (rights?) | Ch5 NINA claim | The primary evidence the verdict rests on. Use only an ad the Q10 fact sheet cites, from an open archive (Chronicling America preferred). |
| 43 | `nicholson-portrait` | Asenath Nicholson, engraved portrait | c. 1847–50 | frontispiece of one of her books (**check**) | Internet Archive / NLI | Ch4 eyewitness spine | The chronicler's face, if a period image exists. Skip if none does. |
| 44 | `beddoe-portrait` | John Beddoe, photograph | c. 1880s | unknown | Wellcome Collection / Royal Anthropological Institute / Commons | Ch3 measurement plate | Optional face for the calipers. |
| 45 | `young-ireland-1848-or-mitchel-trial` | An engraving of Mitchel's 1848 trial or of the Young Ireland rising | 1848 | *Illustrated London News* | Commons / ILN scan | Ch6 Mitchel route | Optional, for the route paragraph. |
| 46 | `famine-emigrant-ship-departure-cork` | "Departure of the Tayleur"? or an ILN Cork/Queenstown emigrant departure scene | 1850s | *Illustrated London News* | Commons / ILN scan | Ch6 | Optional emigration image. **Check** a real title before saving; skip rather than guess. |
| 47a | `eureka-flag` | The Eureka flag (Southern Cross) | 1854 | unknown makers | Art Gallery of Ballarat (original); NLA holds a replica | Ch6 Australia side | The real rebellion flag the research found, in place of a Castle Hill flag. Prefer the gallery's own image and terms. |
| 47b | `mitchel-jail-journal-title` | Title page of Mitchel's *Jail Journal*, naming the *Neptune*, Pernambuco and the Cape | 1854 (first book ed., New York) | John Mitchel | Internet Archive / HathiTrust | Ch6 Mitchel route | Shows the Bermuda leg in his own book. |
| 47 | `kelly-jerilderie-letter-page` | A page of Ned Kelly's Jerilderie Letter | 1879 | Ned Kelly (dictated to Joe Byrne) | State Library Victoria | Ch6 Australia side (memory politics) | Only if the outline keeps the Kelly beat; the library publishes the letter. |
| 48 | `bacons-rebellion-engraving` | Engraving of Bacon's Rebellion or the burning of Jamestown (1676) | 19th-c. book illustration | unknown | Library of Congress / NYPL | Ch3, Bacon beat | Visual anchor for the 1676 settler-bondman rebellion before the 1705 response (F98). **Check** the title and artist; skip rather than guess. |
| 49 | `hening-1705-act-page` | Page facsimile of the 1705 "Act concerning Servants and Slaves" (3 Hening 447) | 1823 (Hening *Statutes at Large* vol. 3) | William Waller Hening (ed.) | Internet Archive / HathiTrust | Ch3 ladder (AL8) | Shows the statutory text granting white-only privileges after Bacon's Rebellion. |
| 50 | `faneuil-hall-1840s` | Faneuil Hall, Boston (period engraving) | c. 1830s–1840s | unknown | Library of Congress / NYPL / Boston Public Library | Ch3 (F100) | Where the 1841 Irish Address had its first American reading on 28 Jan 1842. **Check** date and artist. |
| 51 | `garrison-portrait` | William Lloyd Garrison, portrait | c. 1840s–1860s | unknown | Library of Congress / Boston Public Library / National Portrait Gallery | Ch3 / Ch6 (GA1–GA4) | The abolitionist who named "the bargain" in March 1842. |
| 52 | `liberator-masthead-1842` | *The Liberator* masthead or front page | 1842 | William Lloyd Garrison (ed.) | Boston Public Library / Internet Archive | Ch3 / Ch6 (GA1–GA4) | Period newspaper exhibit for Garrison's coverage of Faneuil Hall and Repeal. |
| 53 | `douglass-narrative-frontispiece-1845` | Frontispiece portrait from Douglass's *Narrative* (Dublin 1845/46 edition preferred if available) | 1845–46 | unknown engraver | Library of Congress / Internet Archive | Ch3 / Ch7 (F101) | Complements row 20 (`douglass-daguerreotype-c1847`) with his Dublin-edition tour-era likeness. |
| 54 | `northern-star-1846-01-03` | Page facsimile: *Northern Star*, 3 Jan 1846, p. 5 (Norfolk curry report) | 3 Jan 1846 | *Northern Star* | NCSE (`ncse.ac.uk`) | Ch4 wall (NF1) | Period exhibit of the translated report on the Duke of Norfolk's curry-powder remark to his Sussex labourers. |
| 55 | `punch-norfolk-curry-1845` | *Punch* cartoon on the Duke of Norfolk and curry powder | late 1845–1846 | *Punch* | Commons / Internet Archive *Punch* scans | Ch4 wall (NF1) | Optional companion if a real contemporary *Punch* cartoon on Norfolk's curry remark exists. **Check**; skip if no real cartoon is found. |
| 56 | `iln-food-riots-1846` | Period engraving of an 1846 food riot or attack on a potato store (Dungarvan/Youghal area preferred) | 1846 | *Illustrated London News* | Commons / ILN scan | Ch4 / Ch5 (WS3, K1) | Crowd's-eye counterweight to the export escorts. **Check** the date and title; skip rather than guess. |
| 57 | `fanon-photo` | Frantz Fanon, photograph | c. 1950s–1961 | unknown | institutional or archival holder | Close (F102) | Optional, probably still in copyright: include only if an openly licensed photo exists; otherwise leave the close text-only. |
| 58 | `cesaire-photo` | Aimé Césaire, photograph | c. 1950s | unknown | institutional or archival holder | Close (F102) | Optional, probably still in copyright: include only if an openly licensed photo exists; otherwise leave the close text-only. |

## When you're done

Report: which rows have files, their pixel sizes, each licence, and every row you couldn't fill and why. Don't
change any other file in the repo.
