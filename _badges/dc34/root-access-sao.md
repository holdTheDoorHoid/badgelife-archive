---
title: Root Access SAO
id: dc34-root-access-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: MakeItHackin and DannerCronise
summary: A standalone-art-object SAO for DEF CON 34 with a home-milled cedar body over a NeoPixel PCB, running 50 built-in light animations with full I2C control from the badge.
functions: An interactive SAO for DEF CON 34's badge. Runs 50 animations standalone (single-button cycling, hold to save a favorite, hold to turn off) or can be fully driven over I2C (address 0x50) by the DC34 badge or a Flipper Zero. Extra GPIO lines can be set as LED outputs or button inputs. Contains part PCB, part real wood, for a rooty tooty good time.
look:
  colors:
  - wood
  shape: null
  themes:
  - hardware tool
tech:
  mcu: ATtiny1616
  leds:
    count: 21
    type: mixed
    note: 10 addressable NeoPixel RGB LEDs plus 11 discrete LEDs (4 with PWM dimming)
  display: null
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: $50
  price_usd: 50.0
  quantity: ''
  availability: sold_out
  availability_note: Shopify listing showed sold out as of 2026-09-06.
  distribution:
  - purchase
  where: Sold via MakeItHackin's Shopify store and Uberflux around DEF CON 34 in Las Vegas; unpicked-up orders were shipped to customers afterward.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: https://github.com/MakeItHackin/RootAccess
  eda_tool: null
links:
- kind: store
  url: https://makeithackin.myshopify.com/products/root-access-sao
  title: Root Access SAO – makeithackin
  label: Shopify store listing
- kind: repo
  url: https://github.com/MakeItHackin/RootAccess
  title: MakeItHackin/RootAccess
  label: DEFCON 34 Root Access Interactive SAO (firmware/docs)
- kind: repo
  url: https://github.com/MakeItHackin/RootAccessI2cApp
  title: MakeItHackin/RootAccessI2cApp
  label: On-badge I2C companion app for DC34 badge firmware (experimental)
- label: uberflux.com/product/MIH-RootAccessSao
  url: https://uberflux.com/product/MIH-RootAccessSao
  kind: store
- label: www.youtube.com/watch?v=q30KheOV6QE
  url: https://www.youtube.com/watch?v=q30KheOV6QE
  kind: video
  archived: https://web.archive.org/web/20260805152608/https://www.youtube.com/watch?v=q30KheOV6QE
images:
- file: assets/images/badges/dc34/root-access-sao/ddbcc11091.jpg
  source: https://makeithackin.myshopify.com/products/root-access-sao
  credit: MakeItHackin
  caption: Root Access SAO, cedar wood body with NeoPixel LEDs
contact:
  discord: makeithackin
  emails:
  - andrew@makeithackin.com
  handles:
  - '@makeithackin'
  - '@dannercronise'
  raw:
  - and
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 33
  updated: 7/5/2026 17:38:26
  listing: New
- kind: url
  url: https://makeithackin.myshopify.com/products/root-access-sao
  title: Root Access SAO – makeithackin
  accessed: '2026-09-06'
  note: Price, sold-out availability, MCU, LED counts, I2C address, cedar body description, product photo.
- kind: url
  url: https://github.com/MakeItHackin/RootAccess
  title: MakeItHackin/RootAccess
  accessed: '2026-09-06'
  note: Confirms hardware (ATtiny1616, 10 NeoPixels, 11 discrete LEDs, I2C 0x50), button gestures, non-volatile favorite storage; no design files or license found in the README.
- kind: url
  url: https://github.com/MakeItHackin/RootAccessI2cApp
  title: MakeItHackin/RootAccessI2cApp
  accessed: '2026-09-06'
  note: Companion badge-side I2C firmware for talking to the SAO; noted as experimental, warns that flashing it erases the badge's shared light key permanently.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Maker's own Shopify listing and GitHub repo confirm hardware and pricing. Could not find design files (KiCad/Gerbers) or an explicit open-source license, so make_your_own.open_source is left null. Quantity made was not stated anywhere found. "DannerCronise" appears only as the sheet's second maker name/handle; no independent page for them was found, so makers.url/role are left off.
last_modified_date: '2026-09-06'
---

Root Access is an interactive SAO that MakeItHackin (with DannerCronise) built for DEF CON 34's badge. Instead of a plain PCB, the board sits under a body milled from cedar sourced from a Tennessee farm, so grain and color vary unit to unit. An ATtiny1616 drives 10 addressable NeoPixel RGB LEDs plus 11 discrete LEDs (four of them PWM-dimmable), cycling through 50 built-in animations — including a Knight Rider scan, Matrix rain, and a Tesla-coil effect — from a single button: a tap advances the mode, a 700ms hold turns it off, and a 3-second hold saves the current animation as the power-on favorite in non-volatile memory.

Beyond running on its own, the SAO exposes a full I2C interface at address 0x50, letting the DEF CON 34 badge or a Flipper Zero take direct control of the animations and use its spare GPIO lines as extra LED outputs or button inputs. MakeItHackin also published a companion project, RootAccessI2cApp, an experimental prebuilt DC34 badge firmware image that adds an on-badge I2C app for talking to the SAO — with a stated warning that flashing it permanently erases the badge's shared light key.

It sold for $50 through MakeItHackin's Shopify store and Uberflux around the DEF CON 34 event in Las Vegas, with orders not picked up on-site shipped out afterward; as of this check the Shopify listing shows it sold out. No hardware design files, BOM, or explicit license were found published alongside the firmware repo, so it is not marked open source.
