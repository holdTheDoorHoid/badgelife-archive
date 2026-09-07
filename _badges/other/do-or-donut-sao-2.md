---
title: Do or Donut SAO
id: other-do-or-donut-sao-2
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2019
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: A donut-shaped LED matrix Shitty Add-On built around an IS31FL3731 driver, with the chip's 16x9 matrix remapped into a ring of multicolour 0603 LEDs; posted November 2019 as a layout test with five white prototype boards ordered from JLCPCB.
functions: 'Programmable LED matrix; the 16x9 grid of the IS31FL3731 driver is rewired into a donut-shaped ring of individually addressable LEDs.'
look:
  colors: [white]
  shape: circle
  themes: [food, minimalist]
tech:
  mcu: none
  leds:
    count: null
    type: "0603 RGB (mixed single-color: red, yellow, orange, green, blue, white, pink, purple)"
    note: "Driven by an IS31FL3731 matrix driver (QFN package used instead of hard-to-source SSOP); LEDs bought in bulk (800 pcs) across the listed colors, not all used on one board."
  display: null
  connectivity: [i2c]
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '5 prototype boards (white soldermask) ordered from JLCPCB'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/168597-do-or-donut-sao
  url: https://hackaday.io/project/168597-do-or-donut-sao
  kind: hackaday
- label: hackaday.io/project/168597-do-or-donut-sao/details
  url: https://hackaday.io/project/168597-do-or-donut-sao/details
  kind: hackaday
- label: hackaday.io/project/168597-do-or-donut-sao/logs
  url: https://hackaday.io/project/168597-do-or-donut-sao/logs
  kind: hackaday
images:
  - file: assets/images/badges/other/do-or-donut-sao-2/d3b20f13de.png
    source: "https://hackaday.io/project/168597-do-or-donut-sao"
    credit: "davedarko"
    caption: "Layout test render of the Do or Donut SAO donut-shaped LED matrix board"
  - file: assets/images/badges/other/do-or-donut-sao-2/dd71631df7.png
    source: "https://hackaday.io/project/168597-do-or-donut-sao/logs"
    credit: "davedarko"
    caption: "Photo of prototype boards from the build log"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/168597-do-or-donut-sao
  title: Do or Donut SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/168597-do-or-donut-sao/details
  title: "Do or Donut SAO - Details"
  accessed: '2026-09-07'
  note: "Confirms IS31FL3731 driver, 16x9 matrix rotated/remapped into the donut ring, and that the posted render was only a layout test needing a redraw."
- kind: url
  url: https://hackaday.io/project/168597-do-or-donut-sao/logs
  title: "Do or Donut SAO - Logs"
  accessed: '2026-09-07'
  note: "Two log entries (Nov 24 and Nov 27, 2019): routing finished and 5 white test boards plus 800 0603 LEDs (red, yellow, orange, green, blue, white, pink, purple) ordered; BOM about 7 EUR/unit; IS31FL3731 sourced in QFN since SSOP was hard to find."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Maker's own Hackaday.io project page and logs confirm the core technical facts (driver chip, matrix remapping, prototype quantity, BOM cost). No event/con is named anywhere on the project - it reads as a general badgelife SAO experiment posted November 2019, not tied to a specific convention, so event is left as 'other'. No price-for-sale, availability, open-source hardware files, or finished-board photos were found; the project's own file count showed zero uploaded design files at last check. LED count on the finished board and any MCU/host requirements beyond the driver chip are not stated."
last_modified_date: '2026-09-07'
---

The Do or Donut SAO is a Shitty Add-On designed by Hackaday.io user davedarko, posted in late November 2019. It takes the 16x9 LED matrix normally addressed by an IS31FL3731 driver chip and remaps it, row by row, into a ring of individually lit 0603 LEDs arranged around a donut-shaped PCB outline. The driver was sourced in a QFN package after the maker found the SSOP version hard to obtain, and the bill of materials for one board came to roughly 7 EUR.

The project moved quickly from concept to hardware: routing was finished and five white-soldermask prototype boards were ordered from JLCPCB on November 24, 2019, alongside a bulk order of 800 0603 LEDs spanning red, yellow, orange, green, blue, white, pink, and purple. The maker was explicit that the posted board render was only a layout test, planning to redraw the design smaller and re-verify the LED arrangement once the arrangement was confirmed against the running row pattern of "1-10-2-11-3-12-4-13-5-14-6-15-7-16-8-17-9-18."

No later log entries, finished-board photos, sale listings, or published design files turned up, so it is unclear whether the SAO progressed past this prototype run. The project page is not tied to any specific convention in the maker's own text, so it is catalogued here as a general badgelife release rather than assigned to a particular event.
