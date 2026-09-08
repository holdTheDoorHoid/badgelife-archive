---
title: The Rabbit-Labs & The Pirates Plunder Badge
id: dc33-the-pirates-plunder-rabbit-labs-def-con-33-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Rabbit-Labs
  url: https://rabbit-labs.com/product/the-rabbit-labs-the-pirates-plunder-badge/
  role: hardware, sales
- name: RocketGod (RocketGod-git)
  url: https://github.com/RocketGod-git/Defcon33-TPP-RL-badge
  role: firmware (full-featured RF/menu firmware)
- name: zR_CrackiiN / JBOHack
  role: firmware (alternate LED-focused firmware)
- name: neednotapply, Talking Sasquatch, Frank, HamSpiced, AWOK, JCMK
  role: collaborators
summary: A limited-run collector's badge co-developed by vendor Rabbit-Labs and hardware/firmware collaborators (including RocketGod) for DEF CON 33, built around an ESP32-S3 with dual sub-GHz radios.
functions: RF transmit/receive and a jamming mode over two onboard CC1101 433 MHz radios, a display-driven menu system (RX, TX, Jammer, a Tesla-themed feature, settings/about screens), an SD-card file browser, and dozens of selectable idle LED animation patterns across 32 addressable RGB LEDs.
look:
  colors: []
  shape: null
  themes:
  - pirate
  - radio
  - security
  - hardware tool
tech:
  mcu: ESP32-S3-N16R8
  leds:
    count: 32
    type: WS2812B
    note: Addressable RGB LEDs driven from a single GPIO, with dozens of selectable idle patterns (breathe, rainbow, fire, matrix, pirate, etc.) in the firmware.
  display: 1.3" OLED (SH1106, I2C, 128x64) - sold as an optional add-on, not included by default
  connectivity:
  - sub-ghz
  - uart
  inputs:
  - buttons
  battery: 18650 Li-ion, with onboard charge controller (PD negotiation, reverse-polarity protection)
  sao_version: null
get_one:
  price: $174.99 (seen discounted to $125)
  price_usd: 174.99
  quantity: ''
  availability: limited
  distribution:
  - purchase
  where: Sold directly by Rabbit-Labs (rabbit-labs.com) and on Tindie; debuted at the Rabbit-Labs vendor booth at DEF CON 33. The maker states remaining stock is very limited and will not be restocked or reproduced.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/RocketGod-git/Defcon33-TPP-RL-badge
  eda_tool: null
  notes: A second, LED-focused firmware by zR_CrackiiN/JBOHack was also offered by the maker but its repository URL was not found.
links:
- label: github.com/RocketGod-git/Defcon33-TPP-RL-badge
  url: https://github.com/RocketGod-git/Defcon33-TPP-RL-badge
  kind: repo
- label: Rabbit-Labs product page
  url: https://rabbit-labs.com/product/the-rabbit-labs-the-pirates-plunder-badge/
  kind: store
- label: Tindie listing
  url: https://www.tindie.com/products/tehrabbitt/the-rabbit-labs-the-pirates-plunder-badge/
  kind: store
images:
  - file: assets/images/badges/dc33/the-pirates-plunder-rabbit-labs-def-con-33-badge/b405b0c960.jpg
    source: "https://rabbit-labs.com/product/the-rabbit-labs-the-pirates-plunder-badge/"
    credit: "Rabbit-Labs"
    caption: "Front of the assembled Rabbit-Labs / Pirates Plunder DEF CON 33 badge"
  - file: assets/images/badges/dc33/the-pirates-plunder-rabbit-labs-def-con-33-badge/b7f320af36.jpg
    source: "https://rabbit-labs.com/product/the-rabbit-labs-the-pirates-plunder-badge/"
    credit: "Rabbit-Labs"
    caption: "Back of the Rabbit-Labs / Pirates Plunder DEF CON 33 badge, showing the ESP32-S3, dual CC1101 modules, and 18650 battery holder"
