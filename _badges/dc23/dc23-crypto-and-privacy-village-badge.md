---
title: DEF CON 23 Crypto and Privacy Village Badge
id: dc23-dc23-crypto-and-privacy-village-badge
layout: badge
parent: DC23
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc23
year: 2015
makers:
- name: Crypto and Privacy Village (Karl Koscher, Jorge Lacoste)
  url: https://github.com/cryptovillage
summary: 'The Crypto and Privacy Village''s DEF CON 23 (2015) village badge: an MSP430G2955 board with a 7-segment display, a ring of twelve PWM-dimmed LEDs, and two buttons, running Energia firmware with flag/easter-egg challenges hashed by ~3000 rounds of XXTEA, plus a party mode and a "Tetris mode" that broadcasts the Tetris theme over AM radio by modulating an LED as a side-channel demo.'
functions: Flag/easter-egg challenges validated by a custom hash built on ~3000 rounds of XXTEA; a "Tetris mode" that plays the Tetris theme over AM radio via electromagnetic interference from a blinking LED (a side-channel attack demo); and a party mode. Two buttons (left/right) provide input; a 7-segment display and a 12-LED ring provide output.
look:
  colors: []
  shape: null
  themes:
  - crypto
  - privacy
  - security
  - village badge
  - ctf
  - puzzle
tech:
  mcu: MSP430G2955
  leds:
    count: 12
    type: discrete
    note: PWM-dimmed ring of LEDs used for animations and the AM-radio "Tetris mode"; color not stated in sources.
  display: 7-segment
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/cryptovillage/badge2015/tree/master/hw
  firmware_url: https://github.com/cryptovillage/badge2015
  eda_tool: KiCad
links:
- label: github.com/cryptovillage/badge2015
  url: https://github.com/cryptovillage/badge2015
  kind: repo
  archived: https://web.archive.org/web/20260907111628/https://github.com/cryptovillage/badge2015
- label: raw.githubusercontent.com/cryptovillage/badge2015/master/README.md
  url: https://raw.githubusercontent.com/cryptovillage/badge2015/master/README.md
  kind: website
  archived: https://web.archive.org/web/20260907111701/https://raw.githubusercontent.com/cryptovillage/badge2015/master/README.md
- label: raw.githubusercontent.com/cryptovillage/badge2015/master/docs/DC23CPV%20Badge%20No%20Flags.pdf
  url: https://raw.githubusercontent.com/cryptovillage/badge2015/master/docs/DC23CPV%20Badge%20No%20Flags.pdf
  kind: website
  archived: https://web.archive.org/web/20260907111717/https://raw.githubusercontent.com/cryptovillage/badge2015/master/docs/DC23CPV%20Badge%20No%20Flags.pdf
- label: raw.githubusercontent.com/cryptovillage/badge2015/master/hw/schematic.pdf
  url: https://raw.githubusercontent.com/cryptovillage/badge2015/master/hw/schematic.pdf
  kind: website
  archived: https://web.archive.org/web/20260907111824/https://raw.githubusercontent.com/cryptovillage/badge2015/master/hw/schematic.pdf
images: []
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/cryptovillage/badge2015
  title: 'GitHub - cryptovillage/badge2015: Hardware, firmware, and documentation for the 2015 Crypto and Privacy Village Badge'
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260907111628/https://github.com/cryptovillage/badge2015
- kind: url
  url: https://raw.githubusercontent.com/cryptovillage/badge2015/master/README.md
  title: badge2015 README
  accessed: '2026-09-07'
  note: Confirmed MCU (MSP430G2955), XXTEA-hashed flag/easter-egg challenges, Tetris-mode AM-radio side channel, dropped compass footprint, and Energia toolchain.
- kind: url
  url: https://raw.githubusercontent.com/cryptovillage/badge2015/master/hw
  title: badge2015 hw directory listing
  accessed: '2026-09-07'
  note: Confirms hardware is KiCad (schematic, PCB, netlist, library files all .sch/.kicad_pcb/.net format).
- kind: url
  url: https://raw.githubusercontent.com/cryptovillage/badge2015/master/firmware/cpvfinal/cpvfinal.ino
  title: badge2015 firmware source (cpvfinal.ino)
  accessed: '2026-09-07'
  note: Confirms a 7-segment display buffer, a 12-element "ring of LEDs" buffer with PWM brightness control, two buttons (left/right), and party-mode/self-test code paths. No LED color or button labeling given in source.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The GitHub repo, README, and firmware source confirm the MCU, the 7-segment display, a 12-LED PWM-dimmed ring, two buttons, XXTEA-based challenge hashing, the Tetris/AM-radio side-channel mode, party mode, and that hardware+firmware are both published (KiCad + Energia). No source found gives LED color, battery, price, quantity made, or distribution details beyond "village badge." No "Baudot mode" was found anywhere in the fetched README or firmware source despite appearing in the pre-research stub summary, so that claim was dropped rather than repeated unverified. The linked "DC23CPV Badge No Flags.pdf" is a binary document automated fetch could not decode; a manual open of that PDF or the schematic.pdf may fill in battery/price/quantity specifics. No photo of the physical badge was found (GitHub only offers its generic social-card image, not a picture of the item). Author names (Karl Koscher, Jorge Lacoste) carried over from the pre-existing entry are not independently confirmed
    by the sources checked here.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc23/dc23-crypto-and-privacy-village-badge.glb
  method: kicad
  source_file: hw/badge2015.kicad_pcb
  generated: '2026-09-07'
  bytes: 259432
---

The Crypto and Privacy Village ran its own village badge for DEF CON 23 in 2015, built around a Texas Instruments MSP430G2955 and coded in Energia (the Arduino-style toolchain for MSP430). The badge's headline feature is a set of flag and easter-egg challenges whose answers are checked with a custom hash built on roughly 3000 rounds of the XXTEA cipher, giving attendees a cryptographic puzzle to work through over the weekend rather than a simple lookup table.

Physically, the badge combines a 7-segment display with a ring of twelve PWM-dimmed LEDs and two buttons (left/right) for input. Beyond the core flag challenges, the firmware hides a party mode and a "Tetris mode" that turns the badge into a crude AM radio transmitter, playing the Tetris theme by exploiting electromagnetic interference from a blinking LED — a hands-on demonstration of a side-channel/emissions attack. The board also carries an unpopulated footprint for a digital compass chip that was dropped late in development and never populated.

Both the hardware (KiCad schematic, PCB, and netlist files) and firmware are published on GitHub under cryptovillage/badge2015, along with a "no flags" version of the challenge documentation for anyone who wants to study the puzzle design without the answers. Specifics like LED color, battery, price, and production quantity are not stated anywhere in the repository's text content that could be retrieved automatically; the linked schematic and challenge PDF likely hold those details but could not be parsed by automated fetch.
