---
title: DJ Controller (2026 add-on)
id: fri3d-2026-dj-controller-2026-add-on
layout: badge
parent: Fri3d Camp 2026
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: fri3d-2026
year: 2026
makers:
- name: Fri3d Camp
  url: https://github.com/Fri3dCamp
summary: A DIY expansion module that turns the Fri3d Camp 2026 badge into a small USB/MIDI DJ controller with faders, pots, encoders, and RGB-lit buttons.
functions: Sends MIDI over USB and UART so it can mix and control music tracks (e.g. via the browser-based "Fri3d Scratcher" app); communicates with the host badge over I2C/UART.
look:
  colors: []
  shape: null
  themes:
  - music
tech:
  mcu: CH32X035
  leds:
    count: 8
    type: WS2812
    note: one LED beneath each of the 8 silicone buttons
  display: none
  connectivity:
  - usb
  - i2c
  - uart
  inputs:
  - buttons
  - rotary encoder
  battery: powered by host badge / USB
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as a soldering kit to Fri3d Camp 2026 attendees alongside the main badge; price and quantity not stated on the documentation site.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Fri3dCamp/dj_2026
  firmware_url: https://github.com/Fri3dCamp/dj_2026
  eda_tool: null
links:
- label: fri3dcamp.github.io/badge_2026/en
  url: https://fri3dcamp.github.io/badge_2026/en/
  kind: website
- label: badge_2026/dj (assembly & specs)
  url: https://fri3dcamp.github.io/badge_2026/dj/
  kind: doc
- label: Fri3dCamp/dj_2026 (GitHub)
  url: https://github.com/Fri3dCamp/dj_2026
  kind: repo
- label: Fri3d Scratcher (browser MIDI mixer demo)
  url: https://fri3dcamp.github.io/fri3d-scratcher/
  kind: website
images:
  - file: assets/images/badges/fri3d-2026/dj-controller-2026-add-on/e75cab7b3e.jpg
    source: "https://fri3dcamp.github.io/badge_2026/dj/"
    credit: "Fri3d Camp"
    caption: "The DJ Add-on kit contents"
  - file: assets/images/badges/fri3d-2026/dj-controller-2026-add-on/a3aa41624a.jpg
    source: "https://fri3dcamp.github.io/badge_2026/dj/"
    credit: "Fri3d Camp"
    caption: "The DJ Add-on fully assembled"
contact: {}
notes:
- Sweep originally spotted this only as a one-line entry ("DJ Controller — Control music and sound") on the badge_2026 overview page; confirmed on the dedicated assembly/spec page at /badge_2026/dj/.
status: released
sources:
- kind: url
  url: https://fri3dcamp.github.io/badge_2026/en/
  title: DJ Controller (2026 add-on)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://fri3dcamp.github.io/badge_2026/dj/
  title: "DJ Add-on — Fri3d Camp 2026"
  accessed: '2026-09-10'
  note: Dedicated assembly/spec page; source of MCU, inputs, LEDs, connectivity, and kit photos.
- kind: url
  url: https://github.com/Fri3dCamp/dj_2026
  title: "Fri3dCamp/dj_2026"
  accessed: '2026-09-10'
  note: GitHub repo listed as the source of hardware/firmware design files.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Maker's own documentation and GitHub repo confirm the item, its purpose, and technical specs. Price, unit quantity, and current availability are not published anywhere found; left empty rather than guessed. Did not open the GitHub repo itself to verify licensing details beyond it being publicly published.
last_modified_date: '2026-09-10'
---

The DJ Add-on is an expansion module Fri3d Camp built for its 2026 badge, turning the badge into a small USB/MIDI DJ controller. It ships as a soldering kit with six potentiometers, three faders, eight silicone buttons arranged in a 3x3 matrix (each lit from underneath by a WS2812 RGB LED), and two connectors for rotary encoders — including support for reused HDD spindle motors as janky encoders. A CH32X035 microcontroller onboard talks to the host badge over I2C and UART, and to a computer over USB, sending MIDI so the controller can mix music tracks.

Fri3d Camp built a companion browser tool, the "Fri3d Scratcher," to demonstrate mixing with the controller, and firmware can be updated through Fri3d's web flasher. Hardware and firmware design files are published on GitHub at Fri3dCamp/dj_2026. The documentation walks through full assembly with photos, but does not state a price, production quantity, or whether kits are still available after the event.
