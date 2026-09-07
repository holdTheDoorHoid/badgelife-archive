---
title: HACKERS CHALLENGE BADGE
id: saintcon-2022-hackers-challenge-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Zevlag
summary: A common SAINTCON minibadge earned by interacting with the Hackers Challenge game's Game Masters.
functions: Lights three LEDs (one uncolored, one red, one blue); no interactivity beyond soldering and display.
look:
  colors: [red, blue]
  shape: null
  themes: [minibadge, hardware tool, ctf, learn to solder]
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: 'One non-colored LED (D1, back side) and one red LED (D2) plus one blue LED (D3) on the front; each has its own resistor (non-colored/R1, red/R2, blue/R3). The maker also suggests mounting the LEDs upside-down as an advanced alternative.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: [contest]
  where: Given out by SAINTCON's Hackers Challenge Game Masters, sometimes after solving a puzzle.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=HACKERS%20CHALLENGE%20BADGE&year=2022
  url: https://minibadge.wiki/?search=HACKERS%20CHALLENGE%20BADGE&year=2022
  kind: website
- label: minibadge.wiki 2022 data export (JSON)
  url: https://minibadge.wiki/2022.json
  kind: doc
images:
  - file: assets/images/badges/saintcon-2022/hackers-challenge-badge/2bbd0f14f7.jpg
    source: "https://minibadge.wiki/data/"
    credit: "Zevlag / minibadge.wiki"
    caption: "Front of the Hackers Challenge minibadge, showing the non-colored, red, and blue LEDs"
  - file: assets/images/badges/saintcon-2022/hackers-challenge-badge/3f0630ec0f.jpg
    source: "https://minibadge.wiki/data/"
    credit: "Zevlag / minibadge.wiki"
    caption: "Back of the Hackers Challenge minibadge, showing the solder pads and header pins"
contact: {}
notes:
- 'category: Official; rarity: Common'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=HACKERS%20CHALLENGE%20BADGE&year=2022
  title: HACKERS CHALLENGE BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2022''.'
- kind: url
  url: https://minibadge.wiki/2022.json
  title: MiniBadge Wiki 2022 data export
  accessed: '2026-09-07'
  note: 'Raw JSON record for this badge: description, soldering instructions (LED/resistor placement), designer, category (Official), rarity (Common), and front/back image paths. The search page itself is JS-rendered and returns no listings to a static fetch; the JSON export was the source that actually carried the badge data.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found is the community-run minibadge.wiki database (third-party, not the maker''s own page); no maker (Zevlag) profile, storefront, or repo was located. Price, quantity made, and board house are not stated in the source (quantityMade recorded as 0, which the site appears to use as "unknown" rather than literally zero, so left blank here rather than guessed). No open-source design files found.'
last_modified_date: '2026-09-07'
---

The Hackers Challenge Minibadge is a common SAINTCON badge designed by Zevlag, tied to SAINTCON's long-running Hackers Challenge puzzle/CTF track. Attendees get one from the Hackers Challenge Game Masters, and per the maker's own notes they "MAY make you solve at least one puzzle to earn one, but then again, maybe not" — so distribution is a mix of contest reward and simple give-away.

The board is a simple three-LED soldering kit: a non-colored LED on the back (D1) and a red (D2) and blue (D3) LED on the front, each with its own through-hole resistor, plus three 2-position headers. The build instructions rate it "Intermediate" and note that the front LEDs can optionally be mounted upside-down as a more advanced variant. It carries no microcontroller and no SAO header.

It's catalogued as "Official" category and "Common" rarity on minibadge.wiki, a community-run archive of SAINTCON minibadges; that site's JSON data export was the only source found, since minibadge.wiki's own search page is rendered client-side and returns no results to a plain fetch. No maker page, storefront, or open-source design files for this specific badge were located.
