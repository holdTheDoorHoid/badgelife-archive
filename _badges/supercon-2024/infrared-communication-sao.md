---
title: Infrared Communication SAO
id: supercon-2024-infrared-communication-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Alec Probst
  url: https://github.com/alecjprobst
- name: Dmitry Pustovit
  url: https://github.com/DmitryPustovit
summary: A simple-on-air (SAO) add-on that lets two Supercon badges talk to each other over infrared light, handling the IR protocol on its own microcontroller so it looks like a plain I2C peripheral to the host badge.
functions: 'Sends and receives short data packets over IR between two SAO boards. The ATtiny85 on board handles IR encoding/decoding and address-based filtering (each packet carries an address byte so multiple SAOs in range don''t interfere), and exposes the result to the host badge over I2C at address 0x08, with up to a 128-byte receive buffer.'
look:
  colors: []
  shape: null
  themes:
  - radio
tech:
  mcu: ATtiny85
  leds: null
  display: null
  connectivity:
  - ir
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed at Hackaday Supercon 8 (2024) as part of the SAO Contest; the project page mentions limited-edition color variants made for trading.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/alecjprobst/IR-Transceiver-SAO
  eda_tool: null
  notes: 'A separate MicroPython driver library (https://github.com/DmitryPustovit/MicroPython-IR-Transceiver-SAO, MIT licensed) is available for talking to the SAO from a host badge. The main firmware repo did not show hardware/Gerber files or an explicit license during this pass.'
links:
- label: hackaday.io/project/197812-infrared-communication-sao
  url: https://hackaday.io/project/197812-infrared-communication-sao
  kind: hackaday
- label: github.com/alecjprobst/IR-Transceiver-SAO
  url: https://github.com/alecjprobst/IR-Transceiver-SAO
  kind: repo
- label: github.com/DmitryPustovit/MicroPython-IR-Transceiver-SAO
  url: https://github.com/DmitryPustovit/MicroPython-IR-Transceiver-SAO
  kind: repo
images:
  - file: assets/images/badges/supercon-2024/infrared-communication-sao/43c0c7db60.jpg
    source: "https://hackaday.io/project/197812-infrared-communication-sao"
    credit: "Alec Probst"
    caption: "Infrared Communication SAO board"
  - file: assets/images/badges/supercon-2024/infrared-communication-sao/8d9a167548.png
    source: "https://hackaday.io/project/197812-infrared-communication-sao"
    credit: "Alec Probst"
    caption: "IR Communication SAO close-up"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197812-infrared-communication-sao
  title: Infrared Communication SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 Add-On Contest — honorable mention''.'
- kind: url
  url: https://hackaday.io/project/197812-infrared-communication-sao
  title: Infrared Communication SAO
  accessed: '2026-09-07'
  note: 'Confirmed makers (Alec Probst and Dmitry Pustovit), event (Supercon 8 SAO Contest, created Sept 2024, v1.0 by Oct 2024), MCU (ATtiny85), IR parts (TSOP58238 receiver, TSAL6102UL 940nm LED), calculated range ~5-7.7m, and links to both GitHub repos.'
- kind: url
  url: https://github.com/alecjprobst/IR-Transceiver-SAO
  title: 'alecjprobst/IR-Transceiver-SAO'
  accessed: '2026-09-07'
  note: 'Firmware repo for the SAO; PlatformIO-based ATtiny85 firmware, references a build video, no hardware files or license found.'
- kind: url
  url: https://github.com/DmitryPustovit/MicroPython-IR-Transceiver-SAO
  title: 'DmitryPustovit/MicroPython-IR-Transceiver-SAO'
  accessed: '2026-09-07'
  note: 'MIT-licensed MicroPython driver for the SAO; confirms I2C address 0x08, 128-byte receive buffer, address-based packet filtering.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for Hackaday Supercon 8 (2024), not Supercon 2025 as the original sweep guessed; event corrected to supercon-2024. Could not confirm price, quantity made, PCB color(s)/shape, LED count (if any beyond the IR LED itself), battery/power source, or whether hardware design files (schematics/Gerbers) are published anywhere -- the firmware repo only contains code. No storefront or press coverage found beyond the Hackaday.io project page and the two GitHub repos.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2025/infrared-communication-sao/
---

The Infrared Communication SAO is an add-on board by Alec Probst and Dmitry Pustovit, built for Hackaday Supercon 8's 2024 SAO Contest. It lets two badges exchange short data packets over infrared light rather than a wired or radio link: an onboard ATtiny85 handles the IR protocol -- encoding, decoding, and per-packet address filtering so nearby units don't cross-talk -- and presents the result to the host badge over a simple I2C interface (default address 0x08, up to 128 bytes per receive buffer). The IR link itself uses a TSOP58238 receiver paired with a TSAL6102UL 940nm IR LED, with a calculated indoor range of roughly 5 meters under normal light and up to about 7.7 meters with a higher LED current setting.

The project's firmware is published on GitHub (ATtiny85 code, PlatformIO-based, with a build-instruction video), and Pustovit separately released an MIT-licensed MicroPython driver library so a host badge can talk to the SAO without reimplementing the protocol. Hardware design files (schematics, board layout, Gerbers) were not found in either repository during this research pass, so it's unclear whether they were published anywhere. The Hackaday.io project page mentions limited-edition color variants made for trading at Supercon, but does not give a price, production quantity, or a general sales channel -- it reads as a badge-add-on-contest project distributed in person rather than sold.
