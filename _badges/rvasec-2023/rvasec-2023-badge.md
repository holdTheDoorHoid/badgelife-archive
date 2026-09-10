---
title: RVAsec 2023 Badge
id: rvasec-2023-rvasec-2023-badge
layout: badge
parent: RVAsec 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2023
year: 2023
makers:
- name: HackRVA
  url: https://www.hackrva.org/badge/
summary: An RP2040-based electronic badge for RVAsec 2023 with an LCD display, three-color LED, D-pad, rotary encoder, IR transceiver and audio output, running a suite of built-in games and apps.
functions: Runs multiple games and apps on the badge OS, including Asteroids, Pong, a maze game, and a Magic 8 Ball; supports adding custom apps via the badge's app framework.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - console
  - arcade
tech:
  mcu: RP2040
  leds:
    count: null
    type: RGB
    note: Described by the maker as a "three-color LED".
  display: LCD display (size not specified)
  connectivity:
  - ir
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - free_drop
  where: Distributed to RVAsec 2023 attendees; described by a third-party source as a limited hotel-package item.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HackRVA/badge2023
  eda_tool: null
links:
- label: badge.gallery/badges/rvasec-2023-badge
  url: https://badge.gallery/badges/rvasec-2023-badge
  kind: website
- label: HackRVA/badge2023 (firmware repo)
  url: https://github.com/HackRVA/badge2023
  kind: repo
- label: hack.RVA badge program
  url: https://www.hackrva.org/badge/
  kind: website
- label: InfoConDB - RVAsec 2023
  url: https://infocondb.org/con/rvasec/rvasec-2023/
  kind: doc
images: []
contact: {}
notes:
- HackRVA electronic badge for RVAsec 2023, also demoed via the HackRVA badge wiki/simulator. Found by the event-year sweep, task con-rvasec. Confirmed real via badge.gallery and the HackRVA firmware repository on GitHub.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/rvasec-2023-badge
  title: RVAsec 2023 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2023''.'
- kind: url
  url: https://badge.gallery/badges/rvasec-2023-badge
  title: RVAsec 2023 Badge - badge.gallery
  accessed: '2026-09-10'
  note: Confirmed the badge exists and supplied features (LCD, three-color LED, D-pad, IR Tx/Rx, rotary encoder, audio out), RP2040 MCU, and that it was a limited hotel-package item.
- kind: url
  url: https://github.com/HackRVA/badge2023
  title: HackRVA/badge2023
  accessed: '2026-09-10'
  note: Maker's own firmware repository; confirmed RP2040 (Raspberry Pi Pico) hardware, open-source firmware in C/CMake, and the list of hardware features (LCD, 3-color LED, D-pad, IR, rotary encoder, audio out).
- kind: url
  url: https://www.hackrva.org/badge/
  title: Badge - hack.RVA
  accessed: '2026-09-10'
  note: Maker's general badge program page; did not carry photos confirmed to be the 2023 badge specifically, so no images were saved from it.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Core facts (maker, MCU, features, open firmware) confirmed by the maker's own GitHub repo and corroborated by badge.gallery. Price, quantity made, exact display size, LED count, and battery/power details were not stated by any source found and are left empty. No image could be confirmed as depicting this specific year's badge (rather than a different year's badge or a generic HackRVA photo), so images were left empty per the never-invent rule.
last_modified_date: '2026-09-10'
---

The RVAsec 2023 badge is an electronic conference badge built by HackRVA, the Richmond, Virginia hacker collective that has produced RVAsec's badge nearly every year since 2012. It is built around a Raspberry Pi Pico (RP2040 microcontroller) and packs an LCD display, a three-color LED, a D-pad, a rotary encoder, an IR transmitter/receiver, and audio output. The badge ships with a small suite of built-in games and apps, including Asteroids, Pong, a maze game, and a Magic 8 Ball, and can be reprogrammed over micro-USB using UF2 flashing.

The firmware is fully open source, published by HackRVA on GitHub as `badge2023`, written in C and built with CMake; the repository also supports building a Linux/Mac simulator (using SDL2) so developers can write and test custom apps without needing the physical hardware. Hardware design files (schematics/PCB) were not found published alongside the firmware at the time of this research.

Per a third-party badge-tracking site, the badge was distributed to attendees as part of a limited hotel-package registration bundle rather than sold separately; exact quantities and pricing were not stated by any source consulted.
