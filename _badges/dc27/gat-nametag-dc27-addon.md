---
title: GAT Nametag DC27 Addon
id: dc27-gat-nametag-dc27-addon
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: 'true (Whiskey Pirate Crew)'
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
summary: An SAO-style nametag addon with a 128x32 OLED that keeps your name upright using an accelerometer, with selectable fonts and RGB LED modes.
functions: Displays a name/text on an OLED with several selectable fonts; uses an ADXL345 accelerometer to rotate the displayed text so it stays upright regardless of how the badge is oriented; has programmable RGB LEDs with selectable color modes; buttons let the wearer configure fonts/modes on the fly; firmware is updatable over USB via an HID bootloader.
look:
  colors: []
  shape: rectangle
  themes:
  - text
  - wearable
tech:
  mcu: EFM8UB20F64G-B
  leds:
    count: null
    type: RGB
    note: Programmable RGB LEDs with selectable color modes; exact count not stated by the maker.
  display: 0.91" SSD1306 OLED (128x32, I2C)
  connectivity:
  - usb
  inputs:
  - buttons
  - accelerometer
  battery: USB or addon-supplied power (dual P-channel FET/diode power-source selection)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: approximately 113 fully assembled units plus 10 partially-assembled ("80%") kits
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to attendees at DEF CON 27 (2019); made as a side project to help fund the maker's Whiskey Pirates badge for DC28, so it was not sold through a separate storefront.
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  firmware_url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  eda_tool: null
  notes: 'Maker published firmware source/binary (gat_nametag_efm8_fw_0.2.7a.7z) and a REV3 schematic image on the Hackaday.io project page; no separate repo link was found.'
links:
- label: hackaday.io/project/166453-gat-nametag-dc27-addon
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  kind: hackaday
images:
- file: assets/images/badges/dc27/gat-nametag-dc27-addon/d5551f3699.jpg
  source: "https://hackaday.io/project/166453-gat-nametag-dc27-addon"
  credit: "true"
  caption: "GAT Nametag DC27 Addon assembled board"
- file: assets/images/badges/dc27/gat-nametag-dc27-addon/3cfb61273f.jpg
  source: "https://hackaday.io/project/166453-gat-nametag-dc27-addon"
  credit: "true"
  caption: "GAT Nametag DC27 Addon, in use"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  title: GAT Nametag DC27 Addon
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  title: GAT Nametag DC27 Addon
  accessed: '2026-09-07'
  note: 'Maker''s own project page; confirmed maker handle, event/year, MCU, display, accelerometer, LEDs, quantity made, open-source firmware/schematic, and images.'
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: 'Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27 | Hackaday'
  accessed: '2026-09-07'
  note: 'Search result confirming the badge appeared among the DEF CON 27 unofficial badge lineup; corroborates maker and purpose (funding the Whiskey Pirates DC28 badge).'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Price and exact LED count are not stated anywhere the maker wrote; it was a free give-away/side project rather than a sold item, so get_one.price and get_one.availability are left unfilled/unknown. sao_version/sao_ports not stated. A related later project "GAT Nametag SC8" (hackaday.io/project/198536) exists for a different event and is reported separately below, not folded into this entry.'
last_modified_date: '2026-09-07'
---

The GAT Nametag DC27 Addon is a name-badge addon built by the maker known as "true," of the Whiskey Pirate Crew, for DEF CON 27 in 2019. It centers on a 0.91" OLED that shows the wearer's name in one of several selectable fonts, paired with an ADXL345 accelerometer so the displayed text rotates to stay upright no matter how the badge is turned or worn. Programmable RGB LEDs and onboard buttons let the wearer switch fonts and light modes on the fly. "GAT" loosely stands for "Greater Addon Technology," a nod to the project being more capable than a typical SAO despite the "addon" name.

The maker built and gave away roughly 113 fully assembled units at DEF CON 27, plus about 10 partially-assembled "80%" units for people who wanted to finish soldering their own. It was created as a side project specifically to help fund the Whiskey Pirates' main badge for DEF CON 28, rather than being sold on its own; the maker's Hackaday.io page also mentions the possibility of a further run for Hackaday Supercon if there was enough interest.

## Make your own

The maker published firmware (source and binary, `gat_nametag_efm8_fw_0.2.7a.7z`) and a REV3 schematic image directly on the Hackaday.io project page, along with confirmation that the USB HID bootloader was tested and working on all units. No separate hardware repository or bill-of-materials link was found; anyone wanting to build one would need to reference the schematic and firmware archive posted there.
