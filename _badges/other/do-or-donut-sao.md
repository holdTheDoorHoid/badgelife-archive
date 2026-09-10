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
  colors:
  - white
  shape: circle
  themes:
  - food
tech:
  mcu: none
  leds:
    count: 144
    type: 0603 SMD LED
    note: Arranged as an 8x18 matrix around/across the donut ring, driven by an IS31FL3731 LED matrix controller.
  display: LED matrix 8x18
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 5 prototype boards (white soldermask) ordered from JLCPCB
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
- label: hackaday.io/project/168597-do-or-donut-sao/details
  url: https://hackaday.io/project/168597-do-or-donut-sao/details
  kind: hackaday
- label: hackaday.io/project/168597-do-or-donut-sao/logs
  url: https://hackaday.io/project/168597-do-or-donut-sao/logs
  kind: hackaday
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
- file: assets/images/badges/other/do-or-donut-sao/d3b20f13de.png
  source: https://hackaday.io/project/168597-do-or-donut-sao
  credit: davedarko
  caption: Layout test render of the Do or Donut SAO donut-shaped LED matrix board
  archived: https://web.archive.org/web/20251210174801/https://hackaday.io/project/168597-do-or-donut-sao
- file: assets/images/badges/other/do-or-donut-sao/dd71631df7.png
  source: https://hackaday.io/project/168597-do-or-donut-sao/logs
  credit: davedarko
  caption: Photo of prototype boards from the build log
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
- kind: url
  url: https://hackaday.io/project/168597-do-or-donut-sao/details
  title: Do or Donut SAO - Details
  accessed: '2026-09-07'
  note: Confirms IS31FL3731 driver, 16x9 matrix rotated/remapped into the donut ring, and that the posted render was only a layout test needing a redraw.
- kind: url
  url: https://hackaday.io/project/168597-do-or-donut-sao/logs
  title: Do or Donut SAO - Logs
  accessed: '2026-09-07'
  note: 'Two log entries (Nov 24 and Nov 27, 2019): routing finished and 5 white test boards plus 800 0603 LEDs (red, yellow, orange, green, blue, white, pink, purple) ordered; BOM about 7 EUR/unit; IS31FL3731 sourced in QFN since SSOP was hard to find.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No specific convention or event is named by the maker anywhere found (Hackaday.io project or GitHub repo); this appears to be a personal badgelife-community project rather than a con-specific release, so event is left as "other". No price, quantity sold, or availability info found — it reads as a small hobbyist test run (5 white boards from JLCPCB) rather than a commercial product. No MCU is present; the IS31FL3731 is an LED driver, not a microcontroller, and it would be driven by whichever host badge it's plugged into. Hardware files (schematic, board, Gerbers) are published on GitHub; no firmware/software repo was found, so open_source is marked partial rather than yes. Merged with duplicate entry 'Do or Donut SAO' (other-do-or-donut-sao-2).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/do-or-donut-sao-2/
---

Do or Donut is a donut-shaped Simple Add-On (SAO) by hobbyist maker davedarko, created in November 2019. Its ring is covered edge-to-edge with tiny 0603 surface-mount LEDs — around 800 were ordered across red, yellow, orange, green, blue, white, pink, and purple — wired as an 8x18 matrix and driven by an IS31FL3731 LED matrix controller, the same driver chip used in many badgelife blinky designs. The layout scatters the LEDs like sprinkles across the donut shape rather than in a clean grid, which was part of the design challenge documented in the project's build logs.

The project doesn't appear to have been made for or sold at a specific convention; it reads as one of several personal SAO designs the maker built and shared through their "Simple Add-ons SAO" GitHub repository and Hackaday.io. The bill of materials ran about 7 EUR per unit, and the maker ordered five white test boards from JLCPCB — consistent with a small prototype run rather than a batch made for con distribution. No price, sale, or giveaway information was found.

## Make your own

The schematic, board layout, and Gerber files for the Do Or DoNut are published in the `Do Or DoNut` folder of davedarko's Simple-Add-ons-SAO GitHub repository, making the hardware side of the project open. No accompanying firmware or driver code repository was located.

## Notes merged from the duplicate entry "Do or Donut SAO"

The Do or Donut SAO is a Shitty Add-On designed by Hackaday.io user davedarko, posted in late November 2019. It takes the 16x9 LED matrix normally addressed by an IS31FL3731 driver chip and remaps it, row by row, into a ring of individually lit 0603 LEDs arranged around a donut-shaped PCB outline. The driver was sourced in a QFN package after the maker found the SSOP version hard to obtain, and the bill of materials for one board came to roughly 7 EUR.

The project moved quickly from concept to hardware: routing was finished and five white-soldermask prototype boards were ordered from JLCPCB on November 24, 2019, alongside a bulk order of 800 0603 LEDs spanning red, yellow, orange, green, blue, white, pink, and purple. The maker was explicit that the posted board render was only a layout test, planning to redraw the design smaller and re-verify the LED arrangement once the arrangement was confirmed against the running row pattern of "1-10-2-11-3-12-4-13-5-14-6-15-7-16-8-17-9-18."

No later log entries, finished-board photos, sale listings, or published design files turned up, so it is unclear whether the SAO progressed past this prototype run. The project page is not tied to any specific convention in the maker's own text, so it is catalogued here as a general badgelife release rather than assigned to a particular event.
