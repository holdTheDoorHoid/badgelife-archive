---
title: Flux Capacitor PCB Badge
id: other-flux-capacitor-pcb-badge-2021
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2021
makers:
- name: Arnov Sharma
  url: https://www.pcbway.com/project/member/?bmbno=068786DB-1EF6-44
summary: A wearable PCB badge replicating the Back to the Future flux capacitor, driven by an ATtiny85 chasing 12 LEDs through four 8205S MOSFETs and powered by a CR2032 coin cell or micro-USB, shared on PCBWay by Arnov Sharma in June 2021 under CC BY-SA 3.0 with Gerbers, schematic, Arduino sketch and an STL.
functions: 'LED chaser animation across 12 LEDs, mimicking the film prop''s light sequence.'
look:
  colors: []
  shape: null
  themes:
  - movie
  - retro computer
  - sci-fi
tech:
  mcu: ATtiny85
  leds:
    count: 12
    type: discrete
    note: 0603 package LEDs switched via four 8205S MOSFETs, running a modified Arduino chaser sketch.
  display: null
  connectivity:
  - usb
  battery: CR2032 coin cell or micro-USB
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Design shared publicly on PCBWay; not sold as a product. Files available for anyone to fabricate.'
make_your_own:
  open_source: 'yes'
  hardware_url: https://www.pcbway.com/project/shareproject/Flux_Capacitor_PCB_Badge.html
  firmware_url: https://www.pcbway.com/project/shareproject/Flux_Capacitor_PCB_Badge.html
  eda_tool: null
  license: CC BY-SA 3.0
  fab_url: https://www.pcbway.com/project/shareproject/Flux_Capacitor_PCB_Badge.html
  notes: 'Gerbers, schematic (fluxcapsch.pdf), a modified Arduino chaser sketch, and a 3D-printable enclosure (badge.stl) are all shared on the PCBWay project page. Designed in OrCAD Cadence and Autodesk Fusion 360.'
links:
- label: www.pcbway.com/project/shareproject/Flux_Capacitor_PCB_Badge.html
  url: https://www.pcbway.com/project/shareproject/Flux_Capacitor_PCB_Badge.html
  kind: fab
- label: www.youtube.com/watch?v=efD6QN1S20o
  url: https://www.youtube.com/watch?v=efD6QN1S20o
  kind: video
- label: www.hackster.io/Arnov_Sharma_makes
  url: https://www.hackster.io/Arnov_Sharma_makes
  kind: article
images:
- file: assets/images/badges/other/flux-capacitor-pcb-badge-2021/007c9b23fc.jpg
  source: "https://www.pcbway.com/project/shareproject/Flux_Capacitor_PCB_Badge.html"
  credit: "Arnov Sharma"
  caption: "The assembled Flux Capacitor PCB badge"
- file: assets/images/badges/other/flux-capacitor-pcb-badge-2021/3eddb10514.jpg
  source: "https://www.pcbway.com/project/shareproject/Flux_Capacitor_PCB_Badge.html"
  credit: "Arnov Sharma"
  caption: "The badge with LEDs lit"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://www.pcbway.com/project/shareproject/Flux_Capacitor_PCB_Badge.html
  title: Flux Capacitor PCB Badge - Share Project - PCBWay
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://www.pcbway.com/project/shareproject/Flux_Capacitor_PCB_Badge.html
  title: Flux Capacitor PCB Badge - Share Project - PCBWay
  accessed: '2026-09-07'
  note: Primary source for maker, date, event, chip, LEDs, power, license, and shared files (Gerbers, schematic, Arduino sketch, STL).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Not a conference badge: made by Arnov Sharma as an entry into PCBWay''s 4th PCB Design Contest (Free Theme category), published June 19, 2021, his first PCB badge design. No price, quantity, or storefront listing found — it was shared as an open design, not sold. Could not reach hackster.io/Arnov_Sharma_makes (HTTP 403) to check for a companion write-up. A different, unrelated entry (dc31-flux-capacitor-sao) already covers a Flux Capacitor-themed SAO for DEF CON 31 by a different maker/product type; not a duplicate of this badge.'
last_modified_date: '2026-09-07'
---

Arnov Sharma designed the Flux Capacitor PCB Badge as his first PCB badge project, publishing it on PCBWay on June 19, 2021 as an entry in the platform's 4th PCB Design Contest (Free Theme category). The badge recreates the glowing time-travel device from *Back to the Future*: an ATtiny85 drives a chaser animation across 12 surface-mount LEDs, switched through four 8205S MOSFETs, so the lights sweep back and forth the way the film prop's did. It runs off a CR2032 coin cell or micro-USB power, drawing only a few milliwatts — Sharma's write-up jokes that his replica needs a small fraction of the "1.21 gigawatts" the fictional original required.

The design was released under a CC BY-SA 3.0 license with everything needed to build one: Gerber files, a schematic (fluxcapsch.pdf), the modified Arduino chaser sketch, and an STL for a 3D-printed enclosure. Sharma built the board using OrCAD Cadence for the schematic and Autodesk Fusion 360 for the enclosure, then assembled prototypes by hand with solder paste, pick-and-place, and hotplate reflow. It was not sold as a product; it exists as an open hardware share for anyone to fabricate.
