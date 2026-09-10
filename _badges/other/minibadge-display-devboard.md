---
title: Minibadge Display Devboard
id: other-minibadge-display-devboard
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 0
makers:
- name: Pips801
  url: https://pips.engineering
summary: A small development PCB that supplies power, battery charging, and a clock signal to custom-built SAINTCON minibadge displays.
functions: 'Powers a custom minibadge display board: provides 3x 3.3V@1A outputs, a clock signal, LiPo battery charge/use via USB-C, and ground/VBATT, so a builder does not have to design their own power circuitry.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - kit
tech:
  mcu: none
  leds: null
  display: null
  connectivity:
  - usb
  battery: LiPo (charged via USB-C, up to 800mA)
  sao_version: null
get_one:
  price: $25 (5-9 units $22 each, 10+ $20 each)
  price_usd: 25
  quantity: ''
  availability: sold_out
  availability_note: Listed as "Out of Stock" on Tindie, checked 2026-09-07.
  distribution:
  - purchase
  where: Sold via the maker's Tindie store (Pips Engineering / Beehive Engineering); design files free on GitHub.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/Pips801/Minibadge-Display-Devboard
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/Pips801/Minibadge-Display-Devboard
  url: https://github.com/Pips801/Minibadge-Display-Devboard
  kind: repo
  archived: https://web.archive.org/web/20260507163112/https://github.com/Pips801/Minibadge-Display-Devboard
- label: Minibadge Display Devboard - Pips Engineering
  url: https://pips.engineering/minibadge-display-devboard/
  kind: website
- label: Minibadge Display Devboard on Tindie
  url: https://www.tindie.com/products/pips/minibadge-display-devboard/
  kind: store
  archived: https://web.archive.org/web/20251215050357/https://www.tindie.com/products/pips/minibadge-display-devboard/
images:
- file: assets/images/badges/other/minibadge-display-devboard/9011dd4f1a.jpg
  source: https://github.com/Pips801/Minibadge-Display-Devboard
  credit: Pips801
  caption: Minibadge Display Devboard, top view
  archived: https://web.archive.org/web/20260507163112/https://github.com/Pips801/Minibadge-Display-Devboard
- file: assets/images/badges/other/minibadge-display-devboard/2eb71738a1.jpg
  source: https://github.com/Pips801/Minibadge-Display-Devboard
  credit: Pips801
  caption: Minibadge Display Devboard, alternate view
  archived: https://web.archive.org/web/20260507163112/https://github.com/Pips801/Minibadge-Display-Devboard
contact: {}
notes:
- host board for displaying minibadges
status: released
sources:
- kind: url
  url: https://github.com/Pips801/Minibadge-Display-Devboard
  title: Minibadge-Display-Devboard
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
  archived: https://web.archive.org/web/20260507163112/https://github.com/Pips801/Minibadge-Display-Devboard
- kind: url
  url: https://github.com/Pips801/Minibadge-Display-Devboard
  title: Minibadge-Display-Devboard README
  accessed: '2026-09-07'
  note: README specs, assembly steps, and datasheet links; confirmed open-source KiCad design and image URLs.
  archived: https://web.archive.org/web/20260507163112/https://github.com/Pips801/Minibadge-Display-Devboard
- kind: url
  url: https://pips.engineering/minibadge-display-devboard/
  title: Minibadge Display Devboard - Pips Engineering
  accessed: '2026-09-07'
  note: Maker's own blog post about the board, posted 2026-01-05; links to Tindie store.
- kind: url
  url: https://www.tindie.com/products/pips/minibadge-display-devboard/
  title: Minibadge Display Devboard - Tindie
  accessed: '2026-09-07'
  note: Price ($25, volume discounts) and out-of-stock status.
  archived: https://web.archive.org/web/20251215050357/https://www.tindie.com/products/pips/minibadge-display-devboard/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a general-purpose development board for the SAINTCON minibadge ecosystem, not something made for one specific convention or year -- it is a tool for builders creating their own minibadge displays, sold year-round via Tindie rather than tied to a single event. No event correction applies; left under "other". No LEDs or display of its own (it is a power/support board for other people's minibadge boards), so tech.leds and tech.display are left empty. Maker also sells a related "ATtiny 816/1616 Minibadge Devboard" on Tindie -- a different product, not this one.
last_modified_date: '2026-09-07'
---

The Minibadge Display Devboard is an open-source development board by Pips801 (Pips Engineering / Beehive Engineering) that handles the power electronics for custom-built SAINTCON minibadge displays. Rather than a badge or SAO itself, it is a support board: it takes USB-C or LiPo battery power and outputs three regulated 3.3V@1A rails, a clock signal, ground, and battery voltage, so someone designing their own minibadge display PCB does not need to solve battery charging, voltage regulation, or clock generation themselves. It connects either via castellated edge-mount pads for direct board-to-board designs or through WAGO push-in terminals for wired setups.

The board is built around a BQ21040 battery management IC, AP7361C voltage regulators, a 74HC4060 clock generator, a DRV8837C clock driver, and a TPS2121 power-path mux. It supports LiPo batteries with optional NTC temperature sensing, up to 800mA charging, and an estimated capacity of 30-40 minibadges spread across its three output rails. The GitHub repository documents a full workflow for designing a compatible display in KiCad, including footprint setup, schematic wiring, and PCB placement guidance, plus a changelog for an "R2" revision that improved thermal management and power-path switching.

The board is sold through the maker's Tindie store for $25 (with volume discounts), though it was out of stock as of this check. All hardware design files are published on GitHub under an open-source license, and the KiCad symbols/footprints are meant to be imported directly into a builder's own minibadge display project.
