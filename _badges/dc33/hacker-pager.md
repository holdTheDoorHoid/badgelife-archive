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
summary: A retro-styled, open-source LoRa "wireless messenger and LoRa radio multitool" in a classic pager form factor, running a custom fork of Meshtastic.
functions: Meshtastic mesh messaging (standalone, or tethered to the Meshtastic phone app over Bluetooth), LoRa packet capture to .pcap with a Wireshark dissector plugin, a spectrum analyzer (850-950 MHz), a CHIP-8 virtual machine for retro games, BadUSB scripts, Bluetooth keyboard support, and vibration/audible alerts for incoming messages.
look:
  colors:
  - green
  - black
  - pink
  - orange
  shape: rectangle
  themes:
  - radio
  - retro computer
  - security
tech:
  mcu: ESP32-S3
  leds:
    count: 48
    type: RGB
    note: 36 addressable RGB LEDs plus 12 addressable UV LEDs used for message notifications.
  display: 192x64 pixel monochrome LCD (green backlight), with an ambient clock mode when idle
  connectivity:
  - lora
  - bluetooth
  - wifi
  battery: rechargeable LiPo
  sao_version: null
get_one:
  price: $200 (standard Green/Black) / $250 (special edition Pink/Black, Orange/Black)
  price_usd: 200.0
  quantity: ''
  availability: sold_out
  availability_note: Storefront checked 2026-09-06; the listing now sells a DEF CON 34 (2026) edition and shows Sold Out.
  distribution:
  - purchase
  - preorder
  where: Sold via preorder on shop.exploitee.rs; preorders sold out ahead of DEF CON 33, with units sold in person at the con and an email list for later batches.
make_your_own:
  open_source: true
  hardware_url: https://github.com/exploiteers/Electronics-Design-Exploiteers-Hacker-Pager
  firmware_url: https://github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  eda_tool: KiCad
  license: CERN OHL-S v2 (hardware and case files)
  notes: Firmware is a fork of Meshtastic. The electronics repo holds a KiCad project plus exported schematic PDFs and BOM files, and describes the design as based on the Heltec V3 LoRa module. A separate repo holds the case, button and acrylic-plate files (FDM-printable, laser-cut acrylic).
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
- label: github.com/exploiteers/Electronics-Design-Exploiteers-Hacker-Pager
  url: https://github.com/exploiteers/Electronics-Design-Exploiteers-Hacker-Pager
  kind: repo
- label: github.com/exploiteers/Case-Design-Files-Exploiteers-Hacker-Pager
  url: https://github.com/exploiteers/Case-Design-Files-Exploiteers-Hacker-Pager
  kind: repo
- label: hackaday.com/2025/07/31/hands-on-the-hacker-pager
  url: https://hackaday.com/2025/07/31/hands-on-the-hacker-pager/
  kind: article
images: []
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
  title: The Hacker Pager - exploitee.rs shop
  accessed: '2026-09-06'
  note: MCU (ESP32-S3), Semtech SX1262 radio, Bluetooth/Wi-Fi, 48 addressable LEDs, dimensions, sold-out status. The listing now advertises a DEF CON 34 (2026) edition (clear/yellow/orange acrylic, from $250); DC33 pricing/colors taken from the Hackaday article instead.
- kind: url
  url: https://hackerpager.net/
  title: Hacker Pager - official site
  accessed: '2026-09-06'
  note: Feature list (Meshtastic, packet capture, Wireshark plugin, spectrum analyzer 850-950 MHz, CHIP-8, BadUSB, Bluetooth keyboards), 192x64 LCD with green backlight, 36 RGB + 12 UV LEDs, LiPo battery, open-source statement.
- kind: url
  url: https://github.com/exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  title: exploiteers/Meshtastic-Exploiteers-Hacker-Pager
  accessed: '2026-09-06'
  note: Firmware repo; confirms it is a fork of Meshtastic and links the separate electronics and case repos.
- kind: url
  url: https://github.com/exploiteers/Electronics-Design-Exploiteers-Hacker-Pager
  title: exploiteers/Electronics-Design-Exploiteers-Hacker-Pager
  accessed: '2026-09-07'
  note: KiCad project, schematic PDFs and BOM; CERN OHL-S v2; based on the Heltec V3 LoRa module.
- kind: url
  url: https://github.com/exploiteers/Case-Design-Files-Exploiteers-Hacker-Pager
  title: exploiteers/Case-Design-Files-Exploiteers-Hacker-Pager
  accessed: '2026-09-07'
  note: Case, button and acrylic-plate files; FDM print guidance; CERN OHL-S v2.
- kind: url
  url: https://hackaday.com/2025/07/31/hands-on-the-hacker-pager/
  title: 'Hands-On: The Hacker Pager'
  accessed: '2026-09-06'
  note: 'DEF CON 33 (2025) details: $200 Green/Black, $250 Pink/Black and Orange/Black, sold-out pre-orders with units at DC33, CERN OHL v2, 36 RGB + 12 UV LEDs, 192x64 LCD, ambient clock mode, vibration/audible alerts, laser-cut acrylic + 3D-printed body.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-checked 2026-09-07 against all cited sources. The maker''s storefront and hackerpager.net now describe the DEF CON 34 (2026) edition (clear/yellow/orange acrylic, from $250), so DC33-specific pricing, colors and availability come from the Hackaday hands-on article; core specs match across maker pages and press. The two product photos saved earlier were removed: they came from the current storefront and show the clear DC34 edition under colored stage lighting, and their captions (''red/blue'', ''blue'' color options) were wrong. Quantity made, SAO header, and inputs were not stated in any source. Radio chip (Semtech SX1262) and dimensions (114 x 84 x 22.2 mm) confirmed but have no field in this schema.'
last_modified_date: '2026-09-07'
related:
- dc34-dc34-hacker-pager
---

The Hacker Pager is a retro-styled, open-source wireless messenger built by exploitee.rs around an Espressif ESP32-S3 and a Semtech SX1262 LoRa radio, running a custom fork of the Meshtastic mesh-networking firmware. Shaped like a classic pager, it carries a 192x64 monochrome LCD with a green backlight (including an idle ambient-clock mode), 36 addressable RGB LEDs plus 12 UV LEDs for notifications, and a rechargeable LiPo battery, and it can operate standalone or tether to the Meshtastic phone app over Bluetooth.

Beyond messaging, the device doubles as a LoRa radio multitool: it can capture packets to .pcap (with an accompanying Wireshark dissector), run a spectrum analyzer over 850-950 MHz, execute a CHIP-8 virtual machine for retro games, and run BadUSB scripts, alongside vibration and audible alerts for incoming messages. At DEF CON 33 (2025) it sold for $200 in standard green/black or $250 in the pink/black and orange/black special editions; preorders sold out ahead of the con, with units sold in person there and an email list for later batches.

Hardware and firmware are open source: the firmware is a public fork of Meshtastic, and the electronics (a KiCad project based on the Heltec V3 LoRa module) and the 3D-printed body, buttons and laser-cut acrylic plates are published under CERN OHL-S v2 in separate GitHub repositories.

## Make your own

The KiCad electronics files, schematic PDFs and BOM are in the electronics repo (`make_your_own.hardware_url`); the case, button and acrylic-plate files are in the case repo (the README recommends FDM printing with a 0.4 mm nozzle and 0.2 mm layers, and lists the M2.5 screws needed); and the firmware is the Meshtastic fork in `make_your_own.firmware_url`. Assembly steps beyond that were not detailed in the sources checked.
