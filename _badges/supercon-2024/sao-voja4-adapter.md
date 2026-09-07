---
title: SAO Voja4 Adapter
id: supercon-2024-sao-voja4-adapter
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Andy Geppert
- name: Koppany Horvath
summary: A small adapter board that lets the Voja4 badge speak I2C (and possibly SPI) over a standard 6-pin SAO socket.
functions: Bridges the Voja4 badge's native interface to a full 6-pin SAO port using discrete transistors, so the badge does not need its own I2C address; provides separate, mutually-exclusive I2C and SPI wiring zones and configurable GPIO1/GPIO2 (input or output) via solder jumpers, plus an optional 3.3V regulator for alternate power input.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ageppert/SAO_Voja4_Adapter
  firmware_url: null
  eda_tool: null
links:
- label: github.com/ageppert/SAO_Voja4_Adapter
  url: https://github.com/ageppert/SAO_Voja4_Adapter
  kind: repo
- label: hackaday.io/project/198394
  url: https://hackaday.io/project/198394-sao-adapter-for-voja4-badge
  kind: hackaday
images:
- file: assets/images/badges/supercon-2024/sao-voja4-adapter/7fe0b9f045.jpg
  source: "https://github.com/ageppert/SAO_Voja4_Adapter"
  credit: "Andy Geppert"
  caption: "SAO Voja4 Adapter connected to an SAO OLED demo"
- file: assets/images/badges/supercon-2024/sao-voja4-adapter/f3a67d20f0.png
  source: "https://github.com/ageppert/SAO_Voja4_Adapter"
  credit: "Andy Geppert"
  caption: "Render of the SAO Voja4 Adapter V1 board, front side"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/ageppert/SAO_Voja4_Adapter
  title: SAO_Voja4_Adapter
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''unknown''.'
- kind: url
  url: https://github.com/ageppert/SAO_Voja4_Adapter/blob/main/README.md
  title: "SAO VOJA4 BADGE ADAPTER README"
  accessed: '2026-09-07'
  note: "Confirmed purpose (I2C/SPI bridge to a 6-pin SAO socket), image filenames, and the Hackaday.io project link."
- kind: url
  url: https://hackaday.io/project/198394-sao-adapter-for-voja4-badge
  title: "SAO Adapter for Voja4 Badge - Hackaday.io"
  accessed: '2026-09-07'
  note: "Confirmed the project was submitted to the Supercon 8 (2024) SAO Contest, with a goal of prototypes ready for Supercon 2024; named the second maker Koppany Horvath; described solder-jumper configurable I2C/SPI zones and GPIO1/2, and an optional 3.3V regulator; hardware is open (Documentation, Electronic Design, Firmware, and Manufacturing Output folders on GitHub)."
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: This is an SAO accessory adapter (not itself a con badge) that adds a 6-pin SAO socket to the Voja4 badge, made for the Supercon 8 (2024) SAO Contest. The Voja4 badge itself is a separate, third-party badge and was not otherwise investigated here. No MCU is on the adapter itself (it's passive/discrete-transistor logic), so tech.mcu is set to "none". EDA tool, license, price, and quantity made were not stated in the repo or Hackaday.io page and are left empty. Removed an unsupported claim that GPIO1/GPIO2 could be configured for UART; only input/output selection is documented. The repo also contains firmware (asm/hex) for a separate SAO OLED demo device used to test the adapter, not for the adapter itself (which has no MCU); make_your_own.firmware_url is left empty and open_source kept "partial" on that basis, since no explicit license was found for the hardware design either. Verified against the maker's own GitHub repo/README and Hackaday.io project page; both saved images were confirmed present in the repo's Images folder with matching dimensions.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/sao-voja4-adapter/
---

The SAO Voja4 Adapter is a small accessory board by Andy Geppert and Koppany Horvath that gives the Voja4 badge a standard 6-pin Simple Add-On (SAO) socket. Rather than exposing the badge's own I2C address, the adapter uses discrete transistors to bridge the badge's native interface out to full SAO-compatible I2C, with an alternate SPI wiring path (the two are mutually exclusive, selected with solder jumpers). GPIO1 and GPIO2 can likewise be configured as inputs or outputs, and an optional onboard 3.3V regulator supports powering the adapter from an alternate source.

The project was entered in the Supercon 8 (2024) SAO Contest, with the team aiming to have working prototypes on hand for testing at Hackaday Supercon 2024. It is documented on Hackaday.io (project #198394) and on GitHub, where the repository is organized into Documentation, Electronic Design, Firmware, and Manufacturing Output folders — suggesting the hardware design was intended to be shared, though no explicit open-source license was located. No pricing, production quantity, or ongoing availability information was found.
