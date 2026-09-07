---
title: HALLWAY TALK'S BADGE
id: saintcon-2023-hallway-talk-s-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: SHIFTY
summary: 'A single-LED SAINTCON 2023 minibadge for the "Hallway Talks" interview series, showing a chameleon holding a microphone.'
functions: 'Passive lanyard minibadge with one LED (D1) driven through a single resistor (R1); no other electronics.'
look:
  colors: [green, white, copper]
  shape: rectangle
  themes: [animal, mascot, text]
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single surface-mount LED (D1) in series with one surface-mount resistor (R1); user-soldered.
  display: none
  connectivity: []
  battery: null
  power: null
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: "Handed out in person at SAINTCON 2023 by finding the Hallway Talks team in the hallways."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=HALLWAY%20TALK%27S%20BADGE&year=2023
  url: https://minibadge.wiki/?search=HALLWAY%20TALK%27S%20BADGE&year=2023
  kind: website
- label: minibadge.wiki data export (2023.json)
  url: https://minibadge.wiki/2023.json
  kind: doc
images:
  - file: assets/images/badges/saintcon-2023/hallway-talk-s-badge/68551baa1f.jpg
    source: "https://minibadge.wiki/data/"
    credit: "SHIFTY / Minibadge Wiki"
    caption: "Front of the HALLWAY TALK'S BADGE minibadge"
  - file: assets/images/badges/saintcon-2023/hallway-talk-s-badge/9d3fc896a4.jpg
    source: "https://minibadge.wiki/data/"
    credit: "SHIFTY / Minibadge Wiki"
    caption: "Back of the HALLWAY TALK'S BADGE minibadge"
contact: {}
notes:
- 'category: Event; rarity: Uncommon'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=HALLWAY%20TALK%27S%20BADGE&year=2023
  title: HALLWAY TALK'S BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2023''.'
- kind: url
  url: https://minibadge.wiki/2023.json
  title: Minibadge Wiki 2023 data export
  accessed: '2026-09-07'
  note: "The site's search page is client-rendered with no server-side results; the underlying 2023.json data export (linked from minibadge.wiki/data/) has the actual record: maker SHIFTY, description, soldering instructions (LED + resistor, single-pad hand soldering), category Event, rarity Uncommon, quantityMade recorded as 0 (not stated), and how-to-acquire text (find the maker in the hallways)."
- kind: url
  url: https://minibadge.wiki/images/2023/hallway-talks-badge-front.png
  title: Hallway Talks badge - front image
  accessed: '2026-09-07'
  note: Front photo of the badge, saved locally.
- kind: url
  url: https://minibadge.wiki/images/2023/hallway-talks-badge-back.png
  title: Hallway Talks badge - back image
  accessed: '2026-09-07'
  note: Back photo of the badge showing the D1 LED and R1 resistor placement, saved locally.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Fact-check pass (2026-09-07): re-fetched the minibadge.wiki 2023.json export directly and confirmed maker, description, category (Event), rarity (Uncommon), quantityMade (0, unset), and how-to-acquire text verbatim. Both saved images were re-downloaded from minibadge.wiki/images/2023/ and are byte-identical in content to the source, and the back image confirms exactly one LED (D1) and one resistor (R1). Corrected one error found by inspecting the back image: the LED and resistor are surface-mount components (visible flat SMD packages), not through-hole as the initial pass stated. Also removed tech.power ('powered by host badge'), which was an uncited inference rather than something stated by any source -- per the research guide, unsupported fields are left blank rather than kept with a caveat. All facts come from the minibadge.wiki 2023 JSON data export, not from the maker's own page (SHIFTY has no separate storefront, Hackaday, or repo found). No design files, BOM, or EDA tool were found; make_your_own left empty rather than guessed. Everything remaining in the entry is now supported by a source actually read."
last_modified_date: '2026-09-07'
---

The HALLWAY TALK'S BADGE is a 2023 SAINTCON minibadge made by SHIFTY for "Hallway Talks," an interview series that covers the behind-the-scenes effort of running SAINTCON. The badge's green PCB carries a chameleon mascot holding a microphone over the word "TALKS," with a single LED (D1) and a matching resistor (R1) as its only components -- both meant to be hand-soldered by the recipient using the single-pad technique, along with the pin headers that let it clip onto a minibadge lanyard chain.

It was not sold; attendees got one for free by finding the Hallway Talks team in the hallways of the convention and talking to them, which is also the joke behind the name. The minibadge.wiki community database lists it under the "Event" category with "Uncommon" rarity, but does not give a quantity made, and no separate maker storefront, repository, or build files for it were found.
