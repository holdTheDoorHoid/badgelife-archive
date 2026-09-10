---
title: Saintcon 2023 Minibadge (RP2040, 72-LED matrix)
id: saintcon-2023-saintcon-2023-minibadge-rp2040-72-led-matrix
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: redactd
  url: https://www.tindie.com/stores/redactd/
summary: A three-PCB-stack SAINTCON 2023 minibadge built around an RP2040, driving a 72-LED RGB matrix with scrolling text.
functions: Displays custom scrolling text on the LED matrix, cycled through display modes with a capacitive touch button; the maker states it has secret functionality when paired with the official SAINTCON 2023 attendee badge. Buyers could request a custom message with a chosen text color and an optional sparkle animation.
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - text
  - minibadge
tech:
  mcu: RP2040
  leds:
    count: 72
    type: RGB
    note: 1x1 RGB LEDs arranged as a matrix on the middle of three stacked PCBs
  display: LED matrix
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $25
  price_usd: 25
  quantity: ''
  availability: sold_out
  availability_note: Listed as out of stock on Tindie since January 25, 2024 (checked 2026-09-08).
  distribution:
  - purchase
  where: Sold by the maker (redactd) on Tindie for $25.
make_your_own:
  open_source: true
  hardware_url: https://github.com/im-redactd/saintcon2023_minibadge
  firmware_url: https://github.com/im-redactd/saintcon2023_minibadge
  eda_tool: null
links:
- label: www.tindie.com/products/redactd/saintcon-2023-minibadge
  url: https://www.tindie.com/products/redactd/saintcon-2023-minibadge/
  kind: store
- label: github.com/im-redactd/saintcon2023_minibadge
  url: https://github.com/im-redactd/saintcon2023_minibadge
  kind: repo
images:
- file: assets/images/badges/saintcon-2023/saintcon-2023-minibadge-rp2040-72-led-matrix/d6261df821.jpg
  source: https://www.tindie.com/products/redactd/saintcon-2023-minibadge/
  credit: redactd
  caption: The three-board minibadge stack showing the RP2040 board, LED matrix, and top acrylic/PCB layer
- file: assets/images/badges/saintcon-2023/saintcon-2023-minibadge-rp2040-72-led-matrix/5176e09cbc.jpg
  source: https://www.tindie.com/products/redactd/saintcon-2023-minibadge/
  credit: redactd
  caption: The minibadge lit up displaying scrolling text on the 72-LED matrix
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/redactd/saintcon-2023-minibadge/
  title: Saintcon 2023 Minibadge (RP2040, 72-LED matrix)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''saintcon-2023''.'
- kind: url
  url: https://github.com/im-redactd/saintcon2023_minibadge
  title: im-redactd/saintcon2023_minibadge
  accessed: '2026-09-08'
  note: Maker's GitHub repo with hardware and firmware source; confirms RP2040 MCU and open-source status.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (maker, price, RP2040, 72-LED matrix, three-board stack, GitHub source) confirmed directly on the maker's own Tindie listing and GitHub repo. Connectivity, battery, and quantity made are not stated anywhere found and are left empty. No third-party press coverage located.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2023/saintcon-2023-minibadge-rp2040-72-led-matrix.glb
  method: kicad
  source_file: Hardware/saintcon-rp2040-platform.kicad_pcb
  generated: '2026-09-10'
  bytes: 134388
---

This SAINTCON 2023 minibadge, made by redactd, is a three-PCB stack-up: a bottom board carrying an RP2040 microcontroller, a middle board holding a 72-LED matrix of 1x1 RGB LEDs, and a top board used as a mechanical/cover layer. It shows scrolling text on the matrix, with a capacitive touch button to cycle through display modes. The maker sold it on Tindie for $25 and offered buyers a custom message with their choice of text color and an optional sparkle animation effect.

The listing also mentions "secret functionality when paired with the official SAINTCON 2023 attendee badge," though no further detail on what that interaction does was found. The badge went out of stock on Tindie in January 2024. Hardware and firmware source are published on GitHub (im-redactd/saintcon2023_minibadge), built around PlatformIO with an Arduino-mbed core and an alternate branch for a different core, with SWD debugging support via Tag-Connect or JLink.

## Make your own

Source files (schematics and firmware) are available at [github.com/im-redactd/saintcon2023_minibadge](https://github.com/im-redactd/saintcon2023_minibadge). The repo is built with PlatformIO; flashing/debugging is done over SWD (Tag-Connect TC2050-IDC-NL or a JLink EDU Mini).
