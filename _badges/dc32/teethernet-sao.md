---
title: teETHernet SAO
id: dc32-teethernet-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: K4r4koyun
  url: https://github.com/k4r4koyun
summary: A SAO with two RJ45 jacks that tests copper Ethernet cables and hides a small UART capture-the-flag challenge.
functions: '[Blinky + Ethernet Cable Tester + Mini CTF + Bonus Sticker] => The SAO has 9 LEDs, which either blink via alternating patters or act as a status indicator for ethernet cable connectivity function. There is a very basic challenge accessible from the UART interface of the SAO. The source code for the badge, instructions to pins and programming environment will also be provided, if anybody wants to repurpose or experiment. Finally, a glow-in-the-dark sticker will be included with the purchase.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - ctf
  - security
tech:
  mcu: ATMEGA328PB-AU
  leds:
    count: 9
    type: null
    note: side-mounted LEDs that shine through the back of the board
  display: null
  connectivity:
  - uart
  battery: null
  sao_version: null
get_one:
  price: $30.00
  price_usd: 30.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold in person at DEF CON 32 in Las Vegas (Aug 1-12, 2024); drops were announced on the maker's Twitter/X.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/k4r4koyun/DEFCON-32-teETHernet-SAO
  firmware_url: null
  eda_tool: null
links:
- label: twitter.com/k4r4koyun
  url: https://twitter.com/k4r4koyun
  kind: social
- label: k4r4koyun/DEFCON-32-teETHernet-SAO
  url: https://github.com/k4r4koyun/DEFCON-32-teETHernet-SAO
  kind: repo
images:
  - file: assets/images/badges/dc32/teethernet-sao/e464c88be7.png
    source: "https://github.com/k4r4koyun/DEFCON-32-teETHernet-SAO"
    credit: "K4r4koyun"
    caption: "teETHernet SAO board photo"
  - file: assets/images/badges/dc32/teethernet-sao/5ec5f97e52.jpg
    source: "https://github.com/k4r4koyun/DEFCON-32-teETHernet-SAO"
    credit: "K4r4koyun"
    caption: "teETHernet SAO board render/schematic view"
contact: {}
notes:
- The SAO will only be sold in person, I'll be in Vegas between 1st and 12th of August. Details regarding drops will be announced on Twitter
status: released
sources:
- kind: sheet
  event: dc32
  row: 74
  updated: '2024-07-06'
- kind: url
  url: https://github.com/k4r4koyun/DEFCON-32-teETHernet-SAO
  title: "GitHub - k4r4koyun/DEFCON-32-teETHernet-SAO"
  accessed: '2026-09-06'
  note: Confirms the SAO was released for DEF CON 32; gives MCU (ATMEGA328PB-AU), 9 LEDs, 2 Ethernet sockets, CTF-over-UART, MIT-licensed schematics, and board photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The maker's project repo (README + schematics PDF) confirms the sheet's description and adds the MCU. Could not reach the maker's Twitter/X profile directly (fetch returned an error) so price/availability/quantity-sold could not be independently verified beyond the sheet listing; no storefront or press coverage found. No firmware source code is published in the repo (only schematics PDF and images), so open_source is marked partial rather than yes, and eda_tool/firmware_url are left empty since the tool used isn't stated.
last_modified_date: '2026-09-06'
---

The teETHernet SAO is a networking-themed add-on board that K4r4koyun sold in person at DEF CON 32 (Las Vegas, August 2024). It carries two RJ45 jacks that let it double as a simple copper twisted-pair Ethernet cable tester, with 9 side-mounted LEDs shining through the back of the board to show either idle blink animations or cable-test status. An ATMEGA328PB-AU microcontroller runs the show, and the board exposes a UART interface hosting a small capture-the-flag challenge; solving it unlocks additional LED animation modes. Buyers also received a glow-in-the-dark sticker with their purchase.

The maker published the schematics (as a PDF) and board photos to a dedicated GitHub repo under an MIT license, with the stated intent of letting people repurpose or experiment with the design; no firmware source code appears to be included in that repo. Distribution was informal: the badge was sold only in person during the con, with drop details announced over the maker's Twitter/X account, so total quantity made and current availability are not documented anywhere public.
