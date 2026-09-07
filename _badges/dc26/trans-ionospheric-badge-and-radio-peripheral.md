---
title: trans-ionospheric — badge and radio peripheral
id: dc26-trans-ionospheric-badge-and-radio-peripheral
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Open Research Institute
  url: https://openresearch.institute/badge/
summary: A hackable conference badge built as a "fun wearable amateur radio peripheral" for Open Research Institute's Phase 4 Ground and Phase 4 Space projects, demonstrated at DEF CON 26.
functions: Runs customizable nRF-based firmware with a Bluetooth LE UART monitor mode that exposes hidden "easter eggs" via apps like nRF UART / nRF Connect; firmware is field-updatable over SWD.
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
  - village badge
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - ble
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Distributed at Open Research Institute's DEF CON 26 (2018) presence in Las Vegas, NV.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/OpenResearchInstitute/trans-ionospheric/tree/master/hardware
  firmware_url: https://github.com/OpenResearchInstitute/trans-ionospheric/tree/master/firmware
  eda_tool: null
  notes: Hardware schematics are shared as Altium (.SchDoc/.CSPcbDoc) files, not fully open EDA source; firmware is Apache 2.0 licensed and builds against the Nordic nRF5 SDK v12.3, implying an nRF51/nRF52-series MCU (not stated explicitly by the maker). Repo overall is LGPL-3.0 per GitHub metadata.
links:
- label: github.com/OpenResearchInstitute/trans-ionospheric
  url: https://github.com/OpenResearchInstitute/trans-ionospheric
  kind: repo
- label: Open Research Institute — badge page
  url: https://openresearch.institute/badge/
  kind: website
- label: 'Hackaday #badgelife DEFCON26 documentary (Trans-Ionospheric segment)'
  url: https://youtu.be/G2fHKRONc6U?t=12m22s
  kind: video
images:
- file: assets/images/badges/dc26/trans-ionospheric-badge-and-radio-peripheral/fe7d5d3b0d.jpg
  source: https://openresearch.institute/badge/
  credit: Open Research Institute
  caption: Trans-Ionospheric badge as demonstrated at DEF CON 26
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/OpenResearchInstitute/trans-ionospheric
  title: trans-ionospheric — badge and radio peripheral
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://openresearch.institute/badge/
  title: badge | Open Research Institute
  accessed: '2026-09-07'
  note: 'Maker''s own badge page: confirms DEF CON 26 (2018) demonstration, describes it as a hackable amateur-radio-themed conference badge, Bluetooth LE easter-egg monitor mode, SWD firmware updates; source of the badge photo.'
- kind: url
  url: https://raw.githubusercontent.com/OpenResearchInstitute/trans-ionospheric/master/firmware/README.md
  title: trans-ionospheric firmware README
  accessed: '2026-09-07'
  note: Confirms firmware targets the Nordic nRF5 SDK v12.3 (nRF51/nRF52-family MCU), Apache 2.0 licensed, and states the badge is based on the unofficial JoCo Cruise 2018 "pirate monkey" badge, itself derived from AND!XOR's DEF CON 25 Bender Badge.
- kind: url
  url: https://api.github.com/repos/OpenResearchInstitute/trans-ionospheric
  title: GitHub repo metadata
  accessed: '2026-09-07'
  note: Repo license (LGPL-3.0), topics (badge, badgelife), created 2018-03-06.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Event corrected from "other" to dc26 (DEF CON 26, 2018) per the maker's own badge page. Exact MCU part number, LED count/type, display, price, and quantity made are not stated by any source found and are left empty rather than guessed; the firmware README implies a Nordic nRF51/nRF52-series chip (nRF5 SDK v12.3 dependency) but does not name the exact part, so tech.mcu is left null. Hardware files are Altium schematics/PCB docs (not a fully open EDA format like KiCad), so make_your_own.open_source is set to "partial" rather than "yes". No storefront or pricing page was found; distribution is inferred as sold/given out at the DEF CON 26 table based on the badge page's "supporting us at our events" phrasing.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/trans-ionospheric-badge-and-radio-peripheral/
model:
  file: assets/models/dc26/trans-ionospheric-badge-and-radio-peripheral.glb
  method: gerber
  source_file: hardware/Outputs
  generated: '2026-09-07'
  bytes: 90428
  size_mm:
  - 132.0
  - 143.2
---

The Trans-Ionospheric is a hackable conference badge built by Open Research Institute as a wearable amateur-radio-themed peripheral tied to the organization's Phase 4 Ground and Phase 4 Space projects. It was demonstrated at DEF CON 26 in Las Vegas in 2018, and appears in a segment of Hackaday's #badgelife DEF CON 26 documentary. The firmware's own README traces its lineage back through the unofficial JoCo Cruise 2018 "pirate monkey" badge to AND!XOR's DEF CON 25 Bender Badge, placing it in that badge-hardware family tree.

The badge runs customizable firmware (Apache 2.0 licensed, built against the Nordic nRF5 SDK v12.3) and exposes a Bluetooth LE UART monitor mode with hidden "easter eggs" reachable through apps like nRF UART or nRF Connect. Owners can reflash it themselves over an SWD interface once they have the needed equipment. Hardware design files (schematics and PCB layout in Altium format) and firmware source are published in the project's GitHub repository, alongside supporting graphics, an NFC subproject, and lanyard artwork.

Specific technical details the maker does not spell out publicly — the exact MCU part number, LED configuration, any onboard display, price, and production quantity — could not be confirmed from the sources reviewed and are left blank here rather than guessed.
