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
summary: A hackable handheld palmtop computer with a QWERTY keyboard and 800x480 display, built around an ESP32-P4 application processor. "Konsool" is the open-source design name; "Tanmatsu" is the pre-assembled product Nicolai Electronics sells.
functions: 'General-purpose hacker terminal: runs a launcher firmware that loads multiple apps (terminal emulator, mesh messaging, camera app, games), plus LoRa/Meshtastic-style mesh communication.'
look:
  colors:
  - black
  - white
  - blue
  shape: rectangle
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: ESP32-P4 (dual-core RISC-V, up to 400MHz) + ESP32-C6 (wifi/BLE/802.15.4 co-processor) + CH32 (keyboard/housekeeping)
  leds:
    count: null
    type: null
    note: Addressable LEDs on the front of the board next to the screen (count not stated).
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
  price: EUR 99.17 (excl. EU VAT) / EUR 120 (incl. VAT)
  price_usd: 102.0
  quantity: ''
  availability: available
  availability_note: Still listed for sale as of a July 2026 Hackaday review; a year into production.
  distribution:
  - preorder
  - purchase
  where: Preordered/purchased pre-assembled from Nicolai Electronics' webshop; the underlying "Konsool" design is open hardware anyone can build.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Nicolai-Electronics/tanmatsu-hardware
  firmware_url: https://github.com/badgeteam
  eda_tool: null
  license: CERN-OHL-P
  notes: Mechanical, electronics, and firmware repos are public under Badge.Team / Nicolai-Electronics GitHub orgs.
links:
- label: badge.team/docs/badges/konsool
  url: https://badge.team/docs/badges/konsool/
  kind: website
  archived: https://web.archive.org/web/20260701215951/https://badge.team/docs/badges/konsool/
- label: badge.team/docs/badges/konsool/konsool-logo.svg
  url: https://badge.team/docs/badges/konsool/konsool-logo.svg
  kind: website
  archived: https://web.archive.org/web/20260701220056/https://badge.team/docs/badges/konsool/konsool-logo.svg
- label: badge.team/docs/badges/konsool/konsool_mascots.svg
  url: https://badge.team/docs/badges/konsool/konsool_mascots.svg
  kind: website
  archived: https://web.archive.org/web/20260701220056/https://badge.team/docs/badges/konsool/konsool_mascots.svg
- label: 'Hackaday: A Closer Look At The Tanmatsu'
  url: https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
  kind: article
  archived: https://web.archive.org/web/20260702100247/https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
- label: 'Hackaday: Review, The Tanmatsu, A Year On'
  url: https://hackaday.com/2026/07/01/review-the-tanmatsu-a-year-on/
  kind: article
  archived: https://web.archive.org/web/20260806015238/https://hackaday.com/2026/07/01/review-the-tanmatsu-a-year-on/
- label: 'Nicolai Electronics: Tanmatsu can now be pre-ordered'
  url: https://nicolaielectronics.nl/blog/2025/01/06/tanmatsu-can-now-be-pre-ordered/
  kind: website
  archived: https://web.archive.org/web/20260418065823/https://nicolaielectronics.nl/blog/2025/01/06/tanmatsu-can-now-be-pre-ordered/
- label: 'CNX Software: Tanmatsu handheld terminal'
  url: https://www.cnx-software.com/2025/01/10/tanmatsu-handheld-terminal-features-esp32-p4-risc-v-mcu-qwerty-keyboard-wifi-bluetooth-802-15-4-and-lora-connectivity/
  kind: article
  archived: https://web.archive.org/web/20260607224727/https://www.cnx-software.com/2025/01/10/tanmatsu-handheld-terminal-features-esp32-p4-risc-v-mcu-qwerty-keyboard-wifi-bluetooth-802-15-4-and-lora-connectivity/
- label: 'GitHub: tanmatsu-hardware'
  url: https://github.com/Nicolai-Electronics/tanmatsu-hardware
  kind: repo
  archived: https://web.archive.org/web/20260301070911/https://github.com/Nicolai-Electronics/tanmatsu-hardware
- label: 'GitHub: badgeteam org'
  url: https://github.com/badgeteam
  kind: repo
  archived: https://web.archive.org/web/20260513082619/https://github.com/badgeteam
- label: media.ccc.de/v/2025-188-tanmatsu-why2025-badge-pcb-design
  url: https://media.ccc.de/v/2025-188-tanmatsu-why2025-badge-pcb-design
  kind: video
- label: Tanmatsu — Nicolai Electronics
  url: https://nicolaielectronics.nl/tanmatsu/
  kind: website
- label: Tanmatsu documentation — specifications
  url: https://docs.tanmatsu.cloud/hardware/specifications/
  kind: doc
