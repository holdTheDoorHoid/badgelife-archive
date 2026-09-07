---
title: GigaGeiger
id: dc33-gigageiger
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: HackMy
  url: https://github.com/Penzz-HM
summary: A Wi-Fi reconnaissance and audit tool styled as a 1950s Geiger counter, using a single rotary dial to switch between channel monitoring, RSSI foxhunting, and OTA firmware flashing.
functions: Wifi AP foxhunt, 2.4ghz wifi congestion meter, OTA updates, radiation dosimeter
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - radio
  - measurement
  - hardware tool
tech:
  mcu: ESP32-S3-WROOM
  leds: null
  display: 1.28" GC9A01 circular LCD
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: $120
  price_usd: 120.0
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing shows sold out as of 2026-09-06; maker noted supply constraints on the Geiger tube used for the side dosimeter attachment as the reason restocking has not happened.'
  distribution:
  - purchase
  - preorder
  where: 'Sold on Tindie (tindie.com/products/38838), with pickup at DEF CON 33 or shipping after the con; also listed on the community badge sheet.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Penzz-HM/GigaGeiger
  firmware_url: https://github.com/Penzz-HM/GigaGeiger
  eda_tool: null
  license: MIT
  notes: 'GitHub repo has firmware (Arduino/C++) and build photos; no explicit KiCad/Gerber files were found in the repo listing reached.'
links:
- label: github.com/Penzz-HM/GigaGeiger
  url: https://github.com/Penzz-HM/GigaGeiger
  kind: repo
- label: GigaGeiger on Tindie
  url: https://www.tindie.com/products/38838/
  kind: store
images:
- file: assets/images/badges/dc33/gigageiger/600bce361b.jpg
  source: "https://github.com/Penzz-HM/GigaGeiger"
  credit: "Penzz-HM / HackMy"
  caption: "GigaGeiger front, external view"
- file: assets/images/badges/dc33/gigageiger/57448f731d.jpg
  source: "https://github.com/Penzz-HM/GigaGeiger"
  credit: "Penzz-HM / HackMy"
  caption: "GigaGeiger screen showing title screen"
contact:
  emails:
  - mwagner@hackmypi.com
notes:
- nope :) Can order on tindie for shipping after con, or pickup at con
status: released
sources:
- kind: sheet
  event: dc33
  row: 5
  updated: 6/2/2025 20:18:28
- kind: url
  url: https://github.com/Penzz-HM/GigaGeiger
  title: "GigaGeiger (Penzz-HM/GigaGeiger) - GitHub"
  accessed: '2026-09-06'
  note: "Maker's own README: features, MCU (ESP32-S3-WROOM), display (GC9A01), three dial modes, MIT license, build photos."
- kind: url
  url: https://www.tindie.com/products/38838/
  title: "GigaGeiger - Tindie product listing"
  accessed: '2026-09-06'
  note: "Confirms $120 price, sold-out status since Aug 6 2025, designer HackMy (Marietta, GA), lanyard+batteries included, dosimeter-tube supply constraint blocking restock."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Quantity made not stated anywhere found. No Gerbers/KiCad files or a distinct firmware_url beyond the same GitHub repo were located. LED info not mentioned by the maker (display-only feedback, no addressable LEDs found), left null rather than guessed.'
last_modified_date: '2026-09-06'
---

The GigaGeiger is a DEF CON 33 badge-style Wi-Fi tool built by the maker HackMy (GitHub user Penzz-HM), styled after a 1950s Geiger counter. A single three-position rotary dial swaps it between three modes: turned all the way left it becomes a 2.4GHz channel monitor that visualizes packet counts per channel like Geiger clicks; centered it becomes a "hot/cold" foxhunt tool that uses RSSI to track down a target MAC address, useful for CTF-style Wi-Fi hunts; and turned all the way right it drops into an OTA web-flasher mode, auto-joining a `GigaGeiger`/`Defcon33` hotspot and showing an IP address to browse to for firmware updates.

Hardware-wise it runs an ESP32-S3-WROOM with a circular GC9A01 LCD for its retro dial-and-gauge display. It sold for $120 on Tindie, with pickup available at DEF CON 33 or shipping afterward, and came with a lanyard and batteries. As of this research pass the Tindie listing has been sold out since August 6, 2025, with the maker citing a shortage of the Geiger-tube dosimeter attachment as the blocker on restocking.

Firmware and build documentation are open source (MIT license) on GitHub, including external and internal build photos and screen captures, though no separate hardware design files (KiCad/Gerbers) were found in the repository.
