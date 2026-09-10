---
title: ToF Add-on (2026)
id: fri3d-2026-tof-add-on-2026
layout: badge
parent: Fri3d Camp 2026
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: fri3d-2026
year: 2026
makers:
- name: Fri3d Camp
summary: 'A SAO add-on for the Fri3d Camp 2026 badge built around an STMicroelectronics VL53L7CH 8x8 multizone time-of-flight sensor, for distance and spatial sensing.'
functions: 'Measures distance and basic spatial/gesture-style sensing via an 8x8 zone time-of-flight array (2-350 cm range, up to 60 Hz sampling, 30 Hz over I2C). Ships with an example app in the badge''s MicroPythonOS appstore; the board also carries eight addressable RGB LEDs and can pair with the separate SAO Mirror add-on.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - measurement
tech:
  mcu: none
  leds:
    count: 8
    type: RGB
    note: Addressable RGB LEDs on the add-on board
  display: null
  connectivity:
  - i2c
  battery: powered by host badge
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
- label: fri3dcamp.github.io/badge_2026/en
  url: https://fri3dcamp.github.io/badge_2026/en/
  kind: website
- label: fri3dcamp.github.io/badge_2026/tof
  url: https://fri3dcamp.github.io/badge_2026/tof/
  kind: doc
images:
- file: assets/images/badges/fri3d-2026/tof-add-on-2026/4602723822.jpg
  source: "https://fri3dcamp.github.io/badge_2026/tof/"
  credit: "Fri3d Camp"
  caption: "The ToF Add-on SAO board with VL53L7CH sensor and RGB LEDs"
- file: assets/images/badges/fri3d-2026/tof-add-on-2026/dbb0e03393.jpg
  source: "https://fri3dcamp.github.io/badge_2026/tof/"
  credit: "Fri3d Camp"
  caption: "The ToF Add-on mounted on the Fri3d Camp 2026 badge"
contact: {}
notes:
- Time-of-flight distance-sensing add-on (VL53L7CH) for the Fri3d Camp 2026 badge, listed alongside the badge on its docs homepage. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task fri3d.
status: listed
sources:
- kind: url
  url: https://fri3dcamp.github.io/badge_2026/en/
  title: ToF Add-on (2026)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:fri3d); event read as ''fri3d-2026''.'
- kind: url
  url: https://fri3dcamp.github.io/badge_2026/tof/
  title: ToF Sensor Add-on for Fri3d Camp 2026 Badge
  accessed: '2026-09-10'
  note: 'Fri3d Camp''s own dedicated docs page for the add-on; confirmed the item exists and supplied chip, sensor specs, LED count, connector type, software support, and images.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed as a real, documented add-on (not just a search snippet) via Fri3d Camp''s own docs site. Type corrected from "accessory" to "sao" since it plugs into the badge''s SAO connector. No pricing, quantity made, availability, or design-file (KiCad/GitHub) links were published on the docs pages checked; left those fields empty rather than guessed. STMicroelectronics and EBV Elektronik are credited as development-support partners but this is not stated as a joint release.'
last_modified_date: '2026-09-10'
---

The ToF Add-on is a SAO accessory for the Fri3d Camp 2026 badge, built around STMicroelectronics' VL53L7CH, an 8x8 multizone time-of-flight sensor. It measures distance from about 2 to 350 cm, sampling at up to 60 Hz (30 Hz when read over I2C), and uses a Class 1 laser at 940 nm. The board plugs into the badge's SAO connector, carries eight addressable RGB LEDs of its own, and can be combined with the separately listed SAO Mirror add-on.

Software support comes through an example application in the badge's MicroPythonOS appstore, alongside reference code STMicroelectronics publishes for the VL53L7CH itself. Fri3d Camp credits EBV Elektronik and STMicroelectronics with backing the project. Pricing, production quantity, and design-file links were not published on the pages checked.
