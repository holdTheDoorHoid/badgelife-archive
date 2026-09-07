---
title: BornHack 2016 badge
id: bornhack-2016-bornhack-2016-badge
layout: badge
parent: Bornhack 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2016
year: 2016
makers:
- name: BornHack
  url: https://github.com/bornhack
summary: 'A solder-it-yourself kit badge for BornHack 2016 (Denmark''s ''Initial Commit'' hacker camp): a Joule Thief circuit that lights a white LED from a single AA battery, doubling as a name tag and small flashlight.'
functions: Lights a white LED as a flashlight/name tag; the PCB includes an open prototyping area for hacking on additional components.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: single white 5mm LED, hackable with alternative colors
  display: none
  connectivity: []
  battery: 1x AA (Joule Thief circuit); can alternatively use a 3.7V 14500 Li-Ion cell
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as a solder-it-yourself kit to attendees of BornHack 2016; no price or quantity stated in the repo.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2016
  firmware_url: null
  gerbers_url: null
  eda_tool: KiCad
  license: CC-BY-SA
  fab_url: null
  notes: Schematics and board files (KiCad) are in the repo alongside full assembly instructions.
links:
- label: github.com/bornhack/badge2016
  url: https://github.com/bornhack/badge2016
  kind: repo
images:
- file: assets/images/badges/bornhack-2016/bornhack-2016-badge/b74baf82f5.jpg
  source: https://github.com/bornhack/badge2016
  credit: BornHack
  caption: Kit contents of the BornHack 2016 badge
- file: assets/images/badges/bornhack-2016/bornhack-2016-badge/4083b25ef5.jpg
  source: https://github.com/bornhack/badge2016
  credit: BornHack
  caption: Assembled BornHack 2016 badge lit up as a flashlight
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2016
  title: BornHack 2016 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''bornhack-2016''.'
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2016/master/README.md
  title: bornhack/badge2016 README
  accessed: '2026-09-07'
  note: Confirmed description, parts list (transistor, LED, resistor, battery clips, switch, ferrite toroid), Joule Thief circuit, CC-BY-SA license, and KiCad design files.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: No price, quantity made, or sales/distribution channel is stated anywhere in the repo — this reads as a badge given to registered attendees rather than sold, but that isn't stated explicitly either, so availability and get_one.where are left partly unconfirmed.
last_modified_date: '2026-09-07'
model:
  file: assets/models/bornhack-2016/bornhack-2016-badge.glb
  method: kicad
  source_file: pcb/Badge_init.kicad_pcb
  generated: '2026-09-07'
  bytes: 171672
---

The BornHack 2016 badge was the badge for BornHack's first event, held in Denmark and described by the organizers as the "Initial Commit" of the annual outdoor hacker camp. Rather than a microcontroller board, it is a deliberately simple learn-to-solder kit: a Joule Thief circuit that steps up a single AA battery to light a white 5mm LED, functioning as both a name tag and a small flashlight. Assembly requires only 18 solder joints, and the PCB leaves an open prototyping area for attendees to add their own components — a design explicitly inspired by the minimal badge from the Hackaday Superconference, which was meant to encourage badge-hacking rather than discourage it.

The hardware is fully open source: schematics and board files were designed in KiCad and published in the badge's GitHub repository under a CC-BY-SA license, alongside a full illustrated assembly guide covering the resistor, switch, transistor, battery clips, hand-wound ferrite coil, and LED.

## Make your own

The repository (github.com/bornhack/badge2016) contains the KiCad schematic and board files plus a parts list: PCB, BC547B transistor, white 5mm LED, 1K resistor, two AA battery clips, an SPDT switch, and a 900nH ferrite toroid for the hand-wound Joule Thief coil, plus two 30cm lengths of wire.
