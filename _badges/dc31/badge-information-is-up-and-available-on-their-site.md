---
title: DN-Badge-12 (Darknet-NG DEF CON 31 Badge)
id: dc31-badge-information-is-up-and-available-on-their-site
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
summary: 'A stopgap offline-communicator badge from the Darknet-NG contest: a TTGO LoRa32 (Meshtastic) board dropped into a 3D-printed case, released as open hardware when the team''s own custom badge was not ready in time.'
functions: Runs stock Meshtastic firmware on the TTGO LoRa32 board for long-range, off-grid text messaging over LoRa, paired to a phone app over Bluetooth; used by the Darknet-NG contest as its "Daemon" communication channel for DEF CON 31.
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
  display: null
  connectivity:
  - lora
  - bluetooth
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - purchase
  - kit
  where: The Meshtastic-based TTGO LoRa32 mainboard was sourced from store.rokland.com; the case, face, back and power-bar are 3D-printed from STL files Darknet-NG published themselves (or via a local hackerspace/library printer). Darknet-NG stated only a limited number of assembled badges would be available at the con itself.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/darknet-ng/Darknet-NG-12-Badge
  firmware_url: null
  eda_tool: null
  notes: 'The case/enclosure design (DN-Badge-version-8.6.0, aka "Darknet-NG-12-Badge") is open source: STL files on GitHub, Thingiverse, and Printables, with editable Tinkercad source files for the body, face, back and power-bar. The mainboard itself is a third-party TTGO LoRa32 module running stock open-source Meshtastic firmware, not a Darknet-NG PCB design.'
links:
- label: darknet-ng.network/darknet-ng-will-return-at-def-con-31
  url: https://darknet-ng.network/darknet-ng-will-return-at-def-con-31/
  kind: website
  archived: https://web.archive.org/web/20251209105400/https://darknet-ng.network/darknet-ng-will-return-at-def-con-31/
- label: store.rokland.com
  url: https://store.rokland.com
  kind: store
  archived: https://web.archive.org/web/20260827005342/https://store.rokland.com/
- label: darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case
  url: https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case/
  kind: website
  archived: https://web.archive.org/web/20260422135443/https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case/
- label: darknet-ng.network/darknet-ng-badge-12-full-setup
  url: https://darknet-ng.network/darknet-ng-badge-12-full-setup/
  kind: doc
  archived: https://web.archive.org/web/20260511203252/https://darknet-ng.network/darknet-ng-badge-12-full-setup/
- label: github.com/darknet-ng/Darknet-NG-12-Badge
  url: https://github.com/darknet-ng/Darknet-NG-12-Badge
  kind: repo
images:
- file: assets/images/badges/dc31/badge-information-is-up-and-available-on-their-site/89e0612bd8.jpg
  source: https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case/
  credit: Darknet-NG (Gater)
  caption: 3D-printed DN-Badge-12 case housing a TTGO LoRa32 board
  archived: https://web.archive.org/web/20260422135443/https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case/
contact: {}
notes:
- This year it is a hands-on experience. Battery and LoRA board from https://store.rokland.com. Case is 3d printed.
- Sheet title was a placeholder ("Badge information is up and available on their site"); the actual project is the DN-Badge-12 / DN-Badge-version-8.6.0 case for a TTGO LoRa32 Meshtastic board, designed by Darknet-NG members "Gater" and "Digital" starting December 2022.
status: released
sources:
- kind: sheet
  event: dc31
  row: 25
  updated: '2023-06-25'
- kind: url
  url: https://darknet-ng.network/darknet-ng-will-return-at-def-con-31/
  title: Darknet-NG will return at DEF CON 31
  accessed: '2026-09-06'
  note: 'Explains the badge was a stopgap: Darknet-NG''s own custom badge wasn''t ready, so they adopted an open-source design from another team for offline (LoRa) communication, with only a limited number available at the con.'
  archived: https://web.archive.org/web/20251209105400/https://darknet-ng.network/darknet-ng-will-return-at-def-con-31/
