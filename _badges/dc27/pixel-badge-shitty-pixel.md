---
title: Pixel Badge (Shitty Pixel)
id: dc27-pixel-badge-shitty-pixel
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
summary: An SAO shaped and lit to look like an oversized WS2812 RGB LED, with a companion standalone "Pixel Badge" controller built to guarantee it would work at DEF CON 27.
functions: 'Cycles through an RGB rainbow by default on 3 LEDs; between roughly 3 and a dozen selectable animations, changeable over I2C or, on the companion Pixel Badge, via onboard buttons (FUNC, SAVE, +, -) with settings saved to EEPROM.'
look:
  colors: []
  shape: null
  themes:
  - meme
tech:
  mcu: ATtiny85
  leds:
    count: 3
    type: reverse-mount
    note: PLCC2 reverse-mount LEDs arranged to mimic a single large WS2812 package
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: v1.69bis
get_one:
  price: $20
  price_usd: 20
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: 'Sold on Tindie as "Silly Pixel - SAO Badge Add On" by blinkingthing; listing showed the seller on a break until Nov 25, 2019 when checked.'
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/164567-pixel-badge-shitty-pixel
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/164567-pixel-badge-shitty-pixel
  url: https://hackaday.io/project/164567-pixel-badge-shitty-pixel
  kind: hackaday
- label: Silly Pixel - SAO Badge Add On (Tindie)
  url: https://www.tindie.com/products/blinkingthing/silly-pixel-sao-badge-add-on/
  kind: store
images:
  - file: assets/images/badges/dc27/pixel-badge-shitty-pixel/624c242b07.jpg
    source: "https://hackaday.io/project/164567-pixel-badge-shitty-pixel"
    credit: "blinkingthing"
    caption: "Pixel Badge (Shitty Pixel) project photo"
  - file: assets/images/badges/dc27/pixel-badge-shitty-pixel/effb98f5d5.png
    source: "https://hackaday.io/project/164567-pixel-badge-shitty-pixel"
    credit: "blinkingthing"
    caption: "Shitty Pixel SAO board detail"
contact: {}
notes:
- Uses AP2331SA-7 between the SAO 3.3v bus and power supply to protect against hot-swap.
- Also includes a CAT24C03WI-GT3 EEPROM for storing animation/settings state, and ICSP pads for reprogramming the ATtiny85.
- 'The Hackaday project covers two related items: the "Shitty Pixel" SAO itself (sold on Tindie, listed there under the name "Silly Pixel", likely a store-policy rename), and a standalone battery-powered "Pixel Badge" controller with its own ATtiny85, buttons, and battery holder, which the maker built specifically to guarantee compatibility because they were not confident the SAO alone would work with every DEF CON 27 badge.'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/164567-pixel-badge-shitty-pixel
  title: Pixel Badge (Shitty Pixel)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/164567-pixel-badge-shitty-pixel
  title: Pixel Badge (Shitty Pixel) - Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed maker (blinkingthing), that it was made for DEF CON 27 (started March 2019), ATtiny85 + CAT24C03WI-GT3 EEPROM + AP2331SA-7 power IC, 3 LEDs, and that Gerbers/schematics/code were shared on the project page.
- kind: url
  url: https://www.tindie.com/products/blinkingthing/silly-pixel-sao-badge-add-on/
  title: Silly Pixel - SAO Badge Add On (Tindie)
  accessed: '2026-09-07'
  note: Confirms price ($20), SAO v1.69bis compatibility, 12 animations, 50mm x 50mm size, and that the seller was on a sales break (checked date shows sold out/unavailable at time of check); datasheet on this listing names the product "W220497AXS14 Sh*tty Pixel".
- kind: url
  url: https://hackaday.io/project/164567-pixel-badge-shitty-pixel/log/166579-pixel-badge-is-born
  title: 'Pixel Badge is born (project log)'
  accessed: '2026-09-07'
  note: Explains the standalone "Pixel Badge" companion controller, its buttons/battery holder, and the maker's stated reason for building it.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Quantity made is not stated anywhere found. Firmware/code repository link was not located (the maker said on the project log they planned to "post the code after Defcon" but no direct GitHub/firmware URL was found in the sources checked). No maker photos of the finished, cased Pixel Badge controller were found distinct from the SAO images saved here.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/pixel-badge-shitty-pixel/
---

The Shitty Pixel is a "Shitty Add-On" (SAO) built by Hackaday.io user blinkingthing for DEF CON 27 (2019), shaped and lit to resemble a giant WS2812 RGB LED. Three reverse-mount LEDs sit under the frosted lens, defaulting to an RGB rainbow cycle but capable of a dozen or so animations set over I2C, driven by an onboard ATtiny85 with a CAT24C03WI-GT3 EEPROM for storing state. An AP2331SA-7 power IC sits between the SAO's 3.3V bus and the board to make it safe to hot-swap onto a live badge. It sold on Tindie (listed there as "Silly Pixel," likely a store-safe rename of the same "Sh*tty Pixel" product) for $20.

Because the maker wasn't confident every DEF CON 27 badge's SAO header would drive the Shitty Pixel correctly, they also built a standalone companion device, the "Pixel Badge": its own battery-powered board with an ATtiny85, an indicator LED, a power switch, and FUNC/SAVE/+/- buttons for cycling and saving animation, speed, and brightness settings to EEPROM. The single Hackaday.io project page (164567) documents both the SAO and its badge-shaped controller together, which is why the archive entry carries both names.

## Make your own

The Hackaday.io project page includes schematics, a Gerber file for the PCB, and Arduino code referenced in the project logs, though no separate hosted firmware repository was found during this research pass.
