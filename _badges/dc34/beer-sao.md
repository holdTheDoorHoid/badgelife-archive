---
title: Beer SAO
id: dc34-beer-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: aerospace-venoms
  url: https://github.com/aerospace-venoms
summary: A red-solo-cup-shaped SAO with a three-digit 7-segment display that reads out beverage temperature from a waterproof probe. Made for winners of DEF CON 34's Beverage Cooling Contraption Contest (BCCC).
functions: Waterproof temperature probe, for measuring your beer temp in real-time. Rectal use optional but encouraged. Displays the reading in Fahrenheit on three 7-segment LED digits, with four selectable brightness levels; falls back to the RP2350's internal die sensor if the external probe is unplugged.
look:
  colors:
  - red
  shape: cup
  themes:
  - beer
  - drink
tech:
  mcu: RP2350
  leds:
    count: 3
    type: 7-segment (common-anode)
    note: Multiplexed via a 74HC595 shift register; shine-through digits under a 3D-printed shroud.
  display: 3-digit 7-segment LED
  connectivity:
  - usb
  battery: powered by host badge or USB-C
  sao_version: null
get_one:
  price: $45
  price_usd: 45.0
  quantity: '56 sold as of check (storefront listed "OUT", pre-order option available)'
  availability: sold_out
  distribution:
  - purchase
  - preorder
  where: Sold directly through the maker's Uberflux storefront; includes the cup SAO, a waterproof DS18B20 probe on a ~250mm cable, and a DEF CON 34 SAO 180-degree adapter.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/aerospace-venoms/BCCC_Temperature_SAO
  firmware_url: https://github.com/aerospace-venoms/BCCC_Temperature_SAO
  eda_tool: KiCad
links:
- label: uberflux.com/product/BUD-BEER-SAO
  url: https://uberflux.com/product/BUD-BEER-SAO
  kind: store
- label: github.com/aerospace-venoms/BCCC_Temperature_SAO
  url: https://github.com/aerospace-venoms/BCCC_Temperature_SAO
  kind: repo
images:
  - file: assets/images/badges/dc34/beer-sao/f8c144bba2.jpg
    source: "https://uberflux.com/product/BUD-BEER-SAO"
    credit: "aerospace-venoms"
    caption: "Beer SAO product photo, red solo-cup shape with 7-segment display"
  - file: assets/images/badges/dc34/beer-sao/baa680f9ed.jpg
    source: "https://uberflux.com/product/BUD-BEER-SAO"
    credit: "aerospace-venoms"
    caption: "Beer SAO with waterproof DS18B20 temperature probe cable"
contact:
  discord: the_ames
  emails:
  - ames@aerospacevenoms.com
notes:
- "Sheet listed the maker as 'Beverage Cooling Contraption Contest'; the item is made by aerospace-venoms (contact: ames), for BCCC winners."
- "Sheet listed price as $10; the maker's storefront lists $45. Kept the storefront price as the sourced figure and noted the discrepancy here."
status: released
sources:
- kind: sheet
  event: dc34
  row: 50
  updated: 7/25/2026 12:09:12
  listing: New
- kind: url
  url: https://uberflux.com/product/BUD-BEER-SAO
  title: "Beer SAO - BUD-BEER-SAO | Uberflux"
  accessed: '2026-09-06'
  note: "Price ($45), package contents, quantity sold (56), sold-out/pre-order status, RP2350 mention, images."
- kind: url
  url: https://github.com/aerospace-venoms/BCCC_Temperature_SAO
  title: "aerospace-venoms/BCCC_Temperature_SAO"
  accessed: '2026-09-06'
  note: "Maker identity, RP2350A chip detail, 7-segment/74HC595 LED design, WTFPL v2 license, KiCad hardware + Pico SDK firmware confirmed open source, dual-core firmware design, DS18B20 sensor with internal-die fallback."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: "Core facts confirmed directly from the maker's own storefront and GitHub repo. Could not find a Hackaday.io page or press coverage; none appears to exist. Exact SAO header version (v1/v1.69bis) not stated in either source, left null. 'Quantity made' (as opposed to units sold) not stated."
last_modified_date: '2026-09-06'
---

The Beer SAO is a red-solo-cup-shaped add-on made by aerospace-venoms (maker handle "ames") for winners of DEF CON 34's Beverage Cooling Contraption Contest (BCCC) — the long-running contest where hackers build janky refrigeration rigs to chill their drinks. Rather than just looking like a beer, it actually measures one: a waterproof DS18B20 probe on a roughly 250mm cable plugs into the board and reports the temperature in Fahrenheit across three 7-segment LED digits, multiplexed through a 74HC595 shift register and shining through a 3D-printed shroud. If the external probe isn't plugged in, the board falls back to reading its own RP2350's internal die temperature instead.

Under the hood it runs a Raspberry Pi RP2350A, split across both cores — one core handles the sensor reads, the other drives the multiplexed display — with USB-C for programming and serial debug, and four selectable brightness levels on hardware revision 1.3 and later. The unit ships as a kit consisting of the cup-shaped SAO board, the waterproof probe, and a DEF CON 34 SAO 180-degree adapter, sold for $45 through the maker's Uberflux storefront; as of this check the listing showed 56 sold and marked "OUT," with a pre-order option still open.

Hardware and firmware are both fully open source under the WTFPL v2 license, published in the `aerospace-venoms/BCCC_Temperature_SAO` GitHub repo: KiCad project files for the board (whose art started as an AI-generated image, refined in Inkscape and imported via the SVG2Shenzhen plugin) plus Raspberry Pi Pico SDK firmware source and prebuilt UF2 images, along with batch-programming build scripts.

## Make your own

The GitHub repo (https://github.com/aerospace-venoms/BCCC_Temperature_SAO) includes the KiCad hardware source and Pico-SDK firmware. Flashing a UF2 image over USB-C in BOOTSEL mode is the general Pico-SDK approach; consult the repo's own build scripts and README for the exact steps and any batch-programming tooling.
