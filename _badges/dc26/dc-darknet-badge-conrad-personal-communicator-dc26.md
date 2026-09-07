---
title: DC Darknet Badge / Conrad Personal Communicator (DC26)
id: dc26-dc-darknet-badge-conrad-personal-communicator-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
series: Darknet
makers:
- name: cmdc0de
  url: https://github.com/cmdc0de
  role: hardware design, firmware
- name: Krux
  url: https://github.com/krux702
  role: badge look/artwork, silkscreen and acrylic puzzle design
- name: Gourry
  url: https://github.com/gourryinverse
  role: firmware
- name: Bunni
  role: hardware advice/consulting
summary: The seventh badge from Darknet Industries' annual DEF CON contest, an unpopulated STM32F411RET6 + ESP-WROOM-32 dev-kit badge with an OLED and a color LCD, built to pair with other players' badges and carry the year's Darknet puzzle contest.
functions: 'Solder-it-yourself kit that becomes a Darknet contest tool: pairs with other agents'' badges over the ESP32''s wifi/BLE, drives a 128x32 OLED (from the ESP32) and a 1.8" color LCD (from the STM32), and carries silkscreen and acrylic puzzles to solve. As a dev kit it exposes ST-Link and ESP32 programming headers so owners can flash their own code and add optional programmable APA-106/APA-102 LEDs. Two SAO headers (one normal, one mirrored) let it take add-ons, including the maker''s own "Eggplant" SAO built into the same kit release.'
look:
  colors: []
  shape: null
  themes:
  - security
  - privacy
  - puzzle
tech:
  mcu: STM32F411RET6 + ESP-WROOM-32
  leds:
    count: 2
    type: discrete
    note: Two standard LEDs (LED2/LED3) ship populated; the board also has unpopulated pads for a set of programmable APA-106 through-hole LEDs on the front and APA-102 SMD LEDs on the back that the builder can add.
  display: 128x32 OLED (driven by the ESP32) + 1.8" color LCD (driven by the STM32)
  connectivity:
  - wifi
  - ble
  inputs:
  - buttons
  battery: LiPo (capacity not stated), JST connector
  sao_version: null
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: over 1200 units made
  availability: unknown
  distribution:
  - kit
  - contest
  where: Distributed as a solder-it-yourself kit to entrants in DEF CON 26's Darknet contest; badges shipped without contest firmware and were updated at the Darknet table in the contest area.
make_your_own:
  open_source: true
  hardware_url: https://github.com/thedarknet/dc26-badge/tree/master/hardware
  firmware_url: https://github.com/thedarknet/dc26-badge/tree/master/firmware
  eda_tool: Eagle
  license: MIT
  notes: The same repo also carries hardware and firmware for the "Eggplant" SAO (ATtiny85) that Krux designed to go with this badge.
links:
- label: github.com/thedarknet/dc26-badge
  url: https://github.com/thedarknet/dc26-badge
  kind: repo
  archived: https://web.archive.org/web/20260907115647/https://github.com/thedarknet/dc26-badge
- label: DarkNet 2018 Badge Kit assembly instructions (Wayback Machine)
  url: https://web.archive.org/web/20260319125018/https://dcdark.net/badge7/index.html
  kind: doc
images: []
contact: {}
notes:
- over 1200 units made
status: released
sources:
- kind: url
  url: https://github.com/thedarknet/dc26-badge
  title: DC Darknet Badge / Conrad Personal Communicator (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
  archived: https://web.archive.org/web/20260907115647/https://github.com/thedarknet/dc26-badge
- kind: url
  url: https://github.com/thedarknet/dc26-badge
  title: thedarknet/dc26-badge
  accessed: '2026-09-07'
  note: README, repo tree, LICENSE (MIT) confirm STM32+ESP32 firmware, Eagle hardware files, and that the "Eggplant" SAO ships from the same repo.
  archived: https://web.archive.org/web/20260907115647/https://github.com/thedarknet/dc26-badge
- kind: url
  url: https://web.archive.org/web/20260319125018/https://dcdark.net/badge7/index.html
  title: DarkNet 2018 Badge Kit (assembly instructions)
  accessed: '2026-09-07'
  note: Maker's own assembly guide (only reachable via Wayback Machine; current dcdark.net is a JS SPA with no static page there). Gives the official board name "Darknet Industries, Conrad Personal Communicator", full parts list, maker credits/roles, SAO details, and Eggplant SAO description.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'PCB color/shape and any price were not stated anywhere found; left empty. The two badge photo URLs referenced from the assembly page (dcdark.net/badge7/image/img_001.jpg and img_002.jpg) are dead — Wayback only holds a soft-404 for them (519 bytes, text/html), so no images could be saved. "Over 1200 units made" is carried over unverified from the original sheet import; no source located that confirms a print run number. sao_version left null: the maker''s text describes "a normal SAO connector" and "a mirrored SAO connector" without giving a pin count.'
last_modified_date: '2026-09-07'
---

The seventh annual badge from Darknet Industries, officially named the "Darknet Industries, Conrad Personal Communicator," was DEF CON 26's contest badge for 2018. It shipped as an unpopulated solder-it-yourself dev kit built around an STM32F411RET6 (ARM Cortex-M4) for the badge's 1.8" color LCD, and an ESP-WROOM-32 handling wifi/Bluetooth and a 128x32 OLED. Hardware was designed by cmdc0de, with help from Bunni and Krux; firmware came from cmdc0de and Gourry; Krux did the badge's look, artwork, and the silkscreen and acrylic puzzles built into the board. As a Darknet contest tool, the badge was meant to pair with other players' badges and carry that year's puzzle line — owners had to visit the Darknet table in the contest area to flash the actual contest firmware, since kits shipped without it.

Past its stock two LEDs, the board leaves pads for programmable APA-106 LEDs on the front and APA-102 SMD LEDs on the back for anyone who wants to go further, plus ST-Link and ESP32 programming headers since the badge doubled as a dev kit. It carries two SAO headers — one standard, one deliberately mirrored — and the same GitHub release includes Krux's companion "Eggplant" SAO (an ATtiny85 board) built specifically to fit the mirrored connector.

## Make your own

Hardware (Eagle files, component library) and firmware (STM32 + ESP32, MIT licensed) are both published at [github.com/thedarknet/dc26-badge](https://github.com/thedarknet/dc26-badge). The maker's own assembly walkthrough — soldering order, LED polarity, SAO header notes, and how to add the optional programmable LEDs — is preserved at the Wayback Machine link above; the live dcdark.net site no longer serves it as a static page.

## History

This badge was the "Darknet-7" entry in Darknet Industries' recurring DEF CON badge line, which the archive has also seen at DEF CON 24, DEF CON 25, and continuing the next year as "Darknet 8."
