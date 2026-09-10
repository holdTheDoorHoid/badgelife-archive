---
title: Tildagon
id: emf-camp-2024-tildagon
layout: badge
parent: EMF Camp 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: emf-camp-2024
year: 2024
makers:
- name: EMF Camp badge team
  url: https://github.com/emfcamp
summary: A reusable hexagonal event badge for EMF Camp 2024, built around an ESP32-S3 with a round LCD and a "hexpansion" edge connector on each of its six sides for user-made add-ons.
functions: Runs MicroPython apps on a round LCD; extended with electronic or simple cardboard "hexpansion" modules plugged into the six edge connectors; supports over-the-air firmware updates over the camp network and USB flashing.
look:
  colors: []
  shape: hexagon
  themes:
  - hardware tool
  - wearable
tech:
  mcu: ESP32-S3
  leds: null
  display: round LCD
  connectivity:
  - wifi
  - ble
  - usb
  battery: compatible with EMF 2016/2018 badge batteries
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - membership
  where: Given to EMF Camp 2024 attendees as the event badge.
make_your_own:
  open_source: true
  hardware_url: https://github.com/emfcamp/badge-2024-hardware
  firmware_url: https://github.com/emfcamp/badge-2024-software
  eda_tool: null
links:
- label: developer.emfcamp.org/badge
  url: https://developer.emfcamp.org/badge/
  kind: website
- label: tildagon.badge.emfcamp.org
  url: https://tildagon.badge.emfcamp.org/
  kind: doc
- label: github.com/emfcamp/badge-2024-hardware
  url: https://github.com/emfcamp/badge-2024-hardware
  kind: repo
- label: github.com/emfcamp/badge-2024-software
  url: https://github.com/emfcamp/badge-2024-software
  kind: repo
images:
- file: assets/images/badges/emf-camp-2024/tildagon/324a9f965e.jpg
  source: "https://tildagon.badge.emfcamp.org/"
  credit: "EMF Camp badge team"
  caption: "Tildagon badge lit by RGB LEDs in the dark"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Duplicate of another entry for the same badge: emf-camp-2024-tildagon-emf-camp-2024-badge, which carries the same core facts plus Hackaday coverage.'
status: released
sources:
- kind: url
  url: https://developer.emfcamp.org/badge/
  title: Tildagon
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://tildagon.badge.emfcamp.org/
  title: Tildagon documentation site
  accessed: '2026-09-10'
  note: Confirmed hardware (ESP32-S3, round screen, hexpansion connectors), event/year, open-source repos, and badge photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Core facts confirmed on the maker's own documentation site (tildagon.badge.emfcamp.org) and developer.emfcamp.org. LED count/type, price, and quantity made were not stated on the sources checked. This entry duplicates emf-camp-2024-tildagon-emf-camp-2024-badge, which already has fuller sourcing (Hackaday coverage) for the same badge.
last_modified_date: '2026-09-10'
---

Tildagon is the EMF Camp 2024 event badge, and the first in the "evergreen" line the EMF Camp badge team designed to be reused as a platform across multiple years (a follow-on version, Spaceagon, appeared for EMF 2026). It is a hexagonal PCB badge built around an ESP32-S3 with 2MB of PSRAM and 8MB of flash, a round LCD, RGB LEDs, an IMU, and six edge connectors ("hexpansions") that accept community-made add-on boards — anything from simple cardboard tabs to full circuit boards. It runs MicroPython and supports both custom apps and background/pattern apps, and can be updated over the air via the camp's network or flashed over USB.

The badge and its documentation are open source, with hardware and firmware published on GitHub under the EMF Camp organization. It was distributed to EMF Camp 2024 attendees as the event badge.
