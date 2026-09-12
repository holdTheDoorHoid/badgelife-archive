---
title: BSidesDFW 2024 Badge
id: bsidesdfw-2024-bsidesdfw-2024-badge
layout: badge
parent: BSides Dfw 2024
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: bsidesdfw-2024
year: 2024
makers:
- name: hon1nbo
  role: circuit design, PCB layout
- name: ibi5
  role: concept & artwork
- name: BearsInPorts
  role: PCB silkscreen art
summary: A beginner soldering kit and light-up badge for BSidesDFW 2024, built around a 555 timer and 74HC595 shift register driving 13 through-hole LEDs in a chasing pattern.
functions: Chasing LED animation across 13 LEDs, driven by a 555-timer clock into a tri-state 74HC595 shift register operated in LED-sink mode. Chase speed is adjustable via an onboard potentiometer.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 13
    type: discrete
    note: Through-hole LEDs (D1-D13) driven in sink mode by a 74HC595 shift register for higher brightness; one LED position was misplaced on badges issued at the event due to a trace re-route caught after fabrication, corrected in the repo's KiCad files.
  display: none
  connectivity: []
  battery: 2x coin cell (6V)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - kit
  where: Distributed to BSidesDFW 2024 attendees as an event badge/soldering kit.
make_your_own:
  open_source: true
  hardware_url: https://github.com/hon1nbo/bsidesdfw-2024-badge
  firmware_url: null
  eda_tool: KiCad
  gerbers_url: https://github.com/hon1nbo/bsidesdfw-2024-badge/tree/main/gerbers
  license: CERN-OHL-P-2.0
  notes: Full KiCad project, gerbers, component models, and silkscreen art are published in the repo; design intentionally kept simple to teach beginners both soldering and basic KiCad hardware design.
links:
- label: github.com/hon1nbo/bsidesdfw-2024-badge
  url: https://github.com/hon1nbo/bsidesdfw-2024-badge
  kind: repo
  archived: https://web.archive.org/web/20251221212717/https://github.com/hon1nbo/bsidesdfw-2024-badge
images:
- file: assets/images/badges/bsidesdfw-2024/bsidesdfw-2024-badge/45de1ca35c.gif
  source: https://github.com/hon1nbo/bsidesdfw-2024-badge
  credit: hon1nbo
  caption: LED chase animation on the assembled badge
  archived: https://web.archive.org/web/20251221212717/https://github.com/hon1nbo/bsidesdfw-2024-badge
contact: {}
notes:
- Official BSidesDFW 2024 conference badge and beginner soldering kit built around a 555-timer clock feeding a 74HC595 shift register driving a chasing-light LED matrix, running on a 6V coin cell. Found by the event-year sweep, task bsides-bsidesdfw.
- Price and production quantity are not stated in the repo; left empty rather than guessed.
status: released
sources:
- kind: url
  url: https://github.com/hon1nbo/bsidesdfw-2024-badge
  title: BSidesDFW 2024 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsidesdfw); event read as ''BSides DFW 2024''.'
  archived: https://web.archive.org/web/20251221212717/https://github.com/hon1nbo/bsidesdfw-2024-badge
- kind: url
  url: https://raw.githubusercontent.com/hon1nbo/bsidesdfw-2024-badge/main/README.md
  title: hon1nbo/bsidesdfw-2024-badge README
  accessed: '2026-09-10'
  note: Confirmed maker roles, theory of operation (555 timer + 74HC595 sink-mode shift register), open-source KiCad files under CERN-OHL-P-2.0, and the known LED-placement errata.
- kind: url
  url: https://raw.githubusercontent.com/hon1nbo/bsidesdfw-2024-badge/main/INSTRUCTIONS.md
  title: hon1nbo/bsidesdfw-2024-badge assembly instructions
  accessed: '2026-09-10'
  note: Component list confirming 13 LEDs, NE555 (marked NESS59) timer, 74HC595 shift register, potentiometer for chase speed, and coin-cell battery holder.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Maker's own repo confirms the badge, its team, and its design in detail. Price and production quantity are not published anywhere found. Battery is described in the README as "6v supply in the form of coin cells" (plural) but the exact cell count/type is not spelled out beyond that, so battery is recorded as best-supported text rather than a specific part number. type changed from badge to kit since the maker positions it primarily as a beginner soldering kit.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsidesdfw-2024/bsidesdfw-2024-badge.glb
  method: kicad
  source_file: KiCAD files/bsidesdfw badge 2024.kicad_pcb
  generated: '2026-09-10'
  bytes: 183320
---

The BSidesDFW 2024 badge is a beginner-friendly soldering kit distributed to attendees of the conference. Rather than using a microcontroller, it teaches through-hole soldering and basic hardware design with a purely discrete circuit: a 555 timer generates a clock signal (speed adjustable with an onboard potentiometer), which feeds a 74HC595 shift register wired in tri-state sink mode. The shift register walks a single "on" position across 13 LEDs in sequence, creating a chasing-light effect, and running the LEDs in sink mode let the designers use brighter LEDs without adding separate drive transistors. Power comes from a coin-cell battery holder providing roughly 6V, with the diode's forward voltage drop used in place of a linear regulator to keep the bill of materials simple and beginner-friendly.

The badge was a team effort: hon1nbo handled circuit design and PCB layout, ibi5 contributed the concept and artwork, and BearsInPorts did the PCB silkscreen art. The project's GitHub repo doubles as a teaching resource, explaining design choices (like the sink-mode shift register and the omission of a voltage regulator) for newcomers following along in KiCad. The repo also documents a known errata: one LED on the badges actually issued at BSidesDFW was shifted out of its intended position due to a late trace re-route, a mistake caught only after fabrication had started and since fixed in the source files.

## Make your own

The full KiCad project, gerbers, 3D models, and silkscreen artwork are published on GitHub under the CERN-OHL-P-2.0 license, along with a written assembly guide. The component list includes an 8-pin 555 timer, a 16-pin 74HC595 shift register, 13 through-hole LEDs, a handful of resistors, a capacitor, a BC548 transistor, a diode, a potentiometer, an SPDT switch, and a coin-cell battery holder — all through-hole parts chosen to be approachable for someone soldering their first board.
