---
title: Defcon 31 SAO ("Defcon Jack")
id: dc31-sao-defcon-jack
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Pierre Cauchois
summary: A self-contained, MCU-free SAO for the DEF CON 31 badge that lights a color-changing LED through a friction-fit, glow-in-the-dark 3D-printed "shard" accessory.
functions: Press the micro-switch to turn the color-changing LED on and off; the light diffuses through the glow-in-the-dark 3D-printed shard and its interchangeable "Defcon Jack" accessory.
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: none
  leds:
    count: 1
    type: color-changing
    note: No current-limiting resistor required.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '30'
  availability: sold_out
  distribution:
  - free_drop
  where: Hand-built and given away at DEF CON 31 to attendees showing off "cool things"; no longer in production.
make_your_own:
  open_source: true
  hardware_url: https://github.com/pierreca/defcon31_sao
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/pierreca/defcon31_sao
  url: https://github.com/pierreca/defcon31_sao
  kind: repo
- label: pierreca.github.io/projects/defcon_31_sao
  url: https://pierreca.github.io/projects/defcon_31_sao/
  kind: website
- label: www.thingiverse.com/thing:6060558
  url: https://www.thingiverse.com/thing:6060558
  kind: website
images:
- file: assets/images/badges/dc31/sao-defcon-jack/d3c3a03a44.jpg
  source: https://pierreca.github.io/projects/defcon_31_sao/
  credit: Pierre Cauchois
  caption: SAO with the LED shining through the shard
- file: assets/images/badges/dc31/sao-defcon-jack/47d94beb35.jpg
  source: https://pierreca.github.io/projects/defcon_31_sao/
  credit: Pierre Cauchois
  caption: Shard with the glow-in-the-dark Defcon Jack accessory attached
contact: {}
notes:
- Battery-powered, MCU-free SAO with a color-changing LED and glow-in-the-dark 3D-printed "Defcon Jack" accessory friction-fit into the DC31 badge chamber; 30 units hand-built. Found by the event-year sweep, task dc31-saos.
- The maker's own project page and README use no fixed capitalized title; "Defcon 31 SAO" / "SAO for the Defcon 31 Badge" both appear in the sweep's sources, so the sheet's title was kept as written.
status: listed
sources:
- kind: url
  url: https://github.com/pierreca/defcon31_sao
  title: Defcon 31 SAO ("Defcon Jack")
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc31-saos); event read as ''dc31''.'
- kind: url
  url: https://pierreca.github.io/projects/defcon_31_sao/
  title: Defcon 31 SAO project page
  accessed: '2026-09-08'
  note: Maker's own write-up; confirmed function, MCU-free design, CR2032 battery, color-changing LED, 30 units hand-built and given away, open-source KiCad/3D files, and photos.
- kind: url
  url: https://github.com/pierreca/defcon31_sao
  title: pierreca/defcon31_sao README
  accessed: '2026-09-08'
  note: Confirmed repo contains KiCad project and 3D-printable (Shapr3d-exported) files; PCB fabbed via OSH Park; no license stated.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (maker, event, function, MCU-free/CR2032/color-changing LED, 30 units, open-source files) confirmed on the maker's own project page and repo. Price is unknown -- it was a free giveaway, not sold, so get_one.price was left blank. No license file found in the repo, so make_your_own.open_source is set to yes (files are published) but license is left null. Thingiverse link (thing:6060558) was not separately fetched; it appears to host the 3D-printable files referenced by the project page.
last_modified_date: '2026-09-10'
model:
  file: assets/models/dc31/sao-defcon-jack.glb
  method: kicad
  source_file: pcb/defcon31_sao.kicad_pcb
  generated: '2026-09-10'
  bytes: 21104
---

Pierre Cauchois built this SAO for DEF CON 31 (2023) as a small, deliberately MCU-free electronic keepsake. A single color-changing LED, wired without a current-limiting resistor, is powered by a CR2032 coin cell and switched on with a micro-switch. The light shines through a friction-fit 3D-printed "shard" that slots into the DC31 badge's accessory chamber, and diffuses further through a glow-in-the-dark 3D-printed "Defcon Jack" piece that attaches to the shard's front.

Cauchois hand-built 30 units and gave them away at the conference to attendees who showed him "cool things," rather than selling them; none are in production now. He published the hardware as open source: a simple KiCad PCB project (fabbed through OSH Park) and Shapr3d-exported 3D-print files for the shard and accessory, available on GitHub and mirrored on Thingiverse.

## Make your own

The GitHub repo (github.com/pierreca/defcon31_sao) holds the KiCad project for the PCB and the 3D-printable files for the shard and Defcon Jack accessory; the project page walks through the build in photos, including the shard's design iterations and the finished assembly friction-fit into a badge chamber.
