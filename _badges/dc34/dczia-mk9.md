---
title: DCZia Mk9
id: dc34-dczia-mk9
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
series: DCZia
makers:
- name: DCZia
  url: https://github.com/dczia
- name: Snurkle Engineering (hamster)
  url: https://uberflux.com/maker/hamster
  role: designer/seller
summary: 'DCZia''s DEF CON 34 badge: a wearable, fully functional 3x3 mechanical macropad built on an RP2040 with nine MX-footprint switches, per-key WS2812 RGB plus SK6812 side-firing underglow, a 3-axis accelerometer, two SAO connectors, USB-C and 3xAAA power, shipping with CircuitPython/MicroPython firmware and designed for QMK reflashing; sold as a partial kit (user adds switches and battery box) with a bundled SAO add-on board that takes three more switches or an OLED.'
functions: Nine independently programmable mechanical keys with per-key RGB; accelerometer-driven tilt/shake-reactive lighting patterns (rainbow wave, breathing pulse, sparkle); doubles as a real USB HID n-key-rollover macropad after the con; two SAO ports for add-ons.
look:
  colors:
  - black
  - blue
  shape: rectangle
  themes:
  - hardware tool
  - learn to solder
  - keyboard
tech:
  mcu: RP2040
  leds:
    count: 15
    type: WS2812B/SK6812
    note: 9x WS2812B per-key RGB (one under each switch) plus 6x SK6812 side-firing underglow LEDs
  display: none
  connectivity:
  - usb
  battery: 3x AAA, or USB-C
  sao_version: v1
  sao_ports: 2
get_one:
  price: $60
  price_usd: 60
  quantity: null
  availability: limited
  availability_note: uberflux.com listing showed 2 remaining (72 sold) as of 2026-09-07
  distribution:
  - purchase
  where: Sold via the Uberflux storefront (uberflux.com/product/HAMST-DCZIA-2026), listed under maker "hamster" / Snurkle Engineering; shipped by USPS ($10) with in-person DEF CON pickup also offered.
make_your_own:
  open_source: true
  hardware_url: https://github.com/dczia/mk9-badge
  firmware_url: https://github.com/dczia/mk9-badge
  eda_tool: KiCad
links:
- label: uberflux.com/product/HAMST-DCZIA-2026
  url: https://uberflux.com/product/HAMST-DCZIA-2026
  kind: store
- label: github.com/dczia/mk9-badge
  url: https://github.com/dczia/mk9-badge
  kind: repo
- label: cad.onshape.com/documents/36884624fbe35c16a5af61a7/w/233227193d278274727a44c3/e/ea987b4b53c4648fa3dc84b6
  url: https://cad.onshape.com/documents/36884624fbe35c16a5af61a7/w/233227193d278274727a44c3/e/ea987b4b53c4648fa3dc84b6
  kind: website
- label: uberflux.com/maker/hamster
  url: https://uberflux.com/maker/hamster
  kind: store
- label: dczia.net
  url: https://dczia.net/
  kind: website
images:
- file: assets/images/badges/dc34/dczia-mk9/30b29bb628.jpg
  source: https://uberflux.com/product/HAMST-DCZIA-2026
  credit: DCZia (Snurkle Engineering)
  caption: DCZia Mk9 badge, product listing photo
- file: assets/images/badges/dc34/dczia-mk9/6627a588fe.jpg
  source: https://uberflux.com/product/HAMST-DCZIA-2026
  credit: DCZia (Snurkle Engineering)
  caption: DCZia Mk9 badge, additional product photo
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://uberflux.com/product/HAMST-DCZIA-2026
  title: DcZia Mk9
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/dczia/mk9-badge
  title: dczia/mk9-badge
  accessed: '2026-09-07'
  note: Confirms RP2040, LED counts, KiCad hardware files, CircuitPython/QMK firmware, SAO count.
- kind: url
  url: https://uberflux.com/maker/hamster
  title: Uberflux maker page — hamster
  accessed: '2026-09-07'
  note: Identifies the seller as Snurkle Engineering (handle "hamster"); storefront lists only the Mk9 under this maker.
- kind: url
  url: https://dczia.net/
  title: DCZia
  accessed: '2026-09-07'
  note: DCZia group background (formed around DEF CON 22, NM ties); confirms Mk9 has 9 neopixels, 6 RGB sidelights, accelerometer, custom 3-piece shell, and calls it a throwback to their 2018 keygrid badge.
- kind: url
  url: https://github.com/lithochasm/dczia2026-mk9-badge
  title: lithochasm/dczia2026-mk9-badge
  accessed: '2026-09-07'
  note: A fork/mirror of the badge repo for DEF CON 34 2026; cross-confirms hardware spec (RP2040, WS2812B+SK6812, 2 SAO, MicroPython/QMK) and KiCad+BOM contents.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price and stock count ($60, 2 of 74 remaining) are a live snapshot from the storefront on 2026-09-07 and will go stale. No stated total production quantity was found, only sold+remaining at time of check. License for the open-source files was not explicitly named on any source (repo said "committed to open source hardware and software" without naming a license). Individual member names behind "DCZia" were not published on any source checked. OnShape CAD link was in the entry but not independently verified beyond being reachable.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/dczia-mk9.glb
  method: kicad
  source_file: hardware/SAO-adapter.kicad_pcb
  generated: '2026-09-07'
  bytes: 128684
---

DCZia's Mk9 is a wearable macropad built for DEF CON 34, continuing a badge series the group has run since forming around DEF CON 22. It packs nine real mechanical switches into a 3x3 grid on an RP2040, with a WS2812B RGB LED under every key and six SK6812 side-firing LEDs for underglow, plus an accelerometer that drives tilt- and shake-reactive lighting modes like a rainbow wave and a breathing pulse. Two SAO headers let it host add-ons, including a bundled expansion board that itself takes three more switches or an OLED. The badge ships as a partial kit — the buyer adds their own switches and battery box — and runs on USB-C or 3x AAA batteries.

It was sold through the Uberflux marketplace by maker "hamster" of Snurkle Engineering for $60, with USPS shipping or in-person DEF CON pickup; as of the research date the listing showed only 2 of an original 74 units left unsold. Firmware ships as CircuitPython/MicroPython with USB HID keyboard support out of the box, and the hardware is also QMK-compatible for anyone who wants to reflash it as a full-time input device after the con. DCZia describes the design as a callback to their earlier keygrid badge from 2018.

## Make your own

Hardware (KiCad schematics and PCB layout, fabrication outputs, BOM) and firmware are published at github.com/dczia/mk9-badge, with pinout and flashing documentation included in the repo. A CAD model is also shared on OnShape. No specific open-source license was stated in the sources checked, only that the group says it is "committed to open source hardware and software."

## History

The Mk9 is the latest in DCZia's annual DEF CON badge line, following the DC30 "30-in-1" educational badge, a DC31 electric sampler badge, DC32's badge, and DC33's "Zippy."
