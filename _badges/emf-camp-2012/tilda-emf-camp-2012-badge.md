---
title: TiLDA (EMF Camp 2012 badge)
id: emf-camp-2012-tilda-emf-camp-2012-badge
layout: badge
parent: EMF Camp 2012
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: emf-camp-2012
year: 2012
makers:
- name: Charles Yarnold
  role: designer
- name: EMF Camp / Electromagnetic Field
  role: organizer
  url: https://www.emfcamp.org
summary: TiLDA is the first EMF Camp attendee badge, a reprogrammable Arduino-compatible development board on a lanyard given to every attendee at the inaugural 2012 event.
functions: By default plays a networked game with the other badges on site to encourage attendees to meet people with differing interests; also communicates with site installations over its wireless and infrared links. Fully reprogrammable via the Arduino IDE, with spare I/O pins for personal projects.
look:
  colors: []
  shape: null
  themes:
  - wearable
  - hardware tool
tech:
  mcu: ATmega32U4
  leds:
    count: 2
    type: RGB
    note: two RGB LEDs
  display: none
  connectivity:
  - ir
  battery: LiPo, rechargeable via microUSB
  sao_version: none
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to every attendee on arrival at EMF Camp 2012; sponsored by the UCL Institute of Making.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/emfcamp/TiLDA
  firmware_url: https://github.com/emfcamp/TiLDA-source
  eda_tool: null
links:
- label: en.wikipedia.org/wiki/Electromagnetic_Field_(festival)
  url: https://en.wikipedia.org/wiki/Electromagnetic_Field_(festival)
  kind: website
- label: 'Revealing TiLDA, our camp badge! (EMF Camp blog, 2012-08-02)'
  url: https://blog.emfcamp.org/2012/08/02/revealing-tilda-our-camp-badge/
  kind: article
- label: emfcamp/TiLDA (hardware, schematics, docs)
  url: https://github.com/emfcamp/TiLDA
  kind: repo
images:
- file: assets/images/badges/emf-camp-2012/tilda-emf-camp-2012-badge/466891b41a.jpg
  source: "https://blog.emfcamp.org/2012/08/02/revealing-tilda-our-camp-badge/"
  credit: "EMF Camp / Charles Yarnold"
  caption: "TiLDA badge PCB, as revealed in the 2012 announcement post"
contact: {}
notes:
- Inaugural EMF badge; ATmega32U4-based, Arduino-compatible.
- 'Based on the Arduino-compatible "Vinciduino" board per the maker''s announcement.'
status: released
sources:
- kind: url
  url: https://en.wikipedia.org/wiki/Electromagnetic_Field_(festival)
  title: TiLDA (EMF Camp 2012 badge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''EMF Camp 2012''.'
- kind: url
  url: https://blog.emfcamp.org/2012/08/02/revealing-tilda-our-camp-badge/
  title: 'Revealing TiLDA, our camp badge!'
  accessed: '2026-09-07'
  note: Maker's own 2012 announcement post; source for designer, chip, LEDs, connectivity, battery, price/distribution, open-source status, and the badge PCB image.
- kind: url
  url: https://github.com/emfcamp/TiLDA
  title: emfcamp/TiLDA
  accessed: '2026-09-07'
  note: "Confirms the repo holds documentation, schematics and libraries for the badge, with firmware in a linked TiLDA-source submodule; supports open_source: yes."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Quantity made and an exact retail/BOM price were not stated anywhere found; badge was given free to attendees, so price/price_usd are left as free/null rather than guessed. No maker photo of the assembled/finished badge (only the pre-manufacture PCB layout image) was found as of this check.
last_modified_date: '2026-09-07'
---

TiLDA was the very first EMF Camp attendee badge, revealed on August 2, 2012, a few weeks before the inaugural event. Every attendee received one on arrival, hung on a lanyard. Sponsored by the UCL Institute of Making and designed by Charles Yarnold, the badge was built around an ATmega32U4 and based on the open-source, Arduino-compatible Vinciduino board, with two RGB LEDs, a single button, 2.4 GHz and infrared wireless links, and a rechargeable LiPo battery charged over microUSB.

By default TiLDA ran a networked game with the other badges on site meant to nudge attendees with different interests into talking to each other, and it could also talk to site installations over its wireless/IR links. It was fully reprogrammable through the standard Arduino IDE and left spare I/O pins free for attendees' own projects, with the explicit goal of giving people something they'd keep using after the camp rather than a badge that ends up in a drawer. It set the naming convention ("TiLDA") that EMF Camp's badge line carried forward through several later hardware generations.

## Make your own

Hardware documentation, schematics and libraries are published in the `emfcamp/TiLDA` GitHub repository, with example firmware in a linked `TiLDA-source` submodule; both were fully open-source per the original announcement.
