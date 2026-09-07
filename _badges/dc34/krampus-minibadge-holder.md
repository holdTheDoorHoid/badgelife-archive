---
title: Krampus Minibadge Holder
id: dc34-krampus-minibadge-holder
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc34
year: 2026
makers:
- name: distinctm1nd
  url: https://ghoul.lol/
summary: A Krampus-themed minibadge holder with an onboard ATtiny 814 driving LEDs, sold by distinctm1nd (Cabinet of Distinctm1nd).
functions: Holds and lights up minibadges. Preorders can be picked up at DC. Note this is a Saintcon-style minibadge holder that requires a small amount of soldering.
look:
  colors: []
  shape: null
  themes:
  - horror
  - holiday
tech:
  mcu: ATtiny814
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $45
  price_usd: 45.0
  quantity: ''
  availability: sold_out
  availability_note: Listed as "Sold out" on ghoul.lol as of 2026-09-06.
  distribution:
  - preorder
  where: Preordered through ghoul.lol (Cabinet of Distinctm1nd); pickup at DEF CON.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/distinctm1nd/krampus_minibadge_holder/tree/main/hardware
  firmware_url: https://github.com/distinctm1nd/krampus_minibadge_holder/tree/main/firmware
  eda_tool: null
links:
- label: ghoul.lol
  url: https://ghoul.lol/
  kind: store
- label: github.com/distinctm1nd/krampus_minibadge_holder
  url: https://github.com/distinctm1nd/krampus_minibadge_holder
  kind: repo
images:
- file: assets/images/badges/dc34/krampus-minibadge-holder/f20c2b9650.png
  source: https://github.com/distinctm1nd/krampus_minibadge_holder
  credit: distinctm1nd
  caption: Krampus Minibadge Holder, front
- file: assets/images/badges/dc34/krampus-minibadge-holder/7fc62d39b9.png
  source: https://github.com/distinctm1nd/krampus_minibadge_holder
  credit: distinctm1nd
  caption: Krampus Minibadge Holder, back
contact:
  discord: distinctm1nd
  emails:
  - distinctm1nd@pm.me
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 55
  updated: 7/31/2026 13:20:05
  listing: New
- kind: url
  url: https://github.com/distinctm1nd/krampus_minibadge_holder
  title: 'GitHub: distinctm1nd/krampus_minibadge_holder'
  accessed: '2026-09-06'
  note: Confirmed maker, ATtiny814 MCU, GPIO dev connector (PA5, PA6, PA7, PB2, PB3), 3-pin UPDI programming connector, and presence of firmware/hardware folders; source of product images.
- kind: url
  url: https://ghoul.lol/
  title: Cabinet of Distinctm1nd (ghoul.lol)
  accessed: '2026-09-06'
  note: Confirmed $45 price and sold-out status for the Krampus Minibadge Holder listing.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Maker''s own GitHub repo and storefront confirm the item, price, and hardware (ATtiny814). LED type/count, exact LED count, quantity made, holder capacity claim, and license were not stated by the maker anywhere findable, so left empty rather than guessed. A third-party summary of the repo mentioned ''holds up to 6 minibadges'' but this could not be independently confirmed from the README text itself, so it was omitted from tech/functions fields. No LICENSE file was found in the repo, hence open_source: partial (hardware/firmware folders exist but no stated license).'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/krampus-minibadge-holder.glb
  method: kicad
  source_file: hardware/krampus_expansion_board.kicad_pcb
  generated: '2026-09-07'
  bytes: 656316
---

The Krampus Minibadge Holder is a holiday-horror-themed minibadge holder made by distinctm1nd (Cabinet of Distinctm1nd) for DEF CON 34. It uses an ATtiny814 microcontroller to drive onboard LEDs, and exposes a small development connector (3V3, GND, and GPIOs PA5, PA6, PA7, PB2, PB3) along with a 3-pin UPDI programming header that doesn't require soldering to reprogram. As a Saintcon-style minibadge holder, assembly requires a small amount of soldering by the owner.

The piece was sold as a $45 preorder through the maker's ghoul.lol storefront, with pickup at DEF CON; it is listed as sold out as of research date. The maker publishes firmware and hardware folders in a public GitHub repository, though no explicit open-source license was found there.
