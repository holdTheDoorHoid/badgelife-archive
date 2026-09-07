---
title: osquery-sao — DEFCON 2024 osquery SAO
id: dc32-osquery-sao-defcon-2024-osquery-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: muffins
  url: https://github.com/muffins
summary: A small ATtiny85-based SAO that drives eight NeoPixel LEDs, made for DEF CON 32 (2024) and branded for the osquery project.
functions: Runs custom AVR firmware that drives a strip of 8 addressable RGB LEDs through a handful of color/animation modes (solid colors, breathing fade, running-light chase), with the active mode selectable over an I2C control interface (slave address 0x42); no other interactive functions are documented.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ATtiny85
  leds:
    count: 8
    type: WS2812
    note: 5050 SMD NeoPixels
  display: none
  connectivity:
  - i2c
  battery: LiPo via JST connector
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/muffins/osquery-sao
  eda_tool: null
  bom_url: https://github.com/muffins/osquery-sao#bom
  license: Apache-2.0
  notes: 'The repo published is firmware/source only ("Repo for the source code running on the DEFCON 2024 osquery SAO badge"), plus a parts BOM with DigiKey/Adafruit/Tindie links. No schematic, PCB layout, or Gerbers were found in the repo, so hardware is only partially open (BOM yes, board files no).'
links:
- label: github.com/muffins/osquery-sao
  url: https://github.com/muffins/osquery-sao
  kind: repo
images: []
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/muffins/osquery-sao
  title: osquery-sao — DEFCON 2024 osquery SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 32/2024''.'
- kind: url
  url: https://github.com/muffins/osquery-sao
  title: 'muffins/osquery-sao: Repo for the source code running on DEFCON 2024 osquery SAO badge'
  accessed: '2026-09-07'
  note: 'README, BOM, LICENSE, and src/main.cpp contents verified directly: confirms ATtiny85 MCU, 8x WS2812 (not WS2812B) 5050 NeoPixels, LiPo/JST power, SAO connector, avrdude flashing fuse settings, Apache-2.0 license, a full BOM with vendor links, and that the firmware selects its LED mode over an I2C interface (slave address 0x42). Repo contains only .gitignore/.pio/.vscode/LICENSE/README.md/platformio.ini/src(main.cpp) — no hardware/PCB files or images.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Every non-empty field and factual sentence was checked directly against the cited GitHub repo (README, BOM section, LICENSE, and src/main.cpp), fetched a second time for this pass. Two corrections: tech.leds.type was WS2812B but the repo and BOM both say plain "WS2812" (not the B variant), so the body and tech field were fixed; tech.connectivity was empty but main.cpp shows the firmware is an I2C slave (address 0x42) that receives its mode/color selection over I2C, so connectivity: [i2c] was added and the functions field updated to describe it. No press coverage, storefront, Hackaday page, or photos of the physical badge turned up in web searches ("osquery SAO DEF CON 32 muffins", "osquery-sao DEF CON 32 photo", "osquery SAO badge giveaway 2024"), so price, quantity, availability, colors, shape, and images remain empty — this is a real gap, not an oversight. Everything else in the entry is supported by the one available source (the maker''s own repo), so status is set to verified rather than researched.'
last_modified_date: '2026-09-07'
---

The osquery-sao is a Simple Add-On built for DEF CON 32 (2024) and branded for the osquery open-source endpoint-visibility project. It is a minimal blinky board: an ATtiny85 microcontroller drives eight WS2812 (NeoPixel 5050) addressable RGB LEDs, with the active color/animation mode set over an I2C control interface, powered by a small LiPo battery through a JST connector, and it plugs into a host badge via a standard SAO connector.

The maker, a GitHub user going by "muffins" (also active in the osquery open-source community, maintaining several osquery-related tooling repos), published only the firmware source and a parts BOM — DigiKey listings for the ATtiny85, resistor, switch, and JST connector, an Adafruit link for the NeoPixels, and a Tindie link for the SAO connector — under an Apache-2.0 license. No schematic, PCB layout, Gerbers, or photos of the finished board were published in the repo, and no independent coverage, storefront listing, or images of the physical SAO could be found elsewhere, so details like color, exact quantity made, and how it was distributed at DEF CON remain unknown.

## Make your own

Firmware and a BOM are available at the GitHub repo. To flash a board: build the firmware with PlatformIO (or compile for AVR) and flash with avrdude, first setting the ATtiny85 fuses with `avrdude -c usbtiny -p attiny85 -U lfuse:w:0xe2:m -U hfuse:w:0xdf:m -U efuse:w:0xff:m`. No PCB design files are published, so recreating the board itself would require reverse-engineering a layout from the BOM.
