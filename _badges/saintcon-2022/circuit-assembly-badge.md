---
title: CIRCUIT ASSEMBLY BADGE
id: saintcon-2022-circuit-assembly-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Jup1t3r
summary: A beginner-level SAINTCON minibadge for the con's Circuit Assembly (soldering) area, mixing through-hole and surface-mount parts on one small board.
functions: 'A 3-way solder jumper on the back selects one of two LED behaviors (solid on or blinking); no other electronic function beyond the LEDs.'
look:
  colors:
  - green
  shape: rectangle
  themes:
  - learn to solder
  - turtle
  - animal
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 'Two SMD LEDs (silkscreened D1/D2 on the back, hand-soldered via the "single-pad method"); the badge''s own instructions carry an explicit polarity warning/diagram, since the LEDs have poor markings for orientation.'
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: 'Given out at SAINTCON''s Circuit Assembly area (the con''s soldering station) to attendees who showed staff something they had soldered themselves.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=CIRCUIT%20ASSEMBLY%20BADGE&year=2022
  url: https://minibadge.wiki/?search=CIRCUIT%20ASSEMBLY%20BADGE&year=2022
  kind: website
images:
  - file: assets/images/badges/saintcon-2022/circuit-assembly-badge/99234c19af.jpg
    source: "https://minibadge.wiki/?search=CIRCUIT%20ASSEMBLY%20BADGE&year=2022"
    credit: "Jup1t3r / minibadge.wiki"
    caption: "Circuit Assembly minibadge, front"
  - file: assets/images/badges/saintcon-2022/circuit-assembly-badge/8e4dfcec21.jpg
    source: "https://minibadge.wiki/?search=CIRCUIT%20ASSEMBLY%20BADGE&year=2022"
    credit: "Jup1t3r / minibadge.wiki"
    caption: "Circuit Assembly minibadge, back"
contact: {}
notes:
- 'category: Official; rarity: Common'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=CIRCUIT%20ASSEMBLY%20BADGE&year=2022
  title: CIRCUIT ASSEMBLY BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2022''.'
- kind: url
  url: https://minibadge.wiki/2022.json
  title: minibadge.wiki 2022 data (CIRCUIT ASSEMBLY BADGE entry)
  accessed: '2026-09-07'
  note: 'Underlying JSON record behind the search page: maker (Jup1t3r), description, soldering instructions and difficulty, category/rarity, quantityMade (recorded as 0, i.e. not stated), acquisition method, and the front/back image URLs.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Verified against the minibadge.wiki search page and the underlying 2022.json record (WebFetch of both), plus the two saved images. Corrected tech.leds: the back-of-board image shows two LED footprints silkscreened D1 and D2, and the soldering instructions call for hand-soldering the LEDs via the "single-pad method" (an SMD technique) — the original entry had wrongly recorded a single THT LED. All other fields checked out: maker, description, soldering difficulty/instructions, category (Official), rarity (Common), quantityMade (0, read as unrecorded), acquisition method, and both image URLs match the source JSON, and the images themselves show the turtle mascot, green PCB, D1/D2 LED pads, and the SOLID/BLINK jumper described. No other maker page, storefront, repo, or press coverage exists to cross-check against.'
last_modified_date: '2026-09-07'
---

The Circuit Assembly Badge is a SAINTCON 2022 minibadge made by Jup1t3r for the con's "Circuit Assembly" area — SAINTCON's name for its communal soldering station. It's a deliberately simple beginner board mixing through-hole and surface-mount parts: two through-hole resistors, a set of four 2-position headers, and two surface-mount LEDs (silkscreened D1 and D2) whose polarity markings the maker's own instructions flag as easy to get backwards, complete with a diagram showing the correct orientation.

Electrically the badge does one thing: a 3-way solder jumper on the back lets the builder choose between the LEDs staying solid on or blinking, by bridging one of two positions (never both, and never all three). There's no microcontroller, no SAO header, and no other function — the badge exists to teach basic soldering technique rather than to do anything on its own.

It wasn't sold; attendees earned one by showing SAINTCON staff at the Circuit Assembly tables something they had soldered themselves, making it a free, in-person "prove you did the work" giveaway rather than a purchase or raffle item. The only record found is the maker's own entry in the minibadge.wiki community database (author: Jup1t3r); no separate storefront, repo, or press coverage of it turned up.
