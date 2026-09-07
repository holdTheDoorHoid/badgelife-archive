---
title: Solana Badge
id: dc34-solana-defcon-badge-26
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: spacemandev-git
  url: https://github.com/spacemandev-git
summary: An open-source ESP32-S3 badge built for DEF CON 34 with a 2.8" LCD, six buttons, a secure element, and a Lua-based OS that lets attendees push small apps to the badge over Wi-Fi or Bluetooth.
functions: Runs "Solana OS," a Lua 5.4 runtime with an SDK for the display, buttons, RGB LEDs, microphones, and secure element. Apps are written in Lua and pushed to a badge by its ID over Wi-Fi or BLE through a small broker service and a companion web app that also flashes firmware over Web Serial. A separate factory test-kit firmware exercises every peripheral for bring-up. The badge can join the DEF CON conference Wi-Fi network (WPA2-Enterprise) with certificate validation.
look:
  colors:
  - green
  shape: rectangle
  themes:
  - crypto
  - logo
  form_factor: pcb badge
tech:
  mcu: ESP32-S3-WROOM-1-N16R8
  leds:
    count: 2
    type: WS2812B-compatible
    note: Two addressable RGB LEDs (D3/D4) run a brand-color gradient on boot.
  display: 2.8" SPI LCD (ILI9341, 320x240)
  connectivity:
  - wifi
  - ble
  - usb
  - i2c
  battery: LiPo with USB-C charging (MCP73831 charger, DW03D protection)
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
  hardware_url: https://github.com/spacemandev-git/solana-defcon-badge-26/tree/main/pcb
  firmware_url: https://github.com/spacemandev-git/solana-defcon-badge-26/tree/main/firmware
  eda_tool: KiCad
links:
- label: github.com/spacemandev-git/solana-defcon-badge-26
  url: https://github.com/spacemandev-git/solana-defcon-badge-26
  kind: repo
images:
  - file: assets/images/badges/dc34/solana-defcon-badge-26/2a580407cc.jpg
    source: "https://github.com/spacemandev-git/solana-defcon-badge-26"
    credit: "spacemandev-git"
    caption: "Front of the v1 Solana Badge PCB, showing the 2.8\" LCD, buttons, and RGB LEDs"
  - file: assets/images/badges/dc34/solana-defcon-badge-26/91350579ac.jpg
    source: "https://github.com/spacemandev-git/solana-defcon-badge-26"
    credit: "spacemandev-git"
    caption: "Back of the v1 Solana Badge PCB"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/spacemandev-git/solana-defcon-badge-26
  title: solana-defcon-badge-26
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 2026''.'
- kind: url
  url: https://raw.githubusercontent.com/spacemandev-git/solana-defcon-badge-26/main/README.md
  title: 'README: Solana Badge'
  accessed: '2026-09-07'
  note: 'Full spec of the board (ESP32-S3-WROOM-1-N16R8, 2.8" ILI9341 LCD, six buttons via TCA9534, two mics, SE050 secure element, two WS2812B-compatible RGB LEDs, USB-C/LiPo), repo layout, Lua "Solana OS" app system, and the WPA2-Enterprise DEF CON Wi-Fi join flow referencing a "defcon34-wifi.crt" certificate, which places the badge at DEF CON 34.'
- kind: url
  url: https://api.github.com/repos/spacemandev-git/solana-defcon-badge-26
  title: GitHub repo metadata
  accessed: '2026-09-07'
  note: 'Repo description reads "2026 Solana Defcon Badge," confirming the year/event as DEF CON 34 (2026).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Event corrected from "other" to dc34 (DEF CON 34, 2026): the repo description says "2026 Solana Defcon Badge" and the firmware README references joining conference Wi-Fi with a "defcon34-wifi.crt" certificate. Hardware/firmware/production files (Gerbers, BOM, pick-and-place) are all published, and the pinout doc says its pin map "match[es] the fabricated hardware," so real boards exist, but no source states price, quantity made, or how/whether it was distributed to attendees versus built by a small team for personal use — those fields are left empty. No maker photos of an assembled/soldered board were found; the two images saved are renders of the bare PCB layout generated from the KiCad files.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/solana-defcon-badge-26/
---

The Solana Badge is an open-source, ESP32-S3-based conference badge built by developer spacemandev-git for DEF CON 34 (2026). It carries a 2.8" ILI9341 LCD, six push buttons behind an I2C expander, stereo PDM microphones, an NXP SE050 secure element, two addressable RGB LEDs, and USB-C charging for a LiPo battery, all on a two-layer KiCad board roughly 78 x 116 mm.

Rather than shipping fixed firmware, the badge runs "Solana OS," a Lua 5.4 runtime with an SDK that reaches every peripheral. Small Lua apps can be written and pushed to a specific badge, identified by an ID derived from its own Ed25519 keypair, over Wi-Fi or Bluetooth through a companion web app and a broker service that relays GitHub-hosted scripts between senders and badges that can't otherwise reach each other. A separate factory test-kit firmware exercises and reports on every peripheral for bring-up, and the badge is built to join the DEF CON conference Wi-Fi network over WPA2-Enterprise with full certificate validation.

The repository publishes complete KiCad schematics and board files, Gerbers, BOM, and pick-and-place data for the current ("v1") revision, plus both firmware images and the web tooling used to flash and manage badges, but does not state a price, production quantity, or how the badge reached attendees.

## Make your own

Hardware is a two-layer KiCad 9 project under `pcb/v1/`, with production Gerbers, a BOM, and pick-and-place files included for the fabricated revision. Firmware lives under `firmware/`: `testkit/` is the bring-up/factory-test sketch (a prebuilt merged flash image is included), and `solana-os/` is the Lua-based application firmware, buildable with `arduino-cli` for an ESP32-S3 with 16 MB flash / 8 MB PSRAM. Both can be flashed over USB with `esptool.py`, or from a browser via the project's `/flash` web page using Web Serial.
