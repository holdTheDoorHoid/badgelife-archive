---
title: UPDeeDeeI SAO
id: dc34-updeedeei-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Xenu (team name is Lepi Labs)
summary: A moth-shaped SAO that doubles as a working UPDI programmer, with a flexible PCB "tongue" wired as a functional USB cable.
functions: UPDI programmer, FPC tongue with functional USB cable, RGB LED eyes with selectable color modes cycled by a button
look:
  colors: []
  shape: moth
  themes:
  - animal
  - hardware tool
  - learn to solder
tech:
  mcu: ATtiny814
  leds:
    count: 2
    type: RGB
    note: Two RGB LEDs light the moth's eyes through hot-glue diffusers; controlled via interrupt-driven PWM.
  display: none
  connectivity:
  - usb
  - uart
  - i2c
  battery: CR2032 (or powered by host badge's SAO connector)
  sao_version: null
get_one:
  price: $35
  price_usd: 35.0
  quantity: 7
  availability: sold_out
  availability_note: 'Uberflux listing showed 7 sold, 0 remaining as of 2026-09-06.'
  distribution:
  - purchase
  where: Sold directly by Lepi Labs via their Uberflux storefront at DEF CON 34.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/lepi-labs/6-dc34-moth-badge
  firmware_url: https://github.com/lepi-labs/6-dc34-moth-badge
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: Repo includes schematics, PCB design, firmware, and artwork, organized into folders for board, code, artwork, and misc docs. License not stated on the repo.
links:
- label: uberflux.com/product/LEPI-dc34-moth
  url: https://uberflux.com/product/LEPI-dc34-moth
  kind: store
- label: github.com/lepi-labs/6-dc34-moth-badge
  url: https://github.com/lepi-labs/6-dc34-moth-badge
  kind: repo
- label: labs.com
  url: https://labs.com
  kind: website
images:
- file: assets/images/badges/dc34/updeedeei-sao/5a6d91c76f.jpg
  source: "https://uberflux.com/product/LEPI-dc34-moth"
  credit: "Lepi Labs"
  caption: "UPDeeDeeI SAO, moth-shaped UPDI programmer with FPC tongue USB cable"
- file: assets/images/badges/dc34/updeedeei-sao/94019163fe.jpg
  source: "https://uberflux.com/product/LEPI-dc34-moth"
  credit: "Lepi Labs"
  caption: "UPDeeDeeI SAO, additional angle showing the moth eyes and CR2032/SAO connector"
contact:
  discord: xenu
  emails:
  - xenu@lepi-labs.com
  handles:
  - '@lepi'
  raw:
  - 'Bluesky:'
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 34
  updated: 7/6/2026 17:41:17
  listing: Update to Existing
- kind: url
  url: https://uberflux.com/product/LEPI-dc34-moth
  title: "UPDeeDeeI SAO product page - Uberflux"
  accessed: '2026-09-06'
  note: "Maker, description, MCU, LEDs, price, quantity sold, images."
- kind: url
  url: https://github.com/lepi-labs/6-dc34-moth-badge
  title: "lepi-labs/6-dc34-moth-badge"
  accessed: '2026-09-06'
  note: "Confirms hardware/firmware are published; details LED count, button mode-cycling, and dual UPDI-programmer/external-target function."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Duplicates dc34-moth-updi-programmer-working-title (same maker, same item, now fully identified). The `labs.com` link in the entry appears to be a broken/generic placeholder (returns HTTP 403, unrelated to Lepi Labs) and could not be confirmed as the maker''s site; left as-is per instructions. SAO header pin count (v1/v1.69bis/v2) not stated by either source, so tech.sao_version left null. No PCB/solder-mask color or license explicitly stated.'
last_modified_date: '2026-09-06'
---

The UPDeeDeeI SAO is a moth-shaped add-on made by Xenu of Lepi Labs for DEF CON 34. Beyond decorating a badge, it is a fully working UPDI programmer built around an ATtiny814, based on the open-source UPDI-programmer design by Stefan Wagner. Its centerpiece trick is a flexible printed-circuit "tongue" that folds out from the moth's mouth and acts as a real USB cable, connecting the SAO to a computer to flash UPDI-capable AVR chips, either the board's own microcontroller or an external target via a jumper. A CH340E handles the USB-to-serial conversion and an AP2122K regulates power, with the UPDI voltage configurable between 3.3V and 5V.

Two RGB LEDs behind hot-glue diffusers form the moth's glowing eyes; a button cycles through several color and lighting modes when the SAO isn't busy programming. It can run off a CR2032 coin cell or draw power from a host badge's SAO connector. Lepi Labs sold it for $35 through their Uberflux storefront, with all 7 units made selling out. The hardware, firmware, and artwork are published on GitHub, split into folders for board design, code, artwork, and miscellaneous documentation, though no explicit open-source license is stated.

This entry duplicates dc34-moth-updi-programmer-working-title, an earlier sheet row for the same maker and item that had only a working title; that entry should be reconciled with this fuller record.
