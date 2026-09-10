---
title: Pumpkin Witch
id: other-pumpkin-witch
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2019
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/twinkletwinkie
summary: A Halloween mini badge shaped like a pumpkin wearing a witch hat, with seven reverse-mount LEDs, a slide switch and a CR2032 coin cell on a black-soldermask, white-silkscreen, OSP-copper PCB that TwinkleTwinkie used to test a matte coating against copper tarnish.
functions: Lights up the pumpkin/witch-hat artwork via seven reverse-mount LEDs; power is toggled with an onboard slide switch.
look:
  colors:
  - black
  - white
  - copper
  shape: pumpkin
  themes:
  - halloween
  - horror
tech:
  mcu: none
  leds:
    count: 7
    type: reverse-mount
    note: 1206 reverse-mount LEDs (or OSRAM/SunLED reverse-gullwing alternatives), one series resistor
  display: null
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/165319-pumpkin-witch
  firmware_url: null
  gerbers_url: https://hackaday.io/project/165319-pumpkin-witch
  eda_tool: null
links:
- label: hackaday.io/project/165319-pumpkin-witch
  url: https://hackaday.io/project/165319-pumpkin-witch
  kind: hackaday
images:
- file: assets/images/badges/other/pumpkin-witch/3ba6c240df.jpg
  source: https://hackaday.io/project/165319-pumpkin-witch
  credit: TwinkleTwinkie
  caption: Pumpkin Witch badge, front
- file: assets/images/badges/other/pumpkin-witch/3d25b3c3e2.jpg
  source: https://hackaday.io/project/165319-pumpkin-witch
  credit: TwinkleTwinkie
  caption: Pumpkin Witch badge, lit LEDs
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/165319-pumpkin-witch
  title: Pumpkin Witch
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/165319-pumpkin-witch
  title: Pumpkin Witch
  accessed: '2026-09-07'
  note: Read for maker, build details (LEDs, switch, battery, PCB finish), publication date, gerber availability, and gallery photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No specific convention tied to this badge; it reads as a standalone Halloween project posted by TwinkleTwinkie on Hackaday.io on 2019-05-01 (event kept as "other"). Web search snippets suggested a Tindie listing with a lanyard, "2 batteries," and a $5-to-STEM-charity donation, but the Tindie store page is Cloudflare-protected and could not be fetched to confirm those details belong to this specific badge rather than another TwinkleTwinkie product, so price/quantity/availability/distribution are left empty rather than guessed. Gerbers (PumpkinWitch_Gerbers_Public.zip) are linked from the project page, so open_source is marked partial (hardware only; no firmware, since the board has no MCU).
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/pumpkin-witch.glb
  method: gerber
  source_file: PumpkinWitch_Gerbers_Public.zip
  generated: '2026-09-10'
  bytes: 156212
  size_mm:
  - 65.0
  - 61.8
---

Pumpkin Witch is a Halloween-themed mini badge by TwinkleTwinkie (Bradán Lane / Twinkie), posted to Hackaday.io on May 1, 2019. The board is shaped like a jack-o'-lantern wearing a witch's hat and lights up using seven reverse-mount 1206 LEDs (with OSRAM or SunLED reverse-gullwing parts noted as alternatives), a single series resistor, and an MSS22D18 SMD slide switch, powered by a CR2032 coin cell in an onboard holder. There is no microcontroller on the board; it is a simple always-on/off LED badge rather than an animated one.

The project doubled as a materials test: TwinkleTwinkie used it to try an OSP (organic solderability preservative) copper finish under black solder mask and white silkscreen, and recommends a coat or two of matte spray paint after assembly to keep the bare copper accents from tarnishing over time. Gerber files (PumpkinWitch_Gerbers_Public.zip) are shared publicly from the Hackaday.io project page, so the board can be reproduced, though no firmware applies since the design has no programmable chip.

Search results referencing a Tindie storefront listing describe a version sold with a lanyard, spare batteries, and a portion of proceeds ($5) donated to a girls' STEM program, but the Tindie page could not be retrieved (Cloudflare challenge) to confirm those specifics apply to Pumpkin Witch specifically rather than a similarly-themed TwinkleTwinkie product, so pricing, quantity, and availability are left unfilled here.
