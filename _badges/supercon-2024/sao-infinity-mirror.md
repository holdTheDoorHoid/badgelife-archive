---
title: SAO Infinity Mirror
id: supercon-2024-sao-infinity-mirror
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Scorch Works
  url: https://hackaday.io/hacker/45858-scorch-works
summary: A miniature infinity-mirror SAO for the Supercon 8 SAO Contest, built from a PCB with 18 white LEDs and a single resistor, two laser-cut two-way-mirror acrylic panels, and a 3D-printed Voronoi-vented bezel, powered directly over the SAO connector with spare GPIO traces left for optional PWM dimming.
functions: Lights 18 small white LEDs behind two two-way-mirror acrylic panels to create an infinity-mirror illusion. No microcontroller onboard; the maker notes unused traces and through-holes on the board for future additions such as a potentiometer dimmer or PWM control from the host badge.
look:
  colors:
  - white
  shape: null
  themes:
  - minimalist
tech:
  mcu: none
  leds:
    count: 18
    type: discrete
    note: 2x3x4mm square clear-package white LEDs, DC 3V / 20mA rated, run off a single resistor.
  display: none
  connectivity: []
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
  open_source: true
  hardware_url: https://hackaday.io/project/198943/files
  firmware_url: null
  gerbers_url: https://hackaday.io/project/198943/files
  eda_tool: KiCad
  notes: 'Files posted on Hackaday.io: KiCad schematic/board, PCB Gerbers, an STL for the 3D-printed Voronoi-vent bezel, an OpenSCAD source for the bezel, and a DXF for laser-cutting the two-way-mirror acrylic panels. No BOM or explicit license was stated on the page.'
links:
- label: hackaday.io/project/198943-sao-infinity-mirror
  url: https://hackaday.io/project/198943-sao-infinity-mirror
  kind: hackaday
  archived: https://web.archive.org/web/20251017173216/https://hackaday.io/project/198943-sao-infinity-mirror
- label: hackaday.io/project/198943/gallery
  url: https://hackaday.io/project/198943/gallery
  kind: hackaday
  archived: https://web.archive.org/web/20251023165315/https://hackaday.io/project/198943/gallery
- label: hackaday.io/project/198943/files
  url: https://hackaday.io/project/198943/files
  kind: hackaday
  archived: https://web.archive.org/web/20251214204445/https://hackaday.io/project/198943/files
images:
- file: assets/images/badges/supercon-2024/sao-infinity-mirror/67db588619.jpg
  source: https://hackaday.io/project/198943/gallery
  credit: Scorch Works
  caption: SAO Infinity Mirror lit up, showing the infinity mirror effect
  archived: https://web.archive.org/web/20251023165315/https://hackaday.io/project/198943/gallery
- file: assets/images/badges/supercon-2024/sao-infinity-mirror/dbf8b3c31a.jpg
  source: https://hackaday.io/project/198943/gallery
  credit: Scorch Works
  caption: SAO Infinity Mirror PCB and components before assembly
  archived: https://web.archive.org/web/20251023165315/https://hackaday.io/project/198943/gallery
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198943-sao-infinity-mirror
  title: SAO Infinity Mirror
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20251017173216/https://hackaday.io/project/198943-sao-infinity-mirror
- kind: url
  url: https://hackaday.io/project/198943-sao-infinity-mirror
  title: SAO Infinity Mirror (project page)
  accessed: '2026-09-07'
  note: Confirmed maker (Scorch Works), event/context (Supercon 8 SAO Contest, 2024), construction (PCB + two-way-mirror acrylic + 3D-printed bezel), and LED spec (18x white, 2x3x4mm, 3V/20mA).
  archived: https://web.archive.org/web/20251017173216/https://hackaday.io/project/198943-sao-infinity-mirror
- kind: url
  url: https://hackaday.io/project/198943/files
  title: SAO Infinity Mirror - Files
  accessed: '2026-09-07'
  note: 'Lists design files: KiCad schematic/board, Gerbers, bezel STL and SCAD source, mirror-cutting DXF.'
  archived: https://web.archive.org/web/20251214204445/https://hackaday.io/project/198943/files
- kind: url
  url: https://hackaday.io/project/198943/gallery
  title: SAO Infinity Mirror - Gallery
  accessed: '2026-09-07'
  note: Source of the two photos saved to this entry.
  archived: https://web.archive.org/web/20251023165315/https://hackaday.io/project/198943/gallery
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker is Scorch Works (Hackaday.io handle), and the project page confirms it was built for the Supercon 8 (2024) SAO Contest, matching the existing event assignment. Price, quantity made, and availability were not stated anywhere on the project page and are left empty. No explicit open-source license was named, though hardware design files are freely posted, so open_source is set to yes on that basis. Could not reach the maker's Hackaday.io profile page directly (redirected to a login wall) for further biographical context.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2024/sao-infinity-mirror.glb
  method: kicad
  source_file: KICAD_SOA_Infinity_mirror_2024_10-23_unz/KICAD_SOA_Infinity_mirror_2024_10-23/SAO_infinity_mirror_2024-10-21.kicad_pcb
  generated: '2026-09-10'
  bytes: 95256
---

The SAO Infinity Mirror is a Supercon Add-On built by Scorch Works for the Hackaday Supercon 8 (2024) SAO Contest. It has no microcontroller of its own: a small PCB carries 18 white LEDs (2x3x4mm clear-package parts, 3V/20mA) driven through a single resistor, plugged straight into the host badge's SAO connector for power. The light from those LEDs bounces between two laser-cut, two-way-mirror acrylic panels to produce the classic infinity-mirror effect of receding reflections, all housed inside a 3D-printed bezel with a decorative Voronoi vent pattern.

The maker left room for expansion, noting unused PCB traces and through-holes that a builder could use to add a potentiometer dimmer or wire in PWM brightness control from the host badge's GPIO.

## Make your own

Design files are posted on the project's Hackaday.io page: a KiCad schematic and board file, ready-to-fab PCB Gerbers, an STL of the Voronoi-vented bezel with its OpenSCAD source for customization, and a DXF cutting file for the two-way-mirror acrylic panels. No bill of materials or explicit license was published alongside the files.
