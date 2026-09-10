---
title: BSides Prague 2025 Badge
id: bsides-cz-2025-bsides-badge-2025-bsides-cz-2025
layout: badge
parent: BSides Cz 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cz-2025
year: 2025
makers:
- name: BSides Czech z.s.
  url: https://github.com/bsidescz
summary: A three-part electronic badge for BSides Prague 2025 (organized by BSides Czech z.s.), made of a CH32V003-based mainboard, small CH32V003 "key" add-on modules with an RGB LED and button, and a head unit built around a commercial round-display ESP32-C3 module.
functions: 'Modular design: small "key" boards (RISC-V CH32V003, WS2812B LED, tactile button) plug into edge connectors on a CH32V003 mainboard, which also carries a piezo buzzer; a separate head unit adds a 1.28-inch round LCD driven by an ESP32-C3. Exact on-badge behavior (games, challenges) is not documented in the repo.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: CH32V003 (mainboard and key modules); ESP32-C3 (head/display module, via a commercial 1.28" round-LCD board)
  leds:
    count: null
    type: WS2812B
    note: One WS2812B per "key" module (from the KiCad footprint/schematic); not confirmed on the mainboard or head unit.
  display: 1.28" round LCD (commercial ESP32-2424S012 module in the head unit)
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
  hardware_url: https://github.com/bsidescz/badge-2025
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bsidescz/badge-2025
  url: https://github.com/bsidescz/badge-2025
  kind: repo
- label: github.com/sorooris/bsides-badge-2025 (fork)
  url: https://github.com/sorooris/bsides-badge-2025
  kind: repo
- label: BSides Czech z.s. (GitHub org)
  url: https://github.com/bsidescz
  kind: website
images: []
contact: {}
notes:
- ESP32-based BSides Czech Republic 2025 badge with a 1.28-inch round display. Found by the event-year sweep, task bsides-any.
- 'Sweep imported the fork (sorooris/bsides-badge-2025) as the title; the maker''s own repo is bsidescz/badge-2025, described only as "Repo containing all the badge bits and pieces" (no proper name given), so this entry uses a descriptive title.'
status: listed
sources:
- kind: url
  url: https://github.com/sorooris/bsides-badge-2025
  title: bsides-badge-2025 (BSides CZ 2025)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides CZ 2025''.'
- kind: url
  url: https://github.com/bsidescz/badge-2025
  title: bsidescz/badge-2025
  accessed: '2026-09-10'
  note: 'Maker''s own repo (sorooris''s repo is a fork of this). Confirms three-folder structure: head, key, mainboard, each with KiCad hardware under HW/.'
- kind: url
  url: https://api.github.com/orgs/bsidescz
  title: bsidescz GitHub org profile
  accessed: '2026-09-10'
  note: 'Org description: "BSides Czech z.s. — Non-profit organizing community conference BSidesPrague". Confirms bsides-cz-2025 (BSides Prague 2025) is the correct event; no separate BSides Prague event id exists in events.yml.'
- kind: url
  url: https://raw.githubusercontent.com/bsidescz/badge-2025/main/mainboard/HW/kicad/bsides25-badge-mainboard-v1.1.kicad_sch
  title: mainboard schematic (KiCad source)
  accessed: '2026-09-10'
  note: 'lib_id references confirm MCU_WCH_CH32V0:CH32V003FxPx, AMS1117-3.3 regulator, MLT-5030 buzzer, MMBT3906 transistor on the mainboard.'
- kind: url
  url: https://raw.githubusercontent.com/bsidescz/badge-2025/main/key/HW/kicad/bsides25-key.kicad_sch
  title: key module schematic (KiCad source)
  accessed: '2026-09-10'
  note: 'lib_id references confirm CH32V003, a WS2812B-2020 LED, and an SKRHABE010 SMD tactile switch on each key module, connecting via an "EDGE_BADGE" edge connector.'
- kind: url
  url: https://api.github.com/repos/bsidescz/badge-2025/git/trees/main?recursive=1
  title: repo file tree (GitHub API)
  accessed: '2026-09-10'
  note: 'head/HW/ contains only the vendor SDK/demo tree for a commercial "1.28inch_ESP32-2424S012" round-display module (ESP32-C3-MINI-1U), confirming the head unit''s chip and display; no separate custom firmware source was found for mainboard or key.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: "Maker's own GitHub org (BSides Czech z.s., organizer of BSidesPrague) confirms the hardware exists and matches the bsides-cz-2025 event with no correction needed. Confidence is medium rather than high because: the repo has no README beyond a one-line description, no photos of an assembled badge were found anywhere (repo, org, or web search), price/quantity/availability/exact functions are undocumented, and no firmware source (only hardware/KiCad) was found. A third-party aggregator (badge.gallery) describes a BSides Prague 2025 badge as a modular, multi-processor PCB with attendee chips for CTF challenges, which is consistent with this mainboard+key+head structure, but that page is itself a secondary source with no images or primary citations, so it was not used to fill any fields. Left empty: get_one.* (price/quantity/availability/where), tech.connectivity (ESP32-C3 supports wifi/ble but usage on this badge is unconfirmed), tech.battery, look.colors/shape, functions detail beyond hardware structure."
last_modified_date: '2026-09-10'
---

The BSides Prague 2025 badge (BSides Czech z.s.'s repo names it only "badge-2025") is a three-piece electronic badge built around two different microcontroller families. A mainboard carries a CH32V003 RISC-V microcontroller, a piezo buzzer, and edge connectors; small "key" modules — each with their own CH32V003, a WS2812B RGB LED, and a tactile button — plug into those connectors. A separate head unit adds a 1.28-inch round LCD, built on a commercial ESP32-C3 display module (the same "GC9A01-class" round-screen boards sold widely as "1.28inch ESP32-2424S012").

This modular structure lines up with an outside account (badge.gallery) of a BSides Prague 2025 badge as a multi-processor PCB where attendees collect small "chips" toward CTF challenges, though that account could not be independently confirmed from the maker's own materials and was not used to fill in any fields here.

## Make your own

The maker's repo (github.com/bsidescz/badge-2025) publishes KiCad hardware source for all three boards — mainboard, key, and head — under each folder's `HW/` directory, including footprints, 3D models, and (for the key module) an STL for a cover. No firmware source was found in the repository; the head unit's folder contains only the vendor SDK/demo code for the underlying commercial display module, not custom badge firmware.
