---
title: Onion SAO
id: dc30-onion-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: seeess
  url: https://github.com/seeess
  role: designer, distributed via the Tor Project vendor booth
summary: A 1.69bis SAO shaped around the Tor Project's onion logo, sold at Tor's
  DEF CON 30 vendor booth as a standalone remake of an earlier onion badge.
functions: 'Cycles through 11 LED blinking patterns with a single button (slow/fast
  cycle, cylon, strobe, random, binary counter, off). Holding or rapidly mashing
  the button starts one of two hidden games: a reaction-time challenge and a
  button-mashing meter. Winning either unlocks an extra blinking mode
  (even/odd pattern or heartbeat), and the last mode plus any unlocks are saved
  to EEPROM across power cycles.'
look:
  colors: []
  shape: null
  themes:
  - privacy
  - security
  - puzzle
tech:
  mcu: ATtiny402
  leds:
    count: 5
    type: discrete
    note: 11 built-in blinking modes plus 2 modes unlockable by winning the on-board games
  display: none
  connectivity: []
  battery: 2x CR123A (holder included) or powered from a host badge's SAO header
  sao_version: v1.69bis
get_one:
  price: $40.00
  price_usd: 40.0
  quantity: ''
  availability: sold_out
  availability_note: Sold at the DEF CON 30 Tor Project vendor booth in 2022; not
    listed anywhere as still available as of 2026-09-06.
  distribution:
  - purchase
  where: Tor Project vendor booth during DEF CON 30
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/seeess/Defcon-Tor-30
  eda_tool: null
  license: WTFPL
  notes: The GitHub repo publishes the ATtiny402 firmware (main.c) and a written
    bill of materials and pinout notes in the README, but no schematic or PCB
    layout files (no KiCad/Eagle/Gerber files in the repo).
links:
- label: github.com/seeess/Defcon-Tor-30
  url: https://github.com/seeess/Defcon-Tor-30
  kind: repo
- label: 'DEF CON 30 Tor SAO feature overview (YouTube)'
  url: https://youtu.be/Rasb8VQQdyw
  kind: video
images:
- file: assets/images/badges/dc30/onion-sao/8ad3052780.jpg
  source: "https://github.com/seeess/Defcon-Tor-30"
  credit: "seeess"
  caption: "Pile of assembled DEF CON 30 Tor SAOs"
contact: {}
notes:
- Remake of the DC27 SAO
- 'The community sheet listed the maker as "Tor Project"; the repo README credits
  an individual designer (GitHub user seeess) who made the board "to help Tor
  out" and it was sold through Tor''s vendor booth, not designed by Tor Project
  staff.'
status: released
sources:
- kind: sheet
  event: dc30
  row: 22
  updated: '2022-06-13'
- kind: url
  url: https://github.com/seeess/Defcon-Tor-30
  title: 'Defcon 30 Tor Badge/SAO Manual (README)'
  accessed: '2026-09-06'
  note: Primary source for maker, MCU, LEDs, games, EEPROM behavior, SAO header
    support, BOM, and license (WTFPL).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts confirmed from the maker's own repo/README. Could not find
    board colors/shape (no clear front-on product photo, only a group photo of
    a pile of assembled boards), exact quantity made, or a Tor Project blog post
    corroborating the booth price.
last_modified_date: '2026-09-06'
---

The Onion SAO is a DEF CON 30 remake of an earlier onion-themed add-on, built by a hacker known as seeess to help the Tor Project run its 2022 vendor booth merchandise. It plugs into a 1.69bis SAO header (or an older 2x2 header, using only the 3V3/GND pins) for power, or runs standalone from a pair of included CR123A batteries. An ATtiny402 drives five LEDs through eleven selectable blink patterns, cycled with a single button.

Beyond the light patterns, the board hides two small games behind the same button: a reaction-time test and a button-mashing meter. Beating either one unlocks an additional LED mode, and the board remembers the last mode used and any unlocks earned via onboard EEPROM. The kit that came with it included a lanyard, an electrical-outlet sticker, and a handcuff key cut to a security bitting, all sold at Tor's booth for $40.

The maker published the ATtiny402 firmware and a full bill of materials on GitHub under the WTFPL, along with a build/troubleshooting manual, though no schematic or PCB layout files are included in the repository.
