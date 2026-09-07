---
title: Darknet-NG 12 Badge
id: dc31-darknet-ng-12-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Darknet-NG
  url: https://darknet-ng.network/
summary: 'A stopgap offline-communicator badge from the Darknet-NG DEF CON contest group: a TTGO LoRa32 (Meshtastic) board dropped into a 3D-printed case, released as open hardware for DEF CON 31.'
functions: Runs stock Meshtastic firmware on a TTGO LoRa32 board for LoRa mesh text messaging, paired to a phone app over Bluetooth; used as Darknet-NG's "Daemon" communication channel at DEF CON 31.
look:
  colors: []
  shape: null
  themes:
  - radio
  - privacy
  - security
tech:
  mcu: ESP32
  leds: null
  display: 0.96" OLED
  connectivity:
  - lora
  - bluetooth
  battery: 3.7V LiPo, Micro JST 1.25 (1100-3000mAh options)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - purchase
  - kit
  where: The TTGO/LILYGO LoRa32 mainboard and battery were sourced by builders separately; the case (body, face, back, power-bar) is 3D-printed from STL files Darknet-NG published themselves. Only a limited number of assembled badges were available at the con itself.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/darknet-ng/Darknet-NG-12-Badge
  firmware_url: null
  eda_tool: null
  notes: 'The case/enclosure design (version 8.6.0/8.6.8, "Darknet-NG-12-Badge") is open source: STL files on GitHub (GPL-3.0), Thingiverse, and Printables, with editable Tinkercad source files. The mainboard is a third-party LILYGO/TTGO LoRa32 module running stock open-source Meshtastic firmware, not a Darknet-NG PCB design. Designed by Darknet-NG members "Gater" and "Digital" starting December 2022.'
links:
- label: darknet-ng.network/darknet-ng-12-badge-for-def-con-31
  url: https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31/
  kind: website
- label: darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case
  url: https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case/
  kind: website
- label: github.com/darknet-ng/Darknet-NG-12-Badge
  url: https://github.com/darknet-ng/Darknet-NG-12-Badge
  kind: repo
images:
- file: assets/images/badges/dc31/darknet-ng-12-badge/aabc96a328.jpg
  source: https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case/
  credit: Darknet-NG
  caption: Assembled Darknet-NG 12 badge case for DEF CON 31
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31/
  title: Darknet-NG 12 Badge for DEF CON 31
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc31''.'
- kind: url
  url: https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case/
  title: Darknet-NG 12 Badge for DEF CON 31 Case
  accessed: '2026-09-07'
  note: Case design details, designers Gater and Digital, STL/Tinkercad file locations, and the source image saved for this entry.
- kind: url
  url: https://github.com/darknet-ng/Darknet-NG-12-Badge
  title: darknet-ng/Darknet-NG-12-Badge
  accessed: '2026-09-07'
  note: Confirms the repo holds only 3D-print STL files (GPL-3.0) for the case, not a custom PCB or firmware.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is the same item already fully researched as dc31-badge-information-is-up-and-available-on-their-site (title "DN-Badge-12 (Darknet-NG DEF CON 31 Badge)"), which carries a more thorough write-up including the Rokland sourcing and full make-your-own steps. Kept this entry filled in per instructions rather than left as a stub; consider merging/removing the duplicate. Could not confirm exact price or quantity made.'
last_modified_date: '2026-09-07'
---

Darknet-NG, the long-running DEF CON contest group, planned an all-new custom badge for DEF CON 31 but ran into delays, so it adopted an open-source stopgap design instead: a LILYGO/TTGO LoRa32 board (an ESP32 with an integrated LoRa radio and a 0.96" OLED) flashed with the open-source Meshtastic firmware, housed in a 3D-printed case the team calls the Darknet-NG 12 Badge (design version 8.6.0/8.6.8). It served as the "Daemon" offline communication channel for the group's DEF CON 31 contest, letting attendees exchange LoRa mesh messages over a phone app paired via Bluetooth.

The enclosure — body, face, back plate, and a "power-bar" battery holder — was designed by Darknet-NG members "Gater" and "Digital" starting in December 2022, after more than 20 iterations. It was released as open hardware (GPL-3.0) ahead of the con, with STL files on GitHub, Thingiverse, and Printables, plus editable Tinkercad source files so builders could customize their own face or body before printing. Because it relied on volunteers' 3D printers rather than a manufactured PCB run, only a limited number of assembled badges were available at the con itself.

This entry duplicates dc31-badge-information-is-up-and-available-on-their-site, which documents the same badge under the title "DN-Badge-12 (Darknet-NG DEF CON 31 Badge)" with additional sourcing detail (the Rokland store for the mainboard/battery) and a full build walkthrough.

## Make your own

1. Get a LILYGO/TTGO LoRa32 (ESP32 + LoRa) board and a compatible 3.7V LiPo battery.
2. Download the case STLs (body, face, back, power-bar) from the [GitHub repo](https://github.com/darknet-ng/Darknet-NG-12-Badge), or start from the linked Tinkercad projects to customize your own face/body first.
3. Slice and 3D print the parts.
4. Assemble: insert the mainboard into the printed body, attach the antenna, install the power-bar battery holder, and close up the case.
5. Flash Meshtastic firmware onto the board and pair it to the Meshtastic mobile app over Bluetooth.

