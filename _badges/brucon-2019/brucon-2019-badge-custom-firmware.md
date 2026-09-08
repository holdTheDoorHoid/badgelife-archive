---
title: BruCON 2019 badge / custom firmware
id: brucon-2019-brucon-2019-badge-custom-firmware
layout: badge
parent: BruCON 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: brucon-2019
year: 2019
makers:
- name: virtualabs (community firmware for the official BruCON 2019 badge)
summary: Official BruCON 2019 conference badge (ESP32, Nokia-style LCD); security researcher virtualabs published an alternate open-source firmware for it built around a homemade Snake game.
functions: 'Custom firmware: a rewritten LCD driver with framebuffer support for fast screen refresh, and a Snake game inspired by the classic Nokia phone game (no font-rendering support was finished in time).'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - arcade
tech:
  mcu: ESP32
  leds: null
  display: Nokia-style LCD
  connectivity: []
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
  hardware_url: null
  firmware_url: https://github.com/virtualabs/brucon-2019/
  eda_tool: null
  license: MIT
  notes: Only the alternate firmware is published here; the badge's own hardware design files were not found.
links:
- label: github.com/virtualabs/brucon-2019
  url: https://github.com/virtualabs/brucon-2019/
  kind: repo
images: []
contact: {}
notes:
- BruCON 2019 conference badge with a Nokia-style LCD and ESP32 MCU, running custom open-source firmware including a Snake game. Found by the event-year sweep, task con-brucon.
- 'Sweep''s title was ''BruCON 2019 badge / custom firmware''; kept as-is since the repo itself has no separate project name beyond "Custom firmware for BruCON 2019 badge."'
status: listed
sources:
- kind: url
  url: https://github.com/virtualabs/brucon-2019/
  title: BruCON 2019 badge / custom firmware
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-brucon); event read as ''BruCON 2019''.'
- kind: url
  url: https://github.com/virtualabs/brucon-2019/
  title: 'virtualabs/brucon-2019: Custom firmware for BruCON 2019 badge'
  accessed: '2026-09-08'
  note: Confirmed MCU (ESP32), display (Nokia-style LCD), MIT license, and firmware features (LCD driver rewrite, framebuffer, Snake game, no font support).
- kind: url
  url: https://raw.githubusercontent.com/virtualabs/brucon-2019/master/README.md
  title: Brucon 2019 Badge Snake game (README)
  accessed: '2026-09-08'
  note: Primary source for the firmware's functions text and the developer's own description of the project.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: The repo (maker's own words) confirms the badge used an ESP32 and a Nokia-style LCD, and describes the Snake-game firmware in detail. Could not find who designed/manufactured the official BruCON 2019 badge hardware itself, nor any photos of the badge, nor price/quantity/distribution details (it was presumably given to attendees, but that is not confirmed). No hardware design files were found, only the firmware. Searched BruCON's own 2019 archive site (archive.brucon.org/2019) but it has no badge-specific page.
last_modified_date: '2026-09-08'
---

The BruCON 2019 conference badge was built around an ESP32 microcontroller driving a Nokia-style LCD screen. Security researcher virtualabs published an alternate, open-source firmware for the badge on GitHub, centered on a homemade Snake game inspired by the classic game from Nokia phones. The firmware includes a rewritten LCD driver with framebuffer support for faster screen refresh, though the developer notes it ran out of time to add font rendering, and that the Snake implementation is "not optimized and does not match the original."

The firmware is released under the MIT license and is meant to be built with Espressif's ESP32 development kit. No hardware design files for the badge itself were found alongside it — this project covers only the alternate firmware, not the badge's PCB or the identity of whoever designed and manufactured the official hardware.

## Make your own

Install the Espressif IoT Development Framework (ESP-IDF) for ESP32, clone the [virtualabs/brucon-2019](https://github.com/virtualabs/brucon-2019/) repository, and build/flash the firmware to a BruCON 2019 badge using the standard ESP-IDF toolchain.
