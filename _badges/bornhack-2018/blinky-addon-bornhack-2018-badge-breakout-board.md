---
title: Blinky_addon (BornHack 2018 badge breakout board)
id: bornhack-2018-blinky-addon-bornhack-2018-badge-breakout-board
layout: badge
parent: BornHack 2018
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: bornhack-2018
year: 2018
makers:
- name: BornHack
summary: A small SAO-style breakout board for the BornHack 2018 badge with eight discrete LEDs driven through an I2C GPIO expander, designed as a beginner soldering exercise.
functions: Lights eight LEDs, individually addressable over I2C via the onboard GPIO expander; built as a soldering-practice add-on rather than a game or tool.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - hardware tool
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: Each LED has its own 1K series resistor; driven via a TCA9534 I2C I/O expander rather than directly from a microcontroller.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Distributed at random, unpopulated, to BornHack 2018 attendees by the badge team; people were encouraged to trade for the specific breakout board they wanted.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2018/tree/breakoutboards/Blinky_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bornhack/badge2018/tree/breakoutboards
  url: https://github.com/bornhack/badge2018/tree/breakoutboards
  kind: repo
- label: github.com/bornhack/badge2018/tree/breakoutboards/Blinky_addon
  url: https://github.com/bornhack/badge2018/tree/breakoutboards/Blinky_addon
  kind: repo
images: []
contact: {}
notes:
- A beginner soldering-exercise add-on board for the BornHack 2018 badge that adds blinking LED functionality. Found by the event-year sweep, task bornhack-2018.
- The sweep's summary ("adds blinking LED functionality") matches what the repo confirms; kept title as the maker wrote the folder name (Blinky_addon), matching the sheet's wording.
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2018/tree/breakoutboards
  title: Blinky_addon (BornHack 2018 badge breakout board)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bornhack-2018); event read as ''bornhack-2018''.'
- kind: url
  url: https://github.com/bornhack/badge2018/tree/breakoutboards/Blinky_addon
  title: Blinky_addon folder, breakoutboards branch, bornhack/badge2018
  accessed: '2026-09-08'
  note: Confirmed the KiCad project exists; netlist lists U1 TCA9534 (I2C GPIO expander), J1 labelled "#badgelife" (SAO connector), and D1-D8 LEDs each with a 1K series resistor R1-R8.
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2018/breakoutboards/README.md
  title: Bornhack Badge 2018 - Breakout boards README
  accessed: '2026-09-08'
  note: Confirms these boards plug onto the badge for extra functionality, were distributed unpopulated and at random with badges, and were explicitly untested/experimental.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via the repo's KiCad netlist and README rather than a written spec page from BornHack; no photo of an assembled board was found, so images are still empty. Reclassified type from accessory to sao since it plugs into the badge's SAO-style header (J1 is labelled "#badgelife") rather than being a passive add-on. Price/quantity unknown; boards were given away unpopulated and distributed at random per the README, with attendees trading for the one they wanted.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bornhack-2018/blinky-addon-bornhack-2018-badge-breakout-board.glb
  method: kicad
  source_file: Blinky_addon/Blinky_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 65620
---

Blinky_addon is one of several breakout boards BornHack's badge team designed for the 2018 badge, meant as a beginner-friendly soldering exercise rather than a functional gadget in its own right. The board carries eight LEDs, each behind its own 1K resistor, driven not directly by GPIO pins but through a TCA9534 I2C I/O expander, so building and populating it also serves as an introduction to I2C peripherals. It connects to the host badge through a 4-pin header labelled "#badgelife" in the design files, following the community SAO convention.

Per the breakoutboards branch README, these boards (Blinky_addon alongside siblings like CapSense_addon and LED_addon) were handed out unpopulated and at random with badges at BornHack 2018, with attendees expected to trade among themselves or visit the badge team to get the specific board and components they wanted. The README also notes the boards were untested and experimental at release. No populated/assembled photos or a formal spec page were found; the KiCad hardware files are published in full on GitHub.
