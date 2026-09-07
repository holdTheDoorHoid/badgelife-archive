---
title: SAO Digital Multimeter
id: supercon-2024-sao-digital-multimeter
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Thomas Flummer
  url: https://hackaday.io/tf
summary: A compact RP2040/CircuitPython digital multimeter with an SAO connector, OLED screen, rotary mode knob and buzzer, built to measure SAO supply voltage, GPIO levels, resistance, LEDs and continuity, entered in the Supercon 8 (2024) SAO contest.
functions: 'Measures SAO input voltage, SAO GPIO voltage, resistance, and LEDs/diodes; continuity testing with a buzzer; two 2mm banana-socket probe connectors. I2C info reading and GPIO write were planned/work-in-progress at submission.'
look:
  colors: []
  shape: null
  themes:
  - measurement
  - hardware tool
  - learn to solder
tech:
  mcu: RP2040
  leds: null
  display: 0.96" OLED
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: 'Entered in the Supercon 8 (2024) SAO badge contest; not described as sold or distributed to attendees generally. Design files are open for anyone to build their own.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/flummer/dmm-sao
  firmware_url: https://github.com/flummer/circuitpython/tree/hxr-sao-dmm
  eda_tool: KiCad
notes: []
links:
- label: github.com/flummer/dmm-sao
  url: https://github.com/flummer/dmm-sao
  kind: repo
- label: hackaday.io/project/198892-sao-digital-multimeter
  url: https://hackaday.io/project/198892-sao-digital-multimeter
  kind: hackaday
- label: github.com/flummer/circuitpython/tree/hxr-sao-dmm
  url: https://github.com/flummer/circuitpython/tree/hxr-sao-dmm
  kind: repo
images:
- file: assets/images/badges/supercon-2024/sao-digital-multimeter/a8d6abe4d3.jpg
  source: "https://github.com/flummer/dmm-sao"
  credit: "Thomas Flummer"
  caption: "The assembled SAO Digital Multimeter with OLED display, rotary knob, and probe leads"
contact: {}
status: released
sources:
- kind: url
  url: https://github.com/flummer/dmm-sao
  title: SAO Digital Multimeter (flummer/dmm-sao)
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/flummer/dmm-sao
  title: flummer/dmm-sao README
  accessed: '2026-09-07'
  note: 'Confirmed RP2040/CircuitPython, KiCad hardware (CC BY-SA 4.0), MIT-licensed firmware, features (resistance/LED/continuity/voltage/GPIO), 3D-printed case, banana probe sockets, image URL.'
- kind: url
  url: https://hackaday.io/project/198892-sao-digital-multimeter
  title: SAO Digital Multimeter project page (hackaday.io)
  accessed: '2026-09-07'
  note: 'Confirmed maker Thomas Flummer, submission to the Supercon 8 (2024) SAO Contest on 2024-10-20, dimensions (41x75mm), rotary encoder + buttons, pogo-pin PCB stack, multilingual assembly guide.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own repo and Hackaday.io project page both confirm the core facts. No storefront, price, or production-quantity information found; this appears to be a contest entry/open-source build-your-own project rather than something sold or distributed at scale, so get_one fields are mostly left empty. LED count/type not specified by the maker (the device tests LEDs but does not appear to use addressable LEDs itself, so tech.leds is left null rather than guessed). No SAO connector pin-count (v1 vs v2) stated in sources, so tech.sao_version left null.'
last_modified_date: '2026-09-07'
---

The SAO Digital Multimeter is a pocket-sized test tool built by Thomas Flummer for the Supercon 8 (2024) SAO Contest. Rather than being a decorative add-on, it is a working instrument: an RP2040 running CircuitPython drives a 0.96" OLED display, a rotary knob for mode selection, function and system buttons, and a buzzer, letting a badge-hacker check an SAO's supply voltage, GPIO levels, resistance, LED/diode condition, and continuity via a pair of 2mm banana-socket probes. The device is slightly larger than a standard SAO at 41x75mm, housed in a 3D-printed unibody case with pogo-pin connections between its front and base PCBs, and ships (in design form) with an SAO cable extension for reaching recessed connectors on other badges.

The hardware (KiCad schematics, PCB files, and 3D-printable case and probe parts) is released under CC BY-SA 4.0, and the CircuitPython firmware is MIT-licensed, both published on the maker's GitHub. Assembly and user guides are provided in English, German, and Danish. No sale price, production quantity, or storefront was found; the project reads as an open-source contest build that others can replicate rather than a batch sold to attendees. At last check the maker listed I2C device inspection and GPIO-write capability as planned but not yet implemented.

## Make your own

Hardware (KiCad source) and case/probe STL files are at [github.com/flummer/dmm-sao](https://github.com/flummer/dmm-sao); firmware is on a dedicated CircuitPython branch at [github.com/flummer/circuitpython/tree/hxr-sao-dmm](https://github.com/flummer/circuitpython/tree/hxr-sao-dmm). The repo includes a PDF schematic and step-by-step assembly/user manuals in three languages.
