---
title: ATtiny 816/1616 Devboard
id: saintcon-2025-attiny-816-1616-devboard
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: Pips
  url: https://minibadge.wiki/?search=&author=Pips
summary: 'A minibadge-format development board for the ATtiny816/1616 microcontroller series, breaking out USART, I2C, DAC, SPI, ADC, and touch-sense pins for prototyping.'
functions: 'Prototyping/breakout board for the ATtiny816 or ATtiny1616: exposes USART (TX/RX/CK/DIR), I2C, SPI, and DAC headers, two ADC (analog input) pads, and two PTC (capacitive touch) pads. Programmed over UPDI via pin 6 (labeled PROG4). Chip is available with 8KB or 16KB of flash.'
look:
  colors:
  - black
  shape: rectangle
  themes:
  - hardware tool
tech:
  mcu: ATtiny816 / ATtiny1616
  leds:
    count: 2
    type: null
    note: 'Description mentions two LEDs on-board; type/color not specified.'
  display: none
  connectivity:
  - uart
  - i2c
  inputs:
  - touch
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: 'Per the maker: "Purchase one from me" (Pips/Pips801); no storefront link or price found.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=ATtiny%20816/1616%20Devboard&year=2025
  url: https://minibadge.wiki/?search=ATtiny%20816/1616%20Devboard&year=2025
  kind: website
images:
- file: assets/images/badges/saintcon-2025/attiny-816-1616-devboard/9efa930334.jpg
  source: "https://minibadge.wiki/?search=ATtiny%20816/1616%20Devboard&year=2025"
  credit: "Pips"
  caption: "Front of the ATtiny 816/1616 devboard minibadge"
- file: assets/images/badges/saintcon-2025/attiny-816-1616-devboard/cca5d23161.jpg
  source: "https://minibadge.wiki/?search=ATtiny%20816/1616%20Devboard&year=2025"
  credit: "Pips"
  caption: "Back of the ATtiny 816/1616 devboard minibadge"
contact: {}
notes:
- 'category: Personal; rarity: Super Rare'
- 'Soldering difficulty listed as "Beginner" (solder pin headers only). Board is marked HW-R1 and silkscreened "Pips801". Warning printed on the board and in the listing: do not plug the board in upside-down.'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=ATtiny%20816/1616%20Devboard&year=2025
  title: ATtiny 816/1616 Devboard
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2025''.'
- kind: url
  url: https://minibadge.wiki/2025.json
  title: 'Minibadge Wiki 2025 data feed (JSON entry for ATtiny 816/1616 Devboard)'
  accessed: '2026-09-07'
  note: 'The wiki''s search page is client-rendered from this JSON feed; used it to get the full listing text (description, soldering instructions, difficulty, quantity, rarity, timestamp) and the front/back image URLs, since the search-filtered page itself does not expose the record server-side.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found is the community-run minibadge.wiki entry (author-submitted, by "Pips"/"Pips801"). No maker storefront, repo, hardware files, or price could be found. quantityMade in the source data is listed as 0, which likely means "not disclosed" rather than a literal zero (the listing also says "Purchase one from me" and rarity "Super Rare"), so quantity and availability are left unset rather than guessed. LED type/color and battery/power are not stated anywhere. No separate hardware or firmware repo was found for this board.'
last_modified_date: '2026-09-07'
---

The ATtiny 816/1616 Devboard is a SAINTCON 2025 minibadge made by Pips (submitting as "Pips801") as a small prototyping platform rather than a wearable art piece. It breaks out the pins of Microchip's ATtiny816 or ATtiny1616 (8-bit AVR parts sharing a footprint, available in 8KB or 16KB flash versions) to labeled header blocks for USART, I2C, SPI, and DAC, plus two analog input pads and two capacitive touch-sense pads. Programming is done over UPDI through a single pin. The board carries two on-board LEDs, though their color and part number are not specified in the listing.

The listing rates it "Beginner" difficulty, since assembly is limited to soldering pin headers, and warns explicitly not to plug the board in upside-down. It is tagged "Personal" category and "Super Rare" rarity on the community wiki, and the only stated way to get one is "Purchase one from me" — no price, quantity, or public storefront link was found. No hardware or firmware repository was located for this board, so open-source status is unknown.
