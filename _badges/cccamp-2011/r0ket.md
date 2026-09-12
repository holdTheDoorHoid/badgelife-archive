---
title: r0ket
id: cccamp-2011-r0ket
layout: badge
parent: Chaos Communication Camp 2011
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cccamp-2011
year: 2011
makers:
- name: Team r0ket (hme et al.)
summary: The official electronic badge of Chaos Communication Camp 2011 (and the 28th Chaos Communication Congress), and a full-featured ARM microcontroller dev board in its own right.
functions: Runs user-written "l0dables" (loadable programs); demos and community software include games such as a Space Invaders clone. Communicates with other r0kets over its onboard 2.4GHz radio.
look:
  colors:
  - black
  shape: rocket
  themes:
  - space
  - hardware tool
tech:
  mcu: LPC1343 (32-bit ARM Cortex-M3, 32KB flash, 8KB SRAM, USB device)
  leds:
    count: 4
    type: discrete
    note: three green (bottom-left, top-left, bottom-right) and one red (top-right) indicator LEDs
  display: 96x68 monochrome (green) LCD, Nokia 1200 panel with Philips PCF8814 controller
  connectivity:
  - usb
  - i2c
  battery: custom 3.7V 600mAh rechargeable LiPo
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/r0ket/r0ket
  firmware_url: https://github.com/r0ket/r0ket
  eda_tool: null
links:
- label: github.com/r0ket/r0ket
  url: https://github.com/r0ket/r0ket
  kind: repo
  archived: https://web.archive.org/web/20260603192725/https://github.com/r0ket/r0ket
- label: r0ket wiki (badge.events.ccc.de)
  url: https://r0ket.badge.events.ccc.de/
  kind: doc
  archived: https://web.archive.org/web/20260713154947/https://r0ket.badge.events.ccc.de/
- label: r0ket hardware specs
  url: https://r0ket.badge.events.ccc.de/hardware
  kind: doc
  archived: https://web.archive.org/web/20260509205607/https://r0ket.badge.events.ccc.de/hardware
images:
- file: assets/images/badges/cccamp-2011/r0ket/34d95bab03.jpg
  source: https://r0ket.badge.events.ccc.de/
  credit: r0ket project / CCC
  caption: r0ket badge, rocket-shaped PCB with monochrome LCD showing a Space Invaders demo
  archived: https://web.archive.org/web/20260713154947/https://r0ket.badge.events.ccc.de/
contact: {}
notes:
- Sweep (task cccamp) originally described this as "an ARM-based microcontroller dev board with e-paper-style display, ~3000 units distributed" — the ARM/dev-board part checks out, but the display is a standard monochrome LCD (not e-paper), and no source found confirms a unit count, so quantity is left blank rather than guessed.
status: released
sources:
- kind: url
  url: https://github.com/r0ket/r0ket
  title: r0ket
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:cccamp); event read as ''cccamp-2011''.'
  archived: https://web.archive.org/web/20260603192725/https://github.com/r0ket/r0ket
- kind: url
  url: https://github.com/hme/r0ket
  title: hme/r0ket
  accessed: '2026-09-08'
  note: README confirms the r0ket was the badge for both Chaos Communication Camp 2011 and 28C3 (28th Chaos Communication Congress); repo is open source.
- kind: url
  url: https://r0ket.badge.events.ccc.de/hardware
  title: hardware [r0ket]
  accessed: '2026-09-08'
  note: 'Official hardware spec page: LPC1343 MCU, Nokia 1200/PCF8814 LCD, 4 LEDs, nRF24L01+ radio, LiPo battery, AT45DB041B flash, five-way nav switch, m0dulbus/Hackerbus expansion.'
  archived: https://web.archive.org/web/20260509205607/https://r0ket.badge.events.ccc.de/hardware
- kind: url
  url: https://r0ket.badge.events.ccc.de/
  title: start [r0ket]
  accessed: '2026-09-08'
  note: Confirms it is a badge/dev-board platform running loadable "l0dables"; source of the Space Invaders photo.
  archived: https://web.archive.org/web/20260713154947/https://r0ket.badge.events.ccc.de/
- kind: url
  url: https://badge.gallery/series/ccc-camp
  title: Chaos Communication Camp - Hacker Con Badges
  accessed: '2026-09-08'
  note: Third-party confirmation of event/year and that r0ket established the CCC Camp badge tradition rad1o later continued.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (event, MCU, display, LEDs, radio, battery, storage, open-source status) confirmed on the maker's own wiki and GitHub repo. Price, quantity made, and distribution method were not stated on any source found and are left blank. sao_version left null since this is a standalone badge, not an SAO host (no SAO header mentioned in the hardware docs). connectivity limited to usb/i2c per the controlled vocabulary; the nRF24L01+ 2.4GHz radio and m0dulbus/Hackerbus expansion (SPI, I2C, GPIO) are noted in tech.leds-adjacent free text and functions/summary instead since "rf" and "spi" are not in the connectivity vocabulary list.
last_modified_date: '2026-09-08'
---

The r0ket was the official electronic badge of Chaos Communication Camp 2011, and was also used as the badge for the 28th Chaos Communication Congress (28C3) later that year. Built around an NXP LPC1343 ARM Cortex-M3 microcontroller, it doubles as a general-purpose development board: a Nokia 1200-style monochrome LCD, a five-way navigation switch, four status LEDs, an nRF24L01+ 2.4GHz radio for badge-to-badge communication, onboard serial flash, and an optional micro SD slot round out the hardware. The PCB itself is cut in the shape of a small rocket.

Software for the r0ket runs as "l0dables" — small loadable programs users write and load onto the badge — and the community produced a range of demos and games, including a Space Invaders-style game shown running on the badge's LCD in the project's own promotional photo. Both the hardware design and firmware are published on GitHub (r0ket/r0ket), and the project is frequently cited as the badge that established the long-running CCC Camp electronic badge tradition, continued by later badges such as rad1o (2015), card10 (2019), and flow3r (2023).

No source found during this research states the exact production quantity, retail price, or how units were distributed to attendees (sold, included with a ticket, etc.); these fields are left blank pending a better source.
