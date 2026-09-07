---
title: Chestoro
id: dc27-dc27-chestoro-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: Twinkle Twinkie
  url: https://hackaday.io/hacker/308303-twinkletwinkie
- name: Wire (Tymkrs)
  url: https://hackaday.io/hacker/308303-twinkletwinkie
  role: firmware collaborator
summary: Chestoro is Twinkle Twinkie's third SAO of the DEF CON 27 badgelife season, a mashup of the Cheshire Cat and Totoro, built with seven side-view LEDs driven by a PIC16F1503 and made in collaboration with Wire of the Tymkrs.
functions: Green eyes and a white mouth glow in animated patterns driven by the onboard MCU; a mode-select button toggles between animations, which after a short while begin rotating randomly.
look:
  colors:
  - purple
  shape: cat
  themes:
  - cat
  - animal
  - movie
tech:
  mcu: PIC16F1503
  leds:
    count: 7
    type: 1204 side-view
    note: driven with 3x 10-ohm resistors, a 10K resistor, and a 10uF capacitor
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing checked 2026-09-07: "This product is no longer available for sale."'
  distribution:
  - purchase
  where: Sold via TwinkleTwinkie's Tindie storefront; now retired/out of stock.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/165323-chestoro-dc27-sao
  url: https://hackaday.io/project/165323-chestoro-dc27-sao
  kind: hackaday
- label: Tindie - TwinkleTwinkie's "Chestoro" Badge SAO
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-chestoro-badge-sao/
  kind: store
  archived: https://web.archive.org/web/20260519051624/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-chestoro-badge-sao/
images:
- file: assets/images/badges/dc27/dc27-chestoro-sao/38fe366918.jpg
  source: https://hackaday.io/project/165323-chestoro-dc27-sao
  credit: TwinkleTwinkie
  caption: Chestoro SAO, front view showing the Cheshire Cat/Totoro mashup face
- file: assets/images/badges/dc27/dc27-chestoro-sao/5296466420.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-chestoro-badge-sao/
  credit: TwinkleTwinkie
  caption: Chestoro SAO product photo from the Tindie listing
  archived: https://web.archive.org/web/20260519051624/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-chestoro-badge-sao/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/165323-chestoro-dc27-sao
  title: Chestoro - DC27 SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/165323-chestoro-dc27-sao
  title: Chestoro - DC27 SAO
  accessed: '2026-09-07'
  note: Confirmed maker, collaborator (Wire of the Tymkrs), LED count/type, MCU, passive components, and SAO v1.69bis compatibility.
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-chestoro-badge-sao/
  title: TwinkleTwinkie's "Chestoro" Badge SAO - Tindie
  accessed: '2026-09-07'
  note: Confirmed it was sold via Tindie and is now retired/sold out; no price or quantity given on the current page.
  archived: https://web.archive.org/web/20260519051624/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-chestoro-badge-sao/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No price, quantity made, or open-source design files were found on either the Hackaday.io project page or the Tindie listing (listing shows only "no longer available for sale").
last_modified_date: '2026-09-07'
---

Chestoro was Twinkle Twinkie's third SAO release of the DEF CON 27 badgelife season, a mashup of the Cheshire Cat and Totoro built in collaboration with Wire of the Tymkrs — their second joint project after the Arc Badge. The design runs on a PIC16F1503 driving seven 1204 side-view LEDs that light the character's green eyes and white mouth; a mode-select button steps through animation patterns, which begin cycling randomly on their own after a short idle period.

The SAO uses the newer v1.69bis (6-pin) standard while remaining backward compatible with the original 4-pin SAO header, and it runs at the standard's 3.3V. It was sold through TwinkleTwinkie's Tindie storefront alongside their other DC27-era add-ons; that listing is now marked as no longer available. No hardware or firmware files, pricing, or production quantity were published on the project's Hackaday.io page or its Tindie listing.
