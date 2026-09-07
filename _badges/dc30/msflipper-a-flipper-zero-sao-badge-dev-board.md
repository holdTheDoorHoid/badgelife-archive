---
title: msFlipper, a Flipper Zero SAO & Badge dev board
id: dc30-msflipper-a-flipper-zero-sao-badge-dev-board
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Harbinger LTD (Andrew Nicholson)
  url: https://hackaday.io/awkward-intelligence
summary: A modular expansion board that lets a Flipper Zero talk to SAO and badge headers, breaking out both SAO and Flipper GPIO pins for sniffing, emulating, or driving badge add-ons.
functions: Exposes mirrored Flipper GPIO and SAO/badge pinouts side by side so a Flipper Zero can sniff SAO/badge communications, emulate an SAO, or drive external components; includes an optional back-side resistor and LED for basic signal testing.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: Optional LED and resistor footprint on the back for basic signal indication; the board itself has no MCU.
  display: none
  connectivity:
  - uart
  - i2c
  sao_version: v1
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/186736-msflipper
  firmware_url: null
  eda_tool: null
get_one:
  price: "$1.00"
  price_usd: 1.0
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  - purchase
  where: Originally given away free at DEF CON 30 (and distributed at ToorCamp); later kits and assembled boards were sold on Tindie for $1, though the Tindie listing was marked "on a break" and not actively taking orders as of the last check.
links:
- label: www.tindie.com/products/awkwardai/msflipper-a-flipper-zero-sao-badge-dev-board
  url: https://www.tindie.com/products/awkwardai/msflipper-a-flipper-zero-sao-badge-dev-board/
  kind: store
- label: hackaday.io/project/186736-msflipper
  url: https://hackaday.io/project/186736-msflipper
  kind: hackaday
images:
  - file: assets/images/badges/dc30/msflipper-a-flipper-zero-sao-badge-dev-board/dfac70f5a8.jpg
    source: "https://www.tindie.com/products/awkwardai/msflipper-a-flipper-zero-sao-badge-dev-board/"
    credit: "Harbinger LTD (awkwardai)"
    caption: "The assembled msFlipper board"
  - file: assets/images/badges/dc30/msflipper-a-flipper-zero-sao-badge-dev-board/1e9ebbef18.jpg
    source: "https://hackaday.io/project/186736-msflipper"
    credit: "awkward-intelligence"
    caption: "msFlipper board render/photo"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/awkwardai/msflipper-a-flipper-zero-sao-badge-dev-board/
  title: msFlipper, a Flipper Zero SAO & Badge dev board
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/186736-msflipper
  title: msFlipper project page
  accessed: '2026-09-07'
  note: Maker's own project page; confirms creation date (Aug 2022), ToorCamp/DEF CON distribution, open Gerber files, and board photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker is listed on Hackaday.io as "awkward-intelligence" (Andrew Nicholson, Harbinger LTD, per the Tindie storefront "awkwardai"). The Tindie listing says it was "Originally created for DEFCON 30" as a free giveaway; the Hackaday.io project page says it was created Aug 2022 and distributed at ToorCamp and intended for DEF CON, consistent with DEF CON 30 (Aug 2022). Hardware Gerbers are shared on the Hackaday.io page (msflipperDoen.zip) but no schematic/source design files or firmware were found, so open_source is marked partial rather than yes. No MCU/chip is on the board itself (LED/resistor only); it relies on the host Flipper Zero. Quantity made and current stock are not stated anywhere found.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/msflipper-a-flipper-zero-sao-badge-dev-board/
---

The msFlipper is a small expansion board that bridges the Flipper Zero to the badge world's SAO (Simple/"Shitty" Add-On) and badge-power ecosystem. Rather than housing its own microcontroller, it breaks out the Flipper's GPIO pins alongside a mirrored SAO/badge pinout, so a Flipper Zero owner can sniff traffic between a badge and its SAOs, emulate an SAO to a badge, or drive external components directly from the Flipper. An optional resistor-and-LED footprint on the back gives a quick way to test signals without extra parts.

It was made by Harbinger LTD, doing business as "awkwardai" on Tindie and "awkward-intelligence" on Hackaday.io. The board was created in August 2022 and given away free at DEF CON 30, with additional units handed out at ToorCamp; the front art, done in MS Paint, is where the name comes from. Kits (board, header cables, wires, resistor, LED, and a quick-start guide) and fully-assembled units later appeared on Tindie for a nominal $1, though that listing was marked "on a break" and not taking orders as of this check. Gerber files for the board are shared on the Hackaday.io project page, but no schematic source or firmware repository was found.

## Make your own

Gerber files (`msflipperDoen.zip`) are available on the [Hackaday.io project page](https://hackaday.io/project/186736-msflipper); no separate firmware is needed since the board is passive and relies on the host Flipper Zero's GPIO.