images:
- file: assets/images/badges/other/konsool-tanmatsu/9d3aade5e1.jpg
  source: https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
  credit: Hackaday / Tanmatsu press photo
  caption: Tanmatsu handheld held in a hand, showing the QWERTY keyboard and screen
  archived: https://web.archive.org/web/20260702100247/https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
- file: assets/images/badges/other/konsool-tanmatsu/aca5c70b74.jpg
  source: https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
  credit: Hackaday / Tanmatsu press photo
  caption: Tanmatsu PCB top half showing components
  archived: https://web.archive.org/web/20260702100247/https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
- file: assets/images/badges/other/konsool-tanmatsu/77501b01e4.jpg
  source: https://nicolaielectronics.nl/tanmatsu/
  credit: Nicolai Electronics
  caption: Tanmatsu handheld terminal device
contact: {}
notes:
- Handheld with QWERTY keyboard, dual-core ESP32-P4 + ESP32-C6 wireless, LoRa mesh, 16MB flash, CATT/QWIIC expansion, CERN-OHL-P licensed; sold pre-assembled as 'Tanmatsu'.
- 'Origin story: Hackaday reports the project began as a proposed badge for the WHY2025 hacker camp (Netherlands) but split off into an independent product after disagreements between the WHY2025 organizers and Badge.Team. In a July 2026 follow-up, the reviewer explicitly states Tanmatsu and the actual WHY2025 badge "are different badges entirely" and declined to elaborate further. Because it was not the con''s official badge and is sold as a general-purpose product rather than tied to one event, event is left as "other" rather than set to why-2025.'
- Spotted by a research agent while working on another entry; not yet researched.
- Sweep's title was "Tanmatsu (WHY2025 badge PCB design)", taken from the media.ccc.de talk title; the maker calls the device simply "Tanmatsu".
- 'DUPLICATE: this is the same device already covered at other/konsool-tanmatsu.md ("Konsool / Tanmatsu"). See duplicate_of in the research report.'
status: released
sources:
- kind: url
  url: https://badge.team/docs/badges/konsool/
  title: Konsool / Tanmatsu
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''Badge.team general-purpose handheld (not tied to one event)''.'
  archived: https://web.archive.org/web/20260701215951/https://badge.team/docs/badges/konsool/
- kind: url
  url: https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
  title: A Closer Look At The Tanmatsu
  accessed: '2026-09-07'
  note: Chip breakdown (ESP32-P4, ESP32-C6, LoRa module, CH32), display size/resolution, LED placement, WHY2025 origin story, image URLs.
  archived: https://web.archive.org/web/20260702100247/https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
- kind: url
  url: https://hackaday.com/2026/07/01/review-the-tanmatsu-a-year-on/
  title: 'Review: The Tanmatsu, A Year On'
  accessed: '2026-09-07'
  note: Confirms it is still commercially available a year later at EUR 99, confirms open-source status and repos, and confirms Tanmatsu is not the same as the WHY2025 badge.
  archived: https://web.archive.org/web/20260806015238/https://hackaday.com/2026/07/01/review-the-tanmatsu-a-year-on/
- kind: url
  url: https://nicolaielectronics.nl/blog/2025/01/06/tanmatsu-can-now-be-pre-ordered/
  title: Tanmatsu can now be pre-ordered
  accessed: '2026-09-07'
  note: Pricing (EUR 99.17 / EUR 120 incl. VAT), preorder mechanics, launcher/AppFS firmware background.
  archived: https://web.archive.org/web/20260418065823/https://nicolaielectronics.nl/blog/2025/01/06/tanmatsu-can-now-be-pre-ordered/
- kind: url
  url: https://www.cnx-software.com/2025/01/10/tanmatsu-handheld-terminal-features-esp32-p4-risc-v-mcu-qwerty-keyboard-wifi-bluetooth-802-15-4-and-lora-connectivity/
  title: Tanmatsu handheld terminal
  accessed: '2026-09-07'
  note: Confirms connectivity list (wifi, BLE, 802.15.4/zigbee, LoRa), USB OTG, microSD, CATT/QWIIC expansion ports.
  archived: https://web.archive.org/web/20260607224727/https://www.cnx-software.com/2025/01/10/tanmatsu-handheld-terminal-features-esp32-p4-risc-v-mcu-qwerty-keyboard-wifi-bluetooth-802-15-4-and-lora-connectivity/
- kind: url
  url: https://media.ccc.de/v/2025-188-tanmatsu-why2025-badge-pcb-design
  title: Tanmatsu (WHY2025 badge PCB design)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://nicolaielectronics.nl/tanmatsu/
  title: Tanmatsu — Nicolai Electronics
  accessed: '2026-09-10'
  note: Maker's product page; MCU, display, connectivity, price, inputs.
- kind: url
  url: https://badge.team/docs/badges/why2025/
  title: badge.team's resignation letter from WHY2025 Team:Badge
  accessed: '2026-09-10'
  note: Primary-source confirmation that badge.team resigned from the official WHY2025 badge project.
