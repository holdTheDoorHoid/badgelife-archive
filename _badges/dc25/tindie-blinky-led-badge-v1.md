---
title: Tindie Blinky LED Badge v1
id: dc25-tindie-blinky-led-badge-v1
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc25
year: 2017
makers:
- name: Jasmine Brackett, Shulie Tornel
summary: A lapel-pin badge shaped like the Tindie mascot's head, with two flashing LED "eyes," designed and produced in about two weeks for distribution at DEF CON 25 (2017).
functions: No interactivity beyond the two flashing LED eyes; a simple always-on blinky circuit run off a coin cell.
look:
  colors:
  - black
  shape: mascot head
  themes:
  - mascot
  - robot
  - wearable
  - pin
  - learn to solder
tech:
  mcu: none
  leds:
    count: 2
    type: RGB
    note: 5mm flashing/multicolor LEDs wired as the mascot's eyes, no current-limiting resistors
  display: none
  connectivity: []
  battery: CR1220
  sao_version: none
get_one:
  price: $1.80 (approximate unit cost)
  price_usd: 1.8
  quantity: 300 (initial DEF CON 25 batch); Hackaday.io notes over 2,000 units produced across later versions
  availability: free
  distribution:
  - free_drop
  - village
  where: Given away at the Hardware Hacking Village at DEF CON 25; later versions distributed as a "learn to solder" kit.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/26056-tindie-blinky-led-badge
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/26056-tindie-blinky-led-badge-v1
  url: https://hackaday.io/project/26056-tindie-blinky-led-badge-v1
  kind: hackaday
- label: hackaday.com/2017/07/27/building-a-def-con-badge-in-two-weeks
  url: https://hackaday.com/2017/07/27/building-a-def-con-badge-in-two-weeks/
  kind: article
- label: hackaday.io/project/26056-tindie-blinky-led-badge
  url: https://hackaday.io/project/26056-tindie-blinky-led-badge
  kind: hackaday
images:
- file: assets/images/badges/dc25/tindie-blinky-led-badge-v1/49fe720540.jpg
  source: https://hackaday.io/project/26056-tindie-blinky-led-badge
  credit: Tindie / Hackaday.io project 26056
  caption: Tindie Blinky LED Badge lapel pin with illuminated eyes
contact: {}
notes:
- Solder-it-yourself blinky kit featuring the Tindie mascot Ohm, distributed around DEF CON 25. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task dc25-saos.
- Lapel-pin-style coin-cell badge shaped like the Hackaday robodog mascot's head, designed in under two weeks and given out 300-strong at the Hardware Hacking Village. Found by the event-year sweep, task dc25-badges.
- The sweep titled this "Tindie/Hackaday Robodog Head Badge (a.k.a. Blinky LED Badge)"; the maker's own Hackaday.io project is titled "Tindie Blinky LED Badge" and the mascot is the Tindie head, not a "robodog" — title corrected accordingly.
- This appears to be the same project (Hackaday.io
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/26056-tindie-blinky-led-badge-v1
  title: Tindie Blinky LED Badge v1
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc25-saos); event read as ''dc25''.'
- kind: url
  url: https://hackaday.com/2017/07/27/building-a-def-con-badge-in-two-weeks/
  title: Tindie/Hackaday Robodog Head Badge (a.k.a. Blinky LED Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc25-badges); event read as ''dc25''.'
- kind: url
  url: https://hackaday.io/project/26056-tindie-blinky-led-badge
  title: Tindie Blinky LED Badge (Hackaday.io project 26056)
  accessed: '2026-09-08'
  note: Maker's own project page; confirms team, LEDs, battery, design files, and production numbers.
research:
  status: stub
  confidence: low
  last_checked: '2026-09-07'
  notes: Imported from the community badge sheet; not yet researched. Merged with duplicate entry 'Tindie Blinky LED Badge' (dc25-tindie-hackaday-robodog-head-badge-a-k-a-blinky-led-badge).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc25/tindie-hackaday-robodog-head-badge-a-k-a-blinky-led-badge/
---


## Notes merged from the duplicate entry "Tindie Blinky LED Badge"

The Tindie Blinky LED Badge started as a two-week scramble by Hackaday's Brian Benchoff, together with Jasmine Brackett and Brandon Rexius, to get a giveaway badge ready for DEF CON 25 in July 2017. It has no microcontroller: a CR1220 coin cell simply drives two 5mm flashing LEDs wired as the eyes of the Tindie mascot's head, with the head shape itself rendered through the PCB's silkscreen, soldermask, and copper layers rather than through an enclosure. The badge is small enough to wear as a lapel pin with a butterfly clutch back.

About 300 of the badges were assembled for the initial DEF CON 25 giveaway, handed out at the Hardware Hacking Village; Hackaday.io's project page for it later cites production well past 2,000 units across subsequent versions, suggesting the design was reused as a "learn to solder" kit for other events. Design files (a full panel layout and vector art for the head) are posted on the Hackaday.io project page, though a clear open-source license was not stated.

This entry was created by an automated sweep under the title "Tindie/Hackaday Robodog Head Badge," but the maker's own project is titled "Tindie Blinky LED Badge" and depicts the Tindie mascot's head rather than the Hackaday robodog — the title above has been corrected to match. The entry also appears to duplicate dc25-tindie-blinky-led-badge-v1, a separate stub created from the same Hackaday.io project (#26056) by a different sweep pass.
