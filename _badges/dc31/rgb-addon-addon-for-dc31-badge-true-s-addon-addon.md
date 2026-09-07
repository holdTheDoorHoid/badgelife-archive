---
title: RGB Addon Addon for DC31 Badge (true's Addon Addon)
id: dc31-rgb-addon-addon-for-dc31-badge-true-s-addon-addon
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: trueControl (true)
  url: https://basic.truecontrol.org/
summary: An RGB LED add-on that plugs into the official DEF CON 31 badge and, in turn, hosts a second GAT or v1.69bis-compliant addon through its own header, so a DC31 badge can run lighting programs while still carrying another shard.
functions: Runs more than six RGB LED programs (twinkle, rainbow, flicker, a moving trail, color toggling, and two accelerometer-reactive modes), each with adjustable parameters (delay, hue, saturation, brightness, sensitivity) saved to EEPROM. Selectable zones and brightness via front buttons (MODE, PROG, SET). Can power a hosted addon with its own LEDs turned off to save power.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: HK32F030MF4P6
  leds:
    count: 8
    type: RGB
    note: Addressable RGB LEDs in 3 configurable zones (5 front-firing, 2 side-firing, 1 rear-firing).
  display: none
  connectivity:
  - usb
  inputs:
  - buttons
  - accelerometer
  battery: rechargeable via USB-C (5V or USB PD); capacity not stated
  sao_version: null
get_one:
  price: $60.00 (marked down to $30.00 as of research date)
  price_usd: 30.0
  quantity: ''
  availability: available
  availability_note: 13 in stock per trueControl Shop, checked 2026-09-07; listing states pickup only at DEF CON 33, ships to buyers after about a week otherwise.
  distribution:
  - purchase
  where: trueControl's own webshop (shop.truecontrol.org)
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://git.trueserve.org/trueControl/dc31-addon-addon-badge-firmware
  eda_tool: null
  notes: Firmware repo is public. The product page promises a schematic link "coming soon" that was not yet posted as of research date.
links:
- label: basic.truecontrol.org/database/dc31/addon-addon
  url: https://basic.truecontrol.org/database/dc31/addon-addon/
  kind: website
- label: dc31-addon-addon-badge-firmware (trueserve Git)
  url: https://git.trueserve.org/trueControl/dc31-addon-addon-badge-firmware
  kind: repo
  archived: https://web.archive.org/web/20260417193634/https://git.trueserve.org/trueControl/dc31-addon-addon-badge-firmware
- label: true's RGB Addon Addon for DC31 Badge (trueControl Shop)
  url: https://shop.truecontrol.org/index.php?product_id=133&route=product%2Fproduct
  kind: store
  archived: https://web.archive.org/web/20260216202719/https://shop.truecontrol.org/index.php?route=product/product&product_id=133
- label: Addon Addon user manual
  url: https://dc31.truecontrol.org/yearsite/manual/addon-addon
  kind: doc
images:
- file: assets/images/badges/dc31/rgb-addon-addon-for-dc31-badge-true-s-addon-addon/ea9f8429b6.jpg
  source: https://shop.truecontrol.org/index.php?product_id=133&route=product%2Fproduct
  credit: trueControl (true)
  caption: true's RGB Addon Addon assembled and lit, showing the RGB LEDs
  archived: https://web.archive.org/web/20260216202719/https://shop.truecontrol.org/index.php?route=product/product&product_id=133
- file: assets/images/badges/dc31/rgb-addon-addon-for-dc31-badge-true-s-addon-addon/d3eac4af8e.jpg
  source: https://shop.truecontrol.org/index.php?product_id=133&route=product%2Fproduct
  credit: trueControl (true)
  caption: The Addon Addon inserted into a DEF CON 31 badge
  archived: https://web.archive.org/web/20260216202719/https://shop.truecontrol.org/index.php?route=product/product&product_id=133
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://basic.truecontrol.org/database/dc31/addon-addon/
  title: RGB Addon Addon for DC31 Badge (true's Addon Addon)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc31''.'
- kind: url
  url: https://dc31.truecontrol.org/yearsite/manual/addon-addon
  title: true's DEF CON 31 RGB Addon Addon - user manual
  accessed: '2026-09-07'
  note: Confirms button operation, RGB program list, and that it hosts GAT or v1.69bis addons through its own connector; charges from 5V/USB PD.
- kind: url
  url: https://git.trueserve.org/trueControl/dc31-addon-addon-badge-firmware
  title: dc31-addon-addon-badge-firmware (trueserve Git)
  accessed: '2026-09-07'
  note: 'README gives specs: HK32F030MF4P6 MCU (16K flash/4K RAM), Type-C USB with XMODEM bootloader, 8x addressable RGB LED in 3 zones, accelerometer, hosts GAT/SAO addons.'
  archived: https://web.archive.org/web/20260417193634/https://git.trueserve.org/trueControl/dc31-addon-addon-badge-firmware
- kind: url
  url: https://shop.truecontrol.org/index.php?product_id=133&route=product%2Fproduct
  title: true's RGB Addon Addon for DC31 Badge - trueControl Shop
  accessed: '2026-09-07'
  note: Confirms price ($60 marked to $30), 13 in stock, fully assembled, insertion instructions, and product photos used for images.
  archived: https://web.archive.org/web/20260216202719/https://shop.truecontrol.org/index.php?route=product/product&product_id=133
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own project page, user manual, firmware repo README, and shop listing all agree on the core facts. Not found: total quantity ever made, exact battery capacity, hardware/schematic files (promised "coming soon" on the shop page but not linked), and LED part number (site just says "addressable RGBLED"). Possible duplicate: _badges/dc31/addon-addon.md ("Addon addon", id dc31-addon-addon) has the same generic title but attributes the maker as "Whiskey Pirate Crew" and lists price $70 — unclear whether that is the same item misattributed on the community sheet or a distinct addon; left untouched per one-entry-per-task rule.'
last_modified_date: '2026-09-07'
related:
- dc31-addon-addon
---

true's Addon Addon is an RGB lighting add-on built for the official DEF CON 31 badge. It plugs into the badge's addon slot and, unusually for a shard, also carries its own header that hosts a second GAT- or v1.69bis-compliant addon, so a DC31 badge wearer could run the Addon Addon's own light shows while still keeping another shard plugged in and powered (with its LEDs off if the wearer wants). It runs on an HK32F030MF4P6 microcontroller and drives 8 addressable RGB LEDs — 5 front-firing, 2 side-firing, and 1 rear-firing — split into 3 independently configurable zones, plus an onboard accelerometer for two motion-reactive lighting modes. Three front buttons (MODE, PROG, SET) step through more than six programs (twinkle, rainbow, flicker, a moving trail effect, color toggling, and the accelerometer modes), each with adjustable parameters saved to EEPROM, and a fourth press cycles brightness.

The board charges over USB-C from a plain 5V source or a USB PD charger, and the same port doubles as a firmware-update path: holding PROG at power-on drops it into an XMODEM bootloader reachable over a CH340 virtual COM port. Firmware source is published on trueControl's self-hosted Gitea, including notes on hacking around STM32CubeIDE to build for the HK32F030 part; a promised schematic link had not been posted as of this research pass.

The Addon Addon has continued to be sold well after DEF CON 31 itself — as of September 2026 it was still listed, fully assembled, on trueControl's own webshop at a discounted $30 (down from $60), with 13 units in stock, sold for pickup at DEF CON 33 or shipped after about a week.

## Make your own

Firmware source and build notes are at the [dc31-addon-addon-badge-firmware repo](https://git.trueserve.org/trueControl/dc31-addon-addon-badge-firmware): clone it, build with STM32CubeIDE (patched per the repo's `hax/` directory) or program via J-Link, or push updates in the field over the Type-C XMODEM bootloader. No hardware/schematic files were found published at research time.
