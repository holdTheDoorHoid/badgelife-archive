---
title: Shitty Kitty V2
id: dc33-shitty-kitty-v2
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
series: Shitty Kitty
makers:
- name: Uberfoo Heavy Industries
  url: https://uberfoo.net
summary: A cat-shaped RP2040 badge with two 0.96" color IPS screens and two fully-wired SAO ports, the second generation of Uberfoo's "Shitty Kitty" line sold at DEF CON 33.
functions: Runs Uberfoo's "SkittyOS" firmware with graphics demos and a customizable scrolling-text name badge (adjustable fonts/sizes with extended character support); each screen can be configured and dimmed independently to save battery. Ships with immediate support for the Skull of Fate SAO from MakeItHackin. Firmware is updated over USB-C using built-in USB mass-storage mode.
look:
  colors:
  - green
  shape: cat
  themes:
  - cat
  - animal
tech:
  mcu: RP2040
  leds:
    count: 2
    type: discrete
    note: Charge (CHRG) and power-good (PG) status LEDs next to the battery-management IC; not addressable/animation LEDs.
  display: 2x 0.96" 80x160 color IPS
  connectivity:
  - usb
  - uart
  - i2c
  inputs:
  - buttons
  battery: LiPo 2000 mAh
  power: USB-C (charging and firmware updates)
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: $75
  price_usd: 75.0
  quantity: ''
  availability: sold_out
  availability_note: 'Wayback Machine snapshot from 2025-07-16 shows the listing marked "Sold out"; checked 2026-09-06.'
  distribution:
  - purchase
  - preorder
  where: Sold as a preorder through Uberfoo's Shopify store (shop.uberfoo.net, now offline); buyers picked badges up at the Badgelife Community area during DEF CON 33, with shipping offered only after the con and only if inventory remained.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Uberfoo-Heavy-Industries/shitty-kitty-v2
  firmware_url: null
  gerbers_url: null
  bom_url: https://github.com/Uberfoo-Heavy-Industries/shitty-kitty-v2/blob/main/shitty_kitty_v2.csv
  eda_tool: KiCad
  license: null
  notes: Hardware (schematic, PCB layout, BOM) is published on GitHub with no license file. The maker's product listing said open-source firmware would be released after DEF CON 33; no firmware repo naming this hardware revision was found. Uberfoo's "skitty-ng" repo (C++, MIT-0 license) may be related firmware for the Shitty Kitty line but could not be confirmed as targeting V2 specifically.
links:
- label: shop.uberfoo.net/products/shitty-kitty-v2
  url: https://shop.uberfoo.net/products/shitty-kitty-v2
  kind: store
- label: github.com/Uberfoo-Heavy-Industries/shitty-kitty-v2
  url: https://github.com/Uberfoo-Heavy-Industries/shitty-kitty-v2
  kind: repo
- label: uberfoo.net
  url: https://uberfoo.net
  kind: website
images:
- file: assets/images/badges/dc33/shitty-kitty-v2/b935a28261.jpg
  source: "https://web.archive.org/web/20250716215340/https://shop.uberfoo.net/products/shitty-kitty-v2"
  credit: "Uberfoo Heavy Industries"
  caption: "Shitty Kitty V2 badge, front view with dual IPS screens"
- file: assets/images/badges/dc33/shitty-kitty-v2/b0612697e2.jpg
  source: "https://web.archive.org/web/20250716215340/https://shop.uberfoo.net/products/shitty-kitty-v2"
  credit: "Uberfoo Heavy Industries"
  caption: "Shitty Kitty V2 badge, back view showing the polycarbonate back case enclosing the 2000 mAh LiPo battery"
contact:
  emails:
  - james@uberfoo.net
notes: []
status: released
sources:
- kind: sheet
  event: dc33
  row: 7
  updated: 6/13/2025 13:36:02
- kind: url
  url: "https://web.archive.org/web/20250716215340/https://shop.uberfoo.net/products/shitty-kitty-v2"
  title: "Shitty Kitty V2 – Uberfoo Heavy Industries (Wayback Machine snapshot, 2025-07-16)"
  accessed: '2026-09-06'
  note: "Full spec sheet (RP2040, dual 0.96in IPS screens, 2000mAh LiPo, dual SAO v1.69bis ports, 5 buttons, USB-C), price, sold-out status, DEF CON 33 pickup details, and the two product photos; the live shop is offline as of 2026-09-06."
- kind: url
  url: "https://github.com/Uberfoo-Heavy-Industries/shitty-kitty-v2"
  title: "Uberfoo-Heavy-Industries/shitty-kitty-v2 (GitHub)"
  accessed: '2026-09-06'
  note: "KiCad schematic/PCB/BOM confirm RP2040 MCU, USB-C, BQ24072/TPS63051 power management, and two SAOv169-BADGE-2x3 connectors; repo has no LICENSE file."
- kind: url
  url: "https://uberfoo.net"
  title: "Uberfoo Heavy Industries"
  accessed: '2026-09-06'
  note: "Confirms maker identity; the site's news item about the first badge launch refers to the original Shitty Kitty, not this V2 revision."
- kind: url
  url: "https://github.com/Uberfoo-Heavy-Industries/skitty-ng"
  title: "Uberfoo-Heavy-Industries/skitty-ng (GitHub)"
  accessed: '2026-09-07'
  note: "Repo exists (C++, MIT-0 license per GitHub metadata) but nothing in it seen names the V2 hardware, so it is only mentioned as a possible firmware repo."
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core specs and pricing come from the maker''s own archived storefront listing and their own GitHub hardware repo, so confidence is high. Quantity made was not stated anywhere found. The firmware repository could not be identified with confidence (see make_your_own.notes). The two saved photos are pulled from the archived Shopify listing, which credits no other photographer, so credited to Uberfoo Heavy Industries. Fact-check 2026-09-07: all fields re-checked against the archived listing (via Wayback), the hardware repo BOM/schematic, uberfoo.net and the sheet (contact email); the case material was corrected to polycarbonate per the listing.'
last_modified_date: '2026-09-07'
---

Shitty Kitty V2 is the second generation of Uberfoo Heavy Industries' cat-shaped badge, sold as a preorder ahead of DEF CON 33 with pickup at the Badgelife Community. The PCB itself is cut into a cat silhouette (with a hole in each ear) and carries two 0.96" 80x160 color IPS screens, each independently dimmable, driven by a Raspberry Pi RP2040. Two fully-wired SAO connectors (1.69bis, 6-pin) each expose their own GPIO, UART and I2C, and the badge ships already able to drive the Skull of Fate SAO from MakeItHackin.

Power comes from an included 2,000 mAh LiPo cell enclosed in a polycarbonate case on the back, charged and managed by a BQ24072 controller with a TPS63051 buck-boost regulator supporting up to 1.5A fast charging; a USB-C port handles both charging and firmware updates, the latter via built-in USB mass-storage support. Five buttons (plus a dedicated boot button) drive the "SkittyOS" firmware, which runs graphics demos and a configurable scrolling-text name-badge mode with adjustable fonts and international character support.

The listing promised the firmware would go open source after DEF CON 33, and the hardware (schematic, PCB layout and BOM) is already public on GitHub, though without a license file. By the time this entry was checked, the shop listing was marked sold out and the storefront itself had gone offline, so quantity made and current availability are unconfirmed.
