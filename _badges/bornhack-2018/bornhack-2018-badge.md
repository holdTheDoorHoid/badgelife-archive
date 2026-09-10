---
title: BornHack 2018 badge
id: bornhack-2018-bornhack-2018-badge
layout: badge
parent: BornHack 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2018
year: 2018
makers:
- name: BornHack
summary: 'The official electronic badge for BornHack 2018, built around a dual-MCU design: a SiLabs Happy Gecko for USB and general use, plus a Nordic nRF51822 for Bluetooth.'
functions: Runs custom firmware compiled by attendees; ships with default test firmware. A BOOT button puts the Happy Gecko into a USB mass-storage bootloader (FAT12) for reflashing without extra tools. The nRF51822 can be separately programmed for Bluetooth experiments.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: EFM32HG322F64G (SiLabs Happy Gecko, Cortex-M0+) + nRF51822 (Nordic, Cortex-M0, BLE)
  leds: null
  display: null
  connectivity:
  - usb
  - ble
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2018/tree/hardware
  firmware_url: https://github.com/bornhack/badge2018
  eda_tool: null
  notes: Hardware design files (including schematic.pdf) live on the "hardware" branch, separate from the firmware on "master". A family of add-on boards is documented on the "breakoutboards" branch, and a companion nRF51 programmer tool lives on the "nrf51prog" branch.
links:
- label: github.com/bornhack/badge2018
  url: https://github.com/bornhack/badge2018
  kind: repo
- label: BornHack 2018 badge schematic (PDF)
  url: https://github.com/bornhack/badge2018/raw/hardware/schematic.pdf
  kind: doc
  accessed: '2026-09-08'
  archived: false
images: []
contact: {}
notes:
- The official electronic badge for BornHack 2018, built around a SiLabs EFM32HG322F64G (Happy Gecko) MCU with a Nordic nRF51822 BLE radio, open-hardware design published on GitHub. Found by the event-year sweep, task bornhack-2018.
- 'Research 2026-09-08: confirmed via the maker''s own GitHub repo and README. No production photos of the assembled badge were found (GitHub''s auto-generated repo preview card is not a photo of the item, so it was not saved). No price, quantity, or distribution details are published anywhere found; left those fields empty rather than guessing. EDA tool is not stated in the repo. Two related items already have their own catalog entries: the breakout/add-on boards (bornhack-2018-blinky-addon-bornhack-2018-badge-breakout-board) and the nRF51 programmer tool (bornhack-2018-nrf51-programmer-for-bornhack-2018-badge).'
status: listed
sources:
- kind: url
  url: https://github.com/bornhack/badge2018
  title: BornHack 2018 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bornhack-2018); event read as ''bornhack-2018''.'
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2018/master/README.md
  title: bornhack/badge2018 README
  accessed: '2026-09-08'
  note: Confirmed dual-MCU hardware (Happy Gecko + nRF51822), bootloader behavior, branch layout for hardware/firmware/breakout boards, and schematic PDF location.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Core hardware facts (chips, connectivity, bootloader, open hardware) confirmed directly from the maker's own repo, so confidence would be high on those points, but pricing, quantity made, distribution, colors, and any photo of the assembled badge were not found anywhere, so overall confidence is medium. No maker storefront, Hackaday post, or press coverage located.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bornhack-2018/bornhack-2018-badge.glb
  method: kicad
  source_file: bornhack_scale_it.kicad_pcb
  generated: '2026-09-10'
  bytes: 470456
---

The BornHack 2018 badge is the official electronic conference badge for BornHack 2018, an outdoor hacker camp in Denmark. It was designed and published by the BornHack team as open hardware, continuing a yearly tradition of custom badges for the event. Unlike the previous year's badge, the 2018 design uses two microcontrollers: a SiLabs EFM32HG322F64G "Happy Gecko" (Cortex-M0+ with built-in USB) handles general badge duties, while a Nordic nRF51822 (Cortex-M0 with Bluetooth Low Energy) provides wireless capability that attendees can program separately.

Reflashing the badge is meant to be approachable: holding the BOOT button puts the Happy Gecko into a bootloader that presents itself as a USB mass-storage device with a FAT12 filesystem, so a new firmware image can be copied on like a file rather than requiring special flashing tools. The badge shipped with a default test firmware, and the BornHack team also published a way to restore it. A separate nRF51 programmer tool (its own catalog entry) is used to flash the Bluetooth chip.

All hardware design files, including the schematic, are published on a dedicated "hardware" branch of the GitHub repository, separate from the firmware source on the main branch, and a family of compatible add-on/breakout boards is documented on a "breakoutboards" branch. No pricing, production quantity, or photographs of the assembled badge were found in any source located during this research pass.

## Make your own

Hardware design files (schematic as a PDF) are on the `hardware` branch of [github.com/bornhack/badge2018](https://github.com/bornhack/badge2018/tree/hardware). Firmware for the Happy Gecko is built from the `master` branch with a standard `arm-none-eabi` GCC toolchain (`make` produces `out/code.bin`); a separate tool on the `nrf51prog` branch programs the Nordic nRF51822 radio chip. Prebuilt binaries for both the default firmware and the nRF51 programmer are also linked from the repository's README for anyone who does not want to compile from source.
