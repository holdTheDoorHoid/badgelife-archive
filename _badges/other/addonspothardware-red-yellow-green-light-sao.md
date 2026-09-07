---
title: AddOnSpot — red/yellow/green light SAO
id: other-addonspothardware-red-yellow-green-light-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: straithe
  url: https://github.com/straithe
summary: 'A shitty add-on (SAO) with a red/yellow/green LED that lets the wearer signal their social availability at an event.'
functions: 'Two toggle switches control a red LED and a green LED independently; turning both on mixes them to yellow. The board can alternatively be driven from the host badge over two GPIO pins (with resistors populated) instead of the switches.'
look:
  colors:
  - red
  - yellow
  - green
  shape: null
  themes:
  - minimalist
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 'One red and one green LED; switched on together they read as yellow. No microcontroller — pure switch/resistor logic, with optional GPIO control from the host badge.'
  display: null
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
  open_source: yes
  hardware_url: https://github.com/straithe/AddOnSpotHardware
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/straithe/AddOnSpotHardware
  url: https://github.com/straithe/AddOnSpotHardware
  kind: repo
images: []
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://github.com/straithe/AddOnSpotHardware
  title: AddOnSpotHardware — red/yellow/green light SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/straithe/AddOnSpotHardware
  title: 'straithe/AddOnSpotHardware: README and KiCad design files'
  accessed: '2026-09-07'
  note: 'README describes the SAO''s purpose and controls; repo contains KiCad schematic/PCB/library files under BSD-3-Clause but no board photos, event mention, price, or quantity information.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Verified against the live repo (README, file listing, license) and all cited facts (LED/switch/GPIO behavior, credited inspiration, KiCad/BSD-3-Clause, no photos or event/price/quantity info) hold up. Corrected status from the researcher''s "released" to "unknown": the repo is design files only with no board photos, storefront, or any account of the SAO being fabricated or worn, so "released" (per the guide''s "people have it") is not supported by any source read — only that the open-source design itself is complete and public. The idea is credited in the README to a tweet by k8em0 and a color-changing-tiara project by elkentaro, but nothing ties this specific SAO to a con, so event/year remain unset. No further web search was possible this session (search budget exhausted) beyond the repo fetch.'
last_modified_date: '2026-09-07'
---

AddOnSpot is an open-source "shitty add-on" (SAO) by GitHub user straithe: a small add-on board with a red LED and a green LED that the wearer can mix to signal their social boundaries at an event — red for "don't approach," green for "come say hi," and both together (reading as yellow) for "only people I know." The idea is credited to a tweet by k8em0 and to elkentaro's earlier color-changing-tiara project.

The board has no microcontroller. Two switches with extended actuators (chosen to be easier to operate for people with long fingernails) drive the red and green LEDs directly. As an alternative to the switches, the host badge can drive the LEDs itself over two GPIO pins, provided the optional series resistors are populated — they're left unpopulated by default so that a badge's pulled-up GPIO pins don't leave the LEDs permanently dim-lit.

The GitHub repository (BSD-3-Clause) contains the full KiCad schematic, PCB layout, project file, and symbol library, but no photos of an assembled board, no storefront listing, and no mention of which convention or year it was built for, so those fields are left empty rather than guessed.
