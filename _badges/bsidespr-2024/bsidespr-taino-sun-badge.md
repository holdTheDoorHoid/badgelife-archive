---
title: BSidesPR Taino Sun Badge
id: bsidespr-2024-bsidespr-taino-sun-badge
layout: badge
parent: BSides Puerto Rico 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsidespr-2024
year: 2024
makers:
- name: So11Deo6loria / BSides Puerto Rico badge team
summary: The official badge for BSides Puerto Rico 2024, a Taino sun design with 50 addressable LEDs and a default Puerto Rico flag color pattern that attendees can reconfigure.
functions: Lights up in a default Puerto Rico flag pattern across 50 WS2812B LEDs arranged around the sun motif; ships with alternate color schemes (e.g. a "cinnamon toast crunch" palette) and a config file so wearers can set their own startup color and pattern; goes into a low-power dormant mode via the button/timeout and wakes on a button press; exposes a UART shell for interacting with the firmware.
look:
  colors: []
  shape: null
  themes:
  - nature
tech:
  mcu: Raspberry Pi Pico
  leds:
    count: 50
    type: WS2812B
    note: Individually addressable LEDs arranged in the sun's rays; default pattern renders the Puerto Rico flag.
  display: none
  connectivity:
  - uart
  battery: CR2477 coin cell
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Given to attendees of BSides Puerto Rico 2024; the badge team ran a talk and a hands-on workshop at the con to help people customize it.
make_your_own:
  open_source: true
  hardware_url: https://github.com/So11Deo6loria/bsidesPRSun/tree/main/hardware
  firmware_url: https://github.com/So11Deo6loria/bsidesPRSun/tree/main/firmware
  eda_tool: KiCad
links:
- label: github.com/So11Deo6loria/bsidesPRSun
  url: https://github.com/So11Deo6loria/bsidesPRSun
  kind: repo
images:
- file: assets/images/badges/bsidespr-2024/bsidespr-taino-sun-badge/29472f8848.gif
  source: https://github.com/So11Deo6loria/bsidesPRSun
  credit: So11Deo6loria / BSides Puerto Rico badge team
  caption: Promotional GIF of the Taino Sun badge lighting up
contact: {}
notes:
- Official BSides Puerto Rico 2024 badge, a customizable sun-themed design with configurable color patterns; team ran a hands-on badge-hacking workshop at the con. Found by the event-year sweep, task bsides-bsidespr.
- The repo's README title and firmware/README call it "BSidesPR Taino Sun" (no trailing "Badge"); kept the sweep's "Badge" wording in the entry title since that is how the sheet listed it.
status: released
sources:
- kind: url
  url: https://github.com/So11Deo6loria/bsidesPRSun
  title: BSidesPR Taino Sun Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsidespr); event read as ''bsidespr-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/So11Deo6loria/bsidesPRSun/main/README.md
  title: bsidesPRSun README
  accessed: '2026-09-10'
  note: Confirmed it is the official 2024 BSidesPR badge, highly configurable, warns continuous LED use limits battery life; makers spoke and ran a workshop at the con.
- kind: url
  url: https://api.github.com/repos/So11Deo6loria/bsidesPRSun/contents/hardware/bsidesPR.csv
  title: bsidesPR.csv (BOM)
  accessed: '2026-09-10'
  note: Bill of materials confirms Raspberry Pi Pico MCU, 50x WS2812B LEDs, and a CR2477-style coin cell holder.
- kind: url
  url: https://raw.githubusercontent.com/So11Deo6loria/bsidesPRSun/main/firmware/source/constants.py
  title: firmware/source/constants.py
  accessed: '2026-09-10'
  note: LED_COUNT=50, UART pins/baud rate, default Puerto Rico flag color scheme and an alternate palette defined in the firmware.
- kind: url
  url: https://raw.githubusercontent.com/So11Deo6loria/bsidesPRSun/main/firmware/source/main.py
  title: firmware/source/main.py
  accessed: '2026-09-10'
  note: Confirms button-triggered low-power/dormant mode with wake-on-button, and a UART shell thread for the badge.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: No price, quantity, or storefront was found; the badge appears to have been distributed to BSidesPR 2024 attendees rather than sold, so availability/price/quantity are left empty. Hardware is KiCad; no separate Gerber/fab share link found beyond what's committed in the repo's hardware/fabrication folders. No maker bio/social links were found beyond the GitHub org "So11Deo6loria".
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsidespr-2024/bsidespr-taino-sun-badge.glb
  method: kicad
  source_file: hardware/bsidesPR.kicad_pcb
  generated: '2026-09-10'
  bytes: 411568
---

The Taino Sun badge was the official badge for BSides Puerto Rico 2024, designed and built by the con's own badge team (published under the GitHub handle So11Deo6loria). It's a Raspberry Pi Pico-based PCB badge with 50 individually addressable WS2812B LEDs arranged around a stylized sun, running off a CR2477 coin cell. Out of the box it boots into a Puerto Rico flag color pattern, but the firmware ships with additional palettes and reads a `config.json` so wearers can pick their own startup color, flag/pattern, and sleep timeout.

The badge is power-conscious: a button both wakes it from a low-power dormant state and can put it back to sleep, and the README warns that running the LEDs continuously will drain the battery quickly. It also exposes a UART shell for interacting with the firmware over serial. The team gave a talk in the con's Main Hall and ran a Saturday workshop to help attendees learn to customize and troubleshoot their badges.

## Make your own

The full KiCad hardware (schematic, PCB, BOM, fabrication outputs, and a 3D model) and the MicroPython firmware source are published in the [bsidesPRSun GitHub repo](https://github.com/So11Deo6loria/bsidesPRSun). The BOM lists a Raspberry Pi Pico, 50x WS2812B LEDs, and the passive/power components needed to drive them from a coin cell.
