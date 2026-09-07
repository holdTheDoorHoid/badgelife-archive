---
title: beepBadge
id: other-beepbadge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: lle
  url: https://github.com/lle
summary: A chainable musical con badge with a beeper/speaker and RGB LEDs; badges plug into each other left-to-right and each holder's stored tune plays in sequence.
functions: Stores a short tune per badge; when badges are physically linked, the leftmost badge's PLAY button triggers the tunes to play in order down the chain, building a collaborative musical sequence.
look:
  colors: []
  shape: null
  themes:
  - music
  - hardware tool
tech:
  mcu: ATmega328P
  leds:
    count: null
    type: WS2812B
    note: Uses the Adafruit NeoPixel library (RGB control module in firmware).
  display: none
  connectivity:
  - uart
  battery: 3x AAA
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/lle/beepBadge/tree/main/hw
  firmware_url: https://github.com/lle/beepBadge/tree/main/firmware
  eda_tool: Eagle
links:
- label: github.com/lle/beepBadge
  url: https://github.com/lle/beepBadge
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/lle/beepBadge
  title: beepBadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/lle/beepBadge/main/readme.md
  title: 'lle/beepBadge: readme.md'
  accessed: '2026-09-07'
  note: Maker's own description, instructions for use, programming method, and acknowledgments (design borrows from the Northsec Pegasis badge and a "Hello my name is" badge).
- kind: url
  url: https://raw.githubusercontent.com/lle/beepBadge/main/firmware/platformio.ini
  title: beepBadge platformio.ini
  accessed: '2026-09-07'
  note: Confirms ATmega AVR target (Arduino Uno framework, 8MHz), usbasp upload protocol, and Adafruit NeoPixel dependency for RGB LEDs.
- kind: url
  url: https://api.github.com/repos/lle/beepBadge/git/trees/main?recursive=1
  title: beepBadge repo file tree
  accessed: '2026-09-07'
  note: Full file listing; hardware board files named "hackfest.brd/.sch/.pro/.cam" (possible working/event name, unconfirmed), Eagle CAD project, gerbers present, no maker photos in the repo.
- kind: url
  url: https://api.github.com/users/lle
  title: GitHub user lle
  accessed: '2026-09-07'
  note: Maker's public GitHub bio ("HW maker and popcorn lover"); no location, company, or event affiliation listed.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No specific convention or year is named anywhere in the repo or maker profile, so event is left as "other" and year as unset/0. The hardware board files are named "hackfest" (hackfest.brd, hackfest.sch, hackfest.pro, hackfest.cam), which may be a working title or the actual event it was built for, but there is no "hackfest" entry in events.yml and no corroborating source, so this is not treated as confirmed. LED count is not stated (NeoPixel library used, but the schematic/gerbers were not opened to count LEDs). No price, quantity, or storefront/availability info was found anywhere; this looks like a one-off personal/DIY project rather than something sold. No maker photos exist in the repository to save. Physical badge-to-badge chaining uses 5-pin connectors (per CAD parts: 5pinMale/5pinFemale) but the exact signaling protocol was not documented beyond a "commControl" firmware module, so connectivity is left as a general guess (uart) rather than asserted with confidence.'
last_modified_date: '2026-09-07'
---

beepBadge is a chainable, musical con badge by maker "lle," built as a mashup of an idea from a previous job, a badge concept for a rave, and the tune-creation minigame from Animal Crossing. Each badge stores its own short tune; when several badges are physically plugged together edge-to-edge, pressing PLAY on the leftmost one plays each connected badge's tune in sequence from left to right, so a chain of badge-holders collectively builds a musical sequence. The badge runs on an ATmega328P (Arduino Uno target at 8MHz) with RGB LEDs driven through the Adafruit NeoPixel library, is powered by 3x AAA batteries, and is programmed over an on-board ISP header using a USBASP-style programmer with PlatformIO.

The hardware borrows design elements from the Northsec "Pegasis" badge and a "Hello my name is" badge, per the maker's own acknowledgments, and was beta-tested with help from a collaborator credited as "Angel." The project is fully open source: Eagle CAD schematics/board files, a gerber archive, and STEP models for its connectors, battery holder, buzzer, switches, and micro-USB port are published in the `hw` folder, alongside complete PlatformIO firmware source in the `firmware` folder covering button handling, sequencing, sound, memory, and inter-badge communication. No convention, year, price, or production quantity is stated anywhere in the repository or the maker's GitHub profile, and no photos of the finished badge are included in the repo.

## Make your own

The hardware is designed in Eagle (`hw/hackfest.sch`, `hw/hackfest.brd`) with gerbers already exported (`hw/gerber/gerber.zip`) and STEP models for sourced parts (microUSB jack, 5-pin male/female link connectors, 3xAAA battery holder, power switch, tactile switch, buzzer) under `hw/cad`. Firmware lives in `firmware/`, built with PlatformIO targeting an Arduino Uno-compatible ATmega328P at 8MHz; flash it over the labeled "Prog Port" (+, -, rst) using a USBASP-type ISP programmer, matching pinout by hand.
