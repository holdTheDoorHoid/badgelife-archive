---
title: DC32 Crest Badge
id: dc32-crest-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Ironwood Cyber
  url: https://www.ironwoodcyber.com/
summary: A two-board electronic badge (an ESP32-based "rear board" plus a "front
  board") built for Ironwood Cyber's DEF CON 32 "Crest Badge" CTF prize; this
  repository holds its PCB, mechanical CAD and firmware source.
functions: 'Firmware is an ESP-IDF ("2024-badge-app") project with a 2nd-stage
  bootloader and a flashable application, built to run on the front/rear board
  stack.'
look:
  colors: []
  shape: null
  themes:
  - fantasy
  - pop culture
  - ctf
tech:
  mcu: ESP32-WROVER-E
  leds: null
  display: null
  connectivity:
  - wifi
  - ble
  battery: null
  sao_version: null
get_one:
  price: free (contest prize)
  price_usd: 0.0
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/badgelife/dc32-crest-badge
  firmware_url: https://github.com/badgelife/dc32-crest-badge/tree/main/firmware
  eda_tool: KiCad
links:
- label: github.com/badgelife/dc32-crest-badge
  url: https://github.com/badgelife/dc32-crest-badge
  kind: repo
- label: 'PCBWay: DC32 Crest Badge Front Board Prototype'
  url: https://www.pcbway.com/project/share/DC32_Crest_Badge_Front_Board_Prototype_53a9e1d2.html
  kind: fab
- label: 'YouTube (The Cyber Distortion Podcast): Introducing the Ironwood Cyber
    DC32 "Crest Badge"'
  url: https://www.youtube.com/watch?v=8ILt5zcA9lQ
  kind: video
images:
- file: assets/images/badges/dc32/crest-badge/81ae305d23.jpg
  source: "https://www.pcbway.com/project/share/DC32_Crest_Badge_Front_Board_Prototype_53a9e1d2.html"
  credit: "Jose Rodriguez / PCBWay"
  caption: "Assembled two-board badge stack with ESP32-WROVER module and U.FL antenna, next to the main board's underside"
- file: assets/images/badges/dc32/crest-badge/45b383e4ff.jpg
  source: "https://www.pcbway.com/project/share/DC32_Crest_Badge_Front_Board_Prototype_53a9e1d2.html"
  credit: "Jose Rodriguez / PCBWay"
  caption: "Main board detail showing USB-C port, battery header, and the Ironwood Cyber tree logo silkscreen"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- 'This appears to be the same badge as dc32-badge-with-unreleased-name-as-of-yet
  (Ironwood Cyber''s "Crest Badge", a DEF CON 32 CTF prize shaped like Zelda''s
  Hylian Crest). That entry was researched from the maker''s own DC32 page and
  third-party coverage and found no public hardware/firmware repo; this repo
  was found separately and is not explicitly branded to Ironwood Cyber, but
  several details line up closely - the repo''s only mechanical CAD file is
  "Triforce.f3d", its PCB prototypes folder has "triforce_sao" and "link_sao"
  subfolders (Zelda''s Triforce and the character Link), its two boards are
  named "front-board" and "rear-board" (matching the PCBWay share titled "DC32
  Crest Badge Front Board Prototype"), and its ESP32-WROVER-E MCU supports the
  wifi/BLE connectivity the other entry''s maker page describes. Treat this as
  a likely duplicate of that entry rather than a confirmed one.'
status: listed
sources:
- kind: url
  url: https://github.com/badgelife/dc32-crest-badge
  title: DC32 Crest Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc32''.'
- kind: url
  url: https://github.com/badgelife/dc32-crest-badge/tree/main/pcb
  title: badgelife/dc32-crest-badge - pcb directory
  accessed: '2026-09-07'
  note: Two boards (front-board, rear-board) built around an ESP32-WROVER-E
    module, KiCad library format (.lib/.pretty); prototypes folder includes
    triforce_sao and link_sao subfolders.
- kind: url
  url: https://github.com/badgelife/dc32-crest-badge/tree/main/cad
  title: badgelife/dc32-crest-badge - cad directory
  accessed: '2026-09-07'
  note: Only mechanical CAD file present is Triforce.f3d.
- kind: url
  url: https://raw.githubusercontent.com/badgelife/dc32-crest-badge/main/firmware/README.md
  title: firmware/README.md
  accessed: '2026-09-07'
  note: 'ESP-IDF project named "2024-badge-app": 2nd-stage bootloader plus
    application, flashed with idf.py; no branding or feature description
    beyond build/flash instructions.'
- kind: url
  url: https://www.pcbway.com/project/share/DC32_Crest_Badge_Front_Board_Prototype_53a9e1d2.html
  title: DC32 Crest Badge Front Board Prototype - PCBWay
  accessed: '2026-09-07'
  note: Shared by Jose Rodriguez, June 2024; provided the two saved photos of
    the assembled front/rear board stack.
- kind: url
  url: https://www.youtube.com/watch?v=8ILt5zcA9lQ
  title: 'SPECIAL RELEASE: Introducing the Ironwood Cyber DC32 "Crest Badge"'
  accessed: '2026-09-07'
  note: Third-party channel video title/description found via search; confirms
    the "Crest Badge" name is Ironwood Cyber's, tied to a CTF where the first
    20 finishers won the badge (not independently re-verified here beyond the
    search snippet).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No page found states outright that this GitHub repo is Ironwood
    Cyber's; the link is inferred from the Zelda-themed folder/file names
    (Triforce, Link) and the front/rear board split matching the PCBWay
    listing, cross-checked against research already on file for
    dc32-badge-with-unreleased-name-as-of-yet. quantity, availability,
    LED and battery details were left blank here since this repo and the
    PCBWay page do not state them; see the other entry for what the maker's
    own page and third-party coverage say about the CTF/prize mechanics,
    look, and touch controls.
last_modified_date: '2026-09-07'
---

This repository holds the hardware and firmware for what looks like the same
badge documented at `dc32-badge-with-unreleased-name-as-of-yet`: Ironwood
Cyber's "Crest Badge," given out to the first 20 finishers of a Capture the
Flag challenge at DEF CON 32. The repo itself carries no Ironwood Cyber
branding, but its contents point the same direction — a KiCad-designed
two-board stack (a "front-board" and "rear-board") built around an
ESP32-WROVER-E module, a single mechanical CAD file named "Triforce.f3d," and
PCB prototype folders named "triforce_sao" and "link_sao," all Legend of
Zelda references that match the other entry's description of a badge shaped
like Hyrule's crest.

Firmware is an ESP-IDF project titled "2024-badge-app," with a second-stage
bootloader and a flashable application built and monitored with `idf.py`; its
README has no feature description beyond build and flash commands, so it adds
no detail about the badge's controls or game beyond what the maker's own page
already provided in the other entry.

Two photos from a PCBWay fabrication share (posted by Jose Rodriguez, June
2024) show the assembled electronics: a rectangular board with a USB-C port,
a battery header, an antenna connector, an ESP32-WROVER-E module, and a
"tree" logo etched into the silkscreen, stacked on brass standoffs above a
second board. No price, quantity or availability information is published
here beyond what is already recorded on the other entry.
