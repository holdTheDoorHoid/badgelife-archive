---
title: ESP32 Meshtastic Minibadge
id: saintcon-2026-esp32-meshtastic-minibadge
layout: badge
parent: Saintcon 2026
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2026
year: 2026
makers:
- name: Pips
summary: A minibadge carrier board for a Seeed XIAO ESP32 module, built for the WIO Meshtastic setup and pre-flashed with Meshtastic firmware.
functions: Runs Meshtastic (LoRa mesh messaging) via the mounted XIAO ESP32 module; firmware can be re-flashed through the official Meshtastic web flasher.
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
tech:
  mcu: ESP32
  leds: null
  display: null
  connectivity:
  - lora
  - meshtastic
  - wifi
  - ble
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '3'
  availability: unknown
  distribution: []
  where: Described by the maker as "secret prototype minibadges"; not a general distribution/sale.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=ESP32%20Meshtastic%20Minibadge&year=2026
  url: https://minibadge.wiki/?search=ESP32%20Meshtastic%20Minibadge&year=2026
  kind: website
- label: minibadge.wiki 2026 data export (JSON)
  url: https://minibadge.wiki/2026.json
  kind: doc
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
images:
- file: assets/images/badges/saintcon-2026/esp32-meshtastic-minibadge/52b211bf5b.jpg
  source: https://minibadge.wiki/data/
  credit: Pips
  caption: Front of the ESP32 Meshtastic Minibadge, with XIAO ESP32 module mounted
  archived: https://web.archive.org/web/20260611104315/http://minibadge.wiki/data/
- file: assets/images/badges/saintcon-2026/esp32-meshtastic-minibadge/b23b6e2c88.jpg
  source: https://minibadge.wiki/data/
  credit: Pips
  caption: Back of the ESP32 Meshtastic Minibadge showing pin headers and jumper pads
  archived: https://web.archive.org/web/20260611104315/http://minibadge.wiki/data/
contact: {}
notes:
- 'category: Personal; qty made: 3'
- 'Board house: OSHPark. Soldering difficulty listed as Beginner.'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=ESP32%20Meshtastic%20Minibadge&year=2026
  title: ESP32 Meshtastic Minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2026''.'
- kind: url
  url: https://minibadge.wiki/2026.json
  title: MiniBadge Wiki 2026 data export
  accessed: '2026-09-07'
  note: 'The search page itself is client-side JS with no server-rendered results; found the underlying JSON data export (linked from minibadge.wiki/data/) and located this badge''s record there: description, soldering instructions, quantity made (3), board house (OSHPark), category (Personal), acquisition note ("secret prototype minibadges"), and front/back image URLs.'
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Only source is the community-run minibadge.wiki database entry (submitted by the maker or a third party); no maker-owned page, repo, or storefront was found for this badge. Price, LED info, display, battery, SAO header, and open-source/design-file status are not stated anywhere and are left empty. "Secret prototype minibadges" suggests very limited/informal distribution rather than a public sale.
last_modified_date: '2026-09-07'
---

The ESP32 Meshtastic Minibadge is a small carrier board by maker Pips, built to hold a Seeed XIAO ESP32 module wired for the WIO Meshtastic setup. It ships pre-flashed with Meshtastic firmware, letting it join a LoRa mesh network out of the box, and can be re-flashed later through the official Meshtastic web flasher if needed.

Assembly is rated Beginner difficulty: solder on the ESP32 module, the 5V jumper (leaving the 3V jumper unsoldered), the diodes, and the pin headers. Only three were made, fabricated through OSHPark, and the maker describes them as "secret prototype minibadges" rather than a badge sold or distributed at large — consistent with a very small, informal batch made for SAINTCON 2026.

No maker-owned project page, repository, or storefront turned up for this badge; everything known about it comes from its entry in the minibadge.wiki community database (surfaced via that site's 2026 JSON data export, since the search page itself is client-rendered). Pricing, LED/display details, battery, SAO compatibility, and whether design files are public remain unknown.
