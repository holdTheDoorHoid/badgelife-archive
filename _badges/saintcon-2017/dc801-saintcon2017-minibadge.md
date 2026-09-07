---
title: DC801-SAINTCON2017-Minibadge
id: saintcon-2017-dc801-saintcon2017-minibadge
layout: badge
parent: Saintcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2017
year: 2017
makers:
- name: hamster
  url: https://github.com/hamster
summary: 'A small DC801-themed SAINTCON 2017 minibadge with two automatic slow-cycling RGB LEDs, usable as a minibadge or a shirt pin.'
functions: 'No interactivity: two 3mm RGB LEDs with built-in auto-color-cycling ICs light up automatically when powered, no MCU or programming involved.'
look:
  colors:
  - black
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 2
    type: 'discrete (3mm auto-cycling RGB, self-contained IC per LED)'
    note: 'LED brightness set by choice of R1: 0 ohm (brightest, 20-55mA), 470 ohm (bright, 3-4mA), or 1k ohm (dim, 1.5-2mA).'
  display: none
  connectivity: []
  battery: 'none (minibadge mode, powered by host SAINTCON badge); optional coin-cell holder board included for standalone shirt-pin mode'
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  firmware_url: null
  eda_tool: KiCad
  license: MIT
  notes: 'Repo includes KiCad PCB files, 3D renders, a BOM (per-unit cost ~$0.91 at 100-unit pricing as of 10/2017), assembly instructions, instruction cards, and a separate battery-holder board for shirt-pin mode.'
links:
- label: github.com/hamster/DC801-SAINTCON2017-Minibadge
  url: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  kind: repo
images:
  - file: assets/images/badges/saintcon-2017/dc801-saintcon2017-minibadge/1530c0055b.jpg
    source: "https://github.com/hamster/DC801-SAINTCON2017-Minibadge"
    credit: "hamster"
    caption: "Front of the assembled DC801 SAINTCON 2017 minibadge"
  - file: assets/images/badges/saintcon-2017/dc801-saintcon2017-minibadge/e54e04fd37.jpg
    source: "https://github.com/hamster/DC801-SAINTCON2017-Minibadge"
    credit: "hamster"
    caption: "Powered DC801 minibadge showing the RGB LEDs lit"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  title: DC801-SAINTCON2017-Minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''SAINTCON 2017''.'
- kind: url
  url: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  title: DC801-SAINTCON2017-Minibadge README
  accessed: '2026-09-07'
  note: 'README and BOM: confirms DC801 theme, two auto-cycling RGB LEDs, minibadge/shirt-pin modes, KiCad files, MIT license, BOM cost ~$0.91/unit at 100 qty (10/2017), battery holder board for shirt-pin mode.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own repo confirms design and BOM. No quantity manufactured, sale price, or distribution method (e.g. free drop vs. sold) is stated anywhere in the repo, so get_one fields are left empty. No MCU is used; the LEDs are self-contained auto-cycling parts, not driven by a controller.'
last_modified_date: '2026-09-07'
---

This is a DC801-themed minibadge made for SAINTCON 2017 by a GitHub user going by "hamster." It plugs into the pin headers of the main SAINTCON 2017 conference badge (or can be worn on its own as a shirt pin) and lights up with two 3mm RGB LEDs that cycle color automatically on their own, without any microcontroller or firmware involved. Builders choose one of three resistor values for R1 to set the LED brightness, from a bright 20-55mA down to a dim 1.5-2mA.

The project is fully open source, with KiCad PCB files, 3D renders, a bill of materials, and printed instruction cards all published in the maker's GitHub repository under the MIT license. The BOM shows an estimated cost of about $0.91 per unit at 100-unit component pricing as of October 2017. A companion board is also included for mounting a coin-cell battery so the minibadge can run standalone as a shirt pin instead of drawing power from the host badge.

No source found states how many units were actually built, whether it was sold or given away, or its retail price, so those fields are left blank.

## Make your own

1. Insert the two LEDs into the back of the board (shorter leg toward the top), bend the legs over the pads, trim, and solder.
2. Choose and solder resistor R1: 0 ohm for brightest (20-55mA), 470 ohm for bright (3-4mA), or 1k ohm for dim (1.5-2mA).
3. For minibadge mode: break pin headers and 8-pin sockets to size, insert the socket pins into the SAINTCON badge, place the minibadge on top, and solder both sides.
4. For shirt-pin mode: skip the pin headers and instead solder the included tie-tack pin to the large pad at the top; optionally add the battery-holder board from the "Shirt Pin Battery" folder for standalone power.

Source: https://github.com/hamster/DC801-SAINTCON2017-Minibadge (KiCad files, BOM, renders, MIT license).
