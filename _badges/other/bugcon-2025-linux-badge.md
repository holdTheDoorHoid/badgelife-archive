---
title: BugCON 2025 Linux Badge
id: other-bugcon-2025-linux-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: Electronic Cats
  url: https://github.com/ElectronicCats
summary: The official BugCON 2025 badge, an open-hardware Linux single-board computer built around the RV1106G3 SoC (based on the Luckfox Pico Pro Max), with an addressable RGB Neopixel strip and a companion expansion board.
functions: 'Boots embedded Linux with Python 3.11 preinstalled; controls 8 WS2812E Neopixels over SPI; exposes GPIO/UART/SPI/I2C/USB/Ethernet for hacking and development; supports external cameras via MIPI CSI and audio in/out via an onboard codec.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
  - learn to solder
tech:
  mcu: RV1106G3
  leds:
    count: 8
    type: WS2812E
    note: Neopixels, driven over SPI
  display: none
  connectivity:
  - usb
  - uart
  - i2c
  - audio
  battery: 18650 Li-ion (with buck converter power management)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ElectronicCats/badge-bugcon-2025
  firmware_url: https://github.com/ElectronicCats/luckfox-pico/tree/bugcon2025
  eda_tool: KiCad
links:
- label: github.com/ElectronicCats/badge-bugcon-2025
  url: https://github.com/ElectronicCats/badge-bugcon-2025
  kind: repo
- label: ElectronicCats/luckfox-pico (bugcon2025 branch)
  url: https://github.com/ElectronicCats/luckfox-pico/tree/bugcon2025
  kind: repo
images: []
contact: {}
notes:
- 'Official BugCON 2025 badge: an open-hardware Linux badge built around the RV1106G3 SoC (ARM Cortex-A7 + RISC-V MCU + NPU) with WS2812 NeoPixels. Found by the event-year sweep, task general-2025.'
- "Sweep's title matched the maker's own naming (repo README calls it 'Badge BugCon 2025' / 'BugCon Badge 2025'); kept as-is."
status: listed
sources:
- kind: url
  url: https://github.com/ElectronicCats/badge-bugcon-2025
  title: BugCON 2025 Linux Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2025); event read as ''BugCON 2025''.'
- kind: url
  url: https://github.com/ElectronicCats/badge-bugcon-2025
  title: 'ElectronicCats/badge-bugcon-2025 README'
  accessed: '2026-09-08'
  note: 'Confirmed maker, chip (RV1106G3, Luckfox Pico Pro Max base), 8x WS2812E LEDs, 18650 battery support, connectivity, and that hardware/firmware are open source (KiCad design files plus a dedicated branch of the ElectronicCats/luckfox-pico SDK repo). No price, quantity, or availability info published.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own GitHub repo (README + file listing). No pricing, quantity, or distribution details are published anywhere in the repo, so get_one fields are left empty. No standalone photo of the assembled badge exists in the repo — only wiring/pinout diagrams (serial.png, general_protocol*.png, usb_*.png, ethernet.png, codec.png) — so no images were saved per the guide''s "item itself, not a diagram" rule. No BugCON event id exists yet in _data/events.yml, so event is left as "other"; this is BugCON 2025 (Mexico City-based hacker conference). The repo also documents an "Add-On" expansion board (PY32F002AA15M MCU) sold/distributed alongside the main badge, which could merit its own entry if photos or details surface later.'
last_modified_date: '2026-09-08'
---

The BugCON 2025 badge is Electronic Cats' first embedded-Linux conference badge, built on the RV1106G3 system-on-chip (an ARM Cortex-A7 paired with a RISC-V co-processor, an NPU, and an image signal processor) rather than the microcontrollers used in the maker's earlier badges. The design is based on the Luckfox Pico Pro Max reference hardware, boots a full Linux userspace with Python 3.11 preinstalled, and exposes GPIO, UART, SPI, I2C, USB, and Ethernet so attendees can treat it as a small hacking computer rather than just a blinky accessory. Eight WS2812E addressable Neopixels, driven over SPI, provide the badge's lighting, and it can run from an 18650 Li-ion cell through an onboard buck converter.

The project ships as two boards: the main badge itself, and a separate "Add-On" expansion board built around a PY32F002AA15M microcontroller that adds further capability and its own decorative design. Both the hardware (KiCad files) and firmware/SDK (a dedicated `bugcon2025` branch of Electronic Cats' `luckfox-pico` repo) are published as open source. No pricing, production quantity, or distribution details were found in the repository or elsewhere, so those fields are left blank pending further sources.
