---
title: Etch sAo Sketch
id: supercon-2024-etch-sao-sketch-2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Andy Geppert (ageppert)
  url: https://hackaday.io/ageppert
summary: An Etch A Sketch-styled SAO with a 1.5-inch 128x128 grayscale SSD1327 OLED, two trim-pot knobs with 3D-printed caps, and a LIS3DH 3-axis accelerometer, all exposed over I2C to the host badge, built for the Supercon 8 (2024) SAO contest with a later V1.3 run manufactured by Elecrow for Hackaday Europe 2025.
functions: "Draws on the OLED as you turn the two potentiometer knobs, Etch-A-Sketch style; the LIS3DH accelerometer can also drive it (e.g. shake-to-clear or tilt input), and since it exposes raw I2C, host badges can run their own demos such as Pong or Snake on the screen."
look:
  colors: []
  shape: null
  themes: [retro computer, art, hardware tool]
tech:
  mcu: none
  leds: null
  display: 1.5" 128x128 grayscale OLED (SSD1327, I2C 0x3C/0x3D)
  connectivity: [i2c]
  inputs: [rotary encoder, accelerometer]
  battery: powered by host badge
  sao_version: null
get_one:
  price: $29
  price_usd: 29
  quantity: ''
  availability: limited
  availability_note: "Tindie listing showed 3 units in stock (pre-assembled, with case) as of 2026-09-07; a companion 'SAO Demo Controller' add-on showed 1 unit in stock."
  distribution: [purchase]
  where: Sold pre-assembled (with case) on Tindie by Machine Ideas, LLC; earlier V1.0/V1.1 runs were sold as kits.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  firmware_url: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  eda_tool: null
links:
- label: hackaday.io/project/197581-etch-sao-sketch
  url: https://hackaday.io/project/197581-etch-sao-sketch
  kind: hackaday
- label: github.com/ageppert/SAO_Etch_sAo_Sketch
  url: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  kind: repo
- label: www.tindie.com/products/36383
  url: https://www.tindie.com/products/36383/
  kind: store
images:
  - file: assets/images/badges/supercon-2024/etch-sao-sketch-2/fac7f899d1.jpg
    source: "https://hackaday.io/project/197581-etch-sao-sketch"
    credit: "Andy Geppert"
    caption: "Etch sAo Sketch SAO with OLED display and knobs"
  - file: assets/images/badges/supercon-2024/etch-sao-sketch-2/5ca5e164b0.jpg
    source: "https://www.tindie.com/products/36383/"
    credit: "Machine Ideas, LLC"
    caption: "Etch sAo Sketch assembled with case, drawing a heart on the OLED"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197581-etch-sao-sketch
  title: Etch sAo Sketch
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  title: "ageppert/SAO_Etch_sAo_Sketch"
  accessed: '2026-09-07'
  note: "Confirmed hardware/firmware are open source; version history (V1.0 Supercon 8, V1.1 Tindie batch, V1.3 Elecrow run for Hackaday Europe 2025); noted I2C pull-up resistance issue and fixes across revisions."
- kind: url
  url: https://www.tindie.com/products/36383/
  title: "SAO Etch sAo Sketch OLED - Tindie"
  accessed: '2026-09-07'
  note: "Price ($29), stock level (3 units), pre-assembled-with-case format, seller (Machine Ideas, LLC), I2C addresses for OLED and accelerometer, mention of optional SAO Demo Controller add-on."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: "No onboard MCU (tech.mcu set to 'none' per guide, since it is a passive I2C peripheral needing a host badge to drive it); leds, shape, sao_version, quantity made, and EDA tool were not stated on any source and are left empty. Price/stock reflect a live Tindie listing checked 2026-09-07 and will drift over time."
last_modified_date: '2026-09-07'
---

The Etch sAo Sketch is Andy Geppert's entry to the Supercon 8 (2024) SAO contest, riffing on the classic Etch-A-Sketch toy as a plug-in add-on for a badge's SAO header. It has no microcontroller of its own: a 1.5-inch 128x128 grayscale SSD1327 OLED and an LIS3DH 3-axis accelerometer sit on the I2C bus, and two potentiometers (fitted with 3D-printed knob caps) feed position into the accelerometer's analog inputs, so whatever host badge is plugged in does the actual drawing logic. Because it just exposes raw I2C peripherals, hosts have run things on it beyond Etch-A-Sketch drawing, including simple games like Pong and Snake.

The design has gone through several hardware revisions: V1.0 was the original Supercon 8 board, V1.1 was a small Tindie batch with a refined potentiometer range and SAO header tweaks, and V1.3 was manufactured by Elecrow for Hackaday Europe 2025 with the I2C pull-up resistors removed to fix a compatibility issue caused by excessive combined pull-up resistance when stacked with a host badge's own pull-ups. As of this research pass it is sold pre-assembled with a case through Tindie (seller Machine Ideas, LLC) for $29, with a separate "SAO Demo Controller" add-on available so the SAO can run standalone demo firmware without a host badge.

Hardware design files and firmware are published on GitHub (ageppert/SAO_Etch_sAo_Sketch), covering the schematic/PCB source, Arduino firmware, and mechanical files for the 3D-printed knob caps and case, though the repository does not spell out a specific open-source license, BOM file, or EDA tool by name.
