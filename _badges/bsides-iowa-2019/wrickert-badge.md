---
title: BSidesIowa 2019 Badge
id: bsides-iowa-2019-wrickert-badge
layout: badge
parent: BSides Iowa 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-iowa-2019
year: 2019
makers:
- name: wrickert
summary: An interactive "penny piano" conference badge for BSidesIowa 2019, played by touching inserted pennies and running MicroPython on an ESP32.
functions: 'Functions as a "penny piano": pressing pennies set into the badge triggers sounds/notes. Rechargeable over micro USB; a 1-second polling sleep mode wakes on penny touch.'
look:
  colors: []
  shape: null
  themes:
  - music
  - learn to solder
tech:
  mcu: ESP32
  leds: null
  display: null
  connectivity:
  - usb
  battery: rechargeable, micro USB
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/wrickert/badge
  firmware_url: https://github.com/wrickert/badge
  eda_tool: KiCad
links:
- label: github.com/wrickert/badge
  url: https://github.com/wrickert/badge
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/wrickert/badge
  title: wrickert badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/wrickert/badge
  title: wrickert/badge README
  accessed: '2026-09-07'
  note: README identifies the badge as a "penny piano" made for the BSidesIowa 2019 conference, running MicroPython on an ESP32; rechargeable via micro USB; programmed via serial REPL / ampy.py; sleep mode wakes when a penny is touched.
- kind: url
  url: https://github.com/wrickert/badge/tree/master/Documents
  title: wrickert/badge - Documents folder
  accessed: '2026-09-07'
  note: Contains Des Moines/Iowa-themed art assets (skyline, Iowa outline, BSides logos) and a "lid.png"/"lid.svg" enclosure-lid outline, but no photographs of an assembled unit.
- kind: url
  url: https://github.com/wrickert/badge/tree/master/Schematic
  title: wrickert/badge - Schematic folder
  accessed: '2026-09-07'
  note: Contains a .kicad_pcb file and a BadgeGerbers folder, confirming the PCB was designed in KiCad with gerbers published.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No matching "BSidesIowa 2019" event exists in _data/events.yml (only other BSides city/year combinations are present), so event is left as 'other' with the year set to 2019; report as event_corrected_to candidate if an event is later added. No photo of an assembled badge was found in the repo (only vector/logo art and an enclosure-lid outline), so images were left empty rather than guessed. LED count, colors, price, quantity made, and availability are not stated anywhere in the repo and were left empty.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/wrickert-badge/
model:
  file: assets/models/bsides-iowa-2019/wrickert-badge.glb
  method: kicad
  source_file: Schematic/_autosave-lid.kicad_pcb
  generated: '2026-09-07'
  bytes: 25232
---

The BSidesIowa 2019 conference badge, made by wrickert (also known online as Untitled Electronics), is an ESP32-based "penny piano": attendees play it by touching pennies set into the board, which act as capacitive-style triggers for sound. It runs MicroPython, and the maker's GitHub README documents how to reach the board's serial REPL (115200 baud) and load code with `ampy.py`, including a workaround for the board's 1-second-polling sleep mode ("press any penny to wake the badge up"). It recharges over a micro USB cable and needs no separate programmer.

The project repository publishes the full design: KiCad schematics and PCB layout, gerbers, footprints, firmware, and reference documents (including an ESP32 module reference design and Des Moines/Iowa-themed artwork used on the badge's silkscreen or enclosure lid). No photos of an assembled badge, and no information on price, quantity produced, or how widely it was distributed at BSidesIowa 2019, were found in the available sources.

## Make your own

The hardware and firmware are both published in [github.com/wrickert/badge](https://github.com/wrickert/badge). The `Schematic` folder holds the KiCad project (schematic, PCB, and a `BadgeGerbers` folder ready to send to a fab), `Footprints` holds custom component footprints, and `Firmware` holds the MicroPython code. To reprogram an assembled unit: connect over USB serial at 115200 baud, press Ctrl+C to stop the running program, then use `ampy -p /dev/ttyUSB0 put main.py` (adjusting the port) to load a new script; if the board doesn't respond it may be asleep and can be woken by touching any penny.
