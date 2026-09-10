---
title: 35C3 Labitat Indie Badge
id: 35c3-2018-35c3-labitat-indie-badge
layout: badge
parent: 35C3
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: 35c3-2018
year: 2018
makers:
- name: Thomas Flummer
  url: https://github.com/flummer
  role: designer, for Labitat
summary: An unofficial, firmware-free badge built by Danish hackerspace Labitat for 35C3, implementing a discrete SR-latch (flip-flop) one-bit memory circuit behind Congress-themed artwork.
functions: Two push buttons set/reset a one-bit SR-latch memory made of discrete transistors; two orange LEDs show the current state, while 20 reverse-mounted green and blue LEDs backlight the front artwork. No microcontroller or firmware; the "hack" is assembly and understanding the circuit.
look:
  colors:
  - green
  - blue
  - orange
  shape: rectangle
  themes:
  - hardware tool
  - learn to solder
  - ctf
tech:
  mcu: none
  leds:
    count: 22
    type: reverse-mount
    note: Two orange LEDs indicate SR-latch state; ten green and ten blue reverse-mounted LEDs backlight the artwork.
  display: none
  connectivity: []
  battery: 2x AA
  sao_version: v1
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to Labitat-affiliated attendees at 35C3 (Leipzig, Dec 2018); exact channel not documented in the sources found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/flummer/35c3-badge
  firmware_url: null
  gerbers_url: https://github.com/flummer/35c3-badge
  eda_tool: KiCad
  notes: Repository includes KiCad schematic/PCB files, Gerbers, and PDF schematics; no BOM or license file found.
links:
- label: badge.gallery/badges/35c3-labitat-indie-badge
  url: https://badge.gallery/badges/35c3-labitat-indie-badge
  kind: website
- label: flummer/35c3-badge on GitHub
  url: https://github.com/flummer/35c3-badge
  kind: repo
images:
- file: assets/images/badges/35c3-2018/35c3-labitat-indie-badge/6c59de962c.jpg
  source: https://github.com/flummer/35c3-badge
  credit: Thomas Flummer
  caption: Assembled 35C3 Labitat Indie Badge showing SR-latch circuit and LED artwork
contact: {}
notes:
- Unofficial SR-latch PCB conference badge brought to 35C3 by Danish hackerspace Labitat. Found by the event-year sweep, task ccc-adjacent.
- Sweep listed the maker only as "Labitat"; the badge.gallery writeup and the linked GitHub repo credit designer Thomas Flummer (working for/with Labitat) as the individual creator.
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/35c3-labitat-indie-badge
  title: 35C3 Labitat Indie Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:ccc-adjacent); event read as ''35C3 2018''.'
- kind: url
  url: https://badge.gallery/badges/35c3-labitat-indie-badge
  title: 35C3 Labitat Indie Badge
  accessed: '2026-09-08'
  note: 'Confirmed description: discrete SR-latch memory circuit, designer Thomas Flummer, no firmware/MCU, optional power-only SAO connector.'
- kind: url
  url: https://github.com/flummer/35c3-badge
  title: flummer/35c3-badge
  accessed: '2026-09-08'
  note: 'Source repo: KiCad schematics, PCB files, Gerbers, PDF schematics, and a PHOTOS folder; confirms maker and event.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Core facts (maker, function, hardware) confirmed by badge.gallery and the maker's own GitHub repo. Could not find price, quantity made, distribution channel, BOM, or a license for the design files. No independent photo of the badge beyond the one in the repo's PHOTOS folder was found.
last_modified_date: '2026-09-10'
model:
  file: assets/models/35c3-2018/35c3-labitat-indie-badge.glb
  method: kicad
  source_file: 35c3_badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 483760
---

The 35C3 Labitat Indie Badge is an unofficial, hacker-made badge that Danish hackerspace Labitat brought to the 35th Chaos Communication Congress in Leipzig in December 2018, designed by Thomas Flummer. Unlike most badgelife projects of the era, it carries no microcontroller or firmware at all: the badge is a discrete-component SR-latch (flip-flop) circuit built from transistors, resistors, and two push buttons, with two orange LEDs showing which state the latch is holding. The rest of its 22 LEDs — ten green and ten blue, reverse-mounted so their light shines through the board — backlight Congress-themed artwork on the front of the PCB.

Running on two AA batteries and carrying an optional power-only SAO connector, the badge's appeal is in understanding and assembling the circuit itself rather than writing code for it. Flummer published the full KiCad design, PCB layout, Gerbers, and schematic PDFs on GitHub, along with a handful of assembly photos, but no bill of materials or license statement was included with the files.

No information surfaced on how many were made, how they were distributed to attendees, or whether any were sold; the sources found describe the badge as something brought specifically for Labitat's own people at the Congress.

## Make your own

Design files (KiCad schematic and PCB, Gerbers, and PDF schematics) are available at https://github.com/flummer/35c3-badge. No published bill of materials was found alongside them.
