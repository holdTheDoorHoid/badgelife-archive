---
title: CDC Badge
id: 39c3-2025-39c3-critical-decentralization-cluster-cdc-badge
layout: badge
parent: 39C3
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: 39c3-2025
year: 2025
makers:
- name: RIAT
  url: https://riat.at
  role: hardware design (GitHub org riatlabs)
- name: dllud
  role: presenter
- name: Pavel Polach
  role: presenter
- name: bobotronic
  role: presenter
summary: An open-hardware ESP32-S3 badge/devboard built around a TROPIC01 secure element, made by RIAT for the Critical Decentralization Cluster (CDC) assembly at 39C3.
functions: 'Workshop/prototyping devboard usable as a wearable badge: nametag and vCard sharing, hardware-backed key vault (FIDO2, TOTP, SSH/GPG, passwords), a Monero hardware wallet, ESPHome smart-home node, Reticulum node, PIV smartcard over USB CCID, and other community firmware.'
look:
  colors: []
  shape: null
  themes:
  - security
  - privacy
  - hardware tool
tech:
  mcu: ESP32-S3
  leds: null
  display: e-paper with frontlight
  connectivity:
  - wifi
  - ble
  - uart
  - i2c
  battery: JST connector, single-cell LiPo (charged via BQ25895)
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed to the Critical Decentralisation Cluster assembly at 39C3 (Hamburg, Dec 27-30 2025); exact distribution method (given away, sold, workshop kit) not stated in sources found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/riatlabs/cdc-badge
  firmware_url: https://github.com/riatlabs/cdc-badge-nametag
  eda_tool: KiCad
links:
- label: github.com/riatlabs/cdc-badge
  url: https://github.com/riatlabs/cdc-badge
  kind: repo
- label: events.ccc.de talk listing - The CDC Badge
  url: https://events.ccc.de/congress/2025/hub/en/event/detail/the-cdc-badge-conference-badge-devboard-with-tropi
  kind: doc
  archived: https://web.archive.org/web/20260101124924/https://events.ccc.de/congress/2025/hub/en/event/detail/the-cdc-badge-conference-badge-devboard-with-tropi
- label: decentral.community/39C3
  url: https://decentral.community/39C3/
  kind: website
  archived: https://web.archive.org/web/20260705210337/https://decentral.community/39C3/
- label: cdc-badge-nametag firmware
  url: https://github.com/riatlabs/cdc-badge-nametag
  kind: repo
images: []
contact: {}
notes:
- Sweep found the item via GitHub only; title corrected from the sweep's wording "39C3 Critical Decentralization Cluster (CDC) Badge" to the maker's own name, "CDC Badge".
- No photo of the assembled badge was found within the search budget (GitHub only shows KiCad source and a generic social-preview card, not a product photo); printables.com and the CCC event page did not yield a fetchable image either.
- Price, quantity made, and exact distribution mechanism (sold vs. given away) were not stated on any source found.
status: released
sources:
- kind: url
  url: https://github.com/riatlabs/cdc-badge
  title: 39C3 Critical Decentralization Cluster (CDC) Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:ccc-adjacent); event read as ''39C3 2025''.'
- kind: url
  url: https://github.com/riatlabs/cdc-badge
  title: 'riatlabs/cdc-badge: CDC Badge'
  accessed: '2026-09-08'
  note: Confirmed maker (RIAT/riatlabs), ESP32-S3 + TROPIC01, e-paper display with frontlight, 12-button keypad, LiPo/JST power, CERN-OHL-P open hardware, KiCad.
- kind: url
  url: https://events.ccc.de/congress/2025/hub/en/event/detail/the-cdc-badge-conference-badge-devboard-with-tropi
  title: 'The CDC Badge: conference badge & devboard with TROPIC01 and ESP32-S3'
  accessed: '2026-09-08'
  note: 39C3 talk listing confirming presenters dllud, Pavel Polach, bobotronic, and that the badge is designed with KiCad and released as open hardware.
  archived: https://web.archive.org/web/20260101124924/https://events.ccc.de/congress/2025/hub/en/event/detail/the-cdc-badge-conference-badge-devboard-with-tropi
