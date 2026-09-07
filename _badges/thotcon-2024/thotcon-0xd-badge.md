---
title: THOTCON 0xD Badge
id: thotcon-2024-thotcon-0xd-badge
layout: badge
parent: Thotcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: thotcon-2024
year: 2025
makers:
- name: Jay (Fourfold)
  url: https://hackaday.io/jmargalus
summary: The official attendee badge for THOTCON 0xD (2025), an ESP32 "Tamagotchi-inspired"
  badge with a 1.3" IPS TFT screen navigated by a parametric capacitive touch wheel
  instead of any moving parts.
functions: iPod-style menu UI navigated by the capacitive touch wheel, on-badge
  mini-games, and OTA firmware updates from day one; badges could also talk to
  each other and to a live conference stats board over MQTT.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - retro computer
  - security
  - hardware tool
tech:
  mcu: ESP32
  leds:
    count: 6
    type: discrete
    note: Row of 6 individual LEDs below the display; firmware repo shows simple
      LED-indicator demo modes.
  display: 1.3" IPS TFT (ST7789, 240x320)
  connectivity:
  - wifi
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '2000'
  availability: unknown
  distribution: []
  where: 'Distributed to attendees of THOTCON 0xD in Chicago, May 30-31, 2025.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/poplicola/thotcon-examples
  firmware_url: https://github.com/poplicola/thotcon-examples
  eda_tool: null
links:
- label: hackaday.io/project/203821-thotcon-0xd-badge
  url: https://hackaday.io/project/203821-thotcon-0xd-badge
  kind: hackaday
- label: poplicola/thotcon-examples (GitHub)
  url: https://github.com/poplicola/thotcon-examples
  kind: repo
images:
  - file: assets/images/badges/thotcon-2024/thotcon-0xd-badge/cfb5bc2634.png
    source: "https://hackaday.io/project/203821-thotcon-0xd-badge"
    credit: "Jay (Fourfold)"
    caption: "The THOTCON 0xD badge, showing its menu screen (Touch Wheel / Mini Games / Credits), touch wheel, THOTCON mascot silkscreen, and lit LED"
contact: {}
notes:
- 2000 fully interactive badges designed/fabbed/shipped.
- 'THOTCON numbers editions in hex; 0xD is the 2025 edition (held May 30-31, 2025
  in Chicago), not 2024. There is no thotcon-2025 entry in _data/events.yml, so
  this entry stays filed under thotcon-2024 per research-guide.md; the year field
  above has been corrected to 2025 to match the sources.'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/203821-thotcon-0xd-badge
  title: Thotcon 0xD Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''THOTCON 0xD''.'
- kind: url
  url: https://hackaday.io/project/203821-thotcon-0xd-badge
  title: Thotcon 0xD Badge - Hackaday.io project page
  accessed: '2026-09-07'
  note: Maker (jay / Fourfold), quantity (2000), MCU (ESP32), display (1.3in IPS
    TFT), capacitive touch wheel input, OTA + MQTT telemetry, laser-cut acrylic
    enclosure, tariff issue during production, published Aug 2025 confirming the
    2025 event date.
- kind: url
  url: https://github.com/poplicola/thotcon-examples
  title: poplicola/thotcon-examples
  accessed: '2026-09-07'
  note: Confirms ESP32 + ST7789 TFT + 6 LEDs + 3 capacitive touch sensors; demo
    firmware only (no gerbers, BOM, or photos in the repo).
- kind: url
  url: https://en.wikipedia.org/wiki/THOTCON
  title: THOTCON - Wikipedia
  accessed: '2026-09-07'
  note: Confirms THOTCON edition-to-year mapping; 0xD occurred May 30-31, 2025,
    and the conference moved to a biannual cycle after 0xC (2023).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday.io project page and GitHub repo confirm the core
    hardware facts, so most of the record is maker-sourced. Could not find price,
    battery/power source, PCB color beyond what's visible in the photo (black
    soldermask), open-source license terms, or whether badges were sold vs. free
    with registration. The GitHub repo explicitly withholds gerbers/BOM/schematics
    ("proprietary content removed"), so make_your_own.open_source is 'partial'
    (firmware examples only, not full hardware files). SAO header presence not
    mentioned by any source, so recorded as 'none' rather than left unknown.
last_modified_date: '2026-09-07'
---

The THOTCON 0xD badge was the official attendee badge for THOTCON 0xD, the Chicago hacker conference's 2025 edition (held May 30-31, 2025). Designed and built by Jay of the studio Fourfold, 2,000 units were produced for the event. Rather than a traditional badge with a knob or button, its main interaction is a parametric capacitive touch wheel wrapped around a 1.3" IPS TFT screen, giving it an iPod-style click-wheel menu with no moving parts. The badge is built around an ESP32, and the visible board carries a row of six LEDs, a stylized THOTCON mascot silkscreen, and the "THOTCON 0xD" edition mark.

Software-wise, the badge shipped with over-the-air firmware updates from day one and used MQTT so units could exchange messages with each other and feed a live conference stats board, alongside on-screen mini-games navigated through the touch wheel. The maker's build write-up also describes some of the production realities of shipping thousands of units quickly, including 1-oz copper/8-8 mil PCB choices made to cut cost and assembly time, a laser-cut acrylic enclosure held together with M2.5 hardware, and an unexpected tariff-classification snag on the TFT panels mid-production.

A cleaned-up firmware repository (three example sketches covering basic touch/LED behavior, a musical "tonechaser" demo, and a menu/game-placeholder build) is public on GitHub, but the maker withheld the Gerbers, bill of materials, and schematics as "proprietary," so the hardware design itself is not fully open.
