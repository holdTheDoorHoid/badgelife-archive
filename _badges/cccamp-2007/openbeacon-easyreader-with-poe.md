---
title: OpenBeacon-EasyReader (with PoE)
id: cccamp-2007-openbeacon-easyreader-with-poe
layout: badge
parent: Chaos Communication Camp 2007
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: cccamp-2007
year: 2007
makers:
- name: OpenBeacon project
  url: https://www.openbeacon.org
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: events.ccc.de/camp/2007/Sputnik
  url: https://events.ccc.de/camp/2007/Sputnik/
  kind: website
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
status: not_an_item
sources:
- kind: url
  url: https://events.ccc.de/camp/2007/Sputnik/
  title: OpenBeacon-EasyReader (with PoE)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://devicehunt.com/view/type/usb/vendor/2366/device/0007
  title: OpenBeacon Ethernet EasyReader PoE II
  accessed: '2026-09-10'
  note: USB device-ID listing confirming EasyReader PoE II is a fixed active-2.4GHz-RFID reader unit made by Bitmanufaktur GmbH, not a wearable device.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: >-
    This is not a badge, SAO, or wearable accessory. The Sputnik CCCamp 2007 page
    lists the OpenBeacon-EasyReader (with PoE) alongside the OpenBeacon USB reader
    as fixed base-station hardware: a Power-over-Ethernet-powered 2.4GHz active RFID
    reader used to pick up signals from the Sputnik tags that attendees actually wore.
    The wearable tag itself is already a separate entry, cccamp-2007-sputnik-openbeacon.
    No pricing, chip, or availability details apply since this was never sold or worn;
    leaving those fields empty rather than guessing.
last_modified_date: '2026-09-10'
---

The OpenBeacon-EasyReader (with PoE) was not something Chaos Communication Camp 2007 attendees wore — it was part of the fixed infrastructure for the "Sputnik" real-time location tracking project. Powered over Ethernet, it acted as a stationary base-station receiver, picking up 2.4GHz active-RFID beacon signals from the Sputnik tags that attendees carried, so their positions and "mood" button presses could be aggregated into the camp-wide tracking display.

The device was built by the OpenBeacon project (Bitmanufaktur GmbH, led by Milosch Meriac), the same team behind the wearable Sputnik tag documented separately in this archive (see `cccamp-2007-sputnik-openbeacon`). A later revision, marketed as "OpenBeacon Ethernet EasyReader PoE II," appears in USB device-ID registries as a distinct active 2.4GHz RFID reader product, confirming this was reader/receiver hardware rather than a badge or SAO.
