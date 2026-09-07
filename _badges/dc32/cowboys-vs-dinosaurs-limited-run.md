---
title: Cowboys vs. Dinosaurs (limited run)
id: dc32-cowboys-vs-dinosaurs-limited-run
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Alt_Bier
  url: https://altbier.us/
summary: A capacitive-touch, ESP32-based indie badge pitting cowboys against dinosaurs in a card-game theme, with a built-in Wi-Fi "adventure game" mode.
functions: Five capacitive touch pads (Cowboys, Dinosaurs, 3000, Society, and a logo button) trigger LED animations and reactions; the badge also hosts its own Wi-Fi access point and web server for an adventure-game mode.
look:
  colors: []
  shape: card
  themes:
  - western
  - dinosaur
  - card game
tech:
  mcu: ESP32 (Wemos Lolin32)
  leds:
    count: 12
    type: mixed
    note: 6 addressable NeoPixels plus 6 traditional single-color LEDs, and a separate battery-charge indicator LED.
  display: none
  connectivity:
  - wifi
  battery: LiPo (rechargeable, USB-C charging, onboard charge circuit)
  sao_version: null
get_one:
  price: $70.00
  price_usd: 70.0
  quantity: ''
  availability: sold_out
  distribution:
  - crowdfunding
  - purchase
  where: Sold as a limited run via an Indiegogo campaign (fully assembled badges sold out); leftover kits were sold at The Hacker Warehouse's vendor table at DEF CON 32.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/gowenrw/cowboys_vs_dinosaurs/tree/main/eda/cowboys_vs_dinos
  firmware_url: https://github.com/gowenrw/cowboys_vs_dinosaurs/tree/main/code
  eda_tool: KiCad
  license: MIT
  notes: Repo also includes artwork, 3D files, and documentation for the badge; maker attributed on GitHub as gowenrw.
links:
- label: twitter.com/alt_bier
  url: https://twitter.com/alt_bier
  kind: social
- label: altbier.us
  url: https://altbier.us/
  kind: website
- label: Cowboys vs. Dinosaurs badge docs
  url: https://cowboysvsdinos.altbier.us/
  kind: doc
- label: gowenrw/cowboys_vs_dinosaurs (GitHub)
  url: https://github.com/gowenrw/cowboys_vs_dinosaurs
  kind: repo
images:
- file: assets/images/badges/dc32/cowboys-vs-dinosaurs-limited-run/a60b5bbfe9.jpg
  source: "https://cowboysvsdinos.altbier.us/"
  credit: "Alt_Bier"
  caption: "Assembled Cowboys vs. Dinosaurs badge, Cowboys touch area lit"
- file: assets/images/badges/dc32/cowboys-vs-dinosaurs-limited-run/b81eed8603.jpg
  source: "https://cowboysvsdinos.altbier.us/"
  credit: "Alt_Bier"
  caption: "Cowboys vs. Dinosaurs badge kit, unassembled parts"
contact: {}
notes:
- Indiegogo link is now closed!! All fully assembled badges are sold out. Only ones left will be kits and will be available at The Hacker Warehouse in the Vendor Area at DEFCON 32.
status: released
sources:
- kind: sheet
  event: dc32
  row: 10
  updated: '2024-07-25'
- kind: url
  url: https://altbier.us/
  title: "altbier.us"
  accessed: '2026-09-06'
  note: Maker's landing page; links to the badge-specific documentation site and confirms the badge was made for "The 3000 Society 2024" con and DEF CON 32.
- kind: url
  url: https://cowboysvsdinos.altbier.us/
  title: "Cowboys vs Dinosaurs Badge - DEFCON 32"
  accessed: '2026-09-06'
  note: Primary documentation page; source for MCU, LED count/type, touch inputs, Wi-Fi adventure-game mode, battery, and photos.
- kind: url
  url: https://github.com/gowenrw/cowboys_vs_dinosaurs
  title: "gowenrw/cowboys_vs_dinosaurs"
  accessed: '2026-09-06'
  note: Confirms open-source hardware/firmware/art, MIT license, and KiCad 7.x EDA files under /eda/cowboys_vs_dinos/.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: >-
    Core facts (maker, MCU, LEDs, inputs, battery, open-source status) confirmed on the maker's own
    documentation site and GitHub repo. Exact quantity made and the assembled-badge price breakdown
    beyond the $70 sheet figure were not stated anywhere found; left empty rather than guessed.
    Could not confirm whether the badge has an SAO header, so tech.sao_version is left null.
    The maker's Twitter/X account could not be fetched directly (login-walled); background on the
    maker's badgelife history came from an archived 2023 Indiegogo page for their prior "Future
    Badge" (DC31) campaign, which links to altbier.us.
last_modified_date: '2026-09-06'
---

Cowboys vs. Dinosaurs is an ESP32-based indie badge by Alt_Bier (maker handle; GitHub credits "gowenrw"), built around a card-game standoff between cowboys and dinosaurs. Five capacitive touch pads — Cowboys, Dinosaurs, 3000, Society, and a logo button — drive a mix of six addressable NeoPixels and six traditional LEDs, and the badge doubles as its own tiny network: it broadcasts a Wi-Fi access point and runs a web server for an on-badge "adventure game" mode. It runs on a Wemos Lolin32 ESP32 dev board and charges over USB-C into an onboard LiPo battery, with a dedicated charge-indicator LED on the back.

The badge was first shown at The 3000 Society's 2024 convention before being sold as a limited run for DEF CON 32 via an Indiegogo campaign at $70. The campaign sold out of fully-assembled units before the con; the badges that remained went out as unassembled kits at The Hacker Warehouse's vendor table in the DEF CON 32 vendor area. The maker released the full project — artwork, KiCad 7.x PCB design, 3D files, and firmware — as open source under the MIT license on GitHub.

## Make your own

Hardware (KiCad project), firmware, artwork, and 3D files are all in the [gowenrw/cowboys_vs_dinosaurs](https://github.com/gowenrw/cowboys_vs_dinosaurs) GitHub repo under the MIT license. The repo layout separates `/art/`, `/code/`, `/eda/cowboys_vs_dinos/` (the KiCad project), `/docs/`, and `/reference_parts/` (a git submodule of reference component documentation) — clone with `git submodule update --init --recursive` to pull that submodule in.
