---
title: Supercon 2022 Badge Card Reader
id: supercon-2022-supercon-2022-badge-card-reader
layout: badge
parent: Supercon 2022
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2022
year: 2022
makers:
- name: Zach Fredin
  url: https://hackaday.io/zakqwy
- name: Ben Hencke
  url: https://hackaday.io/ben-hencke
summary: 'A hand-built optical card reader that loads Sharpie-marked paper "programs" onto the Supercon 2022 badge over UART.'
functions: 'Reads hand-marked paper cards optically and transfers the encoded program to the Supercon 2022 badge over UART. Users draw sync bars and data marks on printed cards with a Sharpie and feed the card through the reader by hand.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: null
  leds:
    count: 26
    type: discrete
    note: 'Two arrays of thirteen salvaged red LEDs (harvested from donor badges), charlieplexed and scanned sequentially to illuminate the card as it passes through.'
  display: none
  connectivity:
  - uart
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '1 (one-off build)'
  availability: not_released
  distribution: []
  where: 'Not distributed; a single unit built and demoed at Supercon 2022.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/188133-supercon-2022-badge-card-reader
  url: https://hackaday.io/project/188133-supercon-2022-badge-card-reader
  kind: hackaday
images:
  - file: assets/images/badges/supercon-2022/supercon-2022-badge-card-reader/ced079b68d.jpg
    source: "https://hackaday.io/project/188133-supercon-2022-badge-card-reader"
    credit: "Zach Fredin / Ben Hencke"
    caption: "Supercon 2022 Badge Card Reader with a marked program card"
  - file: assets/images/badges/supercon-2022/supercon-2022-badge-card-reader/2578e35e7d.jpg
    source: "https://hackaday.io/project/188133-supercon-2022-badge-card-reader"
    credit: "Zach Fredin / Ben Hencke"
    caption: "Card reader attached to the Supercon 2022 badge"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/188133-supercon-2022-badge-card-reader
  title: Supercon 2022 Badge Card Reader
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''Supercon 2022''.'
- kind: url
  url: https://hackaday.io/project/188133-supercon-2022-badge-card-reader
  title: Supercon 2022 Badge Card Reader (Hackaday.io project log)
  accessed: '2026-09-07'
  note: 'Primary source for makers, function, construction, LEDs, and open-source status; identified project page as the definitive source.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'MCU is not a general-purpose microcontroller in the usual sense: the project uses a Pixelblaze Sensor Expansion Board (with a 12-bit, 1 Msps ADC and a transimpedance amplifier) to manage the LEDs and read the card, so tech.mcu is left null rather than guessed. Built point-to-point with 34 AWG magnet wire and cardboard shims rather than on a PCB. Schematics were captured after the fact by a community member and shared as a KiCad file via Google Drive, not published by the makers themselves, so open_source is marked partial with no direct hardware_url. No price/quantity/commercial availability info exists since this was a one-off demo build, not a sold or distributed item. No additional web search was possible (session search budget exhausted); relied on the Hackaday.io project page, which is the maker-authored primary source.'
last_modified_date: '2026-09-07'
---

The Supercon 2022 Badge Card Reader is a one-off accessory built by Zach Fredin (zakqwy) and Ben Hencke (ben-hencke) that lets a Supercon 2022 badge take its programs from paper instead of a computer. A user draws sync bars and data marks on a printed card with a Sharpie, then feeds the card by hand through the reader. Inside, two arrays of thirteen salvaged red LEDs — recovered from donor badges — are charlieplexed and scanned sequentially to illuminate the card, while a Pixelblaze Sensor Expansion Board (with a 12-bit, 1 Msps ADC and a transimpedance amplifier with 1E6 gain) reads the resulting light pattern and decodes it into 32 12-bit words, matching the badge's button count and spacing. The decoded program is sent to the badge over UART, and a single harvested badge button provides the reader's own input.

The whole thing is built point-to-point with 34 AWG polyurethane magnet wire rather than on a custom PCB, with cardboard shims used to hold the LED arrays at the correct gap across the card path — a scrappy, demo-table build rather than a manufactured product. It was never sold or distributed; it existed as a single working prototype shown off at Supercon 2022. The makers did not publish formal hardware or firmware files themselves, but a community member captured the schematic afterward and shared it as a KiCad file over Google Drive, so the design is only partially open.
