---
title: RTV D20
id: dc34-rtv-d20
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Red Team Village
  url: https://redteamvillage.io/
summary: A red PCB badge shaped like a twenty-sided die (d20), sold in the Red Team Village at DEF CON 34.
functions: Front face carries a red two-digit 7-segment display; the back is populated with several red SMD LEDs around a coin-cell holder and two unlabeled DIP/SOIC chips.
look:
  colors:
  - red
  - black
  shape: d20
  themes:
  - fantasy
  - security
  form_factor: pcb badge
tech:
  mcu: null
  leds:
    count: null
    type: null
    note: Several red SMD LEDs visible along the board edges in maker photos; exact count and driver chip not confirmed.
  display: 7-segment display (2-digit)
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: $80
  price_usd: 80.0
  quantity: Limited quantities (exact number not stated)
  availability: limited
  availability_note: 'Per maker post, sold cash-only in the Village during DEF CON 34 (Aug 2026) while supplies lasted; current stock not checked as of 2026-09-06.'
  distribution:
  - purchase
  where: Sold in person at the Red Team Village booth during DEF CON 34, cash only.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: x.com/RedTeamVillage_/status/2080676962515706010
  url: https://x.com/RedTeamVillage_/status/2080676962515706010
  kind: social
images:
- file: assets/images/badges/dc34/rtv-d20/6cf0d9cbc4.jpg
  source: "https://x.com/RedTeamVillage_/status/2080676962515706010"
  credit: "Red Team Village"
  caption: "Front and back of the D20-shaped badge, showing the two-digit 7-segment display, LEDs, and coin-cell battery"
contact:
  discord: .0bli
  emails:
  - 0bli@redteamvillage.io
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 52
  updated: 7/30/2026 19:44:06
  listing: New
- kind: url
  url: https://x.com/RedTeamVillage_/status/2080676962515706010
  title: 'RedTeamVillage on X: badge announcement for DEF CON 34'
  accessed: '2026-09-06'
  note: Confirms price ($80 cash), that it was sold in the Village during DEF CON 34 in limited quantity, and is the source of the product photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    Only source found is the maker's own announcement tweet, which does not name the badge
    "D20" explicitly but shows a die-shaped red PCB badge with a two-digit 7-segment display,
    several LEDs, a CR2032 coin cell, and two unlabeled DIP/SOIC chips on the back. MCU,
    exact LED count/type, SAO header, connectivity, and any game/CTF function could not be
    confirmed from the photo alone; no hardware/firmware repo, storefront listing, or
    Hackaday/press coverage was found. A general Red Team Village Square storefront exists
    (redteamvillage.square.site/shop/badges/3) but is JS-rendered and did not yield item-level
    detail via fetch.
last_modified_date: '2026-09-06'
---

The RTV D20 is Red Team Village's badge for DEF CON 34, shaped like a twenty-sided die rather than the more common rectangular PCB. The red-and-black board carries devil-horn cutouts at the top, a "RED TEAM VILLAGE" wordmark, and a red two-digit 7-segment display on the front face; the back holds a CR2032 coin cell, several red LEDs, and two small unlabeled chips, suggesting some kind of counter, timer, or roll-simulation function that could not be confirmed from available sources.

It was sold cash-only for $80 directly at the Red Team Village booth during DEF CON 34, in limited quantity while supplies lasted, per the group's own announcement post. No storefront listing, hardware/firmware repository, Hackaday.io project, or press coverage turned up beyond that announcement, so most technical details (MCU, exact LED count and type, whether it carries an SAO header, any CTF or game mode) remain unconfirmed.
