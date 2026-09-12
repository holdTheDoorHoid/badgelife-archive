---
title: SecKC DC25 Badge
id: dc25-seckc-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: SecKC (Kansas City infosec meetup)
  url: https://seckc.org/
- name: Badge Pirates (FG, RIXON, NETWORKGEEK)
  url: https://github.com/SecKC
summary: A dev-board-style hardware badge built by the Kansas City SecKC meetup for DEF CON 25, based on a SparkFun ESP32 Thing with a small OLED display and a four-way button menu.
functions: Boots to a scrollable on-device menu (built around bitmap sprites, including an animated logo) navigated with four directional buttons plus the ESP32's onboard button; broadcasts its own "SecKC_Badge" WiFi AP. Attendees extended it further, including one build turned into a rotary-dial "cellphone."
look:
  colors:
  - purple
  - white
  shape: rectangle
  themes:
  - security
  - retro computer
tech:
  mcu: ESP32 (SparkFun ESP32 Thing)
  leds:
    count: 1
    type: discrete
    note: single status LED driven by the firmware
  display: 0.96" SSD1306 OLED
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 60 (preordered as 50, ~60 built)
  availability: unknown
  distribution:
  - preorder
  - membership
  where: Distributed to SecKC members who preordered ahead of DEF CON 25 (2017); demand exceeded the run, so the group also made acrylic backup badges (see the separate SecKC Acrylic Badge entry).
make_your_own:
  open_source: true
  hardware_url: https://github.com/SecKC/Badge-DC25/tree/master/Files
  firmware_url: https://github.com/SecKC/Badge-DC25/tree/master/BadgeCode
  eda_tool: null
links:
- label: hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  kind: article
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
- label: github.com/SecKC/Badge-DC25
  url: https://github.com/SecKC/Badge-DC25
  kind: repo
- label: docs.badgepirates.com catalog
  url: https://docs.badgepirates.com/catalog/
  kind: doc
  archived: https://web.archive.org/web/20260910225903/https://docs.badgepirates.com/catalog/#help-us-fill-the-gaps
images:
- file: assets/images/badges/dc25/seckc-badge/b1f77748ea.jpg
  source: https://github.com/SecKC/Badge-DC25
  credit: SecKC / Badge Pirates
  caption: Assembled SecKC DC25 badge with OLED display lit and SparkFun ESP32 Thing module attached
- file: assets/images/badges/dc25/seckc-badge/2813c1f873.jpg
  source: https://github.com/SecKC/Badge-DC25
  credit: SecKC / Badge Pirates
  caption: Bare SecKC DC25 PCB with silkscreen art (fedora silhouette in laurel wreath, DC XXV, SECKC MMXVII) before final assembly
- file: assets/images/badges/dc25/seckc-badge/9c3e170f57.jpg
  source: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  credit: Hackaday
  caption: SecKC devboard badge, front
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
- file: assets/images/badges/dc25/seckc-badge/14699c1bea.jpg
  source: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  credit: Hackaday
  caption: SecKC devboard badge, back
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
contact: {}
notes:
- NRF-module devboard-style badge (60 units) brought to DEF CON 25 by the Kansas City SecKC group. Found by the event-year sweep, task dc25-saos.
- The original sweep note and Hackaday's article both describe this as built around an "NRF module from SparkFun," but the maker's own firmware repo (SecKC/Badge-DC25) states the platform is a SparkFun ESP32 Thing (ESP32, not an nRF part) with WiFi; the repo is treated as authoritative here.
- Sweep imported the title as "SecKC Badge"; the repo names it "The SecKC Unofficial DEF CON 25 Badge," rendered here as "SecKC DC25 Badge."
- Spotted by a research agent while working on another entry; not yet researched.
- This appears to be a duplicate of dc25-seckc-badge, which already carries fuller, sourced detail (ESP32/OLED, GitHub repo, distribution) confirmed against the same Hackaday article and the SecKC GitHub org. Left as a stub-level duplicate rather than merged, per the one-entry-per-task rule.
status: listed
sources:
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: SecKC Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc25-saos); event read as ''dc25''.'
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
- kind: url
  url: https://github.com/SecKC/Badge-DC25
  title: 'SecKC/Badge-DC25: The SecKC Unofficial DEF CON 25 Badge'
  accessed: '2026-09-08'
  note: Maker's repo; confirmed ESP32 (SparkFun ESP32 Thing) + OLED + WiFi menu firmware, gerbers, BOM, and images of the assembled badge.
