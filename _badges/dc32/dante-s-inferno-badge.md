---
title: Dante's Inferno Badge
id: dc32-dante-s-inferno-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: redactd
  url: https://www.tindie.com/stores/redactd/
summary: A DEF CON 32 electronic badge with two-color solder mask, 60 LEDs across three connected circuit boards, and a running joke that it "sends you to the world famous strip club."
functions: 'Blinky LED patterns across 60 onboard LEDs; has an SAO port for add-ons; maker describes a hidden "secret that connects you to another dimension."'
look:
  colors: []
  shape: null
  themes:
  - horror
  - wearable
tech:
  mcu: null
  leds:
    count: 60
    type: null
    note: 60 LEDs spread across three interconnected circuit boards
  display: null
  connectivity: []
  battery: CR123A
  sao_version: null
  sao_ports: 1
get_one:
  price: $100.00
  price_usd: 100.0
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing showed 1 unit remaining as of 2026-09-06; original sheet price was $200, later listed at $100.'
  distribution:
  - purchase
  where: Sold directly by the maker on Tindie.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/im-redactd/dantes_inferno/
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: 'GitHub repo exists for firmware/documentation but was mostly a "coming soon" placeholder as of 2026-09-06; it describes UF2-based firmware flashing (1200-baud reset into bootloader, drag-and-drop UF2 file, or a boot button under the acrylic pre-sale case) but does not name the MCU or publish hardware files.'
links:
- label: www.tindie.com/products/redactd/dantes-inferno-badge
  url: https://www.tindie.com/products/redactd/dantes-inferno-badge/
  kind: store
- label: github.com/im-redactd/dantes_inferno
  url: https://github.com/im-redactd/dantes_inferno/
  kind: repo
- label: x.com/boofintheface
  url: https://x.com/boofintheface
  kind: social
images:
  - file: assets/images/badges/dc32/dante-s-inferno-badge/520e732525.jpg
    source: "https://www.tindie.com/products/redactd/dantes-inferno-badge/"
    credit: "redactd"
    caption: "Dante's Inferno Badge, front view"
  - file: assets/images/badges/dc32/dante-s-inferno-badge/f0a85d5c09.jpg
    source: "https://www.tindie.com/products/redactd/dantes-inferno-badge/"
    credit: "redactd"
    caption: "Dante's Inferno Badge, alternate view"
contact: {}
notes:
- I do not know if it will be available at DC32 or not. The maker does discuss meeting the required timeline for shipping on tindie.
- Sheet listed price as $200.00; the maker's own Tindie listing shows $100.00 (checked 2026-09-06). Recorded the Tindie price as authoritative per the "prefer the maker's own words" rule.
status: released
sources:
- kind: sheet
  event: dc32
  row: 87
  updated: '2024-07-24'
- kind: url
  url: https://www.tindie.com/products/redactd/dantes-inferno-badge/
  title: Dante's Inferno Badge - Tindie
  accessed: '2026-09-06'
  note: Confirmed maker location, price ($100), LED count/board layout, battery, SAO port, packaging, stock level, and general description.
- kind: url
  url: https://github.com/im-redactd/dantes_inferno/
  title: im-redactd/dantes_inferno GitHub repo
  accessed: '2026-09-06'
  note: Firmware flashing instructions (UF2, 1200-baud reset, boot button); repo otherwise a placeholder, no MCU name or hardware files published as of this check.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Maker (Tindie/GitHub) confirms core facts (LEDs, boards, battery, SAO port, price). Could not confirm the MCU, LED type/part number, quantity made, colors/shape, open-source hardware files, or theme tags beyond a general horror/strip-club joke; GitHub repo is largely unpopulated. x.com/boofintheface could not be checked (site returned HTTP 402 to the fetch tool). Left those fields null/empty rather than guess.'
last_modified_date: '2026-09-06'
---

The Dante's Inferno Badge is an electronic badge redactd sold for DEF CON 32 (2024), named as a joke after the Dante's Inferno strip club rather than the poem. It is built from three interconnected circuit boards carrying 60 LEDs in a two-color solder mask finish, runs off a single CR123A battery, and includes an SAO port so it can host other badgelife add-ons. The maker's listing hints at a hidden "secret that connects you to another dimension" without spelling out what that is.

It was sold directly through the maker's Tindie store for $100 (the community sheet had recorded an earlier $200 asking price), packaged with custom full-color printed packaging, a laser-cut foam insert, and a matching lanyard; Tindie showed only a single unit left in stock when checked. A companion GitHub repository was set up to host firmware and documentation, and describes how to reflash the badge over USB (drag-and-drop a UF2 file after a 1200-baud serial reset, or hold a boot button on pre-sale acrylic-cased units), but as of this check the repo's substantive content was still a placeholder — no microcontroller name, license, or hardware design files were published.
