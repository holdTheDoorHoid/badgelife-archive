---
title: STORE BADGE
id: saintcon-2021-store-badge
layout: badge
parent: Saintcon 2021
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2021
year: 2021
makers:
- name: Jup1t3r
summary: A beginner-level SAINTCON minibadge with two LEDs and a jumper-selectable blink or solid-on mode.
functions: Lights two LEDs (D1, D2); a solder jumper on the back selects blinking (middle+bottom pads) or solid-on (middle+top pads).
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds:
    count: 2
    type: null
    note: Two LEDs (D1, D2); orient with the green dot toward the right of the board.
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=STORE%20BADGE&year=2021
  url: https://minibadge.wiki/?search=STORE%20BADGE&year=2021
  kind: store
images:
- file: assets/images/badges/saintcon-2021/store-badge/8e1bbe65d3.jpg
  source: https://minibadge.wiki/2021.json
  credit: Jup1t3r
  caption: STORE BADGE minibadge, front, showing the dollar-sign cutout artwork and STORE text
  archived: https://web.archive.org/web/20260611101844/http://minibadge.wiki/2021.json
- file: assets/images/badges/saintcon-2021/store-badge/e1b4a495f9.jpg
  source: https://minibadge.wiki/2021.json
  credit: Jup1t3r
  caption: STORE BADGE minibadge, back, showing the LED, resistor, and jumper labels (D1, D2, R1, JP1)
  archived: https://web.archive.org/web/20260611101844/http://minibadge.wiki/2021.json
contact: {}
notes:
- Community sheet lists quantityMade as 0 and leaves category, boardHouse, howToAcquire, and rarity blank; treated here as not stated rather than "zero made."
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=STORE%20BADGE&year=2021
  title: STORE BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2021''.'
- kind: url
  url: https://minibadge.wiki/2021.json
  title: MiniBadge Wiki 2021 data (STORE BADGE record)
  accessed: '2026-09-07'
  note: 'Underlying JSON record behind the minibadge.wiki listing page: soldering instructions, LED count/orientation, jumper behavior, and front/back images.'
  archived: https://web.archive.org/web/20260611101844/http://minibadge.wiki/2021.json
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check against the raw 2021.json record found two unsupported claims that have been corrected: the LEDs were described as "through-hole," but the JSON record never says this and the saved back-of-board photo shows surface-mount LED packages, so "through-hole" was removed from tech.leds.note and the body text. get_one.where claimed the badge was "sold through SAINTCON''s own badge store," but the JSON''s howToAcquire field for this record is actually empty (confirmed by direct fetch of https://minibadge.wiki/2021.json) — that field and the corresponding body sentence have been removed as unsupported. Both saved images were confirmed to be the genuine store-badge-front.png/back.png files for this exact item, but their captions were swapped/wrong (the "front" caption described LED/jumper content that is actually on the back); captions have been corrected to match what each image actually shows. The minibadge.wiki search/listing page itself was independently confirmed to be a client-side
    JS shell with no static content, matching the earlier researcher''s note. Everything remaining in the entry is now supported by the two cited sources. Confidence stays low because only one community data source exists for this item — no maker page, storefront, or press coverage was found.'
last_modified_date: '2026-09-07'
---

The STORE BADGE is a beginner-friendly SAINTCON 2021 minibadge made by Jup1t3r. It's a simple soldering-practice board: two LEDs (D1 and D2) and a single resistor, with no microcontroller.

A three-pad jumper on the back sets the badge's behavior after assembly — bridging the middle and bottom pads makes the LEDs blink, while bridging the middle and top pads holds them solid on. The listing warns builders not to bridge all three pads at once, since that can short the badge and cause problems for the whole board.

Beyond the assembly instructions and the two photos captured here, little else about this badge is documented publicly: quantity made, price, and exact release details were not found in any source checked for this entry.