- kind: url
  url: https://decentral.community/39C3/
  title: 39C3 - decentral.community
  accessed: '2026-09-08'
  note: Confirms the CDC assembly ran at 39C3 in Hamburg, Germany, Dec 27-30 2025.
  archived: https://web.archive.org/web/20260705210337/https://decentral.community/39C3/
- kind: url
  url: https://github.com/riatlabs/cdc-badge-nametag
  title: 'riatlabs/cdc-badge-nametag: CDC Badge Firmware'
  accessed: '2026-09-08'
  note: Simple stock firmware for the badge (nametag with frontlight control), confirms badge has keyboard, e-paper display, and TROPIC01.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): re-fetched all 4 cited sources plus the repo README and docs/datasheets.md directly. All confirmed except tech.sao_version, which was wrong: the researcher recorded "v1" (4-pin) but docs/datasheets.md lists the SAO Port component as a "2x3 2.54mm female header" (6-pin), so corrected to "v2" per the guide''s vocabulary. Everything else in the entry (maker, chip, secure element, display, keypad/TCA9535, battery/BQ25895, three expansion ports, license, EDA tool, presenters, event dates, firmware ecosystem listed in Make-your-own) is directly supported by the maker''s repo/README/docs and the CCC event listing. Price, quantity produced, and exact distribution method remain unfound and are correctly left blank. No usable product photo was located.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/39c3-2025/39c3-critical-decentralization-cluster-cdc-badge.glb
  method: kicad
  source_file: cdc-badge/cdc-badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 1144536
---

The CDC Badge is an open-hardware ESP32-S3 devboard built by RIAT (github.com/riatlabs) for the Critical Decentralisation Cluster (CDC), an assembly that ran at the 39th Chaos Communication Congress (39C3) in Hamburg, December 27-30, 2025. It pairs the ESP32-S3 with a TROPIC01 secure element, an e-paper display with frontlight, a 12-button keypad (via a TCA9535 I/O expander), and a single-cell LiPo power system charged through a BQ25895. Three expansion ports — a full Raspberry Pi 40-pin GPIO header, an SAO port, and a Grove connector — let it take HATs, blinky add-ons, or sensor modules, and it was presented at 39C3 by dllud, Pavel Polach, and bobotronic as both a wearable badge and a general workshop/prototyping platform.

Rather than shipping one fixed firmware, the badge is meant as a base for community projects: a modular hardware-backed key vault (FIDO2, TOTP, SSH/GPG, password storage) built on the TROPIC01, a Monero hardware wallet, an ESPHome port for smart-home use, a Reticulum node, a USB CCID PIV smartcard implementation, and a minimal nametag/vCard-sharing firmware are all published against the same hardware. The full KiCad design (schematics, PCB layout, 3D-printable cases) is released under the CERN Open Hardware Licence v2 - Permissive.

Sources found do not state a price, production quantity, or exactly how badges reached attendees at the CDC assembly (sold, given away, or built in-workshop), so those fields are left blank rather than guessed.

## Make your own

The hardware lives in [riatlabs/cdc-badge](https://github.com/riatlabs/cdc-badge) as a KiCad project (`cdc-badge/`), with 3D-printable cases in `cases/` and a `Makefile` (using KiKit) to generate fabrication outputs. Firmware options include the full-featured [cdc-badge-os](https://github.com/krim404/cdc-badge-os) (PlatformIO/ESP-IDF), the simpler [cdc-badge-nametag](https://github.com/riatlabs/cdc-badge-nametag), and several third-party firmware projects listed in the main repo's README. The badge can be flashed over USB or via UART broken out on the Raspberry Pi header.
