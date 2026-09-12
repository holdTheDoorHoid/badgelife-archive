---
title: 0x0G Badge (Google, DC26)
id: dc26-0x0g-badge-google-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Google
  url: https://github.com/google
summary: The electronic badge Google handed out at 0x0G, its annual invite-only party held alongside DEF CON/Black Hat; a poker-chip-shaped PCB with a ring of LEDs that talk over infrared.
functions: Drives a ring of LEDs and communicates with other badges over infrared (transmitter and decoder in firmware); exact game/interaction logic is not documented in the repo.
look:
  colors: []
  shape: circle
  themes:
  - security
  - hardware tool
tech:
  mcu: PIC16
  leds: null
  display: none
  connectivity:
  - ir
  battery: coin cell
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution:
  - free_drop
  where: Handed out to attendees of 0x0G, Google's private DEF CON/Black Hat week event; not sold.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/google/0x0g-2018-badge/tree/master/board
  firmware_url: https://github.com/google/0x0g-2018-badge/tree/master/firmware.X
  eda_tool: KiCad
  license: Apache-2.0
links:
- label: github.com/google/0x0g-2018-badge
  url: https://github.com/google/0x0g-2018-badge
  kind: repo
  archived: https://web.archive.org/web/20260907113848/https://github.com/google/0x0g-2018-badge
images:
- file: assets/images/badges/dc26/0x0g-badge-google-dc26/bfdd83748a.png
  source: https://github.com/google/0x0g-2018-badge
  credit: Google
  caption: Poker-chip-shaped PCB outline graphic from the badge design files
  archived: https://web.archive.org/web/20260907113848/https://github.com/google/0x0g-2018-badge
contact: {}
notes:
- casino-chip (poker chip) design, round PCB
- Sheet listed the maker as "TwitchyLiquid64", but that handle is not among the repo's contributors or its listed authors (matir@google.com, jsonp@google.com, claymore@google.com, all @google.com); makers has been corrected to Google.
- Repo README states this was "a one-time release, do not expect updates" and is not an officially supported Google product; the repo was archived (read-only) by GitHub in 2022.
status: released
sources:
- kind: url
  url: https://github.com/google/0x0g-2018-badge
  title: 0x0G Badge (Google, DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
  archived: https://web.archive.org/web/20260907113848/https://github.com/google/0x0g-2018-badge
- kind: url
  url: https://github.com/google/0x0g-2018-badge/blob/master/README.md
  title: 0x0G 2018 badge README
  accessed: '2026-09-07'
  note: Confirms it is the badge for 0x0G, Google's annual DEF CON/Black Hat event; PIC microcontroller, LED ring, infrared comms; hardware and firmware both Apache 2.0; lists three @google.com authors, not TwitchyLiquid64.
- kind: url
  url: https://github.com/google/0x0g-2018-badge/tree/master/board
  title: board/ directory listing (KiCad files)
  accessed: '2026-09-07'
  note: KiCad schematic/PCB files reference a Microchip PIC16 MCU library (MCU_Microchip_PIC16.lib) confirming the chip family; battery holder footprint present.
- kind: url
  url: https://github.com/google/0x0g-2018-badge/blob/master/graphics/pokerchip.svg
  title: graphics/pokerchip.svg
  accessed: '2026-09-07'
  note: Poker-chip-shaped board outline graphic, confirming the casino-chip design noted on the intake sheet.
- kind: url
  url: https://github.com/google/0x0g-2018-badge/blob/master/engineering_documentation/INSTRUCTIONS.txt
  title: engineering_documentation/INSTRUCTIONS.txt
  accessed: '2026-09-07'
  note: 'Assembly notes: PIC chip orientation, IR receiver through-hole part, LED polarity, and a coin-cell battery holder making direct contact with a PCB pad (confirms coin-cell battery, no info on LED count/color).'
- kind: url
  url: https://github.com/google/0x0g-2018-badge/graphs/contributors
  title: Repo contributors
  accessed: '2026-09-07'
  note: Only contributor listed is "Matir" (matching matir@google.com in the README); no TwitchyLiquid64.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The GitHub repo (the maker''s own source) confirms the badge is for 0x0G, Google''s private DEF CON/Black Hat week party, in 2018 (DC26), with a PIC16 MCU, IR comms, an LED ring, and a poker-chip-shaped PCB, all open-sourced under Apache 2.0. Could not confirm: quantity made (the sheet''s "520 units" note is unverified against the repo -- left in notes but not entered into get_one.quantity), exact LED count/type or color, price (it was a free giveaway, not sold), and exact PIC16 part number. No maker photo of an assembled/populated badge was found in the repo; the saved image is a design-file graphic of the PCB outline shape, not a photo of the finished item. The sheet-listed maker "TwitchyLiquid64" does not match the repo''s authorship and was corrected to Google.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/0x0g-badge-google-dc26.glb
  method: kicad
  source_file: board/badgeelec.kicad_pcb
  generated: '2026-09-07'
  bytes: 121780
---

The 0x0G badge was made by Google for its own 0x0G party, an invite-only gathering the company runs each year alongside DEF CON and Black Hat in Las Vegas. Rather than a store item, it was a giveaway to attendees at the 2018 edition (DC26). The board is shaped like a poker chip, fitting the party's casino theme, and is built around a Microchip PIC16 microcontroller that drives a ring of LEDs and talks to other badges over infrared, with a coin-cell battery holder on the back.

Google released the full KiCad hardware design and C firmware source for the badge on GitHub under the Apache 2.0 license, alongside assembly instructions covering LED and IR-receiver orientation and PIC chip placement. The README is explicit that this was a one-time release with no expectation of support or updates, and the repository has since been archived (read-only) by GitHub. No information on the exact quantity produced, LED count/color, or PIC16 part number could be confirmed from the repository itself.

## Make your own

The `board/` directory holds the KiCad schematic and PCB layout (including the poker-chip board outline and footprint libraries for the PIC16, an IR receiver, and other components), and `firmware.X/` holds the C source, split into LED driving, IR transmission, and IR decoding modules with a Makefile for the Microchip toolchain. `engineering_documentation/INSTRUCTIONS.txt` walks through assembly orientation for the PIC chip, LEDs, IR receiver, and battery holder.