- kind: url
  url: https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case/
  title: Darknet-NG 12 Badge for DEF CON 31 Case
  accessed: '2026-09-06'
  note: Gives the badge/case name (DN-Badge-version-8.6.0 / Darknet-NG-12-Badge), credits designers Gater and Digital, and links the GitHub/Thingiverse/Printables/Tinkercad source files.
  archived: https://web.archive.org/web/20260422135443/https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31-case/
- kind: url
  url: https://darknet-ng.network/darknet-ng-badge-12-full-setup/
  title: Darknet-NG Badge 12 Full Setup
  accessed: '2026-09-06'
  note: Assembly/flashing walkthrough confirming the mainboard is a TTGO LoRa32 running Meshtastic firmware, paired to iOS/Android over Bluetooth.
  archived: https://web.archive.org/web/20260511203252/https://darknet-ng.network/darknet-ng-badge-12-full-setup/
- kind: url
  url: https://github.com/darknet-ng/Darknet-NG-12-Badge
  title: darknet-ng/Darknet-NG-12-Badge
  accessed: '2026-09-06'
  note: Confirms the repo holds only 3D-print STL files for the case/body/face/back/power-bar, not a custom PCB or firmware.
- kind: url
  url: https://store.rokland.com
  title: Rokland store
  accessed: '2026-09-06'
  note: Checked for the specific LoRa board/battery product; general storefront sells Meshtastic-compatible LoRa hardware and batteries but the exact SKU used could not be confirmed.
  archived: https://web.archive.org/web/20260827005342/https://store.rokland.com/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Retitled from the sheet''s placeholder text. Core facts (TTGO LoRa32 + Meshtastic + 3D-printed case, open-source enclosure files, limited quantity at the con) are confirmed from Darknet-NG''s own blog posts and GitHub repo. Could not confirm: exact price, exact quantity made, LED/display presence (none apparent from sources), or the specific Rokland SKU for the LoRa board/battery mentioned in the original sheet note. No firmware repo of their own was found (they run stock Meshtastic). Not the same item as the dc30 "They still have not said anything..." Darknet entry (different year) or later Darknet-NG entries (dc32-dc34).'
last_modified_date: '2026-09-06'
---

Darknet-NG, the long-running DEF CON contest group, planned an all-new custom badge for DEF CON 31 but ran into part shortages and delays. Rather than go without an offline communication channel for their "Daemon" game, they adopted an existing open-source design: a TTGO LoRa32 module (an ESP32 board with an integrated LoRa radio) flashed with the open-source Meshtastic firmware, housed in a 3D-printed enclosure the team calls the DN-Badge-12 (design version 8.6.0). The mainboard and battery came from the Rokland store, a supplier of Meshtastic-compatible LoRa hardware.

The enclosure — body, face, back plate, and a "power-bar" battery holder — was designed by Darknet-NG members "Gater" and "Digital" starting in December 2022, and was released as open hardware ahead of the con: STL files went up on GitHub, Thingiverse, and Printables, with editable Tinkercad source files for anyone who wanted to customize their own face or body before printing. A companion blog post walked builders through slicing, printing, assembly, and flashing/pairing the Meshtastic firmware over Bluetooth to an Android or iOS phone.

Because it relied on volunteers with 3D printers rather than a manufactured PCB run, Darknet-NG said only a limited number of assembled badges would be available at the conference itself, with the STLs published in advance so attendees could print and build their own beforehand.

## Make your own

1. Get a TTGO LoRa32 (ESP32 + LoRa) board and a suitable battery (Darknet-NG sourced theirs from store.rokland.com).
2. Download the case STLs (body, face, back, power-bar) from the [GitHub repo](https://github.com/darknet-ng/Darknet-NG-12-Badge), or customize your own face/body first in the linked Tinkercad projects.
3. Slice with PrusaSlicer (organic supports recommended for faster cleanup) and print.
4. Assemble: insert the TTGO LoRa32 mainboard into the printed body, attach the antenna, install the power-bar battery holder, and close up the case.
5. Flash Meshtastic firmware onto the board (web flasher at flasher.meshtastic.org on Windows/macOS, or esptool on Linux), then pair it to the Meshtastic mobile app over Bluetooth and set a location name.
