---
title: SAINTCON 2025 badge (compukidmike)
id: saintcon-2025-saintcon-2025-badge-compukidmike
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2025
year: 2025
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: A conference badge shaped like a comically oversized 50mm wrench, built around an ESP32-S3 with a small LCD, addressable RGB LEDs, wifi, and an embedded NFC tag used for an on-site game.
functions: Players interact with "Nuts" (separate NFC devices) that write one-time codes to the NFC tag embedded in the wrench's jaw; the badge checks those codes against a game server to award points or unlock game nodes. The badge also has a joystick-driven LVGL menu on its onboard LCD, faction-colored LED patterns, a boot-progress LED animation, and an SAO/minibadge expansion port.
look:
  colors:
  - grey
  - gold
  - black
  shape: wrench
  themes:
  - hardware tool
  - ctf
  - wearable
tech:
  mcu: ESP32-S3
  leds:
    count: null
    type: RGB
    note: Addressable RGB LEDs run along the wrench's edge via Espressif's led_strip driver; used for faction colors, a boot-progress gradient, and game-event flashes. Exact LED count not stated in the sources.
  display: small square LCD (LVGL UI)
  connectivity:
  - wifi
  - nfc
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
  open_source: true
  hardware_url: https://github.com/compukidmike/Saintcon2025/tree/main/Hardware/Badge
  firmware_url: https://github.com/compukidmike/Saintcon2025/tree/main/Firmware/badge
  eda_tool: KiCad
links:
- label: github.com/compukidmike/Saintcon2025
  url: https://github.com/compukidmike/Saintcon2025
  kind: repo
- label: Saintcon2025-Schematic.pdf
  url: https://github.com/compukidmike/Saintcon2025/blob/main/Hardware/Badge/Saintcon2025-Schematic.pdf
  kind: doc
- label: Saintcon2025-BOM.pdf
  url: https://github.com/compukidmike/Saintcon2025/blob/main/Hardware/Badge/Saintcon2025-BOM.pdf
  kind: doc
images:
- file: assets/images/badges/saintcon-2025/saintcon-2025-badge-compukidmike/94f77605e4.png
  source: https://github.com/compukidmike/Saintcon2025
  credit: compukidmike
  caption: The Saintcon 2025 badge, shaped like an oversized wrench with an embedded NFC tag
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2025
  title: SAINTCON 2025 badge (compukidmike)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''saintcon-2025''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2025/main/README.md
  title: Saintcon 2025 Badge README
  accessed: '2026-09-07'
  note: Confirms wrench shape/size, embedded NFC tag, Nuts game mechanic, and that board files + firmware are included.
- kind: url
  url: https://github.com/compukidmike/Saintcon2025/tree/main/Firmware/badge
  title: Saintcon2025 badge firmware (ESP-IDF)
  accessed: '2026-09-07'
  note: sdkconfig.defaults sets CONFIG_IDF_TARGET=esp32s3, CONFIG_INPUT_JOYSTICK_ENABLED=y, CONFIG_MINIBADGE_ENABLED=y; idf_component.yml pulls in lvgl, espressif/led_strip, and espp/st25dv (NFC), confirming MCU, joystick input, SAO/minibadge port, display UI, addressable LEDs, and NFC chip.
- kind: url
  url: https://github.com/compukidmike/Saintcon2025/tree/main/Hardware/Badge
  title: Saintcon2025 badge hardware files
  accessed: '2026-09-07'
  note: Confirms KiCad source, gerbers, schematic PDF, and BOM PDF are published for the badge PCB.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched README.md, the main repo page, the Firmware/badge file tree, sdkconfig.defaults, main/idf_component.yml, display/config.h, led_patterns.c, the AfterCon .ino, and the Hardware/Badge and Hardware/Nut file listings. Every non-empty field and every sentence in the body is directly supported: wrench shape/size/lanyard hole and the Nuts NFC game mechanic (README); ESP32-S3, LCD+LVGL, joystick input, addressable LEDs via led_strip, wifi, NFC via espp/st25dv (sdkconfig.defaults + idf_component.yml); the LVGL menu/nav UI (components/ui/screens/main/apps/menu.c, nav.c); SAO/minibadge port (CONFIG_MINIBADGE_ENABLED); secure element (CONFIG_SECURE_ELEMENT_ENABLED + ATECC608A); OTA support (badge/ota.c); KiCad/gerbers/schematic/BOM for both the badge and the Nut (Hardware/Badge, Hardware/Nut); and the unrelated AfterCon BLE volume-control Nut sketch (Firmware/AfterCon/.../Saintcon2025NutVolumeControl.ino). The saved photo is byte-for-byte the repo''s
    own SC25Badge.png, confirming colors (grey/gold/black) and shape. No corrections were needed. Still not determined from sources (left empty, correctly): exact LED count/part, exact display size/model, SAO/minibadge header version, battery capacity, and any price/quantity/availability/distribution details.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2025/saintcon-2025-badge-compukidmike.glb
  method: gerber
  source_file: Hardware/Badge/Saintcon2025Gerbers.zip
  generated: '2026-09-10'
  bytes: 183772
  size_mm:
  - 99.9
  - 248.7
---

The SAINTCON 2025 badge, made by compukidmike, takes the form of a comically oversized 50mm wrench with a 10mm lanyard hole. Under the novelty shape it is a real electronic badge built on an ESP32-S3, with a small LCD driven by LVGL, a joystick for menu navigation, addressable RGB LEDs for faction colors and animations, wifi connectivity, and an embedded NFC tag in the wrench's jaw.

The badge's central mechanic revolves around that NFC tag: attendees used separate NFC devices called "Nuts" to write one-time codes onto the badge, which the badge then submitted to a game server to award points or unlock additional game nodes. The badge also includes an SAO/minibadge expansion port, a secure element for cryptographic operations, and OTA update support.

Both the badge and the companion Nut hardware are fully open source: the repository includes KiCad source files, gerbers, schematics, and a bill of materials for both boards, along with the complete ESP-IDF firmware for the badge and the Nuts. A separate AfterCon side project (a BLE volume-control "Nut") is also included in the same repo but is unrelated to the main con game.
