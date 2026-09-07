---
title: Galaxia Wizard Badge
id: dc26-dc26-galaxia-wizard-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: awkward intelligence
  url: https://hackaday.io/Awkwardai
summary: Wizard-and-stars 'Harbinger Sound/Circuits Lab' prototyping board with a dragon-crown top edge, given away free with the maker's DEF CON 26 shitty-add-on sets as an open-ended build-your-own-badge platform.
functions: 'A bare prototyping platform, not a fixed function. The maker built and demonstrated three different circuits on it: an Atari Punk Console synth (two 555 timers, potentiometers, resistors, capacitors, 9V battery), a shitty-add-on holder (coin-cell holder soldered to the exposed star pads, powering rail sets X/Y/Z), and a NodeMCU-based honeypot driving an SSD1306 OLED over rails A-D.'
look:
  colors:
  - black
  - gold
  - silver
  shape: null
  themes:
  - fantasy
  - space
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given away as a freebie with purchases from the maker's DEF CON 26 shitty-add-on sets; not sold individually.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  gerbers_url: https://cdn.hackaday.io/files/1599526843386368/galaxiafinal.zip
  eda_tool: null
links:
- label: hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  kind: hackaday
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- label: hackaday.io/project/159952/files
  url: https://hackaday.io/project/159952/files
  kind: hackaday
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
images:
- file: assets/images/badges/dc26/dc26-galaxia-wizard-badge/6d9737f716.jpg
  source: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  credit: awkward intelligence
  caption: Assembled Galaxia Wizard Badge prototyped as an Atari Punk Console synth, with breadboard-style headers, potentiometers, buttons and a speaker
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- file: assets/images/badges/dc26/dc26-galaxia-wizard-badge/fdf6fa9b0d.jpg
  source: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  credit: awkward intelligence
  caption: Bare Galaxia Wizard Badge PCB showing the dragon-crown top edge, stars and moon silkscreen, chip footprints, potentiometer slots and connector rails
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  title: The Harbinger Shitty Add-on Badges
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  title: The Harbinger Shitty Add-on Badges
  accessed: '2026-09-07'
  note: Maker's own project description and later annotated-guide log post; confirmed maker, event/year, free-with-purchase distribution, that it was an unfinished/open-ended prototyping board (not fully populated as issued), and the three demo circuits built on it.
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- kind: url
  url: https://hackaday.io/project/159952/files
  title: Files - The Harbinger Shitty Add-on Badges
  accessed: '2026-09-07'
  note: Confirmed exact filenames for the two annotated-trace PDFs and the gerber zip, and their sizes/dates.
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'No MCU, LED, or display specs are given as fixed features of the badge itself: it is a bare prototyping platform, and the components used depended on which of the three demo circuits a builder chose (a NodeMCU + SSD1306 in one case, plain SMD LEDs in another). tech fields are left empty rather than guessed. No dedicated schematic file was found on the project page, only the gerbers and the two annotated PDFs; make_your_own.open_source is "partial" since gerbers exist but no schematic/BOM was located. No quantity-made figure is stated anywhere.'
last_modified_date: '2026-09-07'
---

The Galaxia Wizard Badge is a bare prototyping board that awkward intelligence gave away with their DEF CON 26 (2018) shitty-add-on sets, part of "The Harbinger Sound/Circuits Lab." Rather than a finished gadget, it's a wizard-and-stars themed PCB with a dragon-crown top edge, packed with component footprints, potentiometer slots, breadboard-style header rails, a NodeMCU slot, and exposed copper pads meant to work as stylus-style touch inputs. It began life as an idea for a 555-timer synthesizer, but the maker left the final version open-ended as a build-your-own-badge (BYOB) platform for people with ideas but not the budget or skill to design their own board from scratch.

Because it shipped as a kit of possibilities rather than a populated badge, many recipients weren't sure what to do with it, and some assumed parts were missing. The maker eventually posted an annotated guide (two PDFs covering the rail/potentiometer side and the chip-footprint side) explaining the pad layout and noting that five connections on the board were left unrouted. To show what it could become, the maker built three different circuits on the same board: an Atari Punk Console synth using two 555 timers on a 9V battery, a shitty-add-on holder powered by a coin cell soldered to the exposed pads, and a NodeMCU-driven honeypot running an SSD1306 OLED. The badge was never sold individually; it was a bonus for buying the maker's other shitty add-ons at DC26.

## Make your own

Final gerbers for the board are published (`galaxiafinal.zip`), along with the two annotated-trace PDFs (`WiardconxRails.pdf`, `Wizardconx1.pdf`) that walk through the rail/potentiometer section and the chip-footprint/pad section separately. No schematic or bill of materials was found alongside them, so populating the board means working from the gerbers and the annotated pad notes, choosing one of the three demonstrated circuits (or your own) to build.
