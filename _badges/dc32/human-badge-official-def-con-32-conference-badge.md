---
title: DC32 Human Badge (official DEF CON 32 conference badge)
id: dc32-human-badge-official-def-con-32-conference-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: DEF CON
- name: Mar Williams
  url: https://marwilliams.art/blogs/projects/def-con-32-badges
  role: concept, design, art & coordination
- name: Entropic Engineering
  role: circuit design / hardware manufacturing
- name: DmitryGR
  role: firmware, uGB Game Boy emulator, rePALM
- name: Bonnie Finley
  role: game development, 3D case modeling
- name: Nutmeg
  role: game development
- name: Chris Maltby
  role: GB Studio support
- name: Will Tuttle
  role: concept / narrative
- name: Jason Scott
  role: concept / narrative
summary: The official DEF CON 32 (2024) conference badge, a cat-shaped wearable built around the newly released Raspberry Pi RP2350, with a touchscreen that flips over to reveal a working Game Boy emulator for the con's custom GB Studio game.
functions: Runs uGB, a custom Game Boy emulator, to play a DEF CON-themed game built with GB Studio; supports loading classic Game Boy ROMs and custom firmware via the RP2350 SDK; orientation sensor switches modes when the badge is flipped for wearing vs. handheld play.
look:
  colors: [black]
  shape: cat
  themes: [cat, robot, video games, ctf]
tech:
  mcu: RP2350
  leds:
    count: null
    type: RGB
    note: Customizable RGB LEDs.
  display: touch screen (orientation-aware)
  connectivity: [ir, usb]
  inputs: [touch, accelerometer]
  power: USB-C
  battery: LiPo (rechargeable li-ion)
  sao_version: v1
  sao_ports: 1
get_one:
  price: $160 ($200 list, promotional pricing seen at $160; bundle deals for 2+ or classroom 10-pack)
  price_usd: 160
  quantity: ''
  availability: available
  availability_note: 'Listed on us.shop.defcon.org with ~690 units in stock as of 2026-09-07.'
  distribution: [purchase]
  where: DEF CON's official online shop (us.shop.defcon.org), and presumably at DEF CON 32 itself.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/jaku/DEFCON-32-BadgeFirmware
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: MIT (firmware)
  fab_url: null
  notes: Firmware repo is MIT-licensed and public; no hardware/schematic source found. A companion community site, DEFROM.lol, lets people build custom ROM-loaded firmware images.
links:
- label: us.shop.defcon.org/products/dc32-badge
  url: https://us.shop.defcon.org/products/dc32-badge
  kind: website
- label: defcon.org/badge/32
  url: https://defcon.org/badge/32
  kind: website
- label: DEFCON-32-BadgeFirmware (GitHub)
  url: https://github.com/jaku/DEFCON-32-BadgeFirmware
  kind: repo
- label: DEF CON 32 Badges – Mar Williams Art
  url: https://marwilliams.art/blogs/projects/def-con-32-badges
  kind: article
images:
  - file: assets/images/badges/dc32/human-badge-official-def-con-32-conference-badge/17d971ab45.jpg
    source: "https://us.shop.defcon.org/products/dc32-badge"
    credit: "DEF CON"
    caption: "Front of the DC32 human badge, cat-shaped case with touchscreen"
  - file: assets/images/badges/dc32/human-badge-official-def-con-32-conference-badge/baee1764a9.jpg
    source: "https://us.shop.defcon.org/products/dc32-badge"
    credit: "DEF CON"
    caption: "DC32 human badge and accessories laid out on a table"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://us.shop.defcon.org/products/dc32-badge
  title: DC32 Human Badge (official DEF CON 32 conference badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc32''.'
- kind: url
  url: https://defcon.org/badge/32
  title: DEF CON 32 badge (redirect page)
  accessed: '2026-09-07'
  note: Redirects to media.defcon.org gallery; no additional text content found.
- kind: url
  url: https://marwilliams.art/blogs/projects/def-con-32-badges
  title: DEF CON 32 Badges – Mar Williams Art
  accessed: '2026-09-07'
  note: Full maker credit list, theme ("Engage"), case/circuit/firmware/game/music credits.
- kind: url
  url: https://github.com/jaku/DEFCON-32-BadgeFirmware
  title: DEFCON-32-BadgeFirmware
  accessed: '2026-09-07'
  note: Confirms MIT-licensed public firmware repo and DEFROM.lol custom-ROM community site.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own shop listing and Mar Williams'' own project page are the primary sources and agree on core facts. LED count not stated anywhere found. No hardware/schematic source (Gerbers/BOM) was located, only the firmware repo, so make_your_own.open_source is "partial". SAO header count assumed as 1 (standard) since no source states a specific number of ports; sao_version set to v1 as the general SAO-support claim did not specify pin count, so this is a light inference from typical badge conventions rather than a stated fact — flagged here for a human to double check if precision matters. "quantity" (total units manufactured) was not found, only current shop stock (~690) which is recorded in availability_note instead.'
last_modified_date: '2026-09-07'
---

The DC32 Human Badge is the official conference badge for DEF CON 32, held in 2024. It takes the shape of a small cat, built around the then-newly-released Raspberry Pi RP2350 microcontroller (dual Arm Cortex-M33 or dual RISC-V cores, doubled RAM over its predecessor). A touchscreen and orientation sensor let the badge switch between wearable mode and a flipped-over handheld mode, where it runs DmitryGR's custom uGB Game Boy emulator to play a DEF CON-themed game built with the open-source drag-and-drop tool GB Studio. Beyond the built-in game, the badge supports loading classic Game Boy ROMs, a single SAO header for add-ons, IR communication, an SD card slot, a real-time clock, customizable RGB LEDs, and USB-C charging for its rechargeable lithium-ion battery, all inside an ABS injection-molded case.

The badge's concept, design, art and coordination came from Mar Williams, working alongside Entropic Engineering on circuit design, DmitryGR on firmware and the emulator, Bonnie Finley and Nutmeg on the game (with 3D case modeling also by Finley), Chris Maltby (creator of GB Studio) supporting the game tooling, and Will Tuttle and Jason Scott on the badge's narrative, themed around DEF CON 32's "Engage" motto. Manufacturing was handled by ICSN.

## Make your own

The badge's firmware is published on GitHub (jaku/DEFCON-32-BadgeFirmware) under an MIT license, and a community site, DEFROM.lol, lets people upload their own Game Boy ROMs (up to 2MB) to produce custom firmware images for the badge. No hardware design files (schematics, Gerbers, or BOM) were found published by the makers, so full open-source status is partial rather than complete.
