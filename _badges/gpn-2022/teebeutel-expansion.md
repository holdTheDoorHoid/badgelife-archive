---
title: Teebeutel-Expansion
id: gpn-2022-teebeutel-expansion
layout: badge
parent: GPN 2022
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: gpn-2022
year: 2022
makers:
- name: Entropia e.V.
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
- label: github.com/entropia/Teebeutel-Expansion
  url: https://github.com/entropia/Teebeutel-Expansion
  kind: website
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'The sweep''s title "Teebeutel-Expansion" is the repo name; the repo itself calls this a "sample Expansion Board" / reference template, not a specific product.'
status: not_an_item
sources:
- kind: url
  url: https://github.com/entropia/Teebeutel-Expansion
  title: Teebeutel-Expansion (add-on boards for the Teebeutel badge's expansion header)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://raw.githubusercontent.com/entropia/Teebeutel-Expansion/master/docs/modules/ROOT/pages/index.adoc
  title: 'Teebeutel Expansion docs: "This is a sample Expansion Board for the Teebeutel v1.0"'
  accessed: '2026-09-10'
  note: Confirms the repo is a generic template/reference design for building your own expansion boards, plus a list of community-published expansions, not one specific released accessory.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: >-
    This GitHub repo is not a specific badge or SAO; it is Entropia's reference
    "Teebeutel-Expansion" template for GPN20's Teebeutel badge, offered in two
    forms (a stripboard prototyping version and a blank KiCad template) so
    attendees could design their own expansion boards for the badge's
    expansion header (I2C, WS2812, serial, 9 GPIO). The base Teebeutel badge
    already has its own entry (gpn-2022-teebeutel-gpn20-conference-badge). One
    genuine community-made expansion board is linked from the repo's docs: the
    "Image-Sensor Expansion" by Jana-Marie
    (https://github.com/Jana-Marie/Teebeutel-Image-Sensor-Expansion) - reported
    separately as a possible entry. No price, quantity, or distribution
    information applies since this is a template, not a sold/distributed item.
last_modified_date: '2026-09-10'
---

This repository is not itself a badge or accessory that was made and handed out at GPN 2022 (GPN20) — it is Entropia's open-source reference design for building expansion boards that plug into the Teebeutel badge's expansion header (I2C, WS2812, serial, and 9 GPIO pins). It ships in two forms: a stripboard version for quick through-hole prototyping, and a blank KiCad template for designing a custom PCB.

The base Teebeutel badge — an ESP32/MicroPython badge with a 128x128px OLED and WS2812 LEDs — has its own archive entry. The expansion repo's documentation also lists at least one real, specific expansion board built from this template: an "Image-Sensor Expansion" by community member Jana-Marie, which would be a separate, legitimate archive candidate.
