---
title: Purple Cyclops
id: dc32-purple-cyclops
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: Oakmizer
  url: https://hackaday.io/oakmizer
summary: A ~45mm SAO with an AI-generated cyclops character rendered in JLCPCB multicolor silkscreen, built to compare how backlit LEDs diffuse through the PCB from two different mounting layouts.
functions: 'No interactivity beyond lighting; the badge exists to compare LED diffusion through the PCB in two variants: bottom-facing LEDs and side-facing LEDs.'
look:
  colors:
  - purple
  shape: null
  themes: []
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: 2 red and 2 amber SMD LEDs (Inolux and Wurth Elektronik), lit through the PCB from the backside; a 10-ohm resistor is used.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: two small batches (exact count not stated)
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/197216-purple-cyclops
  firmware_url: null
  eda_tool: EasyEDA
links:
- label: hackaday.io/project/197216-purple-cyclops
  url: https://hackaday.io/project/197216-purple-cyclops
  kind: hackaday
  archived: https://web.archive.org/web/20260206212708/https://hackaday.io/project/197216-purple-cyclops
images:
- file: assets/images/badges/dc32/purple-cyclops/3736986300.jpg
  source: https://hackaday.io/project/197216-purple-cyclops
  credit: Oakmizer
  caption: Purple Cyclops SAO, bottom-view LED variant PCB render
  archived: https://web.archive.org/web/20260206212708/https://hackaday.io/project/197216-purple-cyclops
- file: assets/images/badges/dc32/purple-cyclops/1ade8b5775.jpg
  source: https://hackaday.io/project/197216-purple-cyclops
  credit: Oakmizer
  caption: Purple Cyclops SAO, side-view LED variant PCB render
  archived: https://web.archive.org/web/20260206212708/https://hackaday.io/project/197216-purple-cyclops
contact: {}
notes:
- Gerber files for both LED variants are linked from the Hackaday.io project page, in EasyEDA format; no separate firmware exists since the board has no MCU.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197216-purple-cyclops
  title: Purple Cyclops
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''DEF CON 32''.'
  archived: https://web.archive.org/web/20260206212708/https://hackaday.io/project/197216-purple-cyclops
- kind: url
  url: https://hackaday.io/project/197216-purple-cyclops
  title: Purple Cyclops
  accessed: '2026-09-07'
  note: 'Fetched project page for full write-up: maker (Oakmizer), event/year (DEF CON 32, 2024), components (JLCPCB multicolor silkscreen, 4 SMD LEDs, 10-ohm resistor, SMT 2x3 SAO header), two LED-layout variants, Gerber/EasyEDA files, and a noted polarity bug on the side-view variant.'
  archived: https://web.archive.org/web/20260206212708/https://hackaday.io/project/197216-purple-cyclops
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check (2026-09-07): confirmed maker, event, dimensions, LED count/parts (Inolux and Wurth SMD LEDs), 10-ohm resistor, EasyEDA Gerber files for both variants, no-MCU/no-firmware, and the side-view polarity bug by re-fetching the Hackaday.io project page directly. Found and fixed two errors: (1) the two saved images had swapped captions — the file hashed 3736986300 is actually the bottom-view PCB render and 1ade8b5775 is the side-view render, opposite of what was recorded; both are gerber/schematic renders from the page, not photos of an assembled badge, so captions were also updated to say so. (2) removed the "sci-fi" look.theme tag: the project page never describes the character thematically (it just says it is an AI-generated cyclops image), so that tag was an unsupported guess rather than something sourced. Everything else in the entry checked out. Price, quantity made beyond "two small batches," and distribution/availability are still not stated on the project page and
    remain blank; status "released" is inferred from the two batches having been fabricated for a specific past con rather than an explicit statement that attendees received one, so status is left as researched rather than verified.'
last_modified_date: '2026-09-11'
model:
  file: assets/models/dc32/purple-cyclops.glb
  method: gerber
  source_file: clean
  generated: '2026-09-11'
  bytes: 93388
  size_mm:
  - 44.5
  - 44.9
---

The Purple Cyclops is a Simple Add-On (SAO) made by Oakmizer for DEF CON 32 (2024). At about 45mm, it uses JLCPCB's multicolor silkscreen process to render an AI-generated cyclops character directly on the board, with four SMD LEDs (two red, two amber) lighting the design from behind through the PCB substrate.

The project was explicitly an experiment in light diffusion: two small batches were made, one with LEDs facing the bottom of the board and one with LEDs facing the side (the side-facing variant was later improved with hot glue to spread the light more evenly). The side-view board has a documented LED polarity bug that builders need to check before assembly. The badge has no microcontroller — it's a passive, always-lit add-on powered through its SAO connector — so there is no firmware to speak of.

Gerber files for both variants, designed in EasyEDA, are linked from the Hackaday.io project page. No pricing, production quantity, or distribution details (sale, giveaway, etc.) are given, and no storefront listing or other coverage of the badge was found.

## Make your own

Gerbers for both the bottom-view and side-view LED layouts are available on the [Hackaday.io project page](https://hackaday.io/project/197216-purple-cyclops), ready to send to a fab that supports JLCPCB-style multicolor silkscreen. Builders should double-check LED polarity on the side-view variant before soldering, per the maker's own note.
