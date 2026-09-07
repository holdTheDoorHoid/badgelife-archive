---
title: MATRIX BADGE
id: saintcon-2021-matrix-badge
layout: badge
parent: Saintcon 2021
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2021
year: 2021
makers:
- name: Jup1t3r
summary: A SAINTCON 2021 minibadge with a Matrix-themed design that lights RED and BLUE LEDs, requiring a host badge with a clock pin.
functions: 'Lights four LEDs (2 red, 2 blue) driven off a host badge''s clock pin; no onboard microcontroller.'
look:
  colors: []
  shape: null
  themes:
  - sci-fi
tech:
  mcu: null
  leds:
    count: 4
    type: discrete
    note: 'Two red and two blue LEDs; reds mount with the green indicator facing down, blues with it facing up.'
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
- label: minibadge.wiki/?search=MATRIX%20BADGE&year=2021
  url: https://minibadge.wiki/?search=MATRIX%20BADGE&year=2021
  kind: website
- label: minibadge.wiki 2021 data export
  url: https://minibadge.wiki/2021.json
  kind: doc
images:
  - file: assets/images/badges/saintcon-2021/matrix-badge/0a394c5349.jpg
    source: "https://minibadge.wiki/2021.json"
    credit: "Jup1t3r"
    caption: "Matrix Badge minibadge, front"
  - file: assets/images/badges/saintcon-2021/matrix-badge/d90aacc480.jpg
    source: "https://minibadge.wiki/2021.json"
    credit: "Jup1t3r"
    caption: "Matrix Badge minibadge, back"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=MATRIX%20BADGE&year=2021
  title: MATRIX BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2021''.'
- kind: url
  url: https://minibadge.wiki/2021.json
  title: 'MiniBadge Wiki 2021 data export (MATRIX BADGE record)'
  accessed: '2026-09-07'
  note: 'Structured record for the badge: author Jup1t3r, LED count/type/placement, soldering difficulty (Intermediate), special instruction that it requires a host badge with the Clock Pin enabled, and front/back image URLs. Description, category, board house, quantity made, and acquisition method were blank in the source record.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched minibadge.wiki/2021.json and confirmed maker (Jup1t3r), LED count/colors (2 red, 2 blue), the red/blue polarity-orientation note, soldering difficulty (Intermediate), and the clock-pin requirement all match the raw record. Confirmed both saved images (front/back) are byte-for-byte the same artwork as the source''s matrix-badge-front.png/back.png. Confirmed the minibadge.wiki live search UI genuinely returns "No minibadges match your filters yet." for this title, and confirmed Jup1t3r''s 2021 title list includes RFID/NFC Badge, Red Team, and The Vault (referenced in the body as other titles in the same series). No maker page, repo, or storefront was found beyond minibadge.wiki, so price, quantity, and availability remain unconfirmed and are left empty/unknown. No color information was given in the source (only LED colors, recorded under tech.leds); tech.mcu is left null (not "none") since the source never states outright there is no onboard MCU, though the clock-pin requirement strongly implies it.'
last_modified_date: '2026-09-07'
---

The Matrix Badge is a SAINTCON 2021 minibadge by Jup1t3r, part of a large series of minibadges Jup1t3r made for that year's SAINTCON (including titles like RFID/NFC Badge, Red Team, and The Vault). It has no onboard microcontroller: instead it carries four LEDs — two red and two blue — wired to light from a host badge's clock pin, so it only works when plugged into a badge that has clock-pin support enabled.

Soldering is rated intermediate, mainly because the LEDs must go in with specific polarity: the red LEDs mount with their green indicator mark facing down, and the blue LEDs with it facing up, each paired with its own current-limiting resistor. No pricing, production quantity, or distribution details were published in the source record, so those fields are left blank rather than guessed.
