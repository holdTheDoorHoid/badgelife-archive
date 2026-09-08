---
title: nRF51 Programmer for BornHack 2018 badge
id: bornhack-2018-nrf51-programmer-for-bornhack-2018-badge
layout: badge
parent: BornHack 2018
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: bornhack-2018
year: 2018
makers:
- name: BornHack
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/bornhack/badge2018/tree/nrf51prog
  url: https://github.com/bornhack/badge2018/tree/nrf51prog
  kind: repo
images: []
contact: {}
notes:
- A companion programming tool/firmware branch used to flash the nRF51822 Bluetooth radio chip on the BornHack 2018 badge. Found by the event-year sweep, task bornhack-2018.
- 'The sweep''s title treats this as a standalone item; the maker''s own README (github.com/bornhack/badge2018, master branch) describes it only as a firmware utility for the existing "BornHack 2018 badge" entry, not a separate product.'
status: not_an_item
sources:
- kind: url
  url: https://github.com/bornhack/badge2018/tree/nrf51prog
  title: nRF51 Programmer for BornHack 2018 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bornhack-2018); event read as ''bornhack-2018''.'
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2018/master/README.md
  title: 'bornhack/badge2018 README (master branch)'
  accessed: '2026-09-08'
  note: 'Confirms nrf51prog is firmware that runs on the badge''s own Happy Gecko (EFM32HG322F64G) MCU and bit-bangs SWD to flash the badge''s onboard Nordic nRF51822 BLE chip; not a separate product or kit.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: >-
    This is a tool/spec item, not a distinct badge, SAO, or kit: the "nrf51prog" git branch of
    bornhack/badge2018 holds C source (main.c, swd.c, nRF51prog.c, ihex.c, a Makefile) for a
    software SWD programmer that runs on the BornHack 2018 badge's primary Happy Gecko
    (EFM32HG322F64G, Cortex-M0+) microcontroller and is used to flash the badge's secondary
    Nordic nRF51822 (Cortex-M0, BLE) chip. The badge itself already has its own entry,
    bornhack-2018-bornhack-2018-badge. No separate hardware, price, or distribution exists for
    this branch; it is documentation/firmware for the badge people already have. Set to
    not_an_item per the research guide's special-case rule for tool/spec pages.
last_modified_date: '2026-09-08'
---

This is not a distinct badge, SAO, or kit. It is the `nrf51prog` git branch of the
[bornhack/badge2018](https://github.com/bornhack/badge2018) repository: a small SWD (Serial
Wire Debug) programmer, written in C by Emil Renner Berthing, that runs on the BornHack 2018
badge's own SiLabs Happy Gecko (EFM32HG322F64G) microcontroller and bit-bangs the debug
protocol needed to flash firmware onto the badge's secondary chip, a Nordic nRF51822
(Cortex-M0, Bluetooth Low Energy).

The badge itself ships with a default firmware on the Happy Gecko; owners who want to program
the nRF51822 radio can compile or download a prebuilt binary of this tool, flash it to the
Happy Gecko temporarily, use it to load their own code onto the nRF51822, then restore the
badge's normal firmware afterward (the programmer itself is not power-optimized and would hurt
battery life if left running). The actual BornHack 2018 badge is catalogued separately as its
own entry.
