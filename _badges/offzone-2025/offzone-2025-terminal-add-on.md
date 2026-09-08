---
title: OFFZONE 2025 Terminal add-on
id: offzone-2025-offzone-2025-terminal-add-on
layout: badge
parent: OFFZONE 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2025
year: 2025
makers:
- name: BI.ZONE / Craft.Zone
summary: A solder-it-yourself SAO shaped like a computer terminal, built around an LMC555 timer chip that blinks three white LEDs to look like a terminal cursor and status lights.
functions: 'Blinking LED "terminal" display: an LMC555 astable timer drives three white LEDs (one facing down as a "screen" cursor, two facing sideways) with no microcontroller involved.'
look:
  colors:
  - black
  - white
  shape: rectangle
  themes:
  - retro computer
  - hardware tool
  - learn to solder
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: 3x white 1206 LEDs driven by an LMC555 astable oscillator, not individually addressable.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Distributed as a DIY kit/build at OFFZONE 2025 (Craft.Zone add-on line); the maker''s repo gives PCB order specs and a BOM rather than a storefront listing.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2025/terminal_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2025/terminal_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/terminal_addon
  kind: repo
images:
- file: assets/images/badges/offzone-2025/offzone-2025-terminal-add-on/13d1441d3e.png
  source: "https://github.com/bi-zone/offzone-hw/tree/master/2025/terminal_addon"
  credit: "BI.ZONE / Craft.Zone"
  caption: "Terminal add-on PCB preview render"
- file: assets/images/badges/offzone-2025/offzone-2025-terminal-add-on/a46bc844e9.jpg
  source: "https://github.com/bi-zone/offzone-hw/tree/master/2025/terminal_addon"
  credit: "BI.ZONE / Craft.Zone"
  caption: "Assembled terminal add-on, front"
contact: {}
notes:
- Terminal/console-themed add-on board for the OFFZONE 2025 badge. Found by the event-year sweep, task con-phdays.
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/terminal_addon
  title: OFFZONE 2025 Terminal add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2025''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025/terminal_addon
  title: offzone-hw / 2025 / terminal_addon (README, BOM, KiCad files)
  accessed: '2026-09-08'
  note: 'Repo default branch is master (the entry''s original "main" link 404s but the GitHub UI auto-redirects); README gives PCB order spec, BOM, and assembly steps confirming an LMC555-driven 3-LED SAO with a PLD-6 connector.'
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/README.md
  title: offzone-hw repository root README
  accessed: '2026-09-08'
  note: 'Confirms the repo is BI.ZONE/Craft.Zone''s public archive of OFFZONE add-on boards, published as DIY solder kits (order PCB via Gerbers, source parts via the linked BOM).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own repo (README, BOM, KiCad schematic/PCB files) rather than a storefront or press writeup, so no independent price, quantity, or distribution-event confirmation exists beyond the repo itself. No maker website beyond GitHub was found. Could not confirm price, quantity made, or exact distribution method (kit sold at the con vs. free build station) - repo is written as a DIY-at-home guide, but Craft.Zone add-ons are historically handed out/sold at OFFZONE itself, so distribution is left as kit/unknown pending a firsthand report. SAO connector is a 6-pin PLD-6 header per the BOM, read as SAO v1.69bis (6-pin) per the archive''s vocabulary, though the repo does not name it as an SAO standard explicitly.'
last_modified_date: '2026-09-08'
---

The Terminal add-on is one of several add-on boards BI.ZONE / Craft.Zone published for OFFZONE 2025, styled to look like a small computer terminal. It has no microcontroller: an LMC555 timer chip runs in astable mode to blink three white 1206 LEDs, one aimed downward like a screen cursor and two aimed sideways as status lights. The board is black FR4 with white silkscreen and connects to a host badge through a 6-pin PLD connector.

Like the rest of the Craft.Zone add-on line, it is published as an open, solder-it-yourself kit rather than sold pre-assembled: the repository gives PCB fabrication specs (2-layer FR4, black soldermask, HASL finish), a full BOM, Gerbers, and step-by-step soldering instructions aimed at newcomers, alongside the KiCad source files for anyone who wants to modify the design.

## Make your own

Hardware files (KiCad project, PCB, schematic, Gerbers, and BOM) are published at https://github.com/bi-zone/offzone-hw/tree/master/2025/terminal_addon. Order a 2-layer FR4 PCB (1.5 mm, 18 or 35 um copper, black soldermask, white silkscreen, HASL finish) from the Gerbers in `terminal_addon_gbr`, then hand-solder in this order per the README: the LMC555 (U1, matching the pin-1 arrow), the four resistors (R1 1 kOhm, R2 100 kOhm, R3-R5 220 Ohm each), the three white LEDs observing polarity (D1 facing down, D2/D3 facing sideways), the 10 uF capacitor (C1), and finally the PLD-6 connector.
