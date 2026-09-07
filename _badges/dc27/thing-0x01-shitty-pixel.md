---
title: Thing 0x01 - Shitty Pixel
id: dc27-thing-0x01-shitty-pixel
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: blinkingthing
  url: https://hackaday.io/blinkingthing
summary: 'A Shitty Add-On modeled after an oversized WS2812 RGB LED, made by blinkingthing for DEF CON 27.'
functions: 'By default cycles an RGB rainbow animation across its 3 LEDs; a host badge (or a bus pirate/Raspberry Pi) can send I2C commands to change the mode, speed, and per-channel intensity, and save the state to EEPROM.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - retro computer
tech:
  mcu: ATtiny85
  leds:
    count: 3
    type: reverse-mount
    note: PLCC2 reverse-mount RGB LEDs (Osram TOPLED/SunLED style) laid out to mimic a WS2812's internal die and bond wires.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: "$20"
  price_usd: 20
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: 'Sold on Tindie (listed there as "Silly Pixel"); also distributed at DEF CON 27 in 2019.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: blinkingthing.github.io/docs/W220497AXS14.pdf
  url: https://blinkingthing.github.io/docs/W220497AXS14.pdf
  kind: website
- label: Pixel Badge (Shitty Pixel) - Hackaday.io
  url: https://hackaday.io/project/164567-pixel-badge-shitty-pixel
  kind: hackaday
- label: Silly Pixel - SAO Badge Add On on Tindie
  url: https://www.tindie.com/products/blinkingthing/silly-pixel-sao-badge-add-on/
  kind: store
images:
  - file: assets/images/badges/dc27/thing-0x01-shitty-pixel/55cbbd6a43.jpg
    source: "https://www.tindie.com/products/blinkingthing/silly-pixel-sao-badge-add-on/"
    credit: "blinkingthing"
    caption: "Shitty Pixel SAO, an oversized WS2812 RGB LED replica badge add-on"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- Sold under the name "Silly Pixel" on Tindie; the maker's own datasheet and Hackaday.io project both call it "thing 0x01 - Shitty Pixel".
status: released
sources:
- kind: url
  url: https://blinkingthing.github.io/docs/W220497AXS14.pdf
  title: Thing 0x01 - Shitty Pixel
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''other''.'
- kind: url
  url: https://hackaday.io/project/164567-pixel-badge-shitty-pixel
  title: Pixel Badge (Shitty Pixel) | Hackaday.io
  accessed: '2026-09-07'
  note: Confirms it was made for DEF CON 27 (2019), ATtiny85 + EEPROM, 50mm square board, hand-soldered and sold on Tindie plus distributed at the con.
- kind: url
  url: https://www.tindie.com/products/blinkingthing/silly-pixel-sao-badge-add-on/
  title: Silly Pixel - SAO Badge Add On from blinkingthing on Tindie
  accessed: '2026-09-07'
  note: Storefront listing at $20, same 3-LED/12-animation description; listing was showing "on break" (not currently purchasable) when checked; used for a product photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Corrected event from "other" to dc27 (DEF CON 27, 2019) per the maker''s Hackaday.io project and datasheet. No hardware/firmware repo or gerber link was found, so make_your_own fields are left empty rather than guessed. Quantity made and current availability were not stated anywhere found; get_one.availability left as unknown since the Tindie listing''s "on break" status is dated (checked years after the fact, not a live signal). The product is sold under two names: "Shitty Pixel" (maker''s own datasheet/Hackaday.io) and "Silly Pixel" (Tindie storefront, likely a naming variant for the marketplace).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/thing-0x01-shitty-pixel/
---

The Shitty Pixel is a Simple Add-On (SAO) made by blinkingthing for DEF CON 27 in 2019, designed to look like a giant version of the WS2812 RGB LED it imitates functionally: the PCB art traces mimic the die and bond wires you'd see inside the real chip package. Underneath, an ATtiny85 drives three individually controllable PLCC2 reverse-mount RGB LEDs through about a dozen built-in animations, defaulting to a rainbow cycle. An onboard EEPROM (with fields for DC year, maker ID, SAO type ID, and arbitrary data) lets settings persist across power cycles.

Because it follows the SAO v1.69bis standard, the badge exposes its I2C bus so that a host badge — or, failing badge support, a bus pirate or Raspberry Pi — can send simple write commands to change the animation mode, speed, and per-channel (red/green/blue) intensity, and to save or reload that state from EEPROM. The maker's own datasheet is candid that there was no coordination with badge makers ahead of release, so support from any particular host badge wasn't guaranteed.

The board was sold through Tindie (listed there under the name "Silly Pixel") for $20 and also handed out at DEF CON 27. No public hardware or firmware repository was found for this project, so it isn't confirmed as open source.
