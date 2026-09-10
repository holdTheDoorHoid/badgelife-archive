---
title: Disobey 2017 Badge
id: disobey-2017-disobey-2017-badge
layout: badge
parent: Disobey 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: disobey-2017
year: 2017
makers:
- name: Disobey
summary: The official electronic badge for Disobey 2017, an ATmega328P board with seven discrete red LEDs run as a Larson-scanner sweep, a coin-cell battery, and a hidden Morse-code "challenge code" cycled into the light pattern.
functions: Runs a continuous Larson-scanner (Knight Rider style) LED sweep across six LEDs; periodically blinks out a Morse code message on a seventh LED, apparently including a hidden challenge/code as part of the event's badge challenge.
look:
  colors:
  - red
  shape: null
  themes:
  - security
  - ctf
tech:
  mcu: ATmega328P
  leds:
    count: 7
    type: discrete
    note: Seven discrete red LEDs (D1-D7); six driven in a Larson-scanner pattern, one used for the Morse output.
  display: none
  connectivity: []
  battery: CR1225 coin cell (BR1225 holder)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/disobeyfi/badge-2017/tree/master/hw
  firmware_url: https://github.com/disobeyfi/badge-2017/blob/master/morse.c
  eda_tool: null
  gerbers_url: https://github.com/disobeyfi/badge-2017/tree/master/hw/Gerber_v7
  bom_url: https://github.com/disobeyfi/badge-2017/blob/master/hw/BOM_v7.csv
  notes: Repo also ships flasher.sh, an avrdude/usbasp fuse-and-flash script targeting the ATmega328P.
links:
- label: github.com/disobeyfi/badge-2017
  url: https://github.com/disobeyfi/badge-2017
  kind: repo
images: []
contact: {}
notes:
- Hardware design and source files for the Disobey 2017 conference badge, published in the disobeyfi GitHub org. Found by the event-year sweep, task con-disobey.
- Sweep title matched the maker's own title; no change needed.
status: released
sources:
- kind: url
  url: https://github.com/disobeyfi/badge-2017
  title: Disobey 2017 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-disobey); event read as ''Disobey 2017''.'
- kind: url
  url: https://raw.githubusercontent.com/disobeyfi/badge-2017/master/README.md
  title: disobeyfi/badge-2017 README
  accessed: '2026-09-08'
  note: Confirms it is the hardware design + source for the Disobey 2017 badge; README is otherwise minimal.
- kind: url
  url: https://raw.githubusercontent.com/disobeyfi/badge-2017/master/morse.c
  title: morse.c firmware source
  accessed: '2026-09-08'
  note: 'Firmware for the ATmega328P: drives a 6-LED Larson-scanner sweep plus a Morse-coded message on a 7th LED; a code comment (in Finnish) says a "challenge code" is shown periodically.'
- kind: url
  url: https://raw.githubusercontent.com/disobeyfi/badge-2017/master/hw/BOM_v7.csv
  title: BOM_v7.csv
  accessed: '2026-09-08'
  note: Confirms ATMEGA328P-AU MCU, 7x discrete red LEDs (D1-D7), a BR1225 coin-cell holder (CR1225), and unpopulated 2x6/1x6 headers and crystal.
- kind: url
  url: https://raw.githubusercontent.com/disobeyfi/badge-2017/master/flasher.sh
  title: flasher.sh
  accessed: '2026-09-08'
  note: avrdude/usbasp script setting ATmega328P fuses and flashing morse.hex; confirms firmware toolchain.
- kind: url
  url: https://disobey.fi/2017/
  title: Disobey 2017 event page (current, redirected from 2017.disobey.fi)
  accessed: '2026-09-08'
  note: No mention of the 2017 badge specifically (page now shows current-year content); could not confirm price, quantity, or distribution for the 2017 badge.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed as a real, released badge via the maker's own GitHub org (disobeyfi), including schematic/layout PDFs, Gerbers, BOM, and firmware source. Could not find price, quantity made, or distribution details for the 2017 badge specifically; disobey.fi's 2017 event page now redirects to current-year content with no 2017 badge pricing. No photo of the assembled badge was found (GitHub's og:image is just a generic repo social card, not a picture of the board), so images remain empty. A parallel mirror exists at github.com/tomikoski/disobey-badge-2017 (same content, personal fork) and was not used as a source.
last_modified_date: '2026-09-10'
model:
  file: assets/models/disobey-2017/disobey-2017-badge.glb
  method: gerber
  source_file: hw/Gerber_v7
  generated: '2026-09-10'
  bytes: 140756
  size_mm:
  - 75.0
  - 75.0
---

The Disobey 2017 badge is the official electronic badge for Finland's Disobey hacker conference, built around an ATmega328P microcontroller and published as open hardware by the Disobey team on GitHub. The board carries seven discrete red LEDs: six are driven in a classic Larson-scanner ("Knight Rider") sweep, while a seventh LED periodically blinks out a message in Morse code. A comment in the firmware source (in Finnish) notes that a "challenge code" is displayed on roughly every twelfth cycle, suggesting the LED pattern fed into one of the event's badge challenges or puzzles.

The badge is powered by a CR1225 coin cell and includes unpopulated headers and an unpopulated crystal footprint on the board, indicating a stripped-down bill of materials for the shipped units (running on the ATmega328P's internal oscillator rather than an external crystal). The repository publishes the full open-source hardware package — schematic and board-layout PDFs, Gerbers, and a BOM — along with the Arduino-style firmware (`morse.c`) and a shell script (`flasher.sh`) that sets AVR fuses and flashes the firmware over USBasp via avrdude.

No pricing, production quantity, or distribution details for the 2017 badge specifically could be confirmed; Disobey's own event page for 2017 now redirects to current-year content. No photo of the assembled badge was located during this research pass.
