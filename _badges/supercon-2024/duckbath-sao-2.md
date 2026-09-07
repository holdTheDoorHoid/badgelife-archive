---
title: duckBATH SAO
id: supercon-2024-duckbath-sao-2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Adrian Studer (astuder)
  url: https://hackaday.io/astuder
- name: Marc Merlin
  url: https://hackaday.io/marc-merlin
summary: A bathtub-shaped SAO from the duckGLOW project that lights a small rubber duck with an RGB or UV LED, driven by a CH32V003 and controllable over I2C or as a WS2812-style addressable LED; made for the Supercon 8 SAO Contest in 2024.
functions: 'Lights a small rubber duck sitting in a PCB "bathtub" with an RGB or UV LED. Controllable over I2C (default address 0x6C, configurable via solder jumpers to 0x6D/0x6E/0x6F) with per-channel brightness, smooth fading, and phase-offset animation, or driven directly as a WS2812-compatible addressable LED. Settings can be stored as power-on defaults via I2C.'
look:
  colors: []
  shape: null
  themes:
  - duck
  - bathtub
tech:
  mcu: CH32V003
  leds:
    count: 1
    type: RGB
    note: Common-anode RGB LED or a 2-legged UV LED lights the rubber duck; driven by the CH32V003 either via I2C registers or as a single WS2812-protocol addressable pixel on GPIO2.
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
  open_source: yes
  hardware_url: https://github.com/astuder/duckglow/tree/master/duckbath
  firmware_url: https://github.com/astuder/duckglow
  eda_tool: KiCad
links:
- label: hackaday.io/project/198918-duckglow-sao
  url: https://hackaday.io/project/198918-duckglow-sao
  kind: hackaday
- label: github.com/astuder/duckglow
  url: https://github.com/astuder/duckglow
  kind: repo
images:
- file: assets/images/badges/supercon-2024/duckbath-sao-2/1b51655f98.jpg
  source: "https://github.com/astuder/duckglow"
  credit: "Adrian Studer"
  caption: "duckBATH SAO, assembled, with rubber duck"
- file: assets/images/badges/supercon-2024/duckbath-sao-2/e207bef018.png
  source: "https://github.com/astuder/duckglow"
  credit: "Adrian Studer"
  caption: "duckBATH PCB render"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198918-duckglow-sao
  title: duckGLOW SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/198918-duckglow-sao
  title: duckGLOW SAO - Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed maker(s), CH32V003 MCU, I2C/WS2812 dual control, Supercon 8 SAO Contest 2024 entry, boost converter for consistent brightness, sold as partially-assembled kits under the duckJAWS brand on Tindie.
- kind: url
  url: https://github.com/astuder/duckglow
  title: astuder/duckglow (GitHub repo)
  accessed: '2026-09-07'
  note: Confirmed repo contains separate duckjaws and duckbath KiCad projects, MIT license (firmware) plus CERN-OHL-P (hardware), and default I2C address 0x6C with jumper-selectable alternates.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched both cited pages (hackaday.io project page, astuder/duckglow GitHub repo/README) and confirmed every non-empty field and body sentence — maker team, CH32V003, I2C default address 0x6C with jumper-selectable 0x6D-0x6F, WS2812 mode on GPIO2, 3.3V boost converter, Supercon 8 SAO Contest 2024, MIT (firmware) + CERN-OHL-P (hardware) licenses, KiCad files, per-channel brightness/fade/phase registers and power-on-default save register, Supercon-badge/Arduino example code, and the duckJAWS Tindie note. Both saved images verified to exist on disk and to correspond to maker-published files in the repo''s pictures/ folder specifically labeled for this variant (duckbath.jpg, duckbath-render.png), not the sibling duckJAWS shape. duckBATH is one of two PCB shapes in the duckGLOW project (the other being the shark-themed duckJAWS); both share the same CH32V003 firmware and I2C/WS2812 control scheme. Could not confirm a price, quantity made, or availability specific to duckBATH — the Tindie storefront found for the project sells the duckJAWS variant under that brand name, and it is unclear whether duckBATH was sold separately, given away at Supercon, or remains DIY-only (build-your-own from the open KiCad files). Left get_one fields empty rather than guess.'
last_modified_date: '2026-09-07'
---

duckBATH is one of two SAO designs in Adrian Studer and Marc Merlin's duckGLOW project, submitted to the Supercon 8 SAO Contest in 2024. Where its sibling duckJAWS gives the rubber duck a shark-fin surround, duckBATH puts the duck in a small PCB bathtub. Both designs share the same electronics: a CH32V003 microcontroller drives a single RGB (or swappable 2-lead UV) LED that lights the duck from below, with a small boost converter keeping brightness consistent regardless of the host badge's supply voltage.

The LED can be controlled two ways: as an I2C peripheral (default address 0x6C, with solder-jumper options for 0x6D–0x6F) exposing per-channel brightness, fading, and animation-phase registers, or directly as a single WS2812-protocol addressable pixel, so it drops into an existing NeoPixel chain. Settings can be saved as I2C-configured power-on defaults.

Hardware and firmware are fully open source — MIT-licensed code and CERN-OHL-P-licensed KiCad hardware files are on GitHub alongside example code for Supercon-badge and Arduino hosts. The project's duckJAWS variant has been sold as a partially-assembled kit on Tindie; no distribution details specific to the duckBATH shape were found, so pricing, quantity, and availability are left blank here.
