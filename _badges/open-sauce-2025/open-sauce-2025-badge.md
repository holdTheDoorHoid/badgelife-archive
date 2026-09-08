---
title: Open Sauce 2025 Badge
id: open-sauce-2025-open-sauce-2025-badge
layout: badge
parent: Open Sauce 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: open-sauce-2025
year: 2025
makers:
- name: Open Sauce (with DigiKey/PCBWay)
summary: A soldering-kit conference badge that flashes "OPENSAUCE" as a persistence-of-vision message when shaken, and can be reprogrammed with custom animations beamed in over IR from a phone or screen.
functions: 'POV text/animation display on shake; IR photodiode lets attendees "beam" custom animations to the badge from a screen; single pushbutton for mode control.'
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: ATtiny85
  leds:
    count: 5
    type: discrete
    note: Lite-On LTL1CHKRKNN red LEDs (T-1 package), arranged for persistence-of-vision text
  display: none
  connectivity:
  - ir
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - kit
  where: Given to Open Sauce 2025 attendees as an unassembled through-hole soldering kit (ATtiny85, 5 LEDs, IR photodiode, pushbutton, CR2032 clip); DigiKey ran a companion assembly tutorial and supplied/sponsored parts alongside PCBWay.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/ExcessiveOverkill/os2025-badge
  eda_tool: null
links:
- label: www.digikey.com/en/maker/tutorials/2025/assembling-your-2025-open-sauce-badge
  url: https://www.digikey.com/en/maker/tutorials/2025/assembling-your-2025-open-sauce-badge
  kind: website
- label: opensauce.com/badge-25
  url: https://opensauce.com/badge-25/
  kind: website
- label: ExcessiveOverkill/os2025-badge (firmware)
  url: https://github.com/ExcessiveOverkill/os2025-badge
  kind: repo
images:
  - file: assets/images/badges/open-sauce-2025/open-sauce-2025-badge/32d1d617d1.jpg
    source: "https://opensauce.com/badge-25/"
    credit: "Open Sauce"
    caption: "Assembled 2025 Open Sauce badge, front side showing the five LEDs"
  - file: assets/images/badges/open-sauce-2025/open-sauce-2025-badge/22dafcb8d7.jpg
    source: "https://opensauce.com/badge-25/"
    credit: "Open Sauce"
    caption: "Assembled 2025 Open Sauce badge, back side"
contact: {}
notes:
- Official Open Sauce 2025 festival badge built around an ATtiny85 with 5 LEDs, an IR photodiode, and a shake-triggered persistence-of-vision 'OPENSAUCE' text display. Found by the event-year sweep, task con-open-sauce.
status: released
sources:
- kind: url
  url: https://www.digikey.com/en/maker/tutorials/2025/assembling-your-2025-open-sauce-badge
  title: Open Sauce 2025 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-open-sauce); event read as ''Open Sauce 2025''.'
- kind: url
  url: https://opensauce.com/badge-25/
  title: Open Sauce Badge 25
  accessed: '2026-09-08'
  note: Maker's own badge page; parts list, assembly photos, and IR "beam a custom animation" programming feature confirmed here.
- kind: url
  url: https://github.com/ExcessiveOverkill/os2025-badge
  title: ExcessiveOverkill/os2025-badge
  accessed: '2026-09-08'
  note: Firmware repo (os_2025.hex, fuse settings for the ATtiny85); no hardware/Gerber files or license found in the repo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Price, quantity made, and firmware license are not stated anywhere found. PCB color/shape not visible in the available photos (kit and assembly close-ups only, no full front-on shot of the bare board), so look.colors/shape left empty. "DigiKey/PCBWay" sponsored/supplied parts and ran an assembly tutorial but did not design the badge; design/distribution credit stays with Open Sauce per the maker''s own page. Firmware author on GitHub is ExcessiveOverkill; hardware design files were not located.'
last_modified_date: '2026-09-08'
---

Open Sauce 2025 gave attendees a through-hole soldering kit rather than a finished badge: an ATtiny85, five red LEDs, an IR photodiode, a pushbutton, and a CR2032 clip that builders assemble themselves, with DigiKey publishing a step-by-step assembly tutorial and PCBWay and DigiKey supporting the parts and fabrication. Once built and powered, a shake triggers a persistence-of-vision sweep of the five LEDs that spells out "OPENSAUCE" in mid-air.

The badge's other trick is its IR photodiode: holding the badge up to a phone or monitor playing a specially-encoded flashing pattern lets attendees load custom animations onto it without a programmer, an approach documented on the maker's own badge page alongside the parts list and photos. Firmware for the ATtiny85 (source and the fuse settings needed to flash it) is published on GitHub under ExcessiveOverkill's `os2025-badge` repo; no hardware design files or license were found alongside it, so the project counts as partially open source.

## Make your own

Firmware is available as a prebuilt `os_2025.hex` in the `os2025-badge` GitHub repo, with AVRDUDE commands for flashing an ATtiny85 over a USBASP programmer and the specific fuse bytes required (a one-way change: it disables the reset pin for GPIO use). No schematic, PCB layout, or Gerbers were found published alongside the firmware.


