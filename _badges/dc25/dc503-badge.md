---
title: DC503 Wagon Party Badge
id: dc25-dc503-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: Joe Fitz
  url: https://twitter.com/securelyfitz
- name: PDX Badgers / DC503 (Portland)
summary: A wagon-shaped party badge made for the DC503 crew's DEF CON 25 party in 2017, playing on the "Oregon Trail" theme with a small OLED game.
functions: Runs an "Oregon Trail"-parody mini-game on its OLED screen, advertises itself over BLE as "503WAGON", and its board text invites people to follow it to the party's website.
look:
  colors:
  - black
  - wood
  shape: wagon
  themes:
  - pop culture
tech:
  mcu: nRF52832 (Rigado/SparkFun breakout)
  leds:
    count: 4
    type: discrete
    note: Four LEDs in the upper-left corner of the board.
  display: 0.96" OLED (SSD1306, 128x64)
  connectivity:
  - ble
  battery: coin cell
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '100'
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of the DC503 party at DEF CON 25, produced by four team members with professional assembly.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/pdxbadgers/wagonparty
  eda_tool: null
links:
- label: hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  kind: article
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
- label: pdxbadgers/wagonparty
  url: https://github.com/pdxbadgers/wagonparty
  kind: repo
images:
- file: assets/images/badges/dc25/dc503-badge/cc034017cc.jpg
  source: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  credit: Hackaday
  caption: DC503 Wagon Party badge, front (OLED display and BLE module)
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
- file: assets/images/badges/dc25/dc503-badge/3885cfa912.jpg
  source: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  credit: Hackaday
  caption: DC503 Wagon Party badge, back
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
contact: {}
notes:
- Unofficial DEF CON 25 regional badge (100 units) with a Rigado BLE module and a USB-to-serial lanyard, from throws503.party. Found by the event-year sweep, task dc25-saos.
- The event-year sweep's original title, "DC503 Badge," was Hackaday's generic label for the item; the maker's own repo names the project "wagon party," and the board itself reads "The 503 rail!" — so the title here follows that.
status: released
sources:
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: DC503 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc25-saos); event read as ''dc25''.'
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: All The Hardware Badges Of DEF CON 25
  accessed: '2026-09-08'
  note: Confirmed maker (Joe Fitz), Rigado module, coin cell power, USB-to-serial lanyard, 100 units made by a four-person team; source of the two badge photos.
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
- kind: url
  url: https://github.com/pdxbadgers/wagonparty
  title: pdxbadgers/wagonparty
  accessed: '2026-09-08'
  note: Maker's firmware repo. Confirms nRF52832 (SparkFun breakout), SSD1306 OLED 128x64, BLE, and the wagon-wheel button used to enter reprogramming mode. No hardware/Gerber files in the repo, only firmware and sprite art.
- kind: url
  url: https://badge.gallery/series/dc503
  title: DC503 · Hacker Con Badges - badge.gallery
  accessed: '2026-09-08'
  note: Third-party catalog page; used only to confirm this 2017 item is distinct from the DC503 group's other-year badges (2015 bicycle badge, 2018 VIP Banglet, 2019 5ohBEE pager), not as a primary source.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Photo confirms the badge itself: a laser-cut wagon shape with wooden wheels, "The 503 rail!" text, and an OLED showing an Oregon-Trail-style wagon game, matching the repo firmware. Price and exact battery type (e.g. CR2032 vs CR2025) are not stated anywhere found; availability beyond the 2017 party is unknown. The DC503 group made other, different badges in other years (dc23-dc503-badge for 2015, and others for DC26/DC27) — this entry is specifically the 2017 wagon-shaped one.'
last_modified_date: '2026-09-08'
---

The DC503 Wagon Party Badge was made for the 2017 edition of the DC503 party, a privately-run DEF CON 25 side event thrown by Portland, Oregon's DC503 hacker group (aka PDX Badgers, tied to CTRL-H Hackerspace). Designer Joe Fitz and a three-person team had 100 of the badges professionally assembled. The board is laser-cut into a covered-wagon silhouette with wooden spoked wheels, reads "The 503 rail!" along the body, and invites the wearer to "follow me to http://503.party!"

Electronically it is built around an nRF52832 (via a Rigado/SparkFun breakout module) driving a 128x64 SSD1306 OLED screen, with four LEDs and Bluetooth Low Energy connectivity — the firmware advertises the badge over BLE as "503WAGON." A small onboard game riffs on the classic "Oregon Trail," and the badge could be reflashed over a 3.3V USB-to-serial cable, which doubled as a lanyard; holding the left wagon wheel's button while powering on puts it into that programming mode.

## Make your own

The firmware and sprite artwork are open source in the `pdxbadgers/wagonparty` GitHub repository. No hardware design files (schematic, Gerbers, or BOM) were found published alongside it, so a rebuild would need to reproduce the wagon-shaped PCB and the nRF52832/OLED wiring described in the README.
