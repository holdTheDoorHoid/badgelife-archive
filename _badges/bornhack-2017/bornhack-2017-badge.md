---
title: BornHack 2017 badge
id: bornhack-2017-bornhack-2017-badge
layout: badge
parent: BornHack 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2017
year: 2017
makers:
- name: BornHack
summary: The official electronic name badge for BornHack 2017, an irregularly-shaped hackable PCB with an OLED display, buttons, and a USB drag-and-drop bootloader.
functions: Runs user-written firmware; ships with example code and community-made demos (a snake game, a fish physics sim, a starfield effect) that attendees load via the drag-and-drop bootloader.
look:
  colors:
  - black
  - grey
  - white
  shape: irregular, outline echoes the island of Bornholm
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: EFM32HG322F64G (Silicon Labs "Happy Gecko", Cortex-M0+)
  leds: null
  display: 128x64 OLED, SSD1306 controller
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to all BornHack 2017 attendees as their event badge; worn on an included lanyard.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2017/tree/hardware
  firmware_url: https://github.com/bornhack/badge2017
  eda_tool: null
links:
- label: github.com/bornhack/badge2017
  url: https://github.com/bornhack/badge2017
  kind: repo
  archived: https://web.archive.org/web/20251124204348/https://github.com/bornhack/badge2017
- label: The BornHack 2017 Badge (Hackaday)
  url: https://hackaday.com/2017/08/15/the-latest-hacker-camp-badge-comes-from-bornhack/
  kind: article
  archived: https://web.archive.org/web/20260606074343/https://hackaday.com/2017/08/15/the-latest-hacker-camp-badge-comes-from-bornhack/
images:
- file: assets/images/badges/bornhack-2017/bornhack-2017-badge/a6b2ed0914.jpg
  source: https://hackaday.com/2017/08/15/the-latest-hacker-camp-badge-comes-from-bornhack/
  credit: Hackaday / BornHack
  caption: The BornHack 2017 badge PCB with OLED display and buttons
  archived: https://web.archive.org/web/20260606074343/https://hackaday.com/2017/08/15/the-latest-hacker-camp-badge-comes-from-bornhack/
contact: {}
notes:
- Official electronic name badge for BornHack 2017 built around a Silicon Labs EFM32HG322F64G (Happy Gecko) Cortex-M0+ MCU with a 128x64 SSD1306 OLED display, drag-and-drop USB mass-storage bootloader, and irregular PCB shape meant for attendees to hack/modify. Found by the event-year sweep, task bornhack-2017.
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2017
  title: BornHack 2017 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bornhack-2017); event read as ''bornhack-2017''.'
  archived: https://web.archive.org/web/20251124204348/https://github.com/bornhack/badge2017
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2017/master/README.md
  title: bornhack/badge2017 README
  accessed: '2026-09-08'
  note: Confirmed MCU, display, buttons, USB bootloader workflow (badge.xil.se online IDE, drag files to GECKOBOOT drive), and geckonator firmware library; hardware files live in a separate `hardware` branch.
- kind: url
  url: https://hackaday.com/2017/08/15/the-latest-hacker-camp-badge-comes-from-bornhack/
  title: The Latest Hacker Camp Badge Comes From BornHack
  accessed: '2026-09-08'
  note: Confirmed irregular PCB shape, low-power/bootloader design priority, battery holder and prototyping area on the back, and provided the badge photo used here.
  archived: https://web.archive.org/web/20260606074343/https://hackaday.com/2017/08/15/the-latest-hacker-camp-badge-comes-from-bornhack/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: No price or unit count is published anywhere found; the badge was a free giveaway to all attendees (ticket price only), so get_one.price/quantity are left empty. LED presence not documented in any source, so tech.leds stays null. Battery type/capacity not stated beyond "battery holders...on the back side" (Hackaday), so tech.battery is left null rather than guessed. BornHack's own 2017-08-14 news post (bornhack.dk) returned a server error both via WebFetch and curl and could not be checked.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bornhack-2017/bornhack-2017-badge.glb
  method: kicad
  source_file: Bornhack Make Tradition Badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 291700
---

The BornHack 2017 badge was the official electronic name badge handed to every attendee of BornHack, the Danish hacker camp held on the island of Bornholm. Built around a Silicon Labs EFM32HG322F64G "Happy Gecko" Cortex-M0+ microcontroller, it pairs a 128x64 SSD1306 OLED display with a handful of buttons on an irregularly-shaped PCB whose outline nods to the island itself. A row of battery holders and a bare prototyping area occupy the back of the board, leaving the front dedicated to the display, buttons, and a micro-USB port.

The badge's headline feature is its bootloader: holding the BOOT button while plugging in USB makes the badge enumerate as a USB mass-storage device, and a compiled `.bin` firmware image can simply be dragged onto it to reflash the board, no separate programmer required. BornHack paired this with badge.xil.se, a browser-based IDE where attendees could write and compile code against the badge's `geckonator` register-wrapper library without installing a toolchain locally, alongside full instructions for building offline on Linux, macOS, and Windows.

Hardware and firmware are both open source: the firmware and example code live in the main `bornhack/badge2017` GitHub repository (GPL-3.0), while the PCB design files were split out into a separate `hardware` branch of the same repo. Community members used the badge as a small hacking platform during and after the event, producing example programs such as a Snake clone, a fish physics simulation, and a starfield effect that shipped as branches in the repository.

## Make your own

The firmware and example code are in the default branch of https://github.com/bornhack/badge2017; the PCB design files are in the repository's `hardware` branch. Programming requires an ARM `arm-none-eabi` GCC toolchain (or the badge.xil.se web IDE) to produce a `.bin` file, which is copied onto the `GECKOBOOT` mass-storage drive that appears when the badge's BOOT button is held while connecting USB.
