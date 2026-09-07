---
title: DefCon_SecKC_26
id: dc26-defcon-seckc-26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: BadgePirates / SecKC
  url: https://github.com/BadgePiratesLLC
summary: A round electronic badge made by the SecKC (Kansas City hacker/security meetup) crew for DEF CON 26, with a laurel-wreath outline of the SecKC "Bob" mascot picked out in charlieplexed LEDs.
functions: Charlieplexed LED animations (a "snowfall" chase around the wreath and a randomized flash mode), a single button to cycle animation modes, a hidden mode unlocked by holding a magnet to the board (hall-effect sensor), and a WiFi mesh network (painlessMesh) between badges with an on-board mesh-status LED indicator.
look:
  colors:
  - white
  - black
  shape: circle
  themes:
  - skull
  - security
  - hardware tool
  - wearable
  form_factor: pcb badge
tech:
  mcu: ESP32
  leds:
    count: 42
    type: charlieplexed
    note: 'Charlieplexed white LEDs (34 populate the laurel wreath outline plus indicator LEDs) driven with a custom Chaplex library across 7 GPIO control pins.'
  display: none
  connectivity:
  - wifi
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Gerbers
  firmware_url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/BadgeCode
  eda_tool: null
  gerbers_url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/blob/master/Gerbers/SecKC_DC26_Final.zip
  bom_url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/blob/master/BadgePirates_SecKC_DC26Badge_BOM.xlsx
  notes: 'Repo also includes a separate "Daughter" board (GPS, screen/buttons, sensors — see Photos/Daughter_*.JPG) and a matching commemorative coin design, both of uncertain relationship to the main round badge.'
links:
- label: github.com/BadgePiratesLLC/DefCon_SecKC_26
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26
  kind: repo
images:
  - file: assets/images/badges/dc26/defcon-seckc-26/c897f3e972.jpg
    source: "https://github.com/BadgePiratesLLC/DefCon_SecKC_26"
    credit: "BadgePiratesLLC"
    caption: "Assembled SecKC DC26 badge, white PCB variant"
  - file: assets/images/badges/dc26/defcon-seckc-26/c42221f350.jpg
    source: "https://github.com/BadgePiratesLLC/DefCon_SecKC_26"
    credit: "BadgePiratesLLC"
    caption: "SecKC DC26 badge, black PCB variant with LEDs populated"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26
  title: DefCon_SecKC_26
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 26''.'
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/blob/master/BadgeCode/platformio.ini
  title: BadgeCode/platformio.ini
  accessed: '2026-09-07'
  note: 'Confirms MCU (ESP32, esp-wrover-kit board target) and painlessMesh dependency for the WiFi mesh feature.'
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/blob/master/BadgeCode/src/main.ino
  title: BadgeCode/src/main.ino
  accessed: '2026-09-07'
  note: 'Confirms charlieplexed LED layout (42-LED array, 34 in the laurel wreath), single-button animation cycling, hall-effect-unlocked hidden animation, and mesh-status LED.'
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Photos
  title: DefCon_SecKC_26/Photos
  accessed: '2026-09-07'
  note: 'Source of the two saved images (white and black PCB variants); also shows a separate "Daughter" board with GPS/screen/buttons/sensors and SecKC "Bob" mascot artwork.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The repo (archived Dec 2023, so read-only) is the only source found — no press coverage, storefront, or social posts turned up (web search budget was exhausted before those queries could run). Price, quantity made, and distribution/availability are not stated anywhere in the repo and are left empty. The Gerbers folder also has a separate "Daughter_gerber.zip" and the Photos folder shows a distinct daughter board (GPS, screen, buttons, sensors) plus a "Coin" design; it is unclear from the repo alone whether the daughter board shipped as part of this badge or was a separate/optional add-on, so tech fields here describe only the main round wreath board seen in the photos. DEF CON 26 was held in 2018, consistent with the entry''s existing year field; no event correction needed.'
last_modified_date: '2026-09-07'
---

The SecKC DC26 badge was made by BadgePirates for the SecKC (Kansas City-area hacker and information-security meetup) crew to bring to DEF CON 26 in 2018. It's a round PCB, produced in both white and black solder-mask variants, with a laurel wreath cut out of the copper around a silhouette of "Bob," the fedora-wearing SecKC mascot. The wreath itself is picked out in 34 charlieplexed white LEDs, driven off an ESP32 (esp-wrover-kit target) through a custom Chaplex driver across just seven control pins, giving 42 addressable LED positions total including a few off-wreath indicators.

A single button cycles between LED animation modes — a "snowfall" chase that runs down each side of the wreath, a reverse version of the same, and a randomized "flashy flashy" mode — while a hall-effect sensor unlocks an extra animation when a magnet is held near the board. Badges also join a WiFi mesh network using the painlessMesh library, with one of the indicator LEDs showing mesh connection status.

The GitHub repository (archived since December 2023) is the only source found for this entry; it includes full Gerbers, schematic, BOM, and firmware for the main wreath badge, plus files for a separate "Daughter" board (GPS, a screen and buttons, and additional sensors) and a matching commemorative coin, whose exact relationship to the main badge — bundled hardware, optional add-on, or a separate project sharing the repo — isn't stated in the files reviewed. No pricing, production quantity, or distribution details were found.

## Make your own

Firmware source, a PlatformIO project targeting the ESP32 (`esp-wrover-kit` board, Arduino framework), lives under `BadgeCode/`. PCB fabrication files — Gerbers, drill chart, schematic PDF, and a BOM spreadsheet — are under `Gerbers/`. A `How to Program Badge.docx` in the repo root documents the flashing procedure.
