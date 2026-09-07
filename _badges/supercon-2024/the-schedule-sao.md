---
title: The Schedule SAO
id: supercon-2024-the-schedule-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: 'A DS3231 real-time clock SAO with an AT24C32 EEPROM, its silkscreen laid out as a November 2024 calendar so a badge can read the stored Supercon schedule and check the time.'
functions: 'Provides real-time clock (DS3231) and 4KB EEPROM (AT24C32) storage over I2C so a host badge can read and display event schedule data along with the current time.'
look:
  colors: [blue]
  shape: rectangle
  themes: [minimalist, text]
tech:
  mcu: none
  leds: null
  display: null
  connectivity: [i2c]
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '12 PCBs'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/198229-the-schedule-sao
  url: https://hackaday.io/project/198229-the-schedule-sao
  kind: hackaday
- label: davedarko on Hackaday.io
  url: https://hackaday.io/davedarko
  kind: hackaday
- label: supercon.davedarko.com
  url: https://supercon.davedarko.com
  kind: website
images:
  - file: assets/images/badges/supercon-2024/the-schedule-sao/ad57cb0900.jpg
    source: "https://hackaday.io/project/198229-the-schedule-sao"
    credit: "davedarko"
    caption: "The Schedule SAO PCB with November 2024 calendar silkscreen"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/198229-the-schedule-sao
  title: The Schedule SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 SAO Contest entry''.'
- kind: url
  url: https://hackaday.io/project/198229-the-schedule-sao
  title: The Schedule SAO
  accessed: '2026-09-07'
  note: 'Confirmed maker (davedarko), function (DS3231 RTC + AT24C32 EEPROM adapter, SAO), Supercon 8 (2024) SAO Contest entry, 12 PCBs made via Aisler, silkscreen shows a November 2024 calendar; sourced og:image for photo.'
- kind: url
  url: https://supercon.davedarko.com
  title: 'Hackaday Supercon schedule tool'
  accessed: '2026-09-07'
  note: "Maker's companion website for exporting/reading the Supercon schedule; referenced from the project page as the schedule-data source, no additional item details."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for the Supercon 8 (2024) SAO Contest, not Supercon 2025 as originally filed under; corrected event to supercon-2024. Maker''s project page has only one log entry (Oct 17 2024) and does not state a sale price, distribution method, or whether hardware/firmware files are published, so those fields are left empty. No dedicated repo or gerber link was found.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2025/the-schedule-sao/
---

The Schedule SAO is an add-on board by Hackaday.io user davedarko, built for the Supercon 8 (2024) SAO Contest. It adapts a generic DS3231 real-time clock module, paired with an AT24C32 4KB EEPROM, onto an SAO-format board so a host badge can read the current time and pull stored event-schedule data over I2C. The silkscreen doubles as a physical calendar for November 2024, with the Supercon convention weekend picked out using bare tin pads instead of printed numbers.

The maker had 12 PCBs fabricated through Aisler (around €3 with a promotional coupon) and sourced 12 DS3231 modules from AliExpress (about €12 total), suggesting a small personal or contest-entry batch rather than a wide public release. A companion site, supercon.davedarko.com, collects and exports Hackaday Supercon and Supercon Europe schedules, which appears to be the data source the SAO is meant to read. No pricing, distribution details, or open-source hardware/firmware files were found on the project page.
