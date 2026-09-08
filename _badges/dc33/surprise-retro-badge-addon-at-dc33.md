---
title: Surprise Retro badge addon at DC33
id: dc33-surprise-retro-badge-addon-at-dc33
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: Whiskey Pirates (trueControl shop)
  url: https://shop.truecontrol.org/
- name: 'true'
  role: circuit, layout, design and code
- name: Cprossu
  role: concept inspiration
summary: A DC33 "Retro Tech Community" badge addon from trueControl (true and Cprossu), themed around retrocomputing, with a retro peripheral port and RGB LEDs.
functions: Includes at least one antiquated-but-still-usable computer peripheral port, knobs/switches/buttons with a virtual toggle system, and RGB LEDs; a companion manual was required reading to program it. The visual design was kept secret before the con.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: CH32X033
  leds:
    count: 12
    type: RGB
    note: 9x RGB LED plus 3x single-color LED, per the maker's repo description.
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
make_your_own:
  open_source: null
  hardware_url: https://git.trueserve.org/trueControl/dc33-retro-tech-addon
  firmware_url: null
  eda_tool: null
get_one:
  price: $42
  price_usd: 42
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - free_drop
  where: Pre-order online for pickup in person at DEF CON 33, or given away free at the con to interested retrocomputing attendees.
links:
- label: shop.truecontrol.org/index.php?route=product/product&path=59&product_id=430
  url: https://shop.truecontrol.org/index.php?route=product/product&path=59&product_id=430
  kind: store
- label: git.trueserve.org/trueControl/dc33-retro-tech-addon
  url: https://git.trueserve.org/trueControl/dc33-retro-tech-addon
  kind: repo
  archived: https://web.archive.org/web/20260214163754/https://git.trueserve.org/trueControl/dc33-retro-tech-addon
images:
- file: assets/images/badges/dc33/surprise-retro-badge-addon-at-dc33/4d42425205.jpg
  source: https://shop.truecontrol.org/index.php?route=product/product&path=59&product_id=430
  credit: trueControl
  caption: The Surprise Retro badge addon
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://shop.truecontrol.org/index.php?route=product/product&path=59&product_id=430
  title: Surprise Retro badge addon at DC33
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc33''.'
- kind: url
  url: https://git.trueserve.org/trueControl/dc33-retro-tech-addon
  title: trueControl/dc33-retro-tech-addon - trueserve Git
  accessed: '2026-09-07'
  note: Repo page/description confirms MCU (CH32X033), USB, and LED count (9x RGB + 3x single-color).
  archived: https://web.archive.org/web/20260214163754/https://git.trueserve.org/trueControl/dc33-retro-tech-addon
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Storefront description and repo metadata confirm the core facts (maker, MCU, LEDs, price, distribution model). Could not reach the repo file listing (403) or the trueControl BASIC documentation page (403) for firmware/schematic links or a manual, so open_source, firmware_url, colors, and shape are left empty. The product page''s "Availability: 2" figure looked like leftover post-con stock rather than a meaningful quantity, so quantity was left blank; availability recorded as sold_out based on the con-only pickup model and no shipping option ever being enabled.'
last_modified_date: '2026-09-07'
---

The Surprise Retro badge addon was a limited-run SAO/badge addon sold and given away by the Whiskey Pirates operating trueControl's shop at DEF CON 33 (2025), as part of their "Retro Tech Community" theme. The concept came from Cprossu, with true handling the circuit design, PCB layout, and firmware. True kept the visual design a secret ahead of the con, describing it only as "a rapidly designed badge addon" celebrating the era when computers were simpler and more visceral to understand.

The addon is built around a CH32X033 microcontroller with USB connectivity, 9 RGB LEDs and 3 single-color LEDs, at least one antiquated computer peripheral port, and physical controls (knobs, switches, or buttons) tied to a virtual toggle system. A manual was published for buyers, described as required reading to actually program the device. Distribution followed trueControl's usual model for this addon line: pre-orders ($42) reserved a unit for in-person pickup at the con, while the majority (roughly two-thirds to three-quarters) of the units made were given away free to attendees interested in retrocomputing; no shipping option was ever offered.

## Make your own

Source files are published at trueControl's self-hosted Gitea instance (git.trueserve.org/trueControl/dc33-retro-tech-addon), but the repository's file listing could not be reached during this research pass (HTTP 403), so it is unclear whether schematics, Gerbers, and firmware source are all included versus just a description.
