---
title: Darknet-NG 14 badge levels 1, 2 &3
id: dc33-darknet-ng-14-badge-levels-1-2-3
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Darknet-NG
  url: https://darknet-ng.network/
summary: A DIY, buy-your-own-parts Meshtastic mesh-networking badge from Darknet-NG, offered as three build paths of increasing difficulty for DEF CON 33.
functions: Level 1 is an easy Meshtastic starter build on a Heltec V3 board, flashed with DEF CON 33 firmware. Level 2 is a solderless breadboard build on a Seeed Xiao ESP32-S3 with a Wio-SX1262 LoRa module. Level 3 is the same Xiao ESP32-S3 / SX1262 hardware fully soldered into a permanent build. All three join the same LoRa mesh for direct peer-to-peer messaging between agents without cell service or internet, reportedly over several miles line-of-sight.
look:
  colors: []
  shape: null
  themes:
  - radio
  - privacy
  - security
  - kit
tech:
  mcu: ESP32-S3 (Seeed Xiao ESP32-S3, Levels 2/3); Heltec V3 (ESP32, Level 1)
  leds: null
  display: 0.96" OLED I2C (Levels 2/3)
  connectivity:
  - lora
  - gps
  battery: 3.7V LiPo, Micro JST 1.25 connector (Levels 2/3); Heltec V3 onboard battery support (Level 1)
  sao_version: null
get_one:
  price: 'parts kit, buy-your-own: Xiao ESP32S3 & Wio-SX1262 (US915 MHz) ~$9.99 + battery ~$9-24 + breadboard ~$13.59 + OLED ~$7-12 + optional GPS ~$17.88'
  price_usd: null
  quantity: not a fixed production run; attendee-sourced DIY parts kit
  availability: unknown
  distribution:
  - kit
  where: Attendees bought their own parts (Seeed Studio, Amazon, Rokland) following the maker's build guide at darknet-ng.network/badge/; a discount code (DARKNETNG-5) applied at Rokland.
make_your_own:
  open_source: partial
  hardware_url: https://darknet-ng.network/badge/
  firmware_url: null
  eda_tool: null
  notes: Uses off-the-shelf boards (Heltec V3; Seeed Xiao ESP32-S3 + Wio-SX1262) running stock Meshtastic firmware rather than custom hardware or firmware; no Gerbers or repo published, only a parts list and build guide.
links:
- label: darknet-ng.network/badge
  url: https://darknet-ng.network/badge/
  kind: website
  archived: https://web.archive.org/web/20260821062747/https://darknet-ng.network/badge/
- label: Darknet-NG 14 DIY Badge Level 2 (build page)
  url: https://darknet-ng.network/darknet-ng-14-diy-badge-level-2/
  kind: doc
  archived: https://web.archive.org/web/20260821062758/https://darknet-ng.network/darknet-ng-14-diy-badge-level-2/
- label: Darknet-NG 14 DIY Badge Level 3 (build page)
  url: https://darknet-ng.network/darknet-ng-14-diy-badge-level-3/
  kind: doc
  archived: https://web.archive.org/web/20260821062758/https://darknet-ng.network/darknet-ng-14-diy-badge-level-3/
images:
- file: assets/images/badges/dc33/darknet-ng-14-badge-levels-1-2-3/f57d489851.jpg
  source: https://darknet-ng.network/badge/
  credit: Darknet-NG Operatives
  caption: Darknet-NG 14 badge build photo
  archived: https://web.archive.org/web/20260821062747/https://darknet-ng.network/badge/
- file: assets/images/badges/dc33/darknet-ng-14-badge-levels-1-2-3/7328d9052f.jpg
  source: https://darknet-ng.network/badge/
  credit: Darknet-NG Operatives
  caption: Darknet-NG 14 badge components/build
  archived: https://web.archive.org/web/20260821062747/https://darknet-ng.network/badge/
contact:
  emails:
  - thegaterbyte@gmail.com
