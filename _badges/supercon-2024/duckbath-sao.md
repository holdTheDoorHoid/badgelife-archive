---
title: duckBATH SAO
id: supercon-2024-duckbath-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Adrian Studer (astuder)
  url: https://github.com/astuder
- name: Marc Merlin
  url: https://hackaday.io/marc-merlin
summary: A bathtub-shaped SAO from the duckGLOW family with a floating rubber duck lit by an RGB or UV LED, driven by a CH32V003 and controllable over I2C or as a WS2812-style addressable LED, designed for the Supercon 8 SAO Contest.
functions: Lights a 5mm RGB or UV LED inside a rubber duck floating in a bathtub-shaped PCB. Color, brightness, fade speed and phase offset are configurable over I2C (default address 0x6C, selectable to 0x6D-0x6F via solder jumpers), or the SAO can instead be driven directly as a WS2812/NeoPixel-protocol addressable LED on GPIO2. Settings can be saved as power-on defaults.
look:
  colors: []
  shape: bathtub
  themes:
  - duck
  - animal
tech:
  mcu: CH32V003
  leds:
    count: 1
    type: RGB
    note: Common-anode 4-leg RGB or 2-leg UV 5mm diffused LED, inserted into a hole in the rubber duck; driven via a 3.3V boost converter for consistent brightness.
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
  where: Sibling variant duckJAWS was sold assembled on Tindie by the maker; no separate duckBATH storefront listing was found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/astuder/duckglow
  firmware_url: https://github.com/astuder/duckglow
  eda_tool: KiCad
links:
- label: github.com/astuder/duckglow/tree/master
  url: https://github.com/astuder/duckglow/tree/master
  kind: repo
- label: github.com/astuder/duckglow
  url: https://github.com/astuder/duckglow
  kind: repo
  archived: https://web.archive.org/web/20260506012935/https://github.com/astuder/duckglow
- label: hackaday.io/project/198918-duckglow-sao
  url: https://hackaday.io/project/198918-duckglow-sao
  kind: hackaday
  archived: https://web.archive.org/web/20260506012946/https://hackaday.io/project/198918-duckglow-sao
- label: www.youtube.com/watch?v=yjSSQkx-x7U
  url: https://www.youtube.com/watch?v=yjSSQkx-x7U
  kind: video
images:
- file: assets/images/badges/supercon-2024/duckbath-sao/1b51655f98.jpg
  source: https://github.com/astuder/duckglow
  credit: Adrian Studer
  caption: duckBATH SAO with rubber duck lit by RGB LED
  archived: https://web.archive.org/web/20260506012935/https://github.com/astuder/duckglow
- file: assets/images/badges/supercon-2024/duckbath-sao/e207bef018.png
  source: https://github.com/astuder/duckglow
  credit: Adrian Studer
  caption: duckBATH SAO PCB render, bathtub shape
  archived: https://web.archive.org/web/20260506012935/https://github.com/astuder/duckglow
- file: assets/images/badges/supercon-2024/duckbath-sao/1b51655f98.jpg
  source: https://github.com/astuder/duckglow
  credit: Adrian Studer
  caption: duckBATH SAO, assembled, with rubber duck
  archived: https://web.archive.org/web/20260506012935/https://github.com/astuder/duckglow
- file: assets/images/badges/supercon-2024/duckbath-sao/e207bef018.png
  source: https://github.com/astuder/duckglow
  credit: Adrian Studer
  caption: duckBATH PCB render
  archived: https://web.archive.org/web/20260506012935/https://github.com/astuder/duckglow
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/astuder/duckglow/tree/master
  title: 'astuder/duckglow: A set of basic SAOs with glowing rubber duckies'
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/astuder/duckglow
  title: astuder/duckglow
  accessed: '2026-09-07'
  note: Confirmed chip (CH32V003), I2C control, WS2812-compatible mode, LED types, MIT license, and that duckJAWS units were sold assembled on Tindie.
  archived: https://web.archive.org/web/20260506012935/https://github.com/astuder/duckglow
- kind: url
  url: https://hackaday.io/project/198918-duckglow-sao
  title: duckGLOW SAO - Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed makers (Adrian Studer and Marc Merlin), submission to the Supercon 8 SAO Contest in October 2024, and that duckBATH/duckJAWS are the two PCB shapes in the duckGLOW family.
  archived: https://web.archive.org/web/20260506012946/https://hackaday.io/project/198918-duckglow-sao
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The GitHub repo and Hackaday.io project page confirm the design (CH32V003, RGB/UV LED, I2C + WS2812-style control) and that it was made for the Supercon 8 SAO Contest, October 2024. No dedicated duckBATH storefront listing, price, or quantity was found; the maker mentions selling assembled duckJAWS (the shark-shaped sibling) on Tindie, but duckBATH availability/pricing is unconfirmed, so get_one fields are left mostly empty. PCB color/finish not stated in text sources reviewed; leaving look.colors empty rather than guessing from the render thumbnail. Merged with duplicate entry 'duckBATH SAO' (supercon-2024-duckbath-sao-2).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2024/duckbath-sao-2/
---

The duckBATH is a bathtub-shaped SAO ("Shitty Add-On") from Adrian Studer and Marc Merlin's duckGLOW family, made for the Supercon 8 SAO Contest in October 2024. A small rubber duck sits in the tub-shaped PCB with a 5mm LED tucked inside it; a CH32V003 microcontroller drives the LED either as a smoothly fading RGB or UV light controllable over I2C, or as a plain WS2812/NeoPixel-compatible addressable LED, so it works standalone or as part of a larger chain of addressable lights on a badge. Brightness limits, fade speed, phase offset, and the I2C address (one of four, set by solder jumpers) are all configurable, and settings can be saved as the power-on default.

duckBATH shares its design and firmware with the shark-themed duckJAWS variant, which added a second, red-lit LED channel for the shark's teeth/background glow and was sold assembled on Tindie. It is not confirmed whether duckBATH itself was sold separately or only distributed alongside duckJAWS at Supercon.

## Make your own

Hardware and firmware are open source (MIT license) at [github.com/astuder/duckglow](https://github.com/astuder/duckglow), which includes the PCB design files, firmware, and example code for driving the SAO from a Supercon 8 badge or a generic Arduino-compatible host.

## Notes merged from the duplicate entry "duckBATH SAO"

duckBATH is one of two SAO designs in Adrian Studer and Marc Merlin's duckGLOW project, submitted to the Supercon 8 SAO Contest in 2024. Where its sibling duckJAWS gives the rubber duck a shark-fin surround, duckBATH puts the duck in a small PCB bathtub. Both designs share the same electronics: a CH32V003 microcontroller drives a single RGB (or swappable 2-lead UV) LED that lights the duck from below, with a small boost converter keeping brightness consistent regardless of the host badge's supply voltage.

The LED can be controlled two ways: as an I2C peripheral (default address 0x6C, with solder-jumper options for 0x6D–0x6F) exposing per-channel brightness, fading, and animation-phase registers, or directly as a single WS2812-protocol addressable pixel, so it drops into an existing NeoPixel chain. Settings can be saved as I2C-configured power-on defaults.

Hardware and firmware are fully open source — MIT-licensed code and CERN-OHL-P-licensed KiCad hardware files are on GitHub alongside example code for Supercon-badge and Arduino hosts. The project's duckJAWS variant has been sold as a partially-assembled kit on Tindie; no distribution details specific to the duckBATH shape were found, so pricing, quantity, and availability are left blank here.
