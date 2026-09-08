---
title: ToorCamp 2022 Spider Badge
id: toorcamp-2022-toorcamp-2022-spider-badge
layout: badge
parent: ToorCamp 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: toorcamp-2022
year: 2022
makers:
- name: Rich Gonzales / OlyMEGA
summary: 'The official ToorCamp 2022 soldering badge: an analog spider whose four LED eyes light up in the dark, sensed by a photocell and tuned with a potentiometer.'
functions: 'Light-sensing spider eyes (four LEDs) that turn on as ambient light drops, with a potentiometer to adjust the darkness threshold the circuit triggers at. No microcontroller; a slide switch and battery holder round out the build, and the design leaves room for an optional buzzer or tripwire mod.'
look:
  colors: []
  shape: spider
  themes:
  - animal
  - learn to solder
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: Four LEDs form the spider's eyes, driven by a MOSFET switched by a photocell/potentiometer light-sensing circuit.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Distributed at ToorCamp 2022 as the event''s badge-making-village soldering kit.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/events/toorcamp-2022
  url: https://badge.gallery/events/toorcamp-2022
  kind: website
- label: 'ToorCamp Badge assembly guide (PDF)'
  url: https://talks.toorcon.net/media/toorcamp-2020-2019/submissions/KBNKJM/resources/Toorcamp_2022_Badge_assembly_oAFoqzE.pdf
  kind: doc
- label: 'Rich Gonzales talk: designing the ToorCamp badge'
  url: https://talks.toorcon.net/toorcamp-2020-2019/talk/KBNKJM/
  kind: video
images:
- file: assets/images/badges/toorcamp-2022/toorcamp-2022-spider-badge/9db4c5acf2.jpg
  source: "https://talks.toorcon.net/toorcamp-2020-2019/talk/KBNKJM/"
  credit: "Rich Gonzales / OlyMEGA"
  caption: "Prototype of the ToorCamp 2022 spider badge"
contact: {}
notes:
- Official ToorCamp 2022 soldering badge with four LEDs forming light-sensing spider eyes, a photocell, potentiometer and optional alarm mod. Found by the event-year sweep, task con-toorcon.
status: released
sources:
- kind: url
  url: https://badge.gallery/events/toorcamp-2022
  title: ToorCamp 2022 Spider Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-toorcon); event read as ''ToorCamp 2022''.'
- kind: url
  url: https://talks.toorcon.net/toorcamp-2020-2019/talk/KBNKJM/
  title: "Rich Gonzales, ToorCamp badge design talk"
  accessed: '2026-09-08'
  note: 'Confirms Rich Gonzales/OlyMEGA designed the ToorCamp 2022 badge; links the assembly guide PDF and a prototype photo. No price, quantity, or open-source status given.'
- kind: url
  url: https://talks.toorcon.net/media/toorcamp-2020-2019/submissions/KBNKJM/resources/Toorcamp_2022_Badge_assembly_oAFoqzE.pdf
  title: "ToorCamp 2022 Badge assembly guide (PDF)"
  accessed: '2026-09-08'
  note: 'Official assembly guide for the badge; confirms component list (LEDs, photocell, potentiometer, MOSFET, slide switch, battery holder). Could not extract further text (binary PDF).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, official ToorCamp 2022 badge-village soldering kit designed by Rich Gonzales (OlyMEGA), corroborated by badge.gallery and the maker''s own ToorCon talk page plus an official assembly guide PDF. Could not find price, quantity made, whether it is open source, or design/gerber files; no storefront located (likely distributed for free/at-cost in the badge village rather than sold). The assembly-guide PDF text could not be parsed for additional detail beyond the component list already known from badge.gallery.'
last_modified_date: '2026-09-08'
---

The ToorCamp 2022 Spider Badge is the official soldering-village badge for ToorCamp 2022, designed by Rich Gonzales of OlyMEGA. It's a purely analog build with no microcontroller: four LEDs form a spider's glowing eyes, lit by a MOSFET-driven circuit that reacts to a photocell, with a potentiometer letting the builder tune how dark it needs to get before the eyes switch on. A slide switch and battery holder round out the kit, and the design leaves headroom for an optional buzzer or tripwire modification for anyone who wants to extend it.

Gonzales gave a talk at ToorCamp on the badge's design process, covering budgeting, timeline, and the path from concept art to finished board; that talk page links an official assembly quick-start guide PDF and a photo of the badge prototype. Neither that page nor badge.gallery lists a price, production quantity, or whether the hardware/firmware (there being no firmware) design files were released, so those fields are left blank rather than guessed.
