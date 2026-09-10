---
title: joco-2019-badge — JoCo 2019 unofficial badge
id: other-joco-2019-badge-joco-2019-unofficial-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2019
makers:
- name: Open Research Institute
  url: https://github.com/OpenResearchInstitute
summary: An unofficial electronic badge for JoCo Cruise 2019, running new firmware on the badge hardware built for the 2018 cruise, with a Bender-style face of RGB LEDs.
functions: Bluetooth-connected badge firmware (a "mastermind" companion component is referenced in the repo) driving a 14-LED RGB face with dedicated eye and tooth LEDs, plus a Micro SD card slot for content.
look:
  colors: []
  shape: null
  themes:
  - robot
  - sci-fi
tech:
  mcu: nRF52832
  leds:
    count: 14
    type: RGB
    note: Laid out as a 4x3 grid (LEDs 0-11) plus a dedicated "eye" LED (12) and "tooth" LED (13), matching a Bender-style face.
  display: null
  connectivity:
  - bluetooth
  battery: 3x AA
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/OpenResearchInstitute/joco-2019-badge/tree/master/hardware
  firmware_url: https://github.com/OpenResearchInstitute/joco-2019-badge/tree/master/firmware
  eda_tool: Altium
  license: Apache License 2.0 (files were embargoed until 2019-03-16, per the repo README)
  notes: The hardware directory holds Altium schematics/PCB files inherited from the 2018 badge design; the 2019 repo itself is mainly a firmware revision for that existing board.
links:
- label: github.com/OpenResearchInstitute/joco-2019-badge
  url: https://github.com/OpenResearchInstitute/joco-2019-badge
  kind: repo
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/OpenResearchInstitute/joco-2019-badge
  title: joco-2019-badge — JoCo 2019 unofficial badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''JoCo Cruise 2019''.'
- kind: url
  url: https://raw.githubusercontent.com/OpenResearchInstitute/joco-2019-badge/master/README.md
  title: joco-2019-badge README
  accessed: '2026-09-07'
  note: Confirms it is unofficial, based on AND!XOR's DEF CON 25 Bender badge, running on 2018 cruise badge hardware; nRF52832 MCU (Rigado module), 3x AA power, Apache-2.0 license effective 2019-03-16.
- kind: url
  url: https://raw.githubusercontent.com/OpenResearchInstitute/joco-2019-badge/master/LED-Layout.md
  title: joco-2019-badge LED-Layout.md
  accessed: '2026-09-07'
  note: 'LED map: 4x3 grid of 12 LEDs (0-11) plus dedicated eye (12) and tooth (13) LEDs, 14 total.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'JoCo Cruise has no corresponding id in _data/events.yml, so event is left as "other"; this was made for JoCo Cruise 2019 (a themed cruise, not a hacker con in the usual sense). The repo is a firmware revision of AND!XOR''s DEF CON 25 Bender badge, adapted to run on the badge hardware built for the prior year''s cruise (see the related OpenResearchInstitute/joco-2018-badge / phase4ground/joco-2018-badge repo, not fetched here). Could not find price, quantity made, availability/distribution details, or any photo of the assembled badge; the repo''s adobe-illustrator folder contains a file named "P4G_manual_trace_only_badge_1.png" but as of 2026-09-07 that URL actually serves an unrelated vintage radio dial photo, not badge artwork, so no image was saved for this entry. Display field left null: the README mentions a screen near the Micro SD slot but gives no size/type.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/joco-2019-badge-joco-2019-unofficial-badge.glb
  method: gerber
  source_file: hardware/Outputs
  generated: '2026-09-10'
  bytes: 90428
  size_mm:
  - 132.0
  - 143.2
---

The JoCo 2019 badge is an unofficial electronic badge made for JoCo Cruise 2019 by Open Research Institute. Rather than a new board, it reuses the badge hardware built for the 2018 cruise and ships new firmware for it — itself a software revision of the badge AND!XOR designed for DEF CON 25 ("Bender"). The badge is built around a Nordic nRF52832 (a Bluetooth-capable ARM chip, on a Rigado module) and runs off three AA batteries.

The badge's signature feature is its face: a 4x3 grid of 12 RGB LEDs plus two more dedicated to an "eye" and a "tooth," echoing the Bender look of its DEF CON ancestor. It also has a Micro SD card slot next to its screen for loading content. Firmware, hardware design files (inherited Altium schematics/PCB layout from the 2018 board), NFC-related files, and SD card images are all published in the GitHub repo; the maker's README says the material was kept private until March 16, 2019 and released after that under the Apache License 2.0.

Details that would normally round this out — unit price, how many were made, and how badges were distributed to cruise attendees — are not documented in the repo or turned up in a search, so those fields are left blank rather than guessed.

## Make your own

The repo ships firmware, Altium hardware files, Illustrator artwork, NFC components, and an SD card image. Building the firmware requires Nordic's nRF5 SDK v12.3.0 (later SDK versions are noted as incompatible), the GNU ARM Embedded toolchain, and Segger J-Link tools for JTAG flashing/debugging — see the repo's README for the full environment setup.
