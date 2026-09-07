---
title: Iron Gauntlet
id: dc27-dc27-iron-gauntlet-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/hacker/308303-twinkletwinkie
summary: A DEF CON 27 SAO by TwinkleTwinkie shaped like the Marvel Infinity Gauntlet, using seven 1204 side-view LEDs with a hot-glue diffuser to represent the six Infinity Stones, bundled exclusively with the maker's Arc Badge.
functions: 'Lights up the six Infinity Stones using seven side-view LEDs (yellow used two LEDs to match the others'' glow distance); no interactivity beyond illumination.'
look:
  colors: [gold, multicolor]
  shape: null
  themes: [movie, pop culture, jewelry]
tech:
  mcu: none
  leds:
    count: 7
    type: reverse-mount
    note: 1204-package side-view LEDs (red, orange, yellow x2, green, and one more; a planned purple RGB LED was swapped for a single pink LED due to a resistor-placement error) diffused with hot glue.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Bundled exclusively with the Arc Badge, which its Tindie listing marks as its final, now sold-out run (checked 2026-09-07).'
  distribution: [purchase]
  where: Bundled exclusively with TwinkleTwinkie's Arc Badge (DC27 indie badge), sold via Tindie; not sold separately.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  firmware_url: null
  gerbers_url: null
  bom_url: null
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: 'The project page offers a KiCad footprint library for the 1204 side-view LEDs (1204_SVLED.zip); full gerbers/schematics were not found published.'
links:
- label: hackaday.io/project/165322-iron-gauntlet-dc27-sao
  url: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  kind: hackaday
- label: hackaday.io/hacker/308303-twinkletwinkie
  url: https://hackaday.io/hacker/308303-twinkletwinkie
  kind: hackaday
- label: Arc Badge - DC27 Indie Badge (Tindie)
  url: https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
  kind: store
images:
- file: assets/images/badges/dc27/dc27-iron-gauntlet-sao/0506da0c77.jpg
  source: "https://hackaday.io/project/165322-iron-gauntlet-dc27-sao"
  credit: "TwinkleTwinkie"
  caption: "The Iron Gauntlet SAO, a DEF CON 27 accessory shaped like Marvel's Infinity Gauntlet"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  title: Iron Gauntlet - DC27 SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  title: Iron Gauntlet - DC27 SAO
  accessed: '2026-09-07'
  note: "Confirmed LED count/type (7x 1204 side-view LEDs), hot-glue diffuser technique, RGB->pink LED substitution due to a resistor error, and og:image photo of the item."
- kind: url
  url: https://hackaday.io/project/165322/files
  title: Files | Iron Gauntlet - DC27 SAO
  accessed: '2026-09-07'
  note: "Only a KiCad footprint library for the 1204 side-view LEDs is published; no gerbers/schematics/license found."
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
  title: Arc Badge - DC27 Indie Badge (Tindie)
  accessed: '2026-09-07'
  note: "Confirms the SAO was bundled exclusively with the Arc Badge (not sold separately), and that the Arc Badge's final run is sold out."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Could not confirm quantity made, a separate price, or a full open-source hardware/firmware release beyond the KiCad footprint file. TwinkleTwinkie's Hackaday.io hacker profile page could not be read directly (returned a login wall), so bio/other-projects details are not included here."
last_modified_date: '2026-09-07'
---

The Iron Gauntlet is a DEF CON 27 (2019) SAO by TwinkleTwinkie, shaped after Marvel's Infinity Gauntlet. It uses seven side-view LEDs in the 1204 package to stand in for the six Infinity Stones — yellow needed two LEDs to match the glow distance of the others — with the light diffused through a layer of hot glue rather than a milled or printed lens. The maker had originally planned an RGB LED to render purple, but a resistor placed on the wrong side of the LED kept that color from working, so a single pink LED was swapped in as a fix; the project notes a future revision was meant to correct it.

The SAO was never sold on its own. It shipped exclusively bundled with TwinkleTwinkie's Arc Badge, the maker's DC27 indie badge, sold through Tindie together with a lanyard and batteries. The Tindie listing describes that run as final, and as of this check the listing shows it sold out. A KiCad footprint library for the 1204 side-view LEDs is published on the project's Hackaday.io page, but no full gerber set, schematic, or firmware was found.