notes:
- This is not only meant to be used at defcon, but as a means of mesh network communication within your local city when you go back home. There will also be a talk about it, check hacker tracker for Darknet-NG.
status: released
sources:
- kind: sheet
  event: dc33
  row: 37
  updated: 7/31/2025 22:09:34
- kind: url
  url: https://darknet-ng.network/badge/
  title: 'Darknet-NG 14 Badge: Signal in the Noise'
  accessed: '2026-09-06'
  note: Live site now shows DC34 content; used the 2025-07-18 Wayback Machine snapshot (20250803111808) for the DC33-era text describing all three badge levels.
  archived: https://web.archive.org/web/20260821062747/https://darknet-ng.network/badge/
- kind: url
  url: https://darknet-ng.network/darknet-ng-14-diy-badge-level-3/
  title: Darknet-NG 14 DIY Badge Level 3
  accessed: '2026-09-06'
  note: Wayback snapshot (20250803111839) of the Level 3 build/parts page; gave the SX1262/US915 LoRa module, OLED, battery, and GPS parts list. Note the page's body text is a copy-paste of the Level 2 description despite the Level 3 title.
  archived: https://web.archive.org/web/20260821062758/https://darknet-ng.network/darknet-ng-14-diy-badge-level-3/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The live darknet-ng.network/badge/ page has since been overwritten with DEF CON 34 content (a separate nRF52840/SX1262 "SMAO" product, tracked as its own entry dc34-darknet-ng-smao); all DC33-specific facts here come from Wayback Machine snapshots of the badge and Level 3 pages taken 2025-08-03, close to the original 2025-07-18 posting. No dedicated Level 1 build page or Level 2 parts-list snapshot was found (the Level 2 page snapshot mirrors the Level 3 text), so exact Level 1 LED/quantity/price details and a firmware repo link could not be confirmed and are left empty. No GitHub repo or Gerbers were found; Meshtastic itself is open source but Darknet-NG did not publish custom hardware/firmware files for this build.
last_modified_date: '2026-09-06'
---

The Darknet-NG 14 badge was DEF CON 33's entry in an ongoing series of DIY Meshtastic-based mesh-networking badges from the Darknet-NG group, posted to their site on July 18, 2025 as "Signal in the Noise." Rather than shipping a single fixed board, Darknet-NG offered three parallel build paths pitched at different skill levels: Level 1 reused the Heltec V3 board from the previous year's badge with updated DEF CON 33 Meshtastic firmware for the fastest path onto the mesh; Level 2 built the same mesh node on a solderless breadboard around a Seeed Xiao ESP32-S3 and a Wio-SX1262 LoRa module, framed as the cheapest way in; and Level 3 used the identical Xiao ESP32-S3/SX1262 hardware but fully soldered for a more durable, permanent build. All three ran Meshtastic to give attendees direct peer-to-peer LoRa messaging without relying on cell service or internet.

This was a buy-your-own-parts kit rather than a produced run: the site listed specific parts and vendors (Seeed Studio for the mainboard/LoRa combo, Amazon and Rokland for batteries, generic solderless breadboards, and a 0.96" OLED I2C display, with an optional GPS add-on), and attendees sourced and assembled their own units following the maker's guide, with help available at the con and on Discord. The project frames itself explicitly as more than a one-off con badge: the same node is meant to keep working as a general-purpose mesh radio back home.

## Make your own

Follow the build guide at darknet-ng.network/badge/, which links out to level-specific instruction pages. For Levels 2 and 3, order a Seeed Xiao ESP32-S3 + Wio-SX1262 (US915 MHz) kit, a 3.7V LiPo battery with a Micro JST 1.25 connector, a 0.96" OLED I2C display, and (for Level 2) a solderless breadboard with jumper wires; Level 3 uses the same parts soldered together instead. Level 1 instead reuses a Heltec V3 board flashed with the DEF CON 33 Meshtastic firmware. No custom Gerbers, schematics, or firmware repo were published for this build; it relies entirely on off-the-shelf hardware and stock Meshtastic firmware.
