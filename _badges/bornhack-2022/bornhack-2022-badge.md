---
title: BornHack 2022 badge
id: bornhack-2022-bornhack-2022-badge
layout: badge
parent: Bornhack 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2022
year: 2022
makers:
- name: BornHack
  url: https://bornhack.dk/
summary: 'The "Game On" badge for BornHack 2022: a small handheld-controller-shaped board with a color LCD in the middle, built around a Raspberry Pi RP2040 and preloaded with CircuitPython for writing homebrew games.'
functions: Runs homebrew games and other CircuitPython projects on its color LCD; navigation buttons for input; a prototyping area with I/O hookup points for adding a custom joystick or sensors via crocodile clips, conductive thread, or wire.
look:
  colors: []
  shape: null
  themes:
  - console
  - retro computer
  - arcade
tech:
  mcu: RP2040
  leds: null
  display: 0.96" color LCD (ST7735S)
  connectivity:
  - i2c
  battery: 2x AA or USB-C
  sao_version: v1.96bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Given out to attendees of BornHack 2022; not otherwise sold.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2022
  firmware_url: https://github.com/bornhack/badge2022
  eda_tool: KiCad
links:
- label: github.com/bornhack/badge2022
  url: https://github.com/bornhack/badge2022
  kind: repo
  archived: https://web.archive.org/web/20251125153035/https://github.com/bornhack/badge2022
- label: 'Hackaday: Badges Of 2022: BornHack'
  url: https://hackaday.com/2022/07/08/badges-of-2022-bornhack/
  kind: article
  archived: https://web.archive.org/web/20260717220114/https://hackaday.com/2022/07/08/badges-of-2022-bornhack/
- label: 'Adafruit blog: The BornHack 2022 Game On Badge'
  url: https://blog.adafruit.com/2022/07/08/the-bornhack-2022-game-on-badge-circuitpython-piday-rp2040-raspberry_pi/
  kind: article
images:
- file: assets/images/badges/bornhack-2022/bornhack-2022-badge/d36d03c64c.jpg
  source: https://github.com/bornhack/badge2022
  credit: BornHack
  caption: Front of the BornHack 2022 Game On badge, showing the color LCD screen and navigation buttons
  archived: https://web.archive.org/web/20251125153035/https://github.com/bornhack/badge2022
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2022
  title: BornHack 2022 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''bornhack-2022''.'
  archived: https://web.archive.org/web/20251125153035/https://github.com/bornhack/badge2022
- kind: url
  url: https://hackaday.com/2022/07/08/badges-of-2022-bornhack/
  title: 'Badges Of 2022: BornHack'
  accessed: '2026-09-07'
  note: Confirmed the badge is exclusive to attendees at the event; general description of the console form factor.
  archived: https://web.archive.org/web/20260717220114/https://hackaday.com/2022/07/08/badges-of-2022-bornhack/
- kind: url
  url: https://blog.adafruit.com/2022/07/08/the-bornhack-2022-game-on-badge-circuitpython-piday-rp2040-raspberry_pi/
  title: The BornHack 2022 Game On Badge
  accessed: '2026-09-07'
  note: Confirmed MCU, flash, display, connectors, power, prototyping area, and CircuitPython preload.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No price, LED count/type, or exact production quantity found in any source; left empty rather than guessed. Distribution appears to be free/included for attendees (not sold), based on Hackaday's "the only way to get your hands on one is to go to the event") but no source states this explicitly as a giveaway policy, so get_one.distribution was left empty rather than guessed.
last_modified_date: '2026-09-07'
model:
  file: assets/models/bornhack-2022/bornhack-2022-badge.glb
  method: kicad
  source_file: game-on.kicad_pcb
  generated: '2026-09-07'
  bytes: 440924
---

The BornHack 2022 "Game On" badge is a handheld-controller-shaped board built by the BornHack team around a Raspberry Pi RP2040 microcontroller, with 16MB of QSPI flash and a color LCD (ST7735S) in the middle of the board. It ships preloaded with CircuitPython, so attendees can start writing their own games and tools with just a USB-C cable and a text editor, no toolchain setup required.

Beyond the screen and navigation buttons, the badge carries a standard SAO v1.96bis connector and a Qwiic/Stemma QT (I2C) connector for hooking up modules from those ecosystems, plus a bare prototyping area on one side with I/O hookup points meant for crocodile clips, conductive thread, or wire — intended for things like a homemade joystick. It can run on 2x AA batteries or USB-C power, and has M3 mounting holes for expansion boards or cases. The badge was distributed to BornHack 2022 attendees; it was not sold as a separate product. Community-built software for it has included a video player, an AM radio transmitter, and small games like Flappy Bird and Pac-Man clones, and a Survivator arcade game.

## Make your own

The hardware (KiCad v6 schematics and PCB) and firmware are published in the [badge2022 GitHub repository](https://github.com/bornhack/badge2022) under a Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license, including a firmware.uf2 for reflashing.
