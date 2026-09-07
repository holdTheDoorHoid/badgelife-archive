---
title: Tildagon (EMF Camp 2024 Badge)
id: emf-camp-2024-tildagon-emf-camp-2024-badge
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
summary: 'A reusable hexagonal event badge for EMF Camp 2024, built around an ESP32-S3 and a round LCD, with an edge connector ("hexpansion") on each of its six sides for user-made add-ons.'
functions: 'Runs MicroPython apps on a round LCD; can be extended with electronic or simple cardboard "hexpansion" modules plugged into the edge connectors on each side; supports over-the-air firmware updates over the camp network and USB flashing (including a web-based flasher).'
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
  where: 'Given to EMF Camp 2024 attendees (badge came with the ticket; the article notes it was the first EMF badge with an added charge because of the hexpansion edge connectors, but no figure was found).'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/emfcamp/badge-2024-hardware
  firmware_url: https://github.com/emfcamp/badge-2024-software
  eda_tool: null
links:
- label: hackaday.com/2024/06/01/hands-on-with-the-electromagnetic-field-2024-badge
  url: https://hackaday.com/2024/06/01/hands-on-with-the-electromagnetic-field-2024-badge/
  kind: article
- label: hackaday.com/2024/03/23/the-electromagnetic-field-2024-badge-is-a-little-different
  url: https://hackaday.com/2024/03/23/the-electromagnetic-field-2024-badge-is-a-little-different/
  kind: article
- label: github.com/emfcamp/badge-2024-hardware
  url: https://github.com/emfcamp/badge-2024-hardware
  kind: repo
- label: github.com/emfcamp/badge-2024-software
  url: https://github.com/emfcamp/badge-2024-software
  kind: repo
images:
  - file: assets/images/badges/emf-camp-2024/tildagon-emf-camp-2024-badge/c6a2b3c93c.jpg
    source: "https://hackaday.com/2024/06/01/hands-on-with-the-electromagnetic-field-2024-badge/"
    credit: "Hackaday"
    caption: "The Tildagon hexagonal badge with round LCD display and hexpansion edge connectors"
  - file: assets/images/badges/emf-camp-2024/tildagon-emf-camp-2024-badge/11a12d4238.jpg
    source: "https://hackaday.com/2024/06/01/hands-on-with-the-electromagnetic-field-2024-badge/"
    credit: "Hackaday"
    caption: "The Tildagon's two PCBs (front and rear) linked by a ribbon cable"
contact: {}
notes:
- Hexagonal badge with Hexpansion add-on slots; also announced in https://hackaday.com/2024/03/23/the-electromagnetic-field-2024-badge-is-a-little-different/
status: released
sources:
- kind: url
  url: https://hackaday.com/2024/06/01/hands-on-with-the-electromagnetic-field-2024-badge/
  title: Tildagon (EMF Camp 2024 Badge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''EMF Camp 2024''.'
- kind: url
  url: https://hackaday.com/2024/03/23/the-electromagnetic-field-2024-badge-is-a-little-different/
  title: The Electromagnetic Field 2024 Badge Is A Little Different
  accessed: '2026-09-07'
  note: 'Earlier announcement piece; confirms ESP32-S3 MCU, round LCD, hexagonal edge-connector "hexpansion" design, and that this was the first EMF badge with an added charge.'
- kind: url
  url: https://github.com/emfcamp/badge-2024-hardware
  title: emfcamp/badge-2024-hardware
  accessed: '2026-09-07'
  note: 'Official hardware repo; confirms open hardware (hexpansion, tildagon-base, tildagon-2026 folders, BOM spreadsheet, datasheets); README content itself was not retrievable via fetch.'
- kind: url
  url: https://github.com/emfcamp/badge-2024-software
  title: emfcamp/badge-2024-software
  accessed: '2026-09-07'
  note: 'Official firmware repo README; confirms MicroPython firmware for ESP32-S3, MIT-licensed, built via Docker/ESP-IDF v5.5.1, with a web flasher at emfcamp.github.io/badge-2024-software/.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event/year, hexagonal shape, ESP32-S3, round LCD, hexpansion edge connectors, battery compatibility, open source hardware+firmware) are confirmed by Hackaday coverage and the official emfcamp GitHub repos. Could not find: exact LED count/type, SAO header version (the hexpansion connector is a proprietary edge connector, not the standard 4/6-pin SAO header, so sao_version is left null), specific price paid by attendees, total quantity made, or named individual badge-team members. The hardware repo README did not render via automated fetch, so BOM/LED/connector-pinout details in it were not confirmed.'
last_modified_date: '2026-09-07'
---

The Tildagon is EMF Camp's badge for its 2024 event, built around an Espressif ESP32-S3 and a round LCD display. Rather than the usual rectangular PCB, it takes the shape of a hexagon with an edge connector on every side, called a "hexpansion" port, so attendees can plug in add-on modules — anything from simple electronic boards to plain cardboard cut-outs — and, per the badge team's stated goal, keep using compatible modules across future EMF camps rather than throwing them away after one event. It was reportedly the first EMF badge to carry an extra charge beyond the ticket price, attributed to the cost of the six edge connectors.

Two PCBs, front and rear, are linked by a ribbon cable inside the hexagonal shell. The badge supports both USB and over-the-air firmware updates over the camp's network, and its firmware — MicroPython running on the ESP32-S3 — is published as open source (MIT license) alongside the hardware design files in EMF Camp's GitHub organization, including a browser-based flashing tool.

Some details commonly tracked for badges of this kind — the exact LED count and type, a specific attendee price, and total units made — were not stated in the sources checked for this entry.
