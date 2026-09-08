---
title: Do Or Donut
id: other-do-or-donut-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2019
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A donut-shaped SAO with a matrix of surface-mount LEDs driven by an IS31FL3731 controller, arranged around and across the ring like sprinkles on a donut.
functions: Lights up an LED matrix arranged in a donut shape; no other interactive functions documented.
look:
  colors: []
  shape: circle
  themes:
  - food
tech:
  mcu: null
  leds:
    count: 144
    type: 0603 SMD LED
    note: Arranged as an 8x18 matrix around/across the donut ring, driven by an IS31FL3731 LED matrix controller.
  display: LED matrix 8x18
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
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Do%20Or%20DoNut
  firmware_url: null
  eda_tool: null
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/168597-do-or-donut-sao
  url: https://hackaday.io/project/168597-do-or-donut-sao
  kind: hackaday
  archived: https://web.archive.org/web/20251210174801/https://hackaday.io/project/168597-do-or-donut-sao
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/Do%20Or%20DoNut
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Do%20Or%20DoNut
  kind: repo
images:
- file: assets/images/badges/other/do-or-donut-sao/d3b20f13de.png
  source: https://hackaday.io/project/168597-do-or-donut-sao
  credit: davedarko
  caption: Do or Donut SAO with donut-shaped LED matrix
  archived: https://web.archive.org/web/20251210174801/https://hackaday.io/project/168597-do-or-donut-sao
- file: assets/images/badges/other/do-or-donut-sao/dd71631df7.png
  source: https://hackaday.io/project/168597-do-or-donut-sao
  credit: davedarko
  caption: Do or Donut SAO PCB layout / lit LED matrix detail
  archived: https://web.archive.org/web/20251210174801/https://hackaday.io/project/168597-do-or-donut-sao
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/168597-do-or-donut-sao
  title: Do or Donut SAO | Hackaday.io
  accessed: '2026-09-07'
  note: Hackaday.io project page; confirms creator, creation date (Nov 2019), IS31FL3731 driver chip, ~800 0603 LEDs ordered in multiple colors, BOM ~7 EUR per unit, and 5 white JLCPCB test boards ordered. No event is named on the page.
  archived: https://web.archive.org/web/20251210174801/https://hackaday.io/project/168597-do-or-donut-sao
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Do%20Or%20DoNut
  title: davedarko/Simple-Add-ons-SAO — Do Or DoNut
  accessed: '2026-09-07'
  note: Repo folder confirms an 8x18 LED matrix layout and that schematic/board/Gerber files are published (open hardware); no firmware repo found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No specific convention or event is named by the maker anywhere found (Hackaday.io project or GitHub repo); this appears to be a personal badgelife-community project rather than a con-specific release, so event is left as "other". No price, quantity sold, or availability info found — it reads as a small hobbyist test run (5 white boards from JLCPCB) rather than a commercial product. No MCU is present; the IS31FL3731 is an LED driver, not a microcontroller, and it would be driven by whichever host badge it's plugged into. Hardware files (schematic, board, Gerbers) are published on GitHub; no firmware/software repo was found, so open_source is marked partial rather than yes.
last_modified_date: '2026-09-07'
---

Do or Donut is a donut-shaped Simple Add-On (SAO) by hobbyist maker davedarko, created in November 2019. Its ring is covered edge-to-edge with tiny 0603 surface-mount LEDs — around 800 were ordered across red, yellow, orange, green, blue, white, pink, and purple — wired as an 8x18 matrix and driven by an IS31FL3731 LED matrix controller, the same driver chip used in many badgelife blinky designs. The layout scatters the LEDs like sprinkles across the donut shape rather than in a clean grid, which was part of the design challenge documented in the project's build logs.

The project doesn't appear to have been made for or sold at a specific convention; it reads as one of several personal SAO designs the maker built and shared through their "Simple Add-ons SAO" GitHub repository and Hackaday.io. The bill of materials ran about 7 EUR per unit, and the maker ordered five white test boards from JLCPCB — consistent with a small prototype run rather than a batch made for con distribution. No price, sale, or giveaway information was found.

## Make your own

The schematic, board layout, and Gerber files for the Do Or DoNut are published in the `Do Or DoNut` folder of davedarko's Simple-Add-ons-SAO GitHub repository, making the hardware side of the project open. No accompanying firmware or driver code repository was located.
