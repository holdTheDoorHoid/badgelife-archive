---
title: SAINTCON 2025 Nut
id: saintcon-2025-saintcon2025-nut-nfc-token-device-used-to-write-codes-onto-t
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: other
event: saintcon-2025
year: 2025
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: A handheld ESP32-C3 NFC token used in SAINTCON 2025's badge game to write one-time codes onto the NFC tag embedded in that year's wrench-shaped badge.
functions: Writes one-time codes to the NFC tag embedded in the SAINTCON 2025 badge via an onboard NFC reader/writer; the badge then checks those codes in with a game server, which awards points or unlocks game nodes. Has status LEDs and a physical button.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - ctf
tech:
  mcu: ESP32-C3
  leds:
    count: 6
    type: null
    note: 6 addressable status LEDs (LED_NUM_LEDS=6 in firmware config)
  display: none
  connectivity:
  - nfc
  - wifi
  - i2c
  inputs:
  - buttons
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed as part of SAINTCON 2025''s badge game (BadgeLife community: compukidmike, redactd, v0rtex, BP, Mike''s Wife); exact distribution method not confirmed by sources read.'
make_your_own:
  open_source: true
  hardware_url: https://github.com/compukidmike/Saintcon2025/tree/main/Hardware/Nut
  firmware_url: https://github.com/compukidmike/Saintcon2025/tree/main/Firmware/nut
  eda_tool: KiCad
links:
- label: github.com/compukidmike/Saintcon2025/tree/main/Hardware/Nut
  url: https://github.com/compukidmike/Saintcon2025/tree/main/Hardware/Nut
  kind: repo
- label: Saintcon2025 firmware (nut)
  url: https://github.com/compukidmike/Saintcon2025/tree/main/Firmware/nut
  kind: repo
- label: Saintcon2025 repo README
  url: https://github.com/compukidmike/Saintcon2025
  kind: repo
- label: SAINTCON 2025 - compukidmike - The Badge Talk (YouTube)
  url: https://www.youtube.com/watch?v=fYb-d4U15Qc
  kind: video
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2025/tree/main/Hardware/Nut
  title: Saintcon2025 Nut (NFC token device used to write codes onto the badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''saintcon-2025''.'
- kind: url
  url: https://github.com/compukidmike/Saintcon2025
  title: 'compukidmike/Saintcon2025: Saintcon 2025 Badge'
  accessed: '2026-09-07'
  note: 'Repo README explains the badge (a 50mm wrench with an embedded NFC tag) and the game: Nuts are NFC devices that write one-time codes to the badge, which are checked in with a game server for points or to unlock nodes.'
- kind: url
  url: https://github.com/compukidmike/Saintcon2025/blob/main/Firmware/nut/sdkconfig.defaults
  title: Firmware/nut/sdkconfig.defaults
  accessed: '2026-09-07'
  note: ESP-IDF target esp32c3, LED_NUM_LEDS=6, secure element (ATECC608A) enabled, conference Wi-Fi SSID configured.
- kind: url
  url: https://github.com/compukidmike/Saintcon2025/tree/main/Firmware/nut/components
  title: Firmware/nut/components listing
  accessed: '2026-09-07'
  note: Components include nfc-ptx105r-spi (NXP PTX105R NFC reader/writer over SPI), mcp23x17 (I/O expander), and an input component, confirming NFC read/write plus a physical button.
- kind: url
  url: https://www.saintcon.org/com-badgelife/
  title: Community - BadgeLife (SAINTCON)
  accessed: '2026-09-07'
  note: Confirms compukidmike led the SAINTCON 2025 BadgeLife/badge-game team (with redactd, v0rtex, BP, Mike's Wife) and that there was a collaborative badge game that year.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (what it is, maker, event, MCU, NFC chip, LED count, open-source status) come from the maker's own repo and firmware config, so those are solid. Could not find price, quantity made, exact distribution mechanism (raffle vs given to all players vs contest prize), battery type, or any photo of the physical Nut device itself - only the badge's own photo (SC25Badge.png) and 3D-print STL filenames (Saintcon2025Nut.stl, NutBase, NutButton, NutRing, NutWithButtonHole) were found, no rendered/photographed image. The SAINTCON 2025 badge talk YouTube video likely has more detail but its page content could not be extracted via fetch.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2025/saintcon2025-nut-nfc-token-device-used-to-write-codes-onto-t.glb
  method: gerber
  source_file: Hardware/Nut/Saintcon2025NutGerbers.zip
  generated: '2026-09-10'
  bytes: 184340
  size_mm:
  - 100.0
  - 100.0
---

The Nut is a small NFC token built by SAINTCON badge designer compukidmike as the interactive piece of SAINTCON 2025's badge game. That year's conference badge was a comically oversized 50mm wrench with an NFC tag embedded in its head; the game required players to find and use Nuts around the venue, which wrote one-time codes onto the badge's NFC tag. Those codes were then checked in against a game server, awarding points or unlocking further game content.

Electronically, the Nut is built around an ESP32-C3 with an NXP PTX105R NFC reader/writer (SPI), an ATECC608A secure element, six addressable status LEDs, an MCP23x17 I/O expander, and a physical button, and it joined the conference Wi-Fi network to talk to the game server. The 3D-printed enclosure parts (base, ring, button, and a button-hole variant of the main body) suggest the token was housed in a small printed case rather than a bare PCB.

Hardware (KiCad source, gerbers, and schematic) and firmware (ESP-IDF source) for the Nut are published in compukidmike's Saintcon2025 GitHub repository alongside the matching badge files, making the whole game system open source. No photo of the assembled Nut device, and no information on how many were made or how they were handed out, was found in the sources checked.
