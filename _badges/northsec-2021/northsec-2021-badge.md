---
title: NorthSec 2021 Badge
id: northsec-2021-northsec-2021-badge
layout: badge
parent: NorthSec 2021 (remote/virtual)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2021
year: 2021
makers:
- name: NorthSec
  url: https://nsec.io/
summary: The official electronic badge for NorthSec 2021, an ESP32-based board with a color screen and an onboard RPG-style CTF hiding ten flags.
functions: Boots into a medieval-themed RPG-style game on its color screen; ten hidden flags spread across the game map and a CLI reachable over serial, solvable for Discord roles without giving any advantage in the main NorthSec CTF.
look:
  colors: []
  shape: null
  themes:
  - ctf
  - fantasy
  - security
tech:
  mcu: ESP32
  leds:
    count: 15
    type: NeoPixel
    note: ''
  display: color LCD
  connectivity:
  - wifi
  - bluetooth
  - ble
  - uart
  battery: null
  sao_version: null
get_one:
  price: $60
  price_usd: 60
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold through NorthSec's online shop around the (remote) 2021 event.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/nsec/nsec-badge
  firmware_url: https://github.com/nsec/nsec-badge
  eda_tool: null
links:
- label: boschko.ca/northsec-2021-badge-writeup
  url: https://boschko.ca/northsec-2021-badge-writeup/
  kind: website
- label: nsec.io/badge2021
  url: https://nsec.io/badge2021/
  kind: website
- label: github.com/nsec/nsec-badge
  url: https://github.com/nsec/nsec-badge
  kind: repo
- label: 'erichogue.ca: NorthSec 2021 Badge Writeup - Part 1'
  url: https://erichogue.ca/2021/05/NorthSec2021BadgeFirstFlags/
  kind: article
images:
- file: assets/images/badges/northsec-2021/northsec-2021-badge/a5afab531f.jpg
  source: https://nsec.io/badge2021/
  credit: NorthSec
  caption: Official NorthSec 2021 electronic badge
contact: {}
notes:
- Official NorthSec 2021 badge, issued despite the conference running fully remote for the second year of the pandemic; formed the basis of a set of badge-specific CTF challenges. Found by the event-year sweep, task northsec.
- The NorthSec GitHub repo (nsec/nsec-badge) is a living repository reused year to year; its current default branch documents the 2025 badge (ESP32-C3, 18 LEDs, 5 buttons), not the 2021 hardware, so tech fields here rely on NorthSec's own 2021 badge page and third-party writeups rather than the repo as it stands today.
status: released
sources:
- kind: url
  url: https://boschko.ca/northsec-2021-badge-writeup/
  title: NorthSec 2021 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:northsec); event read as ''northsec-2021''.'
- kind: url
  url: https://nsec.io/badge2021/
  title: Badge 2021 • NorthSec
  accessed: '2026-09-08'
  note: 'Maker''s own badge page: ESP32, 15 NeoPixels, color display, WiFi/BLE/classic BT, unlocked flash, firmware/schematics promised on GitHub after the event.'
- kind: url
  url: https://github.com/nsec/nsec-badge
  title: nsec/nsec-badge
  accessed: '2026-09-08'
  note: NorthSec badge repo (open source, multiple licenses); default branch currently documents the 2025 hardware revision, not 2021.
- kind: url
  url: https://erichogue.ca/2021/05/NorthSec2021BadgeFirstFlags/
  title: NorthSec 2021 Badge Writeup - Part 1 - First Flags
  accessed: '2026-09-08'
  note: Confirms $60 price sold through NorthSec's online shop, and the RPG game / ten-flag CTF layer separate from the main competition.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Core facts (MCU, LEDs, display, connectivity, price, CTF structure) confirmed by NorthSec's own 2021 badge page plus two independent attendee writeups. Exact LED type model (NeoPixel is a brand, not a specific part number), display panel size/part, button count, battery/power option, EDA tool, and quantity made were not stated by any source found and are left empty rather than guessed. availability set to sold_out since this was a one-time 2021 event sale with no indication of ongoing sales.
last_modified_date: '2026-09-10'
model:
  file: assets/models/northsec-2021/northsec-2021-badge.glb
  method: kicad
  source_file: hw/2025/nsec-badge-2025.kicad_pcb
  generated: '2026-09-10'
  bytes: 566028
---

NorthSec held its 2021 edition fully remotely for the second year running, but the crew built and sold a real electronic badge anyway: an ESP32-based board with a color screen, 15 NeoPixel RGB LEDs, Wi-Fi and both classic and low-energy Bluetooth, and a UART serial port left open for tinkering (NorthSec noted the flash was not locked, inviting custom firmware). It sold through NorthSec's online shop for $60 around the event.

Rather than gating any part of the main CTF, the badge carried its own self-contained layer of fun: powering it on drops the holder into a small medieval-themed RPG rendered on the screen, with ten flags hidden across the game world and reachable partly through a CLI over the serial connection. Solving them earned Discord roles rather than competition points. Attendees documented reverse-engineering the firmware and game logic in detail (Eric Hogue's multi-part writeup, and a separate walkthrough by Marc-André Boschko), and NorthSec's own competition write-ups page credits several people for the badge's firmware RE and main-flag challenges.

## Make your own

NorthSec publishes badge hardware and firmware in the `nsec/nsec-badge` GitHub repository under open licenses, and said at the time that 2021 schematics and source would follow shortly after the event. That repository is reused year over year, though, and its current default branch documents a later (2025) hardware revision rather than the 2021 board, so anyone wanting the exact 2021 files should check the repo's history/tags for that year's directory rather than the README as it reads today.
