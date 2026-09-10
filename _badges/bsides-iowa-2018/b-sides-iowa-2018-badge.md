---
title: B-Sides Iowa 2018 Badge
id: bsides-iowa-2018-b-sides-iowa-2018-badge
layout: badge
parent: BSides Iowa 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-iowa-2018
year: 2018
makers:
- name: Black Cat Labs (G Rice)
  url: https://github.com/blackcatlabs
summary: BSides Iowa's first electronic badge, a low-cost ATtiny85 board with 12 charlieplexed LEDs, designed to be cheap to manufacture and easy for attendees to customize.
functions: LED patterns, personalization, and a broken-out GPIO/SPI header for hacking.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ATtiny85
  leds:
    count: 12
    type: charlieplexed
    note: 8K flash, internal clock
  display: none
  connectivity: []
  battery: CR2032
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
  hardware_url: https://github.com/blackcatlabs/bsidesiowa2018/blob/master/badge.brd
  firmware_url: https://github.com/blackcatlabs/bsidesiowa2018/blob/master/badge.c
  eda_tool: Eagle
  license: GPL-3.0
  bom_url: https://github.com/blackcatlabs/bsidesiowa2018/blob/master/bom.xlsx
  notes: Schematic also published as circuit.pdf; firmware built with Arduino IDE + damellis ATtiny board package; programmed via a 2x3 header or pogo-pin AVR adapter.
links:
- label: github.com/blackcatlabs/bsidesiowa2018
  url: https://github.com/blackcatlabs/bsidesiowa2018
  kind: repo
images: []
contact: {}
notes:
- BSides Iowa's first electronic badge, an ATtiny85-based board with 12 charlieplexed LEDs powered by a CR2032 coin cell, documented on GitHub. Found by the event-year sweep, task bsides-bsides-iowa.
- The sweep title matched the maker's own README title ("B-Sides Iowa Badge"/"B-Sides Iowa 2018 Badge"); kept as-is.
status: listed
sources:
- kind: url
  url: https://github.com/blackcatlabs/bsidesiowa2018
  title: B-Sides Iowa 2018 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-iowa); event read as ''BSides Iowa 2018''.'
- kind: url
  url: https://github.com/blackcatlabs/bsidesiowa2018/blob/master/README.md
  title: bsidesiowa2018 README
  accessed: '2026-09-10'
  note: Confirmed maker (G Rice), ATtiny85/12 charlieplexed LEDs/CR2032 specs, functions, Eagle/Arduino IDE tooling, GPL-3.0 license, and PCB fab (Seeed Fusion).
- kind: url
  url: https://api.github.com/repos/blackcatlabs/bsidesiowa2018/contents/
  title: bsidesiowa2018 repo file listing
  accessed: '2026-09-10'
  note: Repo contains badge.brd, badge.sch, badge.c, bom.xlsx, circuit.pdf, LICENSE (GPL-3.0); no photos of the assembled badge in the repo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Only source found is the maker's own GitHub repo, which is thorough on hardware/firmware but does not state price, quantity made, or distribution/availability, and contains no photo of the assembled board. A web search turned up no press coverage, storefront, or additional images beyond the repo itself, so no images could be saved.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-iowa-2018/b-sides-iowa-2018-badge.glb
  method: kicad
  source_file: badge.brd
  generated: '2026-09-10'
  bytes: 46240
---

BSides Iowa's first electronic badge was designed by G Rice of Black Cat Labs with two goals in mind: keep manufacturing costs low for a small non-profit conference, and make the board friendly for attendees to hack on. The result is a simple ATtiny85-based badge with 12 charlieplexed LEDs, 8K of flash, and a CR2032 coin cell for power, fabricated through Seeed Fusion PCB.

The badge exposes a programmable header (or pogo-pin pads for an AVR programmer) so wearers can flash their own firmware, and breaks out GPIO/SPI for further hacking. The maker's README explicitly invites other conferences to reuse the design as a starting point for their own badges.

## Make your own

The full project — Eagle schematic (`badge.sch`) and board (`badge.brd`) files, a PDF of the circuit, the ATtiny85 firmware (`badge.c`), and a bill of materials (`bom.xlsx`) — is published under the GPL-3.0 license at github.com/blackcatlabs/bsidesiowa2018. Firmware was built in the Arduino IDE using the `damellis/attiny` board package; the badge is programmed either through a soldered 2x3 header or a pogo-pin adapter aligned over the microcontroller.
