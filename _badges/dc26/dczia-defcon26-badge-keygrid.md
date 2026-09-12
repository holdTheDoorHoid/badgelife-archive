---
title: DCZia Defcon26-Badge (KeyGrid)
id: dc26-dczia-defcon26-badge-keygrid
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
series: DCZia
makers:
- name: DCZia
  url: https://github.com/dczia
summary: 'A DIY DEF CON 26 group badge from the DCZia (New Mexico) hacker crew: an ESP32 board with a 4x4 grid of mechanical keyswitches lit by RGB LEDs and a small OLED for menus and light-show output.'
functions: Interactive 4x4 mechanical keypad with an RGB LED under each key for light shows, a 128x32 OLED for menu settings and visual output, and BLE advertising (with a DEF CON manufacturer ID) so badges can talk to phones or each other. Supports Shitty Add-On (SAO) accessories.
look:
  colors:
  - green
  - black
  shape: rectangle
  themes:
  - hardware tool
  - retro computer
  - radio
tech:
  mcu: ESP32
  leds:
    count: 16
    type: reverse-mount
    note: One Neopixel-style RGB LED under each of the 16 mechanical keyswitches.
  display: 0.91" OLED (128x32, SSD1306)
  connectivity:
  - ble
  - wifi
  inputs:
  - buttons
  battery: 3x AA or USB power
  sao_version: v1
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Made by and distributed among DCZia crew/community members for DEF CON 26 (2018); not a public storefront item.
make_your_own:
  open_source: true
  hardware_url: https://github.com/dczia/Defcon26-Badge/tree/master/Hardware/KeyGridBadge
  firmware_url: https://github.com/dczia/Defcon26-Badge/tree/master/Software
  eda_tool: KiCad
  fab_url: null
  notes: Repo includes KiCad hardware (schematic, PCB, gerbers), an Arduino/ESP32 firmware sketch, keycap files, and design source for the card art. A September 2021 update added a prebuilt firmware binary that fixed a boot-loop bug.
links:
- label: github.com/dczia/Defcon26-Badge
  url: https://github.com/dczia/Defcon26-Badge
  kind: repo
  archived: https://web.archive.org/web/20260512135511/https://github.com/dczia/Defcon26-Badge
images:
- file: assets/images/badges/dc26/dczia-defcon26-badge-keygrid/e65d740f32.jpg
  source: https://github.com/dczia/Defcon26-Badge
  credit: DCZia
  caption: KeyGrid badge PCB render, front, green soldermask
  archived: https://web.archive.org/web/20260512135511/https://github.com/dczia/Defcon26-Badge
- file: assets/images/badges/dc26/dczia-defcon26-badge-keygrid/f048fcce2a.jpg
  source: https://github.com/dczia/Defcon26-Badge
  credit: DCZia
  caption: KeyGrid badge PCB render, back, green soldermask
  archived: https://web.archive.org/web/20260512135511/https://github.com/dczia/Defcon26-Badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/dczia/Defcon26-Badge
  title: DCZia Defcon26-Badge (KeyGrid)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 26''.'
  archived: https://web.archive.org/web/20260512135511/https://github.com/dczia/Defcon26-Badge
- kind: url
  url: https://github.com/dczia/Defcon26-Badge
  title: dczia/Defcon26-Badge README
  accessed: '2026-09-07'
  note: Confirmed maker (DCZia), event/year (DEF CON 26, 2018), badge name ("KeyGrid" from Hardware/KeyGridBadge folder), ESP32 MCU, SSD1306 OLED, 16 Neopixel-mini LEDs under a 4x4 Gatreon Blue keyswitch grid, BLE/Wi-Fi, 3xAA or USB power, SAO support, and open KiCad hardware + firmware.
  archived: https://web.archive.org/web/20260512135511/https://github.com/dczia/Defcon26-Badge
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No price, quantity made, or public distribution channel found; this looks like a crew-built badge circulated within the DCZia group/community rather than sold, so get_one fields are mostly left empty. No independent (non-GitHub) coverage found before the web-search budget for this task ran out; only the maker's own repo was used, which is the highest-quality source anyway. DCZia is a recurring DEF CON group (see also their DC30, DC31, DC32, DC33 badges already in the archive) but this repo does not name individual team members, only the "DCZia" identity.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/dczia-defcon26-badge-keygrid.glb
  method: kicad
  source_file: Hardware/KeyGridBadge/KeyGridBadge.kicad_pcb
  generated: '2026-09-07'
  bytes: 536836
---

The KeyGrid badge is a DIY group badge built by DCZia, a New Mexico-based DEF CON crew, for DEF CON 26 in 2018. It follows on from an earlier DCZia badge that used mechanical keyswitches, continuing that retro feel with a 4x4 grid of "Gatreon Blue" mechanical keyswitches under clear keycaps, each backlit by its own RGB LED. An ESP32 microcontroller drives the light shows, reads the keypad, and talks Bluetooth Low Energy (and potentially Wi-Fi), while a small 0.91" 128x32 OLED at the top of the board shows menu settings and other status output. Power comes from 3x AA batteries or USB, and the board carries a Shitty Add-On (SAO) header so it can host other badges' add-ons.

Development ran through the first half of 2018: an initial "Proto Dos" revision was tested, keycaps and switches were sourced, and BLE advertising was added ahead of DEF CON 26 using a DC26-specific manufacturer ID. The final "KeyGridBadge" hardware revision and matching Arduino/ESP32 firmware were finished in time for the con. Unlike a commercial badge, it does not appear to have been sold; it was built by and for the DCZia group's own members and community, and the repository's own history is the primary account of who touched it and when.

## Make your own

The GitHub repository (github.com/dczia/Defcon26-Badge) publishes everything needed to build one: the KiCad schematic, PCB layout and gerbers for the KeyGridBadge under `Hardware/KeyGridBadge`, keycap design files under `Hardware/Keycaps`, and the firmware sketch under `Software`. Follow the Espressif ESP32 Arduino core setup instructions linked in the README, flash the sketch (a prebuilt binary with a boot-loop fix was added in September 2021), and use Nordic's nRF Connect app to inspect its BLE advertisement.
