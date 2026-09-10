---
title: H2HC 2015 Badge
id: h2hc-2015-h2hc-2015-badge
layout: badge
parent: H2HC 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: h2hc-2015
year: 2015
makers:
- name: security-bits.de (Brian)
  url: https://security-bits.de/
summary: A conference badge for H2HC 2015 built as a customized Arduino Leonardo, directly programmable from the Arduino IDE.
functions: 'General-purpose I/O board: 8 GPIO pins plus UART, I2C, and SPI (with three chip-select lines), all remapped to the badge''s own pin numbering. No badge-specific game or CTF function is documented.'
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: ATmega32u4 (Arduino Leonardo)
  leds: null
  display: none
  connectivity:
  - uart
  - i2c
  - spi
  battery: null
  sao_version: none
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
- label: security-bits.de/electronics/badges/h2hc_15
  url: https://security-bits.de/electronics/badges/h2hc_15/
  kind: website
- label: security-bits.de/electronics/badges/h2hc_18
  url: https://security-bits.de/electronics/badges/h2hc_18/
  kind: website
  note: H2HC 2018 badge writeup; references the 2015 badge as prior work and notes it can be reused as an Arduino-compatible programmer.
images:
  - file: assets/images/badges/h2hc-2015/h2hc-2015-badge/dec26edfe2.jpg
    source: "https://security-bits.de/electronics/badges/h2hc_15/"
    credit: "security-bits.de (Brian)"
    caption: "H2HC 2015 badge front, showing Arduino Leonardo-based PCB"
  - file: assets/images/badges/h2hc-2015/h2hc-2015-badge/c8ad17d6da.jpg
    source: "https://security-bits.de/electronics/badges/h2hc_15/"
    credit: "security-bits.de (Brian)"
    caption: "H2HC 2015 badge back"
contact: {}
notes:
- The original sweep only saw this badge mentioned as prior work on the H2HC 2018 writeup page; a dedicated page for the 2015 badge itself was since found and confirms it directly (security-bits.de/electronics/badges/h2hc_15/).
- No price, quantity, LED, or display information is published on the maker's page; left empty rather than guessed.
- No hardware/firmware source files are linked from the page.
status: released
sources:
- kind: url
  url: https://security-bits.de/electronics/badges/h2hc_18/
  title: H2HC 2018 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''H2HC 2015''.'
- kind: url
  url: https://security-bits.de/electronics/badges/h2hc_15/
  title: H2HC 2015 Badge
  accessed: '2026-09-10'
  note: Maker's own dedicated page for this badge; confirms it as a customized Arduino Leonardo run at 5V, gives the remapped pinout (8 GPIO, UART, I2C, SPI with 3 chip-select lines), and provides front/back/layout photos.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-10'
  notes: Fact-checked against both cited pages directly. The h2hc_15 page confirms it is a customized Arduino Leonardo run at 5V with the stated remapped pinout (8 GPIO, UART, I2C, SPI with 3 chip-select lines on A3-A5) and shows front/back/layout photos; it does not name "ATmega32u4" verbatim, that chip is the standard MCU on any Arduino Leonardo, so tech.mcu is a safe inference rather than a direct quote. The h2hc_18 page confirms the cross-reference to the 2015 badge as a reusable programmer. Fixed a wrong title on the h2hc_18 source entry (was mislabeled "H2HC 2015 Badge"). Price, quantity, availability, LED/display specs, and source files remain unpublished anywhere found, so those fields stay empty.
last_modified_date: '2026-09-10'
---

The H2HC 2015 Badge is a customized Arduino Leonardo built by security-bits.de (Brian) for the H2HC security conference in Brazil. Running at 5V, it uses the ATmega32u4 microcontroller and can be programmed directly from any Arduino-compatible IDE. The badge's original pin layout was remapped during redesign, exposing 8 general-purpose I/O pins alongside UART, I2C, and SPI (with three separate chip-select lines) for interfacing with other hardware.

The badge is documented on the maker's own site with front, back, and layout photos, but no pricing, production quantity, or availability details are published. A later H2HC 2018 badge writeup by the same maker references this 2015 badge as prior work, noting it can also serve as an Arduino-compatible programmer for its successor — suggesting continuity in security-bits.de's ongoing series of H2HC badges.
