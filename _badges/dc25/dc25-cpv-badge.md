---
title: The 2017 Crypto and Privacy Village Badge
id: dc25-dc25-cpv-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: Crypto & Privacy Village (Karl Koscher / supersat, Whitney Merrill, Justin Culbertson)
  url: https://cryptovillage.org/
summary: 'The Crypto & Privacy Village''s DEF CON 25 badge: an ESP-WROOM-32 board running MicroPython with an EFM8UB1 USB co-processor, a 128x64 backlit LCD, a rotary encoder, capacitive touch pads, eight APA102 RGB LEDs, an ATECC508A crypto chip, an SD card slot and a headphone jack that streamed DEF CON radio, shipped in a matte black gilded box with earbuds.'
functions: 'Runs user-hackable MicroPython; drove a backlit LCD and 8 APA102 RGB LEDs via rotary encoder and capacitive touch pads; used the ATECC508A to locate/authenticate other badges wirelessly; had an SD card slot and a headphone jack that streamed DEF CON radio. Lanyards and the badge back carried ciphers, and the team cut ornate PCB "keys" as part of the puzzle.'
look:
  colors:
  - black
  - gold
  shape: rectangle
  themes:
  - crypto
  - privacy
  - security
  - puzzle
  - village badge
tech:
  mcu: ESP-WROOM-32 (ESP32) with an EFM8UB1 USB co-processor
  leds:
    count: 8
    type: APA102
    note: APA102-2020 package RGB LEDs
  display: 128x64 backlit LCD (ERC12864-1)
  connectivity:
  - wifi
  - bluetooth
  - ble
  - usb
  - audio
  battery: null
  sao_version: null
get_one:
  price: '$120 assembled; $50 for non-functional/unassembled boards after assembled stock sold out'
  price_usd: 120
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - village
  where: Sold in person at the Crypto & Privacy Village at DEF CON 25 (2017); checked via press coverage, 2026-09-07.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/cryptovillage/badge2017
  firmware_url: https://github.com/cryptovillage/badge2017
  eda_tool: null
links:
- label: github.com/cryptovillage/badge2017
  url: https://github.com/cryptovillage/badge2017
  kind: repo
  archived: https://web.archive.org/web/20260907112820/https://github.com/cryptovillage/badge2017
- label: hackaday.io/project/25893-the-2017-crypto-and-privacy-village-badge
  url: https://hackaday.io/project/25893-the-2017-crypto-and-privacy-village-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260907112942/https://hackaday.io/project/25893-the-2017-crypto-and-privacy-village-badge
- label: hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  kind: article
  archived: https://web.archive.org/web/20260306173057/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
images:
  - file: assets/images/badges/dc25/dc25-cpv-badge/21ee29599a.jpg
    source: "https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/"
    credit: "Hackaday"
    caption: "Front of the assembled 2017 Crypto and Privacy Village badge"
  - file: assets/images/badges/dc25/dc25-cpv-badge/7020d24e98.jpg
    source: "https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/"
    credit: "Hackaday"
    caption: "The badge's matte black gilded presentation box"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/cryptovillage/badge2017
  title: cryptovillage/badge2017 - The 2017 Crypto and Privacy Village Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260907112820/https://github.com/cryptovillage/badge2017
- kind: url
  url: https://hackaday.io/project/25893-the-2017-crypto-and-privacy-village-badge
  title: "The 2017 Crypto and Privacy Village Badge - Hackaday.io"
  accessed: '2026-09-07'
  note: Confirmed makers (Karl Koscher, Whitney Merrill, Justin Culbertson), chip list (ESP-WROOM-32, EFM8UB1, ATECC508A, ERC12864-1 LCD, 8x APA102-2020 LEDs), and a documented VBUS design flaw.
  archived: https://web.archive.org/web/20260907112942/https://hackaday.io/project/25893-the-2017-crypto-and-privacy-village-badge
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: "All The Hardware Badges Of DEF CON 25 - Hackaday"
  accessed: '2026-09-07'
  note: Source for price ($120 assembled, $50 unassembled after sellout), the gilded box/earbud presentation, rotary encoder/capacitive touch controls, and photos.
  archived: https://web.archive.org/web/20260306173057/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Exact production quantity not stated by any source found. Battery/power source not documented (badge may have been USB-powered only; not confirmed). Rumor mentioned by Hackaday that the badge could interact with "Bender on a Bender" units is unverified and not included as fact.
last_modified_date: '2026-09-07'
---

The Crypto & Privacy Village built its DEF CON 25 (2017) badge around an ESP-WROOM-32 module running MicroPython, paired with an EFM8UB1 8-bit USB co-processor, an ATECC508A crypto chip, a 128x64 backlit LCD, eight APA102 RGB LEDs, a rotary encoder, and capacitive touch pads. Karl Koscher (supersat), Whitney Merrill, and Justin Culbertson led the project. Badges shipped with an SD card slot and a headphone jack that streamed DEF CON radio, and could locate or authenticate other badges wirelessly using the onboard crypto chip.

Presentation was a big part of the badge's identity: it came in a matte black box with gilded lettering and a magnetic closure, packaged with a set of earbuds. Both the lanyard and the badge's back panel carried ciphers as part of a built-in puzzle, and the team cut ornate PCB "keys" to go with it. Badges sold in person at the village for $120 assembled; once that stock ran out, the team sold remaining unassembled boards for $50 to hackers willing to finish the build themselves.

The project's hardware and firmware were published on GitHub, including full schematics (Rev20170621). A known hardware issue was documented after release: the EFM8's VBUS pin could be damaged if USB was plugged in before the badge was powered on, since 5V appears on VBUS while VCC is still ramping to 3.3V; the team recommended powering on before charging, or cutting a trace as a permanent fix.

## Make your own

Hardware and firmware are both open source at [github.com/cryptovillage/badge2017](https://github.com/cryptovillage/badge2017), which includes firmware, hardware (schematics/PCB), and docs directories, plus the Rev20170621 schematic PDF.
