---
title: 2017 Car Hacking Village Badge
id: dc25-2017-car-hacking-village-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: CanBusHack
summary: A truck-shaped automotive-hacking tool badge for the DEF CON 25 (2017) Car Hacking Village, built around dual OBD2 ports, four CAN channels plus CAN FD, and a LIN bus for practicing real vehicle-network attacks.
functions: 'Routes CAN1-CAN4 and CAN FD to a male or female OBD2 connector via a jumper header (P6), exposes a LIN bus header, an automotive-Ethernet header, and JTAG debug headers for both onboard microcontrollers; drives a bank of discrete status LEDs through 74HC595 shift registers.'
look:
  colors: []
  shape: truck
  themes:
  - automotive
  - security
  - hardware tool
  - village badge
tech:
  mcu: 'NXP MK60FX512VLQ15 (Kinetis, primary); NXP S32K144 (secondary co-processor, not populated on all units) - firmware/PCB silkscreen for the primary chip also references MK63F12, sources do not reconcile this'
  leds: 'discrete LEDs (LTST-C191KSKT), driven via 74HC595 shift registers'
  display: null
  connectivity:
  - usb
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
  open_source: partial
  hardware_url: https://github.com/CanBusHack/2017carhackingvillagebadge/blob/master/DEFCON_2017_QCM.pdf
  firmware_url: https://github.com/CanBusHack/2017carhackingvillagebadge
  eda_tool: Altium
  license: GPL-3.0
  notes: 'Firmware/build projects for both microcontrollers are in the repo (folders DC2017 and DC2017_S32); the hardware side is published only as a rendered schematic PDF, not editable Altium source or Gerbers, so hardware release is partial rather than full.'
links:
- label: github.com/CanBusHack/2017carhackingvillagebadge
  url: https://github.com/CanBusHack/2017carhackingvillagebadge
  kind: repo
  archived: https://web.archive.org/web/20260907112246/https://github.com/CanBusHack/2017carhackingvillagebadge
- label: 'DEFCON_2017_QCM.pdf (full schematic)'
  url: https://github.com/CanBusHack/2017carhackingvillagebadge/blob/master/DEFCON_2017_QCM.pdf
  kind: doc
- label: 'Badge hardware notes (connector pinouts)'
  url: https://github.com/CanBusHack/2017carhackingvillagebadge/blob/master/doc/Badge_hardware_notes.txt
  kind: doc
images: []
contact: {}
notes:
- Repo name and description confirm 'Def Con 2017 Car Hacking Village Badge'.
- 'No photo of the physical badge was found on the repo or in a search of its pages; only a generic GitHub OpenGraph card image exists, so no images were saved.'
- 'Hardware notes describe a "Truck Overlay" and reference a "Front tire of truck overlay," indicating the board is shaped like a truck; no image confirms color or exact silkscreen.'
- 'Price, quantity made, and distribution method (e.g. sold vs. given to village volunteers) are not stated anywhere in the repo; left unknown rather than guessed.'
status: listed
sources:
- kind: url
  url: https://github.com/CanBusHack/2017carhackingvillagebadge
  title: 2017 Car Hacking Village Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 25 (2017)''.'
  archived: https://web.archive.org/web/20260907112246/https://github.com/CanBusHack/2017carhackingvillagebadge
- kind: url
  url: https://raw.githubusercontent.com/CanBusHack/2017carhackingvillagebadge/master/doc/Badge_hardware_notes.txt
  title: 'Badge_hardware_notes.txt'
  accessed: '2026-09-07'
  note: 'Connector-by-connector hardware notes: confirms primary MCU (NXP MK60FX512VLQ15), optional secondary MCU (NXP S32K144), CAN1-4 + CAN FD routing via jumper header P6, LIN bus header, automotive-Ethernet header, and dual (male/female) OBD2 connectors. Also confirms the board carries a truck-shaped overlay ("Front tire of truck overlay").'
- kind: url
  url: https://raw.githubusercontent.com/CanBusHack/2017carhackingvillagebadge/master/README.md
  title: 'README.md'
  accessed: '2026-09-07'
  note: 'Confirms title "Def Con 2017 Car Hacking Village Badge" and that the repo is the SDK and hardware setup, released for public use.'
