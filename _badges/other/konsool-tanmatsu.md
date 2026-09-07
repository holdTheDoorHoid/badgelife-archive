---
title: Konsool / Tanmatsu
id: other-konsool-tanmatsu
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2026
makers:
- name: Badge.Team (Renze Nicolai, Paul Honig, Julian Scheffers, et al.)
  url: https://badge.team/
- name: Nicolai Electronics
  url: https://nicolaielectronics.nl/
  role: sells the pre-assembled "Tanmatsu" version, handles manufacturing and regulatory compliance
summary: 'A hackable handheld palmtop computer with a QWERTY keyboard and 800x480 display, built around an ESP32-P4 application processor. "Konsool" is the open-source design name; "Tanmatsu" is the pre-assembled product Nicolai Electronics sells.'
functions: 'General-purpose hacker terminal: runs a launcher firmware that loads multiple apps (terminal emulator, mesh messaging, camera app, games), plus LoRa/Meshtastic-style mesh communication.'
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: ESP32-P4 (dual-core RISC-V, up to 400MHz) + ESP32-C6 (wifi/BLE/802.15.4 co-processor) + CH32 (keyboard/housekeeping)
  leds: {count: null, type: null, note: 'Addressable LEDs on the front of the board next to the screen (count not stated).'}
  display: 3.97" 800x480 MIPI DSI, 60Hz
  connectivity:
  - wifi
  - ble
  - lora
  - zigbee
  - usb
  - i2c
  battery: null
  sao_version: v2
get_one:
  price: "EUR 99.17 (excl. EU VAT) / EUR 120 (incl. VAT)"
  price_usd: 102.0
  quantity: ''
  availability: available
  availability_note: 'Still listed for sale as of a July 2026 Hackaday review; a year into production.'
  distribution:
  - preorder
  - purchase
  where: Preordered/purchased pre-assembled from Nicolai Electronics' webshop; the underlying "Konsool" design is open hardware anyone can build.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Nicolai-Electronics/tanmatsu-hardware
  firmware_url: https://github.com/badgeteam
  eda_tool: null
  license: CERN-OHL-P
  notes: 'Mechanical, electronics, and firmware repos are public under Badge.Team / Nicolai-Electronics GitHub orgs.'
links:
- label: badge.team/docs/badges/konsool
  url: https://badge.team/docs/badges/konsool/
  kind: website
- label: badge.team/docs/badges/konsool/konsool-logo.svg
  url: https://badge.team/docs/badges/konsool/konsool-logo.svg
  kind: website
- label: badge.team/docs/badges/konsool/konsool_mascots.svg
  url: https://badge.team/docs/badges/konsool/konsool_mascots.svg
  kind: website
- label: 'Hackaday: A Closer Look At The Tanmatsu'
  url: https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
  kind: article
- label: 'Hackaday: Review, The Tanmatsu, A Year On'
  url: https://hackaday.com/2026/07/01/review-the-tanmatsu-a-year-on/
  kind: article
- label: 'Nicolai Electronics: Tanmatsu can now be pre-ordered'
  url: https://nicolaielectronics.nl/blog/2025/01/06/tanmatsu-can-now-be-pre-ordered/
  kind: website
- label: 'CNX Software: Tanmatsu handheld terminal'
  url: https://www.cnx-software.com/2025/01/10/tanmatsu-handheld-terminal-features-esp32-p4-risc-v-mcu-qwerty-keyboard-wifi-bluetooth-802-15-4-and-lora-connectivity/
  kind: article
- label: 'GitHub: tanmatsu-hardware'
  url: https://github.com/Nicolai-Electronics/tanmatsu-hardware
  kind: repo
- label: 'GitHub: badgeteam org'
  url: https://github.com/badgeteam
  kind: repo
images:
- file: assets/images/badges/other/konsool-tanmatsu/9d3aade5e1.jpg
  source: "https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/"
  credit: "Hackaday / Tanmatsu press photo"
  caption: "Tanmatsu handheld held in a hand, showing the QWERTY keyboard and screen"
- file: assets/images/badges/other/konsool-tanmatsu/aca5c70b74.jpg
  source: "https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/"
  credit: "Hackaday / Tanmatsu press photo"
  caption: "Tanmatsu PCB top half showing components"
