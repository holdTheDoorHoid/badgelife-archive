---
title: Cyber Ægg
id: bornhack-2026-cyber-gg
layout: badge
parent: Bornhack 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2026
year: 2026
makers:
- name: badge.team
- name: Thomas Flummer
summary: A LoRa/MeshCore camp badge for BornHack 2026 built around an e-paper egg-shaped board, designed to keep being useful as a desktop clock and mesh radio after the event ends.
functions: 'On-site: a Tamagotchi-style virtual pet game (BornPets, with seven integrated mini-games), an event calendar with ICS import, and an NFC station game (feed/heal/inspire/sleep, authenticated with Ed25519). After the event: a MeshCore LoRa mesh network node (private messages, channels, contact discovery), a desktop clock with digital and analog watch faces, and a 32-slot alarm system, all controllable from a phone over BLE (Nordic UART Service) via the MeshCore app.'
look:
  colors:
  - black
  - red
  - white
  shape: egg
  themes:
  - cyberpunk
  - radio
  - security
  - puzzle
tech:
  mcu: nRF52840
  leds:
    count: 3
    type: RGB
    note: three addressable RGB LEDs on GPIO
  display: 1.54" e-paper, 152x152px, SSD1680Z8/SSD1675 controller
  connectivity:
  - ble
  - lora
  - nfc
  - i2c
  - usb
  battery: single-cell (capacity not published; firmware optimized for week-long low-power operation)
  sao_version: none
  inputs:
  - joystick
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: badge.team lists the badge as "delivered and sold out" (checked 2026-09-07)
  distribution:
  - purchase
  where: Sold through badge.team ahead of/at BornHack 2026; sold out by the time of this research pass.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/badgeteam/bornhack2026-hardware
  firmware_url: https://github.com/badgeteam/bornhack2026-firmware
  eda_tool: KiCad
  license: 'Hardware: MIT. Firmware: Apache 2.0 (+ an additional empty-file license per License.md)'
  notes: The hardware repo explicitly flags the design as BETA and warns not to order boards from it yet as of this check. Manufacturing notes target JLCPCB.
links:
- label: hackaday.com/2026/07/17/the-bornhack-2026-cyber-aegg-is-a-badge-with-a-life-afterwards
  url: https://hackaday.com/2026/07/17/the-bornhack-2026-cyber-aegg-is-a-badge-with-a-life-afterwards/
  kind: article
  archived: https://web.archive.org/web/20260831031636/https://hackaday.com/2026/07/17/the-bornhack-2026-cyber-aegg-is-a-badge-with-a-life-afterwards/
- label: badge.team
  url: https://badge.team/
  kind: website
  archived: https://web.archive.org/web/20260822195634/https://badge.team/
- label: badgeteam/bornhack2026-hardware
  url: https://github.com/badgeteam/bornhack2026-hardware
  kind: repo
- label: badgeteam/bornhack2026-firmware
  url: https://github.com/badgeteam/bornhack2026-firmware
  kind: repo
- label: badge.team/docs/badges/bornhack-2026
  url: https://badge.team/docs/badges/bornhack-2026/
  kind: website
  archived: https://web.archive.org/web/20260717235018/https://badge.team/docs/badges/bornhack-2026/
- label: bornhack2026-hardware (Codeberg)
  url: https://codeberg.org/Ranzbak/bornhack2026-hardware
  kind: repo
  archived: null
- label: bornhack-firmware-2026 (Codeberg)
  url: https://codeberg.org/Ranzbak/bornhack-firmware-2026
  kind: repo
  archived: https://web.archive.org/web/20260716120938/https://codeberg.org/Ranzbak/bornhack-firmware-2026
images:
- file: assets/images/badges/bornhack-2026/cyber-gg/24206e6f75.jpg
  source: https://hackaday.com/2026/07/17/the-bornhack-2026-cyber-aegg-is-a-badge-with-a-life-afterwards/
  credit: Hackaday
  caption: The BornHack 2026 Cyber Ægg badge
  archived: https://web.archive.org/web/20260831031636/https://hackaday.com/2026/07/17/the-bornhack-2026-cyber-aegg-is-a-badge-with-a-life-afterwards/
