---
title: IDK NFC Badge
id: dc33-p0ns-idk-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: p0ns/idk
  url: https://idk.bz
summary: A customizable electronic badge built around an ESP32-C3 and an ST25DV NFC chip that shares one of four programmable URLs when tapped, with rainbow LED animations on scan.
functions: Cycles through 4 hardcoded URLs (via button press, NFC scan, or a saved state on power-up) written to an NFC tag that phones can read by tapping the badge; two RGB LEDs play a rainbow "pride" animation for 2.5 seconds on each scan, with a button to make the lighting stay on permanently. The board is modular and still works partially assembled, as an NFC field detector (LEDs only) or a passive NFC tag (NFC chip only).
look:
  colors: []
  shape: null
  themes:
  - nfc
  - hardware tool
tech:
  mcu: ESP32-C3
  leds:
    count: 2
    type: SK6812-SIDE-4020
    note: side-mount RGB LEDs driven with FastLED's "pride" rainbow effect; plus a plain red LED that lights when an NFC field is present.
  display: none
  connectivity:
  - nfc
  - i2c
  battery: LiPo (rechargeable via PH2.0 connector and charging circuit)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://gitlab.com/idkidkidk/idk-nfc-esp32-c3
  firmware_url: https://gitlab.com/idkidkidk/idk-nfc-esp32-c3
  eda_tool: null
  notes: Maker's site says schematic/board files and Arduino source are on GitLab; page did not state a license.
links:
- label: idk.bz
  url: https://idk.bz
  kind: website
  archived: https://web.archive.org/web/20251128205942/https://idk.bz/
- label: idk.bz/idk-nfc (project writeup)
  url: https://idk.bz/idk-nfc/
  kind: article
- label: GitLab - idk-nfc-esp32-c3
  url: https://gitlab.com/idkidkidk/idk-nfc-esp32-c3
  kind: repo
- label: twitter.com/p0ns
  url: https://twitter.com/p0ns
  kind: social
- label: defcon.social/p0ns
  url: https://defcon.social/p0ns
  kind: social
images:
- file: assets/images/badges/dc33/p0ns-idk-listed-for-def-con-33-no-details/effae759e7.jpg
  source: https://idk.bz/idk-nfc/
  credit: p0ns/idk
  caption: IDK NFC badge PCB, front
- file: assets/images/badges/dc33/p0ns-idk-listed-for-def-con-33-no-details/5c5b811a7e.jpg
  source: https://idk.bz/idk-nfc/
  credit: p0ns/idk
  caption: IDK NFC badge schematic
contact: {}
notes:
- Sheet listed only the maker ("p0ns/idk") for DEF CON 33 with no badge title; the title above was recovered from the maker's site.
status: released
sources:
- kind: sheet
  event: dc33
  row: 65
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://idk.bz
  title: IDK (p0ns's site)
  accessed: '2026-09-06'
  note: Home page lists "IDK NFC badge" (May 17, 2025) as the featured project, by p0ns, alongside prior years' DC31 SAO and DC32 IDK SAO.
  archived: https://web.archive.org/web/20251128205942/https://idk.bz/
- kind: url
  url: https://idk.bz/idk-nfc/
  title: IDK NFC badge - IDK
  accessed: '2026-09-06'
  note: Full project writeup - features, schematic, firmware description, BOM notes, and link to the GitLab repo.
- kind: url
  url: https://gitlab.com/idkidkidk/idk-nfc-esp32-c3
  title: idk-nfc-esp32-c3 (GitLab)
  accessed: '2026-09-06'
  note: Confirms the repo exists, created May 17, 2025 (same date as the blog post); could not read file contents or license via fetch.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The community sheet only listed the maker as expected for DEF CON 33, with no badge name. p0ns/idk's own site (idk.bz) follows a clear yearly pattern - a "DEFCON31 SAO" post, an "IDK SAO" post dated May 16, 2024 for DC32, and an "IDK NFC badge" post dated May 17, 2025. By that pattern the IDK NFC badge is almost certainly what they brought to DEF CON 33, but no page explicitly says "DEF CON 33" - hence medium rather than high confidence. Same maker previously listed with several other stub titles for DC32 (420 Bud SAO, Battery SAO, Disappointing Badge, IDK SAO) - those are separate, untouched entries. Could not find price, quantity, or distribution details (no storefront found); left those fields empty. Could not read the GitLab repo's README or confirm its license via automated fetch.
last_modified_date: '2026-09-06'
---

The IDK NFC badge is p0ns/idk's 2025 entry in a run of yearly DEF CON projects that also includes a "DEFCON31 SAO" and 2024's "IDK SAO." Built around an ESP32-C3 paired with an ST25DV NFC chip, it works as a tap-to-share badge: touching a phone to it opens one of four hardcoded URLs (by default idk.bz, lonelyhackers.club, p0ns.org, and a YouTube link), which the wearer can cycle through with a button press or let the badge auto-advance on every scan. Two SK6812 side-mount RGB LEDs play a two-and-a-half-second rainbow "pride" animation each time the tag is read, with a second button to leave the lighting on continuously.

The board is deliberately modular - people who received an unpopulated or partially populated unit could still use it as a plain NFC field detector (LEDs only) or a passive NFC tag (chip only) without the microcontroller. Firmware is written in Arduino using Wire.h, ST25DVSensor.h, Preferences.h, and FastLED.h, and the source plus board files are published on GitLab for anyone who wants to build their own.

The community badge sheet's DEF CON 33 row only recorded the maker's handle with no badge title, so the title, description, and specs above come entirely from the maker's own site rather than from the sheet.

## Make your own

Schematic, board layout, and Arduino firmware are on GitLab at [idkidkidk/idk-nfc-esp32-c3](https://gitlab.com/idkidkidk/idk-nfc-esp32-c3). The maker's parts list: an ESP32-C3-SuperMini module, an ST25DV NFC chip with its passive components, SK6812-SIDE-4020 RGB LEDs, a plain red LED for NFC-field indication, two tactile buttons, and (optionally) a small LiPo cell with a PH2.0 connector and charge circuit for a rechargeable build.
