---
title: Star Trek SAO Phaser v2.2
id: dc34-star-trek-sao-phaser-v2-2
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Hak4Kidz Lab
  url: https://www.tindie.com/stores/h4klab/
summary: 'A DIY-solder SAO shaped like a Star Trek: The Original Series type-2 phaser, with LEDs that light the barrel and a top "tracer" strip. Proceeds support the Hak4Kidz youth electronics nonprofit.'
functions: No onboard logic; lights up via coin-cell/host-badge power and a switch-free LED circuit (side-view and shine-down LEDs).
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
    note: Side-view/shine-down LEDs illuminate the barrel through the PCB, plus a visual tracer LED strip across the top; no switch (removed to reduce footprint).
  display: none
  connectivity: []
  battery: coin cell
  sao_version: v1.69bis
get_one:
  price: $30
  price_usd: 30.0
  quantity: 50 (per the DC31 listing for the same product)
  availability: unknown
  distribution:
  - purchase
  where: Sold via Tindie (Hak4Kidz Lab store); also listed on the DC34 community badge sheet at $35
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: youtube.com/shorts/N2FldDU5t80?feature=share
  url: https://youtube.com/shorts/N2FldDU5t80?feature=share
  kind: video
- label: x.com/hak4kidz
  url: https://x.com/hak4kidz
  kind: social
- label: linkedin.com/company/hak4kidz
  url: https://linkedin.com/company/hak4kidz
  kind: social
- label: tindie.com/products/h4klab/star-trek-sao-phaser-v22
  url: https://www.tindie.com/products/h4klab/star-trek-sao-phaser-v22/
  kind: store
images:
- file: assets/images/badges/dc34/star-trek-sao-phaser-v2-2/d2177b30f2.png
  source: https://www.tindie.com/products/h4klab/star-trek-sao-phaser-v22/
  credit: Hak4Kidz Lab
  caption: Star Trek SAO Phaser v2.2 with front tracer LED lit
contact:
  discord: healwhans
  emails:
  - healwhans@hak4kidz.com
notes:
- Tindie listing text says the product was 'Made for DC31'; the same item (same $30 price, same design) also appears on the DC31 community sheet as 'Star Trek Type 2 Phaser SAO' with a note of '50 available.' It looks like this is a recurring Tindie product that Hak4Kidz also brought to/listed for DC34, rather than a new DC34-specific design.
status: listed
sources:
- kind: sheet
  event: dc34
  row: 19
  updated: 6/16/2026 16:23:33
  listing: New
- kind: url
  url: https://www.tindie.com/products/h4klab/star-trek-sao-phaser-v22/
  title: Star Trek SAO Phaser v2.2 from Hak4Kidz Lab on Tindie
  accessed: '2026-09-06'
  note: Primary source for description, features, price ($30), SAO connector type, and product photos.
- kind: url
  url: https://youtube.com/shorts/N2FldDU5t80?feature=share
  title: Star Trek SAO Phaser v2.2 (YouTube Short)
  accessed: '2026-09-06'
  note: Video confirms title; no description/transcript text was retrievable, so it added no additional facts.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Maker page (Tindie) confirms the design, LED layout, SAO 1.69bis connector, and $30 price; the sheet listed $35, so both prices are recorded (price kept as sheet-listed $35 per the entry's existing get_one.price, with $30 noted from Tindie in notes — see get_one.where). No MCU/chip is used (passive LED SAO). Could not confirm exact LED count, quantity made specifically for DC34, or whether it was still in stock at the con. X/LinkedIn links returned no usable page content (X required login). This appears to be the same underlying product as dc31-star-trek-type-2-phaser-sao, sold/listed again for DC34 rather than a new design.
last_modified_date: '2026-09-06'
related:
- dc31-star-trek-type-2-phaser-sao
---

The Star Trek SAO Phaser v2.2 is a DIY-solder shortcut-and-add-on (SAO) shaped like the type-2 phaser from Star Trek: The Original Series, made by Hak4Kidz Lab, the badgelife arm of the Hak4Kidz youth electronics education nonprofit. It plugs into a standard SAO 1.69bis header or can be worn on its own as a pin. The board uses side-view and shine-down LEDs to light the barrel through the PCB and adds a "tracer" LED effect across the top of the phaser, with LF HASL finishing meant to give the board a more realistic prop look. The design removed a physical switch from the earlier version to keep the footprint small.

Per the maker's Tindie listing, v2.2 is "a huge upgrade" from a Star Trek Phaser v1 the studio made in 2019, and the color scheme changed from green to blue between versions. The listing itself says the board was "made for DC31" (DEF CON 31, 2023), and the DC31 community badge sheet independently lists what appears to be the same item ("Star Trek Type 2 Phaser SAO," $30, "50 available") — so this looks like the same Tindie product that Hak4Kidz continued to sell and also listed on the community sheet for DC34, rather than a new design created specifically for 2026. All proceeds are stated to support the Hak4Kidz mission.

No microcontroller is used; the board is a passive, battery/host-powered LED circuit. Open-source hardware/firmware files were not found during this research pass.
