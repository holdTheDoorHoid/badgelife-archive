---
title: stm8_minibadges
id: other-stm8-minibadges
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: other
year: 0
makers:
- name: Professor-plum
summary: A collection of five DIY minibadges (Metroid, Pitfall, Doom, Phoenix, VoodooDoll) built around the low-cost STM8S001J3 microcontroller. Metroid, Pitfall, and Doom drive a small TFT LCD with looping retro-game sprite animations; Phoenix and VoodooDoll use a single LED instead.
functions: Metroid, Pitfall, and Doom play looping sprite animations on a TFT LCD themed to their namesake game or character; Phoenix pulses a touch-sensitive LED "eye" that blinks rapidly when touched and was tied to a CTF at the 2019 SAINTCON badge (per the maker, the touch-triggered link display only worked about 1 in 100 touches); VoodooDoll drives a single red/green LED.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - arcade
  - pop culture
  - ctf
tech:
  mcu: STM8S001J3
  leds: null
  display: TFT LCD (ST7735 driver) on Metroid, Pitfall, and Doom; Phoenix and VoodooDoll use a single LED instead
  connectivity: []
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
  open_source: partial
  hardware_url: https://github.com/Professor-plum/stm8_minibadges
  firmware_url: https://github.com/Professor-plum/stm8_minibadges
  eda_tool: Eagle
  license: MIT
  notes: Bare-metal C firmware (no libraries) built with SDCC and flashed via ST-Link V2 and stm8flash (2x, 3V3/GND/SWIM only); Eagle CAD PCB files (.sch/.brd/.pdf) are included for Doom, Metroid, Phoenix, and Pitfall, but not for VoodooDoll — its own README says the maker "can't seem to locate the Eagle files" for it, so only its firmware is published.
links:
- label: github.com/Professor-plum/stm8_minibadges
  url: https://github.com/Professor-plum/stm8_minibadges
  kind: repo
images:
- file: assets/images/badges/other/stm8-minibadges/b592028b49.jpg
  source: https://github.com/Professor-plum/stm8_minibadges
  credit: Professor-plum
  caption: Assembled STM8 minibadge PCB showing TFT LCD and STM8S001J3 layout
- file: assets/images/badges/other/stm8-minibadges/b6aa2d09ab.gif
  source: https://github.com/Professor-plum/stm8_minibadges
  credit: Professor-plum
  caption: Metroid-themed minibadge TFT display animation
contact: {}
notes:
- collection of STM8S001J3-based minibadges
status: listed
sources:
- kind: url
  url: https://github.com/Professor-plum/stm8_minibadges
  title: stm8_minibadges
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/Professor-plum/stm8_minibadges
  title: 'Professor-plum/stm8_minibadges: Repository of mini badges using the stm8s001j3'
  accessed: '2026-09-07'
  note: 'README and repo tree: chip choice/cost, assembly and flashing instructions, MIT license, five badge designs (Metroid, Pitfall, Doom, Phoenix, VoodooDoll), Eagle CAD files, no event or price info given.'
- kind: url
  url: https://github.com/Professor-plum/stm8_minibadges/blob/master/Phoenix/README.md
  title: stm8_minibadges/Phoenix/README.md at master
  accessed: '2026-09-07'
  note: 'Fact-check pass: Phoenix uses a red LED, not a TFT LCD; is touch-sensitive; and "had a CTF associated with it" tied to "the 2019 SAINTCON badge" where a touched URL displayed on the main badge (worked ~1/100 touches). Contradicts prior summary/functions claiming all five badges use a TFT LCD with no interactivity.'
- kind: url
  url: https://github.com/Professor-plum/stm8_minibadges/blob/master/VoodooDoll/README.md
  title: stm8_minibadges/VoodooDoll/README.md at master
  accessed: '2026-09-07'
  note: 'Fact-check pass: VoodooDoll ("Voodoo Doll SOA") uses a red/green LED, not a TFT LCD; maker states he "can''t seem to locate the Eagle files" for this one, so no hardware/PCB files are published for it (firmware only). Contradicts prior make_your_own.notes claiming Eagle files exist for all five, and prior eda_tool value of "EasyEDA" (repo tree shows .sch/.brd/.pdf, i.e. Eagle CAD, matching the body text but not the front-matter field as originally written).'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07) found the prior draft overgeneralized from the Metroid/Doom/Pitfall designs to all five: only those three use a TFT LCD; Phoenix and VoodooDoll each use a single LED instead, and Phoenix is touch-interactive. Corrected summary, functions, tech.display, and look.themes (added "ctf") accordingly. Also corrected make_your_own.eda_tool from "EasyEDA" to "Eagle" (repo file tree has .sch/.brd/.pdf, Eagle''s formats — this matches the body text, which already said Eagle, but not the field as first written) and open_source from "yes" to "partial", since VoodooDoll''s own README says the maker could not locate its Eagle files, so only its firmware is published. Event is left as "other"/year 0 for the collection as a whole, but Phoenix''s own README explicitly ties it to "the 2019 SAINTCON badge" and a CTF — that badge alone likely deserves its own entry under a saintcon-2019 event (not currently in events.yml), flagged in this run''s report rather than created
    here. No event/date/price/quantity/distribution info exists for Doom, Metroid, Pitfall, or VoodooDoll specifically, so those fields stay empty. tech.leds is left empty because the field is a single count/type for the whole collection and LED presence/count varies by design (Doom/Metroid/Pitfall: none; Phoenix: 1; VoodooDoll: 1) — recording it accurately would require splitting the entry, which is out of scope for this pass. Both saved images were confirmed to match files actually in the repo (layout.JPG and Metroid/metroid.gif, the latter byte-identical to the saved copy).'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/stm8-minibadges.glb
  method: kicad
  source_file: saint lcd.brd
  generated: '2026-09-10'
  bytes: 34240
---

The stm8_minibadges repo is a personal project by GitHub user Professor-plum collecting five small DIY badge designs — Metroid, Pitfall, Doom, Phoenix, and VoodooDoll — all built around the STM8S001J3, a microcontroller the maker favors for being cheaper than an ATtiny (about $0.23 each) despite an awkward pinout. Three of the five (Metroid, Pitfall, Doom) pair the STM8 with a TFT LCD (driven with ST7735 commands) that plays a looping sprite animation themed to the badge's namesake game. The other two use a single LED instead: VoodooDoll drives a red/green LED, and Phoenix drives a red LED "eye" that pulses normally and blinks rapidly when its touch sensor is triggered — the maker's own notes say Phoenix "had a CTF associated with it" and tie it specifically to "the 2019 SAINTCON badge," where touching it was meant to display a URL on the main conference badge, though the maker notes this only worked on roughly 1 in 100 touches.

The firmware for every badge is written in bare-metal C with no libraries, compiled with SDCC, and flashed over SWIM using an ST-Link V2 and stm8flash — done twice per flash, per the maker's notes, since the first attempt "rarely takes." Assembly of the LCD-based designs is hand-soldered: LCD first, then the STM8 chip (oriented carefully), then a resistor and capacitor, then the pin header legs.

Aside from Phoenix's tie to the 2019 SAINTCON badge, there is no indication in the repository of a convention, year, price, or production run for the other four designs — they read as an ongoing personal design exercise rather than badges sold or distributed at an event. Source code for all five designs is published under the MIT license; Eagle CAD PCB layouts are included for Doom, Metroid, Phoenix, and Pitfall, but the maker notes he could not locate VoodooDoll's Eagle files, so that one is firmware-only.
