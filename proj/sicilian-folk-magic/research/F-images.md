# Group F: images (open-licensed candidates for the cutout look)

Research worker report, 2026-11-23. Prompt: `prompts.md`, Group F.
No images were downloaded. Every row was checked by opening the museum's own object page; the "License" column
says what that page states. Image URLs are the ones the object page itself exposes (Met: its IIIF "main-image"
link; Rijksmuseum: its micr.io IIIF link; Wellcome: its IIIF link). Where no file URL was shown, the cell says
"page only".

**How the license bases read**
- **Met (The Metropolitan Museum of Art):** object page labelled "Public Domain"; under the Met's Open Access
  policy those images are released CC0. Rows where the Met page did *not* show the label are left out (listed in
  "Rejected" below).
- **NGA (National Gallery of Art, Washington):** object page states "This object's media is free and in the public
  domain" and links the NGA Open Access policy (CC0 for open-access images). NGA pages did not expose a direct
  file URL to the fetcher; download is from the page's Media Options.
- **Rijksmuseum:** object page states "Public domain" with the Creative Commons Public Domain Mark 1.0.
- **Wellcome Collection:** object page shows "Public Domain Mark" and "You can use this work for any purpose
  without restriction under copyright law."
- **DIA (Detroit Institute of Arts):** object page states "Public Domain".
- **Walters Art Museum:** the object pages fetched did **not** state a license. Walters is generally known as an
  open-access (CC0) museum, but that was not confirmed on these pages, so both Walters rows are flagged VERIFY.

**Cut-out rating** (A = clean silhouette on a plain, gold or dark ground, or a museum object photo on a neutral
backdrop; B = figure separable with some masking work; C = a scene, use whole as a framed panel, not a puppet).
Ratings come from each page's own description plus the work's known format (gold-ground panel, object photo,
print on white). The images themselves were not viewed, so **check each one before committing**.

## Candidates

