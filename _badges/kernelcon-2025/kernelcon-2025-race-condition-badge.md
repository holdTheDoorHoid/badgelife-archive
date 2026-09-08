---
title: Kernelcon 2025 Race Condition Badge
id: kernelcon-2025-kernelcon-2025-race-condition-badge
layout: badge
parent: Kernelcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: kernelcon-2025
year: 2025
makers:
- name: ZonkSec
  url: https://github.com/ZonkSec
summary: A Raspberry Pi Pico-powered racing badge for Kernelcon 2025 with a "buzz wire" style physical track game, reaction tests, and CTF-unlockable LED patterns.
functions: 'Track-racing game with easy/normal/hard modes and an off-track tolerance parameter, a reaction-speed test, a synthesizer/sound mode, LED-pattern unlocks tied to earned CTF flags and achievements, high-score tracking, and a solder-your-own bonus track add-on for the hardware village.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - ctf
tech:
  mcu: RP2040
  leds:
    count: 7
    type: RGB
    note: Seven addressable RGB LEDs alongside a TM1637-driven seven-segment display.
  display: 7-segment (TM1637)
  connectivity: []
  battery: 3x AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed to Kernelcon 2025 attendees (Hilton Omaha Downtown Old Market, Omaha, NE, April 3-4, 2025); assembled by Cyber City Circuits in Augusta, GA.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/ZonkSec/kernelcon-2025-badge
  eda_tool: null
links:
- label: badge.gallery/badges/kernelcon-2025-race-condition-badge
  url: https://badge.gallery/badges/kernelcon-2025-race-condition-badge
  kind: website
- label: 2025.badge.kernelcon.org
  url: https://2025.badge.kernelcon.org/
  kind: website
- label: github.com/ZonkSec/kernelcon-2025-badge
  url: https://github.com/ZonkSec/kernelcon-2025-badge
  kind: repo
images:
- file: assets/images/badges/kernelcon-2025/kernelcon-2025-race-condition-badge/b5e9648316.png
  source: "https://2025.badge.kernelcon.org/"
  credit: "ZonkSec / Kernelcon"
  caption: "The Race Condition Badge, Kernelcon 2025's RP2040-based racing-game badge"
contact: {}
notes:
- Raspberry Pi Pico-based racing-game conference badge for Kernelcon 2025. Found by the event-year sweep, task con-kernelcon.
- The sweep listed the maker as "Kernelcon"; the badge site and GitHub repo credit ZonkSec (Tyler Rosonke) as designer, with collaborators elaboratreues and popcorndan, and Cyber City Circuits handling assembly. ZonkSec has made the Kernelcon badge for multiple years (2019-2026).
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/kernelcon-2025-race-condition-badge
  title: Kernelcon 2025 Race Condition Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kernelcon); event read as ''Kernelcon 2025''.'
- kind: url
  url: https://2025.badge.kernelcon.org/
  title: Kernelcon 2025 Badge - Race Condition
  accessed: '2026-09-08'
  note: 'Official badge microsite: game mechanic ("buzz wire" style track racing, leaderboard), badge photo, note that source was released April 4, 2025.'
- kind: url
  url: https://github.com/ZonkSec/kernelcon-2025-badge
  title: 'GitHub - ZonkSec/kernelcon-2025-badge'
  accessed: '2026-09-08'
  note: 'Firmware/3D-print/kiosk source repo; confirms ZonkSec as maker. No README with full specs found; no separate hardware/KiCad folder seen, so open_source marked partial.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Price and quantity made are not published anywhere found; left empty. No standalone hardware/Gerber files were located in the repo (only firmware, 3D prints, and a kiosk app), so make_your_own.open_source is "partial" rather than "yes". The original online leaderboard has since been decommissioned per the badge site.'
last_modified_date: '2026-09-08'
---

The Race Condition Badge was Kernelcon 2025's conference badge, built around a Raspberry Pi Pico (RP2040) with a TM1637 seven-segment display and seven addressable RGB LEDs, running on three AAA batteries. Designed by Tyler Rosonke (ZonkSec) with collaborators elaboratreues and popcorndan, and assembled by Cyber City Circuits in Augusta, Georgia, it turned the badge into a physical "buzz-wire" style racing game: wearers raced a track with an off-track tolerance parameter across easy, normal, and hard modes, competed on a live leaderboard, and could unlock bonus LED patterns by completing reaction tests or earning CTF flags at the con (Hilton Omaha Downtown Old Market, April 3-4, 2025).

A hardware-village extra let attendees solder together and plug in an additional bonus racing track using headers, jumper wires, and a detection pad, extending the game beyond the stock board. ZonkSec released the firmware, 3D-print files, and the kiosk/leaderboard software to GitHub on April 4, 2025; the original online leaderboard has since been retired in favor of a raw data export. No separate hardware (KiCad/Gerber) repository or published price/quantity figures were found.

## Make your own

Firmware, 3D-print files, and the leaderboard kiosk app are published at https://github.com/ZonkSec/kernelcon-2025-badge. No hardware design files (schematic/PCB/BOM) were located alongside them.
