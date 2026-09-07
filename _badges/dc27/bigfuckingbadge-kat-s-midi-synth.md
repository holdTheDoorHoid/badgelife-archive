---
title: 'BigFuckingBadge: Kat''s MIDI Synth'
id: dc27-bigfuckingbadge-kat-s-midi-synth
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: hexum064
  url: https://hackaday.io/hexum064
  role: lead / hardware & firmware
- name: pinguino
  url: null
  role: team member
- name: Bunny1billion
  url: null
  role: team member
- name: Erin
  url: null
  role: team member
summary: An intentionally oversized DEF CON 27 conference badge built as a joke about going "really, really big" on a minimal budget and timeline, with a working MIDI synth and controller built in.
functions: Plays roughly 45 pre-loaded MIDI songs from an onboard flash chip and also works as a built-in MIDI controller, driven by capacitive-touch pad buttons. Several silly Easter eggs are hidden in the firmware.
look:
  colors: []
  shape: null
  themes:
  - music
  - meme
tech:
  mcu: ATtiny412
  leds:
    count: null
    type: APA201c
    note: RGB LEDs; exact count not stated by the maker.
  display: none
  connectivity:
  - audio
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hexum064/BFB-DC27-Board-and-Circuit
  firmware_url: https://github.com/Hexum064/ATTINY412_MIDI_BASIC
  eda_tool: null
links:
- label: hackaday.io/project/166765-bigfuckingbadge-kats-midi-synth
  url: https://hackaday.io/project/166765-bigfuckingbadge-kats-midi-synth
  kind: hackaday
- label: BFB-DC27-Board-and-Circuit (schematics/board files)
  url: https://github.com/Hexum064/BFB-DC27-Board-and-Circuit
  kind: repo
- label: ATTINY412_MIDI_BASIC (MIDI synth firmware)
  url: https://github.com/Hexum064/ATTINY412_MIDI_BASIC
  kind: repo
- label: attiny412_midi_controller_spi_flash (MIDI controller / flash interface firmware)
  url: https://github.com/Hexum064/attiny412_midi_controller_spi_flash
  kind: repo
- label: BigFuckingBadge.com
  url: http://www.BigFuckingBadge.com
  kind: website
images:
- file: assets/images/badges/dc27/bigfuckingbadge-kat-s-midi-synth/4eee53b2de.jpg
  source: "https://hackaday.io/project/166765-bigfuckingbadge-kats-midi-synth"
  credit: "hexum064"
  caption: "The BigFuckingBadge: Kat's MIDI Synth, an oversized DEF CON 27 badge"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/166765-bigfuckingbadge-kats-midi-synth
  title: 'BigFuckingBadge: Kat''s MIDI Synth'
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/166765-bigfuckingbadge-kats-midi-synth
  title: 'BigFuckingBadge: Kat''s MIDI Synth'
  accessed: '2026-09-07'
  note: Confirmed event (DEF CON 27, 2019), maker team, functions (MIDI player/controller, ~45 songs, capacitive touch, APA201c RGB LEDs), dual ATtiny412 MCUs, and linked GitHub repos for hardware and firmware.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Named after hexum064''s daughter Katerina. Maker describes the project as built with "no budget" for the event as a one-off; no price, quantity, or general public availability/distribution info found, so those fields are left empty. Exact LED count not stated. The project creator noted in an April 2025 discussion that the linked files "are all over the place," so the three GitHub repos above may not be fully organized.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/bigfuckingbadge-kat-s-midi-synth/
---

The BigFuckingBadge: Kat's MIDI Synth is an intentionally oversized conference badge built for DEF CON 27 (2019) by a four-person team — hexum064 (lead), pinguino, Bunny1billion, and Erin — as a joke about making something "really, really big" with no budget and little time. It's dedicated to hexum064's daughter, Katerina.

Under the huge form factor, the badge is a real working MIDI device: it plays around 45 pre-loaded songs stored on an onboard flash chip and doubles as a MIDI controller, played through capacitive-touch pad buttons. Two ATtiny412 microcontrollers do the work, and the badge lights up with APA201c RGB LEDs. The firmware hides a handful of silly Easter eggs in keeping with the project's tongue-in-cheek premise.

## Make your own

The hardware and firmware are open source, split across three of hexum064's GitHub repositories: [BFB-DC27-Board-and-Circuit](https://github.com/Hexum064/BFB-DC27-Board-and-Circuit) for the board and schematic, [ATTINY412_MIDI_BASIC](https://github.com/Hexum064/ATTINY412_MIDI_BASIC) for the MIDI synth code, and [attiny412_midi_controller_spi_flash](https://github.com/Hexum064/attiny412_midi_controller_spi_flash) for the MIDI controller and SPI flash interface. The maker has noted the files are spread across these repos rather than consolidated in one place.
