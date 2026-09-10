---
title: BSides Boise 2017 Electronic Badge
id: bsides-boise-2017-bsides-boise-2017-electronic-badge
layout: badge
parent: BSides Boise 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-boise-2017
year: 2017
makers:
- name: BSides Boise 2017 Badge team
summary: A hackable conference badge built around a Lolin ESP-12 NodeMCU (ESP8266) clone, mounted on a breadboard-style PCB with four RGB LEDs, meant to be programmed live at the con and kept afterward.
functions: Learn-to-program badge; attendees control four onboard RGB LEDs via the Arduino IDE for visual feedback while learning ESP8266 development.
look:
  colors: []
  shape: rectangle
  themes:
  - learn to solder
  - hardware tool
tech:
  mcu: ESP8266
  leds:
    count: 4
    type: RGB
    note: Mounted on a 30-pin breadboard-style PCB for visual feedback
  display: none
  connectivity:
  - wifi
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
  open_source: 'yes'
  hardware_url: https://github.com/BSidesBoise/BSidesBoise17Badge
  firmware_url: https://github.com/BSidesBoise/BSidesBoise17Badge
  eda_tool: null
links:
- label: github.com/BSidesBoise/BSidesBoise17Badge
  url: https://github.com/BSidesBoise/BSidesBoise17Badge
  kind: repo
images: []
contact: {}
notes:
- Hackable badge built around a Lolin ESP-12 NodeMCU (ESP8266) with four RGB LEDs on a breadboard-style PCB, Arduino-IDE programmable. Found by the event-year sweep, task bsides-portland.
status: released
sources:
- kind: url
  url: https://github.com/BSidesBoise/BSidesBoise17Badge
  title: BSides Boise 2017 Electronic Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-portland); event read as ''BSides Boise 2017''.'
- kind: url
  url: https://raw.githubusercontent.com/BSidesBoise/BSidesBoise17Badge/master/README.md
  title: BSidesBoise17Badge README
  accessed: '2026-09-10'
  note: 'Maker''s own writeup: design goal, MCU choice (Lolin ESP-12 NodeMCU clone, ESP8266), 4 RGB LEDs, breadboard mount, Arduino IDE programming, Fritzing project by @badgerops, docs/building.md instructions.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Repo confirms design and build details in the maker's own README, so this is a real, released badge (not a stub/rumor). Price, quantity made, and distribution/availability were not stated anywhere in the repo. No photos of the assembled badge were found in the repository (only datasheets and a Fritzing schematic under docs/), so no images were saved. Title matches the maker's own README heading exactly.
last_modified_date: '2026-09-10'
---

The BSides Boise 2017 Electronic Badge is a "hackable" conference badge built by the BSides Boise 2017 badge team around a Lolin ESP-12 NodeMCU clone (ESP8266), mounted on a 30-pin breadboard-style PCB with four RGB LEDs. The team's stated goal was a badge attendees could tinker with during the con and keep using afterward, so it doubles as a learn-to-program platform: the LEDs give simple, immediate visual feedback while attendees write and flash their own code.

The badge is programmed through the Arduino IDE, and the project repository includes a step-by-step guide (docs/building.md, plus a linked Instructables writeup) for configuring the IDE to target the Lolin NodeMCU. Datasheets for the LEDs and the NodeMCU clone are included, along with a Fritzing schematic contributed by GitHub user @badgerops.

Both hardware and firmware are published openly on GitHub. No pricing, production quantity, or distribution details were found in the available sources, and no photos of the assembled badge (as opposed to schematic/datasheet documentation) turned up in the repository.
