---
title: Thermal Superconf 2017 Badge
id: supercon-2017-thermal-superconf-2017-badge
layout: badge
parent: Supercon 2017
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2017
year: 2017
makers:
- name: sphereinabox
  url: https://hackaday.io/sphereinabox
summary: A hardware mod that adds a low-resolution thermal camera to the stock 2017 Hackaday Superconference badge.
functions: Combines a thermal camera feed with the badge's existing visible-light camera into a single composite image.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - measurement
tech:
  mcu: null
  leds: null
  display: 128x64 visible-camera feed, 8x8 thermal overlay
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
  open_source: yes
  hardware_url: null
  firmware_url: https://bitbucket.org/sphereinabox/thermalsuperconf17badge
  eda_tool: null
links:
- label: hackaday.io/project/28259-thermal-superconf-2017-badge
  url: https://hackaday.io/project/28259-thermal-superconf-2017-badge
  kind: hackaday
- label: bitbucket.org/sphereinabox/thermalsuperconf17badge
  url: https://bitbucket.org/sphereinabox/thermalsuperconf17badge
  kind: repo
images:
  - file: assets/images/badges/supercon-2017/thermal-superconf-2017-badge/7054969a42.jpg
    source: "https://hackaday.io/project/28259-thermal-superconf-2017-badge"
    credit: "sphereinabox"
    caption: "The modified Supercon 2017 badge with the added Panasonic GridEye thermal sensor"
contact: {}
notes:
- Hardware mod turning the 2017 Supercon camera badge into a crude thermal camera. Found by the event-year sweep, task supercon-2017.
- The sweep's title matched the maker's own project title exactly; no change needed.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/28259-thermal-superconf-2017-badge
  title: Thermal Superconf 2017 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2017); event read as ''supercon-2017''.'
- kind: url
  url: https://hackaday.io/project/28259-thermal-superconf-2017-badge
  title: Thermal Superconf 2017 Badge - Hackaday.io
  accessed: '2026-09-08'
  note: 'Confirmed maker (sphereinabox), what it is, hardware used, and completion date; also linked the Bitbucket source repo.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: This is a personal hardware mod of the stock 2017 Hackaday Superconference badge, not a separate badge/SAO sold or distributed on its own — no price, quantity, or distribution info exists because it was never offered to others. MCU, LED count, and battery are not documented on the project page (it modifies the stock badge's existing hardware rather than adding its own). Only one photo was found (the project's main image); no additional in-progress or detail shots were posted.
last_modified_date: '2026-09-08'
---

sphereinabox built this as a personal project for the 2017 Hackaday Superconference, modifying the stock Supercon badge (which already carried a small visible-light camera) by adding a Panasonic GridEye thermal-imaging sensor. The result overlays a coarse 8x8-pixel thermal reading on top of the badge's existing 128x64 visible-camera feed, producing a crude but functional thermal camera the creator jokingly compared to commercial units like the FLIR One or FLIR C2. The project page describes it as working well enough to draw attention from other attendees, with 466 views and 10 likes on Hackaday.io as of research time.

The project was completed and posted November 17, 2017, shortly after the con. Source code for the mod is published on Bitbucket, though no separate hardware files (schematic/PCB) were found — the mod appears to piggyback on the existing badge hardware plus the added sensor, wired and coded ad hoc rather than as a redistributable kit.

## Make your own

Firmware/source is available at the linked Bitbucket repository (sphereinabox/thermalsuperconf17badge). No published bill of materials or wiring diagram was found beyond what appears in the source and the project log itself.
