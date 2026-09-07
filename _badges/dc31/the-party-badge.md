---
title: The Party Badge
id: dc31-the-party-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Florida Man
  url: https://floridaman.party
- name: Nothingness
  role: PCB art / design (credited on the back of the board, with Industrious Kraken as sponsor)
summary: A toucan-shaped electronic PCB badge sold as admission to the FLORIDAMAN party at DEF CON 31, doubling as a voice-changing novelty toy.
functions: 'Advertised as "Echo, the mystical voice changing toucan": scream into the beak (mic) and altered sound comes out of the tail (onboard speaker). Also served as the paid admission token for the FLORIDAMAN party and its open bar.'
look:
  colors:
  - white
  - gold
  - black
  shape: bird
  themes:
  - bird
  - animal
  - mascot
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: 3-cell AA/AAA holder visible on the reverse of the PCB (exact cell size not confirmed by text sources)
  sao_version: null
get_one:
  price: $110
  price_usd: 110
  quantity: ''
  availability: sold_out
  availability_note: Listed as "Out of stock" on store.floridaman.party as of a September 2023 (post-event) archive snapshot.
  distribution:
  - purchase
  where: Sold through the FLORIDAMAN party's own WooCommerce store (store.floridaman.party), SKU FMB-2023. Purchase included admission to the party and its open bar; the party was held at Margaritaville, Las Vegas, on August 11, 2023.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: floridaman.party
  url: https://floridaman.party
  kind: website
- label: store.floridaman.party (badge product page)
  url: https://store.floridaman.party/product/florida_man-2023-badge/
  kind: store
images:
- file: assets/images/badges/dc31/the-party-badge/577694e38a.png
  source: https://store.floridaman.party/product/florida_man-2023-badge/
  credit: FLORIDAMAN Party / Jonathan Singer
  caption: The Party Badge (Echo the voice-changing toucan), front
- file: assets/images/badges/dc31/the-party-badge/706fee64ae.png
  source: https://store.floridaman.party/product/florida_man-2023-badge/
  credit: FLORIDAMAN Party / Jonathan Singer
  caption: The Party Badge (Echo the voice-changing toucan), back, showing the battery holder and sponsor credit
contact:
  twitter: '@jonathansinger, @infosecanon'
notes:
- The badge grants you entry into the party. You know the party does not start until Florida Man arrives
- The store listed it as the "FLORIDA_MAN 2023 Badge" (SKU FMB-2023); the archive entry keeps the sheet's title, "The Party Badge."
- Product copy called it "Echo, the mystical voice changing toucan," framing the party admission badge as a voice-changer novelty.
- The FLORIDAMAN party is an annual Florida-themed DEF CON party organized by Jonathan Singer (@jonathansinger, @infosecanon); 2023 was its 8th year.
- The back of the PCB credits "Nothingness" for the art/design and "Industrious Kraken" as sponsor.
status: released
sources:
- kind: sheet
  event: dc31
  row: 42
  updated: '2023-06-20'
- kind: url
  url: https://floridaman.party
  title: FLORIDAMAN Party 2026 (current site)
  accessed: '2026-09-06'
  note: Confirms the recurring annual FLORIDAMAN party and organizer Jonathan Singer.
- kind: url
  url: https://web.archive.org/web/20230619140246/https://floridaman.party/
  title: FLORIDAMAN 2023 Party (Wayback Machine capture, June 2023)
  accessed: '2026-09-06'
  note: 2023 party page confirming the badge included event access, date (Aug 11, 2023), venue (Margaritaville, Las Vegas), and that it was the 8th annual party.
- kind: url
  url: https://web.archive.org/web/20230924103027/https://store.floridaman.party/product-category/badges/
  title: Badges | FLORIDA_MAN 2023 (Wayback Machine capture, Sept 2023)
  accessed: '2026-09-06'
  note: Shows the badge listed at $110, marked "Out of stock" after the event, with front/back product photos.
- kind: url
  url: https://store.floridaman.party/product/florida_man-2023-badge/
  title: FLORIDA_MAN 2023 Badge (live product page)
  accessed: '2026-09-06'
  note: Product description ("Echo, the mystical voice changing toucan"), SKU FMB-2023, price $110, source of the front/back images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts (what it is, price, maker, distribution) come from the maker's own storefront copy and site, plus a Wayback Machine snapshot for stock status since the live store no longer lists the 2023 product. Exact battery cell size (AA vs AAA), MCU/voice-IC identity, and LED presence could not be confirmed from available photos or text and are left blank. Manufactured quantity was not stated anywhere found.
last_modified_date: '2026-09-06'
related:
- dc32-florida-man-listed-for-def-con-32-no-details
---

"The Party Badge" was the admission token for the 2023 FLORIDAMAN party, the 8th annual running of an unofficial DEF CON 31 party thrown by Florida-based infosec people at Margaritaville in Las Vegas on August 11, 2023. Rather than a plain paper ticket, organizer Jonathan Singer (who runs the party under the handles @jonathansinger and @infosecanon) sold a $110 electronic novelty badge shaped like a toucan and marketed as "Echo, the mystical voice changing toucan" — scream into the beak and a distorted version comes out of the tail-mounted speaker. The PCB's silkscreen credits "Nothingness" for the artwork/design and "Industrious Kraken" as a sponsor.

The badge doubled as proof of purchase: owning one got you into the party and its open bar. It was sold directly through the party's own WooCommerce store (SKU FMB-2023) and was marked out of stock shortly after the event. No hardware or firmware files were found, and there is no indication the design was released as open source.

The board carries a 3-cell battery holder and several push buttons on the back, but the exact battery size and the identity of the socketed chip on the front (visible in photos but unlabeled in any source found) could not be confirmed from text sources, so those fields are left blank rather than guessed.
