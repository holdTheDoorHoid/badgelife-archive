---
title: Shitty Add-On Fix
id: dc26-shitty-add-on-fix
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc26
year: 2018
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/twinkletwinkie
summary: A small patch board that corrects a flipped and rotated SAO connector on a misprinted badge, restoring power and ground to the add-on header.
functions: Passes power and ground between a badge and a Shitty Add-On through a bridging 2x2 header; has a footprint for an 0805 resistor on the power line that can be bridged with solder if not needed.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: '250'
  availability: unknown
  distribution:
  - free_drop
  where: Bundled with rejected "Fat Pika" (DC26 Shitty Add-on) boards by the maker; not sold separately.
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/158885-shitty-add-on-fix
  firmware_url: null
  eda_tool: KiCad
images:
  - file: assets/images/badges/dc26/shitty-add-on-fix/cc8cd174f3.jpg
    source: "https://hackaday.io/project/158885-shitty-add-on-fix"
    credit: "TwinkleTwinkie"
    caption: "The Shitty Add-On Fix patch board"
contact: {}
notes:
- Patch board fixing misplaced SAO connectors.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/158885-shitty-add-on-fix
  title: Shitty Add-On Fix
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/158885-shitty-add-on-fix
  title: Shitty Add-On Fix (Hackaday.io project page)
  accessed: '2026-09-07'
  note: 'Project description, BOM (Harwin M20-9980245 2x2 headers, 0805 resistor), gerbers/KiCad/dxf files, and a project log confirming the maker had 250 made to bundle with rejected "Fat Pika" boards.'
- kind: url
  url: https://hackaday.io/twinkletwinkie
  title: TwinkleTwinkie (Hackaday.io profile)
  accessed: '2026-09-07'
  note: 'Confirms "Fat Pika" (the badge these rejects came from) is listed as "TwinkleTwinkie''s DC26 Shitty Add-on #2", dating this fix board to DEF CON 26, 2018.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is not a badge or SAO in its own right but a small patch/adapter board the maker made to salvage boards from a bad SAO connector print run on their DC26 "Fat Pika" add-on. No price is listed anywhere; it appears to have been given away bundled with the reject boards rather than sold. Final distribution plan was still undecided as of the last project log entry (2018-06-20), so availability is left unknown. No image beyond the one og:image found; no separate storefront or repo outside the Hackaday.io project page.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/shitty-add-on-fix/
---

TwinkleTwinkie's "Fat Pika" was their second Shitty Add-On (SAO) built for DEF CON 26 in 2018, but a manufacturing run came back with the SAO header footprint flipped and rotated, leaving the power and ground pins misaligned. Rather than scrap the boards, TwinkleTwinkie designed this small patch/bridge board: it sits between the badge's SAO header and the add-on's own header, carrying just power and ground, with a footprint for an 0805 resistor on the power line (bridge it with solder if a resistor isn't needed).

The maker had OSH Park prototypes tested successfully on a first-run "Fat Pika" reject, then ordered 250 units to bundle with the other reject boards from that print run, planning to sort out distribution once they arrived from China. No price or formal storefront was ever attached to it; it functioned as a fix included with otherwise-defective add-ons rather than a product sold on its own.

## Make your own

The Hackaday.io project page includes a downloadable zip with gerbers, the KiCad project, and the original board outline as a .dxf file. Building one requires two Harwin M20-9980245 2x2 headers (one for the badge side, one for the add-on side) and, optionally, an 0805 resistor for the power line. The maker explicitly invites others to fork the design for other SAO pinout mismatches, noting that the pin labels under "Add-on" must match your own hardware before using it as-is.
