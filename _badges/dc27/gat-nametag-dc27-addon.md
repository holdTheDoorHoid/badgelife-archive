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
- name: true (Whiskey Pirate Crew)
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
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: approximately 113 fully assembled units plus 10 partially-assembled ("80%") kits
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to attendees at DEF CON 27 (2019); made as a side project to help fund the maker's Whiskey Pirates badge for DC28, so it was not sold through a separate storefront.
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  firmware_url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  eda_tool: null
  notes: Maker published firmware source/binary (gat_nametag_efm8_fw_0.2.7a.7z) and a REV3 schematic image on the Hackaday.io project page; no separate repo link was found.
links:
- label: hackaday.io/project/166453-gat-nametag-dc27-addon
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  kind: hackaday
  archived: https://web.archive.org/web/20260218145209/https://hackaday.io/project/166453-gat-nametag-dc27-addon
- label: basic.truecontrol.org/dc27/gat-nametag
  url: https://basic.truecontrol.org/dc27/gat-nametag/
  kind: website
images:
- file: assets/images/badges/dc27/gat-nametag-dc27-addon/d5551f3699.jpg
  source: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  credit: 'true'
  caption: GAT Nametag DC27 Addon assembled board
  archived: https://web.archive.org/web/20260218145209/https://hackaday.io/project/166453-gat-nametag-dc27-addon
- file: assets/images/badges/dc27/gat-nametag-dc27-addon/3cfb61273f.jpg
  source: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  credit: 'true'
  caption: GAT Nametag DC27 Addon, in use
  archived: https://web.archive.org/web/20260218145209/https://hackaday.io/project/166453-gat-nametag-dc27-addon
- file: assets/images/badges/dc27/gat-nametag-dc27-addon/d5551f3699.jpg
  source: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  credit: true (trueControl)
  caption: GAT Nametag DC27 Addon
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  title: GAT Nametag DC27 Addon
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
  archived: https://web.archive.org/web/20260218145209/https://hackaday.io/project/166453-gat-nametag-dc27-addon
- kind: url
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  title: GAT Nametag DC27 Addon
  accessed: '2026-09-07'
  note: Maker's own project page; confirmed maker handle, event/year, MCU, display, accelerometer, LEDs, quantity made, open-source firmware/schematic, and images.
  archived: https://web.archive.org/web/20260218145209/https://hackaday.io/project/166453-gat-nametag-dc27-addon
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27 | Hackaday
  accessed: '2026-09-07'
  note: Search result confirming the badge appeared among the DEF CON 27 unofficial badge lineup; corroborates maker and purpose (funding the Whiskey Pirates DC28 badge).
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- kind: url
  url: https://basic.truecontrol.org/dc27/gat-nametag/
  title: GAT Nametag Addon (DC27)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27''. Page now returns 404 despite still being linked from the site''s own navigation; content confirmed via Hackaday.io project instead.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price and exact LED count are not stated anywhere the maker wrote; it was a free give-away/side project rather than a sold item, so get_one.price and get_one.availability are left unfilled/unknown. sao_version/sao_ports not stated. A related later project "GAT Nametag SC8" (hackaday.io/project/198536) exists for a different event and is reported separately below, not folded into this entry. Merged with duplicate entry 'GAT Nametag Addon (DC27)' (dc27-gat-nametag-addon-dc27).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc27/gat-nametag-addon-dc27/
---

The GAT Nametag DC27 Addon is a name-badge addon built by the maker known as "true," of the Whiskey Pirate Crew, for DEF CON 27 in 2019. It centers on a 0.91" OLED that shows the wearer's name in one of several selectable fonts, paired with an ADXL345 accelerometer so the displayed text rotates to stay upright no matter how the badge is turned or worn. Programmable RGB LEDs and onboard buttons let the wearer switch fonts and light modes on the fly. "GAT" loosely stands for "Greater Addon Technology," a nod to the project being more capable than a typical SAO despite the "addon" name.

The maker built and gave away roughly 113 fully assembled units at DEF CON 27, plus about 10 partially-assembled "80%" units for people who wanted to finish soldering their own. It was created as a side project specifically to help fund the Whiskey Pirates' main badge for DEF CON 28, rather than being sold on its own; the maker's Hackaday.io page also mentions the possibility of a further run for Hackaday Supercon if there was enough interest.

## Make your own

The maker published firmware (source and binary, `gat_nametag_efm8_fw_0.2.7a.7z`) and a REV3 schematic image directly on the Hackaday.io project page, along with confirmation that the USB HID bootloader was tested and working on all units. No separate hardware repository or bill-of-materials link was found; anyone wanting to build one would need to reference the schematic and firmware archive posted there.

## Notes merged from the duplicate entry "GAT Nametag Addon (DC27)"

The GAT Nametag Addon was released by the maker "true" (of trueControl / Whiskey Pirates) at DEF CON 27 in 2019 as a badge addon built to the GAT/SAO v1.69bis standard. It centers on a small OLED display that shows the wearer's name in one of several selectable fonts, and it uses an onboard accelerometer to keep the text upright no matter which way the badge is rotated or flipped. Programmable RGB LEDs and a pair of rear buttons round out the hardware, letting the wearer switch fonts, colors, and display modes on the fly.

By late July 2019 the maker had built roughly 113 working units, along with a number of partially-assembled "80% kits," and distributed them at DEF CON 27 through a closed reservation process rather than open retail sale. Firmware (version 0.2.7a) and a REV3 schematic were shared as downloadable files on the project's Hackaday.io page.
