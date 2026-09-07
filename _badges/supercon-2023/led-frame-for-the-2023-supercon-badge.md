---
title: LED Frame for the 2023 Supercon Badge
id: supercon-2023-led-frame-for-the-2023-supercon-badge
layout: badge
parent: Supercon 2023
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2023
year: 2023
makers:
- name: makeTVee
  url: https://hackaday.io/maketvee
summary: A custom resin-printed frame that adds 280 individually addressable RGB LEDs around the official 2023 Supercon badge, driven by a Raspberry Pi Pico.
functions: Runs Micropython animations across the LED ring using a neopixel library, at roughly 25% brightness to stay within power limits.
look:
  colors:
  - multicolor
  shape: null
  themes:
  - hardware tool
tech:
  mcu: Raspberry Pi Pico
  leds:
    count: 280
    type: WS2812B-1010
    note: 1x1mm package addressable LEDs, wired to GPIO28 on the Pico, run at ~25% brightness (5mA per channel per LED).
  display: none
  connectivity: []
  battery: LiPo (custom holder sized to fit the badge's existing AA slots)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not sold; a personal badge-hack project built by the maker for their own 2023 Supercon badge.'
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/193633-led-frame-for-the-2023-supercon-badge
  firmware_url: null
  eda_tool: Fusion 360
  notes: 'The frame is a resin-printed STL (designed in Fusion360) shared on the Hackaday.io project page; a companion LiPo battery holder is shared separately on Printables. Firmware source was not published on the project page, only that it runs Micropython with a neopixel library.'
links:
- label: hackaday.io/project/193633-led-frame-for-the-2023-supercon-badge
  url: https://hackaday.io/project/193633-led-frame-for-the-2023-supercon-badge
  kind: hackaday
images:
- file: assets/images/badges/supercon-2023/led-frame-for-the-2023-supercon-badge/25d03998ce.png
  source: "https://hackaday.io/project/193633-led-frame-for-the-2023-supercon-badge"
  credit: "makeTVee"
  caption: "The LED frame lit up on the 2023 Supercon badge"
- file: assets/images/badges/supercon-2023/led-frame-for-the-2023-supercon-badge/1bf37c3a10.jpg
  source: "https://hackaday.io/project/193633-led-frame-for-the-2023-supercon-badge"
  credit: "makeTVee"
  caption: "The resin-printed LED frame during assembly"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/193633-led-frame-for-the-2023-supercon-badge
  title: LED Frame for the 2023 Supercon Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''Supercon 2023''.'
- kind: url
  url: https://hackaday.io/project/193633-led-frame-for-the-2023-supercon-badge
  title: LED Frame for the 2023 Supercon Badge
  accessed: '2026-09-07'
  note: 'Primary source for maker (makeTVee), components (280x WS2812B-1010, Raspberry Pi Pico, GPIO28), Micropython/neopixel firmware, Fusion360-designed resin-printed frame, LiPo battery holder shared on Printables, and build story (hand-soldered at the con over 1.5 days).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a badge-hack accessory (an LED add-on frame) built by an attendee for the official 2023 Supercon badge, not a commercially distributed badge/SAO itself, so price/quantity/availability fields do not apply and are left empty. The firmware source code was not found published (only the language/library used); the Printables battery-holder link was mentioned but its URL was not given on the project page and could not be confirmed. No independent third-party coverage (press, forums) was found beyond the maker''s own Hackaday.io project page.'
last_modified_date: '2026-09-07'
---

The LED Frame for the 2023 Supercon Badge is a badge-hack accessory built by Hackaday.io user makeTVee, who wanted their official Supercon 2023 badge to carry more light than it shipped with. The frame itself is a resin-printed ring designed in Fusion 360 that wraps around the badge and holds 280 individually addressable WS2812B-1010 LEDs (a tiny 1x1mm package), wired to GPIO28 of a Raspberry Pi Pico riding alongside the badge's own electronics.

Animations are written in MicroPython using a neopixel library, and the LEDs are run at around 25% brightness to keep current draw manageable, since each LED can pull up to 5mA per color channel at full output. To power the array without overtaxing the badge, the maker designed a separate LiPo battery holder sized to drop into the badge's existing AA battery slots, published as a companion file on Printables. The frame was hand-soldered on site at Supercon using a Pinecil USB-C iron and magnifying glasses, taking about a day and a half of work before the maker got it running.

This is a one-off personal project rather than a kit or product for sale — it was not distributed to other attendees, and the write-up focuses on the design and build process rather than availability. The STL for the frame is shared on the Hackaday.io project page, making the hardware side reproducible, though the firmware source itself was not posted there.