- file: assets/images/badges/bornhack-2026/cyber-gg/48934658b4.jpg
  source: https://badge.team/docs/badges/bornhack-2026/
  credit: Badge.Team
  caption: Cyber Ægg badge, front view
  archived: https://web.archive.org/web/20260717235018/https://badge.team/docs/badges/bornhack-2026/
- file: assets/images/badges/bornhack-2026/cyber-gg/b40f328897.jpg
  source: https://badge.team/docs/badges/bornhack-2026/
  credit: Badge.Team
  caption: Cyber Ægg badge, back view
  archived: https://web.archive.org/web/20260717235018/https://badge.team/docs/badges/bornhack-2026/
contact: {}
notes:
- nRF52840, LoRa, e-paper; doubles as desktop clock/Tamagotchi post-event
- Firmware uses an Embassy-based async framework on the nRF52840; LoRa radio is an SX1262 transceiver operating at 869.618 MHz (EU/UK narrow band) for MeshCore.
- Egg-shaped low-power badge, nRF52840, 1.54in tri-color e-paper, SX1262 LoRa mesh, BLE app, NFC tag, virtual pet 'BornPets' game.
status: released
sources:
- kind: url
  url: https://hackaday.com/2026/07/17/the-bornhack-2026-cyber-aegg-is-a-badge-with-a-life-afterwards/
  title: Cyber Ægg
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''BornHack 2026''.'
  archived: https://web.archive.org/web/20260831031636/https://hackaday.com/2026/07/17/the-bornhack-2026-cyber-aegg-is-a-badge-with-a-life-afterwards/
- kind: url
  url: https://badge.team/
  title: badge.team
  accessed: '2026-09-07'
  note: Confirms badge.team collaborated with Thomas Flummer on the Cyber Ægg for BornHack 2026; lists it as delivered and sold out; confirms designs are open source on GitHub.
  archived: https://web.archive.org/web/20260822195634/https://badge.team/
- kind: url
  url: https://github.com/badgeteam/bornhack2026-hardware
  title: badgeteam/bornhack2026-hardware
  accessed: '2026-09-07'
  note: 'Hardware README: nRF52840 MCU, 3x addressable RGB LEDs, 1.54" 152x152 e-paper (SSD1680Z8), SX1262 LoRa, NFC, QWIIC I2C, USB, MIT license; flagged as BETA design, do not order boards yet.'
- kind: url
  url: https://github.com/badgeteam/bornhack2026-firmware
  title: badgeteam/bornhack2026-firmware
  accessed: '2026-09-07'
  note: 'Firmware README: Embassy-based async firmware; BornPets Tamagotchi game with 7 minigames; MeshCore LoRa node at 869.618 MHz with BLE NUS phone app control; dual watch faces, 32-slot alarms, ICS calendar import; NFC station game with Ed25519 auth; Apache 2.0 + empty-file license.'
