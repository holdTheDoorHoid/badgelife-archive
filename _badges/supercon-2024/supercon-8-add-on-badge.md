---
title: Supercon Add-On Badge
id: supercon-2024-supercon-8-add-on-badge
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2024
year: 2024
makers:
- name: Hackaday
  url: https://github.com/Hack-a-Day
summary: 'The official Hackaday Supercon 8 (2024) badge: a hub for six SAO ports built around a Raspberry Pi Pico W (RP2040) running MicroPython, designed so attendees combine I2C add-ons and can program a CH32V003 proto petal directly from the badge.'
functions: 'Runs MicroPython out of the box (open a serial terminal, Thonny, or VSCode to program it). Acts as an I2C hub for its six SAO ports -- reading/writing SAOs like the LED and Touchwheel petals via writeto_mem()/readfrom_mem(). Also doubles as a programmer for the included i2c_proto_petal, a CH32V003 RISC-V protoboard SAO for building custom I2C devices (using Charles Lohr''s ch32fun library). A separate community project, "Super-8", let multiple badges talk to each other by bridging their I2C buses over MQTT.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Used at Hackaday Supercon 8 (2024) and reused at 2025 Hackaday Europe; sources do not state how it was distributed.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware
  firmware_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/software
  eda_tool: EasyEDA
links:
- label: github.com/astuder/2024-Supercon-8-Add-On-Badge
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2024/supercon-8-add-on-badge/da51f9f001.jpg
  source: "https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge"
  credit: "Hackaday"
  caption: "The Supercon 8 add-on badge with six SAO ports populated"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  title: 2024 Supercon 8 -- Supercon Add-On Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  title: 2024 Supercon 8 -- 2025 Hackaday Europe -- Simple Add-On Badge
  accessed: '2026-09-07'
  note: 'Official Hackaday repo README: describes the badge as a six-SAO I2C hub running MicroPython, the CH32V003 proto petal, and the Super-8 multi-badge MQTT bridge.'
- kind: url
  url: https://raw.githubusercontent.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/main/software/micropython/RPI_PICO_W-20240602-v1.23.0.uf2
  title: software/micropython firmware file listing
  accessed: '2026-09-07'
  note: 'Filename (RPI_PICO_W ... .uf2) confirms the badge''s MCU is an RP2040 (Raspberry Pi Pico W board/module).'
- kind: url
  url: https://api.github.com/repos/Hack-a-Day/2024-Supercon-8-Add-On-Badge/contents/hardware/badge
  title: hardware/badge file listing
  accessed: '2026-09-07'
  note: 'File extensions (.CSPcbDoc, .cdr) in the hardware/badge folder indicate EasyEDA (Pro) design files rather than KiCad.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'No PCB color, LED count/type, display, SAO header version, price, quantity-made, or distribution-method figures were stated in any source found, so those fields are left empty/unknown.'
last_modified_date: '2026-09-07'
---

The 2024 Supercon 8 badge, made by Hackaday for its annual Supercon conference, is built around a hub-and-spoke idea: instead of packing in a screen or game, it puts six SAO ports on the board and lets attendees' add-ons talk to each other over I2C. The badge itself runs MicroPython on a Raspberry Pi Pico W (RP2040), so getting started is as simple as plugging it into a computer and opening a serial terminal, Thonny, or VS Code -- no toolchain required.

One of the SAOs that shipped with the badge is a protoboard petal built around a CH32V003 RISC-V microcontroller, which the main badge can program directly, using Charles Lohr's `ch32fun` library. This turns the badge into a mini development platform: attendees could design and flash their own I2C devices during the con. A community side project called "Super-8," built during Supercon by a contributor going by Aask, bridged multiple badges' I2C buses together over MQTT, letting badges cooperate across the room (at the cost of replacing the stock firmware).

The hardware and firmware are fully open, published across two GitHub repositories (the official `Hack-a-Day` org repo and a contributor fork by `astuder`), with schematics, PCB design files (EasyEDA), a BOM, and the MicroPython image included. The badge was also reused at 2025 Hackaday Europe. Design details like solder-mask color, LED count, unit price, and how many were produced were not stated in the sources found.
