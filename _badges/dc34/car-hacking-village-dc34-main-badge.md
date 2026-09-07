---
title: Car Hacking Village DC34 Main Badge
id: dc34-car-hacking-village-dc34-main-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: uberwoozle
  url: https://github.com/car-hacking-village
summary: The DEF CON 34 Car Hacking Village main badge, an automotive-themed board built around real CAN bus tooling that can emulate a car's network on a single PCB.
functions: 'Runs a MicroPython REPL shell with autocomplete; speaks CAN 2.0/FD over a DB9 connector and over USB (SLCAN protocol); can emulate a virtual ECU, scan for DTCs, and run CAN deauthentication attacks as part of the village CTF; has two CAN-enabled SAO expansion slots and programmable LED "blinkies".'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - village badge
  - ctf
tech:
  mcu: RP2040
  leds: null
  display: none
  connectivity:
  - usb
  - uart
  battery: null
  sao_version: null
get_one:
  price: $115
  price_usd: 115
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold through Uberflux's online store; listed as 0 remaining/sold out when checked.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/car-hacking-village/Main-Badge-Firmware
  eda_tool: null
links:
- label: uberflux.com/product/WOOZL-DC34-CHV-BADGE
  url: https://uberflux.com/product/WOOZL-DC34-CHV-BADGE
  kind: store
- label: car-hacking-village/Main-Badge-Firmware
  url: https://github.com/car-hacking-village/Main-Badge-Firmware
  kind: repo
- label: car-hacking-village/chv_badgetools
  url: https://github.com/car-hacking-village/chv_badgetools
  kind: repo
- label: Car Hacking Village
  url: https://www.carhackingvillage.com/
  kind: website
images:
- file: assets/images/badges/dc34/car-hacking-village-dc34-main-badge/9d500bd652.jpg
  source: "https://uberflux.com/product/WOOZL-DC34-CHV-BADGE"
  credit: "uberwoozle / Uberflux"
  caption: "Car Hacking Village DC34 main badge product photo"
contact: {}
notes:
- 'Uberflux. $115, status: sold out.'
status: released
sources:
- kind: url
  url: https://uberflux.com/product/WOOZL-DC34-CHV-BADGE
  title: Car Hacking Village DC34 Main Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''DEF CON 34 Car Hacking Village''.'
- kind: url
  url: https://github.com/car-hacking-village/Main-Badge-Firmware
  title: car-hacking-village/Main-Badge-Firmware
  accessed: '2026-09-07'
  note: 'Confirms RP2040 + MCP251863 CAN transceiver; described as base firmware for the CHV main badge (2026+), emulating a car on a single PCB.'
- kind: url
  url: https://github.com/car-hacking-village/chv_badgetools
  title: car-hacking-village/chv_badgetools
  accessed: '2026-09-07'
  note: 'Host-side Python CAN utilities for talking to the DC34 badge over USB (SLCAN).'
- kind: url
  url: https://www.carhackingvillage.com/
  title: Car Hacking Village
  accessed: '2026-09-07'
  note: 'Organizer site, used to confirm the village/org identity.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The Uberflux storefront calls it an "ESP32-class board", but the Car Hacking Village org''s own Main-Badge-Firmware repo (base firmware for the "CHV main badge (2026+)") targets an RP2040 with an MCP251863 CAN transceiver, which is the value recorded here since it is the maker''s own source. No dedicated hardware/schematic repo for the DC34 board was found (only DC32-era hardware repos exist in the org), so hardware_url, LED count/type, and quantity made are left empty. Firmware is public on GitHub; the storefront also says software will be made fully open source after DEF CON, so open_source is marked partial pending that release.'
last_modified_date: '2026-09-07'
---

The DC34 Car Hacking Village main badge is an automotive-security-themed board sold through Uberflux for $115, built by uberwoozle for the Car Hacking Village's DEF CON 34 CTF. Rather than being a passive prop, it doubles as real CAN bus test equipment: it exposes a DB9 CAN 2.0/FD connector and a USB (SLCAN) interface, runs a MicroPython REPL with autocomplete, and can emulate a virtual ECU, scan for diagnostic trouble codes, and perform CAN deauthentication attacks as part of the village's competition. Two CAN-enabled SAO expansion slots let it host companion add-ons, and it includes programmable LED effects.

Under the hood it is built around an RP2040 microcontroller paired with an MCP251863 CAN transceiver, per the Car Hacking Village GitHub organization's own "Main-Badge-Firmware" repository, which describes it as firmware for "emulating a car on a single PCB." Host-side Python tooling (`chv_badgetools`) lets a computer talk to the badge over USB. The badge sold out on Uberflux, and the village has said the supporting software will be fully open-sourced after DEF CON concludes.
