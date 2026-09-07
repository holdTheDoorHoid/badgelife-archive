---
title: micropython-dc32 (unnamed badge/firmware project)
id: dc32-micropython-dc32-unnamed-badge-firmware-project
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: unknown
event: dc32
year: 2024
makers:
- name: p0ns
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
- label: github.com/p0ns/micropython-dc32
  url: https://github.com/p0ns/micropython-dc32
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: not_an_item
sources:
- kind: url
  url: https://github.com/p0ns/micropython-dc32
  title: micropython-dc32 (unnamed badge/firmware project)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc32''.'
- kind: url
  url: https://raw.githubusercontent.com/p0ns/micropython-dc32/main/README.md
  title: micropython-dc32 README
  accessed: '2026-09-07'
  note: Build/flash instructions confirming this is a MicroPython firmware port for RP2350, not a hardware design.
- kind: url
  url: https://raw.githubusercontent.com/p0ns/micropython-dc32/main/main.py
  title: micropython-dc32 main.py
  accessed: '2026-09-07'
  note: Demo script drives an ST7789 TFT and a 9-pixel NeoPixel strip and shows a PNG, matching the official DEF CON 32 badge's known hardware.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: This is a small firmware repo, not a distinct badge or SAO. It documents how to build a custom MicroPython
    (with the st7789_mpy display driver) for the RP2350 and flash it onto a badge, plus a demo main.py that drives
    an ST7789 TFT and 9 NeoPixels and shows an image (lhc-320x240.png) - hardware that matches the official DEF CON 32
    badge, so this looks like a hack/mod for running MicroPython on the stock con badge rather than an independent
    creation. No hardware files, BOM, store listing, or product name are given. Set to not_an_item per the research
    guide's "tool/tutorial" case.
last_modified_date: '2026-09-07'
---

`micropython-dc32` is a small firmware repository by GitHub user p0ns, published around DEF CON 32 (2024), rather than a standalone badge or SAO. It gives build instructions for compiling a custom MicroPython firmware for the RP2350 (Raspberry Pi Pico 2 chip) with the `st7789_mpy` display driver, and includes a demo `main.py` that drives an ST7789 TFT screen and a 9-pixel NeoPixel strip, cycling rainbow colors and displaying a bundled image.

The display and LED setup in the demo code matches the hardware of the official DEF CON 32 badge, suggesting this project is a guide for getting MicroPython running on the stock con badge rather than a maker's independent hardware design. There is no product name, hardware design, BOM, or store listing associated with it, so it does not fit the archive's badge/SAO criteria and is recorded here as a reference/tool entry rather than a catalog item.

