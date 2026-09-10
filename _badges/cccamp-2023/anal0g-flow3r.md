---
title: anal0g flow3r
id: cccamp-2023-anal0g-flow3r
layout: badge
parent: Chaos Communication Camp 2023
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: cccamp-2023
year: 2023
makers:
- name: wenzellabs
  url: https://wenzellabs.de/
summary: A solder-it-yourself tribute to the 2023 CCCamp "flow3r" badge, built as a purely analog 5-stage ring oscillator in a five-petal flower shape.
functions: 'No microcontroller: a 5-stage analog ring oscillator (BC547B transistors, capacitors, resistors) drives one amber LED per petal, each slowly fading up, fading down, and passing the light to its neighbor in sequence.'
look:
  colors:
  - purple
  shape: floral
  themes:
  - floral
  - nature
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 5
    type: discrete
    note: amber LEDs, one per petal, driven directly by the analog oscillator stages (no driver IC)
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: $13.98 (volume discount $11.88 at 10+)
  price_usd: 13.98
  quantity: ''
  availability: available
  availability_note: 'Lectronz listing showed "Stock available: 10" as of 2026-09-10.'
  distribution:
  - purchase
  - kit
  where: Sold as a soldering kit through the maker's Lectronz store; includes PCB, components, CR2032 battery, slide switch, and a choice of lanyard color.
make_your_own:
  open_source: yes
  hardware_url: https://codeberg.org/wenzellabs/anal0g_flow3r
  firmware_url: null
  eda_tool: KiCad
  license: CERN-OHL-S-2.0
  notes: Hardware (KiCad schematics/PCB) and an assembly guide are published on Codeberg (mirrored to GitHub); there is no firmware since the circuit is purely analog.
links:
- label: codeberg.org/wenzellabs/anal0g_flow3r
  url: https://codeberg.org/wenzellabs/anal0g_flow3r
  kind: website
- label: github.com/wenzellabs/anal0g_flow3r
  url: https://github.com/wenzellabs/anal0g_flow3r
  kind: repo
- label: lectronz.com/products/anal0g-flow3r
  url: https://lectronz.com/products/anal0g-flow3r
  kind: store
- label: wenzellabs.de
  url: https://wenzellabs.de/
  kind: website
images:
  - file: assets/images/badges/cccamp-2023/anal0g-flow3r/1d6039f1d1.jpg
    source: "https://codeberg.org/wenzellabs/anal0g_flow3r"
    credit: "wenzellabs"
    caption: "anal0g flow3r front, purple flower-shaped PCB with 5 amber LED petals"
  - file: assets/images/badges/cccamp-2023/anal0g-flow3r/870dec274e.jpg
    source: "https://codeberg.org/wenzellabs/anal0g_flow3r"
    credit: "wenzellabs"
    caption: "anal0g flow3r animated: LEDs pulsing sequentially around the petals"
contact: {}
notes:
- Confirmed via the maker's own Codeberg repo and Lectronz storefront (the original sweep saw only a search snippet).
status: released
sources:
- kind: url
  url: https://codeberg.org/wenzellabs/anal0g_flow3r
  title: anal0g flow3r
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:cccamp); event read as ''Chaos Communication Camp 2023''.'
- kind: url
  url: https://codeberg.org/wenzellabs/anal0g_flow3r
  title: wenzellabs/anal0g_flow3r on Codeberg
  accessed: '2026-09-10'
  note: Maker's repo — confirms description, no-MCU analog oscillator design, components, CR2032 power, CERN-OHL-S license, and images (front/back photos and animated GIF).
- kind: url
  url: https://lectronz.com/products/anal0g-flow3r
  title: anal0g flow3r by wenzellabs - Lectronz
  accessed: '2026-09-10'
  note: 'Maker''s storefront — confirms it is a tribute to the 2023 CCCamp flow3r badge, price ($13.98, $11.88 at 10+), kit contents (PCB, components, CR2032, lanyard color choices), and stock (10 available).'
- kind: url
  url: https://wenzellabs.de/
  title: wenzellabs - HW / SW / FW dev & own products
  accessed: '2026-09-10'
  note: Maker's own site, confirms wenzellabs (Matthias Wenzel) as the identity behind the project.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Core facts (maker, purpose as a flow3r tribute, no-MCU analog design, open-source hardware, price/stock) confirmed directly on the maker's own repo and store page. Exact total production quantity was not stated anywhere found; only live stock count was available.
last_modified_date: '2026-09-10'
---

The anal0g flow3r is a solder-it-yourself tribute to the official 2023 Chaos Communication Camp badge, "flow3r," made by wenzellabs (Matthias Wenzel). Rather than reproducing that badge's microcontroller-driven synth and display, the anal0g flow3r strips the idea down to a purely analog circuit: a 5-stage ring oscillator built from BC547B transistors, capacitors, and resistors, laid out on a purple PCB shaped like a five-petaled flower. Each petal carries one amber LED that slowly brightens, dims, and hands the light off to its neighbor, producing a continuous chase-and-fade effect with no code involved.

It ships as a soldering kit — PCB, all passive and active components, a slide switch, CR2032 battery and holder, plus a choice of lanyard color (black, purple, neon green, or grey) — sold through the maker's Lectronz store for $13.98 (discounted to $11.88 at ten or more). The hardware design, including KiCad source files and an assembly guide, is published on Codeberg (mirrored to GitHub) under the CERN Open Hardware Licence v2 - Strongly Reciprocal; since the circuit is fully analog there is no firmware to publish.

## Make your own

The KiCad schematic and PCB layout, plus a PDF assembly guide, are available in the project's Codeberg repository (`doc/en_assembly_guide_anal0g_flow3r.pdf`) under an open hardware license, making it straightforward to fabricate and build your own copy.
