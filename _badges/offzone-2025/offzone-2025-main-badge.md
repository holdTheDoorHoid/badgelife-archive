---
title: OFFZONE 2025 Main Badge
id: offzone-2025-offzone-2025-main-badge
layout: badge
parent: OFFZONE 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: offzone-2025
year: 2025
makers:
- name: BI.ZONE
summary: 'The interactive badge for OFFZONE 2025, used to track conference activities and earn "offcoins" redeemable for merchandise.'
functions: 'Tracks participation in conference tasks and challenges, earning gamified points ("offcoins") that attendees exchange for merchandise; connects to a computer over USB-C and presents a COM-port interface for interacting with it.'
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: null
  leds: null
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Given to attendees of OFFZONE 2025 (Moscow, August 21-22, 2025).'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: 2025.offzone.moscow/badge-and-offcoins
  url: https://2025.offzone.moscow/badge-and-offcoins/
  kind: website
- label: bi-zone/offzone-hw (2025 add-ons)
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025
  kind: repo
  note: 'Repo has folders for the 2025 Craft.Zone add-ons (angel-and-devil, anonymous, bear, boombox, terminal) but no folder for the main badge itself.'
images:
- file: assets/images/badges/offzone-2025/offzone-2025-main-badge/a1cf43a2f6.jpg
  source: "https://2025.offzone.moscow/badge-and-offcoins/"
  credit: "BI.ZONE"
  caption: "OFFZONE 2025 main badge"
- file: assets/images/badges/offzone-2025/offzone-2025-main-badge/dd9bd9d5e2.png
  source: "https://2025.offzone.moscow/badge-and-offcoins/"
  credit: "BI.ZONE"
  caption: "OFFZONE 2025 badge component/board diagram"
contact: {}
notes:
- Interactive OFFZONE 2025 badge with auto-sensing USB-C/battery power, color-shifting LEDs, and backward-compatible add-on connectors for collectible Craft.Zone add-ons. Found by the event-year sweep, task con-phdays.
status: released
sources:
- kind: url
  url: https://2025.offzone.moscow/badge-and-offcoins/
  title: OFFZONE 2025 Main Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2025''.'
- kind: url
  url: https://2025.offzone.moscow/badge-and-offcoins/
  title: "Бейдж и офкоины - 2025.offzone.moscow"
  accessed: '2026-09-08'
  note: 'Maker page: confirms BI.ZONE as organizer/maker, dual battery/USB-C power with auto-detection, multiple LEDs, USB-C for PC connection with a COM-port interface, and a backward-compatible add-on connector for Craft.Zone add-ons. No MCU, price, quantity, or design-file info given.'
- kind: url
  url: https://bi.zone/eng/news/obyavlyaem-daty-i-mesto-provedeniya-offzone-2025/
  title: 'OFFZONE 2025: dates and venue confirmed'
  accessed: '2026-09-08'
  note: 'Confirms OFFZONE 2025 ran August 21-22, 2025 in Moscow (GOELRO), organized by BI.ZONE.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025
  title: 'bi-zone/offzone-hw at master, 2025 folder'
  accessed: '2026-09-08'
  note: 'Checked for main-badge design files; only Craft.Zone add-on folders (angel-and-devil, anonymous, bear, boombox, terminal) exist for 2025, no main-badge hardware published.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed the badge exists and is described on BI.ZONE''s own OFFZONE 2025 page. Could not find the MCU/chip, LED count/type, exact quantity made, price, or any published hardware/firmware files for the main badge specifically (the bi-zone/offzone-hw repo publishes the 2025 Craft.Zone add-ons but not the main badge). No English-language coverage found beyond BI.ZONE''s own site and a general event wrap-up.'
last_modified_date: '2026-09-08'
---

The OFFZONE 2025 main badge is the interactive conference badge handed to attendees of BI.ZONE's OFFZONE cybersecurity conference, held August 21-22, 2025 in Moscow. Like prior years' badges, it doubles as the interface for the event's gamified track: attendees earn "offcoins" by completing tasks and challenges around the venue, which can then be exchanged for merchandise.

The badge auto-detects and switches between battery and USB-C power, and connects to a computer via USB-C, presenting itself as a COM-port device rather than a traditional file-transfer peripheral. It carries multiple LEDs described by BI.ZONE as lighting up and shimmering, and includes an add-on connector that is backward-compatible with earlier years' connectors, letting it accept the collectible Craft.Zone add-ons made for OFFZONE 2025 (Angel and Devil, Anonymous, Bear, Boombox, and Terminal).

BI.ZONE's own hardware repository publishes source files for the 2025 Craft.Zone add-ons but, as of this research, does not include a folder for the main badge itself, so its schematic, firmware, and BOM appear unpublished. No MCU, exact LED count/type, price, or production quantity is stated on the maker's page or in the repo.
