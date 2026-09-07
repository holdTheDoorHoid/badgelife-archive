---
title: Uncut Gem (Quantum Village)
id: dc33-uncut-gem-quantum-village
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc33
year: 2025
makers:
- name: Quantum Village
  url: https://github.com/QuantumVillage
summary: 'An open-source nitrogen-vacancy (NV) center diamond magnetometer kit built from consumer-grade parts, released by Quantum Village at DEF CON 33.'
functions: 'Detects magnetic fields using NV-center diamond quantum sensing; an ESP32 with an OLED screen drives a low-noise photodiode amplifier and a microwave generator (ADF4350/1) to run the measurement.'
look:
  colors: []
  shape: null
  themes:
  - science
  - hardware tool
  - measurement
tech:
  mcu: ESP32
  leds: null
  display: OLED
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: '~£115 in parts (~$145 USD)'
  price_usd: 145
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Self-build from published BOM and PCB/firmware files; V2 was released at DEF CON 33 (2025) via Quantum Village.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/QuantumVillage/UncutGem/tree/main/hardware
  firmware_url: https://github.com/QuantumVillage/UncutGem/tree/main/firmware
  eda_tool: null
  license: AGPL-3.0
  fab_url: null
  bom_url: https://github.com/QuantumVillage/UncutGem/blob/main/BuildGuide/BuildGuide.md
  notes: 'Commercial licensing is also available directly through Quantum Village Inc.'
links:
- label: github.com/QuantumVillage/UncutGem
  url: https://github.com/QuantumVillage/UncutGem
  kind: repo
images:
  - file: assets/images/badges/dc33/uncut-gem-quantum-village/1568f65c6e.jpg
    source: "https://github.com/QuantumVillage/UncutGem"
    credit: "Quantum Village"
    caption: "Uncut Gem NV-center diamond magnetometer, front view"
  - file: assets/images/badges/dc33/uncut-gem-quantum-village/0e2a390995.jpg
    source: "https://github.com/QuantumVillage/UncutGem"
    credit: "Quantum Village"
    caption: "Uncut Gem NV-center diamond magnetometer, back view"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- 'Not a wearable badge or SAO in the usual sense: it is a benchtop DIY quantum-sensing instrument (an NV-center diamond magnetometer) that Quantum Village publishes as an open-source build. Filed as type: kit.'
status: released
sources:
- kind: url
  url: https://github.com/QuantumVillage/UncutGem
  title: Uncut Gem (Quantum Village)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/QuantumVillage/UncutGem/main/README.md
  title: 'UncutGem README'
  accessed: '2026-09-07'
  note: 'Confirmed maker (Quantum Village Inc.), that V2 shipped at DEF CON 33 (2025), BOM/cost breakdown (~£115), ESP32 + OLED, AGPL-3.0 license, and image file paths.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo README confirms Quantum Village Inc. as maker and that "V2" launched at DEF CON 33 (2025); corrected event from "other" to dc33 on that basis. Quantity made and whether/how many were distributed at the village (vs. purely self-build) are not stated in the repo. No third-party coverage (Hackaday, press, storefront) was found within search budget to corroborate distribution details. LED count/type and exact OLED size not specified in the README.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/uncut-gem-quantum-village/
---

The Uncut Gem is an open-source nitrogen-vacancy (NV) center diamond magnetometer built by Quantum Village, a DEF CON village focused on hands-on quantum computing and sensing. Rather than a wearable badge, it is a benchtop instrument: an ESP32 board with an OLED display controls a low-noise photodiode amplifier and an ADF4350/1 microwave generator to interrogate a small NV-center diamond, letting a builder detect magnetic fields using the same quantum effect found in professional-grade quantum sensors. Version 2 of the project was released at DEF CON 33 in 2025.

The design is fully open under the AGPL-3.0 license, with PCB schematics, a diamond-mounting design, 3D-printable parts, Arduino-based firmware, and a full build guide published in the GitHub repository. The project deliberately favors off-the-shelf and consumer-grade components to keep the total bill of materials around £115 (roughly $145 USD), spanning the battery pack, laser module, microwave generator and amplifier chain, PCB, OLED screen, ESP32 module, and the diamond itself, so hobbyists can build a working quantum magnetometer without lab-grade equipment.

## Make your own

Everything needed to build one is in the repository: `/hardware/pcb` for the PCB schematics and parts, `/hardware/DiamondMount` for the diamond-mounting hardware, `/3D-files` for printable enclosure parts, `/firmware` for the Arduino-based control code, and `BuildGuide/BuildGuide.md` for step-by-step assembly instructions. Commercial licensing is available directly through Quantum Village Inc. for anyone wanting to build and sell units.
