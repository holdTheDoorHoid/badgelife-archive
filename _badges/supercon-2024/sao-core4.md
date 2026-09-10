---
title: SAO Core4 - A Nibble of Core Memory with I2C
id: supercon-2024-sao-core4
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Andy Geppert
  url: https://hackaday.io/andy-geppert
- name: Koppany Horvath
  url: null
summary: An SAO holding four bits of real ferrite core memory backlit by orange LEDs, read and written over I2C through a GPIO expander, with dual SAO ports for stacking, a hidden QWIIC/STEMMA QT port, jumper-selectable I2C address and a magnetic stylus for playing a memory game; the board was shrunk to 1.5 x 2 inches to meet the Supercon 8 SAO contest rules.
functions: Displays and lets you set 4 bits of physical core memory over I2C; includes a resettable sense/latch circuit, an onboard memory demo game playable with a magnetic stylus, and pass-through I2C so any host badge (6502, Voja4, Z80, etc.) can bit-bang the protocol.
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - hardware tool
  - learn to solder
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Early hand-reworked V0.1.1 kits were handed out at VCF Midwest 2024; Version 0.2 was brought to Supercon 8 (2024) for the Add-on Contest. No storefront or fixed price found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/ageppert/SAO_CORE4
  firmware_url: https://github.com/ageppert/SAO_CORE4
  eda_tool: null
links:
- label: github.com/ageppert/SAO_CORE4
  url: https://github.com/ageppert/SAO_CORE4
  kind: repo
- label: hackaday.io/project/197235-sao-core4-a-nibble-of-core-memory-with-i2c
  url: https://hackaday.io/project/197235-sao-core4-a-nibble-of-core-memory-with-i2c
  kind: hackaday
  archived: https://web.archive.org/web/20251018074830/https://hackaday.io/project/197235-sao-core4-a-nibble-of-core-memory-with-i2c
- label: hackaday.io/project/197235/logs
  url: https://hackaday.io/project/197235/logs
  kind: hackaday
- label: www.hackster.io/news/andy-geppert-s-sao-core4-adds-nostalgic-four-bit-memory-tech-to-modern-conference-badges-05f3bf6c8300
  url: https://www.hackster.io/news/andy-geppert-s-sao-core4-adds-nostalgic-four-bit-memory-tech-to-modern-conference-badges-05f3bf6c8300
  kind: article
images:
- file: assets/images/badges/supercon-2024/sao-core4/e8c608b054.jpg
  source: https://github.com/ageppert/SAO_CORE4
  credit: Andy Geppert
  caption: Render of the SAO Core4 board, front view
- file: assets/images/badges/supercon-2024/sao-core4/1ab6ad9178.jpg
  source: https://github.com/ageppert/SAO_CORE4
  credit: Andy Geppert
  caption: Physical prototypes of the SAO Core4 board
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/ageppert/SAO_CORE4
  title: SAO_CORE4 - A Nibble of Core Memory
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/197235-sao-core4-a-nibble-of-core-memory-with-i2c
  title: SAO Core4 - A Nibble of Core Memory with I2C
  accessed: '2026-09-07'
  note: Confirmed maker team (Andy Geppert with Koppany Horvath), core feature set, MCP23017 GPIO expander driving the 4-bit core matrix and LEDs, dual SAO ports, QWIIC/STEMMA QT pass-through, and that it was submitted to both the Tiny Games Challenge and the Supercon 8 (2024) SAO contest.
  archived: https://web.archive.org/web/20251018074830/https://hackaday.io/project/197235-sao-core4-a-nibble-of-core-memory-with-i2c
- kind: url
  url: https://hackaday.io/project/197235/logs
  title: SAO Core4 build logs
  accessed: '2026-09-07'
  note: Confirmed hardware version history (V0.1.0 through V1.2), that V0.1.1 rework kits were given out at VCF Midwest 2024, and that V0.2 was the version brought to Supercon 2024 for the Add-on Contest. No price or production quantity was stated.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own GitHub and Hackaday.io project pages confirm what the badge is, its purpose, and that it was built for Supercon 8's 2024 SAO contest, so core facts are maker-sourced. No LED count/type, price, or production quantity was published anywhere found; left empty rather than guessed. Hackster.io coverage exists but the article page returned a Cloudflare block (HTTP 403) and could not be read. tech.mcu is set to none because the SAO itself has no microcontroller (an MCP23017 I2C GPIO expander drives it, not a program-running chip); logic/control comes from the host badge over I2C.
last_modified_date: '2026-09-07'
---

The SAO Core4, by Andy Geppert with Koppany Horvath, puts a small nibble of genuine ferrite core memory onto a Simple Add-On board. Four physical cores are wired into a matrix that a host badge can set and read over I2C, driven through an MCP23017 GPIO expander that also lights orange backlighting LEDs behind each core and manages a resettable sense/latch circuit. Because the protocol only needs bit-banged I2C, the maker's notes point out that essentially any badge platform, from a 6502 to a Voja4 to a Z80, can drive it.

The board went through several hardware revisions across 2024, shrinking from an early prototype down to a final 1.5 x 2 inch form factor to satisfy the size rules of Supercon 8's SAO/Add-on Contest, which is what version 0.2 was built for. Along the way it picked up two stacked SAO ports for daisy-chaining other add-ons, a hidden QWIIC/STEMMA QT connector, a jumper-selectable I2C address, and a small onboard memory game played with a magnetic stylus. Early hand-reworked V0.1.1 kits were given out to a smaller audience at VCF Midwest 2024 before the Supercon-ready V0.2 was finished.

Hardware and firmware are both published on GitHub, including datasheets, an Arduino demo, and manufacturing files, but no fixed retail price, production quantity, or ongoing storefront was found in any source consulted.

## Make your own

The [SAO_CORE4 GitHub repository](https://github.com/ageppert/SAO_CORE4) contains the electronic design files, manufacturing outputs, datasheets for the core memory components and MCP23017, and an Arduino-compatible firmware demo (originally targeting an RP2040-Zero for bench testing) that shows how to drive the board over I2C.
