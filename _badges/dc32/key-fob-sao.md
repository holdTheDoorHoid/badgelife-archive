---
title: Key Fob SAO
id: dc32-key-fob-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: Car Hacking Village
  url: https://www.carhackingvillage.com
summary: A $50 CAN-based SAO from the Car Hacking Village for DEF CON 32, shaped like a car key fob with an onboard 125 KHz LF receiver, a 433 MHz transmitter, and touch buttons for its own CTF challenges.
functions: |-
  CTF Challenges
  125 KHz (LF) Receiver
  433 MHz Transmitter
  Touch Buttons
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - ctf
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - rfid
  - sub-ghz
  inputs:
  - touch
  battery: null
  sao_version: null
get_one:
  price: $50.00
  price_usd: 50.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold at the Car Hacking Village booth at DEF CON 32 (2024), alongside the CHV Main Badge and the Speedometer and PRND SAOs.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.carhackingvillage.com
  url: https://www.carhackingvillage.com
  kind: website
  archived: https://web.archive.org/web/20260810193641/https://www.carhackingvillage.com/
- label: car-hacking-village/CHV_SAO_Specification (GitHub)
  url: https://github.com/car-hacking-village/CHV_SAO_Specification
  kind: repo
images:
- file: assets/images/badges/dc32/key-fob-sao/2538b0ad19.png
  source: https://www.carhackingvillage.com/
  credit: Car Hacking Village
  caption: 2024 Key FOB SAO product photo from the Car Hacking Village site
  archived: https://web.archive.org/web/20260810193641/https://www.carhackingvillage.com/
contact: {}
notes:
- CHV's SAO headers are CAN-based rather than the usual I2C SAO bus (3.3V/GND plus CAN TX/RX), per the CHV SAO Specification repo, so "sao_version" above is left null rather than mapped to the standard v1/v1.69bis vocabulary.
status: listed
sources:
- kind: sheet
  event: dc32
  row: 36
  updated: ''
- kind: url
  url: http://web.archive.org/web/20240811090612/https://www.carhackingvillage.com/
  title: Car Hacking Village (Wayback Machine capture, 11 Aug 2024)
  accessed: '2026-09-07'
  note: Archived DC32 badge lineup page listing the "2024 Key FOB sao" at $50 with CTF Challenges, 125 KHz (LF) Receiver, 433 MHz Transmitter, and Touch Buttons, alongside the $100 CHV Main Badge (RP2040, 4 CAN networks, 4 SAO connectors) and the $50 Speedometer and PRND SAOs. Source of the product photo.
- kind: url
  url: https://www.carhackingvillage.com/
  title: Car Hacking Village
  accessed: '2026-09-07'
  note: Current site no longer lists the DC32 badge/SAO lineup or a price; only a general note that the SAO standard was updated to include CAN TX/RX remains.
  archived: https://web.archive.org/web/20260810193641/https://www.carhackingvillage.com/
- kind: url
  url: https://github.com/car-hacking-village/CHV_SAO_Specification
  title: car-hacking-village/CHV_SAO_Specification
  accessed: '2026-09-07'
  note: Documents CHV's CAN-based SAO header (3.3V, GND, CAN TX, CAN RX in place of I2C), which the Key Fob SAO plugs into on the CHV Main Badge.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Confirmed via an archived (Wayback Machine) copy of carhackingvillage.com from August 2024, which matches the sheet row exactly (title, $50 price, and all four listed functions) and supplied the product photo. The live site no longer carries this page, and no dedicated GitHub repo for the Key Fob SAO specifically was found (the org's public repos cover the Main Badge, Speedometer SAO CTF, and Speedometer/PRND firmware, but not this one), so mcu, LED count, open-source status, and quantity/current availability remain unconfirmed.
last_modified_date: '2026-09-07'
---

The Key Fob SAO was one of four add-ons the Car Hacking Village sold at its DEF CON 32 (2024) booth, built around CHV's own CAN-based SAO standard rather than the usual I2C SAO bus. Shaped and themed as a car key fob, it carries a 125 KHz low-frequency receiver and a 433 MHz transmitter — the two bands used by real vehicle remote entry and immobilizer systems — plus touch buttons, wrapped around its own CTF challenge. It plugged into one of the four SAO headers on that year's $100 CHV Main Badge (an RP2040 board with four onboard CAN networks and a dry CAN connector for tapping real vehicle buses), sitting in a lineup alongside a Speedometer SAO and a PRND (Park/Reverse/Neutral/Drive) SAO, each also $50.

No dedicated hardware or firmware repository specific to the Key Fob SAO turned up in CHV's public GitHub organization, so its MCU, LED count, and open-source status are left blank rather than guessed. Its current availability is also unconfirmed: the con-year page that documented it has since been removed from the live carhackingvillage.com and the item does not appear in CHV's current online store.
