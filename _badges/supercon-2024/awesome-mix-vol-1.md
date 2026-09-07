---
title: Awesome Mix Vol. 1
id: supercon-2024-awesome-mix-vol-1
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Dustin Johnson
  url: https://hackaday.io/hacker/1532341-dustin-johnson
summary: A cassette-tape-shaped SAO with 14 WS2812B backlit LED spools that animate Play, Pause, Fast Forward and Rewind when triggered over I2C by the badge, built on an RP2040 as a demonstration of the maker's FUFF badge-to-SAO communication protocol for the Supercon 8 (2024) SAO Contest.
functions: Animates Play, Pause, Fast Forward and Rewind states on its LED "tape spools" in response to commands sent from the host badge over I2C using the maker's FUFF transport-layer protocol; the fast-forward/rewind animations include an indexing offset meant to imitate the asymmetric spinning of a real cassette's rotational indicator.
look:
  colors: []
  shape: card
  themes:
  - music
  - retro computer
tech:
  mcu: RP2040
  leds:
    count: 14
    type: WS2812B
    note: Two WS2812B RGB LED arrays arranged as the cassette's two tape spools.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://bitbucket.org/di0/fuff-over-i2c
  eda_tool: null
links:
- label: hackaday.io/project/198466-awesome-mix-vol-1
  url: https://hackaday.io/project/198466-awesome-mix-vol-1
  kind: hackaday
- label: bitbucket.org/di0/fuff-over-i2c
  url: https://bitbucket.org/di0/fuff-over-i2c
  kind: website
images:
  - file: assets/images/badges/supercon-2024/awesome-mix-vol-1/d3235eb558.jpg
    source: "https://hackaday.io/project/198466-awesome-mix-vol-1"
    credit: "Dustin Johnson"
    caption: "Awesome Mix Vol. 1 cassette-tape SAO"
  - file: assets/images/badges/supercon-2024/awesome-mix-vol-1/849d9ad1a2.png
    source: "https://hackaday.io/project/198466-awesome-mix-vol-1"
    credit: "Dustin Johnson"
    caption: "Awesome Mix Vol. 1 SAO detail"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198466-awesome-mix-vol-1
  title: Awesome Mix Vol. 1
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/198466-awesome-mix-vol-1
  title: Awesome Mix Vol. 1
  accessed: '2026-09-07'
  note: "Confirmed maker, event/year, RP2040 MCU, LED count/type and arrangement, I2C/FUFF communication, animation behavior, BOM (WS2812B arrays, 220 ohm resistor, 100uF capacitor), and firmware repo link; source of both saved images."
- kind: url
  url: https://bitbucket.org/di0/fuff-over-i2c
  title: di0 / FUFF-over-I2C — Bitbucket
  accessed: '2026-09-07'
  note: "Confirmed the firmware repository exists and is public (RP2040 I2C-slave examples in C++ and MicroPython); no separate hardware/Gerber files or license text found there."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Price, quantity made, and availability/distribution are not stated on the Hackaday.io project page or the linked firmware repo; left empty rather than guessed. No SAO header pin-count (v1/v1.69bis/v2) is specified by the maker, so tech.sao_version is left null. No hardware design files (schematic/PCB/Gerbers) were found, only the FUFF-over-I2C firmware repo, so make_your_own.open_source is 'partial'. Status set to 'released' since this was a working, demonstrated SAO for the Supercon 8 (2024) SAO Contest, not merely listed."
last_modified_date: '2026-09-07'
---

The Awesome Mix Vol. 1 is a cassette-tape-shaped SAO that Dustin Johnson built for the Supercon 8 (2024) SAO Contest. Its two WS2812B LED arrays, totaling 14 LEDs, sit behind the badge's tape-spool cutouts and light up to animate Play, Pause, Fast Forward, and Rewind, with the fast-forward and rewind modes offset slightly to mimic the uneven spin of a real cassette's rotational indicator. The board is built around an RP2040, ported from an earlier Arduino prototype.

Beyond being a cassette homage, the badge doubles as a demonstration piece for FUFF, Johnson's own transport-layer protocol for badge-to-SAO communication over I2C. FUFF is designed to let a host badge and an add-on talk without either side needing advance knowledge of the other's feature set, and the Awesome Mix Vol. 1's animations are driven entirely by FUFF commands sent from the host badge rather than run locally. The firmware, including RP2040 I2C-slave examples in both C++ and MicroPython, is published in Johnson's `fuff-over-i2c` repository on Bitbucket; no hardware design files (schematic, PCB layout, or Gerbers) for the SAO itself were found published alongside it.

No pricing, production quantity, or distribution details for the SAO were located on its Hackaday.io project page or in the firmware repository.

## Make your own

Firmware for the FUFF-over-I2C protocol, including RP2040 I2C-slave examples in C++ and MicroPython, is published at https://bitbucket.org/di0/fuff-over-i2c. No hardware files for the Awesome Mix Vol. 1 board itself have been located; anyone recreating the SAO from the firmware alone would need to design their own board around an RP2040 driving two WS2812B LED arrays (14 LEDs total) with a 220 ohm resistor and 100 uF capacitor per the BOM noted on the project page.
