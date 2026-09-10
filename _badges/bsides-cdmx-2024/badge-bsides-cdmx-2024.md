---
title: Badge BSides CDMX 2024
id: bsides-cdmx-2024-badge-bsides-cdmx-2024
layout: badge
parent: BSides Cdmx 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cdmx-2024
year: 2024
makers:
- name: Electronic Cats
  url: https://electroniccats.com/
summary: 'The official electronic badge for BSides CDMX 2024, an ESP32-C6 badge with an OLED display and NeoPixels that talks to a laptop over USB serial.'
functions: 'Boots to a serial console (115200 baud over USB-C) that prints badge text/status; drives an OLED display and addressable NeoPixel LEDs. No games or CTF functions are documented in the repo.'
look:
  colors: []
  shape: null
  themes:
  - cat
  - security
tech:
  mcu: ESP32-C6
  leds:
    count: null
    type: NeoPixel
    note: ''
  display: OLED
  connectivity:
  - usb
  - uart
  battery: 2x AA battery holder
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Distributed to attendees/staff/speakers/sponsors of BSides CDMX 2024; no public storefront listing found.'
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/ElectronicCats/badge-bsides-cdmx-2024/tree/main/hardware
  firmware_url: https://github.com/ElectronicCats/badge-bsides-cdmx-2024/tree/main/firmware
  eda_tool: KiCad
  license: 'Hardware: CERN Open Hardware Licence v1.2; Firmware: GPL-3.0'
  notes: 'Repo includes six role-specific board variants (Community, Guest, Speaker, Sponsor, Staff, and the Shitty Addon) as separate KiCad projects.'
links:
- label: github.com/ElectronicCats/badge-bsides-cdmx-2024
  url: https://github.com/ElectronicCats/badge-bsides-cdmx-2024
  kind: repo
images: []
contact: {}
notes:
- Electronic Cats' badge for BSides Mexico City 2024, flashable/serial-controlled over USB. Found by the event-year sweep, task bsides-any.
- 'The sweep''s title read plainly as the repo name ("Badge bsides CDMX 2024"); retitled here to standard capitalization ("Badge BSides CDMX 2024") to match the maker''s own conference-name capitalization.'
status: released
sources:
- kind: url
  url: https://github.com/ElectronicCats/badge-bsides-cdmx-2024
  title: Badge bsides CDMX 2024
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides CDMX 2024''.'
- kind: url
  url: https://raw.githubusercontent.com/ElectronicCats/badge-bsides-cdmx-2024/main/README.md
  title: 'README: Badge bsides CDMX 2024'
  accessed: '2026-09-10'
  note: 'Confirmed MCU (ESP32C6), NeoPixel LEDs, USB-C, OLED display, 2x AA battery holder, Shitty Addon Connector, 115200-baud serial usage, and hardware/firmware licenses.'
- kind: url
  url: https://api.github.com/repos/ElectronicCats/badge-bsides-cdmx-2024/contents/hardware
  title: 'Repo contents: hardware/'
  accessed: '2026-09-10'
  note: 'Confirmed six role-specific KiCad board variants (Community, Guest, ShittyAddon, Speaker, Sponsor, Staff); no rendered photos or images present in the repo.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, event, MCU, LEDs, display, battery, connectivity, open-source status, licenses) confirmed directly from the maker''s own GitHub repository and README. No pricing, quantity-made, or storefront/availability information is published anywhere found; get_one fields left mostly empty. No photos of the assembled badge were found in the repo (no image files) or via web search, so images could not be saved. A YouTube video titled "Badge Life: Making of the BSides 2024 Badge From Start to Finish" appears to cover this badge''s development but was not opened (budget); worth a future look for photos/quotes. A badge.gallery listing for "BSides CDMX 2025" describes a related but different-year Electronic Cats badge (Puya PY32F030F28U6TR MCU) — not this entry.'
last_modified_date: '2026-09-10'
---

Electronic Cats designed the official electronic badge for BSides CDMX 2024, the Mexico City chapter of the community-run Security BSides conference series. The badge is built around an ESP32-C6 microcontroller with an OLED display and addressable NeoPixel LEDs, runs on two AA batteries, and connects to a computer over USB-C, where it presents a 115200-baud serial console that prints badge status text.

The project was released as six separate role-specific PCB variants — Community, Guest, Speaker, Sponsor, Staff, and a companion "Shitty Addon" board — each with its own KiCad design files in the GitHub repository, alongside a shared "electroniccats" schematic/PCB library. Sponsors credited for making the badge possible include HSBC and the BSides CDMX organizing team.

## Make your own

Full hardware (KiCad schematics, PCB layouts, and STEP models for each role variant) and firmware source are published in the [GitHub repository](https://github.com/ElectronicCats/badge-bsides-cdmx-2024). Hardware is released under the CERN Open Hardware Licence v1.2 and firmware under GPL-3.0. To use a badge: connect it via USB-C, then open its serial port at 115200 baud (Arduino IDE, PuTTY, or `screen`) to see badge text.
