---
title: TiDAL
id: emf-camp-2022-tidal
layout: badge
parent: EMF Camp 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: emf-camp-2022
year: 2022
makers:
- name: EMF Camp badge team
summary: 'The official EMF Camp 2022 badge: a tiny USB-C wearable with a display, joystick, motion sensor and compass, built around an ESP32-S3.'
functions: 'Runs MicroPython apps installed from an online app store ("the Hatchery"); can be programmed live over USB using a browser-based WebSerial editor at editor.badge.emfcamp.org.'
look:
  colors:
  - blue
  - white
  shape: rectangle
  themes:
  - sea
  - electronics
tech:
  mcu: ESP32-S3
  leds: null
  display: small display (size unspecified by sources)
  connectivity:
  - wifi
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: 'Given to EMF Camp 2022 attendees as their event badge; not sold separately.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/emfcamp/TiDAL-Hardware
  firmware_url: https://github.com/emfcamp/TiDAL-Firmware
  eda_tool: null
links:
- label: badge.emfcamp.org/TiDAL
  url: https://badge.emfcamp.org/TiDAL/
  kind: website
- label: developer.emfcamp.org/badge/2022-tidal
  url: https://developer.emfcamp.org/badge/2022-tidal/
  kind: website
- label: archive.org/details/emf2022-tidal-badge-guide
  url: https://archive.org/details/emf2022-tidal-badge-guide
  kind: website
- label: emfcamp/tidal-docs
  url: https://github.com/emfcamp/tidal-docs
  kind: doc
- label: emfcamp/TiDAL-Firmware
  url: https://github.com/emfcamp/TiDAL-Firmware
  kind: repo
- label: emfcamp/TiDAL-Hardware
  url: https://github.com/emfcamp/TiDAL-Hardware
  kind: repo
images:
  - file: assets/images/badges/emf-camp-2022/tidal/9035185561.jpg
    source: "https://github.com/emfcamp/tidal-docs"
    credit: "EMF Camp"
    caption: "Edge view of the TiDAL badge showing its display, joystick and buttons"
contact: {}
notes:
- Official EMF Camp 2022 badge, the badge team's first tiny-form-factor badge and first with USB-C, with an app-store/hatchery ecosystem for third-party software; not yet in the archive. Found by the event-year sweep, task emf-badges.
- Sweep imported the title as "TiDAL"; the maker's own materials also style it "TiDAL" (all-caps TiDAL with lowercase i), no change needed.
status: released
sources:
- kind: url
  url: https://badge.emfcamp.org/TiDAL/
  title: TiDAL
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-badges); event read as ''emf-camp-2022''.'
- kind: url
  url: https://developer.emfcamp.org/badge/2022-tidal/
  title: TiDAL (EMF 2022 badge) - developer.emfcamp.org
  accessed: '2026-09-08'
  note: Confirms it is the official 2022 EMF Camp badge with an app development/Hatchery ecosystem; no hardware specs given here.
- kind: url
  url: https://ia801407.us.archive.org/21/items/emf2022-tidal-badge-guide/badge%2Bflyer_djvu.txt
  title: TiDAL Badge flyer (EMF Camp 2022)
  accessed: '2026-09-08'
  note: 'Maker''s own flyer text: USB-C, display, joystick and buttons; ESP32-S3 WiFi processor, motion sensor, compass, and a security chip; A/B/FRONT buttons; two flex-cable expansion connectors; MicroPython apps via Hatchery.'
- kind: url
  url: https://github.com/emfcamp/tidal-docs
  title: emfcamp/tidal-docs README
  accessed: '2026-09-08'
  note: Confirms open documentation and links to firmware/hardware repos; source of the device edge-view image; notes on WiFi limitations.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Both hardware and firmware repos are public (TiDAL-Hardware, TiDAL-Firmware), so open_source is set to yes even though no explicit license statement was read. Display size/resolution, exact LED usage, and battery capacity are not stated in any source checked (official flyer, docs README, developer site) and are left empty rather than guessed. Price/quantity are not applicable in the normal sense: TiDAL was the included event badge for EMF Camp 2022 ticket holders, not a separately sold item, so get_one.price/quantity are left blank and availability is set to free/free_drop.'
last_modified_date: '2026-09-08'
---

TiDAL was the official badge handed to every attendee of EMF Camp 2022, the UK hacker camp. It was the badge team's first attempt at a genuinely tiny badge and their first to use USB-C, a deliberate departure from the larger, more badge.team-style boards EMF had shipped in prior years. Under a coral/wave-themed silkscreen, it packs an ESP32-S3, a small display, a joystick, three buttons (A, B, and FRONT), a motion sensor, a compass, and a security chip, plus a pair of flex-cable connectors for expansion boards.

Rather than shipping fixed firmware, TiDAL apps are written in MicroPython and distributed through an online store the team called "the Hatchery," with a browser-based WebSerial editor for live coding over USB without any local toolchain. Both the firmware and hardware design files are published on GitHub (TiDAL-Firmware and TiDAL-Hardware), continuing EMF Camp's practice of open-sourcing its badges after the event.

As with all EMF Camp badges, TiDAL was not sold as a standalone product; it came bundled with a ticket to EMF Camp 2022 and its documentation lives on alongside the team's badges going back to 2012.
