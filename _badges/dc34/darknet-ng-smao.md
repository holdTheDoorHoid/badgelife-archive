---
title: Darknet-NG SMAO
id: dc34-darknet-ng-smao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Darknet-NG
summary: A Meshtastic mesh-radio node built into a full SAO, pre-flashed with the official DEF CON build and DEFCONnect configuration.
functions: A full Meshtastic node on an SAO
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
tech:
  mcu: nRF52840 (RAK4630 module)
  leds: null
  display: none
  connectivity:
  - lora
  - ble
  battery: none, powered by badge SAO rail or USB-C
  sao_version: null
get_one:
  price: $55
  price_usd: 55.0
  quantity: '125 units (presale)'
  availability: limited
  availability_note: 'Checked 2026-09-06: listed as presale on uberflux.com, pickup-only at DEF CON 34, no shipping.'
  distribution:
  - purchase
  - preorder
  where: Sold via uberflux.com/product/DNNG-SMAO as a presale, picked up in person at DEF CON 34.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/DNNG-SMAO
  url: https://uberflux.com/product/DNNG-SMAO
  kind: store
- label: discord.gg/BgQMDABx3v
  url: https://discord.gg/BgQMDABx3v
  kind: social
images:
- file: assets/images/badges/dc34/darknet-ng-smao/82e3354171.jpg
  source: "https://uberflux.com/product/DNNG-SMAO"
  credit: "Darknet-NG"
  caption: "Darknet-NG SMAO product photo"
- file: assets/images/badges/dc34/darknet-ng-smao/8abd0657ea.jpg
  source: "https://uberflux.com/product/DNNG-SMAO"
  credit: "Darknet-NG"
  caption: "Darknet-NG SMAO detail photo"
contact:
  discord: Boko
  emails:
  - dcbokonon@gmail.com
notes: []
status: listed
sources:
- kind: sheet
  event: dc34
  row: 44
  updated: 7/18/2026 16:43:45
  listing: New
- kind: url
  url: https://uberflux.com/product/DNNG-SMAO
  title: "Darknet-NG SMAO – Uberflux"
  accessed: '2026-09-06'
  note: "Source for maker name, specs (nRF52840/RAK4630 module, SX1262 LoRa radio, dual Johanson chip antennas), power/pairing behavior, price, presale quantity (125 units), and pickup-only availability."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Only the Uberflux storefront listing was reachable; the linked Discord invite is not a fetchable content source and no Hackaday.io, GitHub, or press coverage was found for this specific item. LED count/type, PCB color/shape, SAO header version, and open-source status are not stated on the storefront page and are left empty rather than guessed.'
last_modified_date: '2026-09-06'
---

The Darknet-NG SMAO is a Standard Add-On built around a full Meshtastic LoRa mesh-radio node rather than the usual blinky add-on electronics. It is built on a Nordic nRF52840 (on a RAK4630 module) paired with a Semtech SX1262 LoRa radio tuned to the US 915 MHz band, with separate Johanson chip antennas for LoRa and 2.4 GHz Bluetooth. Each unit ships pre-flashed with the official DEF CON Meshtastic build and DEFCONnect configuration (CLIENT_MUTE role, ShortTurbo preset, +10 dBm TX power), so it works as a mesh node the moment it is powered.

Unlike most SAOs, it needs no separate battery: it draws power either from the host badge's SAO rail or from USB-C, switching automatically between the two. Configuration is done over Bluetooth LE through the standard Meshtastic mobile app, with each unit carrying its own unique BLE pairing PIN, and the firmware can be reflashed over USB-C using UF2 or a web flasher if an owner wants to run something other than the DEF CON build.

Made by Boko under the Darknet-NG name, it was sold as a $55 presale of 125 units through Uberflux, for pickup only at DEF CON 34 with no shipping offered.
