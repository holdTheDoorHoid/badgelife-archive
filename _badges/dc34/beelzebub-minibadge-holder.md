---
title: Beelzebub Minibadge Holder
id: dc34-beelzebub-minibadge-holder
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc34
year: 2026
makers:
- name: distinctm1nd
  url: https://github.com/distinctm1nd
summary: An open-source, horror-themed holder that displays five SAINTCON-style minibadges behind 24 addressable NeoPixel LEDs.
functions: Lights 24 NeoPixel LEDs behind five mounted minibadges, with pre-programmed light themes plus a 3-pin UPDI connector for custom ATtiny firmware.
look:
  colors:
  - black
  shape: null
  themes:
  - horror
  - halloween
  - village badge
tech:
  mcu: ATtiny814
  leds:
    count: 24
    type: NeoPixel
    note: Pre-programmed themes included; user-programmable via a 3-pin UPDI connector.
  display: none
  connectivity: []
  battery: USB or batteries (optional battery holder, requires soldering)
  sao_version: null
get_one:
  price: $45
  price_usd: 45.0
  quantity: ''
  availability: sold_out
  availability_note: Listed as sold out on the maker's Shopify store as of 2026-09-06.
  distribution:
  - purchase
  where: Sold via the maker's Shopify store (ghoul.lol), with DEF CON pickup offered as a checkout option; comes assembled except for the minibadge headers and optional battery holder, which require soldering. Minibadges themselves are not included.
make_your_own:
  open_source: true
  hardware_url: https://github.com/distinctm1nd/beelzebub_minibadge_holder/tree/main/hardware
  firmware_url: https://github.com/distinctm1nd/beelzebub_minibadge_holder/tree/main/firmware
  eda_tool: null
  license: null
  notes: Maker's store listing describes it as "open source hardware and software"; no license file found in the repo.
links:
- label: ghoul.lol
  url: https://ghoul.lol/
  kind: store
- label: github.com/distinctm1nd/beelzebub_minibadge_holder
  url: https://github.com/distinctm1nd/beelzebub_minibadge_holder
  kind: repo
- label: Beelzebub Minibadge Holder (product page)
  url: https://ghoul.lol/products/beelzebub-minibadge-holder
  kind: store
images:
- file: assets/images/badges/dc34/beelzebub-minibadge-holder/f1a0d441c8.jpg
  source: https://github.com/distinctm1nd/beelzebub_minibadge_holder
  credit: distinctm1nd
  caption: Assembled Beelzebub minibadge holder with LEDs lit
- file: assets/images/badges/dc34/beelzebub-minibadge-holder/1d4c8bc8cc.png
  source: https://github.com/distinctm1nd/beelzebub_minibadge_holder
  credit: distinctm1nd
  caption: Beelzebub minibadge holder PCB front view
contact:
  discord: distinctm1nd
  emails:
  - distinctm1nd@pm.me
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 54
  updated: 7/31/2026 13:17:37
  listing: New
- kind: url
  url: https://github.com/distinctm1nd/beelzebub_minibadge_holder
  title: distinctm1nd/beelzebub_minibadge_holder
  accessed: '2026-09-06'
  note: 'README and repo structure: ATtiny814 MCU, 3-pin UPDI programming connector, firmware/hardware/images directories.'
- kind: url
  url: https://ghoul.lol/products/beelzebub-minibadge-holder
  title: Beelzebub Minibadge Holder – Cabinet of Distinctm1nd
  accessed: '2026-09-06'
  note: Price ($45), sold-out status, 24 NeoPixel LEDs, open source hardware/software claim, assembly and DEF CON pickup details.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Maker's GitHub repo and Shopify store agree on the core facts (ATtiny814, 24 NeoPixels, open source). No license file found in the repo despite the "open source" claim, so license is left empty. Quantity made is not stated anywhere found.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/beelzebub-minibadge-holder.glb
  method: gerber
  source_file: hardware/beelzebub_expansion_board.kicad_pcb
  generated: '2026-09-07'
  bytes: 458808
  size_mm:
  - 142.5
  - 141.9
---

The Beelzebub Minibadge Holder is a horror-themed accessory by distinctm1nd, sold through their Cabinet of Distinctm1nd store for DEF CON 34. It mounts five SAINTCON-style minibadges behind a backlight of 24 addressable NeoPixel LEDs, driven by an ATtiny814 microcontroller. The board ships mostly assembled, with pre-programmed light themes ready to go out of the box, but the minibadge headers and an optional battery holder are left for the buyer to solder, and the minibadges themselves are sold separately.

The design is open source: firmware and hardware files are published on GitHub, and the LEDs are re-programmable over a 3-pin UPDI connector without needing to desolder anything. The maker's README points programmers unfamiliar with UPDI toward a megatinycore/Arduino IDE walkthrough as a starting point. The unit sold for $45 with an option for DEF CON pickup at checkout, and is listed as sold out as of this research pass.

## Make your own

Hardware and firmware sources are in the `hardware/` and `firmware/` directories of the [GitHub repo](https://github.com/distinctm1nd/beelzebub_minibadge_holder). Programming uses the ATtiny814's UPDI interface via the board's 3-pin connector; no soldering is required to reflash it. The README recommends setting up megatinycore in the Arduino IDE for first-time UPDI programmers, and notes that a resistor normally needed in series with pin 6 is already built onto the board.
