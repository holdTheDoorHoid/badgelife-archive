---
title: DC Zia Laser Theremin Badge
id: dc27-dc-zia-laser-theremin-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: DC Zia
  url: https://dczia.net/
- name: snurkle engineering
  url: https://www.tindie.com/stores/hamster/
  role: kit seller / hardware design
summary: A wearable "laser theremin" synth badge that uses two laser time-of-flight sensors to track hand movement and control an onboard synthesizer, letting the wearer play music by waving their hands over it.
functions: Plays like a theremin using two laser time-of-flight (VL53L0X) sensors to sense hand distance and control pitch/volume; a rotary encoder selects the waveform; has onboard speaker/amplifier and a 1/8" headphone jack for audio out; OLED display for UI; SD card storage; two SAO ports for add-ons.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - music
  - hardware tool
  - radio
tech:
  mcu: Rigado BMD-340 (NRF52-based ARM Cortex-M4F, 64MHz, Bluetooth 5)
  leds:
    count: null
    type: RGB
    note: Onboard Neopixel RGB LEDs.
  display: 0.96" OLED (SSD1306)
  connectivity:
  - bluetooth
  - uart
  - audio
  battery: null
  sao_version: null
  sao_ports: 2
  inputs:
  - buttons
  - rotary encoder
get_one:
  price: $120
  price_usd: 120
  quantity: '75'
  availability: sold_out
  availability_note: Tindie listing showed "Out of Stock" as of 2019-11-24; still listed as out of stock when checked 2026-09-07.
  distribution:
  - purchase
  - kit
  where: Sold as a partially-assembled kit (badge came with laser-cut acrylic "Key Alignment Diffuser," clicky keys, OLED screen, headers, and battery pack left for the buyer to install) via Tindie, by seller "snurkle engineering."
make_your_own:
  open_source: true
  hardware_url: https://github.com/dczia/Defcon27-Badge
  firmware_url: https://github.com/dczia/Defcon27-Badge
  gerbers_url: null
  bom_url: null
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: Hardware designed in KiCad; firmware built with GNU ARM GCC, programmed via J-Link Segger (SD-card programming was planned but noted as "coming soon" in the repo README).
links:
- label: github.com/dczia/Defcon27-Badge
  url: https://github.com/dczia/Defcon27-Badge
  kind: repo
  archived: https://web.archive.org/web/20260523084127/https://github.com/dczia/Defcon27-Badge
- label: DCZia Laser Theremin Complete Badge Kit (Tindie)
  url: https://www.tindie.com/products/hamster/dczia-laser-theremin-complete-badge-kit/
  kind: store
  archived: https://web.archive.org/web/20260503133903/https://www.tindie.com/products/hamster/dczia-laser-theremin-complete-badge-kit/
- label: DCZia Laser Theremin Blank PCB (Tindie)
  url: https://www.tindie.com/products/hamster/dczia-laser-theremin-blank-pcb/
  kind: store
  archived: https://web.archive.org/web/20260503100409/https://www.tindie.com/products/hamster/dczia-laser-theremin-blank-pcb/
- label: 'Hackaday: Pictorial Guide to the Unofficial Electronic Badges of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- label: Build Guide
  url: https://github.com/dczia/Defcon27-Badge/blob/master/BuildGuide.md
  kind: doc
  archived: https://web.archive.org/web/20260509190427/https://github.com/dczia/Defcon27-Badge/blob/master/BuildGuide.md
images:
- file: assets/images/badges/dc27/dc-zia-laser-theremin-badge/03771e00ed.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday / DC Zia
  caption: DC Zia Laser Theremin badge, front view
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- file: assets/images/badges/dc27/dc-zia-laser-theremin-badge/499e054e70.jpg
  source: https://www.tindie.com/products/hamster/dczia-laser-theremin-complete-badge-kit/
  credit: snurkle engineering / Tindie
  caption: DC Zia Laser Theremin badge kit, assembled with laser sensors visible
  archived: https://web.archive.org/web/20260503133903/https://www.tindie.com/products/hamster/dczia-laser-theremin-complete-badge-kit/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/dczia/Defcon27-Badge
  title: DC Zia Laser Theremin Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
  archived: https://web.archive.org/web/20260523084127/https://github.com/dczia/Defcon27-Badge
- kind: url
  url: https://github.com/dczia/Defcon27-Badge
  title: 'GitHub - dczia/Defcon27-Badge: DCZia Defcon27 Laser Theremin Synthesizer Badge - 2019'
  accessed: '2026-09-07'
  note: Repo README - full feature list, MCU, sensors, KiCad, build/software docs.
  archived: https://web.archive.org/web/20260523084127/https://github.com/dczia/Defcon27-Badge
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27
  accessed: '2026-09-07'
  note: Confirms VL53L0X sensor, BMD-340 module, and that 75 badges were made.
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- kind: url
  url: https://www.tindie.com/products/hamster/dczia-laser-theremin-complete-badge-kit/
  title: DCZia Laser Theremin complete badge kit from snurkle engineering on Tindie
  accessed: '2026-09-07'
  note: Price ($120), out-of-stock status, seller (snurkle engineering), kit contents and product photos.
  archived: https://web.archive.org/web/20260503133903/https://www.tindie.com/products/hamster/dczia-laser-theremin-complete-badge-kit/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: LED count not stated anywhere found; battery type not stated (kit description mentions "battery pack" installed by buyer but no chemistry/size given). A separate bare "blank PCB" version was also sold on Tindie for builders who wanted to source their own parts.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc27/dc-zia-laser-theremin-badge.glb
  method: kicad
  source_file: Hardware/laser-theremin.kicad_pcb
  generated: '2026-09-07'
  bytes: 690116
---

The DC Zia Laser Theremin Badge was the DC Zia group's unofficial badge for DEF CON 27 (2019), built around a laser theremin concept: two time-of-flight distance sensors (Adafruit VL53L0X breakouts) track how close a wearer's hands are, and that distance data drives a small onboard synthesizer, letting the wearer "play" the badge by waving their hands over it. A rotary encoder switches between waveforms, a 0.96" OLED shows badge state, and the sound comes out through an onboard speaker/amplifier or a 1/8" headphone jack. The badge runs on a Rigado BMD-340 module (an NRF52-based ARM Cortex-M4F with Bluetooth 5), stores data on an SD card, carries onboard RGB LEDs, and exposes two SAO ports for other badges to plug into.

The badge was designed in KiCad with firmware written for GNU ARM GCC, and both hardware and software were published on GitHub by the dczia organization. Roughly 75 units were made. It was sold, not fully assembled, as a kit through Tindie by seller "snurkle engineering" for $120 — buyers finished the build themselves, installing the laser-cut acrylic "Key Alignment Diffuser," the Kailh low-profile clicky keyswitches, the OLED screen, headers, and a battery pack. A bare PCB was also sold separately for anyone who wanted to source their own parts. The kit sold out and the Tindie listing has shown "Out of Stock" since November 2019.
