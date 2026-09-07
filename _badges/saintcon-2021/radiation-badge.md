---
title: RADIATION BADGE
id: saintcon-2021-radiation-badge
layout: badge
parent: Saintcon 2021
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2021
year: 2021
makers:
- name: Jup1t3r
summary: A beginner-friendly SAINTCON 2021 minibadge with three LEDs and a solder-jumper mode select for blinking or solid-on.
functions: 'Three LEDs light up in a blink or solid-on mode, selected by which pair of jumper pads the builder solders.'
look:
  colors: []
  shape: null
  themes:
  - radio
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: Triangle-cutout LEDs; light-emitting side faces the board, aligned to a matching silkscreen shape.
  display: none
  connectivity: []
  battery: null
  sao_version: none
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
- label: minibadge.wiki/?search=RADIATION%20BADGE&year=2021
  url: https://minibadge.wiki/?search=RADIATION%20BADGE&year=2021
  kind: website
images:
- file: assets/images/badges/saintcon-2021/radiation-badge/37ca5091ac.jpg
  source: "https://minibadge.wiki/?search=RADIATION%20BADGE&year=2021"
  credit: "Jup1t3r"
  caption: "Front of the Radiation Badge, SAINTCON 2021 minibadge"
- file: assets/images/badges/saintcon-2021/radiation-badge/e7c30e3773.jpg
  source: "https://minibadge.wiki/?search=RADIATION%20BADGE&year=2021"
  credit: "Jup1t3r"
  caption: "Back of the Radiation Badge, SAINTCON 2021 minibadge"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=RADIATION%20BADGE&year=2021
  title: RADIATION BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2021''.'
- kind: url
  url: https://minibadge.wiki/2021.json
  title: MiniBadge Wiki 2021 data (RADIATION BADGE entry)
  accessed: '2026-09-07'
  note: 'Underlying JSON record behind the search-filtered wiki page; gave soldering instructions, LED count, special jumper warning, front/back image URLs, and confirmed conferenceYear 2021. quantityMade, category, boardHouse, howToAcquire, and rarity fields were present but empty in the source.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The minibadge.wiki listing is a community-submitted record, not the maker''s own page, and no maker profile, storefront, or repo for "Jup1t3r" could be located, so price, quantity, availability, and open-source status are unknown. The record''s description field is blank; summary/functions above are drawn from the soldering and special instructions, which do describe the board''s actual behavior (LED count and blink/solid jumper). No PCB color could be confirmed from the source text (only images, which were not analyzed for color).'
last_modified_date: '2026-09-07'
---

The Radiation Badge is a beginner-level minibadge made by Jup1t3r for SAINTCON 2021, part of the con's long-running tradition of small hobbyist-built badges that attendees collect and trade. It carries three discrete LEDs, each mounted with its light-emitting face toward the board and aligned to a triangular silkscreen cutout, along with three identical resistors that can be soldered in any orientation.

The badge's one design quirk is its mode-select jumper: builders choose between a blinking pattern or a solid-on LED by bridging a different pair of the three jumper pads (middle+top for blinking, middle+bottom for solid), and the listing specifically warns not to bridge all three pads at once, since that can short the badge and disrupt the rest of it.

Beyond the community wiki record that documents its assembly, no maker page, storefront, or repository for the badge could be found, so how many were made, how they were distributed, and whether it is still available are unknown.
