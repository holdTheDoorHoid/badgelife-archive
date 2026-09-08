---
title: Kernelcon 2024 [a]nalyze [i]nternet Badge
id: kernelcon-2024-kernelcon-2024-a-nalyze-i-nternet-badge
layout: badge
parent: Kernelcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: kernelcon-2024
year: 2024
makers:
- name: zonksec (Tyler Rosonke)
  url: https://2024.badge.kernelcon.org/about.html
- name: Cyber City Circuits
  role: assembly
summary: An analog, microcontroller-free LAN cable tester badge for Kernelcon 2024, using a 555 timer and 4017 decade counter with a diode network to test each conductor of an RJ45 cable in turn.
functions: 'Tests a LAN (Ethernet) cable one conductor at a time: a 555 timer astable oscillator clocks a 4017 decade counter that pulls each RJ45 pin high in sequence, while a diode network lets every other line serve as a ground-return path. Head-side LEDs show which line is under test; LEDs on a detachable remote end show where the signal arrived, revealing miswiring or continuity faults. An activities-page mod shows how to make the remote end reattachable.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - measurement
  - security
tech:
  mcu: none
  leds: discrete
  display: none
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
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'Full schematic published as PNG and PDF on the official badge site (no Gerbers/EDA source files found).'
links:
- label: badge.gallery/badges/kernelcon-2024-analyze-internet-badge
  url: https://badge.gallery/badges/kernelcon-2024-analyze-internet-badge
  kind: website
- label: 2024.badge.kernelcon.org
  url: https://2024.badge.kernelcon.org/
  kind: website
- label: About the badge (design writeup)
  url: https://2024.badge.kernelcon.org/about.html
  kind: doc
- label: Badge schematic (PDF)
  url: https://2024.badge.kernelcon.org/badge_schematic.pdf
  kind: doc
- label: Interactive BOM
  url: https://2024.badge.kernelcon.org/ibom.html
  kind: doc
- label: Cable-testing activity instructions
  url: https://2024.badge.kernelcon.org/activities.html
  kind: doc
images:
  - file: assets/images/badges/kernelcon-2024/kernelcon-2024-a-nalyze-i-nternet-badge/89afd837b6.png
    source: "https://2024.badge.kernelcon.org/"
    credit: "zonksec (Tyler Rosonke) / Kernelcon 2024"
    caption: "The [a]nalyze [i]nternet Kernelcon 2024 badge, an analog LAN cable tester"
contact: {}
notes:
- Analog 555/4017-timer based LAN cable tester conference badge for Kernelcon 2024, deliberately kept firmware-free. Found by the event-year sweep, task con-kernelcon.
- 'Sweep title used "analyze internet"; the maker''s own site and badge.gallery both style it "[a]nalyze [i]nternet badge" — kept as the title.'
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/kernelcon-2024-analyze-internet-badge
  title: Kernelcon 2024 [a]nalyze [i]nternet Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kernelcon); event read as ''Kernelcon 2024''.'
- kind: url
  url: https://2024.badge.kernelcon.org/
  title: '[a]nalyze [i]nternet badge | kernelcon 2024 badge'
  accessed: '2026-09-08'
  note: 'Official badge site home page; confirms name, "no microcontrollers" LAN cable tester, badge.png image, and maker credit "built by zonksec".'
- kind: url
  url: https://2024.badge.kernelcon.org/about.html
  title: About The Badge
  accessed: '2026-09-08'
  note: 'Design writeup: 555 timer + 4017 decade counter, diode network, head/remote LED banks, designer zonksec (Tyler Rosonke), assembly by Cyber City Circuits (Augusta, GA), and schematic PDF/PNG links.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (design, maker, assembler, mechanism) confirmed on the maker''s own badge site. Price, quantity made, and distribution/availability were not stated anywhere found and are left blank. No Gerbers or EDA project files were found, only the schematic PDF/PNG, so make_your_own.open_source is set to partial rather than yes.'
last_modified_date: '2026-09-08'
---

The [a]nalyze [i]nternet badge was Kernelcon 2024's attendee badge, designed and prototyped by zonksec (Tyler Rosonke) and assembled by Cyber City Circuits in Augusta, GA. Continuing the con's prior year's approach, it deliberately has no microcontroller: a 555 timer in astable configuration produces a roughly 1 Hz clock that drives a 4017 decade counter, which pulls each pin of an RJ45 jack high in turn to test one conductor of a LAN cable at a time.

A network of diodes lets every untested line double as a ground-return path, so the detachable remote end can be as simple as a plug that shorts all eight lines together. LEDs on the badge's head show which line is currently under test, while LEDs on the remote show where that signal actually arrived, letting a user spot broken conductors or crossed pairs on a cable. The badge site's activities page includes instructions for modifying the remote so it can be repeatedly reattached rather than snapped off once.

## Make your own

The maker published a full schematic as both a PNG and a PDF on the official badge site, along with an interactive bill of materials. No Gerbers, board files, or firmware are needed since the design is purely analog, but no EDA source project was found, so build-from-scratch would mean re-laying-out the board from the schematic.
