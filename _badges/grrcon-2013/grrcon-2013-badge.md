---
title: GrrCON 2013 Badge
id: grrcon-2013-grrcon-2013-badge
layout: badge
parent: GrrCON 2013
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: grrcon-2013
year: 2013
makers:
- name: GRMakers
summary: A skull-shaped, Arduino Uno Rev3-compatible conference badge made for GrrCON 2013, with schematics, board files and firmware published on GitHub.
functions: Runs as a standard Arduino Uno Rev3 (via the onboard ATmega328P and ATmega16U2 USB interface chip), so it is programmable like any Arduino board after the con.
look:
  colors: []
  shape: skull
  themes:
  - skull
  - security
tech:
  mcu: ATmega328P
  leds: null
  display: none
  connectivity:
  - usb
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
  open_source: 'yes'
  hardware_url: https://github.com/GRMakers/GrrCON_2013_Badge/tree/master/Hardware
  firmware_url: https://github.com/GRMakers/GrrCON_2013_Badge/tree/master/Software
  eda_tool: Eagle
links:
- label: github.com/GRMakers/GrrCON_2013_Badge
  url: https://github.com/GRMakers/GrrCON_2013_Badge
  kind: repo
images: []
contact: {}
notes:
- ATMEGA328P Arduino-based skull-shaped electronic badge for GrrCON 2013, with schematics and firmware published on GitHub. Found by the event-year sweep, task con-derbycon.
status: listed
sources:
- kind: url
  url: https://github.com/GRMakers/GrrCON_2013_Badge
  title: GrrCON 2013 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-derbycon); event read as ''GrrCON 2013''.'
- kind: url
  url: https://github.com/GRMakers/GrrCON_2013_Badge
  title: GRMakers/GrrCON_2013_Badge - README
  accessed: '2026-09-08'
  note: Confirmed the badge is an Arduino Uno Rev3-based board with a skull outline, ATmega328P main processor plus ATmega16U2 for USB, Eagle 6.4 schematic/board files, CC-BY-SA licensed hardware, and a note that the "skull" outline itself is not licensed for reuse without permission.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Only source found is the maker's GitHub repo (GRMakers org), which confirms the badge is real and gives the technical design (ATmega328P + ATmega16U2, Arduino Uno Rev3 architecture, skull-shaped PCB, Eagle CAD files, CC-BY-SA license on the board/schematic). The repo has no photos of an assembled badge, so no images could be saved for this entry. A websearch turned up a YouTube video titled "GrrCON 2013 Badge - designed by Twisted Blades LLC" crediting a different designer name, but the video's actual content was not retrievable (only YouTube boilerplate loaded), so that credit is unconfirmed and not added to makers. Price, quantity made, LED count/type, and availability/distribution are not stated anywhere found and are left empty. A fork exists at github.com/mfarver/GrrCON_2013_Badge but appears to be a plain copy of the same repo, not a separate item.
last_modified_date: '2026-09-10'
model:
  file: assets/models/grrcon-2013/grrcon-2013-badge.glb
  method: kicad
  source_file: GrrCON-Badge-Rev1.brd
  generated: '2026-09-10'
  bytes: 283788
---

The GrrCON 2013 Badge is a skull-shaped conference badge built around the same architecture as an Arduino Uno Rev3: an ATmega328P as the main processor paired with an ATmega16U2 handling USB. GRMakers published the full Eagle 6.4 schematic and board layout, a bill of materials, and the software/bootloader files on GitHub, along with the exact fuse settings used to program the main chip and the USB interface chip.

The board layout and schematic are released under a Creative Commons Share-Alike license, but the README specifically carves out the GrrCON "skull" outline itself, asking that it not be reused without permission — so the design is open in terms of circuit and code, but the shape is treated separately.

Because it shares Arduino Uno Rev3's architecture, the badge can be programmed and used like a standard Arduino board after the conference. No photos of an assembled unit, pricing, quantity, or distribution details were found in the repository or elsewhere during this pass.