### Saint Rosalia (Palermo)

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 1 | Saint Rosalie Interceding for the Plague-stricken of Palermo | Anthony van Dyck | 1624 | Met (71.41) | Public Domain → CC0 (Met OA) | https://www.metmuseum.org/art/collection/search/436257 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/436257/2004265/main-image | B: the saint floats in clouds over the city; she and the putti can be masked out, and the city becomes a backdrop layer |
| 2 | The Virgin and Saint Rosalia Interceding with Christ | Carlo Maratti | 1625–1713 (artist's life) | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/340744 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/340744/760886/main-image | B: pen sketch on bare paper; easy to lift, but loose line |
| 3 | Saint Rosalia Crowned by the Child Jesus | Paulus Pontius after van Dyck | 17th c. | NGA (2008.91.3) | "free and in the public domain" (NGA OA) | https://www.nga.gov/artworks/141204-saint-rosalia-crowned-child-jesus | page only | B: engraving; figures can be cut from the hatched ground |
| 4 | Saint Rosalia (engraving) | P. Pontius after van Dyck | 17th c. | Wellcome | Public Domain Mark | https://content.www.wellcomecollection.org/works/dyt5b7g7 | page only | B: second impression of #3; use whichever scan is sharper |
| 5 | Saint Rosalia (etching) | W. Unger after van Dyck | 19th c. | Wellcome (7142i) | Public Domain Mark | https://preview.wellcomecollection.org/works/taje8c8z | page only | B |
| 6 | Heilige Rosalia | Cornelis de Bout, after an anonymous design | plate 1675–1735; impression 1930–42 | Rijksmuseum (RP-P-1942-122) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/Heilige-Rosalia--665441b93f3dd33223f7dcae59971cda | https://iiif.micr.io/BoVkC/full/^1024,538/0/default.webp | B: oval half-length with skull and branch. Note: modern pull from an old plate; Rijksmuseum still marks it PD |

### Rosalia's feast (the Festino) and Palermo

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 7 | The car of Saint Rosalia (colour aquatint) | J.P.L.L. Houël | 1780s | Wellcome (7145i) | Public Domain Mark | https://content.www.wellcomecollection.org/works/r9fx7s46 | page only | A/B: the triumphal float is one big shape, a ready-made parade puppet |
| 8 | The car of Saint Rosalia (aquatint) | W. Daniell, after another artist's drawing | 4 June 1823 | Wellcome (7144i) | **VERIFY:** the fetched page showed no license line, though its sister items carry PDM | https://preview.wellcomecollection.org/works/njgva6a3 | page only | A/B: second view of the float |
| 9 | View of the Portal and Principal Entrance of the Cathedral of Palermo during the Festival of Sta. Rosalia | Louis Jean Desprez | n.d. (c. 1780s) | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/336850 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/336850/755094/main-image | C: a festival stage set, good as a backdrop or proscenium |
| 10 | Voyage pittoresque… des royaumes de Naples et de Sicile (plate shown: Vuë Perspective du Port de Messine) | Saint-Non, with designs by Fragonard, Hubert Robert and others | 1781–86 | Met (1994.219) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/365649 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/365649/1475627/main-image | C: backdrop; the book has more Sicilian plates worth browsing |
| 11 | Twee inwoners van Sicilië (Blaise Motta "the Cyclops"), plate 116 of Voyage pittoresque des isles de Sicile | J.P.L.L. Houël | 1782–87 | Rijksmuseum (RP-P-1999-1711) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/Twee+inwoners+van+Sicilië--37c196eaedd4ad9cc51d4770ad4a0ba3 | https://iiif.micr.io/FVHYz/full/^1024,538/0/default.webp | B: Rijksmuseum holds the Houël series (264 plates); search it there for Rosalia and Agatha plates |
| 12 | Gezicht op de catacomben van de Kapucijnen te Palermo | anonymous wood engraving (Nederlandsch Magazijn) | 1837 | Rijksmuseum (RP-P-2018-3421) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/Gezicht-op-de-catacomben-van-de-Kapucijnen-te-Palermo--ff75abda41fe3cdfbb8e93f094a73f3c | https://iiif.micr.io/NWyRl/full/^1024,538/0/default.webp | C: memento-mori backdrop |
| 13 | Interieur van de crypte van de kapucijnen te Palermo (albumen photo) | Giorgio Sommer | c. 1860s–1914 | Rijksmuseum (RP-F-F16850) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/RP-F-F16850--b0b7465ac373ff96c1f300afa075a547 | https://iiif.micr.io/BXSYD/full/^1024,538/0/default.webp | C: a 19th-c. photo of the dead (mummies), no living people. Strong, but use with tact |

### Saint Agatha (Catania)

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 14 | Saint Agatha (bronze statuette) | Italian, probably Naples | mid-17th c. | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/197071 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/197071/1580050/main-image | A: full-figure baroque statuette, object photo; top pick |
| 15 | Saint Agatha | Bernardo Cavallino | 1640s | DIA (45.508) | "Public Domain" (DIA page) | https://dia.org/collection/saint-agatha-36681 | page only | B: Neapolitan baroque half-length, probably on a dark ground; confirm on the image |
| 16 | St. Agatha | Francesco Furini | 17th c. (Florence) | Walters (37.1839) | **VERIFY:** not stated on page | https://art.thewalters.org/detail/34385 | page only | A/B: the page says sfumato figure "out of a dark background", with pincers and palm |
| 17 | Saints Catherine of Alexandria, Barbara, Agatha, and Margaret | Giovanni di Paolo | c. 1470 | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/436514 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/436514/795048/main-image | A: gold ground, standing figures; Agatha can be lifted out alone |
| 18 | Martyrdom of Saint Agatha in an Initial D | Sano di Pietro | c. 1470–73 | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/461122 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/461122/913344/main-image | C: illuminated initial, a ready-made drop cap |
| 19 | Saint Agatha (drawing) | Paul Flandrin | 19th c. | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/337085 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/337085/755718/main-image | A: graphite outline on tracing paper, nearly a cut line already |
| 20 | S. Agatha (with the dish of breasts) | Pieter de Bailliu I | 1623–60 | Rijksmuseum (RP-P-OB-22.552) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/Heilige-Agatha-met-schaal-met-afgesneden-borsten--5857ebae0f627694040ee9fb880abb6b | https://iiif.micr.io/Inloi/full/^1024,538/0/default.webp | B: tall full-figure print (225×116 mm) |
| 21 | S. Agatha | Schelte à Bolswert after Rubens | 17th c. | Rijksmuseum (RP-P-BI-2530) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/RP-P-BI-2530--6e3af277682607c225cb5eb6029330e0 | https://iiif.micr.io/GuRKe/full/^1024,538/0/default.webp | B: pairs with #26, the same series' Lucy |
| 22 | Heilige Agatha vastgebonden aan boom | anonymous, after Marcantonio Raimondi | 1500–75 | Rijksmuseum (RP-P-OB-11.886) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/RP-P-OB-11.886--e895eff4b1e21b72da31a00e0f3ffaf1 | https://iiif.micr.io/jkbIr/full/^1024,538/0/default.webp | B: tiny (82 mm), so scan resolution may limit it |

### Saint Lucy (Syracuse)

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 23 | Saint Lucy | Francisco de Zurbarán | c. 1625/30 | NGA (1943.7.11) | "free and in the public domain" (NGA OA) | https://www.nga.gov/artworks/12209-saint-lucy | page only | A: dark brown ground, eyes on a plate, palm, flower crown; top pick |
| 24 | Saint Lucy | Francesco del Cossa | c. 1473/74 | NGA (1939.1.228) | "free and in the public domain" (NGA OA) | https://www.nga.gov/artworks/369-saint-lucy | page only | A: gold ground, holds the eyes on a flower-like stem, which is wonderfully odd |
| 25 | Saint Lucy | Francesco Zaganelli | c. 1500 | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/437957 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/437957/798340/main-image | A: gold-ground panel |
| 26 | S. Lucia (with dagger) | Schelte à Bolswert after Rubens | 17th c. | Rijksmuseum (RP-P-BI-2538) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/RP-P-BI-2538 | https://iiif.micr.io/KJZSk/full/^1024,538/0/default.webp | B |
| 27 | Heilige Lucia met twee ogen op bord | anonymous, after Marcantonio Raimondi | 1500–75 | Rijksmuseum (RP-P-OB-11.898) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/RP-P-OB-11.898--db7c7d386b628e7ea3bad432f77f2f43 | https://iiif.micr.io/PtFdn/full/^1024,538/0/default.webp | B: tiny (81 mm) |
| 28 | The Martyrdom of Saint Lucy (altarpiece wing) | Master of the Figdor Deposition | c. 1505–10 | Rijksmuseum (SK-A-1688) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/SK-A-1688 | https://iiif.micr.io/zMHpz/full/^1024,538/0/default.webp | C: crowded narrative with oxen, pyre and sword; mine it for small props |
| 29 | Saint Lucy | Sienese, mid-14th c. (once given to Simone Martini) | mid-14th c. | Walters (37.756) | **VERIFY:** not stated on page | https://art.thewalters.org/detail/37.756 | page only | A: gold-ground altarpiece wing with lamp and dagger |

### Saint Joseph (the March 19 tables)

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 30 | St. Joseph (crèche figure) | attrib. Salvatore di Franco, Naples | 2nd half 18th c. | Met (64.164.3a–c) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/204104 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/204104/467959/main-image | A+: a real poseable puppet (wire body, terracotta head) in an object photo; ideal for the look |
| 31 | Saint Joseph (statuette) | probably Quito, Ecuador | 2nd half 18th c. | Met (64.164.213) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/204309 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/204309/411884/main-image | A: polychrome and gilt object photo. Useful for the Sicilian/Latino side note: same crèche gift as #30, a Latin American Joseph |
| 32 | Saint Joseph and the Christ Child | Domenico Maria Viani | 1690s | NGA (2000.140.2) | "free and in the public domain" (NGA OA) | https://www.nga.gov/artworks/117675-saint-joseph-and-christ-child | page only | A/B: the page says "plain background", in an oval |
| 33 | Saint Joseph with the Christ Child | Paul Troger | c. 1720 | NGA (2012.135.1) | "free and in the public domain" (NGA OA) | https://www.nga.gov/artworks/160530-saint-joseph-christ-child | page only | B: foliage behind |
| 34 | Saint Joseph and the Infant Jesus | Giuseppe Bottani | mid-18th c. | NGA (2015.4.2) | "free and in the public domain" (NGA OA) | https://www.nga.gov/artworks/168779-saint-joseph-and-infant-jesus | page only | B: radiant halo, textured ground |

### Demeter / Ceres and Persephone / Proserpina (Sicily's own goddesses)

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 35 | Two terracotta busts (Persephone or Demeter), Greek, Sicilian | Greek, Sicilian | 4th c. BCE | Met (1994.600.1–.2) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/256204 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/256204/2012076/main-image | A: votive busts made in Sicily, object photo; top pick for the "before the saints" beat |
| 36 | Ten marble fragments of the Great Eleusinian Relief (Demeter, Persephone, Triptolemos) | Roman copy of a Greek original | c. 27 BCE–14 CE | Met (14.130.9) | Public Domain → CC0 | https://www.metmuseum.org/toah/works-of-art/14.130.9 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/248899/540132/main-image | B: relief figures; each goddess can be masked out |
| 37 | Ceres (Summer) | Antoine Watteau | c. 1717/18 | NGA (1961.9.50) | "free and in the public domain" (NGA OA) | https://www.nga.gov/artworks/46149-ceres-summer | page only | B: on clouds in a pale sky, wheat crown, sickle; soft edges |
| 38 | Plate 14: Ceres in a niche | Giovanni Jacopo Caraglio after Rosso Fiorentino | 1526 | Met (49.97.235) | Public Domain → CC0 | https://metmuseum.org/art/collection/search/368136 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/368136/784919/main-image | A: full standing figure in a niche with sickle and torch; the niche is a built-in cut line |
| 39 | Proserpina met bloemen (Gods and Goddesses 8/20) | Jacob Binck after Caraglio | 1530 | Rijksmuseum (RP-P-1951-178H) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/RP-P-1951-178H--d7f6c6cb3553538faa8975a2fded717f | https://iiif.micr.io/UnOJg/full/^1024,538/0/default.webp | A: single standing figure in a niche; pairs with #38 |
| 40 | Ceres (Women from Classical Mythology 4/6) | Nikolaus Solis | 1552–84 | Rijksmuseum (RP-P-OB-54.337) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/RP-P-OB-54.337 | https://iiif.micr.io/BEeLW/full/^1024,538/0/default.webp | B: very small (56 mm) |
| 41 | The Cult of Ceres | Jan Saenredam after Goltzius | 1596 | NGA (2012.92.606) | "free and in the public domain" (NGA OA) | https://www.nga.gov/artworks/154029-cult-ceres | page only | C: a crowded scene |
| 42 | Without Ceres and Bacchus, Venus Would Freeze | Jacob Matham after Goltzius | 1588 | NGA (2011.139.17) | "free and in the public domain" (NGA OA) | https://www.nga.gov/artworks/156038-without-ceres-and-bacchus-venus-would-freeze | page only | B: Ceres with her cornucopia separable |
| 43 | Rape of Proserpina (porcelain group) | Gaspero Bruschi after Foggini, Doccia | c. 1750 | Met (1997.377) | Public Domain → CC0 | https://www.metmuseum.org/toah/works-of-art/1997.377 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/208847/487753/main-image | A: a baroque sculpture group in an object photo; the abduction near Enna as a puppet |
| 44 | Rape of Persephone with Pluto on horseback at right | Giuseppe Scolari | 1590–1607 | Met (22.73.3-152) | Public Domain → CC0 | https://metmuseum.org/art/collection/search/361899 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/361899/1551548/main-image | B/C: bold woodcut with flames from the chasm; great graphic texture |
| 45 | Roof van Proserpina | Cornelis Cort after Frans Floris | 1565 | Rijksmuseum (RP-P-1983-10) | Public Domain Mark 1.0 | https://www.rijksmuseum.nl/en/collection/object/RP-P-1983-10--791a551e57e82ce01cd25898ef9cc7fe | https://iiif.micr.io/jIWYV/full/^1024,538/0/default.webp | C: scene with a chariot by a forest |

### Isis

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 46 | Statuette of Isis nursing Horus | Egyptian | Late Period, 664–332 BCE | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/553002 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/553002/2533573/main-image | A: full-figure bronze in an object photo; the visual rhyme with Madonna and Child |
| 47 | Statuette of Isis with the infant Horus (faience) | Egyptian | Ptolemaic, 332–30 BCE | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/548310 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/548310/1214471/main-image | A: turquoise faience, which reads well small |
| 48 | Isis and Horus (cupreous metal) | Egyptian | 664–30 BCE | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/570685 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/570685/1214152/main-image | A |

### Majolica (Sicilian maiolica) and tiles

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 49 | Albarello | Lazzaro workshop, Palermo | 2nd half 16th c. | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/188537 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/188537/1614048/main-image | A: object photo, and the only firmly Palermo-made piece here; crop its band for pattern swatches |
| 50 | Pharmacy jar (albarello) | possibly Sicily | dated 1551 | Met (02.5.18) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/188536 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/188536/1614045/main-image | A |
| 51 | Albarello | Sicily | 16th c. | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/188538 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/188538/1614051/main-image | A |
| 52 | Albarello | Sicily or Faenza | 2nd half 16th c. | Met (02.5.21) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/188539 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/188539/1614052/main-image | A |
| 53 | Pharmacy jar (albarello) | Castel Durante or Sicily | c. 1540–50 | Met (02.5.22) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/188540 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/188540/1614053/main-image | A |
| 54 | Albarello | probably Vincenzo di Marco, Sicily or Faenza | 2nd half 16th c. | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/197222 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/197222/1616927/main-image | A |
| 55 | Albarello | probably Vincenzo di Marco, Sicily or Faenza | 2nd half 16th c. | Met | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/197224 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/197224/1616768/main-image | A |
| 56 | Tile with corner edge | Italian, Rome | c. 1617–27 | Met (2012.93) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/238925 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/238925/1564127/main-image | A: an Italian baroque-era tile, flat and tileable. Not Sicilian |

### Baroque frames and ornament

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 57 | Gilt ripple frame | Sicilian(?) per the Met | late 17th c. | Met (1975.1.2326) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/461318 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/461318/915603/main-image | A: an empty frame object photo with gilt over orange-red bole; a ready overlay |
| 58 | Salvator Rosa frame | Naples | late 17th c. | Met (1975.1.2197) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/461030 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/461030/916510/main-image | A: dark ebonized moldings |
| 59 | Palatina-style Salvator Rosa frame | Southern Italy | late 17th c. | Met (1975.1.2176) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/461635 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/461635/916460/main-image | A |
| 60 | Cassetta frame (crystal, lapis, niello) | Rome, in early-17th-c. style | 1880–1900 | Met (1975.1.2292) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/461189 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/461189/916492/main-image | A: jewel-box look; note it's a 19th-c. revival |

### Reliquaries and crèche figures

| # | Title | Artist | Date | Holder | License (basis) | Page stating license | Image file URL | Cut-out |
|---|---|---|---|---|---|---|---|---|
| 61 | Reliquary bust of a bishop-saint (gilt bronze) | Italian, possibly Rome | early 17th c. | Met (68.141.5) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/204848 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/204848/1579671/main-image | A: post-Tridentine relic cult, the right era |
| 62 | Reliquary Bust of Saint Juliana | circle of Giovanni di Bartolo | c. 1376 | Met (61.266) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/471908 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/471908/956196/main-image | A: female saint bust, a stand-in for the Agatha bust type. Not Sicilian |
| 63 | Reliquary of Mary Magdalene (with a tooth) | Tuscany | 14th–15th c. | Met (17.190.504) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/464469 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/464469/1635809/main-image | A |
| 64 | Angel (crèche figure) | Naples | 2nd half 18th c. | Met (64.164.16a–c) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/204117 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/204117/1657167/main-image | A+: a hanging angel puppet |
| 65 | Angel (crèche figure) | Naples | 2nd half 18th c. | Met (64.164.12a–c) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/204113 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/204113/1657163/main-image | A+ |
| 66 | Angel (crèche figure) | Naples | 2nd half 18th c. | Met (64.164.28a–c) | Public Domain → CC0 | https://www.metmuseum.org/art/collection/search/204129 | https://collectionapi.metmuseum.org/api/collection/v1/iiif/204129/1658690/main-image | A+ |

### Ex-votos (painted thank-you panels; Italian, not confirmed Sicilian)

All Wellcome, Public Domain Mark, "an Italian painter". These are scenes: use each whole as a framed panel (C),
or cut the hovering saint or Madonna out of the top corner (B).

| # | Title | Date | Ref | Page stating license | Image file URL |
|---|---|---|---|---|---|
| 67 | A woman appealing to Christ, to Sansovino's Virgin and Child and to Saint Nicholas on behalf of her child | early 19th c. | 44888i | https://content.www.wellcomecollection.org/works/c2gx372n | https://iiif.wellcomecollection.org/image/V0017436/full/full/0/default.jpg |
| 68 | Angelo Loerch, being run over by a horse and carriage, makes a vow to the Madonna del Parto | 1883 | 44952i | https://wellcomecollection.org/works/jnkbky3g | thumbnail only: https://iiif.wellcomecollection.org/thumbs/b12027649_0001.jp2/full/!200,200/0/default.jpg |
| 69 | A person praying to the Virgin for the recovery of a child lying sick in bed | 1700–99 | 44953i | https://wellcomecollection.org/works/mtmtcmrk | thumbnail only: https://iiif.wellcomecollection.org/thumbs/b12027650_0001.jp2/full/!200,200/0/default.jpg |
| 70 | A woman praying for a child, with intercessors in a fire | 1887 | 44883i | https://wellcomecollection.org/works/qqnpsxe7 | thumbnail only: https://iiif.wellcomecollection.org/thumbs/b12026955_0001.jp2/full/!200,200/0/default.jpg |
| 71 | A man praying to Sansovino's Virgin and Child | n.d. | 44879i | https://wellcomecollection.org/works/zsa7x85f | https://iiif.wellcomecollection.org/image/V0017427/full/800%2C/0/default.jpg |
| 72 | Ernesto Jagovaggi ill in bed, two women praying for his recovery, 27 October 1866 | 1866 | 44871i | https://wellcomecollection.org/works/vkuyhr72 | https://iiif.wellcomecollection.org/image/V0017419/full/800%2C/0/default.jpg |
| 73 | A miraculous cure described in the New Testament | n.d. | 44904i | https://wellcomecollection.org/works/rmqggcmd | https://iiif.wellcomecollection.org/image/V0017452/full/800%2C/0/default.jpg |

**Count:** 73 rows. 70 have a license confirmed on the holder's own page; 3 are flagged VERIFY (#8, #16, #29).
#6 is marked PD by the Rijksmuseum but is a modern impression from an old plate (noted).

## Top picks for puppets
Choose these first, because they are already objects photographed on plain grounds, or figures on gold or dark
grounds: #30 St Joseph crèche figure, #64–66 Neapolitan angels, #14 bronze Agatha, #23 Zurbarán Lucy, #24 Cossa
Lucy, #17 Giovanni di Paolo saints, #38/#39 Caraglio and Binck goddesses in niches, #35 Sicilian Persephone busts,
#43 Doccia Proserpina group, #46–48 Isis statuettes, #7 Rosalia's float, #57 Sicilian(?) gilt frame.
The crèche figures are literally puppets, with wire bodies made to be posed, which fits the brief exactly.

## Gaps and notes
- **Sicilian tile panels (riggiole, Caltagirone or Palermo wall panels):** none found in an open-licensed collection.
  The best open stand-ins are the Palermo and Sicily albarelli (#49–55) for pattern, plus the Roman tile (#56).
  Caltagirone and Palermo tiles appear mostly in dealer listings and on Google Arts & Culture (not open-licensed),
  and in the V&A (its image terms are non-commercial, so not used here).
- **Sicilian ex-votos specifically:** the Wellcome set is Italian, with no Sicilian provenance stated. A US National
  Library of Medicine exhibit page shows Sicilian ex-votos from Trecastagni and Catania (1927–48), but the images
  are credited "Courtesy Giuseppe Maimone Editore, Catania and Mario Alberghina". That is not an open license, so
  it is a lead only, not a candidate.
- **Science Museum Group (London)** holds many Italian maiolica ex-voto plaques (Deruta, "P.G.R." = *per grazia
  ricevuta*, "by grace received"). Its pages release only the data as CC0 and the text as CC BY; no image license
  was stated, so the images weren't counted.
- **Baroque church interiors of Sicily:** only 19th-c. photos (#13) and festival views (#9, #10) were found. The
  Rijksmuseum lists 19th-c. Palermo Cathedral photos by Rive, Incorpora and Crupi (not individually checked).
- **Houël, Voyage pittoresque des isles de Sicile (1782–87):** the Rijksmuseum holds the plates PD (#11), and so
  does Wellcome (#7). That series is the richest single source of period Sicilian feasts, rites and catacombs, so
  browse it on rijksmuseum.nl for Agatha and Rosalia plates. The NGA owns the bound volumes but shows no images.
- **Latino side note:** #31 (a Quito St Joseph, in the same Met crèche gift as the Neapolitan figures) is the one
  open-licensed bridge found. Mexican tin retablos were not reached (see below).
- Left out: Met prints whose pages showed no PD label and no image (Cort's Martyrdom of St Agatha, La Placa's
  *La Reggia in Trionfo* 1736, the Guidi Ceres, Le Pautre's Proserpina, the Domenichi frame design, the Picart
  cartouche); Met 257439 (restituted in 2022, image restricted); Met 20th-c. French tiles (restricted); Walters
  and DIA image files (not exposed).

## What was tried
- Met, NGA, Rijksmuseum, Wellcome, DIA and Walters object pages: read through the page fetcher.
- Art Institute of Chicago (Saint Agatha, Saints Lucy and Barbara): pages refused the fetch. Counted as tried.
- Direct APIs (Met, AIC, Cleveland, Europeana, Getty, Wikimedia Commons, NGA) were blocked by this environment's
  network proxy. Wikimedia Commons, Europeana and Getty were not otherwise reached.
- The shared web-search budget ran out before searches for Mexican retablos, Cooper Hewitt tiles, Rijksmuseum
  Italian tiles and Europeana could run. A follow-up pass could cover those, plus the Houël plates on
  rijksmuseum.nl.
- Nothing from the video game *Rock of Ages* was used, and there are no photos of living people.
