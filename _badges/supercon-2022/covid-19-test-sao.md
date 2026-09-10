---
title: COVID-19 test SAO
id: supercon-2022-covid-19-test-sao
layout: badge
parent: Supercon 2022
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2022
year: 2022
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A COVID-19 rapid-test-shaped SAO whose result strip blinks via a 555 timer on the back, made as a give-away for internet friends at Supercon 2022.
functions: Blinks two red LEDs (mounted upside down) at roughly 2-3 Hz via an LMC555 astable timer circuit, mimicking a test-strip result line.
look:
  colors:
  - red
  shape: null
  themes:
  - meme
  - pop culture
  - minimalist
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two red LEDs, soldered upside down, driven directly by an LMC555 astable oscillator (no microcontroller).
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  availability_note: 'Checked 2026-09-07: given away at events, not sold.'
  distribution:
  - free_drop
  where: Handed out as a give-away to friends at Supercon 2022, and again at 37C3 (Congress) in December 2023.
make_your_own:
  open_source: true
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/COVID-19%20Test%20SAO
  firmware_url: null
  gerbers_url: null
  bom_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/COVID-19%20Test%20SAO
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: 'BOM: LMC555 timer, two red LEDs (installed upside down), 1uF capacitor, resistors 100 ohm x2, 150 ohm, 390k ohm. KiCad schematic and PCB layout files are in the repo.'
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/187615-covid-19-sao-simple-add-on
  url: https://hackaday.io/project/187615-covid-19-sao-simple-add-on
  kind: hackaday
  archived: https://web.archive.org/web/20251217070056/https://hackaday.io/project/187615-covid-19-sao-simple-add-on
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/COVID-19%20Test%20SAO
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/COVID-19%20Test%20SAO
  kind: repo
images:
- file: assets/images/badges/supercon-2022/covid-19-test-sao/ec0c50a30b.jpg
  source: https://hackaday.io/project/187615-covid-19-sao-simple-add-on
  credit: davedarko
  caption: COVID-19 Test SAO board
  archived: https://web.archive.org/web/20251217070056/https://hackaday.io/project/187615-covid-19-sao-simple-add-on
- file: assets/images/badges/supercon-2022/covid-19-test-sao/867f8e16a7.jpg
  source: https://hackaday.io/project/187615-covid-19-sao-simple-add-on
  credit: davedarko
  caption: COVID-19 Test SAO lit up
  archived: https://web.archive.org/web/20251217070056/https://hackaday.io/project/187615-covid-19-sao-simple-add-on
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/187615-covid-19-sao-simple-add-on
  title: COVID-19 SAO (Simple Add-on) - Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker, Supercon 2022 give-away context, 37C3 (2023) re-distribution, 555-timer LED blink concept, and photos.
  archived: https://web.archive.org/web/20251217070056/https://hackaday.io/project/187615-covid-19-sao-simple-add-on
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/COVID-19%20Test%20SAO
  title: Simple-Add-ons-SAO/COVID-19 Test SAO at main
  accessed: '2026-09-07'
  note: Confirmed BOM (LMC555, two red LEDs upside down, 1uF cap, resistors) and that KiCad source files are published.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No price/quantity figures found; it was a free give-away, not sold, so price/quantity fields are left empty/free rather than guessed. No firmware (none needed — pure 555 analog circuit) and no explicit license found in the repo.
last_modified_date: '2026-09-07'
---

The COVID-19 Test SAO is a small joke add-on made by davedarko (GitHub/Hackaday.io) as a give-away for friends at Supercon 2022. Shaped to evoke a rapid antigen test strip, it uses an LMC555 timer wired as an astable oscillator to blink two red LEDs — soldered upside-down — at a couple of flashes per second, standing in for a wavering "positive" test line. There is no microcontroller; the whole circuit is a handful of passive parts (two 100 ohm resistors, a 150 ohm and a 390k ohm resistor, and a 1uF capacitor) around the 555 chip, plugged into a host badge's SAO header for power.

Distribution was informal and free: davedarko handed out boards (with loose resistors in small bags for the recipient to solder) at Supercon 2022, and again at the 37C3 Chaos Communication Congress in December 2023. The design lives in davedarko's Simple-Add-ons-SAO GitHub repository alongside his other small SAO projects, with KiCad schematic and PCB source files published for anyone who wants to build their own.
