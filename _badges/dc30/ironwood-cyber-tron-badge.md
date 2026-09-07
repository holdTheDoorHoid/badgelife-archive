---
title: Ironwood Cyber Tron Badge
id: dc30-ironwood-cyber-tron-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
redirect_from:
- /badges/dc30/iwc/
type: badge
event: dc30
year: 2022
makers:
- name: Ironwood Cyber Team
  url: https://github.com/Ironwood-Cyber
- name: kimboslice
  role: PCB
- name: notthatguy
  role: PCB, embedded software
- name: joehacksalot
  role: PCB, embedded software
- name: Shiloh
  role: companion web app
- name: LeetPanda
  role: website
- name: Spaghetti Code
  role: website
summary: Ironwood Cyber Team's Tron-themed badge for DEF CON 30, a two-board LED-ring design with a touch interface and a companion web app.
functions: 'Lights 70 addressable LEDs arranged in two concentric rings (inner and outer); the front board is a capacitive touch interface for the rear board''s electronics.'
look:
  colors: []
  shape: circle
  themes:
  - tron
  - sci-fi
tech:
  mcu: ESP-series (exact part not stated)
  leds:
    count: 70
    type: RGB
    note: Two concentric rings (inner and outer), diffused through 3D-printed material between the two boards.
  display: null
  connectivity: []
  battery: LiPo, rechargeable
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
  hardware_url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  firmware_url: null
  eda_tool: KiCad
links:
- label: Schematics repo (Ironwood-Cyber/dc30-badge-hw)
  url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  kind: repo
images: []
contact: {}
notes:
- The GitHub repo's own README and GitHub description say the schematics are "Defcon 29 Kicad Schematics", while the badge.life page filed this as the DC30 (2022) Tron badge. The hardware may have originated for DC29 and been carried forward/reused for DC30; sources disagree and neither confirms which con the physical badge was actually distributed at.
status: listed
sources:
- kind: sheet
  event: dc30
  row: 38
  updated: '2022-07-22'
- kind: url
  url: https://badge.life/badges/dc30/iwc/
  title: Original badge.life archive page
  accessed: '2026-09-06'
  note: Migrated from the badge.life Badge Archive; the original page is preserved as the entry body. Lists the maker/dev team and the seven original photo filenames (tron1-tron7.jpg), none of which resolve any longer.
- kind: url
  url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  title: 'Ironwood-Cyber/dc30-badge-hw: Tron badge hardware schematics'
  accessed: '2026-09-06'
  note: 'README describes the badge: two PCBs joined by 3D-printed diffusion material, a touch-input front board, 70 addressable LEDs in two rings, rechargeable LiPo circuit, and USB reprogramming via esp-idf/UART. Repo description says "Defcon 29 Kicad Schematics".'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'No price, quantity, availability, exact MCU part number, or firmware/web-app repo could be found; the "Source Repo" link on the original badge.life page was itself a TODO placeholder and no public firmware or companion-web-app repo exists under the Ironwood-Cyber GitHub org. The seven original badge photos (tron1-tron7.jpg) referenced by the badge.life page 404 and could not be saved. This entry duplicates dc30-tron-badge (same event, same maker "Ironwood Cyber"), which was imported separately from the community sheet with a Reddit/Twitter-raffle distribution note; the two were not merged per instructions.'
last_modified_date: '2026-09-06'
---
## Developers

### Pcb devs:
- kimboslice
- notthatguy
- joehacksalot

### Embedded Software devs:
- notthatguy
- joehacksalot

### Companion Web App dev: 
- Shiloh

### Website devs:
- LeetPanda
- Spaghetti Code  

## Project Links
- [Schematics Repo](https://github.com/Ironwood-Cyber/dc30-badge-hw)
- [Source Repo](TODO)

## Badge images

The original badge.life page referenced seven photos (tron1–tron7.jpg) that were never committed to its repository, so they are not reproduced here.

The Ironwood Cyber Team built this Tron-themed badge for DEF CON 30 (2022) as a two-PCB assembly: a front board that provides a capacitive-touch interface, and a rear board carrying all the electronics, joined by 3D-printed diffusion material that spreads the light from 70 addressable LEDs arranged in two concentric rings. It runs on an ESP-series microcontroller with a rechargeable LiPo battery and can be reprogrammed over USB using esp-idf and USB UART. The team split the work across PCB design (kimboslice, notthatguy, joehacksalot), embedded firmware (notthatguy, joehacksalot), a companion web app (Shiloh), and the project's website (LeetPanda, Spaghetti Code).

The hardware schematics (KiCad) are published on GitHub, though the repository's own description labels them "Defcon 29 Kicad Schematics" even though the badge.life archive filed the badge under DC30 — it's unclear from available sources whether the design was originally made for DC29 and reused, or the repo description is simply outdated. No firmware repository, companion web app source, price, production quantity, or availability information was published, and the badge's original photos are no longer reachable.

## Make your own

Hardware schematics (KiCad) are available in the [dc30-badge-hw repository](https://github.com/Ironwood-Cyber/dc30-badge-hw), which documents the two-board LED-ring design and its LiPo/USB circuitry. No firmware source, bill of materials, or Gerber files have been published alongside it.
