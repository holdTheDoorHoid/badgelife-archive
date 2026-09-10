---
title: LED Blinky Addon
id: bornhack-2018-led-addon
layout: badge
parent: BornHack 2018
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: bornhack-2018
year: 2018
makers:
- name: BornHack
summary: A single-LED SAO breakout board designed as a beginner soldering exercise for the BornHack 2018 badge.
functions: Lights one through-hole LED from the badge's VCC/GND rails; no logic or blinking circuitry of its own.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: 5mm through-hole LED
  display: null
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Distributed unpopulated (bare PCB, no components) at random with BornHack 2018 badges; more could be traded for or picked up from the badge team.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2018/tree/breakoutboards/LED_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bornhack/badge2018/tree/breakoutboards/LED_addon
  url: https://github.com/bornhack/badge2018/tree/breakoutboards/LED_addon
  kind: website
images: []
contact: {}
notes:
- Sweep found the title as 'LED_addon' (the repo folder/directory name); the schematic itself titles the board "LED Blinky Addon", used here.
- 'The breakoutboards branch README states plainly: "these boards are NOT tested, so consider them experimental." Treat functionality as unverified beyond the schematic.'
status: listed
sources:
- kind: url
  url: https://github.com/bornhack/badge2018/tree/breakoutboards/LED_addon
  title: LED_addon
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2018/breakoutboards/README.md
  title: Bornhack Badge 2018 - Breakout boards (branch README)
  accessed: '2026-09-10'
  note: Explains the breakoutboards branch is a set of unpopulated, experimental add-on PCBs distributed randomly with the 2018 badges for soldering practice.
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2018/breakoutboards/LED_addon/LED_addon.sch
  title: LED_addon.sch
  accessed: '2026-09-10'
  note: KiCad schematic confirms it is a single LED wired to VCC/GND through a 2x2 ShittyAddon-footprint SAO connector, titled "LED Blinky Addon".
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed via the maker's (BornHack) own GitHub repo and schematic; no photos of an assembled unit exist since the boards were distributed bare/unpopulated and the branch itself says they are untested. No press or third-party coverage found. Price and quantity made are not stated anywhere.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bornhack-2018/led-addon.glb
  method: kicad
  source_file: LED_addon/LED_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 20328
---

The LED Blinky Addon is one of several small breakout boards BornHack designed to plug into the SAO header of the BornHack 2018 conference badge. Rather than being a finished gadget, it's a deliberately simple beginner soldering exercise: a single 5mm through-hole LED wired straight across the badge's VCC and GND pins through a 2x2 ShittyAddon-style SAO connector, with no microcontroller or driver circuitry of its own.

These add-on boards (which also included a CapSense addon and a Blinky addon among others) were handed out unpopulated and at random alongside the main badges, so attendees could solder on their own components, trade boards with each other, or pick up spares from the badge team. BornHack's own branch README for the project describes the whole set as experimental and explicitly untested.

The hardware files (KiCad schematic, PCB layout, and netlist) are published in the `breakoutboards` branch of BornHack's `badge2018` GitHub repository, making it fully open source, though no firmware is needed since the board is purely passive.

