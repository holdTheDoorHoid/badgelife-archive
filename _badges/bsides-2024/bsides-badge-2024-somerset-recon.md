---
title: bsides-badge-2024 (Somerset Recon)
id: bsides-2024-bsides-badge-2024-somerset-recon
layout: badge
parent: BSides 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-2024
year: 2024
makers:
- name: Somerset Recon
  url: https://github.com/Somerset-Recon
summary: 'A WarGames-themed conference badge made for BSides San Diego 2024, built around a wireless rock-paper-scissors attack/defend game over BLE.'
functions: 'Wireless rock-paper-scissors game played over BLE: badges alternate between attack mode (scanning for and connecting to defending badges) and defend mode, scoring points for successful attacks. Hidden CTF challenges are reachable over UART through the SAO connector, styled as WOPR terminal games (Global Thermonuclear War, Tic-Tac-Toe) referencing the movie WarGames. Later firmware adds a glitchy custom-name display shown at boot when the SCAN button is held.'
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - movie
  - radio
tech:
  mcu: ESP32-C3
  leds:
    count: 1
    type: null
    note: 'Single red LED indicates when the badge is in attack mode.'
  display: null
  connectivity:
  - ble
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '400'
  availability: free
  distribution:
  - free_drop
  where: 'Distributed to attendees at the BSides San Diego 2024 conference.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Somerset-Recon/bsides-badge-2024/tree/main/kiCad
  firmware_url: https://github.com/Somerset-Recon/bsides-badge-2024/tree/main/software
  eda_tool: KiCad
links:
- label: github.com/Somerset-Recon/bsides-badge-2024
  url: https://github.com/Somerset-Recon/bsides-badge-2024
  kind: repo
  archived: https://web.archive.org/web/20260907104727/https://github.com/Somerset-Recon/bsides-badge-2024
images:
  - file: assets/images/badges/bsides-2024/bsides-badge-2024-somerset-recon/f86208f12d.jpg
    source: "https://github.com/Somerset-Recon/bsides-badge-2024"
    credit: "Somerset Recon"
    caption: "Front of the BSides San Diego 2024 badge"
  - file: assets/images/badges/bsides-2024/bsides-badge-2024-somerset-recon/7c24076c42.jpg
    source: "https://github.com/Somerset-Recon/bsides-badge-2024"
    credit: "Somerset Recon"
    caption: "Back of the BSides San Diego 2024 badge"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Somerset-Recon/bsides-badge-2024
  title: bsides-badge-2024 (Somerset Recon)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides 2024''.'
  archived: https://web.archive.org/web/20260907104727/https://github.com/Somerset-Recon/bsides-badge-2024
- kind: url
  url: https://raw.githubusercontent.com/Somerset-Recon/bsides-badge-2024/main/README.md
  title: 'Somerset-Recon/bsides-badge-2024: README'
  accessed: '2026-09-07'
  note: 'Confirmed maker, event (BSides San Diego 2024), 400 units distributed, ESP32-C3, BLE rock-paper-scissors gameplay, WOPR/UART CTF challenges, red attack-mode LED, KiCad hardware + Arduino firmware open source, flashing instructions.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched the GitHub repo page and raw README and confirmed every populated field and every factual sentence in the body/Make-your-own section against them (event, maker, 400-unit free distribution, ESP32-C3, BLE rock-paper-scissors mechanic, red attack-mode LED, UART/SAO WOPR CTF with Global Thermonuclear War and Tic-Tac-Toe, open-source KiCad hardware + Arduino firmware, flashing steps, and the later-firmware glitch name display). Both saved images exist on disk and the repo page confirms it hosts front/back badge photos. No event id exists in events.yml for "BSides San Diego 2024" specifically (only the generic "bsides-2024"), so event was left as bsides-2024. Display hardware, exact LED part/type, SAO header version, battery, and price/cost remain unstated in any source found and are correctly left empty.'
last_modified_date: '2026-09-07'
---

Somerset Recon built this badge for BSides San Diego 2024, distributing 400 units to attendees. It runs on an ESP32-C3 and centers on a wireless rock-paper-scissors game played over Bluetooth Low Energy: a red LED marks a badge as being in "attack" mode, and pressing the scan button lets it search out and connect to nearby badges sitting in "defend" mode, scoring points for time spent connected to a target.

Layered on top of the game is a WarGames-themed CTF: hidden challenges are reachable over UART through the badge's SAO connector, presented as WOPR terminal games including a Global Thermonuclear War riff and Tic-Tac-Toe, each hiding a flag. A later firmware revision (not the version flashed onto the conference badges) adds a glitch-style custom name display shown at boot when the SCAN button is held.

## Make your own

Hardware (KiCad schematics and Gerbers) and firmware (Arduino sketches plus a required Ticker library) are both published in the GitHub repo under separate `kiCad` and `software` folders. To reflash a badge: install the Ticker library from the repo (not the Arduino Library Manager's version), open `latest.ino` in the Arduino IDE, install the "esp32" board package by Espressif, connect via a 6-pin legless TAG-Connect probe to the badge's TAG port, select the "ESP32C3 Dev Module" board, and upload.