contact: {}
notes:
- Handheld with QWERTY keyboard, dual-core ESP32-P4 + ESP32-C6 wireless, LoRa mesh, 16MB flash, CATT/QWIIC expansion, CERN-OHL-P licensed; sold pre-assembled as 'Tanmatsu'.
- 'Origin story: Hackaday reports the project began as a proposed badge for the WHY2025 hacker camp (Netherlands) but split off into an independent product after disagreements between the WHY2025 organizers and Badge.Team. In a July 2026 follow-up, the reviewer explicitly states Tanmatsu and the actual WHY2025 badge "are different badges entirely" and declined to elaborate further. Because it was not the con''s official badge and is sold as a general-purpose product rather than tied to one event, event is left as "other" rather than set to why-2025.'
status: released
sources:
- kind: url
  url: https://badge.team/docs/badges/konsool/
  title: Konsool / Tanmatsu
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''Badge.team general-purpose handheld (not tied to one event)''.'
- kind: url
  url: https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
  title: A Closer Look At The Tanmatsu
  accessed: '2026-09-07'
  note: 'Chip breakdown (ESP32-P4, ESP32-C6, LoRa module, CH32), display size/resolution, LED placement, WHY2025 origin story, image URLs.'
- kind: url
  url: https://hackaday.com/2026/07/01/review-the-tanmatsu-a-year-on/
  title: 'Review: The Tanmatsu, A Year On'
  accessed: '2026-09-07'
  note: 'Confirms it is still commercially available a year later at EUR 99, confirms open-source status and repos, and confirms Tanmatsu is not the same as the WHY2025 badge.'
- kind: url
  url: https://nicolaielectronics.nl/blog/2025/01/06/tanmatsu-can-now-be-pre-ordered/
  title: Tanmatsu can now be pre-ordered
  accessed: '2026-09-07'
  note: 'Pricing (EUR 99.17 / EUR 120 incl. VAT), preorder mechanics, launcher/AppFS firmware background.'
- kind: url
  url: https://www.cnx-software.com/2025/01/10/tanmatsu-handheld-terminal-features-esp32-p4-risc-v-mcu-qwerty-keyboard-wifi-bluetooth-802-15-4-and-lora-connectivity/
  title: Tanmatsu handheld terminal
  accessed: '2026-09-07'
  note: 'Confirms connectivity list (wifi, BLE, 802.15.4/zigbee, LoRa), USB OTG, microSD, CATT/QWIIC expansion ports.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts confirmed across the maker''s own badge.team page, Nicolai Electronics'' own blog, and independent press (Hackaday, CNX Software) that agree closely. Not confirmed: LED count/type, battery spec (reviews mention USB-C power but not a battery capacity figure so left null rather than guessed), total units made, and total sales/current stock. Event intentionally left as "other": Tanmatsu began as a WHY2025 badge proposal but the maker states on record it is a distinct product from the actual WHY2025 badge, so it isn''t recorded as that con''s badge.'
last_modified_date: '2026-09-07'
---

The Konsool is an open-source handheld computer design from Badge.Team, the Dutch collective behind many European hacker-camp badges. Sold pre-assembled by Nicolai Electronics as the "Tanmatsu" ("terminal" in Japanese), it pairs a dual-core ESP32-P4 RISC-V application processor with an ESP32-C6 for wireless (wifi, Bluetooth LE, 802.15.4/Zigbee) and an onboard LoRa module for mesh networking. The device is built as a PCB-and-3D-printed-shell sandwich with a silicone QWERTY keyboard on the front face beneath a 3.97" 800x480 MIPI DSI display running at 60Hz, plus addressable LEDs next to the screen, a speaker, a 3.5mm audio jack, and expansion via Qwiic, PMOD, and SAO connectors.

The project's roots are tangled with WHY2025: Hackaday reports it began as a proposed badge for that Dutch hacker camp but broke away into an independent commercial product after a falling-out between the camp's organizers and Badge.Team. A year-later Hackaday review directly asked about the resemblance to the eventual WHY2025 badge (both use the same ESP32-P4/C6 combination) and the reviewer stated only that "they are different badges entirely," declining to say more. Because of that, this entry treats Tanmatsu as a general-purpose Badge.Team product rather than as any specific con's badge.

Tanmatsu first went up for preorder in January 2025 at EUR 99.17 (EUR 120 with EU VAT included), with Nicolai Electronics handling assembly, regulatory testing, and fulfillment while the underlying Konsool hardware and firmware remain open source under CERN-OHL-P. As of a July 2026 follow-up review it was still commercially available at the same roughly EUR 99 price point, with US warehouse distribution reportedly planned to help with import tariffs for American buyers.

## Make your own

Hardware design files (schematics as PDF, CERN-OHL-P licensed) live in the `Nicolai-Electronics/tanmatsu-hardware` GitHub repository; firmware components, including the AppFS launcher system and terminal emulator, are published across the `badgeteam` GitHub organization and the ESP Component Registry.
