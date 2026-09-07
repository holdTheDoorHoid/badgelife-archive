---
title: Touchwheel SAO
id: supercon-2024-touchwheel-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: todbot
  url: https://github.com/todbot/TouchwheelSAO
summary: A capacitive touch-wheel SAO by todbot (ATtiny816 firmware, I2C memory-map interface) that was distributed with the Supercon 8 badge and is included in the badge repo as a git submodule.
functions: 'Three interleaved capacitive touch pads report finger position (0-255) over I2C; three side-light "Neopixel"-compatible RGB LEDs (plus one status LED on the back) are also controllable over I2C via a documented register map.'
look:
  colors: []
  shape: circle
  themes:
  - hardware tool
tech:
  mcu: ATtiny816
  leds:
    count: 4
    type: RGB
    note: Three side-light Neopixel-compatible RGB LEDs shining through the center disk, plus one status LED on the back of the board.
  display: null
  connectivity:
  - i2c
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed with the Hackaday Supercon 8 (2024) badge; bundled into astuder's 2024-Supercon-8-Add-On-Badge repo as a git submodule.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/todbot/TouchwheelSAO
  firmware_url: https://github.com/todbot/TouchwheelSAO/tree/main/firmware/TouchwheelSAO_attiny816
  eda_tool: null
links:
- label: github.com/astuder/2024-Supercon-8-Add-On-Badge
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  kind: repo
- label: github.com/todbot/TouchwheelSAO
  url: https://github.com/todbot/TouchwheelSAO
  kind: repo
images:
- file: assets/images/badges/supercon-2024/touchwheel-sao/3ec72ad4a2.jpg
  source: "https://github.com/todbot/TouchwheelSAO"
  credit: "todbot"
  caption: "3D render of the Touchwheel SAO board, front view"
- file: assets/images/badges/supercon-2024/touchwheel-sao/6c091a95e4.jpg
  source: "https://github.com/todbot/TouchwheelSAO"
  credit: "todbot"
  caption: "3D render of the Touchwheel SAO board, alternate angle"
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
  url: https://github.com/todbot/TouchwheelSAO
  title: todbot/TouchwheelSAO
  accessed: '2026-09-07'
  note: "Maker's own repo README: features, chip (ATtiny816), LED/touch details, I2C register map, open-source hardware/firmware files, and board renders."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Maker's README (todbot/TouchwheelSAO) confirms the design was made for Hackaday Supercon 2024 and is fully open source (schematics, Gerbers, BOM, firmware). No price, production quantity, or availability status is published anywhere found; it appears to have been a bundled/free add-on with the Supercon 8 badge rather than sold separately, so distribution is recorded as free_drop and get_one.price/quantity are left empty. Could not confirm PCB solder-mask color from the fetched text (only renders were available as images, not a colored spec)."
last_modified_date: '2026-09-07'
---

The Touchwheel SAO is a capacitive-touch add-on board designed by todbot for the Hackaday Supercon 8 badge (2024). It presents three touch pads arranged in an interleaved disk, letting a user's finger position (0-255) be read over I2C, while three "Neopixel"-compatible RGB LEDs shine through the center of the wheel and can likewise be driven over I2C using a documented register map. A fourth status LED sits on the back of the board. The design builds on todbot's earlier "touchwheel0" experiments and runs on an ATtiny816 microcontroller, the same chip family used in Adafruit's seesaw boards, programmed through the standard Arduino toolchain via megaTinyCore.

The SAO was bundled into the official Supercon 8 badge project as a git submodule (see astuder/2024-Supercon-8-Add-On-Badge), meaning it shipped alongside — or as part of — the badge given to Supercon 2024 attendees rather than being sold as a standalone product. The board went through at least two package revisions during development (QFN to SOIC and back to QFN, per the maker's dated build notes) to suit JLCPCB's assembly requirements.

## Make your own

The project is fully open source under GPL-3.0. The repository provides schematics as a PDF, an interactive BOM viewer, and production-ready files (Gerbers, BOM CSV, component-position CSV) suitable for ordering boards from a fab like JLCPCB. Firmware for the ATtiny816 is included and builds with the Arduino IDE plus the megaTinyCore board package; it uses a modified version of todbot's TouchyTouch capacitive-touch library.
