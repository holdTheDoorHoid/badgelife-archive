---
title: Telegraph Badge (Hackerhotel 2024)
id: hackerhotel-2024-telegraph-badge-hackerhotel-2024
layout: badge
parent: Hackerhotel 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackerhotel-2024
year: 2024
makers:
- name: Badge.Team (Nikolett, Guru-san, Renze, Tom Clement, CH23, Norbert, Zac, SqyD, Martijn, Julian, Dimitri, Yvo)
  url: https://github.com/badgeteam
summary: The official Hackerhotel 2024 badge, built around a Victorian-telegraph theme with puzzles inspired by the Cooke and Wheatstone telegraph's unusual input method.
functions: An interactive badge with a telegraph-themed puzzle game; text is entered through a Cooke & Wheatstone-style multi-switch typing interface rather than a keyboard.
look:
  colors:
  - black
  - red
  shape: rectangle
  themes:
  - retro computer
  - puzzle
  - hardware tool
tech:
  mcu: ESP32-C6
  leds:
    count: null
    type: null
    note: LED matrix used for the telegraph-style keyboard interface, plus one addressable status LED
  display: 296x128 e-paper (red/black)
  connectivity:
  - wifi
  - ble
  battery: LiPo, charged over USB-C
  sao_version: v1
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Distributed to attendees of Hackerhotel 2024; not otherwise sold that we found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/badgeteam/hackerhotel-2024-hardware
  firmware_url: https://github.com/badgeteam/hackerhotel-2024-firmware-esp32c6
  eda_tool: KiCad
  license: CERN-OHL-P
  notes: A second co-processor (CH32V003) has its own firmware repo at https://github.com/badgeteam/hackerhotel-2024-firmware-ch32v003. SAO design files are at https://github.com/badgeteam/hackerhotel-2024-sao. A 3D-printable case/lanyard adapter is on Printables.
links:
- label: badge.team/docs/badges/hackerhotel-2024
  url: https://badge.team/docs/badges/hackerhotel-2024/
  kind: website
- label: badge.team/docs/badges/hackerhotel-2024/badge1.jpg
  url: https://badge.team/docs/badges/hackerhotel-2024/badge1.jpg
  kind: website
- label: badge.team/docs/badges/hackerhotel-2024/badge2.jpg
  url: https://badge.team/docs/badges/hackerhotel-2024/badge2.jpg
  kind: website
- label: badge.team/docs/badges/hackerhotel-2024/screen1.jpg
  url: https://badge.team/docs/badges/hackerhotel-2024/screen1.jpg
  kind: website
- label: hackerhotel-2024-hardware (GitHub)
  url: https://github.com/badgeteam/hackerhotel-2024-hardware
  kind: repo
- label: hackerhotel-2024-firmware-esp32c6 (GitHub)
  url: https://github.com/badgeteam/hackerhotel-2024-firmware-esp32c6
  kind: repo
- label: hackerhotel-2024-firmware-ch32v003 (GitHub)
  url: https://github.com/badgeteam/hackerhotel-2024-firmware-ch32v003
  kind: repo
- label: hackerhotel-2024-sao (GitHub)
  url: https://github.com/badgeteam/hackerhotel-2024-sao
  kind: repo
- label: Hackerhotel 2024 badge cover and lanyard adapter (Printables)
  url: https://www.printables.com/model/744855-hackerhotel-2024-badge-cover-and-lanyard-adapter
  kind: fab
images:
- file: assets/images/badges/hackerhotel-2024/telegraph-badge-hackerhotel-2024/fda087b89f.jpg
  source: https://badge.team/docs/badges/hackerhotel-2024/
  credit: Badge.Team
  caption: Telegraph badge front, e-paper display and five three-way switches
- file: assets/images/badges/hackerhotel-2024/telegraph-badge-hackerhotel-2024/962284ae57.jpg
  source: https://badge.team/docs/badges/hackerhotel-2024/
  credit: Badge.Team
  caption: Close-up of the badge's e-paper screen
contact: {}
notes:
- Victorian telegraph theme, ESP32-C6, 296x128 red/black e-paper, five 3-way switches for Cooke & Wheatstone-style typing mode, SAO + QWIIC connectors.
status: released
sources:
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2024/
  title: Telegraph Badge (Hackerhotel 2024)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''Hackerhotel 2024''.'
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2024/
  title: Hackerhotel 2024 | Badge.Team
  accessed: '2026-09-07'
  note: 'Maker''s own handbook page: theme, MCU, display, switches, SAO/QWIIC connectors, USB-C charging, list of maker volunteers.'
- kind: url
  url: https://github.com/badgeteam/hackerhotel-2024-hardware
  title: badgeteam/hackerhotel-2024-hardware
  accessed: '2026-09-07'
  note: Confirmed hardware is open source (KiCad design files, gerbers, schematic PDF), under CERN-OHL-P license.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: LED count/type for the telegraph-keyboard matrix was not stated on the maker's page or in the hardware repo description; left empty. No price or production quantity found (badge was distributed to Hackerhotel 2024 attendees, not sold separately as far as we could find), so get_one.price/quantity/availability are left unfilled/unknown.
last_modified_date: '2026-09-07'
model:
  file: assets/models/hackerhotel-2024/telegraph-badge-hackerhotel-2024.glb
  method: gerber
  source_file: hh2024.kicad_pcb
  generated: '2026-09-07'
  bytes: 345304
  size_mm:
  - 90.4
  - 114.0
---

The Telegraph badge was Badge.Team's official badge for Hackerhotel 2024, built by a volunteer crew (Nikolett, Guru-san, Renze, Tom Clement, CH23, Norbert, Zac, SqyD, Martijn, Julian, Dimitri, and Yvo) around a Victorian-telegraph theme. Rather than a keyboard, text is entered through five three-way switches in a Cooke & Wheatstone-inspired scheme, shown on a 296x128 red/black e-paper display. An ESP32-C6 (Wi-Fi 6, BLE, 802.15.4) runs the main firmware, with a CH32V003 as a co-processor; the badge also carries an SAO header, a QWIIC connector, and a LiPo battery charged over USB-C.

Hardware, both firmware projects, and the SAO reference design are published on GitHub under CERN-OHL-P, with the PCB designed in KiCad; a 3D-printable case and lanyard adapter is shared separately on Printables. No sale price, production run size, or post-event availability was found in the sources checked — the badge appears to have been distributed directly to Hackerhotel 2024 attendees rather than sold through a storefront.

## Make your own

Hardware (KiCad schematic/PCB, gerbers, schematic PDF) is at the `hackerhotel-2024-hardware` repo; ESP32-C6 firmware is in `hackerhotel-2024-firmware-esp32c6` and the CH32V003 co-processor firmware in `hackerhotel-2024-firmware-ch32v003`, both on the badgeteam GitHub org. SAO design files are in `hackerhotel-2024-sao`. All are licensed CERN-OHL-P. A 3D-printable cover/lanyard adapter model is available on Printables.
