---
title: Retro Tech Community Addon
id: dc32-retro-tech-community-addon
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
series: Retro Tech
makers:
- name: trueControl
  url: https://basic.truecontrol.org/database/
summary: A GAT/SAO-standard addon designed by trueControl for the Retro Tech Community group at DEF CON 32, styled as a tiny green-screen terminal cursor with light-up ambient "programs."
functions: Simulates an old terminal cursor that can be set to white, green, amber, or off, with adjustable flash rate and brightness. Also runs five selectable ambient light programs (rainbow, color fades, twinkling, a fast alternating pattern, and a non-functional "operating a keyboard" placeholder) chosen randomly during idle "program run mode," with per-program parameters (rate, hue, saturation, twinkle count) tunable via the two buttons and knob; settings are saved to onboard EEPROM.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - text
tech:
  mcu: CH32V003F4P6
  leds:
    count: 12
    type: RGB
    note: 9x RGB LEDs (one per letter of "RETRO"), driven by an IS31FL3729 LED matrix controller with adjustable current control and 8-bit PWM per channel, plus 3x single-color cursor LEDs (white, amber, green).
  display: none
  connectivity:
  - uart
  inputs:
  - buttons
  - rotary encoder
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://git.trueserve.org/trueControl/dc32-retro-tech-addon/src/branch/master/hardware
  firmware_url: https://git.trueserve.org/trueControl/dc32-retro-tech-addon/src/branch/master/firmware
  eda_tool: null
links:
- label: basic.truecontrol.org/database/dc32/retro-tech
  url: https://basic.truecontrol.org/database/dc32/retro-tech/
  kind: website
- label: git.trueserve.org/trueControl/dc32-retro-tech-addon
  url: https://git.trueserve.org/trueControl/dc32-retro-tech-addon
  kind: repo
- label: Retro Tech user manual (ASCII)
  url: https://basic.truecontrol.org/database/dc32/retro-tech-manual.txt
  kind: doc
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://basic.truecontrol.org/database/dc32/retro-tech/
  title: Retro Tech Community Addon
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc32''.'
- kind: url
  url: https://git.trueserve.org/trueControl/dc32-retro-tech-addon
  title: 'trueControl/dc32-retro-tech-addon: Retro Tech Community GAT addon at DEF CON 32'
  accessed: '2026-09-07'
  note: Confirms hardware/firmware are published (CH32V003F4P6, IS31FL3729, 9x RGB + 3x single-color LEDs); README describes build/flash process via MounRiver Studio or UART bootloader.
- kind: url
  url: https://basic.truecontrol.org/database/dc32/retro-tech-manual.txt
  title: Retro Tech Community GAT user manual v1
  accessed: '2026-09-07'
  note: Describes the three operating modes, the five selectable "programs," and their tunable parameters.
- kind: url
  url: https://basic.truecontrol.org/database/
  title: trueControl BASIC — Badge / Addon Service & Information Center
  accessed: '2026-09-07'
  note: Lists the DC32 "Retro Tech Community addon" under trueControl's own designs, separately from the site's "Whiskey Pirate Crew" badge list — the source for correcting the maker attribution.
- kind: url
  url: https://shop.truecontrol.org/index.php?route=product/category&path=59_81
  title: 'trueControl Shop: DEF CON 32 badges'
  accessed: '2026-09-07'
  note: Only "Peppercon9 Addon" and "Flames" are listed for sale under DEF CON 32; the Retro Tech Community addon is absent, consistent with it being made for/distributed through the Retro Tech Community group rather than sold in trueControl's storefront.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker corrected: the community sheet this entry was imported from attributes this and several other DC32 items to "Whiskey Pirate Crew (not badgelife)," but trueControl''s own site lists "Retro Tech Community addon" under its own DC32 designs, distinct from its separate "Whiskey Pirate Crew" badge list, and the firmware/hardware repo is under the trueControl git org. No photo of the assembled addon was found (the site has no item photos; the only image in the repo is a schematic, not a photo of the item, so no images were saved). Price, quantity made, and exact distribution method (village giveaway vs. limited drop) were not stated anywhere found; the item does not appear in trueControl''s own shop alongside the two DC32 items that were sold there. The "Retro Tech Community" is a recurring DEF CON village/community (also present at DC33 and DC34) celebrating vintage computing; this addon appears to have been made for that group specifically, per trueControl''s site organization, though no page states that relationship explicitly beyond the shared name.'
last_modified_date: '2026-09-07'
---

The Retro Tech Community Addon is a GAT-standard (SAO v1.69bis-compatible) badge addon that trueControl designed for DEF CON 32, styled after an old terminal's blinking cursor. Nine RGB LEDs, one for each letter of "RETRO," are driven through an IS31FL3729 LED matrix controller, alongside three single-color cursor LEDs (white, amber, green). A CH32V003F4P6 RISC-V microcontroller runs the show, with two buttons and a knob letting the wearer cycle the cursor's color and flash rate, adjust brightness, and enable one or more of five ambient light "programs" (rainbow, fades, twinkling, a fast alternating pattern, and an unused placeholder). Settings persist across power cycles in onboard EEPROM, and the addon exposes a UART bootloader on its GAT aux pins for reflashing without a dedicated debug probe.

Both the hardware (schematics) and firmware are published in trueControl's self-hosted git server, with a MounRiver Studio-based build process and a WCHISP-compatible UART bootloader as an alternative to a WCH-LinkE debug probe. The addon does not appear in trueControl's own storefront alongside that year's other DC32 items ("Flames" and the Peppercon9 addon), suggesting it was made specifically for the Retro Tech Community — a recurring DEF CON village celebrating vintage computing — rather than sold generally; no source found states its price, quantity, or exact distribution method.

## Make your own

Firmware and hardware files are published at trueControl's git server (`git clone https://git.trueserve.org/trueControl/dc32-retro-tech-addon`). Firmware is a MounRiver Studio project targeting the CH32V003; it can be flashed via a WCH-LinkE debug probe, or via the built-in UART bootloader (hold BTN2 while powering on to enter bootloader mode, then flash over TTL UART on the GAT header using any WCHISP-compatible utility).

## History

This is the DC32 edition of a recurring "Retro Tech" addon line trueControl has produced for the Retro Tech Community group across multiple DEF CONs, including a DC33 edition (built around a CH32X033 with USB) and a DC34 "Retro Memories 26" edition.
