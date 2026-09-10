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
- name: Brian Benchoff
  url: https://hackaday.io/benchoff
  role: design
- name: Jasmine Brackett
  url: https://hackaday.io/jasmine-brackett
  role: design
- name: Brandon Rexius
  url: https://hackaday.io/brandon-rexius
  role: instructions
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
- file: assets/images/badges/dc25/tindie-blinky-led-badge-v1/42e93741b3.png
  source: "https://hackaday.io/project/26056-tindie-blinky-led-badge-v1"
  credit: "Hackaday.io project 26056"
  caption: "Tindie Blinky LED Badge with flashing eye LEDs"
contact: {}
notes:
- Solder-it-yourself blinky kit featuring the Tindie mascot Ohm, distributed around DEF CON 25. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task dc25-saos.
- Lapel-pin-style coin-cell badge shaped like the Hackaday robodog mascot's head, designed in under two weeks and given out 300-strong at the Hardware Hacking Village. Found by the event-year sweep, task dc25-badges.
- The sweep titled this "Tindie/Hackaday Robodog Head Badge (a.k.a. Blinky LED Badge)"; the maker's own Hackaday.io project is titled "Tindie Blinky LED Badge" and the mascot is the Tindie head, not a "robodog" — title corrected accordingly.
- 'The original sweep listed makers as "Jasmine Brackett, Shulie Tornel." Neither the Hackaday.io project team list nor the Hackaday.com article mentions a "Shulie Tornel" — the confirmed team is Brian Benchoff, Jasmine Brackett, and Brandon Rexius (with Kaylee handling kit assembly and Joe Kim credited for artwork). Makers field corrected accordingly.'
- This is a distinct, earlier project from other-hackaday-blinky-led-badge (the 2018 "Jolly Wrencher" skull badge), which the maker's own project page describes as derived from this Tindie-head circuit — not a duplicate.
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
  accessed: '2026-09-10'
  note: Maker's own project page; confirms team (Tindie, Benchoff, Jasmine Brackett, Brandon Rexius), LEDs, battery, design files, and production numbers. Re-checked to verify the makers field.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Core facts (team, LEDs, battery, price, quantity, distribution) confirmed directly on the maker''s Hackaday.io project pages (both the v1-suffixed and base URLs) and the Hackaday.com article. Corrected the makers field, which the sweep had wrong (see notes). No stated open-source license for the design files, so make_your_own.open_source stays "partial." Could not confirm whether "Kaylee" (assembly) or "Joe Kim" (artwork) should be listed as makers or are better described as contributors; left out of the makers list since sources frame them as helping rather than designing.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/dc25/tindie-hackaday-robodog-head-badge-a-k-a-blinky-led-badge/
---


The Tindie Blinky LED Badge started as a two-week scramble by Hackaday's Brian Benchoff, together with Jasmine Brackett and Brandon Rexius, to get a giveaway badge ready for DEF CON 25 in July 2017. It has no microcontroller: a CR1220 coin cell simply drives two 5mm flashing LEDs wired as the eyes of the Tindie mascot's head, with the head shape itself rendered through the PCB's silkscreen, soldermask, and copper layers rather than through an enclosure. The badge is small enough to wear as a lapel pin with a butterfly clutch back.

About 300 of the badges were assembled for the initial DEF CON 25 giveaway, handed out at the Hardware Hacking Village; Hackaday.io's project page for it later cites production well past 2,000 units across subsequent versions, suggesting the design was reused as a "learn to solder" kit for other events. Design files (a full panel layout and vector art for the head) are posted on the Hackaday.io project page, though a clear open-source license was not stated.

This entry was originally created by an automated sweep under the title "Tindie/Hackaday Robodog Head Badge," and separately under the maker's actual title "Tindie Blinky LED Badge" by a second sweep pass; the two were duplicates of the same Hackaday.io project (#26056) and have been merged here under the maker's own title. A related but distinct 2018 badge, the Jolly-Wrencher-themed "Hackaday Blinky LED Badge" (`other-hackaday-blinky-led-badge`), reuses this circuit and is documented as a separate entry.

## Make your own

Design files are posted on the [Hackaday.io project page](https://hackaday.io/project/26056-tindie-blinky-led-badge): `FullBoard.zip` (the panel Gerbers), plus `TindieHead.ai` and `DiamondDog.ai` vector artwork for the head and decorative elements. No firmware is needed since the board has no microcontroller — the flashing/color-cycling behavior comes from the LEDs themselves. No open-source license is stated for the files.