- kind: url
  url: https://docs.badgepirates.com/catalog/
  title: BadgePirates Documents - Catalog
  accessed: '2026-09-08'
  note: Confirms this as the earliest public DefCon SecKC badge entry (2017, DC25); no additional price/quantity detail.
  archived: https://web.archive.org/web/20260910225903/https://docs.badgepirates.com/catalog/#help-us-fill-the-gaps
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker's own GitHub repo confirms hardware platform, firmware behavior, and provides gerbers/BOM/images, so core technical facts are solid. Price and final availability status (whether any went unsold) were not stated anywhere found. EDA tool used for the PCB is not indicated in the repo (only Gerbers/BOM are published, no schematic source). Confidence held at medium rather than high because the two secondary sources (Hackaday, the sweep) disagree with the maker on the wireless chip (nRF vs ESP32), and no maker statement on price was located. Merged with duplicate entry 'SecKC Badge (PCB devboard)' (dc25-seckc-badge-pcb-devboard).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/dc25/seckc-badge-pcb-devboard/
model:
  file: assets/models/dc25/seckc-badge.glb
  method: gerber
  source_file: Files/SecKCDC25Badge_gerber-Prod.zip
  generated: '2026-09-10'
  bytes: 127892
  size_mm:
  - 140.0
  - 95.0
---

The SecKC DC25 badge was the Kansas City SecKC meetup's hardware badge for DEF CON 25 (2017), built by a subset of the group who would go on to call themselves Badge Pirates. It's a purple PCB laid out like a dev board: a SparkFun ESP32 Thing module does the work, driving a small SSD1306 OLED that shows an animated laurel-wreath-and-fedora logo and a menu navigated with four directional buttons (plus the ESP32's onboard button). The badge also spins up its own "SecKC_Badge" WiFi access point. The group preordered 50 boards from members and ended up building around 60, but demand still outran supply, so they filled the gap with a separate run of acrylic badges (its own archive entry).

Hardware and firmware are both published on GitHub (SecKC/Badge-DC25): Gerbers, a BOM, and the Arduino sketch that drives the OLED menu and button navigation. Some attendees pushed the open design further at the con itself — Hackaday's write-up of DEF CON 25 hardware badges singles out one build that turned the badge into a functioning cellphone with a rotary dial.

One discrepancy worth flagging: both Hackaday's article and the archive's own discovery sweep describe the badge as built around "an NRF module from SparkFun," but the maker's firmware source lists the platform plainly as an ESP32 (SparkFun ESP32 Thing) with WiFi, not an nRF radio. This entry follows the maker's repo as the more authoritative source.

## Notes merged from the duplicate entry "SecKC Badge (PCB devboard)"

SecKC, the Kansas City infosec meetup, built this devboard-style badge for DEF CON 25 (2017), designing it around an nRF module from SparkFun. The group took preorders for 50 boards and ended up building around 60, but demand outstripped supply; when they couldn't get additional boards built in time, they handed out edge-lit acrylic badges as a stopgap for members who missed out on the PCB (see the separate SecKC Acrylic Badge entry).

The badge was built to be hacked on, and Hackaday's DEF CON 25 badge roundup notes that attendees took it further, with one build reworking it into a rotary-dial "cellphone."

This entry appears to describe the same physical badge as `dc25-seckc-badge`, which carries a fuller, independently-sourced write-up (SparkFun ESP32 Thing, OLED display, GitHub repo). That detail was not copied over here since it wasn't re-confirmed against this entry's own sources.
