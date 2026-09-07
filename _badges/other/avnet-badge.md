---
title: Avnet Badge
id: other-avnet-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2019
makers:
- name: Avnet
  url: https://hackaday.io/project/167164-avnet-badge
  role: 'Natalia and Abraham (project team)'
summary: An LED badge showing the Avnet logo, built as a soldering-challenge project with a push-button-controlled light-mode cycle.
functions: 'Push button cycles through several LED lighting/animation modes.'
look:
  colors: []
  shape: logo
  themes:
  - logo
tech:
  mcu: ATtiny85-20SU
  leds:
    count: 5
    type: reverse-mount
    note: One LED required an added NTR2101P P-channel MOSFET to work around current limitations on the reset pin.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Prototype built for an Avnet-run soldering challenge at Jalisco Maker Faire, Nov 2019; page notes Avnet employees interested in a board could contact the team directly.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/167164-avnet-badge
  url: https://hackaday.io/project/167164-avnet-badge
  kind: hackaday
images:
- file: assets/images/badges/other/avnet-badge/930c7ec450.png
  source: "https://hackaday.io/project/167164-avnet-badge"
  credit: "Natalia and Abraham (Avnet)"
  caption: "Avnet Badge PCB with LEDs"
- file: assets/images/badges/other/avnet-badge/afdfd2fda9.png
  source: "https://hackaday.io/project/167164-avnet-badge"
  credit: "Natalia and Abraham (Avnet)"
  caption: "Avnet Badge assembly detail"
contact: {}
notes:
- "Made for a soldering challenge at Jalisco Maker Faire (Guadalajara, Mexico), November 2019 -- no matching event id exists in events.yml, so event is left as 'other'."
status: released
sources:
- kind: url
  url: https://hackaday.io/project/167164-avnet-badge
  title: Avnet Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/167164-avnet-badge
  title: Avnet Badge
  accessed: '2026-09-07'
  note: 'Maker''s own Hackaday.io project page: confirms makers (Natalia and Abraham), Jalisco Maker Faire soldering-challenge context (Nov 2019), ATtiny85-20SU MCU, 5 LEDs (reverse-mount, one needing an added NTR2101P MOSFET), CR2032 power, push-button mode cycling, and KiCad/Inkscape/svg2mod design tools. Two gallery photos saved.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found is the maker''s own Hackaday.io project page (no independent corroboration; web search budget was exhausted before a second search could be run). No price, quantity, or public hardware/firmware repo links are given on the page, so those fields are left empty. No event id in events.yml matches "Jalisco Maker Faire"; event kept as other.'
last_modified_date: '2026-09-07'
---

The Avnet Badge is a small LED badge built around an ATtiny85-20SU microcontroller, made by Natalia and Abraham as a soldering-challenge project for an Avnet-run activity at the Jalisco Maker Faire in Guadalajara, Mexico, in November 2019. The board lights up an Avnet-logo arrangement of five LEDs, some of them reverse-mounted, and a push button lets the wearer cycle through different lighting modes. It runs off a single CR2032 coin cell.

The team designed the board in KiCad (with artwork from Inkscape converted via the svg2mod script) and documented a hardware hiccup on their Hackaday.io page: current limits on the ATtiny85's reset pin meant one LED needed an added NTR2101P P-channel MOSFET to drive properly. The project page does not list a price, production quantity, or a public repository for the hardware or firmware; it mentions that Avnet employees interested in a board could contact the team directly, suggesting distribution was informal and limited to participants and staff of the soldering event rather than a general public release.