- kind: url
  url: https://badge.team/docs/badges/bornhack-2026/
  title: Cyber Ægg (Bornhack 2026 badge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''BornHack 2026''.'
  archived: https://web.archive.org/web/20260717235018/https://badge.team/docs/badges/bornhack-2026/
- kind: url
  url: https://codeberg.org/Ranzbak/bornhack2026-hardware
  title: bornhack2026-hardware (Codeberg)
  accessed: '2026-09-07'
  note: 'Hardware repo README: LoRa/BLE/NFC connectivity, joystick input, three discrete RGB LEDs, QWIIC I2C port; design marked BETA/prototype stage one.'
- kind: url
  url: https://codeberg.org/Ranzbak/bornhack-firmware-2026
  title: bornhack-firmware-2026 (Codeberg)
  accessed: '2026-09-07'
  note: Firmware repo (Rust/Embassy) confirming open-source firmware for the badge.
  archived: https://web.archive.org/web/20260716120938/https://codeberg.org/Ranzbak/bornhack-firmware-2026
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (maker, chip, connectivity, display, open-source status) confirmed directly from badge.team and the maker's own GitHub repos, which outrank the Hackaday press coverage per the research guide. Price and quantity produced were not stated anywhere found; left empty. Battery capacity not specified in the hardware README. No SAO header info found (this is a standalone badge, not confirmed to have SAO ports either way, so left null). Merged with duplicate entry 'Cyber Ægg (Bornhack 2026 badge)' (bornhack-2026-cyber-gg-bornhack-2026-badge).
last_modified_date: '2026-09-07'
model:
  file: assets/models/bornhack-2026/cyber-gg.glb
  method: kicad
  source_file: bornhack2026-hardware.kicad_pcb
  generated: '2026-09-07'
  bytes: 1468208
redirect_from:
- /badges/bornhack-2026/cyber-gg-bornhack-2026-badge/
---

The Cyber Ægg is badge.team's badge for BornHack 2026, made in collaboration with Thomas Flummer. Shaped like an egg with a flat bottom for desk placement, it runs on a Nordic nRF52840 with a 1.54" e-paper display, three RGB LEDs, an SX1262 LoRa radio, and NFC. During the week-long camp it plays host to a Tamagotchi-style virtual pet game (BornPets) with seven mini-games, an event calendar, and an NFC-based station game where players feed, heal, or inspire their pet using Ed25519-authenticated taps.

The badge is explicitly designed not to become e-waste once BornHack ends: its firmware repurposes the same hardware as a MeshCore LoRa mesh-network node, a desktop clock with digital and analog watch faces, and a 32-slot alarm clock, all manageable from a phone over Bluetooth using the official MeshCore app. Both the hardware (MIT licensed) and firmware (Apache 2.0) are open source on GitHub, though the hardware repository currently warns that the design is still beta and cautions against ordering boards from it as-is.

By the time of this research pass, badge.team's site listed the Cyber Ægg as delivered and sold out; no price or total production quantity was published in any source found.

## Make your own

Hardware and firmware are both public on GitHub (`badgeteam/bornhack2026-hardware`, MIT license; `badgeteam/bornhack2026-firmware`, Apache 2.0). The hardware repo includes production files intended for JLCPCB, but as of this check its authors flag the design as BETA and ask that people not order their own boards from it yet.

## Notes merged from the duplicate entry "Cyber Ægg (Bornhack 2026 badge)"

The Cyber Ægg is BornHack 2026's official badge, designed by Badge.Team with an egg-shaped shell that nods to 1990s Tamagotchi virtual pets. It runs on a Nordic nRF52840, driving a 1.54-inch tri-color (black/red/white) e-paper display and a 5-way joystick with select/execute/cancel buttons. Onboard radios include Bluetooth Low Energy, an NFC tag, and a Semtech SX1262 LoRa chip used for mesh networking over MeshCore, letting badges talk to each other and relay messages across the camp without infrastructure. A rechargeable battery, topped up over USB-C, is meant to last a full week-long BornHack event on one charge.

The signature software feature is BornPets, a virtual-pet game with mini-games built around the egg form factor, though the badge also supports alternative firmware including a Community Edition, a DOOM port, and CircuitPython. Both the hardware (KiCad) and firmware (Rust, built on the Embassy async framework) are published on Codeberg under Ranzbak's account, and the hardware repo describes the board as still in "prototype stage one" and marked BETA, with antenna performance not yet validated at the time these sources were checked.

## Make your own

Hardware design files (KiCad) are at the `bornhack2026-hardware` repo on Codeberg, and firmware source (Rust/Embassy) is at `bornhack-firmware-2026`, also on Codeberg. No separate BOM or Gerber-only share link was found; the KiCad project itself is the hardware source.
