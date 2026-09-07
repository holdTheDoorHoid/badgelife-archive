---
title: DC30-Tarot-Badge (DC540)
id: dc30-tarot-badge-dc540
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: DC540 Defcon Group
  url: https://dc540.org
summary: A Raspberry Pi Pico-powered badge with a 2.2" LCD and a 24-LED illuminated wheel that displays tarot cards, offers readings from three decks, and runs pairing and scavenger-hunt games with other badge wearers.
functions: Displays tarot card readings from three loaded decks (Rider-Waite-Smith, Tarot de Marseille, and a hand-drawn "Shitty Deck"); flashcard game to learn tarot meanings; a "pair" game between two badge wearers; a scavenger-hunt challenge tied to imagery on the Rider-Waite deck with real prizes; supports loading custom decks from the SD card.
look:
  colors: []
  shape: circle
  themes:
  - occult
  - fantasy
  - puzzle
  - ctf
tech:
  mcu: Raspberry Pi Pico (RP2040)
  leds:
    count: 24
    type: null
    note: 24 LEDs behind an unmasked wheel with symbols, illuminating segments of the decorative wheel; custom light-separation wheels can be 3D printed/laser cut from provided STL/SVG files.
  display: 2.2" ILI9341 LCD, 240x320, with integrated SD card reader
  connectivity:
  - none
  battery: null
  sao_version: null
get_one:
  price: $75
  price_usd: 75
  quantity: '25'
  availability: sold_out
  distribution:
  - purchase
  where: Sold on Tindie by DC540 Nova; an initial batch of 25 was made, with team members keeping units and roughly 10 extras sold/given out at DEF CON 30. The Tindie listing was later marked unavailable while the seller paused sales.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/DC540-Nova/DC30-Tarot-Badge
  eda_tool: null
links:
- label: github.com/DC540-Nova/DC30-Tarot-Badge
  url: https://github.com/DC540-Nova/DC30-Tarot-Badge
  kind: repo
- label: DC540 Tarot Badge (for DC30) on Tindie
  url: https://www.tindie.com/products/dc540_nova/dc540-tarot-badge-for-dc30/
  kind: store
- label: 'The DC540 Tarot Badge: DC30 Debut'
  url: https://dc540.org/xxx/2022/08/the-dc540-tarot-badge-dc30-debut/
  kind: article
- label: Promotional video (YouTube)
  url: https://youtu.be/l6vM9SNLcsQ
  kind: video
images:
- file: assets/images/badges/dc30/tarot-badge-dc540/51d414daab.jpg
  source: "https://github.com/DC540-Nova/DC30-Tarot-Badge"
  credit: "DC540 Nova"
  caption: "The DC540 Tarot Badge, DEF CON 30 promotional photo"
- file: assets/images/badges/dc30/tarot-badge-dc540/95e4863400.png
  source: "https://www.tindie.com/products/dc540_nova/dc540-tarot-badge-for-dc30/"
  credit: "DC540 Nova"
  caption: "DC540 Tarot Badge listed on Tindie showing the illuminated wheel and LCD"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/DC540-Nova/DC30-Tarot-Badge
  title: DC30-Tarot-Badge (DC540)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 30''.'
- kind: url
  url: https://github.com/DC540-Nova/DC30-Tarot-Badge
  title: 'DC30-Tarot-Badge README'
  accessed: '2026-09-07'
  note: 'Confirmed event/year, Raspberry Pi Pico MCU, deck names, MIT license, and that the maker declined to publish Gerbers or raw firmware source.'
- kind: url
  url: https://www.tindie.com/products/dc540_nova/dc540-tarot-badge-for-dc30/
  title: DC540 Tarot Badge (for DC30) - Tindie listing
  accessed: '2026-09-07'
  note: 'Price ($75), 2.2" 240x320 ILI9341 display with SD reader, 24 LEDs, NRF transceiver, scavenger-hunt feature, and listing marked unavailable.'
- kind: url
  url: https://dc540.org/xxx/2022/08/the-dc540-tarot-badge-dc30-debut/
  title: 'The DC540 Tarot Badge: DC30 Debut'
  accessed: '2026-09-07'
  note: 'Production quantity (batch of 25, ~10 extra units at DEF CON 30), deck names, pairing/scavenger-hunt games, and MicroPython/dual-core/AES firmware details.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Battery/power source and firmware license terms for the hardware design (only the software is MIT-licensed; the maker explicitly declined to publish Gerbers or raw source) were not stated by any source. The Tindie listing mentions an NRF transceiver for wireless communication, but no source describes what it is used for (badge pairing may be done via NRF or another means); left connectivity as none since no confirmed protocol was named for it.'
last_modified_date: '2026-09-07'
---

The DC540 Tarot Badge was the DEF CON 30 (2022) electronic badge from DC540 Nova, a Northern Virginia-based DEF CON group. Built around a Raspberry Pi Pico, it pairs a 2.2" ILI9341 LCD with an SD card reader and a ring of 24 LEDs lighting up segments of a decorative wheel visible through the badge's face. The badge can display and "read" tarot cards from three preloaded decks — the classic Rider-Waite-Smith and Tarot de Marseille decks alongside a hand-drawn "Shitty Deck" — and includes a flashcard game for learning card meanings, a "pair" interaction between two badge wearers, and a scavenger-hunt challenge tied to imagery in the Rider-Waite deck that came with real prizes.

Only a small run was made: DC540 built about 25 units, and after the team's own members kept theirs and a few were lost during testing, roughly ten were available for other attendees at the con, sold through the group's Tindie storefront for $75. The Tindie listing was later marked unavailable as the seller (an all-volunteer, DC540-run nonprofit) paused sales.

DC540 published the badge's firmware (MicroPython, running on the Pico's dual cores, with AES encryption used for some game logic) and the deck art files under the MIT license on GitHub, along with instructions for loading custom tarot decks onto the SD card. The maker was explicit that the PCB design files ("Gerbers? Not on your life") and firmware source beyond the shipped .uf2 build were not being released, citing embarrassment over the routing rather than any secrecy concern.
