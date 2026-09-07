---
title: Avocado SAO
id: dc30-avocado-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Twinkle Twinkie
  url: https://www.tindie.com/stores/twinkletwinkie/
summary: A googly-eyed avocado-shaped SAO with a squishy 3D-printed "pit" that hides a random-flashing RGB LED.
functions: The RGB LED inside the squishy avocado pit flashes random colors when the SAO is powered through a host badge's SAO header.
look:
  colors: [green]
  shape: avocado
  themes: [food]
tech:
  mcu: none
  leds:
    count: 1
    type: RGB
    note: Mounted inside a squishy 3D-printed avocado "pit"; flashes random colors.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v2
get_one:
  price: $20
  price_usd: 20.0
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing checked 2026-09-06; shows the shop "on break" and not accepting orders.
  distribution:
  - purchase
  where: Sold on Tindie by Twinkle Twinkie
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/twinkletwinkie/twinkletwinkies-avocado-sao
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-avocado-sao/
  kind: store
images:
  - file: assets/images/badges/dc30/avocado-sao/c878f6f698.jpg
    source: "https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-avocado-sao/"
    credit: "Twinkle Twinkie"
    caption: "The Avocado SAO with googly eyes and RGB LED seed, connected via SAO header"
  - file: assets/images/badges/dc30/avocado-sao/de3da82a67.jpg
    source: "https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-avocado-sao/"
    credit: "Twinkle Twinkie"
    caption: "Avocado SAO shown with its SAOv2 female connector"
contact: {}
notes:
- Available 18Jul2022
status: released
sources:
- kind: sheet
  event: dc30
  row: 45
  updated: '2022-07-09'
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-avocado-sao/
  title: "TwinkleTwinkie's Avocado SAO - Tindie"
  accessed: '2026-09-06'
  note: Product description, price, power spec, connector, and package contents; product photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Only source found was the maker's Tindie listing; no Hackaday, GitHub, or press coverage located for this specific SAO, so hardware/firmware openness and exact production quantity are unknown. Web search budget was exhausted mid-task, limiting the search for secondary coverage.
last_modified_date: '2026-09-06'
---

Twinkle Twinkie's Avocado SAO is a small plug-in accessory made for DEF CON 30 badges with an SAO header. It is shaped like a green avocado half, complete with googly eyes, and its "pit" is a squishy 3D-printed piece that hides a single RGB LED which flashes random colors while the SAO is powered.

The board uses a keyed 2x3 SAO v2 (6-pin) female connector and runs on 3.3V supplied by the host badge, so it carries no microcontroller or battery of its own. It sold for $20 on Tindie starting July 18, 2022, and came packaged with a spare SAOv2 female connector so buyers could test it on a breadboard before wiring it to a badge. Twinkle Twinkie's Tindie shop later went on break and stopped accepting orders; no hardware or firmware files for the design could be located.
