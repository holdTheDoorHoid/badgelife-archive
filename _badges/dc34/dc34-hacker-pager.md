---
title: The Hacker Pager
id: dc34-dc34-hacker-pager
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: exploitee.rs
  url: https://exploitee.rs/
summary: 2026 edition of exploitee.rs's retro-styled LoRa/Meshtastic wireless messenger, sold as DEF CON 34 conference pickup with a new transparent SLA resin body and clear, fluorescent-yellow or fluorescent-orange acrylic panels, built on an ESP32-S3 and Semtech SX1262 with a 192x64 LCD and 36 RGB plus 12 UV LEDs.
functions: Standalone Meshtastic messaging over LoRa with no phone required (a companion app is optional); .pcap packet capture for protocol analysis; spectrum analysis in the 850-950 MHz range; a built-in CHIP-8 virtual machine for retro games; BadUSB script support; custom notification melodies and channel configuration through its own on-device UI.
look:
  colors:
  - clear
  - yellow
  - orange
  shape: null
  themes:
  - radio
  - hardware tool
  - security
  - retro computer
tech:
  mcu: ESP32-S3
  leds:
    count: 48
    type: RGB
    note: 36 addressable RGB LEDs plus 12 addressable UV LEDs
  display: 192x64 monochrome LCD, green adjustable backlight
  connectivity:
  - lora
  - meshtastic
  - bluetooth
  - wifi
  - usb
  battery: rechargeable LiPo, USB-C charging
  sao_version: null
get_one:
  price: $250
  price_usd: 250
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: DEF CON 34 conference pickup (Aug 4 and 6, 2026) and shop.exploitee.rs; sold out as of the September 7, 2026 check, with online restocking for U.S. shipping planned for late September 2026.
make_your_own:
  open_source: true
  hardware_url: https://github.com/exploiteers/Electronics-Design-Exploiteers-Hacker-Pager
  firmware_url: https://github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  eda_tool: null
links:
- label: hackerpager.net
  url: https://hackerpager.net/
  kind: website
- label: shop.exploitee.rs/shop/p/the-hacker-pager
  url: https://shop.exploitee.rs/shop/p/the-hacker-pager
  kind: store
- label: github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  url: https://github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  kind: repo
- label: github.com/exploiteers/Electronics-Design-Exploiteers-Hacker-Pager
  url: https://github.com/exploiteers/Electronics-Design-Exploiteers-Hacker-Pager
  kind: repo
- label: github.com/exploiteers/Case-Design-Files-Exploiteers-Hacker-Pager
  url: https://github.com/exploiteers/Case-Design-Files-Exploiteers-Hacker-Pager
  kind: repo
images:
- file: assets/images/badges/dc34/dc34-hacker-pager/1ee1b0db34.jpg
  source: https://hackerpager.net/
  credit: exploitee.rs
  caption: The Hacker Pager, front view, clear resin body with LCD and RGB LED array
- file: assets/images/badges/dc34/dc34-hacker-pager/45e1a32df3.jpg
  source: https://hackerpager.net/
  credit: exploitee.rs
  caption: The Hacker Pager, back view showing internal PCB through clear resin body
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackerpager.net/
  title: The Hacker Pager | exploitee.rs
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackerpager.net/
  title: The Hacker Pager | exploitee.rs
  accessed: '2026-09-07'
  note: Confirmed maker, features, MCU (ESP32-S3), radio (SX1262), display, LED counts, DEF CON 34 pickup dates, firmware repo link, and image URLs (dc34front.webp, dc34back.webp).
- kind: url
  url: https://shop.exploitee.rs/shop/p/the-hacker-pager
  title: The Hacker Pager - exploitee.rs shop
  accessed: '2026-09-07'
  note: Confirmed price ($250, limit 2/order), sold-out status, restock timing, dimensions, color/finish options (clear standard, yellow/clear and orange/clear limited, Philanthropist blind-bag edition), Bluetooth/Wi-Fi connectivity, and box contents (microSD card, lanyard, desk stand).
- kind: url
  url: https://github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  title: exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  accessed: '2026-09-07'
  note: Confirmed the firmware is an open-source fork of Meshtastic with hardware-specific modifications; repo includes a LICENSE file (specific license not read).
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched hackerpager.net, shop.exploitee.rs, and all three linked GitHub repos (firmware, electronics, case). Every non-empty field and body sentence is supported: maker, ESP32-S3 MCU, SX1262 radio, 192x64 LCD, 36 RGB + 12 UV LEDs, Bluetooth/Wi-Fi/USB-C/LiPo, functions (pcap capture, spectrum analysis, CHIP-8, BadUSB, custom melodies), price $250, sold_out status, Aug 4/6 2026 pickup, late-September restock, open-source hardware+firmware links, both saved images (front/back) match hackerpager.net''s own product photos. No corrections needed. Quantity made is still not stated anywhere found; exact firmware license text was not fully read. Incidentally confirmed but left unfilled per no-new-research scope: the electronics repo states KiCad as its EDA tool and CERN-OHL-S v2 as its hardware license (tech.eda_tool/license remain null/empty pending a dedicated research pass). This is exploitee.rs''s second annual Hacker Pager; the DC33 edition has its
    own entry at _badges/dc33/hacker-pager.md.'
last_modified_date: '2026-09-07'
related:
- dc33-hacker-pager
---

The Hacker Pager is exploitee.rs's second annual conference wireless messenger, sold to DEF CON 34 attendees in August 2026 with online restocking to follow. It is a standalone LoRa/Meshtastic mesh-networking device built around an ESP32-S3 microcontroller and a Semtech SX1262 radio, with a 192x64 monochrome LCD, 36 addressable RGB LEDs plus 12 UV LEDs, Bluetooth and Wi-Fi, and USB-C-rechargeable LiPo power. Beyond messaging, it doubles as a LoRa toolkit: it can capture packets to .pcap files for analysis, run a spectrum analyzer across 850-950 MHz, execute BadUSB scripts, and run CHIP-8 games through a built-in virtual machine.

The 2026 edition moved to a transparent SLA-resin case with interchangeable clear, fluorescent-yellow, or fluorescent-orange acrylic panels, plus a limited "Philanthropist" edition sold with blind-bag acrylic plates. It sold for $250 (limit two per order) with conference pickup slots on August 4 and 6, 2026, and was sold out on the shop site as of this check, with U.S. shipping restocks planned for late September 2026. Each unit ships with a 32 GB microSD card, a wrist lanyard, and a desk stand.

## Make your own

Both hardware and firmware are published as open source. The firmware (a Meshtastic fork with Hacker Pager-specific hardware support) is at github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager, the electronics design files are at github.com/exploiteers/Electronics-Design-Exploiteers-Hacker-Pager, and the 3D-printable/machined case design files are at github.com/exploiteers/Case-Design-Files-Exploiteers-Hacker-Pager. The firmware repo documents build and flashing instructions and links to a web-based flasher tool.

## History

This is the second Hacker Pager from exploitee.rs; the original DEF CON 33 (2025) edition has its own archive entry.
