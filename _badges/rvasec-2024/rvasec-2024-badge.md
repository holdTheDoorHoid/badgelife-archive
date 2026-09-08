---
title: 'R.O.V.E.R. (RVAsec 2024 Badge)'
id: rvasec-2024-rvasec-2024-badge
layout: badge
parent: RVAsec 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2024
year: 2024
makers:
- name: HackRVA
  url: https://github.com/HackRVA
summary: HackRVA's 2024 RVAsec conference badge, a handheld game-console-style badge named R.O.V.E.R. (Remotely Operable Vehicle for Exploratory Research) with a color LCD, D-pad, and two action buttons.
functions: Runs custom badge apps (games, tools) loaded via a firmware image; supports IR transmit/receive for badge-to-badge communication and includes a rotary encoder, buttons, D-pad, audio output, and a serial/CLI interface for development. A desktop simulator (SDL2-based) lets developers test apps without hardware.
look:
  colors:
  - white
  - black
  shape: null
  themes:
  - console
  - arcade
  form_factor: pcb badge
tech:
  mcu: RP2040 (Raspberry Pi Pico)
  leds:
    count: null
    type: null
    note: At least one 3-color (RGB) status LED, plus separate discrete LEDs near the screen.
  display: color LCD (small square TFT, exact size not stated)
  connectivity:
  - ir
  - usb
  inputs:
  - buttons
  - d-pad
  - rotary encoder
  - microphone
  battery: null
  power: micro USB
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: https://github.com/HackRVA/badge2024
  eda_tool: null
  notes: Firmware, build instructions, and a BADGE-APP-HOWTO.md guide for writing custom apps are published on GitHub, along with a desktop simulator. No separate hardware/schematic repo was found linked from this project; the firmware repo does not appear to include KiCad/Gerber files itself.
links:
- label: github.com/HackRVA/badge2024
  url: https://github.com/HackRVA/badge2024
  kind: repo
images:
- file: assets/images/badges/rvasec-2024/rvasec-2024-badge/40cbae72b2.jpg
  source: "https://github.com/HackRVA/badge2024"
  credit: "HackRVA"
  caption: "The HackRVA 2024 badge (R.O.V.E.R.), showing the LCD screen, D-pad, A/B buttons, and micro USB port"
contact: {}
notes:
- HackRVA badge firmware and emulator for RVAsec 2024, demoed on YouTube. Found by the event-year sweep, task con-rvasec.
- 'The sweep''s title read simply "RVAsec 2024 Badge"; the maker''s repo and silkscreen name the badge "R.O.V.E.R." (Remotely Operable Vehicle for Exploratory Research), so the title above uses that name with the sweep''s generic label kept as a parenthetical.'
status: released
sources:
- kind: url
  url: https://github.com/HackRVA/badge2024
  title: RVAsec 2024 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2024''.'
- kind: url
  url: https://github.com/HackRVA/badge2024
  title: HackRVA/badge2024 — README and repo contents
  accessed: '2026-09-08'
  note: Confirmed maker (HackRVA), event/year (RVAsec 2024), MCU (RP2040/Pico), display, D-pad, IR, rotary encoder, audio, micro USB flashing procedure, and that firmware/simulator source is open. Also the source of the badge photo (images/badge-image-1024.png) and the "R.O.V.E.R." name found in that image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed as a real, released badge via the maker's own GitHub repo (firmware, build docs, and a photo of the assembled board). Could not find a separate hardware/schematic repo, pricing, quantity made, or distribution details (RVAsec badges are typically given to attendees/volunteers rather than sold, but this was not stated anywhere found). LED count/type and exact display size are visible in the photo but not specified in text sources, so left unset rather than guessed. No storefront, Hackaday.io page, or press coverage found in a couple of searches.
last_modified_date: '2026-09-08'
---

HackRVA, the Richmond, Virginia hacker collective behind RVAsec's badge each year, built a handheld game-console-style badge for RVAsec 2024. It runs on a Raspberry Pi Pico (RP2040) and centers on a small color LCD flanked by a soldered D-pad and two action buttons (A/B), with a micro USB port for power and firmware flashing. The board's silkscreen names it "R.O.V.E.R." — Remotely Operable Vehicle for Exploratory Research — even though HackRVA's own repo and the sweep that found it both refer to it more generically as "RVAsec Badge 2024."

Beyond the core input/display hardware, the badge includes an IR transmitter/receiver for badge-to-badge interaction, a rotary encoder, a status LED, a microphone, and audio output, with HackRVA's firmware repo describing the LED, input, IR, encoder, and audio subsystems as functional at time of writing (with audio/jack input and some extensions still noted as in-progress).

## Make your own

HackRVA published the badge's firmware source, a CMake-based build setup for both the physical hardware and a desktop SDL2 simulator, and a detailed `BADGE-APP-HOWTO.md` guide for writing custom badge apps, all in the `HackRVA/badge2024` GitHub repository. Flashing is done by holding a button near the screen while plugging in a micro USB cable, which mounts the Pico as a USB storage device that a compiled `.uf2` firmware file is copied onto. No separate schematic/PCB (hardware-design) repository was found linked from the project, so it is treated here as firmware-open rather than fully hardware-open.
