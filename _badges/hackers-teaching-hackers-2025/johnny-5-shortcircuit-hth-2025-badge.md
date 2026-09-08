---
title: Johnny 5 (2025 HTH Badge)
id: hackers-teaching-hackers-2025-johnny-5-shortcircuit-hth-2025-badge
layout: badge
parent: 'HTH 2025: Short Circuit'
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackers-teaching-hackers-2025
year: 2025
makers:
- name: HTHackers
summary: 'The 2025 Hackers Teaching Hackers conference badge, an STM32-based "repair the robot" puzzle badge named for the film Short Circuit.'
functions: 'Serial-shell puzzle: repair three damaged modules (Comms, Power Core, Personality Matrix) via a "S.A.I.N.T. OS" command shell to unlock the badge, including a Morse-code visual clue and a secondary diagnostic UART data stream.'
look:
  colors:
  - black
  - gold
  shape: null
  themes:
  - robot
  - sci-fi
  - puzzle
  - ctf
  - learn to solder
tech:
  mcu: STM32L031G6U6
  leds: null
  display: none
  connectivity:
  - uart
  battery: CR2450
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Distributed as the conference badge to attendees of Hackers Teaching Hackers 2025.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HTHackers/J5-ShortCircuit
  eda_tool: null
links:
- label: github.com/HTHackers/J5-ShortCircuit
  url: https://github.com/HTHackers/J5-ShortCircuit
  kind: repo
images:
- file: assets/images/badges/hackers-teaching-hackers-2025/johnny-5-shortcircuit-hth-2025-badge/59b7c0c92b.jpg
  source: "https://github.com/HTHackers/J5-ShortCircuit"
  credit: "HTHackers"
  caption: "Johnny 5 badge PCB on its lanyard, showing the CR2450 battery holder and primary/diagnostic UART headers, HTH 2025"
contact: {}
notes:
- STM32L031-based 'repair the robot' badge for HTH 2025 with Morse-code and diagnostic-stream puzzles leading to a flag. Found by the event-year sweep, task con-blue-team-con.
- 'Sweep title was "Johnny 5 ShortCircuit (HTH 2025 Badge)"; the maker''s own README calls it simply "Johnny 5 - 2025 HTH Badge," so the title was shortened to match. "ShortCircuit"/"J5-ShortCircuit" is the GitHub repo name, referencing the 1986 film Short Circuit that the badge''s "I W4NT T0 L1V3" flag also nods to.'
status: released
sources:
- kind: url
  url: https://github.com/HTHackers/J5-ShortCircuit
  title: Johnny 5 ShortCircuit (HTH 2025 Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-blue-team-con); event read as ''Hackers Teaching Hackers 2025''.'
- kind: url
  url: https://github.com/HTHackers/J5-ShortCircuit
  title: 'HTHackers/J5-ShortCircuit README'
  accessed: '2026-09-08'
  note: 'Confirmed maker, event/year, MCU (STM32L031G6U6), CR2450 battery, dual-UART shell puzzle mechanics, and firmware repo/license; source of the badge photo.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Repo confirms hardware, firmware, and puzzle design in the maker''s own words, but no separate storefront, price, quantity, or LED/lighting spec was found, and hardware design files (schematic/PCB) were not located in the repo (only firmware source). Distribution assumed to be a standard given-out conference badge; not explicitly stated as free in the README.'
last_modified_date: '2026-09-08'
---

Johnny 5 is the 2025 Hackers Teaching Hackers (HTH) conference badge, built around an STM32L031G6U6 microcontroller and named after the robot from the 1986 film *Short Circuit* (the GitHub repo is titled "J5-ShortCircuit"). Rather than a purely decorative board, it ships in a "damaged" state and challenges holders to repair it through a text-based "S.A.I.N.T. OS" shell reached over a primary UART (LPUART1, 115200 baud). Fixing the badge means solving three linked puzzles: decoding Morse code flashed by an eye LED to repair the Comms Array, reading a hidden stabilization key out of a second diagnostic UART stream (USART2, 9600 baud) to fix the Power Core, and conversing with an onboard "Personality Matrix" to unlock a final capture-the-flag token.

The board is powered by a CR2450 coin cell (or 3V external supply) and exposes labeled solder pads for reset, SWD programming (swdio), and both UART interfaces, making it approachable for attendees to probe and reflash. The firmware source is published on GitHub under HTHackers/J5-ShortCircuit with a LICENSE file, though no separate hardware design files (schematic or PCB) were found in the repo, so the project is only partially open source as documented.

No separate storefront, price, or production-quantity information was located; the badge appears to have been distributed directly to HTH 2025 attendees as their conference badge.
