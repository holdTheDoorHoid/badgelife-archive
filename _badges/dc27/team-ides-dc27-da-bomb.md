---
title: Team IDES DC27 Da Bomb
id: dc27-team-ides-dc27-da-bomb
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: John Adams
  url: https://hackaday.io/john-adams
  role: Team Ides
- name: Bill Paul
  role: Team Ides
summary: A rechargeable, BLE-linked electronic badge made by Team Ides for DEF CON 27, following their DC25 "Ides of Defcon" badge.
functions: RGB LED effects, stereo sound (up to 24-bit/96kHz) through PCB-mounted speakers, a small LCD, a Konami-code easter egg via its seven buttons, and BLE GATT-based multiplayer games between badges.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: nRF52840 (BMD-340 module)
  leds:
    count: null
    type: null
    note: Driven by an IS31FL3736 32x8 matrix LED driver chip (replaced earlier WS2812B parts) with global current control for dimming.
  display: small LCD
  connectivity:
  - ble
  battery: rechargeable (LiPo)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '500'
  availability: unknown
  distribution:
  - crowdfunding
  where: Sold via a Kickstarter campaign and troupeit.com/badge.
make_your_own:
  open_source: true
  hardware_url: https://github.com/netik/dc27_badge
  firmware_url: https://github.com/netik/dc27_badge
  eda_tool: null
links:
- label: hackaday.io/project/161163-team-ides-dc27-da-bomb
  url: https://hackaday.io/project/161163-team-ides-dc27-da-bomb
  kind: hackaday
  archived: https://web.archive.org/web/20251105151814/https://hackaday.io/project/161163-team-ides-dc27-da-bomb
- label: github.com/netik/dc27_badge
  url: https://github.com/netik/dc27_badge
  kind: repo
  archived: https://web.archive.org/web/20260509062554/https://github.com/netik/dc27_badge
images:
- file: assets/images/badges/dc27/team-ides-dc27-da-bomb/20ab33f703.jpg
  source: https://hackaday.io/project/161163-team-ides-dc27-da-bomb
  credit: Team Ides (John Adams / Bill Paul)
  caption: Da Bomb badge for DEF CON 27
  archived: https://web.archive.org/web/20251105151814/https://hackaday.io/project/161163-team-ides-dc27-da-bomb
- file: assets/images/badges/dc27/team-ides-dc27-da-bomb/6d917f87a1.jpg
  source: https://hackaday.io/project/161163-team-ides-dc27-da-bomb
  credit: Team Ides (John Adams / Bill Paul)
  caption: 3D render of the Da Bomb badge PCB
  archived: https://web.archive.org/web/20251105151814/https://hackaday.io/project/161163-team-ides-dc27-da-bomb
contact: {}
notes:
- Sheet listed a bare quantity of "500 units planned" and a Kickstarter goal of $35k-40k, with $15,000 in pledges reported reached during the campaign; exact final price per unit was not confirmed from the sources checked, so get_one.price is left blank.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/161163-team-ides-dc27-da-bomb
  title: Team IDES DC27 Da Bomb
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''DEF CON 27''.'
  archived: https://web.archive.org/web/20251105151814/https://hackaday.io/project/161163-team-ides-dc27-da-bomb
- kind: url
  url: https://github.com/netik/dc27_badge
  title: netik/dc27_badge
  accessed: '2026-09-07'
  note: Confirms open-source hardware/firmware repo (Apache 2.0) with Kickstarter, artwork, hardware and software directories.
  archived: https://web.archive.org/web/20260509062554/https://github.com/netik/dc27_badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, MCU, LEDs, BLE, sound, LCD, open-source repo) confirmed from the Hackaday.io project page and the maker's GitHub repo. Could not confirm a per-unit retail price or exact LED count/type; the Kickstarter campaign page and troupeit.com/badge storefront both returned errors (403/404) when checked directly, so availability/current storefront status is unconfirmed and left as unknown.
last_modified_date: '2026-09-07'
---

Da Bomb is the DEF CON 27 badge from Team Ides, the pairing of John Adams and Bill Paul, following their earlier "Ides of Defcon" badge for DC25. It runs on a Nordic nRF52840 (BMD-340 module) under ChibiOS, and pairs RGB LED effects (driven by an IS31FL3736 matrix LED driver, an upgrade from the WS2812B chips used previously) with a small LCD and stereo sound through onboard speakers, reportedly supporting audio up to 24-bit/96kHz. Seven buttons on the badge support a Konami-code easter egg, and badges can find each other and play multiplayer games over Bluetooth Low Energy using BLE GATT services.

The project was funded through a Kickstarter campaign with a stated goal in the $35k-40k range, reporting roughly $15,000 in pledges during the drive, and was also sold through troupeit.com/badge; about 500 units were planned. Both the hardware and firmware are open-sourced on GitHub under an Apache 2.0 license, with the repository organized into Kickstarter, Artwork, Hardware, and Software directories.

## Make your own

Hardware and firmware are both published at github.com/netik/dc27_badge under the Apache 2.0 license. The repo's `Hardware` directory holds the PCB design/schematics and `Software` holds the ChibiOS-based firmware; no separate BOM, Gerber-share, or EDA tool was identified from the pages checked.
