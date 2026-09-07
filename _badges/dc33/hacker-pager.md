---
title: Hacker Pager
id: dc33-hacker-pager
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: exploitee.rs
  url: https://shop.exploitee.rs/shop/p/the-hacker-pager
summary: A retro-styled, open-source LoRa "wireless messenger and radio multitool" in a classic pager form factor, running a custom fork of Meshtastic.
functions: Meshtastic mesh messaging (standalone or as a gateway), LoRa packet capture with a Wireshark plugin, a spectrum analyzer (850-950 MHz), a CHIP-8 virtual machine for retro games, BadUSB scripts, Bluetooth keyboard support, and vibration/audible alerts for incoming messages.
look:
  colors: [black, green, blue, red, white]
  shape: rectangle
  themes: [radio, retro computer, security, privacy]
tech:
  mcu: ESP32-S3
  leds:
    count: 48
    type: RGB
    note: 36 addressable RGB LEDs plus 12 UV LEDs used for message notifications.
  display: 192x64 pixel monochrome LCD (green backlight), with an ambient clock mode when idle
  connectivity: [lora, bluetooth, wifi]
  battery: rechargeable LiPo
  sao_version: null
get_one:
  price: $200 (standard Green/Black) / $250 (special edition colors)
  price_usd: 200.0
  quantity: ''
  availability: sold_out
  distribution: [purchase, preorder]
  where: Sold via preorder on shop.exploitee.rs; preorders sold out ahead of DEF CON 33, with in-person sales planned at the con and further online restocks afterward.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  firmware_url: https://github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  eda_tool: null
  license: CERN OHL v2 (hardware)
  notes: Firmware is a fork of Meshtastic; separate GitHub repos exist for the electronics design and the case design (laser-cut acrylic and 3D-printed parts) alongside the main firmware repo.
links:
- label: shop.exploitee.rs/shop/p/the-hacker-pager
  url: https://shop.exploitee.rs/shop/p/the-hacker-pager
  kind: store
- label: hackerpager.net
  url: https://hackerpager.net/
  kind: website
- label: github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  url: https://github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  kind: repo
- label: hackaday.com/2025/07/31/hands-on-the-hacker-pager
  url: https://hackaday.com/2025/07/31/hands-on-the-hacker-pager/
  kind: article
images:
  - file: assets/images/badges/dc33/hacker-pager/9eda04f37c.jpg
    source: "https://shop.exploitee.rs/shop/p/the-hacker-pager"
    credit: "exploitee.rs"
    caption: "The Hacker Pager device, red/blue color option"
  - file: assets/images/badges/dc33/hacker-pager/25e07ba8dc.jpg
    source: "https://shop.exploitee.rs/shop/p/the-hacker-pager"
    credit: "exploitee.rs"
    caption: "The Hacker Pager device, blue color option"
contact:
  raw:
  - Discord - zenofex
notes:
- Pre-orders are sold out. Badge will be available for purchase in person at DC33 and more will be available on line post-DC33.
status: released
sources:
- kind: sheet
  event: dc33
  row: 52
  updated: 7/28/2025
- kind: url
  url: https://shop.exploitee.rs/shop/p/the-hacker-pager
  title: "The Hacker Pager - exploitee.rs shop"
  accessed: '2026-09-06'
  note: "Price, colors, MCU/radio/LED specs, and product photos. Note: this listing has since been updated to advertise a newer DEF CON 34 (2026) edition of the same product; DC33-specific pricing/colors were cross-checked against the Hackaday article below."
- kind: url
  url: https://hackerpager.net/
  title: "Hacker Pager - official site"
  accessed: '2026-09-06'
  note: "Feature list (Meshtastic, packet capture, spectrum analyzer, CHIP-8, BadUSB), display detail, open-source claim."
- kind: url
  url: https://github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  title: "exploiteers/Meshtastic-Exploiteers-Hacker-Pager"
  accessed: '2026-09-06'
  note: "Confirms firmware is a Meshtastic fork; open source with separate electronics/case design repos."
- kind: url
  url: https://hackaday.com/2025/07/31/hands-on-the-hacker-pager/
  title: "Hands-On: The Hacker Pager"
  accessed: '2026-09-06'
  note: "DEF CON 33 (2025) specific details: $200/$250 pricing, sold out pre-orders expected at DC33, CERN OHL v2 license, LED counts, display size."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: "The maker's own storefront and hackerpager.net currently describe an updated DEF CON 34 (2026) edition (photos labeled 'dc34', mentions of DC34 dates), since the listing appears to be reused/updated year over year rather than archived per-release. Core specs (ESP32-S3, SX1262 LoRa radio, 192x64 LCD, Meshtastic fork, CERN OHL v2) are consistent across sources and are unlikely to differ from the DC33 (2025) release described in the Hackaday hands-on article, which is used here for DC33-specific pricing and availability. Quantity made and exact SAO header presence/version were not found in any source and are left empty. Radio chip (Semtech SX1262) and physical dimensions (114 x 84 x 22.2 mm) were confirmed but are not modeled as separate fields in this schema."
last_modified_date: '2026-09-06'
---

The Hacker Pager is a retro-styled, open-source wireless messenger built by exploitee.rs around an Espressif ESP32-S3 and a Semtech SX1262 LoRa radio, running a custom fork of the Meshtastic mesh-networking firmware. Shaped like a classic pager, it carries a 192x64 monochrome LCD with a green backlight (including an idle ambient-clock mode), 36 addressable RGB LEDs plus 12 UV LEDs for notifications, and a rechargeable LiPo battery, and it can operate standalone or pair with a phone over Bluetooth.

Beyond messaging, the device doubles as a LoRa radio multitool: it can capture packets (with an accompanying Wireshark plugin), run a spectrum analyzer over 850-950 MHz, execute a CHIP-8 virtual machine for retro games, and fire off BadUSB scripts, alongside vibration and audible alerts for incoming messages. It sold for $200 in standard green/black or $250 in special-edition colors; preorders sold out ahead of DEF CON 33 (2025), with the maker planning in-person sales at the con and further online restocks afterward.

Hardware and firmware are open source: the firmware is a public fork of Meshtastic, the hardware is released under CERN OHL v2, and separate GitHub repositories cover the electronics design and the 3D-printed/laser-cut acrylic case, alongside the main firmware repo linked here.

## Make your own

The firmware, electronics design, and case design files are published on GitHub (see `make_your_own.hardware_url`); build steps beyond flashing the Meshtastic fork were not detailed in the sources checked.
