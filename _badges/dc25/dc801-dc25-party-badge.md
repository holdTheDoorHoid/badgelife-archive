---
title: DC801 DC25 Party Badge
id: dc25-dc801-dc25-party-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: DC801
  url: https://github.com/dc801
summary: 'A wearable BLE-connected party badge shaped like a helmeted face, built by the DC801 (Salt Lake City DEF CON group) for DEF CON 25.'
functions: 'Bluetooth Low Energy communication between badges; RGB "eyes"; helmet and helmet-wing LED arrays; onboard speaker; four buttons plus two hidden capacitive touch buttons; SPI LCD screen; breakout pins and JTAG for hacking.'
look:
  colors: []
  shape: null
  themes:
  - robot
tech:
  mcu: nRF52832
  leds:
    count: 15
    type: RGB
    note: '2 RGB LEDs for eyes, 7 yellow LEDs on the helmet, 6 red LEDs on the helmet wings'
  display: SPI LCD screen
  connectivity:
  - ble
  battery: LiPo (charged via MCP73831 over micro USB)
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
  hardware_url: https://github.com/dc801/DC25PartyBadge/tree/master/Hardware
  firmware_url: https://github.com/dc801/DC25PartyBadge/tree/master/Software
  eda_tool: Eagle
  license: MIT
  notes: 'Firmware built with Eclipse + GNU ARM GCC, flashed with a J-Link Segger JTAG programmer, uses the Nordic s132 softdevice.'
links:
- label: github.com/dc801/DC25PartyBadge
  url: https://github.com/dc801/DC25PartyBadge
  kind: repo
  archived: https://web.archive.org/web/20260907113014/https://github.com/dc801/DC25PartyBadge
images:
- file: assets/images/badges/dc25/dc801-dc25-party-badge/70193f8c54.jpg
  source: "https://github.com/dc801/DC25PartyBadge"
  credit: "Cat Murdock"
  caption: "DC801 DC25 party badge, worn"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/dc801/DC25PartyBadge
  title: DC801 DC25 Party Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 25''.'
  archived: https://web.archive.org/web/20260907113014/https://github.com/dc801/DC25PartyBadge
- kind: url
  url: https://raw.githubusercontent.com/DC801/DC25PartyBadge/master/Readme.md
  title: 'DC801_DC25PartyBadge Readme'
  accessed: '2026-09-07'
  note: 'Full readme text: hardware (Rigado BMD-300/nRF52832), LED counts, I/O list, software toolchain, Eagle design files, license, photo credit, maker Twitter handles.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Maker's own repo confirms hardware and firmware details. Price, quantity made, and distribution method were not stated anywhere in the repo; no storefront, Hackaday page, or press coverage was found in the searches available this session (web search budget was exhausted, so coverage relied on the repo itself and one archived GitHub page). Shape/look themes are inferred loosely from the 'helmet' and 'eyes' language in the readme and the photo (a stylized robot/helmeted face) rather than stated outright, so look.shape is left null pending a clearer look at the board outline."
last_modified_date: '2026-09-07'
---

The DC801 DC25 Party Badge is a Bluetooth Low Energy wearable built by DC801, the Salt Lake City DEF CON group, for DEF CON 25 in 2017. It centers on a Rigado BMD-300 module (a Nordic nRF52832, 16 MHz Cortex-M4F with 512 kB flash and 64 kB RAM) and packs a helmet-and-eyes LED layout: two RGB "eyes," seven yellow LEDs across the "helmet," and six red LEDs on the "helmet wings." It also carries a small SPI LCD, a speaker, four buttons, two hidden capacitive touch buttons, breakout pins, and a JTAG header for tinkering, all powered from a LiPo cell charged over micro USB through an MCP73831 charger.

The hardware (Eagle CAD schematics and board files) and firmware (built with Eclipse and the GNU ARM GCC toolchain against Nordic's s132 softdevice, flashed via a J-Link Segger JTAG programmer) are both published on GitHub under the MIT license, making this a fully open-source badge. The project photo, credited to Cat Murdock, shows the badge as worn. Beyond the repo itself, no pricing, production quantity, or distribution details were found; the maker's readme points to Twitter handles @rushan_ee and @hamster for updates but gives no storefront or announcement post.