- kind: url
  url: https://hackaday.com/2025/08/12/when-a-badge-misses-the-mark-why-2025/
  title: The WHY 2025 Badge And Its 18650s
  accessed: '2026-09-10'
  note: Confirms a different team ultimately built the actual WHY2025 badge after badge.team's exit.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts confirmed across the maker''s own badge.team page, Nicolai Electronics'' own blog, and independent press (Hackaday, CNX Software) that agree closely. Not confirmed: LED count/type, battery spec (reviews mention USB-C power but not a battery capacity figure so left null rather than guessed), total units made, and total sales/current stock. Event intentionally left as "other": Tanmatsu began as a WHY2025 badge proposal but the maker states on record it is a distinct product from the actual WHY2025 badge, so it isn''t recorded as that con''s badge. Merged with duplicate entry ''Tanmatsu'' (why-2025-tanmatsu-why2025-badge-pcb-design).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/why-2025/tanmatsu-why2025-badge-pcb-design/
model:
  file: assets/models/other/konsool-tanmatsu.glb
  method: gerber
  source_file: tanmatsu.kicad_pcb
  generated: '2026-09-10'
  bytes: 378756
  size_mm:
  - 114.9
  - 129.9
---

The Konsool is an open-source handheld computer design from Badge.Team, the Dutch collective behind many European hacker-camp badges. Sold pre-assembled by Nicolai Electronics as the "Tanmatsu" ("terminal" in Japanese), it pairs a dual-core ESP32-P4 RISC-V application processor with an ESP32-C6 for wireless (wifi, Bluetooth LE, 802.15.4/Zigbee) and an onboard LoRa module for mesh networking. The device is built as a PCB-and-3D-printed-shell sandwich with a silicone QWERTY keyboard on the front face beneath a 3.97" 800x480 MIPI DSI display running at 60Hz, plus addressable LEDs next to the screen, a speaker, a 3.5mm audio jack, and expansion via Qwiic, PMOD, and SAO connectors.

The project's roots are tangled with WHY2025: Hackaday reports it began as a proposed badge for that Dutch hacker camp but broke away into an independent commercial product after a falling-out between the camp's organizers and Badge.Team. A year-later Hackaday review directly asked about the resemblance to the eventual WHY2025 badge (both use the same ESP32-P4/C6 combination) and the reviewer stated only that "they are different badges entirely," declining to say more. Because of that, this entry treats Tanmatsu as a general-purpose Badge.Team product rather than as any specific con's badge.

Tanmatsu first went up for preorder in January 2025 at EUR 99.17 (EUR 120 with EU VAT included), with Nicolai Electronics handling assembly, regulatory testing, and fulfillment while the underlying Konsool hardware and firmware remain open source under CERN-OHL-P. As of a July 2026 follow-up review it was still commercially available at the same roughly EUR 99 price point, with US warehouse distribution reportedly planned to help with import tariffs for American buyers.

## Make your own

Hardware design files (schematics as PDF, CERN-OHL-P licensed) live in the `Nicolai-Electronics/tanmatsu-hardware` GitHub repository; firmware components, including the AppFS launcher system and terminal emulator, are published across the `badgeteam` GitHub organization and the ESP Component Registry.

## Notes merged from the duplicate entry "Tanmatsu"

Tanmatsu is a handheld "pocket terminal" built around Espressif's ESP32-P4 application processor (dual-core RISC-V, 768 KB SRAM, 32 MB PSRAM) paired with an ESP32-C6 radio co-processor for Wi-Fi 6, Bluetooth LE 5, and Thread/Zigbee. It has an 800x480 MIPI DSI color LCD, a metal-dome QWERTY keyboard, a LoRa radio (868/915 MHz or 433 MHz variants), and expansion via QWIIC, PMOD, and SAO connectors plus swappable internal "personality modules."

The device traces back to badge.team, the Dutch collective behind many European congress badges, and was originally being developed as the badge for WHY2025 ("What Hackers Yearn"). In early 2025, badge.team's core team publicly resigned from the WHY2025 Team:Badge project over a dispute with the event organizers and IFCAT, splitting Tanmatsu off from the WHY2025 badge program. Renze Nicolai continued the hardware independently through Nicolai Electronics, which now sells assembled Tanmatsu units directly (around €120) with an ESP-IDF-based launcher firmware and OTA update support. The badge that WHY2025 attendees actually received in August 2025 was a separate device built by a different team, and drew its own coverage for battery-safety issues with its 18650 cells.

This entry was created from a media.ccc.de recording of a HackerHotel 2025 talk by Renze Nicolai and Paul Honig about the Tanmatsu PCB design process. The device itself is already documented in this archive under `other/konsool-tanmatsu.md`.
