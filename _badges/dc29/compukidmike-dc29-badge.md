---
title: DEF CON 29 Official Badge
id: dc29-compukidmike-dc29-badge
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: compukidmike (MK Factor)
  url: https://mkfactor.com/
summary: 'The official DEF CON 29 (2021) attendee badge: a four-key RGB mechanical macro pad designed by Michael "compukidmike" and Katie Whiteley (MK Factor), configurable over USB and able to link edge-to-edge with other attendees'' badges.'
functions: 'Four hot-swappable Gateron Blue mechanical keys with individually addressable RGB, out of the box mapped to Discord controls (mute, push-to-talk, emotes); three capacitive touch pads used for volume control; ships as a USB serial device with a configuration interface for remapping keys and LED colors; edge connectors let badges physically link together; updates via UF2 drag-and-drop in USB mass-storage bootloader mode; persistent challenge/game stats stored separately from firmware in flash.'
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - puzzle
tech:
  mcu: ATSAMD21G16B
  leds:
    count: 4
    type: RGB
    note: One RGB LED per mechanical key
  display: none
  connectivity:
  - usb
  battery: CR2032
  sao_version: null
get_one:
  price: $300
  price_usd: 300
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold in person at DEF CON 29 (Las Vegas, 2021) as the conference's official attendee badge.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/compukidmike/Defcon29
  firmware_url: https://github.com/compukidmike/Defcon29
  eda_tool: null
links:
- label: github.com/compukidmike/Defcon29
  url: https://github.com/compukidmike/Defcon29
  kind: repo
- label: MK Factor
  url: https://mkfactor.com/
  kind: website
- label: 'Hackaday: Hands On: DEF CON 29 Badge Embraces The New Normal'
  url: https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
  kind: article
images:
- file: assets/images/badges/dc29/compukidmike-dc29-badge/46e884c0c9.jpg
  source: "https://github.com/compukidmike/Defcon29"
  credit: "compukidmike (MK Factor)"
  caption: "Badge type variants for the DEF CON 29 official badge"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- This is the official DEF CON 29 conference badge itself, not a third-party SAO or add-on.
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Defcon29
  title: compukidmike DC29 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc29''.'
- kind: url
  url: https://github.com/compukidmike/Defcon29
  title: 'GitHub - compukidmike/Defcon29: DEF CON 29 Badge (by MK Factor)'
  accessed: '2026-09-07'
  note: 'README confirms this is the official DEF CON 29 badge (ATSAMD21G16B MCU, UF2 bootloader, links to DEF CON Media Server); code/hardware files published under an open license.'
- kind: url
  url: https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
  title: 'Hands On: DEF CON 29 Badge Embraces The New Normal'
  accessed: '2026-09-07'
  note: 'Confirms four-key RGB mechanical macro pad, Gateron Blue switches, capacitive touch volume pads, USB-C, CR2032 battery, edge connectors for linking badges.'
- kind: url
  url: https://mkfactor.com/
  title: MK Factor
  accessed: '2026-09-07'
  note: 'Confirms MK Factor is Michael (compukidmike) and Katie Whiteley, the badgelife duo credited with designing the DEF CON 29 badge; site itself does not list DC29 pricing/quantity details.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This entry, sourced from a "SAOs to buy" link list, actually documents the official DEF CON 29 conference badge (not a standalone SAO or a third-party add-on) designed by Michael "compukidmike" and Katie Whiteley under the MK Factor name. Quantity produced was not found in available sources; $300 price is widely reported as the in-person badge price for DC29 but could not be confirmed on a maker storefront since it was sold directly at the con.'
last_modified_date: '2026-09-07'
---

The DEF CON 29 badge was the official electronic conference badge for DEF CON's 2021 event, designed by Michael "compukidmike" and Katie Whiteley, who work together as MK Factor — one of badgelife's best-known husband-and-wife design teams. Built around an Atmel/Microchip ATSAMD21G16B (a 32-bit Cortex-M0+ chip with 64KB flash and 8KB RAM), the badge takes the form of a four-key RGB mechanical macro pad using hot-swappable Gateron Blue switches, with three capacitive touch pads for volume control. Out of the box it was configured as a Discord control pad (mute, push-to-talk, emotes), but it enumerates as a USB serial device with its own configuration interface, letting owners remap each key's function and RGB color.

Badges could be physically linked together edge-to-edge with other attendees' units, and could run untethered from a computer off a CR2032 coin cell. Firmware is field-updatable by holding a button while plugging the badge in over USB, which drops it into a UF2 mass-storage bootloader; challenge/game progress is stored separately in flash so it survives firmware updates. MK Factor published the badge's firmware source and some hardware design files on GitHub under a permissive license, along with compiled `.uf2` files that fixed a 31-character bug found during the con, and pointed to the official DEF CON Media Server for the full Microchip Studio toolchain used to build it.

## Make your own

Hardware and firmware files are on GitHub at [compukidmike/Defcon29](https://github.com/compukidmike/Defcon29). The repo includes compiled `.uf2` firmware updates (flash by holding the bottom-right button while plugging the badge into USB to enter bootloader mode, then dragging the file onto the resulting mass-storage device) and source written in Microchip Studio 7.0 with the ASF framework; a `Hardware` folder holds board/reference files including an image of the badge type variants. The bootloader-protected first 8KB of flash is fuse-locked; removing it requires an SWD programmer.
