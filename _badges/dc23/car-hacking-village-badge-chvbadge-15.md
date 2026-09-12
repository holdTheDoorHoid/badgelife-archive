---
title: 'DEF CON 23 Car Hacking Village Badge: Capture the VIN'
id: dc23-car-hacking-village-badge-chvbadge-15
layout: badge
parent: DC23
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc23
year: 2015
makers:
- name: lanrat / Car Hacking Village
summary: A hackable badge for the DEF CON 23 Car Hacking Village, tied to a "Capture the VIN" game and scripted in the open-source, C-like PAWN language.
functions: Runs user-hackable PAWN scripts and exposes a CAN bus interface; can act as a CAN-based network interface in Linux via SocketCan. Used for a "Capture the VIN" hacking game/CTF, with classes taught on-site on how to hack the badge.
look:
  colors: []
  shape: null
  themes:
  - village badge
  - security
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed at the DEF CON 23 Car Hacking Village.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/lanrat/CHVBadge_15
  eda_tool: null
links:
- label: github.com/lanrat/CHVBadge_15
  url: https://github.com/lanrat/CHVBadge_15
  kind: repo
- label: DEF CON Forums - Car Hacking Village Capture The VIN Badge
  url: https://forum.defcon.org/node/221175
  kind: article
- label: 'YouTube: DEF CON 23 - Vehicle Hacking Village - Nathan Hoch - The Badge and PAWN'
  url: https://www.youtube.com/watch?v=nK4nufSjR3g
  kind: video
  archived: https://web.archive.org/web/20260218173934/https://www.youtube.com/watch?v=nK4nufSjR3g
images:
- file: assets/images/badges/dc23/car-hacking-village-badge-chvbadge-15/3eddbfdb02.jpg
  source: https://github.com/lanrat/CHVBadge_15
  credit: lanrat
  caption: Photo of the DEF CON 23 Car Hacking Village badge
contact: {}
notes:
- The archive sweep's original wording was "OBD2-plug-shaped village badge with CAN Bus header/jumper connections, scripted in Pawn on an STM32 Cortex-M0" — the STM32/Cortex-M0 chip claim and the OBD2-plug shape could not be confirmed from any source read; they are left out of tech.mcu and look.shape rather than guessed.
- Found by the event-year sweep, task dc23-all.
status: released
sources:
- kind: url
  url: https://github.com/lanrat/CHVBadge_15
  title: DEF CON 23 Car Hacking Village Badge (CHVBadge_15)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc23-all); event read as ''dc23''.'
- kind: url
  url: https://forum.defcon.org/node/221175
  title: Car Hacking Village Capture The VIN Badge - DEF CON Forums
  accessed: '2026-09-08'
  note: Confirms the badge name ("Capture the VIN"), that it runs the open-source PAWN scripting language, and that classes were taught on hacking it.
- kind: url
  url: https://www.youtube.com/watch?v=nK4nufSjR3g
  title: DEF CON 23 - Vehicle Hacking Village - Nathan Hoch - The Badge and PAWN
  accessed: '2026-09-08'
  note: Corroborates that the badge and its PAWN scripting were the subject of a DEF CON 23 talk/demo by Nathan Hoch.
  archived: https://web.archive.org/web/20260218173934/https://www.youtube.com/watch?v=nK4nufSjR3g
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via the maker's GitHub repo (README, pinout image, SocketCan doc) and a DEF CON forum thread that this is a real, hackable DEF CON 23 Car Hacking Village badge, informally called "Capture the VIN," that runs the PAWN scripting language and exposes CAN bus access (SocketCan-compatible over an FTDI serial link at 230400 baud). Could not confirm the MCU, LED count, display, battery/power, price, quantity made, or exact shape from any source read — the sweep's "STM32 Cortex-M0" / "OBD2-plug-shaped" claims are noted above but left unfilled since no source confirmed them. The GitHub repo has been archived (read-only) since 2019-05-13.
last_modified_date: '2026-09-08'
---

The DEF CON 23 (2015) Car Hacking Village badge, informally called "Capture the VIN," was a hackable badge tied to a CAN-bus hacking game run at the village. It was scriptable in PAWN, an open-source C-like scripting language, and the village ran classes teaching attendees how to hack the badge and use it to interact with a car's CAN bus. lanrat, a village contributor, published a companion GitHub repository with a Windows SDK, FTDI driver notes, serial settings (230400 baud, 8N1), a pinout diagram, and a guide for using the badge as a SocketCan-compatible CAN interface on Linux.

Specific hardware details — the MCU, LED and display configuration, battery, price, and production quantity — are not documented in any source found and are left blank rather than guessed. The GitHub repository has been archived (read-only) since May 2019, but remains available as a historical reference.

## Make your own

The firmware/tooling side is open: lanrat's repository (linked above) contains the Windows-based SDK, FTDI driver guidance, and a `BusPirate.md` / `SocketCan.md` set of docs for programming and interfacing with the badge. No hardware design files (schematic/PCB/Gerbers) were found.
