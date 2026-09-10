---
title: BornHack 2021 badge
id: bornhack-2021-bornhack-2021-badge
layout: badge
parent: Bornhack 2021
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: bornhack-2021
year: 2021
makers:
- name: BornHack
  url: https://github.com/bornhack
summary: A bare prototyping board rather than a full electronic badge, built around an SAO connector and a Qwiic/STEMMA QT connector with through-hole and SMD prototyping pads.
functions: No built-in functions of its own; attendees wired up their own circuits on the prototyping pads at the badge-hacking tent, using SAO and Qwiic breakouts as a starting point (some built simple blinkies).
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - kit
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Given to BornHack 2021 attendees as the year's conference badge.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2021
  firmware_url: null
  eda_tool: KiCad
  license: CC BY-SA 4.0
  notes: Repo requires KiCad nightly (5.99) to open; includes schematic, PCB layout, a PDF schematic, and a render.
links:
- label: github.com/bornhack/badge2021
  url: https://github.com/bornhack/badge2021
  kind: repo
  archived: https://web.archive.org/web/20251126063657/https://github.com/bornhack/badge2021
images:
- file: assets/images/badges/bornhack-2021/bornhack-2021-badge/d7275caa09.png
  source: https://github.com/bornhack/badge2021
  credit: BornHack
  caption: KiCad render of the BornHack 2021 SAO prototyping board badge
  archived: https://web.archive.org/web/20251126063657/https://github.com/bornhack/badge2021
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2021
  title: BornHack 2021 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''bornhack-2021''.'
  archived: https://web.archive.org/web/20251126063657/https://github.com/bornhack/badge2021
- kind: url
  url: https://hackaday.com/2021/09/03/the-bornhack-badge-gets-a-bubble/
  title: The BornHack Badge Gets A Bubble | Hackaday
  accessed: '2026-09-07'
  note: Confirms the 2021 badge was an SAO prototyping board (not a powered electronic badge) due to the chip shortage, and that attendees hacked on it at the camp.
  archived: https://web.archive.org/web/20260512004630/https://hackaday.com/2021/09/03/the-bornhack-badge-gets-a-bubble/
- kind: url
  url: https://hackaday.com/2021/08/31/reporting-from-bornhack-2021-hacker-camps-making-it-through-the-pandemic/
  title: 'Reporting From BornHack 2021: Hacker Camps Making It Through The Pandemic | Hackaday'
  accessed: '2026-09-07'
  note: Background on BornHack 2021 as an in-person camp during the pandemic; general context, no new badge specifics.
  archived: https://web.archive.org/web/20260514034229/https://hackaday.com/2021/08/31/reporting-from-bornhack-2021-hacker-camps-making-it-through-the-pandemic/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The 2021 badge was designed as a bare SAO prototyping board rather than a chip-based electronic badge, reportedly because of the semiconductor shortage that year (per Hackaday coverage) and because most attendees already had SAO-capable badges from 2019/2020. No MCU, LED, price, or production-quantity figures are published anywhere found. Designer is credited to the BornHack org account on GitHub; individual designer name not confirmed in sources checked.
last_modified_date: '2026-09-07'
model:
  file: assets/models/bornhack-2021/bornhack-2021-badge.glb
  method: kicad
  source_file: hex_diy.kicad_pcb
  generated: '2026-09-07'
  bytes: 352272
---

The BornHack 2021 badge broke from the event's usual pattern of a microcontroller-driven electronic badge. Facing the global chip shortage, the organizers instead handed out a bare prototyping board: a PCB with an SAO (Shitty/Simple Add-On) connector footprint and a Qwiic/STEMMA QT I2C connector, its signal lines broken out to a grid of through-hole and SMD prototyping pads. The reasoning, per contemporary Hackaday coverage, was partly necessity and partly practicality — most returning attendees already carried an SAO-equipped badge from BornHack 2019 or 2020, so a plain expansion platform let them keep building without needing new silicon.

At the camp's badge-hacking tent, discrete components were made available so attendees could wire up their own circuits directly on the board, from simple LED blinkies to more involved builds. One widely covered example combined the badge with a separate silicone "bubble" add-on incorporating its own microcontroller, pressure sensor, motor driver, LED, and small air pump, but that was an attendee project built on top of the platform rather than a feature of the badge itself.

Design files (KiCad schematic, PCB layout, and a PDF schematic reference) are published on GitHub under CC BY-SA 4.0, though the repository notes it requires a KiCad nightly build (5.99) to open correctly.

## Make your own

The hardware is fully open: clone [bornhack/badge2021](https://github.com/bornhack/badge2021), open the project in a KiCad 5.99 nightly build (later stable KiCad releases may not open it correctly), and fabricate from the included PCB layout. There is no firmware, since the board ships without a microcontroller — populate the SAO and Qwiic breakout pads with whatever components a given project calls for.
