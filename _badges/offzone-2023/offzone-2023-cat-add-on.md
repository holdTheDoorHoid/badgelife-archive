---
title: OFFZONE 2023 Cat add-on
id: offzone-2023-offzone-2023-cat-add-on
layout: badge
parent: OFFZONE 2023
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2023
year: 2023
makers:
- name: BI.ZONE / Craft.Zone
summary: A cat-shaped SAO add-on for OFFZONE 2023, built as a two-board set — a main body board and a separate blue-LED "eyeset" board that plugs on top of it.
functions: Lights up with three red 1206 LEDs on the main board plus a blue 1206 LED on the eyeset board wired as the cat's eye.
look:
  colors:
  - white
  - blue
  shape: cat
  themes:
  - cat
  - animal
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: 3x red 1206 LEDs on the main board, 1x blue 1206 LED on the separate cat_eyeset board
  display: null
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2023/cat_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bi-zone/offzone-hw/tree/master/2023/cat_addon
  url: https://github.com/bi-zone/offzone-hw/tree/master/2023/cat_addon
  kind: repo
- label: habr.com/ru/companies/bizone/news/737540
  url: https://habr.com/ru/companies/bizone/news/737540/
  kind: website
images:
  - file: assets/images/badges/offzone-2023/offzone-2023-cat-add-on/17bf08de89.jpg
    source: "https://github.com/bi-zone/offzone-hw/tree/master/2023/cat_addon"
    credit: "BI.ZONE"
    caption: "Assembled cat add-on, front, showing eye LEDs"
  - file: assets/images/badges/offzone-2023/offzone-2023-cat-add-on/5553784a0f.jpg
    source: "https://github.com/bi-zone/offzone-hw/tree/master/2023/cat_addon"
    credit: "BI.ZONE"
    caption: "Assembled cat add-on, back, showing PLD-4 connector"
contact: {}
notes:
- Cat-themed add-on board for the OFFZONE 2023 badge, from BI.ZONE's Craft.Zone add-on contest. Found by the event-year sweep, task con-phdays.
- 'The sweep''s notes described the Habr article as being about this specific add-on; the article it linked is actually BI.ZONE''s general call for Craft.Zone add-on contest entries (deadline June 26, 5x5cm max, 100mA/3.3V, I2C, single/double-sided PCB) and does not name or picture the cat add-on itself.'
status: listed
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2023/cat_addon
  title: OFFZONE 2023 Cat add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2023''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2023/cat_addon
  title: cat_addon — bi-zone/offzone-hw
  accessed: '2026-09-08'
  note: 'Repo default branch is master, not main; confirmed the folder contents (README, KiCad source, Gerbers, BOM, preview image, cat_eyeset sub-board).'
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/2023/cat_addon/README.md
  title: cat_addon README
  accessed: '2026-09-08'
  note: 'Assembly instructions and BOM: 2-layer FR4 board, white soldermask on the main board, blue soldermask on the cat_eyeset sub-board; 3x red 1206 LEDs + 3x 220-ohm resistors + PLD-4 connector on the main board, 1x blue 1206 LED + 1x 220-ohm resistor + PLD-4 connector on the eyeset board.'
- kind: url
  url: https://habr.com/ru/companies/bizone/news/737540/
  title: BI.ZONE Craft.Zone add-on contest announcement (Habr)
  accessed: '2026-09-08'
  note: 'This is the general contest call-for-entries, not coverage of this specific add-on; it gives the contest''s technical constraints (max 5x5cm, 100mA at 3.3V, I2C interface, Gerber submission) that entries like this one had to meet.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, built board via the maker''s own repo (KiCad source, Gerbers, BOM, README with assembly steps and photos) — not just a search snippet. No maker statement was found on price, quantity made, or how/whether it was distributed to attendees; treated as a contest entry rather than a mass-distributed badge since it came out of the Craft.Zone add-on contest. No MCU is on the board itself — it is a passive LED add-on wired via I2C to the host OFFZONE 2023 badge, matching the contest''s stated interface. Could not confirm whether "BI.ZONE / Craft.Zone" or an individual contestant is the actual designer; the repo is BI.ZONE''s official OFFZONE hardware archive but this could be a submitted community entry archived there.'
last_modified_date: '2026-09-08'
---

The cat add-on is a small SAO built for OFFZONE 2023's Craft.Zone add-on contest, in which BI.ZONE invited attendees to design their own custom add-ons (max 5x5 cm, 3.3 V, 100 mA, I2C) for the con's badge. It ships as two boards: a white-soldermask main body carrying three red 1206 LEDs, and a separate blue-soldermask "cat_eyeset" board carrying a single blue 1206 LED that solders on top of a plastic spacer to form the cat's eye. Both boards are 2-layer FR4, 1.5 mm thick, and connect to the host badge through a PLD-4 connector.

Hardware is fully open — the maker's `offzone-hw` GitHub repository (BI.ZONE's public archive of OFFZONE hardware) includes the KiCad schematic and PCB source, Gerbers, a BOM, and a short assembly guide with build photos. No MCU is fitted; the board is a passive, LED-only accessory that draws power and I2C from the badge it plugs into.

What isn't documented anywhere the sweep or this pass could find is who specifically designed it, whether it won the contest, how many were made, or whether it was ever handed out beyond the contest context — the repo and BOM cover fabrication and assembly only.
