---
title: SaO Mirror (2026)
id: fri3d-2026-sao-mirror-2026
layout: badge
parent: Fri3d Camp 2026
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: fri3d-2026
year: 2026
makers:
- name: Fri3d Camp
  url: https://fri3dcamp.github.io/badge_2026/en/
summary: 'A small passive PCB adapter for the Fri3d Camp 2026 badge that flips a SAO-connector sensor to face the opposite side of the badge, mainly so the ToF Add-on can point outward.'
functions: 'Redirects a SAO-mounted sensor (e.g. the ToF Add-on) to face the "other" side of the badge; optionally carries 8 WS2812 RGB LEDs for extra visualization.'
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 8
    type: WS2812B
    note: Optional; not included in the standard kit, solder yourself if wanted.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed as part of the official Fri3d Camp 2026 hardware add-on lineup alongside the Communicator, DJ Controller, ToF, and LoRa add-ons.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Fri3dCamp/badge_2026_hw
  firmware_url: null
  eda_tool: null
links:
- label: fri3dcamp.github.io/badge_2026/en
  url: https://fri3dcamp.github.io/badge_2026/en/
  kind: website
- label: SaO Mirror documentation page
  url: https://fri3dcamp.github.io/badge_2026/mirror/
  kind: doc
- label: badge_2026_hw (hardware design files)
  url: https://github.com/Fri3dCamp/badge_2026_hw
  kind: repo
images:
- file: assets/images/badges/fri3d-2026/sao-mirror-2026/7863973421.jpg
  source: "https://fri3dcamp.github.io/badge_2026/mirror/"
  credit: "Fri3d Camp"
  caption: "SaO Mirror kit parts"
- file: assets/images/badges/fri3d-2026/sao-mirror-2026/7067a8085a.jpg
  source: "https://fri3dcamp.github.io/badge_2026/mirror/"
  credit: "Fri3d Camp"
  caption: "SaO Mirror PCB mounted on the Fri3d Camp 2026 badge, redirecting a SAO to face the opposite direction"
contact: {}
notes:
- 'Sweep''s snippet called it a "Shitty Add-On with a mirror effect" and listed it as an SAO; the maker''s own documentation describes it instead as a passive adapter PCB that flips a SAO-connector sensor to the other side of the badge (no "mirror effect" in the optical sense, and it is not itself a functional SAO so much as a mounting accessory). Title changed from "SAO Mirror" to "SaO Mirror" to match the maker''s own capitalization.'
status: released
sources:
- kind: url
  url: https://fri3dcamp.github.io/badge_2026/en/
  title: SAO Mirror (2026)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:fri3d); event read as ''fri3d-2026''.'
- kind: url
  url: https://fri3dcamp.github.io/badge_2026/mirror/
  title: SaO Mirror - Fri3d 2026
  accessed: '2026-09-10'
  note: 'Maker''s own documentation page for the SaO Mirror: describes its purpose, assembly, optional LEDs, and includes photos.'
- kind: url
  url: https://github.com/Fri3dCamp/badge_2026_hw
  title: 'Fri3dCamp/badge_2026_hw: The hardware design files for the Fri3dcamp 2026 badge'
  accessed: '2026-09-10'
  note: 'Repository holding open hardware design files for the 2026 badge and its add-ons, including the SaO Mirror.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Confirmed on Fri3d''s own documentation site, not just a search snippet. Price, quantity made, and availability status are not published anywhere found; left empty/unknown. Could not confirm whether the design files repo contains a mirror-specific subfolder without deeper browsing of the repo tree, so hardware_url points to the repo root rather than a specific path.'
last_modified_date: '2026-09-10'
---

The SaO Mirror is a small, passive PCB accessory in the official Fri3d Camp 2026 hardware lineup, sitting alongside the badge's Communicator, DJ Controller, ToF, and LoRa add-ons. Rather than being a standalone functional SAO, it exists to solve a mounting problem: a sensor plugged into a badge's SAO connector normally faces one fixed direction, and the Mirror PCB flips that orientation so the sensor points the other way. Fri3d's documentation calls out the ToF (time-of-flight) Add-on specifically as the sensor this is built for, letting wearers aim it outward from the badge instead of wherever the SAO header happens to point.

The kit ships with the connectors needed to mount it, plus a solder bridge that must be closed to complete the circuit. As an optional extra, builders can solder on 8 WS2812B RGB LEDs for visual flair; these are not included in the base kit and require no special software changes to use once soldered, since they're handled by the existing badge/add-on ecosystem. The design is part of Fri3d's open hardware release for 2026, published in the `badge_2026_hw` repository alongside the rest of the badge's hardware.

No price, production quantity, or specific availability window is published on Fri3d's site.
