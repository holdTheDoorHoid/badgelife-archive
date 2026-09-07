---
title: "Darknet-NG 13 Badge"
id: dc32-another-badge-similar-to-past-years
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Darknet-NG
  url: https://darknet-ng.network/
summary: A DIY LoRa meshnet badge built around a Heltec WiFi LoRa 32 V3 board in a custom 3D-printed case, for joining DC Darknet's private Meshtastic mesh at DEF CON 32.
functions: Forms a badge that will interact with a private LoRa meshnet; runs Meshtastic firmware for peer-to-peer, infrastructure-free messaging between agents.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - kit
tech:
  mcu: none
  leds: null
  display: null
  connectivity:
  - lora
  battery: 3.7V LiPo, Micro JST 1.25 connector (1100 mAh options used by the community)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: About 40 (per the community sheet; parts and case are DIY, not centrally manufactured)
  availability: unknown
  distribution:
  - free_drop
  - kit
  where: DC Darknet said it would have about 40 badges to provide for donations; the badge itself is a DIY build (people source the Heltec WiFi LoRa 32 V3 board and battery themselves and 3D-print the case) rather than a single pre-made item handed out.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/darknet-ng/Darknet-NG-13-Badge
  firmware_url: null
  eda_tool: null
  notes: The published repo (GPL-3.0) contains only the 3D-printable case files (body, battery housing, buttons, face plate); there is no custom PCB. The electronics are an off-the-shelf Heltec WiFi LoRa 32(V3) module running Meshtastic firmware, not badge-specific firmware.
links:
- label: darknet-ng.net
  url: https://darknet-ng.net
  kind: website
- label: darknet-ng.network/darknet-ng-13-badge
  url: https://darknet-ng.network/darknet-ng-13-badge/
  kind: website
- label: Darknet-NG 13 DIY Badge Case (assembly steps)
  url: https://darknet-ng.network/darknet-ng-13-diy-badge-case/
  kind: doc
- label: darknet-ng/Darknet-NG-13-Badge (GitHub)
  url: https://github.com/darknet-ng/Darknet-NG-13-Badge
  kind: repo
- label: Darknet-NG 13 Badge on Printables
  url: https://www.printables.com/model/943540-darknet-ng-13-badge
  kind: fab
images:
- file: assets/images/badges/dc32/another-badge-similar-to-past-years/2a18a6a226.jpg
  source: "https://darknet-ng.network/darknet-ng-13-diy-badge-case/"
  credit: "Darknet-NG"
  caption: "Assembled Darknet-NG 13 badge case with Heltec WiFi LoRa 32 V3 board"
- file: assets/images/badges/dc32/another-badge-similar-to-past-years/689bf4ddee.jpg
  source: "https://darknet-ng.network/darknet-ng-13-diy-badge-case/"
  credit: "Darknet-NG"
  caption: "Development versions of the Darknet-NG 13 badge case"
contact:
  raw:
  - DC Darknet will have about 40 of these badges to provide for donations.
notes:
- |-
  Go to the following blog post: darknet-ng.network/darknet-ng-13-badge
  This is a DIY LoRa meshnet badge. Pieces/parts will be gathered by you. Directions will be released in stages.
status: released
sources:
- kind: sheet
  event: dc32
  row: 43
  updated: ''
- kind: url
  url: https://darknet-ng.network/darknet-ng-13-badge/
  title: "Darknet-NG 13 DIY Badge – Darknet-NG"
  accessed: '2026-09-06'
  note: Confirms MCU (Heltec WiFi LoRa 32 V3, US915 MHz), battery, DIY assembly steps, and that it forms a private LoRa mesh.
- kind: url
  url: https://darknet-ng.network/darknet-ng-13-diy-badge-case/
  title: "Darknet-NG 13 DIY Badge Case – Darknet-NG"
  accessed: '2026-09-06'
  note: Case assembly instructions, photos of the assembled unit, and STL/TinkerCAD links.
- kind: url
  url: https://github.com/darknet-ng/Darknet-NG-13-Badge
  title: "darknet-ng/Darknet-NG-13-Badge"
  accessed: '2026-09-06'
  note: Confirms GPL-3.0 license and that the repo holds only 3D-printed case files, no PCB or firmware.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    This is the "Darknet-NG 13" badge for DEF CON 32: a DIY case (Heltec WiFi LoRa 32 V3 module
    running Meshtastic) rather than a custom PCB. Retitled from the sheet's placeholder wording
    to the maker's actual project name. No exact price, total quantity, or firmware repo (Meshtastic
    is third-party, not a Darknet-NG fork) was found. Likely duplicates dc32-secret-badge-no-info-at-all:
    both are "Darknet (Gulo)" rows for dc32 (sheet rows 42 and 43) linking to the same
    darknet-ng-13-badge blog post; the sheet appears to have logged the pre-announcement teaser and
    the badge itself as separate rows.
last_modified_date: '2026-09-06'
---

DC Darknet's badge for DEF CON 32 was not a fabricated PCB but a DIY kit: a Heltec WiFi LoRa 32(V3) module (running the open-source Meshtastic firmware) housed in a custom 3D-printed case, letting wearers join a private LoRa mesh network for infrastructure-free peer-to-peer messaging across the con. Builders sourced the electronics and battery themselves and printed the case from files Darknet-NG published, with assembly and configuration instructions released in stages leading up to the event. The group said it would have about 40 badges on hand to provide in exchange for donations to OSSEM HOLON, a 501(c)(3) nonprofit.

Only the case design is published on GitHub (GPL-3.0); there is no custom circuit board or badge-specific firmware behind it, since the Meshtastic firmware running on the Heltec board is a separate open-source project. The case files are also mirrored on Printables and Thingiverse, and a TinkerCAD project lets builders customize per-agent details before printing.

## Make your own

1. Order a Heltec WiFi LoRa 32(V3) board (US915 MHz for North American DEF CON use) and a compatible 3.7V LiPo battery with a Micro JST 1.25 connector.
2. Flash the board with Meshtastic firmware and join the DC Darknet mesh channel.
3. 3D-print the case parts (body, battery housing, buttons, face plate) from the [GitHub repo](https://github.com/darknet-ng/Darknet-NG-13-Badge) or [Printables listing](https://www.printables.com/model/943540-darknet-ng-13-badge) in PETG, and assemble with two M2x25mm screws.
