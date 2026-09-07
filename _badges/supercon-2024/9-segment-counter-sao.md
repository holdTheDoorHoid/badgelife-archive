---
title: 9-Segment Counter SAO
id: supercon-2024-9-segment-counter-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: martinbros
  url: https://hackaday.io/martinbros
summary: A Simple Add-On with a two-digit 9-segment (not 7-segment) RGB display that counts things, built as an entry to Supercon 8's SAO contest.
functions: Increment/decrement a stored count via onboard buttons, over I2C, or via a clock input pin (~150Hz); each digit can be set to one of 7 colors; up to 49 numbers can be stored in non-volatile EEPROM.
look:
  colors:
  - red
  - blue
  shape: rectangle
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: ATtiny84
  leds:
    count: null
    type: RGB
    note: 9-segment display elements are RGB (7 selectable colors per digit); also breaks out a neopixel-compatible pin (GP2, 470-ohm resistor) for chaining additional addressable LEDs.
  display: 9-segment 2-digit counter display
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Made as an entry to the Supercon 8 (2024) SAO contest; not known to have been sold.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/martinbros/9SegCounter
  firmware_url: https://github.com/martinbros/9SegCounter
  eda_tool: null
  license: GPL-3.0
  notes: Repo includes CAD/PCB design folders, firmware source, and build photos; specific KiCad/Gerber/BOM file paths were not confirmed.
links:
- label: hackaday.io/project/198460-9-segment-counter-sao
  url: https://hackaday.io/project/198460-9-segment-counter-sao
  kind: hackaday
- label: github.com/martinbros/9SegCounter
  url: https://github.com/martinbros/9SegCounter
  kind: repo
images:
  - file: assets/images/badges/supercon-2024/9-segment-counter-sao/3b4a72797d.jpg
    source: "https://hackaday.io/project/198460-9-segment-counter-sao"
    credit: "martinbros"
    caption: "9-Segment Counter SAO, assembled with 2-digit 9-segment display"
  - file: assets/images/badges/supercon-2024/9-segment-counter-sao/60a8cc09b3.jpg
    source: "https://hackaday.io/project/198460-9-segment-counter-sao"
    credit: "martinbros"
    caption: "9-Segment Counter SAO PCB detail"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198460-9-segment-counter-sao
  title: 9-Segment Counter SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 SAO Contest entry''.'
- kind: url
  url: https://hackaday.io/project/198460-9-segment-counter-sao
  title: 9-Segment Counter SAO
  accessed: '2026-09-07'
  note: 'Confirmed maker (martinbros), event (Supercon 8 SAO Contest, 2024), MCU (ATtiny84), functions, and repo link.'
- kind: url
  url: https://github.com/martinbros/9SegCounter
  title: martinbros/9SegCounter
  accessed: '2026-09-07'
  note: 'Confirmed open-source hardware+firmware, GPL-3.0 license, and that the design was inspired by counting conversations at Supercon.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Event corrected from supercon-2025 to supercon-2024: the project page and repo both describe it as an entry to the Supercon 8 (2024) SAO contest, and the entry''s own year field already said 2024. Price, quantity made, LED count, and SAO header version were not stated on either the Hackaday.io page or the GitHub repo and are left empty. Availability is unclear -- no storefront was found, so it is treated as a contest entry rather than a sold product; status set to "released" since photos of the assembled unit exist. Confidence is medium: the maker''s own pages are the source for everything, but several tech fields (LED count, sao_version) could not be confirmed.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2025/9-segment-counter-sao/
---

The 9-Segment Counter SAO is a Simple Add-On built by Hackaday.io user martinbros as an entry to the Supercon 8 (2024) SAO contest. Instead of the traditional 7-segment digit, it displays two digits using a 9-segment layout, with each segment capable of RGB color, giving each digit 7 selectable colors. The maker describes the original motivation as tracking how many conversations you have at Supercon.

An ATtiny84 microcontroller drives the display and can be controlled three ways: front-panel buttons to increment or decrement the count and cycle colors, an I2C interface (address 4) for external read/write access to the display and the chip's 512-byte EEPROM, or a clock input pin that increments the count on a falling edge at speeds up to roughly 150Hz. Up to 49 stored numbers can be held in non-volatile memory. A neopixel-compatible output pin is also broken out for chaining additional addressable LEDs.

## Make your own

Hardware and firmware are published under the GPL-3.0 license at github.com/martinbros/9SegCounter, which includes CAD/PCB design folders, firmware source, and build photos. The repository's specific file layout (Gerbers, BOM, schematic format) was not fully inventoried during this pass -- check the repo directly for build files.
