---
title: NorthSec 2016 Badge
id: northsec-2016-northsec-2016-badge
layout: badge
parent: NorthSec 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2016
year: 2016
makers:
- name: NorthSec
summary: 'The official electronic badge for NorthSec 2016, a dual-microcontroller board with an OLED display, Bluetooth Low Energy, and capacitive touch buttons.'
functions: 'Displays custom graphics/animations on its OLED screen and communicates over Bluetooth Low Energy; programmable via SWD or USB DFU. Specific on-badge games or CTF tie-ins are not documented in the available sources.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: nRF51822 + STM32F072CB
  leds:
    count: 2
    type: discrete
    note: one red and one green indicator LED, driven by the nRF51822
  display: OLED
  connectivity:
  - ble
  - usb
  inputs:
  - touch
  - buttons
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
  open_source: yes
  hardware_url: https://github.com/nsec/nsec-badge/tree/nsec16
  firmware_url: https://github.com/nsec/nsec-badge/tree/nsec16
  eda_tool: null
links:
- label: github.com/nsec/nsec-badge/tree/nsec16
  url: https://github.com/nsec/nsec-badge/tree/nsec16
  kind: repo
images: []
contact: {}
notes:
- Official NorthSec 2016 badge (first year every conference and competition attendee received one); source on the nsec16 branch of nsec/nsec-badge. Found by the event-year sweep, task northsec.
status: released
sources:
- kind: url
  url: https://github.com/nsec/nsec-badge/tree/nsec16
  title: NorthSec 2016 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:northsec); event read as ''northsec-2016''.'
- kind: url
  url: https://raw.githubusercontent.com/nsec/nsec-badge/nsec16/README.md
  title: 'nsec/nsec-badge README (nsec16 branch)'
  accessed: '2026-09-08'
  note: 'Confirms dual-MCU design (nRF51822 + STM32F072CB), OLED display, red/green LEDs, touch buttons, USB, and SWD/USB-DFU programming; open-source hardware and firmware.'
- kind: url
  url: https://badge.gallery/series/northsec
  title: 'NorthSec · Hacker Con Badges'
  accessed: '2026-09-08'
  note: 'Third-party badge-tracking site corroborating the same feature set for the 2016 badge; no pricing, quantity, or photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'The nsec/nsec-badge repo (nsec16 branch) confirms this is a real, dual-MCU (nRF51822 + STM32F072CB) badge with an OLED display, BLE, red/green LEDs, and touch buttons, and that hardware and firmware are open source. No maker page, storefront, or press coverage gave price, quantity made, or availability, so those remain unknown. No photo of the assembled badge was found -- the repo only contains small OLED icon bitmaps (cat faces, icons), not photos of the item, so no images were saved. The claim in the sweep-era notes that "every conference and competition attendee received one" could not be independently confirmed from the sources checked, so get_one.availability/distribution were left unset rather than guessed; status was raised to "released" since the repo and third-party badge tracker both confirm this badge was actually built and used, beyond just being listed on a sheet.'
last_modified_date: '2026-09-08'
---

The NorthSec 2016 badge was the electronic badge issued for NorthSec, the Montreal-based hacking conference and competition. It is a dual-microcontroller design: a Nordic nRF51822 (ARM Cortex-M0, with Bluetooth Low Energy) drives the badge's OLED display, battery management, and red/green indicator LEDs, while an STMicroelectronics STM32F072CB (also Cortex-M0) handles the capacitive touch buttons and USB port. Both chips can be reprogrammed over Serial Wire Debug with a Tag-Connect cable and a compatible probe (the team used a Black Magic Probe), and the STM32 side also supports field updates over USB DFU by holding down its program button while resetting.

NorthSec published the badge's hardware and firmware as open source on the `nsec16` branch of the `nsec/nsec-badge` GitHub repository, including build instructions and a Makefile-based toolchain for compiling the ARMv6-M firmware. The repository's image assets are small OLED icon bitmaps used by the badge's UI (cat faces, a battery icon, an NSec logo, and similar), rather than photographs of the finished board, so no image of the physical badge could be sourced for this entry.

Pricing, production quantity, and how the badge was distributed to attendees are not documented in the sources checked here; a separate community note associated with this entry states that every conference and competition attendee received one, but that specific claim was not independently verified against a primary NorthSec source during this research pass.

## Make your own

Hardware schematics and firmware source for both microcontrollers are in the `nsec/nsec-badge` repository on the `nsec16` branch. Building the firmware requires an `arm-none-eabi` GCC toolchain targeting `armv6-m` with the nano variant of newlib; each microcontroller has its own Makefile. The nRF51822 side also needs Nordic's SDK v6.1 with the S110 SoftDevice v7.0 for BLE. Flashing can be done over SWD (Tag-Connect TC2030-CTX-NL cable plus a Black Magic Probe or similar) for both chips, or over USB DFU for the STM32 side by holding its program button while pressing reset.
