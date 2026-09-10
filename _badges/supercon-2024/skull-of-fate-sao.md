---
title: Skull of Fate SAO
id: supercon-2024-skull-of-fate-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: MakeItHackin and p1x317h13f
  url: https://hackaday.io/hacker/1518893-makeithackin
summary: A tarot-card SAO representing Atropos of the Greek Fates, with a SAMD21, 42 NeoPixel LED eye animations, accelerometer, PDM microphone and an ST25DV64KC NFC chip that delivers one of 78 Rider-Waite tarot readings, entered in the Supercon 8 SAO Contest in 2024.
functions: Default mode cycles through 25 eye animations (left button) and color adjustments (right button), with some animations reacting to motion (accelerometer) and sound (microphone). Holding both buttons switches to tarot mode, which "draws" a random card from the 78-card Rider-Waite deck and writes the reading to the onboard NFC chip for NFC-enabled devices to read. Also functions as an I2C client, so it can be read by a compatible host badge (e.g. Raspberry Pi Pico W).
look:
  colors:
  - black
  shape: skull
  themes:
  - skull
  - horror
  - fantasy
tech:
  mcu: ATSAMD21G18A (SAMD21, Arduino-compatible)
  leds:
    count: 44
    type: WS2812B
    note: XL-1010RGBC-WS2812B 1mm addressable RGB LEDs used for eye animations
  display: none
  connectivity:
  - nfc
  - i2c
  battery: null
  sao_version: null
get_one:
  price: $45
  price_usd: 45
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - contest
  where: Sold via Tindie; also entered in the Supercon 8 SAO Contest at Hackaday Supercon 2024. Tindie listing shows out of stock since June 20, 2025.
make_your_own:
  open_source: true
  hardware_url: https://github.com/MakeItHackin/SkullOfFate/
  firmware_url: https://github.com/MakeItHackin/SkullOfFate/
  eda_tool: null
links:
- label: hackaday.io/project/198974-skull-of-fate-sao
  url: https://hackaday.io/project/198974-skull-of-fate-sao
  kind: hackaday
  archived: https://web.archive.org/web/20260506065633/https://hackaday.io/project/198974-skull-of-fate-sao
- label: github.com/MakeItHackin/SkullOfFate
  url: https://github.com/MakeItHackin/SkullOfFate/
  kind: repo
  archived: https://web.archive.org/web/20260506065631/https://github.com/MakeItHackin/SkullOfFate
- label: www.tindie.com/products/makeithackin/skull-of-fate-sao
  url: https://www.tindie.com/products/makeithackin/skull-of-fate-sao/
  kind: store
  archived: https://web.archive.org/web/20260503104521/https://www.tindie.com/products/makeithackin/skull-of-fate-sao/
- label: youtu.be/K-RiMK6Kz78
  url: https://youtu.be/K-RiMK6Kz78
  kind: video
images:
- file: assets/images/badges/supercon-2024/skull-of-fate-sao/2b392d0f14.jpg
  source: https://hackaday.io/project/198974-skull-of-fate-sao
  credit: MakeItHackin and p1x317h13f
  caption: Skull of Fate SAO, skull-shaped tarot SAO with NeoPixel eyes
  archived: https://web.archive.org/web/20260506065633/https://hackaday.io/project/198974-skull-of-fate-sao
- file: assets/images/badges/supercon-2024/skull-of-fate-sao/26870a25f6.jpg
  source: https://www.tindie.com/products/makeithackin/skull-of-fate-sao/
  credit: MakeItHackin
  caption: Skull of Fate SAO product photo from the Tindie listing
  archived: https://web.archive.org/web/20260503104521/https://www.tindie.com/products/makeithackin/skull-of-fate-sao/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198974-skull-of-fate-sao
  title: Skull of Fate SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260506065633/https://hackaday.io/project/198974-skull-of-fate-sao
- kind: url
  url: https://hackaday.io/project/198974-skull-of-fate-sao
  title: Skull of Fate SAO - Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker, event/contest (Supercon 8 SAO Contest 2024), MCU, sensors, NFC chip, dual-mode function, and that Gerbers/schematics are on GitHub.
  archived: https://web.archive.org/web/20260506065633/https://hackaday.io/project/198974-skull-of-fate-sao
- kind: url
  url: https://www.tindie.com/products/makeithackin/skull-of-fate-sao/
  title: Skull of Fate SAO - Tindie listing
  accessed: '2026-09-07'
  note: Price ($45), sold-out status (since 2025-06-20), LED count/animation count, and full feature description.
  archived: https://web.archive.org/web/20260503104521/https://www.tindie.com/products/makeithackin/skull-of-fate-sao/
- kind: url
  url: https://github.com/MakeItHackin/SkullOfFate/
  title: MakeItHackin/SkullOfFate - GitHub
  accessed: '2026-09-07'
  note: Exact part numbers (ATSAMD21G18A-MU, LIS3DHTR, GMA4030H11-F26, HX3144ESO, ST25DV16K-IER6T3, W25Q128JVSIQ), MIT license, and confirmation that Gerbers/schematic/BOM/code are published.
  archived: https://web.archive.org/web/20260506065631/https://github.com/MakeItHackin/SkullOfFate
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: EDA tool not stated on any source checked. Quantity made not stated. sao_version (4-pin vs 6-pin) not stated in sources checked, left null. Battery/power not stated (likely powered by host badge via SAO header, but not confirmed in sources so left null).
last_modified_date: '2026-09-07'
---

The Skull of Fate SAO is a tarot-themed add-on built by MakeItHackin and p1x317h13f for the Supercon 8 SAO Contest at Hackaday Supercon 2024. Styled after Atropos of the Greek Fates, the skull-shaped board runs a SAMD21 microcontroller and packs 44 tiny WS2812B NeoPixels into its eye sockets for 25 selectable animations, plus an accelerometer and PDM microphone so some animations react to motion and sound.

Its signature feature is the tarot mode: holding both onboard buttons "draws" a random card from a full 78-card Rider-Waite deck and writes the reading to an onboard ST25DV64KC NFC chip, which any NFC-reading phone or device can then pick up. It also works as an I2C client, letting a compatible host badge (such as a Raspberry Pi Pico W) talk to it directly.

The design is fully open source under the MIT license, with Gerbers, schematics, artwork, a bill of materials, and Arduino/MicroPython code examples published on GitHub. It was sold on Tindie for $45 and has been out of stock since June 2025; the quantity produced was not stated in the sources checked.
