---
title: Not Just a Crosswalk
id: dc34-not-just-a-crosswalk
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: RivaClan
  url: https://github.com/keeloi79
summary: An 18-LED rainbow SAO from RivaClan (Caelyb Riva) built as a hardware protest against 2025-2026 removals of rainbow crosswalk street art in Florida and Texas cities.
functions: Two tactile buttons cycle through LED animation effects and color palettes; a persistent-memory system on the CH32V003 saves the last-used effect and palette across power cycles. Can be worn powered by USB-C or plugged into a host badge's SAO port.
look:
  colors: [black, multicolor]
  shape: rectangle
  themes: [pride, security, hardware tool]
tech:
  mcu: CH32V003
  leds:
    count: 18
    type: WS2812-2020 (side-emitting, SK6812D-EC3210R)
    note: Custom-tuned PWM for a flicker-free pulse/breathing effect down to 1% duty cycle.
  display: none
  connectivity: []
  inputs:
  - buttons
  battery: null
  power: USB-C or SAO header (3.3V step-up via MT3608L boost converter)
  sao_version: v1.69bis / v2
  sao_ports: 1
get_one:
  price: $35
  price_usd: 35.0
  quantity: ''
  availability: unknown
  availability_note: 'Checked 2026-09-06: no separate storefront listing found beyond the maker''s Ko-fi page, which returned an access error when checked.'
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/keeloi79/not-a-crosswalk-sao
  firmware_url: https://github.com/keeloi79/not-a-crosswalk-sao
  gerbers_url: null
  bom_url: https://github.com/keeloi79/not-a-crosswalk-sao/blob/main/docs/BOM.md
  eda_tool: EasyEDA
  license: 'GPL-3.0 (firmware), CERN-OHL-S-2.0 (hardware), CC-BY-SA-4.0 (docs)'
  fab_url: null
  notes: PCB assembly was done through JLCPCB. LED driver code builds on Blake Sands' open WS2812 driver for the CH32V003.
links:
- label: ko-fi.com/caelybr
  url: https://ko-fi.com/caelybr
  kind: store
- label: github.com/keeloi79/not-a-crosswalk-sao
  url: https://github.com/keeloi79/not-a-crosswalk-sao
  kind: repo
- label: cdn.discordapp.com/attachments/614861657004310530/1512614773915652228/IMG_2982.mov?ex=6a4ba009&is=6a4a4e89&hm=a4dca3b820a3f9e9f690449d089838d2bd432553027ad043e860dad4b5a172af&
  url: https://cdn.discordapp.com/attachments/614861657004310530/1512614773915652228/IMG_2982.mov?ex=6a4ba009&is=6a4a4e89&hm=a4dca3b820a3f9e9f690449d089838d2bd432553027ad043e860dad4b5a172af&
  kind: video
images:
- file: assets/images/badges/dc34/not-just-a-crosswalk/7c4667834c.png
  source: "https://github.com/keeloi79/not-a-crosswalk-sao"
  credit: "keeloi79 (Caelybr)"
  caption: "The SAO lit in various color patterns, spelling out NOT JUST A CROSSWALK across its rainbow LED bars"
- file: assets/images/badges/dc34/not-just-a-crosswalk/cb949402c8.jpg
  source: "https://github.com/keeloi79/not-a-crosswalk-sao"
  credit: "keeloi79 (Caelybr)"
  caption: "Close-up of the rainbow WS2812 LED array lit through the crosswalk-style cutout pattern"
contact:
  discord: Caelyb
  emails:
  - caelyb@caelyb.com
  handles:
  - '@caelybr'
  raw:
  - 'Insta:'
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 30
  updated: 7/5/2026 17:19:17
  listing: New
- kind: url
  url: https://github.com/keeloi79/not-a-crosswalk-sao
  title: "not-a-crosswalk-sao (GitHub repo)"
  accessed: '2026-09-06'
  note: "Primary source: README and inline docs give the mission statement, LED/MCU specs, power design, buttons, licensing, and credits."
- kind: url
  url: https://github.com/keeloi79
  title: "keeloi79 (GitHub profile)"
  accessed: '2026-09-06'
  note: "Confirms the maker's name as Caelyb Riva, Instagram handle caelybr; no direct mention of 'RivaClan' but the surname Riva matches the sheet's maker name."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Ko-fi page (ko-fi.com/caelybr) returned HTTP 403 on fetch, so price/availability/quantity beyond the sheet''s $35 could not be confirmed there. No separate storefront or Hackaday.io project page was found. Quantity made and current availability are unknown. The linked Discord video attachment was not fetched (attachment URL, not a page). Type set to sao (not badge) based on the repo describing it as a "Simple Add-On (SAO) designed for Defcon 34," though the sheet''s functions text says it can also be worn standalone via USB-C.'
last_modified_date: '2026-09-06'
---

Not Just a Crosswalk is a rainbow-lit SAO built by RivaClan (Caelyb Riva, aka Caelybr) for DEF CON 34. Eighteen side-emitting WS2812-2020 LEDs shine through a crosswalk-striped cutout in the PCB silkscreen, driven by a CH32V003 RISC-V microcontroller with two tactile buttons — one to cycle LED effects, one to change color palettes — and flash memory that remembers the last settings used. It runs standalone on USB-C or draws power through a host badge's SAO header, with an onboard boost converter and auto-switching MOSFET so the LEDs stay at full brightness either way.

The project's README frames it explicitly as a hardware protest: the maker built it in response to state-mandated removals of rainbow crosswalk street art in Miami Beach, Austin, Gainesville, and San Antonio during 2025 and 2026. Hardware, firmware, and documentation are all published on GitHub under open licenses (CERN-OHL-S-2.0 for the hardware, GPL-3.0 for the firmware), with PCB assembly handled by JLCPCB and the low-level LED driver code built on Blake Sands' open-source WS2812 driver for the CH32V003.

## Make your own

The GitHub repository (github.com/keeloi79/not-a-crosswalk-sao) has everything needed to build one: `docs/HARDWARE.md` covers the schematic and PCB layout, `docs/firmware.md` covers build/flash instructions (programmed via a WCH-LinkE SWIO adapter), and `docs/BOM.md` lists the components, sourced and assembled through JLCPCB.