- kind: url
  url: https://github.com/CanBusHack/2017carhackingvillagebadge/blob/master/DEFCON_2017_QCM.pdf
  title: 'DEFCON_2017_QCM.pdf'
  accessed: '2026-09-07'
  note: 'Full schematic PDF, copyright "DEFCON 2017 - (C) 2017 Specialized Solutions LLC" (CanBusHack''s parent company), dated 7/28/2017. Shows an LED bank (LEDx8 sheet, repeated) driven by 74HC595 shift registers into discrete LTST-C191KSKT LEDs, and confirms the schematics were authored in Altium (native .SchDoc file paths embedded in the PDF metadata).'
- kind: url
  url: https://api.github.com/repos/CanBusHack/2017carhackingvillagebadge/contents/DC2017
  title: 'DC2017 firmware folder listing'
  accessed: '2026-09-07'
  note: 'Embedded firmware project (Kinetis Design Studio/Eclipse-style .ebp/.elay project files, linker scripts, an MK63F12 SVD file) for the primary microcontroller.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo, README, hardware notes doc, and the schematic PDF all corroborate each other on the core hardware (dual MCU, CAN1-4 + CAN FD, LIN, dual OBD2, automotive Ethernet, JTAG). No maker storefront, press coverage, or photos of the assembled badge were found, so price, quantity, distribution, exact color/finish, and whether this badge was sold vs. given away could not be confirmed. The primary MCU part number differs between the hardware notes text (MK60FX512VLQ15) and an SVD file in the firmware project (MK63F12) - both Kinetis parts, discrepancy unresolved and noted rather than guessed at. WebSearch quota was exhausted before additional queries (maker + "badge", maker + "DEF CON") could run; only the repo and its contents (README, hardware notes, schematic PDF, firmware folder listing) were used as sources this pass.'
last_modified_date: '2026-09-07'
---

The 2017 Car Hacking Village Badge is a truck-shaped automotive security tool built by CanBusHack (published under its corporate name, Specialized Solutions LLC) for the Car Hacking Village at DEF CON 25. Rather than a wearable blinky badge, it functions as a hands-on CAN bus and vehicle-network testing platform: a jumper header lets a user route any of four CAN channels or a CAN FD channel to either a male or female OBD2 connector, and the board separately exposes a LIN bus header and an automotive-Ethernet header, all backed by JTAG debug access to its two onboard microcontrollers.

The board is built around an NXP Kinetis MK60FX512VLQ15 as its primary microcontroller, with an optional secondary NXP S32K144 co-processor that CanBusHack notes "is not populated on all badges." A firmware project bundled in the repo's `DC2017_S32` folder references the S32K144, while the `DC2017` folder's linker/debug files reference an MK63F12 part instead of the MK60FX512VLQ15 named in the hardware notes - the two documents disagree on the exact primary chip, and that discrepancy is left unresolved here rather than guessed at. A bank of discrete LEDs (LTST-C191KSKT), driven by 74HC595 shift registers, provides status indication.

CanBusHack released the firmware build projects for both microcontrollers and a full schematic PDF (authored in Altium) under GPL-3.0, describing the repository as "our SDK and Hardware Setup." No Gerbers or editable Altium source were published alongside it, so the hardware release is partial even though the firmware is complete. No photos of the assembled badge, and no listed price, production quantity, or distribution details (sold vs. given to village participants) turned up in the repo or elsewhere; those fields are left blank rather than assumed.

## Make your own

The repository (github.com/CanBusHack/2017carhackingvillagebadge, GPL-3.0) contains everything needed to reproduce the firmware and reference the hardware:

- `DC2017/` - embedded firmware project (linker scripts, an MK63F12 SVD, source) for the primary microcontroller.
- `DC2017_S32/` - embedded firmware project for the secondary NXP S32K144 co-processor.
- `DEFCON_2017_QCM.pdf` - full schematic, useful as a hardware reference even without native Altium files.
- `Truck Overlay.pdf` - the badge's truck-shaped overlay/silkscreen artwork.
- `doc/Badge_hardware_notes.txt` - connector-by-connector pinout notes (JTAG headers, CAN/OBD2 jumper mapping, LIN, automotive Ethernet).
