---
title: Remote Control SAO
id: supercon-2024-remote-control-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Ben Combee
  url: https://hackaday.io/unwiredben
summary: A Simple Add-On that turns a badge into a reprogrammable infrared remote control, built for the Supercon 8 (2024) SAO Contest.
functions: Emits IR codes to control TVs and other IR-compatible devices; 12 capacitive touch pads act as remote buttons; red and green status LEDs shine through the PCB to show mode/activity.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - remote
tech:
  mcu: ATtiny1614
  leds:
    count: 2
    type: discrete
    note: One red and one green single-color LED, mounted to shine through the PCB.
  display: none
  connectivity:
  - i2c
  - ir
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/197866-remote-control-sao
  url: https://hackaday.io/project/197866-remote-control-sao
  kind: hackaday
images:
  - file: assets/images/badges/supercon-2024/remote-control-sao/9c3c43061f.jpg
    source: "https://hackaday.io/project/197866-remote-control-sao"
    credit: "Ben Combee"
    caption: "Remote Control SAO board"
  - file: assets/images/badges/supercon-2024/remote-control-sao/9f4bf74824.jpg
    source: "https://hackaday.io/project/197866-remote-control-sao"
    credit: "Ben Combee"
    caption: "Remote Control SAO, back side"
contact: {}
notes: []
status: announced
sources:
- kind: url
  url: https://hackaday.io/project/197866-remote-control-sao
  title: Remote Control SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 SAO Contest entry''.'
- kind: url
  url: https://hackaday.io/project/197866-remote-control-sao
  title: Remote Control SAO
  accessed: '2026-09-07'
  note: 'Maker name, event/year, MCU, LED, IR/touch functions, and SAO connector pinout confirmed from the Hackaday.io project page and its build logs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for the Supercon 8 (2024) SAO Contest, not Supercon 2025 as originally filed; event corrected to supercon-2024. Also uses a Microchip CAP1114 capacitive-touch/LED-driver IC alongside the ATtiny1614. Project logs describe prototype runs (5 PCBs + stencil from JLCPCB for ~$21; ~$120 in parts for 25 boards) but no finished price, quantity, or public release/availability was found, and no hardware/firmware repo link was found on the project page, so those fields are left empty. Still shown as an active Hackaday.io project (status kept as announced rather than released).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2025/remote-control-sao/
---

The Remote Control SAO is a Simple Add-On by Ben Combee (unwiredben), built as an entry in the Supercon 8 (2024) SAO Contest at Hackaday Superconference. Rather than just decorating a badge, it turns the SAO port into a working infrared remote control: an ATtiny1614 microcontroller drives an IR emitter and reads a 12-pad capacitive touch surface (via a Microchip CAP1114 touch/LED-driver chip) so the badge wearer can send programmable IR codes to a TV or other IR-controlled device. Two small LEDs, one red and one green, are mounted so their light shines through the PCB itself to indicate status.

The project page documents early prototyping, including small JLCPCB runs (five boards plus stencil for about $21) and a rougher per-unit parts cost when building a batch of 25, but does not state a final retail price, a total quantity produced, or whether it was ever sold or distributed beyond the contest. No public hardware or firmware repository was found linked from the project page, so open-source status is left unknown rather than assumed.
