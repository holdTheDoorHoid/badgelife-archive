---
title: MAP4
id: other-map4
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 2016
makers:
- name: Anool Mahidharia
  url: https://hackaday.io/anool-mahidharia
- name: Vaibhav Chhabra
  url: https://hackaday.io/vaibhav-chhabra
summary: A simple blinky learn-to-solder badge kit built for workshops at Maker's Asylum, a hackerspace in Mumbai, India.
functions: Three LEDs light up when powered by a coin battery; no microcontroller. Built as a soldering-practice project, with variants for different LED colors, blinking LEDs, or a light-dependent resistor in place of a series resistor for light-controlled brightness.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: Series current-limiting resistors; color and blink behavior customizable per builder.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as a soldering kit at Maker's Asylum workshops in Mumbai and Delhi, India.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/MakersAsylumIndia/MAP4
  firmware_url: null
  eda_tool: KiCad
  license: CERN Open Hardware Licence v1.2
  notes: Repo includes schematics, silk legends, dimension drawings, and copper layer PDFs, plus KiCad source and board renders across multiple revisions.
links:
- label: hackaday.io/project/27414-map4
  url: https://hackaday.io/project/27414-map4
  kind: hackaday
  archived: https://web.archive.org/web/20260610181035/https://hackaday.io/project/27414-map4
- label: github.com/MakersAsylumIndia/MAP4
  url: https://github.com/MakersAsylumIndia/MAP4
  kind: repo
images:
- file: assets/images/badges/other/map4/6121a65956.jpg
  source: https://hackaday.io/project/27414-map4
  credit: Anool Mahidharia / Vaibhav Chhabra
  caption: MAP4 blinky badge kit
  archived: https://web.archive.org/web/20260610181035/https://hackaday.io/project/27414-map4
- file: assets/images/badges/other/map4/c580a286ad.jpg
  source: https://hackaday.io/project/27414-map4
  credit: Anool Mahidharia / Vaibhav Chhabra
  caption: MAP4 badge assembled with LEDs and coin battery
  archived: https://web.archive.org/web/20260610181035/https://hackaday.io/project/27414-map4
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/27414-map4
  title: MAP4
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
  archived: https://web.archive.org/web/20260610181035/https://hackaday.io/project/27414-map4
- kind: url
  url: https://hackaday.io/project/27414-map4
  title: MAP4 project page (Hackaday.io)
  accessed: '2026-09-07'
  note: Confirmed maker names, purpose, LED/battery specs, and repo link; project logged Sep 2017, kit built May 2016.
  archived: https://web.archive.org/web/20260610181035/https://hackaday.io/project/27414-map4
- kind: url
  url: https://github.com/MakersAsylumIndia/MAP4
  title: MakersAsylumIndia/MAP4 (GitHub)
  accessed: '2026-09-07'
  note: Confirmed open-source KiCad hardware files and CERN OHL v1.2 license; no microcontroller.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: MAP4 is not a hacker-conference badge; it is a learn-to-solder blinky kit made for workshops at Maker's Asylum, a hackerspace in Mumbai, India (led in part by Mitch Altman, May 2016). No matching event exists in events.yml, so event is left as 'other'. No price, quantity made, or current availability was found; the Hackaday.io project is marked complete but does not state whether the kit is still distributed.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/map4.glb
  method: kicad
  source_file: kicad/map4_v9/MAP4.kicad_pcb
  generated: '2026-09-10'
  bytes: 76968
---

MAP4 is a simple learn-to-solder badge built by Anool Mahidharia and Vaibhav Chhabra for workshops at Maker's Asylum, a hackerspace with locations in Mumbai and Delhi, India. The kit was built in May 2016 for a workshop led by Mitch Altman, and the project page was published to Hackaday.io in September 2017.

The badge has no microcontroller: it is a purely analog circuit with three LEDs, series current-limiting resistors, and a CR2032 coin cell, designed to teach beginners soldering, resistor color codes, and multimeter use. Builders can customize it with different LED colors or blinking LEDs, or swap in a light-dependent resistor so the LEDs respond to ambient light.

## Make your own

The hardware is fully open, published on GitHub under the CERN Open Hardware Licence v1.2. The repository includes KiCad source files, schematics, silk legend and dimension drawings, and copper layer PDFs across several board revisions, making it straightforward to reproduce or adapt the design.
