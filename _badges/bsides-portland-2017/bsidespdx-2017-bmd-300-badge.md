---
title: BSidesPDX 2017 BMD-300 Badge
id: bsides-portland-2017-bsidespdx-2017-bmd-300-badge
layout: badge
parent: BSidesPDX 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-portland-2017
year: 2017
makers:
- name: PDX Badgers
  url: https://github.com/pdxbadgers
summary: A Nordic BMD-300 BLE badge made by PDX Badgers for BSidesPDX 2017, with an OLED display and a four-pin expansion header used for the conference's "Ox-Vox" add-on.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: BMD-300
  leds: null
  display: 0.96" OLED
  connectivity:
  - ble
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/pdxbadgers/pcb-2017
  firmware_url: null
  eda_tool: Eagle
links:
- label: badge.gallery/badges/bsidespdx-2017-bmd-300-badge
  url: https://badge.gallery/badges/bsidespdx-2017-bmd-300-badge
  kind: website
- label: github.com/pdxbadgers/pcb-2017
  url: https://github.com/pdxbadgers/pcb-2017
  kind: repo
images: []
contact: {}
notes:
- Nordic BMD-300 BLE SoC conference badge with OLED display and CR2032 power, held Oct 20-21 2017 at the Oregon Convention Center. Found by the event-year sweep, task bsides-portland.
- No photo of the physical badge was found; only the Eagle design files and event context are documented.
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/bsidespdx-2017-bmd-300-badge
  title: BSidesPDX 2017 BMD-300 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-portland); event read as ''BSidesPDX 2017''.'
- kind: url
  url: https://github.com/pdxbadgers/pcb-2017
  title: 'pdxbadgers/pcb-2017: bsidespdx badger 2017'
  accessed: '2026-09-10'
  note: PDX Badgers' public repo with Eagle schematic/board files (bsides2017.sch, bsides2017.brd) and BOM for the badge; confirms it is an Eagle-designed board, no README with chip/feature detail.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Existence and specs confirmed by badge.gallery and independently by the pdxbadgers/pcb-2017 GitHub repo, including its bom.csv (BMD-300 SoC, Harwin CR2032 holder, ALPS SSSS810701 slide-type power switch, an AliExpress-linked 0.96" 128x64 OLED module, a Harwin 4-pin 2.54mm right-angle header, and two ALPS SKRHABE010 nav switches). Neither source gives price, quantity made, or distribution method, and no photo of the assembled badge could be located, so those fields are left empty. The four-pin right-angle header is confirmed to exist and to be used for Rob Rehrig''s "Ox-Vox" add-on, but nothing ties it to the SAO connector standard, so tech.sao_version stays null and the summary was reworded to drop an unsupported "SAO-style" characterization. The two navigation switches are corroborated by the BOM but tech.inputs is left unset since the guide has no confirmed-but-uncatalogued convention for it here.'
last_modified_date: '2026-09-10'
---

The BSidesPDX 2017 BMD-300 Badge is a conference badge built by the PDX Badgers group for BSidesPDX, held October 20-21, 2017 at the Oregon Convention Center in Portland, Oregon. It is built around a Nordic BMD-300 Bluetooth Low Energy SoC module and includes a small OLED display, a CR2032 coin-cell power supply with a slide switch, and a four-pin SMD right-angle header used to connect an expansion add-on.

That expansion header was used for "Ox-Vox," an add-on board presented at the conference by Rob Rehrig, reportedly demoed before the main badge itself was made public. Beyond that, no production numbers, pricing, or distribution details for the badge have surfaced.

## Make your own

PDX Badgers published the badge's hardware design in the `pdxbadgers/pcb-2017` GitHub repository, which contains an Eagle schematic (`bsides2017.sch`), board layout (`bsides2017.brd`), custom component libraries, and a bill of materials (`bom.csv`). No firmware source was found alongside the hardware files.
