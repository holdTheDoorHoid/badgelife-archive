---
title: NorthSec 2017 Badge
id: northsec-2017-northsec-2017-badge
layout: badge
parent: NorthSec 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2017
year: 2017
makers:
- name: NorthSec
  url: https://github.com/nsec
summary: 'The official NorthSec 2017 conference/CTF badge: a dual-MCU PCB badge with an OLED display, touch buttons, and Bluetooth Low Energy, worn by attendees and used to run CTF challenges over USB.'
functions: 'Displays a customizable avatar and name on its OLED screen (set over BLE); the STM32 side exposes CTF challenges over USB during the competition; separate firmware builds existed for conference, admin, speaker, and CTF roles.'
look:
  colors: [blue]
  shape: badge
  themes: [security, ctf, hardware tool]
tech:
  mcu: nRF51822 + STM32F072CB
  leds:
    count: 2
    type: discrete
    note: red and green indicator LEDs, driven by the nRF51822
  display: OLED
  connectivity: [ble, usb]
  inputs:
  - touch buttons
  power: 2x AAA or USB
  battery: 2x AAA
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: [free_drop]
  where: Given to NorthSec 2017 conference and CTF attendees.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/nsec/nsec-badge/tree/2017
  firmware_url: https://github.com/nsec/nsec-badge/tree/2017
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: 'README links a schematic PDF and placeholder PCB/BOM links on the badge''s own website (xn--rr8b.ga), which is no longer reachable; firmware source for both MCUs is in the repo. Depends on the proprietary Nordic SDK v12.1.0 and s130 SoftDevice, which are non-free but freely redistributed.'
links:
- label: github.com/nsec/nsec-badge (2017 branch)
  url: https://github.com/nsec/nsec-badge/tree/2017
  kind: repo
images:
  - file: assets/images/badges/northsec-2017/northsec-2017-badge/3dc5c60f3e.jpg
    source: "https://github.com/nsec/nsec-badge/tree/2017"
    credit: "NorthSec Team Badge"
    caption: "NorthSec 2017 badge PCB art: a Soviet-style star-and-wheat crest around the OLED window, touch-button D-pad, and #nsec17 markings"
  - file: assets/images/badges/northsec-2017/northsec-2017-badge/5e3f044a4b.jpg
    source: "https://github.com/nsec/nsec-badge/tree/2017"
    credit: "NorthSec Team Badge"
    caption: "Two assembled badges connected by a programming/data cable, AAA battery holders visible on the back"
contact: {}
notes:
- Official NorthSec 2017 badge; source on the "2017" branch of nsec/nsec-badge. Found by the event-year sweep, task northsec.
- 'The sweep''s recorded link (.../tree/nsec17) 404s; the correct branch is named "2017", not "nsec17".'
status: released
sources:
- kind: url
  url: https://github.com/nsec/nsec-badge/tree/nsec17
  title: NorthSec 2017 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:northsec); event read as ''northsec-2017''. This exact URL 404s.'
- kind: url
  url: https://github.com/nsec/nsec-badge/tree/2017
  title: nsec/nsec-badge, 2017 branch
  accessed: '2026-09-08'
  note: 'Correct repo branch for the 2017 badge; README describes hardware (nRF51822 + STM32F072CB, OLED, BLE, touch buttons, red/green LEDs, 2xAAA/USB power) and build/programming instructions.'
- kind: url
  url: https://raw.githubusercontent.com/nsec/nsec-badge/2017/README.md
  title: nsec-badge README (2017 branch, raw)
  accessed: '2026-09-08'
  note: 'Confirmed hardware overview text and that PCB/BOM links in the README are empty placeholders; schematic PDF is hosted on the badge''s now-dead website.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Maker''s own repo (README) confirms hardware and purpose. Price, quantity made, and open availability status are not stated anywhere found; the badge''s own website (xn--rr8b.ga) is dead so the schematic PDF and any photos hosted there could not be checked. PCB/BOM links in the README were placeholders even when the badge was current, so hardware_url/firmware_url point at the repo generally rather than specific files. Two photos of the physical badge (front PCB art, and two units wired together) were pulled from website/images/ in the repo.'
last_modified_date: '2026-09-08'
---

The NorthSec 2017 badge is the official conference and CTF badge for NorthSec, Montreal's applied security conference, built by NorthSec's own "Team Badge." It uses two ARM Cortex-M0 microcontrollers on one board: a Nordic nRF51822 that drives the OLED display, the red/green status LEDs, battery management, and Bluetooth Low Energy, and an STMicroelectronics STM32F072CB that handles the touch buttons and USB port. Attendees could set a custom avatar and name over BLE, while the STM32 side exposed capture-the-flag challenges over USB during the competition; separate firmware images existed for regular attendees, admins, speakers, and CTF-specific roles.

The badge runs off two AAA batteries and/or USB power (1.8-5.5V DC), and each MCU can be reprogrammed over SWD via a 6-pin Tag-Connect pad, or the STM32 side via USB DFU. Firmware and hardware source for both chips live in the `nsec-badge` GitHub repository's `2017` branch; the nRF51 firmware depends on Nordic's (non-free but freely distributed) SDK v12.1.0 and s130 SoftDevice. The repository's README pointed to a schematic PDF and separate PCB/BOM pages hosted on the badge's own site, but that site (a punycode domain) is no longer reachable, and the PCB/BOM links in the README itself were empty placeholders even at the time.

No price, production quantity, or sale information was found; the badge appears to have been distributed to attendees as part of admission rather than sold. Two images of the physical hardware were recovered from the repository itself: the front PCB artwork (a star-and-wheat crest framing the OLED window and a five-button D-pad) and a photo of two assembled badges connected by a wire harness.

## Make your own

The `nsec-badge` repo (branch `2017`) has separate `nrf51/` and `stm32/` directories, each with its own `Makefile`. Building the nRF51 firmware requires an ARM `armv6-m` GCC toolchain plus Nordic's SDK v12.1.0 and s130 SoftDevice (fetched automatically via `make nordicsdk`); the STM32 side depends on the `libopencm3` library, included as a git submodule. Both chips can be flashed over SWD with a Black Magic Probe via a 6-pin Tag-Connect cable, or the STM32 via USB DFU.
