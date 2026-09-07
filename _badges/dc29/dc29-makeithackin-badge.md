---
title: MakeItHackin DEF CON 29 Badge
id: dc29-dc29-makeithackin-badge
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: MakeItHackin
  url: https://github.com/MakeItHackin
summary: Unofficial credit-card-shaped DEF CON 29 badge by MakeItHackin built around an ATtiny85 with an OLED display, RGB NeoPixels, a light sensor, a button and a SAO connector, carrying real 8.2 MHz Checkpoint and 58 kHz Sensormatic retail security tags so it sets off store alarm gates; sold on Tindie as the 'Anti-Theft Electronic Badge made for DEF CON 29' either fully assembled or as a kit, with a July 2023 firmware update adding menu scrolling and a 'shoplifting' video game.
functions: OLED menu system with scrolling, a built-in 'shoplifting' video game (added in a July 2023 firmware update), RGB NeoPixel lighting, and a light sensor for ambient response.
look:
  colors: []
  shape: card
  themes:
  - security
  - crime
  - retro computer
tech:
  mcu: ATtiny85
  leds:
    count: null
    type: RGB
    note: NeoPixel/WS2812-style RGB LEDs; exact count not stated by the maker.
  display: 0.96" OLED
  connectivity: []
  inputs:
  - button
  battery: null
  sao_version: null
get_one:
  price: $35 kit / $50 assembled
  price_usd: 50
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shows the product as retired/no longer available as of 2026-09-07.
  distribution:
  - purchase
  - kit
  where: Sold by the maker on Tindie, fully assembled or as a DIY kit (kit ships with the ATtiny85 in SOIC-8 and a 6-pin ISP header unsoldered).
make_your_own:
  open_source: true
  hardware_url: https://github.com/MakeItHackin/DEFCON29Badge
  firmware_url: https://github.com/MakeItHackin/DEFCON29Badge
  eda_tool: null
links:
- label: github.com/MakeItHackin/DEFCON29Badge
  url: https://github.com/MakeItHackin/DEFCON29Badge
  kind: repo
  archived: https://web.archive.org/web/20260513103905/https://github.com/MakeItHackin/DEFCON29Badge/
- label: www.tindie.com/products/makeithackin/makeithackin-def-con-29-electronic-badge
  url: https://www.tindie.com/products/makeithackin/makeithackin-def-con-29-electronic-badge/
  kind: store
- label: youtu.be/G82_usjS0wA
  url: https://youtu.be/G82_usjS0wA
  kind: video
- label: youtu.be/OIYtvjFRpec
  url: https://youtu.be/OIYtvjFRpec
  kind: video
images:
- file: assets/images/badges/dc29/dc29-makeithackin-badge/488e5599e8.jpg
  source: https://www.tindie.com/products/makeithackin/makeithackin-def-con-29-electronic-badge/
  credit: MakeItHackin
  caption: The MakeItHackin DEF CON 29 badge, credit-card shaped with OLED display and security tags
- file: assets/images/badges/dc29/dc29-makeithackin-badge/6a95cd1912.jpg
  source: https://github.com/MakeItHackin/DEFCON29Badge
  credit: MakeItHackin
  caption: PCB render of the badge showing ATtiny85, OLED, and SAO connector layout
  archived: https://web.archive.org/web/20260513103905/https://github.com/MakeItHackin/DEFCON29Badge/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/MakeItHackin/DEFCON29Badge
  title: DC 29 Badge and SAO (MakeItHackin/DEFCON29Badge)
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260513103905/https://github.com/MakeItHackin/DEFCON29Badge/
- kind: url
  url: https://github.com/MakeItHackin/DEFCON29Badge
  title: MakeItHackin/DEFCON29Badge README
  accessed: '2026-09-07'
  note: Confirms MCU, OLED, RGB LEDs, SAO connector, credit-card shape rationale, and dual security tags (8.2 MHz Checkpoint / 58 kHz Sensormatic); open-source hardware and firmware.
  archived: https://web.archive.org/web/20260513103905/https://github.com/MakeItHackin/DEFCON29Badge/
- kind: url
  url: https://www.tindie.com/products/makeithackin/makeithackin-def-con-29-electronic-badge/
  title: Anti-Theft Electronic Badge for DEF CON 29 (Tindie listing)
  accessed: '2026-09-07'
  note: Confirms assembled ($50) vs kit ($35) pricing, sold-out/retired status, light sensor, lanyard, 6-pin ISP header, and the July 2023 firmware update adding menu scrolling and a 'shoplifting' game.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's GitHub README and Tindie listing agree on the core facts. Exact LED count, PCB solder-mask color, and total quantity made are not stated anywhere found; left empty rather than guessed.
last_modified_date: '2026-09-07'
---

MakeItHackin's DEF CON 29 badge is an unofficial, credit-card-shaped electronic badge built around an ATtiny85 microcontroller, a 0.96" OLED display, RGB NeoPixel-style LEDs, a light sensor, a button, and a standard SAO connector. Its gimmick is literal: two working retail anti-theft tags are embedded in blank spots on the board, one tuned to 8.2 MHz for Checkpoint gate systems and one to 58 kHz for Sensormatic systems, so the badge itself can trip a store's security gates. The maker chose the credit-card outline specifically to play off that retail-security theme.

The badge was sold through Tindie, either fully assembled or as a DIY kit (the kit ships with the ATtiny85 in a SOIC-8 package and a 6-pin ISP header unsoldered, requiring the buyer to program it). Pricing was $35 for the kit and $50 assembled, and a lanyard was included. As of this check the Tindie listing shows the product retired and no longer purchasable. In July 2023 the maker pushed a firmware update adding OLED menu scrolling and a small built-in "shoplifting" video game.

## Make your own

Hardware design files, firmware source, and a bill of materials are published on GitHub at github.com/MakeItHackin/DEFCON29Badge under the maker's "unofficial DEF CON badge" series. The repository also links two YouTube videos: one unboxing and programming a fully-assembled unit, and one walking through kit assembly.
