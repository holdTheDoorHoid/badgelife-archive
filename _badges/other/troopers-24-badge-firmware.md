---
title: TROOPERS24 badge firmware
id: other-troopers-24-badge-firmware
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2024
makers:
- name: Badge.Team
  url: https://badge.team/
summary: The ESP32-based hackable badge issued at the TROOPERS24 security conference, with an SPI TFT display, keyboard, NFC reader, and SD card support.
functions: 'Runs a launcher for on-device apps built on the PAX graphics library, plus device testing/setup and over-the-air (OTA) firmware updates.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP32
  leds:
    count: null
    type: WS2812B
    note: Driven via the components/ws2812 driver in the firmware.
  display: TFT LCD (SPI, ST77xx-family driver)
  connectivity:
  - wifi
  - nfc
  - rfid
  - i2c
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/badgeteam/troopers24-firmware
  eda_tool: null
  notes: 'Firmware (MIT-licensed, ESP-IDF v4.4.7) is published; a board-support-package repo (troopers24-bsp) manages the hardware drivers, but no schematic/Gerber repo was found.'
links:
- label: github.com/badgeteam/troopers24-firmware
  url: https://github.com/badgeteam/troopers24-firmware
  kind: website
- label: github.com/badgeteam/troopers24-bsp
  url: https://github.com/badgeteam/troopers24-bsp
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sweep used the title "Troopers 24 badge firmware"; renamed to match the maker''s own repo name, "TROOPERS24 badge firmware".'
status: listed
sources:
- kind: url
  url: https://github.com/badgeteam/troopers24-firmware
  title: Troopers 24 badge firmware
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/badgeteam/troopers24-firmware
  title: 'GitHub - badgeteam/troopers24-firmware: TROOPERS24 ESP32 firmware: Launcher'
  accessed: '2026-09-10'
  note: 'README confirms this is the ESP32 firmware for the TROOPERS24 badge (Badge.Team): PAX graphics, keyboard, I2C PCA9555, ST25R3911B NFC, SD card, WS2812 LEDs, appfs, QR code, MIT license, ESP-IDF v4.4.7. The README''s component table lists "components/spi-ili9341", but the repository''s actual git tree (checked via the GitHub API) has no spi-ili9341 submodule committed - only "components/spi-st77xx" is present, so the README is stale on the display driver; corrected tech.display accordingly. main/ source files (wifi_ota.c, wifi_cert.c, wifi_defaults.c, http_download.c) confirm wifi connectivity and OTA-over-wifi.'
- kind: url
  url: https://github.com/badgeteam/eps32-component-spi-st77xx
  title: 'GitHub - badgeteam/eps32-component-spi-st77xx: ESP32 component: ST77XX LCD display'
  accessed: '2026-09-10'
  note: 'The display driver submodule actually committed in troopers24-firmware''s tree (components/spi-st77xx). README says it "should work with all ST77* drivers" but "has only been tested with ST7789VI" - used to correct tech.display from the README-table''s ILI9341 claim to a generic ST77xx description.'
- kind: url
  url: https://github.com/badgeteam/troopers24-bsp
  title: 'GitHub - badgeteam/troopers24-bsp: TROOPERS24 badge board support package'
  accessed: '2026-09-10'
  note: 'Confirms a separate ESP-IDF board-support-package repo exists for the TROOPERS24 badge hardware; its own README description text is a reused/unedited copy referring to the "MCH2022 badge" (a badge.team template artifact, not evidence this is that badge).'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Confirmed this is a real item: the actual conference badge handed out at TROOPERS24 (2024), not just a firmware-only project (repo created 2024-05-29, ahead of the June 2024 event). Fact-check pass corrected tech.display: the firmware README''s component table names an ILI9341 driver, but the repository''s actual committed submodules (verified via the GitHub API git-tree, not just the README) only include components/spi-st77xx, not spi-ili9341 - so the display field was changed from "ILI9341 TFT LCD (SPI)" to a generic ST77xx-family description, and the ILI9341 mentions were removed from the summary and body. Everything else in the entry checked out against the firmware repo, its source files (wifi_ota.c etc. confirm wifi/OTA), and the BSP repo. Could not find a dedicated badge.team documentation page, a hardware/schematic repository, price, quantity made, distribution details, LED count, battery type, exact display size, or any photos of the physical badge (checked badge.team/docs/badges/, badge.gallery, and web search - none mention a TROOPERS24 badge). The events.yml vocabulary has troopers-2019/2020/2022/2023/2025 but no "troopers-2024" id, so event is left as "other" pending that event being added; this item was made for TROOPERS (Heidelberg, Germany) 2024.'
last_modified_date: '2026-09-10'
---

The TROOPERS24 badge is the hackable conference badge given to attendees of TROOPERS 2024, the enterprise-security conference held annually in Heidelberg, Germany. As with several other TROOPERS-era badges, the firmware was built by the Dutch collective Badge.Team, continuing a collaboration that also produced badges for TROOPERS19, TROOPERS20, TROOPERS22, TROOPERS23, and TROOPERS25.

The badge runs on an ESP32 and pairs a keyboard with an SPI TFT display (driven via an ST77xx-family display driver), using Badge.Team's PAX graphics library to drive a home-screen app launcher. It also includes an ST25R3911B NFC/RFID reader, SD card storage, I2C peripheral support (via a PCA9555 I/O expander), and WS2812 addressable LEDs, plus over-the-air update support so the firmware could be patched during the event. The firmware source is MIT-licensed and published on GitHub, along with a separate board-support-package repository for the hardware drivers; no public schematic or Gerber files for the board itself were located.

No pricing, production quantity, distribution method, or photos of the physical badge were found during this pass — only the firmware and BSP repositories, which describe its capabilities but not its physical presentation.
