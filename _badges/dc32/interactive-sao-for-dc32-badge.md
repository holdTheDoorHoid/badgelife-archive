---
title: Interactive SAO for DC32 Badge
id: dc32-interactive-sao-for-dc32-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: MakeItHackin
summary: A demo/teaching SAO for the DEF CON 32 badge that can be switched between LED output and button input, meant to show off both directions of the SAO interface.
functions: 'Switches between two modes via a slide switch on the User 1 line: LED output mode (drives either a NeoPixel/WS2812 RGB LED or a discrete LED) or button input mode (sends a configurable high or low signal on button press). User 1 and User 2 lines are broken out as GPIO28/GPIO29; I2C SDA/SCL lines are present but not exercised in the demo.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: null
  leds:
    count: 1
    type: WS2812
    note: Also supports a discrete LED instead of the NeoPixel, selectable by the same switch.
  display: none
  connectivity:
  - i2c
  sao_version: v1
get_one:
  price: $20.00
  price_usd: 20.0
  quantity: ''
  availability: limited
  availability_note: Tindie listing showed "Only 4 left in stock" as of 2026-09-07.
  distribution:
  - purchase
  where: Sold on Tindie by MakeItHackin.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: The maker's GitHub repo (linked from the listing) holds a README/tutorial and product photos only; no schematic, PCB, or firmware files are published there.
links:
- label: www.tindie.com/products/makeithackin/interactive-sao-for-dc32-badge
  url: https://www.tindie.com/products/makeithackin/interactive-sao-for-dc32-badge/
  kind: store
- label: github.com/MakeItHackin/InteractiveSAO
  url: https://github.com/MakeItHackin/InteractiveSAO/
  kind: doc
  note: Tutorial/documentation repo with photos; no design files.
  archived: https://web.archive.org/web/20260508145218/https://github.com/MakeItHackin/InteractiveSAO/
- label: 'YouTube: Interactive SAO for DEF CON 32 Badge demo'
  url: https://youtu.be/WPPUDujF5oE
  kind: video
images:
- file: assets/images/badges/dc32/interactive-sao-for-dc32-badge/2842b23a72.jpg
  source: https://www.tindie.com/products/makeithackin/interactive-sao-for-dc32-badge/
  credit: MakeItHackin
  caption: The Interactive SAO plus included stickers and googly eyes
- file: assets/images/badges/dc32/interactive-sao-for-dc32-badge/8d1c1b0453.jpg
  source: https://www.tindie.com/products/makeithackin/interactive-sao-for-dc32-badge/
  credit: MakeItHackin
  caption: Front of the Interactive SAO board
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/makeithackin/interactive-sao-for-dc32-badge/
  title: Interactive SAO for DC32 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc32''.'
- kind: url
  url: https://github.com/MakeItHackin/InteractiveSAO/
  title: MakeItHackin/InteractiveSAO
  accessed: '2026-09-07'
  note: Confirmed the repo is documentation/photos only, no published hardware or firmware files.
  archived: https://web.archive.org/web/20260508145218/https://github.com/MakeItHackin/InteractiveSAO/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: MCU is not stated anywhere in the listing or repo (the tutorial uses an external "badge simulator" Arduino, which is not the SAO itself, so it was not recorded as tech.mcu). Quantity made is not stated, only remaining stock (4) at the time of checking. Price is confirmed at $20 from the Tindie schema data.
last_modified_date: '2026-09-07'
---

The Interactive SAO for DC32 Badge is a small teaching/demo add-on built by MakeItHackin (Huntsville, Alabama) for DEF CON 32 in 2024. Rather than being a themed novelty, it is explicitly built to show off both directions of the SAO interface: a slide switch on the User 1 line puts it into either LED output mode, where it drives a WS2812 NeoPixel or a plain discrete LED, or button input mode, where a press sends a configurable high or low signal back to the host badge. User 1 and User 2 are broken out as GPIO28/GPIO29, and I2C lines are present on the header for debugging, though unused in the demo itself.

It was sold on Tindie for $20, packaged with a handful of stickers (Hacker Summer Camp, Make It Hacken, DC32 Engage, DC32 Flipboard) and a pair of googly eyes for decoration. The maker published a companion GitHub repo and a YouTube walkthrough covering the pinout and both operating modes, but the repo itself holds only the tutorial writeup and product photos rather than schematics, PCB files, or firmware.

Confidence is medium: the Tindie listing and its embedded product schema confirmed the price, description, and photos, and the GitHub repo was checked directly to confirm no design files are published there. The MCU used inside the SAO is not stated by the maker anywhere reviewed.
