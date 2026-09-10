---
title: RFID/NFC 2024 minibadge
id: saintcon-2024-rfid-nfc-2024-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: ICEMAN
  role: designer
- name: GOBO42
  role: designer
summary: A passive SAINTCON minibadge for the RFID/NFC Community, powered by the host badge and lit by two SMD LEDs; the design is decorative, with no RFID/NFC chip on board.
functions: Lights up via two LEDs when plugged into a host badge's minibadge header; no active RFID/NFC hardware.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two 1206 SMD LEDs, each with its own series resistor.
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
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/RFID-NFC-2024
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/RFID-NFC-2024
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/RFID-NFC-2024
  kind: repo
- label: SAINTCON MiniBadge Community
  url: https://saintcon.org/minibadges/
  kind: website
images: []
contact: {}
notes:
- 2024 edition of an RFID/NFC minibadge (distinct from the 2021 RFID/NFC BADGE, the 2022/2023 RFID/NFC Community Badges, and the 2023 RFID Rocket already in the archive). Found by the event-year sweep, task saintcon-2024.
- 'The sweep''s original title was "RFID-NFC-2024 minibadge"; retitled to "RFID/NFC 2024 minibadge" to match the slash used elsewhere in this badge family (RFID/NFC BADGE, RFID/NFC Community Badge).'
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/RFID-NFC-2024
  title: RFID-NFC-2024 minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/RFID-NFC-2024/RFID-NFC-2024.kicad_sch
  title: RFID-NFC-2024.kicad_sch
  accessed: '2026-09-10'
  note: 'Schematic: MiniBadge_Simple connector, 2x LED (Device:LED) each with an R_US series resistor, +3.3V/GND rails only. No MCU, no RFID/NFC IC — confirms this is a passive/decorative minibadge, not an active RFID/NFC device.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/RFID-NFC-2024/RFID-NFC-2024.kicad_pcb
  title: RFID-NFC-2024.kicad_pcb
  accessed: '2026-09-10'
  note: 'Silkscreen text reads "RFID/NFC", "RFID/NFC COMMUNITY", "2024", and "ICEMAN & GOBO42" (credited as designers). Footprints: MiniBadge_Simple connector, 2x 1206 LED, 2x 1206 resistor.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: 'utahsaint-org/MiniBadges2024: Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: Repo README confirms this is the official SAINTCON 2024 minibadge collection maintained by the SAINTCON/Utah SAINT org.
- kind: url
  url: https://saintcon.org/minibadges/
  title: MiniBadges - SAINTCON 26
  accessed: '2026-09-10'
  note: General context on the SAINTCON MiniBadge community (led by SHIFTY and distinctm1nd), which runs the minibadge space and yearly designs; did not mention this specific badge by name.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >-
    Confirmed via the official utahsaint-org/MiniBadges2024 GitHub repo, which holds
    real KiCad hardware files (schematic + PCB) for this minibadge, not just a
    sweep snippet. The schematic and PCB silkscreen show it is a simple passive
    design (two LEDs, no MCU or RFID/NFC IC) representing SAINTCON's RFID/NFC
    Community, designed by ICEMAN and GOBO42. Could not find price, quantity made,
    distribution method, or a photo of the assembled badge — no per-badge README
    exists in the repo, and a 38 MB PDF minibadge guide
    (2024-SAINTCON-MiniBadge-Guide-v3.0) that likely covers pricing/distribution
    for all 2024 minibadges was found but not practical to fetch/parse within
    budget. No image of the physical item was found (repo only has vector SVG
    silhouette pieces used for the silkscreen artwork, not photos), so `images`
    is left empty rather than guessed.
last_modified_date: '2026-09-10'
---

The RFID/NFC 2024 minibadge is one of the community minibadges made for SAINTCON 2024, representing the conference's RFID/NFC Community (the group that later became the RF Signal Sanctum community). Despite the name, the board itself carries no RFID or NFC hardware: its schematic shows only the standard SAINTCON minibadge power connector feeding two SMD LEDs through series resistors, so the badge simply lights up when plugged into a host badge's minibadge header. The "RFID/NFC" theming lives entirely in the PCB artwork and silkscreen.

The design is credited on the PCB silkscreen to ICEMAN and GOBO42, and its KiCad source files (schematic, PCB layout, and the SVG artwork used for the board's graphics) are published in the official `utahsaint-org/MiniBadges2024` repository alongside dozens of other 2024 SAINTCON minibadges. No price, production quantity, or distribution details were found for this specific badge, nor a photo of the assembled board.

## Make your own

Hardware files (KiCad schematic and PCB, plus SVG artwork) are published at https://github.com/utahsaint-org/MiniBadges2024/tree/main/RFID-NFC-2024. No firmware is applicable since the board has no MCU.
