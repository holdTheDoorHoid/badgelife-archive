---
title: Star Trek Type 2 Phaser SAO
id: dc31-star-trek-type-2-phaser-sao
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Hak4Kidz Lab
  url: https://www.tindie.com/stores/h4klab/
summary: 'A DIY-solder SAO shaped like a Star Trek: The Original Series type-2 phaser, with LEDs that light the barrel and a top "tracer" strip. Proceeds support the Hak4Kidz youth electronics nonprofit.'
functions: No onboard logic; lights up via coin-cell/host-badge power with side-view and shine-down LEDs (no switch).
look:
  colors:
  - blue
  shape: phaser
  themes:
  - sci-fi
  - tv
  - pop culture
  - learn to solder
tech:
  mcu: none
  leds:
    count: null
    type: reverse-mount
    note: Side-view/shine-down LEDs illuminate the barrel through the PCB, plus a visual "tracer" LED strip across the top; no switch (removed to reduce footprint).
  display: none
  connectivity: []
  battery: coin cell
  sao_version: v1.69bis
get_one:
  price: $30.00
  price_usd: 30.0
  quantity: '50'
  availability: unknown
  distribution:
  - purchase
  where: Sold via Tindie (Hak4Kidz Lab store); the DC31 community sheet listed it at $30 with "50 available (assembly to start soon)"
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: tindie.com/products/h4klab/star-trek-sao-phaser-v22
  url: https://www.tindie.com/products/h4klab/star-trek-sao-phaser-v22/
  kind: store
images:
- file: assets/images/badges/dc31/star-trek-type-2-phaser-sao/d2177b30f2.png
  source: https://www.tindie.com/products/h4klab/star-trek-sao-phaser-v22/
  credit: Hak4Kidz Lab
  caption: Star Trek Type 2 Phaser SAO with front tracer LED lit
contact:
  discord: healwhans
  emails:
  - healwhans@hak4kidz.com
notes:
- This appears to be the same underlying Tindie product later re-listed for DC34 as 'Star Trek SAO Phaser v2.2' (see dc34-star-trek-sao-phaser-v2-2). The Tindie listing itself states the board was 'made for DC31,' and the DC31 community sheet's price ($30) and description match the Tindie listing exactly, while the DC34 sheet listed it at $35.
status: listed
sources:
- kind: sheet
  event: dc31
  row: 52
  updated: '2023-07-21'
- kind: url
  url: https://www.tindie.com/products/h4klab/star-trek-sao-phaser-v22/
  title: Star Trek SAO Phaser v2.2 from Hak4Kidz Lab on Tindie
  accessed: '2026-09-06'
  note: Primary source; confirms maker, SAO 1.69bis connector, LED layout, price, "made for DC31" origin, and product photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Identified via the dc34 entry for the same product line (dc34-star-trek-sao-phaser-v2-2), whose Tindie listing states the board was "made for DC31." The DC31 sheet's price ($30) and "50 available" note match the Tindie listing. Could not confirm exact LED count, whether the DC31 units were the v2 or v2.2 revision specifically, or final DC31 sell-through/availability. No open-source hardware/firmware files were found. Duplicate of the same product as dc34-star-trek-sao-phaser-v2-2.
last_modified_date: '2026-09-06'
related:
- dc34-star-trek-sao-phaser-v2-2
---

The Star Trek Type 2 Phaser SAO is a DIY-solder shortcut-and-add-on shaped like the type-2 phaser from Star Trek: The Original Series, made by Hak4Kidz Lab, the badgelife arm of the Hak4Kidz youth electronics education nonprofit. It plugs into a standard SAO 1.69bis header (or can stand alone as a pin) and uses side-view and shine-down LEDs to light the barrel through the PCB, plus a "tracer" LED effect across the top. There is no onboard microcontroller — it is a passive, battery/host-powered LED circuit — and proceeds support the Hak4Kidz mission of teaching kids electronics.

The DC31 community badge sheet listed the item at $30 with "50 available (assembly to start soon)," matching the price and description on Hak4Kidz Lab's Tindie storefront listing for the "Star Trek SAO Phaser v2.2," which itself states the board was "made for DC31" (2023). The same product was later also listed on the DC34 (2026) community sheet, suggesting Hak4Kidz has continued selling and re-listing this design at successive DEF CONs rather than producing a new one each year.

No open-source hardware or firmware files were located for this design during research.
