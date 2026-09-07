---
title: UPDeeDeeI Adapter SAO
id: dc34-moth-updi-programmer-working-title
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Xenu (Lepi Labs)
  url: https://lepi-labs.com
summary: A moth-eyed SAO sold at DEF CON 34 that doubles as a fully working UPDI programmer, complete with a folding "USB tongue" FPC cable.
functions: Cycles through RGB color effects and lighting modes on its two eye LEDs via a mode button; functions as a UPDI programmer that can flash its own onboard ATtiny814 or an external target MCU.
look:
  colors:
  - black
  - purple
  - gold
  - red
  shape: moth
  themes:
  - animal
  - hardware tool
  - learn to solder
tech:
  mcu: ATtiny814
  leds:
    count: 2
    type: RGB
    note: Two 90-degree RGB LEDs behind UV-resin diffusers form the moth's eyes; a separate blue TX LED indicates programming activity.
  display: none
  connectivity:
  - usb
  - uart
  - i2c
  battery: CR2032 (or powered by host badge's SAO connector)
  sao_version: null
  sao_ports: 1
get_one:
  price: ~$40
  price_usd: 40.0
  quantity: 7
  availability: sold_out
  availability_note: Not listed on lepi-labs.com/shop as of 2026-09-06; likely sold at the con itself and not restocked online.
  distribution:
  - purchase
  where: Sold directly by Lepi Labs at DEF CON 34.
make_your_own:
  open_source: true
  hardware_url: https://github.com/lepi-labs/6-dc34-moth-badge
  firmware_url: https://github.com/lepi-labs/6-dc34-moth-badge
  gerbers_url: null
  bom_url: null
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: Repository contains KiCad schematics/PCB (board/), firmware (code/), art files (art/), and the USB tongue FPC design (tongue_fpc/). No LICENSE file found in the repo.
links:
- label: lepi-labs.com/shop
  url: https://lepi-labs.com/shop
  kind: store
- label: lepi-labs.com
  url: https://lepi-labs.com
  kind: website
- label: lepi-labs/6-dc34-moth-badge
  url: https://github.com/lepi-labs/6-dc34-moth-badge
  kind: repo
- label: uberflux.com/product/LEPI-dc34-moth
  url: https://uberflux.com/product/LEPI-dc34-moth
  kind: store
- label: labs.com
  url: https://labs.com
  kind: website
images:
- file: assets/images/badges/dc34/moth-updi-programmer-working-title/e4381b1a17.jpg
  source: https://github.com/lepi-labs/6-dc34-moth-badge
  credit: Lepi Labs (Xenu)
  caption: UPDeeDeeI Adapter SAO with moth-eye RGB LEDs and folding USB tongue cable
- file: assets/images/badges/dc34/moth-updi-programmer-working-title/5a6d91c76f.jpg
  source: https://uberflux.com/product/LEPI-dc34-moth
  credit: Lepi Labs
  caption: UPDeeDeeI SAO, moth-shaped UPDI programmer with FPC tongue USB cable
- file: assets/images/badges/dc34/moth-updi-programmer-working-title/94019163fe.jpg
  source: https://uberflux.com/product/LEPI-dc34-moth
  credit: Lepi Labs
  caption: UPDeeDeeI SAO, additional angle showing the moth eyes and CR2032/SAO connector
contact:
  discord: xenu
  emails:
  - xenu@lepi-labs.com
  raw:
  - 'Bluesky:'
  handles:
  - '@lepi'
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 10
  updated: 5/26/2026 20:39:07
  listing: New
- kind: url
  url: https://github.com/lepi-labs/6-dc34-moth-badge
  title: 'lepi-labs/6-dc34-moth-badge: RGB SAO with onboard UPDI adapter'
  accessed: '2026-09-06'
  note: Confirmed real title ("UPDeeDeeI Adapter"), MCU (ATtiny814), LED setup, UPDI programmer function, USB tongue cable, pin layout, and repo contents (KiCad board files, firmware, art).
- kind: url
  url: https://lepi-labs.com
  title: Lepi Labs
  accessed: '2026-09-06'
  note: Confirmed maker identity (Lepi Labs, a furry-community badge collective) and general product lines; no mention of this specific SAO on the site.
- kind: url
  url: https://lepi-labs.com/shop
  title: Lepi Labs Shop
  accessed: '2026-09-06'
  note: This SAO is not currently listed in the shop (other Lepi Labs badges are), suggesting it was sold only at DEF CON 34 and not restocked online.
- kind: sheet
  event: dc34
  row: 34
  updated: 7/6/2026 17:41:17
  listing: Update to Existing
- kind: url
  url: https://uberflux.com/product/LEPI-dc34-moth
  title: UPDeeDeeI SAO product page - Uberflux
  accessed: '2026-09-06'
  note: Maker, description, MCU, LEDs, price, quantity sold, images.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Sheet listed only a working title ("Moth UPDI programmer"); found the actual project via the maker's GitHub org, titled "UPDeeDeeI Adapter SAO" (GitHub repo lepi-labs/6-dc34-moth-badge, described by the maker as "RGB SAO with onboard UPDI adapter"). Retitled per research-guide rules while keeping the original id/filename. Could not confirm quantity made, exact price, or a license for the open-source files; the maker's own shop no longer lists it as of this check, so exact current availability is unclear (marked unknown rather than guessed). No separate Hackaday.io or storefront listing found for this specific item. Merged with duplicate entry 'UPDeeDeeI SAO' (dc34-updeedeei-sao).
last_modified_date: '2026-09-06'
redirect_from:
- /badges/dc34/updeedeei-sao/
---

The UPDeeDeeI Adapter is a Simple Add-On sold by Lepi Labs (maker Xenu) at DEF CON 34. It was listed on the community badge sheet only under a working title, "Moth UPDI programmer," but the maker's own GitHub repository reveals its real name and a moth theme carried through in its two glowing RGB eyes, each a 90-degree LED behind a UV-resin diffuser, cycled through colors and effects with a mode button.

Beyond being a wearable SAO with the standard I2C/GPIO pinout, the board is a genuinely useful tool: its onboard ATtiny814, CH340E USB-to-serial chip, and voltage regulation let it act as a full UPDI programmer, capable of flashing either its own microcontroller or an external target selected via jumpers and a 3V/5V switch. Rather than a plain USB-C-only design, it also includes a flexible "USB tongue" — a working FPC cable built into the moth's mouth that folds out to plug into a port directly.

The hardware and firmware are shared on GitHub (schematics and PCB in KiCad, firmware source, and the art and FPC tongue designs all included), though no explicit license file was found in the repository. As of this check the item is not listed on Lepi Labs' online shop, consistent with it having been a con-exclusive sale rather than an ongoing product.

## Notes merged from the duplicate entry "UPDeeDeeI SAO"

The UPDeeDeeI SAO is a moth-shaped add-on made by Xenu of Lepi Labs for DEF CON 34. Beyond decorating a badge, it is a fully working UPDI programmer built around an ATtiny814, based on the open-source UPDI-programmer design by Stefan Wagner. Its centerpiece trick is a flexible printed-circuit "tongue" that folds out from the moth's mouth and acts as a real USB cable, connecting the SAO to a computer to flash UPDI-capable AVR chips, either the board's own microcontroller or an external target via a jumper. A CH340E handles the USB-to-serial conversion and an AP2122K regulates power, with the UPDI voltage configurable between 3.3V and 5V.

Two RGB LEDs behind hot-glue diffusers form the moth's glowing eyes; a button cycles through several color and lighting modes when the SAO isn't busy programming. It can run off a CR2032 coin cell or draw power from a host badge's SAO connector. Lepi Labs sold it for $35 through their Uberflux storefront, with all 7 units made selling out. The hardware, firmware, and artwork are published on GitHub, split into folders for board design, code, artwork, and miscellaneous documentation, though no explicit open-source license is stated.

This entry duplicates dc34-moth-updi-programmer-working-title, an earlier sheet row for the same maker and item that had only a working title; that entry should be reconciled with this fuller record.
