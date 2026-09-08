---
title: Unofficial 36C3 Badge
id: 36c3-2019-unofficial-36c3-badge
layout: badge
parent: 36C3
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: 36c3-2019
year: 2019
makers:
- name: Thomas Flummer
  url: https://thomasflummer.com
summary: A bring-your-own-controller badge PCB with 8 WS2812B LEDs, made for 36C3, that ships as bare PCB plus LEDs and lets the wearer hack in whatever microcontroller they like.
functions: No onboard controller or firmware of its own; the 8 addressable LEDs are driven by whatever microcontroller the wearer wires in (the maker's own build ran a CircuitPython rainbow animation on an Adafruit Feather M4 Express).
look:
  colors:
  - orange
  - black
  shape: null
  themes:
  - minimalist
  - learn to solder
  - hardware tool
tech:
  mcu: none
  leds:
    count: 8
    type: WS2812B
    note: Board ships without a controller; 8x WS2812B and 8x 100nF decoupling caps included. Maker's demo build used an Adafruit Feather M4 Express running CircuitPython.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'Example CircuitPython firmware (a NeoPixel rainbow animation, code.py) is published inline on the maker''s project page; no PCB/Gerber files or a repo link were found.'
links:
- label: thomasflummer.com/projects/36c3-badge
  url: https://thomasflummer.com/projects/36c3-badge/
  kind: website
images:
- file: assets/images/badges/36c3-2019/unofficial-36c3-badge/56d8905b29.jpg
  source: "https://thomasflummer.com/projects/36c3-badge/"
  credit: "Thomas Flummer"
  caption: "The unofficial 36C3 badge PCB"
- file: assets/images/badges/36c3-2019/unofficial-36c3-badge/871aabadc6.jpg
  source: "https://thomasflummer.com/projects/36c3-badge/"
  credit: "Thomas Flummer"
  caption: "The badge mounted with an Adafruit Feather M4 Express controller"
contact: {}
notes:
- Bring-your-own-controller badge PCB with 8 WS2812B LEDs for 36C3 in Leipzig, designed to accept external microcontrollers like the Adafruit Feather M4. Found by the event-year sweep, task ccc-adjacent.
- 'Maker''s own title is lowercase "Unofficial 36c3 badge"; kept the sweep''s title-case wording "Unofficial 36C3 Badge" for consistency with the archive''s other 36C3 entries.'
status: listed
sources:
- kind: url
  url: https://thomasflummer.com/projects/36c3-badge/
  title: Unofficial 36C3 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:ccc-adjacent); event read as ''36C3 2019''.'
- kind: url
  url: https://thomasflummer.com/projects/36c3-badge/
  title: Unofficial 36c3 badge
  accessed: '2026-09-08'
  note: Maker's own project page; confirmed design (bare PCB, 8x WS2812B, no controller included), the AllPCB orange finish, Bleeptrack logo art, and the example CircuitPython firmware.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own project page. Price, quantity made, and availability (whether it was sold, given away, or is still obtainable) are not stated anywhere on the page and could not be found elsewhere; no PCB/hardware design files or a repo link were found, only the inline example firmware. No press or third-party coverage located.'
last_modified_date: '2026-09-08'
---

This is a deliberately minimal, bring-your-own-controller badge Thomas Flummer designed for 36C3 (Chaos Communication Congress, Leipzig, 2019), inspired by the earliest Hackaday Superconference badge. The PCB ships bare, with no microcontroller: it includes only 8 WS2812B addressable LEDs, 8 matching 100nF decoupling capacitors, and a lanyard, leaving the choice of brain, and the resulting hacks, entirely up to whoever wears it. The board uses AllPCB's "red" soldermask option to get an orange finish over copper, with a matte black silkscreen carrying artwork by Bleeptrack (the same logo used on 34C3's Fairydust congress) on the back.

Flummer's own build used an Adafruit Feather M4 Express running CircuitPython, wired to the LED data line with three short wirewrap connections and mounted face-in against the badge PCB to keep the sandwich thin. He published a short example firmware, a simple NeoPixel rainbow animation, on the project page along with build notes such as trimming and re-balling header pins so solder joints do not snag on clothing.

No pricing, production quantity, or distribution details are given on the maker's page, and no PCB design files or repository were found, so it is unclear how many were made or how attendees obtained one.
