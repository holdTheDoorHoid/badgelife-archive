---
title: Atari Emulator for Hackaday Badge
id: hackaday-belgrade-2018-atari-emulator-for-hackaday-badge
layout: badge
parent: Hackaday Belgrade 2018
grand_parent: Badge Archive
nav_exclude: true
type: other
event: hackaday-belgrade-2018
year: 2018
makers:
- name: Max
  url: https://hackaday.io/Shmuma
summary: An unofficial Atari 2600 emulator firmware for the 2018 Hackaday Belgrade badge, running the 6502 CPU and a basic TIA graphics implementation.
functions: Emulates enough of the Atari 2600 (6502 CPU, basic TIA video with WSYNC/COLUBK handling, NTSC palette) to run simple 4K cartridge ROMs linked directly into the firmware; the badge's 8MB flash could in principle hold around 2,000 such ROMs.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - console
  - arcade
tech:
  mcu: PIC32MX370
  leds: null
  display: full-color graphics screen (badge's built-in display)
  connectivity: []
  battery: powered by host badge
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
  firmware_url: https://github.com/Shmuma/basic-badge/tree/atari
  eda_tool: null
links:
- label: hackaday.io/project/166288-atari-emulator-for-hackaday-badge
  url: https://hackaday.io/project/166288-atari-emulator-for-hackaday-badge
  kind: hackaday
- label: Shmuma/basic-badge (atari branch)
  url: https://github.com/Shmuma/basic-badge/tree/atari
  kind: repo
images:
- file: assets/images/badges/hackaday-belgrade-2018/atari-emulator-for-hackaday-badge/ba0f13fe29.jpg
  source: "https://hackaday.io/project/166288-atari-emulator-for-hackaday-badge"
  credit: "Max (Shmuma)"
  caption: "Atari emulator running on the Hackaday Belgrade 2018 badge"
contact: {}
notes:
- The discovery sweep filed this under supercon-2018; the project is actually built for the "2018 Hackaday Belgrade Hardware Badge" (hardware lead Voja Antonic, software lead Jaromir Sukuba), a PIC32MX370-based badge handed out at Hackaday Belgrade 2018, not a Superconference badge.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/166288-atari-emulator-for-hackaday-badge
  title: Atari Emulator for Hackaday Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2018); event read as ''supercon-2018''.'
- kind: url
  url: https://hackaday.io/project/166288-atari-emulator-for-hackaday-badge
  title: Atari Emulator for Hackaday Badge (project page)
  accessed: '2026-09-10'
  note: Confirmed maker (Max / Shmuma), target hardware (Hackaday Badge, PIC32MX370), feature set, and creation date (June 28, 2019); links to the firmware repo.
- kind: url
  url: https://github.com/Shmuma/basic-badge/tree/atari
  title: Shmuma/basic-badge, atari branch
  accessed: '2026-09-10'
  note: Confirmed the target badge is the "2018 Hackaday Belgrade Hardware Badge" (Voja Antonic hardware, Jaromir Sukuba software), MCU PIC32MX370F512H, and that this is a fork/branch of the badge's stock BASIC-interpreter firmware.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, host hardware, feature set) come from the maker''s own project page and repo, but price, quantity, and whether the emulator firmware was ever distributed beyond the repo/project page are not stated anywhere found. No standalone photo of just the emulator UI was available beyond the project''s hero image; treat the display/LED fields as describing the host badge, not an add-on board, since this is firmware for the existing hardware rather than a separate physical item.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/supercon-2018/atari-emulator-for-hackaday-badge/
---

Max (Hackaday.io user Shmuma) built an unofficial Atari 2600 emulator as custom firmware for the 2018 Hackaday Belgrade badge, a PIC32MX370-based pocket-computer badge designed by Voja Antonic (hardware) and Jaromir Sukuba (software) for Hackaday Belgrade 2018. The project, started in mid-2019 as a fork of the badge's stock BASIC-interpreter firmware, implements a basic 6502 CPU core and a minimal TIA graphics chip (handling WSYNC and COLUBK) with an NTSC color palette, enough to run simple 4K Atari cartridge ROMs linked directly into the firmware image.

At the point captured by available sources the project was explicitly a work in progress: CPU instruction timing, sprite rendering, PIA input registers, sound, and a proper ROM-loading scheme (rather than ROMs compiled into the firmware) were all listed as still to do. There is no evidence found of the emulator being packaged, sold, or distributed as a finished product — it reads as a solo hobby project built for and shared with the existing Hackaday Belgrade badge community, with the source available on GitHub.
