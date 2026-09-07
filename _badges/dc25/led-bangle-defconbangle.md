---
title: LED Bangle (defconbangle)
id: dc25-led-bangle-defconbangle
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc25
year: 2017
makers:
- name: Nisha K.
  url: https://nishakm.github.io/things/defconbangle/
summary: A one-off 3D-printed LED wristbangle Nisha K. built as a gift for a friend heading to DEF CON 25 (2017), lit by a strip of neopixels driven by an Adafruit Gemma board.
functions: Cycles through three different blinking/lighting patterns on its neopixel strip; battery-powered so it runs untethered while worn.
look:
  colors:
  - black
  shape: null
  themes:
  - wearable
  - jewelry
tech:
  mcu: Adafruit Gemma
  leds:
    count: 13
    type: RGB
    note: Two short neopixel strips soldered together into one 13-LED run, backed in black.
  display: none
  connectivity: []
  battery: coin cell (6V holder)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '1 (made as a personal gift, not sold)'
  availability: not_released
  distribution: []
  where: 'Never distributed; a one-off given to a friend.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/nishakm/blinkybracelet
  firmware_url: https://github.com/nishakm/blinkybracelet
  eda_tool: null
  notes: 'Repo includes FreeCAD design files (basic_bangle.fcstd/.fcstd1) and an STL for the 3D-printed bangle body, plus Arduino sketches for the Gemma. The maker''s blog post cites GPL v2 for some library code; the GitHub repo itself is licensed Apache-2.0 — noted here as a source disagreement, not resolved.'
links:
- label: nishakm.github.io/things/defconbangle
  url: https://nishakm.github.io/things/defconbangle/
  kind: website
- label: nishakm/blinkybracelet (GitHub)
  url: https://github.com/nishakm/blinkybracelet
  kind: repo
images:
- file: assets/images/badges/dc25/led-bangle-defconbangle/db131398ac.jpg
  source: "https://nishakm.github.io/things/defconbangle/"
  credit: "Nisha K."
  caption: "The finished LED bangle worn on the wrist"
- file: assets/images/badges/dc25/led-bangle-defconbangle/fb0e822393.jpg
  source: "https://nishakm.github.io/things/defconbangle/"
  credit: "Nisha K."
  caption: "Neopixel strip wiring soldered to the back strip"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://nishakm.github.io/things/defconbangle/
  title: LED Bangle (defconbangle)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc25 (DEF CON 25, 2017 - one-off made for a friend, precursor project to the DC503 Banglet)''.'
- kind: url
  url: https://github.com/nishakm/blinkybracelet
  title: nishakm/blinkybracelet
  accessed: '2026-09-07'
  note: Source repo for firmware and 3D-printed bangle CAD files; confirms Apache-2.0 license and file contents.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own blog post and linked GitHub repo both confirm this was a one-off gift made for DEF CON 25 (2017), not a sold or distributed item. Exact LED strip part number (e.g. WS2812B vs SK6812) not stated by the maker, so tech.leds.type is left as generic RGB. Blog text says code is GPL2.0-licensed while the repo itself shows an Apache-2.0 LICENSE file; left both facts recorded rather than guessing which is authoritative. No further press or third-party coverage found.'
last_modified_date: '2026-09-07'
---

Nisha K. built this LED bangle as a one-off gift for a friend attending DEF CON 25 in 2017, documenting the build on her personal site. It is a 3D-printed black wristband housing a run of 13 neopixel-style RGB LEDs (two shorter strips soldered together), driven by an Adafruit Gemma board and powered by a coin-cell holder. The firmware cycles through three blinking light patterns.

The project was never sold or distributed — a single unit was made and given away — but Nisha published the design files and code on GitHub (nishakm/blinkybracelet), including FreeCAD source and an STL for the bangle body plus the Arduino sketches used to drive the LEDs. She describes it as more of a personal learning project (particularly around charlieplexed LED driving code) than a polished, reproducible build.
