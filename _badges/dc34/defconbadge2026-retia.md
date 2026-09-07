---
title: DefconBadge2026 (Retia)
id: dc34-defconbadge2026-retia
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Retia LLC
  url: https://retia.io
summary: An ESP32-S3 badge with a 2.4" color touchscreen and 915 MHz LoRa radio, built by Retia LLC for DEF CON. Ships with flashable firmware for DOOM, a full NES emulator, and mesh-networking tools (Meshtastic, MeshCore, Reticulum/RNode).
functions: 'Runs swappable firmware images: DOOM (with audio), a full NES emulator with a 37-game homebrew library and save states, Meshtastic and MeshCore mesh messaging (including full-color touchscreen messenger UIs), a Reticulum RNode LoRa transceiver, WLEDkitty, and an ESP32 Bus Pirate hardware-hacking multitool (I2C/SPI/UART/1-Wire/JTAG tools, RF waterfall/sniffer/scanner, Wi-Fi/BLE scanning).'
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - hardware tool
tech:
  mcu: ESP32-S3
  leds:
    count: 10
    type: WS2812B
    note: plus a green debug LED
  display: 2.4" ILI9341 240x320 color TFT with XPT2046 resistive touch
  connectivity:
  - wifi
  - ble
  - lora
  - meshtastic
  - usb
  - i2c
  - uart
  battery: 2x AA (boost) or USB-C, auto-switching
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/RetiaLLC/DefconBadge2026/tree/main/hardware
  firmware_url: https://github.com/RetiaLLC/DefconBadge2026/tree/main/firmware
  eda_tool: KiCad
links:
- label: github.com/RetiaLLC/DefconBadge2026
  url: https://github.com/RetiaLLC/DefconBadge2026
  kind: repo
- label: Retia LLC store (retia.io)
  url: https://retia.io
  kind: store
- label: 'GitHub: RetiaLLC/badge-launcher (Badge Launcher firmware)'
  url: https://github.com/RetiaLLC/badge-launcher
  kind: repo
images:
- file: assets/images/badges/dc34/defconbadge2026-retia/d338d9c6c6.jpg
  source: https://github.com/RetiaLLC/DefconBadge2026
  credit: Retia LLC
  caption: The badge running DOOM on its 2.4-inch touchscreen
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/RetiaLLC/DefconBadge2026
  title: DefconBadge2026 (Retia)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 2026 (ESP32-S3)''.'
- kind: url
  url: https://github.com/RetiaLLC/DefconBadge2026
  title: 'RetiaLLC/DefconBadge2026: README'
  accessed: '2026-09-07'
  note: Full spec table (MCU, display, radio, LEDs, power, expansion), firmware list, and repo layout confirmed via raw README.md.
- kind: url
  url: https://retia.io/
  title: Retia Webstore
  accessed: '2026-09-07'
  note: Checked maker storefront; the DEF CON badge is not currently listed as a purchasable product there (store sells "Nugget" boards, kits, and gear instead).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The GitHub repo is named DefconBadge2026 and its README is titled "DEF CON Badge (2026)", and search results describe it as built for DEF CON 2026 (DC34); however the repo's own GitHub description calls it the "Retia 2024 DEF CON badge" and the KiCad source file is named 2024_def_con_badge_v1.kicad_pcb, suggesting the hardware design dates to 2024 and was reused/rebadged. No price, quantity, or distribution channel was found; the badge does not appear on Retia's current storefront, so it was likely given out at an event or workshop rather than sold. Status set to released since hardware and multiple firmware releases exist and photographic evidence (DOOM screenshot) is in the repo, but where/how people obtained one is unconfirmed.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/defconbadge2026-retia/
model:
  file: assets/models/dc34/defconbadge2026-retia.glb
  method: kicad
  source_file: hardware/kicad/2024_def_con_badge_v1.kicad_pcb
  generated: '2026-09-07'
  bytes: 583452
---

The DefconBadge2026 is an ESP32-S3-based hardware platform made by Retia LLC, a company that also sells the "WiFi Nugget" line of beginner hacking boards. The badge centers on a 2.4-inch color touchscreen, a 915 MHz LoRa radio, ten WS2812B NeoPixels, a piezo buzzer, a micro-SD slot, and expansion via SAO v2, QWIIC/I2C, UART, and SPI headers. It runs on two AA batteries or USB-C power.

Rather than a single fixed firmware, the badge is designed to be reflashed with different experiences: a full-speed port of DOOM, a NES emulator with a 37-game homebrew library, and several off-grid mesh-networking builds (Meshtastic, MeshCore, and a Reticulum RNode transceiver), plus an ESP32 Bus Pirate multitool for I2C/SPI/UART/JTAG hacking and RF sniffing. Retia's companion "Badge Launcher" project lets a single flash and a micro-SD card switch between several of these modes from an on-badge menu.

The GitHub repository's own description and its KiCad source filename both refer to a "2024" badge, while the repo name and README title say "2026," so it is unclear whether this is a fresh DC34 (2026) design or an earlier badge reused and rebranded. Hardware (KiCad 8) and firmware are both published on GitHub, but no price, production quantity, or sales channel was found, and the badge is not listed on Retia's current webstore — it was most likely distributed at DEF CON or an associated workshop rather than sold as a standalone product.

## Make your own

Hardware sources (KiCad 8, schematic PDF) and firmware are in the GitHub repo. Flashing DOOM is as simple as `esptool --chip esp32s3 --port <PORT> write-flash 0x0 firmware/doom/doom-audio.factory.bin`; other firmware (Meshtastic, MeshCore, Reticulum/RNode, the ESP32 Bus Pirate, and the Anemoia NES emulator) is linked from the README along with ready-to-flash release images. Two PlatformIO/ESP-IDF example projects (`hello-badge`, `sd-test`) are included as starting templates for custom firmware.
