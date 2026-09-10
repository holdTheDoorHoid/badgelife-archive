---
title: HillHacks Badge
id: other-hillhacks-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2016
makers:
- name: Tavish Naruka
  url: https://hackaday.io/ntavish
summary: A simple, cheap ATtiny85-based conference badge made for HillHacks 2016, designed to be end-user assemblable and USB-programmable without extra programmer hardware.
functions: Runs Arduino sketches on an ATtiny85; can be flashed with a Trinket/Micronucleus bootloader for USB programming, or use V-USB code to act as a custom USB device (e.g. keyboard or mouse). Has a pushbutton and a status LED, plus a small prototyping area on the board.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: ATtiny85
  leds: null
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/ntavish/hillhacks2016_badge
  firmware_url: https://github.com/ntavish/hillhacks2016_badge
  eda_tool: KiCad
links:
- label: hackaday.io/project/9926-hillhacks-badge
  url: https://hackaday.io/project/9926-hillhacks-badge
  kind: hackaday
  archived: https://web.archive.org/web/20251118223057/https://hackaday.io/project/9926-hillhacks-badge
- label: github.com/ntavish/hillhacks2016_badge
  url: https://github.com/ntavish/hillhacks2016_badge
  kind: repo
images:
- file: assets/images/badges/other/hillhacks-badge/6c38b47f37.jpg
  source: https://hackaday.io/project/9926-hillhacks-badge
  credit: Tavish Naruka
  caption: The HillHacks 2016 badge PCB
  archived: https://web.archive.org/web/20251118223057/https://hackaday.io/project/9926-hillhacks-badge
- file: assets/images/badges/other/hillhacks-badge/87f3fc30be.jpg
  source: https://hackaday.io/project/9926-hillhacks-badge
  credit: Tavish Naruka
  caption: The HillHacks 2016 badge, assembled
  archived: https://web.archive.org/web/20251118223057/https://hackaday.io/project/9926-hillhacks-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/9926-hillhacks-badge
  title: HillHacks Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''HillHacks''.'
  archived: https://web.archive.org/web/20251118223057/https://hackaday.io/project/9926-hillhacks-badge
- kind: url
  url: https://github.com/ntavish/hillhacks2016_badge
  title: ntavish/hillhacks2016_badge
  accessed: '2026-09-07'
  note: 'Maker''s own repo: KiCad hardware files, Arduino firmware examples, CERN Open Hardware License; confirms open source hardware and firmware.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Made by Tavish Naruka for HillHacks, a hacker/maker gathering held in the Himalayas (India) in 2016 - no matching event id exists in events.yml, so this stays filed under "other". No price, production quantity, or LED count found on either the Hackaday.io project or the GitHub repo. Naruka also gave a "Making a PCB Badge" talk at the HillHacks pre-event (30 April 2016) covering this design.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/hillhacks-badge.glb
  method: kicad
  source_file: badge1.kicad_pcb
  generated: '2026-09-10'
  bytes: 244300
---

Tavish Naruka designed this badge for HillHacks 2016, a small hacker gathering held in the Himalayas in India. The goal, as described on the project's Hackaday.io page, was something simple and cheap to build with no extra programmer hardware required, and possibly assemblable by the wearer. At its core is an ATtiny85, which can be flashed with a Trinket or Micronucleus bootloader to become USB-programmable, or run V-USB code so the badge presents itself as a custom USB device such as a keyboard or mouse. The board carries a single status LED, a pushbutton, and a small prototyping area for further hacking.

## Make your own

Both the hardware and firmware are published on GitHub (ntavish/hillhacks2016_badge) under the CERN Open Hardware License. The repository includes KiCad schematic and board files plus example Arduino sketches, along with setup notes for the Arduino IDE and bootloader installation. The README notes a couple of manufacturing quirks worth knowing before ordering boards: the button footprint needs manual adjustment, and the battery holder pins need slight bending to fit.
