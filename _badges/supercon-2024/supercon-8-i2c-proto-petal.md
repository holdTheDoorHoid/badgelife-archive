---
title: I2C Proto Petal
id: supercon-2024-supercon-8-i2c-proto-petal
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Hackaday
  url: https://github.com/Hack-a-Day
summary: A CH32V003-based prototyping SAO for the Supercon 8 badge that can be configured as an arbitrary I2C device, with all chip I/O broken out, a debug LED on PD0, and a Program jumper so the badge itself can flash it.
functions: 'Bare I2C prototyping platform: all CH32V003 GPIO broken out to header pins for the user to wire up sensors, actuators, or other peripherals. Ships with demo firmware that runs the onboard LED as an I2C-controlled blinkie.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: CH32V003
  leds:
    count: 1
    type: null
    note: Single LED wired to pin PD0 for debugging; demo firmware drives it as an I2C blinkie.
  display: null
  connectivity:
  - i2c
  battery: powered by host badge
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
  hardware_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/i2c_proto_petal
  firmware_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/i2c_proto_petal_tutorial
  eda_tool: KiCad
links:
- label: github.com/astuder/2024-Supercon-8-Add-On-Badge
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/i2c_proto_petal
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/i2c_proto_petal
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/i2c_proto_petal_tutorial
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/i2c_proto_petal_tutorial
  kind: repo
images:
- file: assets/images/badges/supercon-2024/supercon-8-i2c-proto-petal/ed05316607.jpg
  source: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/i2c_proto_petal
  credit: Hackaday
  caption: Front of the I2C Proto Petal SAO showing the CH32V003 and broken-out headers
- file: assets/images/badges/supercon-2024/supercon-8-i2c-proto-petal/6e43f478f8.jpg
  source: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/i2c_proto_petal
  credit: Hackaday
  caption: Back of the I2C Proto Petal SAO showing the Program jumper pads
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  title: 2024 Supercon 8 -- Supercon Add-On Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/i2c_proto_petal
  title: hardware/sao/i2c_proto_petal README
  accessed: '2026-09-07'
  note: 'Maker''s own README: CH32V003-based, all I/O broken out, LED on PD0, Program jumper for in-situ flashing from the badge; source of the front/back photos.'
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/i2c_proto_petal_tutorial
  title: i2c_proto_petal_tutorial
  accessed: '2026-09-07'
  note: Tutorial walking through flashing compiled firmware (e.g. blink.bin) onto the petal's CH32V003 via the badge's own REPL/bit-bang programmer.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Official Hackaday/Supercon reference design, not a separate maker's product -- it lives directly in the Supercon 8 Add-On Badge repo alongside the other official petals. No price, quantity, or distribution details were found; it reads as a reference/example petal and companion tutorial (for people to build their own with the published KiCad files and gerbers) rather than a badge that was sold or handed out as a finished unit, but no source states that explicitly, so get_one and status are left as found. LED color/type not specified in the README.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2024/supercon-8-i2c-proto-petal.glb
  method: kicad
  source_file: hardware/sao/i2c_proto_petal/sao_proto.kicad_pcb
  generated: '2026-09-10'
  bytes: 250124
---

The I2C Proto Petal is one of the official SAO ("petal") reference designs published in Hackaday's repo for the Supercon 8 (2024) Add-On Badge. Rather than a fixed-purpose gadget, it is a deliberately minimal prototyping board built around the inexpensive CH32V003 RISC-V microcontroller: every pin on the chip is routed out to the SAO header, leaving the builder free to wire up whatever I2C peripheral they want to create. The only components populated on the board itself are a single debug LED on pin PD0 and a small header that, when jumpered, ties GPIO1 to the CH32's SDIO line so the host badge can program the chip in place without an external programmer.

Hackaday published matching demo firmware showing the onboard LED being toggled as a simple I2C blinkie, plus a companion tutorial (`i2c_proto_petal_tutorial`) walking builders through flashing compiled binaries like `blink.bin` onto the petal directly from the badge's REPL. Full KiCad source and gerbers are included in the hardware folder, making the petal a straightforward starting point for anyone building a custom I2C add-on for the Supercon 8 badge ecosystem.

## Make your own

KiCad hardware files and gerbers are in `hardware/sao/i2c_proto_petal` of the `Hack-a-Day/2024-Supercon-8-Add-On-Badge` repository. To bring one up: populate the board (CH32V003, the PD0 LED, and optionally solder the Program jumper closed if you'll be reflashing it often), then follow the steps in `i2c_proto_petal_tutorial` to push compiled firmware to the chip using the Supercon 8 badge's own bit-bang programmer over its REPL.
