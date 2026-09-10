---
title: TouchwheelSAO
id: supercon-2024-touchwheelsao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: todbot
  url: https://hackaday.io/hacker/35-todbot
summary: Capacitive touchwheel SAO for Hackaday Supercon 2024 with three interleaved touch pads, three side-lit RGB LEDs, and an ATtiny816 that reports finger position (0-255) over I2C via the standard SAO pinout.
functions: Reads finger position (0-255) across three interleaved capacitive touch pads and reports it over I2C; the three side-lit "Neopixel"-compatible RGB LEDs are also controllable over I2C via a documented register map.
look:
  colors: []
  shape: circle
  themes:
  - hardware tool
tech:
  mcu: ATtiny816
  leds:
    count: 3
    type: RGB
    note: Three "Neopixel"-compatible side-light RGB LEDs shine through the center of the wheel; one additional status LED on the back of the board.
  display: none
  connectivity:
  - i2c
  - uart
  battery: powered by host badge
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
  open_source: true
  hardware_url: https://github.com/todbot/TouchwheelSAO/
  firmware_url: https://github.com/todbot/TouchwheelSAO/tree/main/firmware/TouchwheelSAO_attiny816
  eda_tool: KiCad
links:
- label: hackaday.io/project/199100-touchwheelsao
  url: https://hackaday.io/project/199100-touchwheelsao
  kind: hackaday
- label: github.com/todbot/TouchwheelSAO
  url: https://github.com/todbot/TouchwheelSAO/
  kind: repo
- label: TouchwheelSAO gerbers (production files)
  url: https://todbot.github.io/TouchwheelSAO/schematics/TouchwheelSAO/production/TouchWheelSAO.zip
  kind: fab
- label: TouchwheelSAO schematic PDF
  url: https://todbot.github.io/TouchwheelSAO/schematics/TouchwheelSAO/TouchwheelSAO_sch.pdf
  kind: doc
- label: github.com/astuder/2024-Supercon-8-Add-On-Badge
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2024/touchwheelsao/3ec72ad4a2.jpg
  source: https://github.com/todbot/TouchwheelSAO/
  credit: todbot
  caption: Render of the TouchwheelSAO board
- file: assets/images/badges/supercon-2024/touchwheelsao/6c091a95e4.jpg
  source: https://github.com/todbot/TouchwheelSAO/
  credit: todbot
  caption: Render of the TouchwheelSAO board showing the touch pads and LEDs
- file: assets/images/badges/supercon-2024/touchwheelsao/3ec72ad4a2.jpg
  source: https://github.com/todbot/TouchwheelSAO
  credit: todbot
  caption: 3D render of the Touchwheel SAO board, front view
- file: assets/images/badges/supercon-2024/touchwheelsao/6c091a95e4.jpg
  source: https://github.com/todbot/TouchwheelSAO
  credit: todbot
  caption: 3D render of the Touchwheel SAO board, alternate angle
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/199100-touchwheelsao
  title: TouchwheelSAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/todbot/TouchwheelSAO/
  title: todbot/TouchwheelSAO
  accessed: '2026-09-07'
  note: Repo README and firmware confirm features, ATtiny816 MCU, three RGB LEDs plus a rear status LED, I2C register map, GPL-3.0 license, and links to gerbers/BOM/schematic. Design notes show the chip package was switched from QFN to SOIC and back to QFN during design (Sep 2024).
- kind: url
  url: https://api.github.com/repos/todbot/TouchwheelSAO
  title: todbot/TouchwheelSAO (GitHub API metadata)
  accessed: '2026-09-07'
  note: Confirmed repo license is GPL-3.0 and description ties the project to Hackaday Supercon 2024.
- kind: url
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  title: 2024 Supercon 8 -- Supercon Add-On Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday.io project page and GitHub repo agree on all core facts. Price, quantity made, and distribution/availability details are not stated on either page, so those fields are left empty; the project reads as a maker's own conference badge accessory (todbot is a known prolific SAO/badge designer) rather than a commercial listing, so status is set to released rather than left unknown, since renders/photos and a finished 'production version' exist. No SAO header version (v1/v1.69bis) is stated in the sources. Merged with duplicate entry 'Touchwheel SAO' (supercon-2024-touchwheel-sao).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2024/touchwheel-sao/
---

TouchwheelSAO is a capacitive-touch Simple Add-On board that todbot designed for Hackaday Supercon 2024 (Supercon 8). It arranges three touch pads in an interleaved disk pattern so a finger sliding around the wheel produces a smooth 0-255 position reading, similar in spirit to the maker's earlier "touchwheel0" boards. Three "Neopixel"-compatible RGB LEDs sit beneath the disk and shine through its center, with a fourth status LED on the back of the board; both the touch position and the LEDs are exposed over I2C through a documented register map, and the standard SAO pinout leaves spare GPIO lines wired out to UART TX/RX.

The board runs on an ATtiny816 (the same chip family used in Adafruit's seesaw boards), compiled with the standard Arduino toolchain via megaTinyCore, and uses a modified version of todbot's own TouchyTouch capacitive-sensing library. Design notes in the repository show the MCU package went from QFN to SOIC and back to QFN over the course of September 2024 to suit JLCPCB assembly, and the SAO header footprint had to be hand-corrected late in the process so the board could be assembled correctly.

Hardware and firmware are both fully open source under the GPL-3.0 license: the GitHub repository includes gerbers, a bill of materials, component-position files, an interactive BOM viewer, and a schematic PDF, alongside renders and video of both the prototype and finished "production version" of the board. Neither the Hackaday.io project page nor the GitHub repo states a price, production quantity, or how the board was distributed at Supercon.

## Notes merged from the duplicate entry "Touchwheel SAO"

The Touchwheel SAO is a capacitive-touch add-on board designed by todbot for the Hackaday Supercon 8 badge (2024). It presents three touch pads arranged in an interleaved disk, letting a user's finger position (0-255) be read over I2C, while three "Neopixel"-compatible RGB LEDs shine through the center of the wheel and can likewise be driven over I2C using a documented register map. A fourth status LED sits on the back of the board. The design builds on todbot's earlier "touchwheel0" experiments and runs on an ATtiny816 microcontroller, the same chip family used in Adafruit's seesaw boards, programmed through the standard Arduino toolchain via megaTinyCore.

The SAO was bundled into the official Supercon 8 badge project as a git submodule (see astuder/2024-Supercon-8-Add-On-Badge), meaning it shipped alongside — or as part of — the badge given to Supercon 2024 attendees rather than being sold as a standalone product. The board went through at least two package revisions during development (QFN to SOIC and back to QFN, per the maker's dated build notes) to suit JLCPCB's assembly requirements.

## Make your own

The project is fully open source under GPL-3.0. The repository provides schematics as a PDF, an interactive BOM viewer, and production-ready files (Gerbers, BOM CSV, component-position CSV) suitable for ordering boards from a fab like JLCPCB. Firmware for the ATtiny816 is included and builds with the Arduino IDE plus the megaTinyCore board package; it uses a modified version of todbot's TouchyTouch capacitive-touch library.
