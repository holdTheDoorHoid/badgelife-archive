---
title: BSides Dublin 2026 Harp Badge
id: bsides-dublin-2026-bsides-dublin-2026-harp-badge
layout: badge
parent: BSides Dublin 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-dublin-2026
year: 2026
makers:
- name: BSides Dublin organizers
summary: 'The official electronic conference badge for BSides Dublin 2026, built around an STM32L053R8Tx with capacitive touch, LEDs, a buzzer, and a hidden CTF.'
functions: 'Six capacitive touch strings play notes on a two-octave piezo buzzer, with 7 PWM-driven LEDs and a USB serial CLI (type `help`); 4 CTF flags are hidden in the badge.'
look:
  colors: []
  shape: null
  themes:
  - music
  - ctf
  - security
tech:
  mcu: STM32L053R8Tx
  leds:
    count: 7
    type: discrete
    note: 7x yellow LEDs, PWM-controlled
  display: none
  connectivity:
  - usb
  battery: CR2032 or USB (auto-detected)
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
  hardware_url: https://github.com/BSidesDublin/HardwareBadge2026/tree/main/production_files
  firmware_url: https://github.com/BSidesDublin/HardwareBadge2026/tree/main/firmware
  eda_tool: null
links:
- label: github.com/BSidesDublin/HardwareBadge2026
  url: https://github.com/BSidesDublin/HardwareBadge2026
  kind: repo
images: []
contact: {}
notes:
- Official electronic conference badge for BSides Dublin 2026 built around an STM32L053R8Tx with 6 capacitive touch strings, 7 PWM LEDs, a two-octave piezo buzzer, USB-C/CR2032 power, and 4 hidden CTF flags; firmware and hardware files are on GitHub. Found by the event-year sweep, task bsides-singapore.
status: listed
sources:
- kind: url
  url: https://github.com/BSidesDublin/HardwareBadge2026
  title: BSides Dublin 2026 Harp Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-singapore); event read as ''BSides Dublin 2026''.'
- kind: url
  url: https://raw.githubusercontent.com/BSidesDublin/HardwareBadge2026/main/README.md
  title: 'BSidesDublin/HardwareBadge2026 README'
  accessed: '2026-09-10'
  note: 'Confirmed hardware specs, firmware/hardware being open source, CTF flags, and repo layout.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Repo confirms the badge exists and its hardware/firmware are fully open source, but has no price, production quantity, availability, or photos of the assembled board, and no maker name beyond "BSides Dublin" organizers as a group. No storefront, Hackaday, or press coverage found. Left get_one fields and images empty rather than guess; shape/colors left empty since no photo was found.'
last_modified_date: '2026-09-10'
---

The Harp Badge is the official electronic conference badge for BSides Dublin 2026, designed and built by the conference's organizers. It centers on an STM32L053R8Tx (Cortex-M0+) microcontroller driving six capacitive touch strings that play notes on a two-octave piezo buzzer, evoking the badge's namesake instrument, alongside seven PWM-controlled yellow LEDs. The badge is powered by either a CR2032 coin cell or USB-C, with automatic source detection, and exposes a USB serial CLI for interacting with the device.

Beyond the musical interface, the badge hides four CTF flags for attendees to find, and ships with a crystal-less USB DFU bootloader that makes firmware recovery straightforward even after a bad flash. All firmware source (bootloader and application), hardware design files, gerbers, BOM, and manufacturing/pick-and-place data are published on GitHub, making the badge fully open source.

No pricing, production quantity, or availability information was published, and no photos of the assembled badge were found in the repository or elsewhere, so those fields are left empty pending further sources.

## Make your own

Hardware and firmware are both public in the [BSidesDublin/HardwareBadge2026](https://github.com/BSidesDublin/HardwareBadge2026) repository. Firmware is built with `arm-none-eabi-gcc` and `make` (`cd firmware && make` for the unified bootloader+application image); it can be flashed over USB DFU (`dfu-util -a 0 -D firmware/application/build/stm32l053-app.bin -R -w`) or via SWD with an ST-Link. Gerbers, BOM, and pick-and-place data for manufacturing the board live under `production_files/`.
