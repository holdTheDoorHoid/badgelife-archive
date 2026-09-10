---
title: Hacker Hotel 2023 Badge
id: other-hacker-hotel-2023-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2023
makers:
- name: Pim
  role: lead, hardware and software
- name: Sake
  role: challenges/puzzle design
- name: Nikolett S.
  url: https://www.ankhaneko.art/
  role: artwork
summary: The official badge for Hacker Hotel 2023 (Netherlands), an RP2040-based puzzle device styled as an ancient stone tablet, used to run a venue-wide treasure hunt and a challenge-response text adventure.
functions: Doubles as event ID and game device. A row of buttons/LEDs acts as the "data and address lines" of a small computer that attendees use to enter codes found around the venue; solving the puzzle unlocks a bonus text adventure played over USB serial. Firmware is MicroPython, updated via .uf2 files over the RP2040's native USB bootloader.
look:
  colors:
  - blue
  - gold
  shape: rectangle
  themes:
  - puzzle
  - ctf
  - retro computer
tech:
  mcu: RP2040
  leds: null
  display: none
  connectivity:
  - usb
  battery: CR2032 (or USB-C power)
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of Hacker Hotel 2023
make_your_own:
  open_source: true
  hardware_url: https://github.com/AnesidoraCorporation/hh2023hardware
  firmware_url: https://github.com/AnesidoraCorporation/hh2023firmware
  eda_tool: null
  notes: Also see https://github.com/AnesidoraCorporation/hh2023documentation (docs) and https://github.com/AnesidoraCorporation/hh2023firmwareupdate (binary firmware updates).
links:
- label: hackaday.com/2023/03/10/hacker-hotel-2023-had-a-very-cool-badge
  url: https://hackaday.com/2023/03/10/hacker-hotel-2023-had-a-very-cool-badge/
  kind: article
  archived: https://web.archive.org/web/20251116064854/https://hackaday.com/2023/03/10/hacker-hotel-2023-had-a-very-cool-badge/
- label: raspberrypi.com/news/rp2040-smart-event-badges-for-hacker-hotel
  url: https://www.raspberrypi.com/news/rp2040-smart-event-badges-for-hacker-hotel/
  kind: article
- label: badge.team/docs/badges/hackerhotel-2023
  url: https://badge.team/docs/badges/hackerhotel-2023/
  kind: doc
  archived: https://web.archive.org/web/20251208045559/https://badge.team/docs/badges/hackerhotel-2023/
- label: github.com/AnesidoraCorporation
  url: https://github.com/AnesidoraCorporation
  kind: repo
images:
- file: assets/images/badges/other/hacker-hotel-2023-badge/09d2dff390.jpg
  source: https://hackaday.com/2023/03/10/hacker-hotel-2023-had-a-very-cool-badge/
  credit: Hacker Hotel 2023 badge team
  caption: Hacker Hotel 2023 badge, front
  archived: https://web.archive.org/web/20251116064854/https://hackaday.com/2023/03/10/hacker-hotel-2023-had-a-very-cool-badge/
- file: assets/images/badges/other/hacker-hotel-2023-badge/9e98a8ebfe.jpg
  source: https://hackaday.com/2023/03/10/hacker-hotel-2023-had-a-very-cool-badge/
  credit: Hacker Hotel 2023 badge team
  caption: Close-up of the back of the PCB showing stonework-style artwork
  archived: https://web.archive.org/web/20251116064854/https://hackaday.com/2023/03/10/hacker-hotel-2023-had-a-very-cool-badge/
contact: {}
notes:
- Made for Hackerhotel 2023 (Netherlands, February 2023). No matching event id exists in _data/events.yml (it has hackerhotel-2019, hackerhotel-2020, hackerhotel-2024 but not 2023), so event is left as "other" per research guide.
status: released
sources:
- kind: url
  url: https://hackaday.com/2023/03/10/hacker-hotel-2023-had-a-very-cool-badge/
  title: Hacker Hotel 2023 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''Hacker Hotel 2023''.'
  archived: https://web.archive.org/web/20251116064854/https://hackaday.com/2023/03/10/hacker-hotel-2023-had-a-very-cool-badge/
- kind: url
  url: https://www.raspberrypi.com/news/rp2040-smart-event-badges-for-hacker-hotel/
  title: RP2040 smart event badges for Hacker Hotel
  accessed: '2026-09-07'
  note: Confirms maker team (Pim, Sake, Nikolett), RP2040/CR2032, free distribution, and open-source GitHub org.
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2023/
  title: Hackerhotel 2023 badge documentation
  accessed: '2026-09-07'
  note: Gives the badge's name (Anesidora Mk1), USB-C or coin cell power, MicroPython/.uf2 firmware, and role breakdown.
  archived: https://web.archive.org/web/20251208045559/https://badge.team/docs/badges/hackerhotel-2023/
- kind: url
  url: https://github.com/AnesidoraCorporation
  title: AnesidoraCorporation GitHub org
  accessed: '2026-09-07'
  note: Lists the badge's hardware, firmware, firmware-update, and documentation repos used for make_your_own links.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Sources agree on maker team, RP2040/CR2032, MicroPython firmware, and free distribution to attendees. LED count/type, exact price (was free), and quantity made are not stated in any source found, so those fields are left empty. The badge is internally named "Anesidora Mk1" per badge.team; kept the sheet title as the entry title per guide.
last_modified_date: '2026-09-07'
---

The Hacker Hotel 2023 badge (internally "Anesidora Mk1") was built by a team of three — Pim (hardware and software lead), Sake (puzzle/challenge design), and artist Nikolett S. — for Hackerhotel 2023, a Dutch hacker camp held at a hotel venue in February 2023. It runs on an RP2040 and is powered by either a CR2032 coin cell or USB-C, with firmware written in MicroPython and distributed as .uf2 files that flash over the RP2040's stock USB bootloader.

Rather than a typical blinky badge, it was built as the key to a venue-wide puzzle hunt: a row of buttons and LEDs along the bottom two-thirds of the PCB stand in for the data and address lines of a small computer, and attendees enter codes gathered from around the hotel to progress through a challenge-response game of increasing difficulty. A companion lanyard, printed to resemble punched tape, carried a code that unlocked a bonus text-adventure game playable over USB serial.

Visually the badge departs from typical badgelife style: the top third holds the circuitry, while artwork worked directly into the copper and soldermask layers gives the board the look of an ancient stone tablet or gravestone, in a deep lapis-blue and gold palette designed by Nikolett. The project is fully open source, with hardware, firmware, firmware-update, and documentation repositories published under the AnesidoraCorporation GitHub organization; it was given free to Hacker Hotel 2023 attendees rather than sold.