contact: {}
notes:
- Independent DEF CON 33 badge with CC1101 RF transceiver (TX/RX/jammer), display and menu system, firmware open-sourced on GitHub; not present in the archive's existing dc33 list. Found by the event-year sweep, task dc33-indie.
- The discovery sweep's sources list only the RocketGod-git GitHub repo, which holds the full-featured firmware but no product/vendor context. The repo README itself has no text, only badge photos and a RocketGod logo image.
- The sweep's title ("The Pirates' Plunder - Rabbit-Labs DEF CON 33 Badge") is a rephrasing of the repo name; the maker (Rabbit-Labs) sells it as "The Rabbit-Labs & The Pirates Plunder Badge", which this entry now uses.
status: listed
sources:
- kind: url
  url: https://github.com/RocketGod-git/Defcon33-TPP-RL-badge
  title: The Pirates' Plunder - Rabbit-Labs DEF CON 33 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc33-indie); event read as ''dc33''.'
- kind: url
  url: https://raw.githubusercontent.com/RocketGod-git/Defcon33-TPP-RL-badge/main/badge%20pins.txt
  title: badge pins.txt
  accessed: '2026-09-08'
  note: Confirms MCU (ESP32-S3-N16R8), dual CC1101 radios, OLED, SD card, 5-way switch, and 32 WS2812B LEDs on GPIO21.
- kind: url
  url: https://raw.githubusercontent.com/RocketGod-git/Defcon33-TPP-RL-badge/main/globals.h
  title: globals.h
  accessed: '2026-09-08'
  note: Confirms menu structure (RX/TX/Jammer/Tesla/Settings), SH1106 128x64 display, and the list of LED idle patterns.
- kind: url
  url: https://rabbit-labs.com/product/the-rabbit-labs-the-pirates-plunder-badge/
  title: The Rabbit-Labs & The Pirates Plunder Badge
  accessed: '2026-09-08'
  note: Maker's own product listing - price, limited/no-restock availability, collaborator list, optional OLED, included lanyard/Foxx SAO, battery/charge-controller detail, and product photos.
- kind: url
  url: https://www.tindie.com/products/tehrabbitt/the-rabbit-labs-the-pirates-plunder-badge/
  title: The Rabbit-Labs & The Pirates Plunder Badge - Tindie
  accessed: '2026-09-08'
  note: Corroborates maker (Rabbit-Labs, Sayreville NJ), DEF CON 33 vendor-booth debut, price ($174.99), limited/no-restock status, and specs.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core hardware facts (MCU, dual CC1101, LEDs, display, SD card, menu firmware) confirmed directly from the maker''s firmware repo source files. Commercial details (price, availability, "very limited" stock, included lanyard/Foxx SAO, battery spec) come from the maker''s own storefront and Tindie listing, which agree with each other, so confidence is medium rather than high because exact quantity made and a hard sold-out date were not stated. Not verified: hardware design files/gerbers location (link not found - hardware_url left empty), exact LED count wiring beyond the pins file, and whether the badge shipped with the OLED display or it was always a separate add-on purchase (the product listing implies it is optional/additional).'
last_modified_date: '2026-09-08'
---

The Rabbit-Labs & The Pirates Plunder Badge is a limited-run collector's badge that debuted at the Rabbit-Labs vendor booth at DEF CON 33 in 2025. It was a group effort: Rabbit-Labs produced and sold the hardware, while firmware and features came from a handful of collaborators including RocketGod, zR_CrackiiN, JBOHack, and others credited on the product page. The board is built around an ESP32-S3-N16R8 with two onboard CC1101 433 MHz radio modules, a 5-way directional switch, an SD card reader, 32 addressable WS2812B RGB LEDs, a SAO port, and a slot for an 18650 lithium battery with its own charge/protection circuit.

Two independent firmware options exist for the badge. RocketGod's public repository implements a full menu-driven interface on an SH1106 OLED display, with RX, TX, and jammer modes for the sub-GHz radios, a Tesla-themed feature, file operations off the SD card, and dozens of selectable LED idle animations (rainbow, fire, matrix, pirate-themed, and more). A second, LED-focused firmware from zR_CrackiiN/JBOHack was also offered by the maker for people who wanted lighting effects without the RF tooling.

Rabbit-Labs sold the badge directly through its own storefront and on Tindie for around $175 (seen discounted to $125), bundled with a lanyard and a "Foxx" electrostatic-reactive SAO. The maker describes stock as very limited with no plans to restock or produce more once sold out. The OLED display appears to be sold as a separate add-on rather than included standard, based on the product listing's wording.
