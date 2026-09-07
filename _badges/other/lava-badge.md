---
title: LAVA BADGE
id: other-lava-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: redactd (HCKBADGES)
summary: 'A pyramid-shaped wearable badge that runs a live fluid-simulation "lava" effect across 425 addressable LEDs behind laser-cut acrylic.'
functions: 'Real-time lava/fluid simulation with 9 animations and 27 color palettes; two capacitive touch pads (front face and back logo) for control; serial console over USB-C; battery monitoring with auto-dimming and a low-battery indicator.'
look:
  colors: []
  shape: pyramid
  themes:
  - sci-fi
tech:
  mcu: RP2350
  leds:
    count: 425
    type: null
    note: 17 x 31 addressable LED array arranged behind laser-cut acrylic in a pyramid layout
  display: none
  connectivity:
  - usb
  battery: CR123A with USB-C charging
  sao_version: null
  inputs:
  - touch
get_one:
  price: "$100 badge only / $105 with battery"
  price_usd: 100
  quantity: ''
  availability: limited
  availability_note: 'As of 2026-09-06, Uberflux listed 4 remaining of the base badge and 4 remaining with battery, described as a "pre DC sale" ending the following Monday.'
  distribution:
  - purchase
  where: Sold directly by redactd through the Uberflux storefront.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/RDCTD-LAVA
  url: https://uberflux.com/product/RDCTD-LAVA
  kind: store
images:
  - file: assets/images/badges/other/lava-badge/1b2fd64350.jpg
    source: "https://uberflux.com/product/RDCTD-LAVA"
    credit: "redactd"
    caption: "LAVA BADGE pyramid-shaped badge with LED lava effect"
  - file: assets/images/badges/other/lava-badge/225e272f88.jpg
    source: "https://uberflux.com/product/RDCTD-LAVA"
    credit: "redactd"
    caption: "LAVA BADGE alternate view"
contact: {}
notes:
- 'Uberflux. $105, status: ships.'
status: listed
sources:
- kind: url
  url: https://uberflux.com/product/RDCTD-LAVA
  title: LAVA BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/RDCTD-LAVA
  title: LAVA BADGE product page
  accessed: '2026-09-07'
  note: 'Confirmed maker, specs (RP2350, 425 LEDs, touch pads, CR123A + USB-C), price, and remaining stock. Product images pulled from this page.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The maker (redactd) is a known DEF CON badge maker, and the store page describes this as a "pre DC sale," but the page gives no explicit event/year (no "DEF CON 33/34" or "2025/2026" text found), and the pre-sale framing does not clearly match the access date (after DEF CON 34, Aug 2026), so event is left as "other" rather than guessed. Firmware/hardware repo is referenced as "coming soon" but no link was published at time of research. No design files, LED part number, or exact quantity made were stated.'
last_modified_date: '2026-09-07'
---

LAVA BADGE is a pyramid-shaped wearable badge by redactd (of HCKBADGES), built around an RP2350 microcontroller driving 425 addressable LEDs arranged in a 17x31 array behind laser-cut acrylic. The effect is a live fluid/lava simulation rather than fixed animation, with 9 animation modes and 27 color palettes selectable through two capacitive touch pads — one on the front face, one on the back logo.

The badge is powered by a CR123A battery with USB-C charging, and includes battery-level monitoring that dims the display and shows a low-battery warning. A serial console is exposed over USB-C, and the maker's listing notes a firmware repository "coming soon," though no link had been published as of research.

It was sold directly by redactd through the Uberflux storefront as a limited "pre DC sale," priced at $100 for the badge alone or $105 with a battery included, with only a handful of units remaining at last check. The listing did not state which specific DEF CON (or other event) year the badge was made for, so the event here is left unassigned pending a clearer source.
