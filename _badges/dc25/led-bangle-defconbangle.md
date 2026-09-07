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
  battery: 2x coin cell (6V holder)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 1 (made as a personal gift, not sold)
  availability: not_released
  distribution: []
  where: Never distributed; a one-off given to a friend.
make_your_own:
  open_source: true
  hardware_url: https://github.com/nishakm/blinkybracelet
  firmware_url: https://github.com/nishakm/blinkybracelet
  eda_tool: null
  notes: Repo includes FreeCAD design files (basic_bangle.fcstd/.fcstd1) and an STL for the 3D-printed bangle body, plus Arduino sketches for the Gemma. The maker's blog post cites GPL v2 for some library code; the GitHub repo itself is licensed Apache-2.0 — noted here as a source disagreement, not resolved.
links:
- label: nishakm.github.io/things/defconbangle
  url: https://nishakm.github.io/things/defconbangle/
  kind: website
- label: nishakm/blinkybracelet (GitHub)
  url: https://github.com/nishakm/blinkybracelet
  kind: repo
images:
- file: assets/images/badges/dc25/led-bangle-defconbangle/db131398ac.jpg
  source: https://nishakm.github.io/things/defconbangle/
  credit: Nisha K.
  caption: The Adafruit Gemma board mounted on the bangle, held in hand
- file: assets/images/badges/dc25/led-bangle-defconbangle/fb0e822393.jpg
  source: https://nishakm.github.io/things/defconbangle/
  credit: Nisha K.
  caption: Neopixel strip wiring soldered to the back strip
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://nishakm.github.io/things/defconbangle/
  title: LED Bangle (defconbangle)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as dc25 (DEF CON 25, 2017 - one-off made as a gift for a friend, worn to the "503 party" at the con).'
- kind: url
  url: https://github.com/nishakm/blinkybracelet
  title: nishakm/blinkybracelet
  accessed: '2026-09-07'
  note: Source repo for firmware and 3D-printed bangle CAD files; confirms Apache-2.0 license and file contents.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched both the maker''s blog post and the GitHub repo and confirmed every remaining field and body sentence against them. Two corrections made: (1) the caption on db131398ac.jpg wrongly said "worn on the wrist" - the blog has no such photo; both saved images are close-up construction shots (the Gemma board mounted on the bangle, and the soldered strip wiring), so the caption was corrected to match what the image actually shows. (2) A source note claimed this was a "precursor project to the DC503 Banglet" - the blog post does not mention any DC503 or Banglet project (it only mentions the bangle being worn to "the 503 party" at DEF CON), so that unsupported claim was removed. Also corrected tech.battery from "coin cell" to "2x coin cell" per the blog''s own description of two coin batteries totaling 6V. Everything else (maker, event/year, one-off/never-sold status, Gemma MCU, 13-LED two-strip build, three blinking patterns, GPLv2-vs-Apache-2.0 license
    discrepancy, repo contents) is directly supported by the two cited sources. Exact LED part number (WS2812B vs SK6812) is still not stated by the maker, so tech.leds.type remains generic RGB. No further press or third-party coverage found.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc25/led-bangle-defconbangle.glb
  method: kicad
  source_file: dc5032018banglet.brd
  generated: '2026-09-07'
  bytes: 141896
---

Nisha K. built this LED bangle as a one-off gift for a friend attending DEF CON 25 in 2017, documenting the build on her personal site. It is a 3D-printed black wristband housing a run of 13 neopixel-style RGB LEDs (two shorter strips soldered together), driven by an Adafruit Gemma board and powered by a coin-cell holder. The firmware cycles through three blinking light patterns.

The project was never sold or distributed — a single unit was made and given away — but Nisha published the design files and code on GitHub (nishakm/blinkybracelet), including FreeCAD source and an STL for the bangle body plus the Arduino sketches used to drive the LEDs. She describes it as more of a personal learning project (particularly around charlieplexed LED driving code) than a polished, reproducible build.
