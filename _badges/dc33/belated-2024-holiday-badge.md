---
title: Belated 2024 Holiday Badge
id: dc33-belated-2024-holiday-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: klipper
  url: https://mkfactor.com/shop/index.php?rt=product/product&product_id=132
summary: A gingerbread-house-shaped soldering kit badge with an ESP32, 25 RGB LEDs acting as an advent-calendar countdown, and two customizable window displays, running WLED.
functions: |-
  25 RGB LEDs, Dual Screens, and an ESP32 running WLED, and a SAINTCON Minibadge Header. This was going to be a 2024 project, that got...ahem...delayed. So now it is a 2025 holiday badge with fond memories of 2024? Or maybe I can't remember what year it is? But hey! it's here in PLENTY of time for next christmas and it only says 2024 on the back... so you're good... yeah.. totally

  Will be at DEFCON, happy to meet up and deliver
look:
  colors: []
  shape: house
  themes:
  - holiday
  - learn to solder
  - kit
tech:
  mcu: ESP32
  leds:
    count: 25
    type: RGB
    note: Runs WLED; used as a 25-day advent-calendar countdown to Christmas.
  display: two window displays (updateable with different images)
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: $40
  price_usd: 40.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold through the MK Factor storefront and on Tindie as a soldering kit; surface-mount parts pre-soldered, buyer solders the through-hole parts.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/compukidmike/BCTDWDFK
  firmware_url: https://github.com/compukidmike/WLED-BCTDWDFK
  eda_tool: null
links:
- label: mkfactor.com/shop/index.php?rt=product/product&product_id=132
  url: https://mkfactor.com/shop/index.php?rt=product/product&product_id=132
  kind: store
- label: compukidmike/BCTDWDFK (hardware/assembly)
  url: https://github.com/compukidmike/BCTDWDFK
  kind: repo
- label: compukidmike/WLED-BCTDWDFK (firmware)
  url: https://github.com/compukidmike/WLED-BCTDWDFK
  kind: repo
- label: Holiday Soldering Kit on Tindie
  url: https://www.tindie.com/products/compukidmike/holiday-soldering-kit/
  kind: store
images:
  - file: assets/images/badges/dc33/belated-2024-holiday-badge/498d4815b7.jpg
    source: "https://www.tindie.com/products/compukidmike/holiday-soldering-kit/"
    credit: "MK Factor (klipper)"
    caption: "The gingerbread-house-shaped 2024 Holiday Badge with dual window displays and RGB LEDs"
  - file: assets/images/badges/dc33/belated-2024-holiday-badge/deaa3ddb3e.jpg
    source: "https://mkfactor.com/shop/index.php?rt=product/product&product_id=132"
    credit: "MK Factor (klipper)"
    caption: "Assembled 2024 Holiday Badge in the MK Factor shop listing"
contact:
  emails:
  - klipper@lgclassic.com
notes: []
status: listed
sources:
- kind: sheet
  event: dc33
  row: 54
  updated: 7/30/2025
- kind: url
  url: https://mkfactor.com/shop/index.php?rt=product/product&product_id=132
  title: 2024 Holiday Badge - MK Factor shop
  accessed: '2026-09-06'
  note: Primary listing; price, chip, LED count, screens, WLED, SAINTCON minibadge spot, source code link.
- kind: url
  url: https://github.com/compukidmike/BCTDWDFK
  title: compukidmike/BCTDWDFK (GitHub)
  accessed: '2026-09-06'
  note: Hardware/assembly repo; confirms ESP32, 25 addressable LEDs on GPIO17, button, SAO-compatible header, gingerbread-house PCB shape, schematic PDF.
- kind: url
  url: https://github.com/compukidmike/WLED-BCTDWDFK
  title: compukidmike/WLED-BCTDWDFK (GitHub)
  accessed: '2026-09-06'
  note: Firmware repo (WLED fork/config with daily presets); confirms both hardware and firmware are open source.
- kind: url
  url: https://www.tindie.com/products/compukidmike/holiday-soldering-kit/
  title: Holiday Soldering Kit - Tindie
  accessed: '2026-09-06'
  note: Same kit sold on Tindie as "Holiday Soldering Project - Gingerbread House with Advent LEDs and Screens in the Windows"; $40 (volume discounts for 2+), USA shipping only, seller MKFactor (Mike, Riverton UT), 52 orders at time of check.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts confirmed directly on the maker's own storefront and GitHub repos. Quantity made/remaining and current stock status not stated anywhere found, so get_one.quantity and availability are left unknown. No dedicated Hackaday.io project page found.
last_modified_date: '2026-09-06'
---

The Belated 2024 Holiday Badge is a gingerbread-house-shaped soldering kit made by klipper of MK Factor, sold both through the MK Factor storefront and on Tindie. It is built around an ESP32 running WLED, with 25 addressable RGB LEDs used as an advent-calendar countdown and two window displays that can be updated with different images. A header on the house's "chimney" accepts a SAINTCON-style minibadge. As a kit, its surface-mount parts arrive pre-soldered, and the buyer solders the through-hole components (the ESP32 module, displays, button, and minibadge header) themselves.

The badge was originally planned as a 2024 project but was finished late, so the maker sold it in 2025 while keeping the "2024" branding on the back as a joke, framing it as being "in plenty of time for next Christmas." It was priced at $40 (with volume discounts on Tindie for multiple units) and offered for pickup or delivery at DEF CON 33, alongside standard shipping within the USA.

Both the hardware and firmware are open source. The hardware/assembly repository (`compukidmike/BCTDWDFK`) includes a schematic PDF and step-by-step build instructions, and the firmware repository (`compukidmike/WLED-BCTDWDFK`) provides a WLED build with daily preset automation for the LED countdown.

## Make your own

Hardware files, a schematic PDF, and assembly instructions are in [compukidmike/BCTDWDFK](https://github.com/compukidmike/BCTDWDFK); the WLED firmware and preset files are in [compukidmike/WLED-BCTDWDFK](https://github.com/compukidmike/WLED-BCTDWDFK). Builders solder the ESP32 module, the two displays, the tactile button, and the SAO-style minibadge header to the gingerbread-house PCB, then flash `firmware.bin` and load `wled_presets.json` through WLED's web interface.
