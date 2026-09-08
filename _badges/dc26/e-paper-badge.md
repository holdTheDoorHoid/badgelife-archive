---
title: E-Paper Badge
id: dc26-e-paper-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Drew Fustini
  url: https://github.com/pdp7
summary: A DIY name badge built around a Teensy LC and a 2.15" Pervasive Displays e-paper panel, with capacitive touch buttons to page through a gallery of images.
functions: Capacitive touch buttons let the wearer cycle through a set of images shown on the e-paper display, including a Hackaday Jolly Wrencher graphic.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - text
tech:
  mcu: Teensy LC
  leds: null
  display: 2.15" e-paper (Pervasive Displays E2215CS062)
  connectivity: []
  inputs:
  - touch
  battery: 3.7V 500mAh LiPo
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Personal project, worn by the maker; not sold. Design files are freely downloadable.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/pdp7/kicad-teensy-epaper
  firmware_url: https://github.com/pdp7/kicad-teensy-epaper
  eda_tool: KiCad
  license: Apache-2.0
  fab_url: https://oshpark.com/shared_projects/1CiimZcf
  notes: Repo also has an OSH Park shared-project link for ordering bare boards. Assembly notes warn that the trace between VIN and VUSB must be cut for battery operation.
links:
- label: hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3
  url: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  kind: article
- label: github.com/pdp7/kicad-teensy-epaper
  url: https://github.com/pdp7/kicad-teensy-epaper
  kind: repo
- label: blog.oshpark.com/2018/09/01/e-paper-badge-is-a-hint-at-great-things-to-come
  url: https://blog.oshpark.com/2018/09/01/e-paper-badge-is-a-hint-at-great-things-to-come/
  kind: article
- label: oshpark.com/shared_projects/1CiimZcf
  url: https://oshpark.com/shared_projects/1CiimZcf
  kind: fab
images:
- file: assets/images/badges/dc26/e-paper-badge/ab4874ba45.jpg
  source: "https://github.com/pdp7/kicad-teensy-epaper"
  credit: "Drew Fustini"
  caption: "Assembled E-Paper Badge with Teensy LC and 2.15\" e-paper display"
- file: assets/images/badges/dc26/e-paper-badge/4dcb409ca1.jpg
  source: "https://github.com/pdp7/kicad-teensy-epaper"
  credit: "Drew Fustini"
  caption: "Back of the E-Paper Badge showing the Teensy LC and battery connector"
contact: {}
notes:
- E-paper display based badge shown at DEF CON 26, per Hackaday's roundup vol.3. Found by the event-year sweep, task dc26-saos.
status: released
sources:
- kind: url
  url: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  title: E-Paper Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc26-saos); event read as ''dc26''.'
- kind: url
  url: https://github.com/pdp7/kicad-teensy-epaper
  title: 'GitHub - pdp7/kicad-teensy-epaper: E-Paper Badge with Teensy LC designed in KiCad'
  accessed: '2026-09-08'
  note: Maker's own repo; confirms Teensy LC + Pervasive Displays 2.15" e-paper, Apache-2.0 license, battery details, and source images.
- kind: url
  url: https://blog.oshpark.com/2018/09/01/e-paper-badge-is-a-hint-at-great-things-to-come/
  title: E-Paper Badge is a Hint at Great Things to Come
  accessed: '2026-09-08'
  note: Reprints the Hackaday coverage and confirms maker, event, and features.
- kind: url
  url: https://oshpark.com/shared_projects/1CiimZcf
  title: KiCad Teensy E-Paper Badge [0a40263] - OSH Park
  accessed: '2026-09-08'
  note: Confirms board dimensions and that it connects a Pervasive Displays 2.15" E-Paper (E2215CS062) to a Teensy LC (Teensy 3.2 also compatible).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own GitHub repo (pdp7/kicad-teensy-epaper) confirms the Hackaday sweep hit and adds full detail (chip, display part number, license, battery, images). This was Drew Fustini's personal badge worn to DEF CON 26's Hackaday meetup, not a mass-produced or sold item, so get_one fields are mostly left empty/unknown - it was never distributed. No price, quantity, or storefront found because none exists; it inspired the 2018 Open Hardware Summit collaborative badge at MIT but that is a separate project, not covered here.
last_modified_date: '2026-09-08'
---

Drew Fustini, a "Friend of Hackaday," designed the E-Paper Badge as his own name badge for DEF CON 26 in 2018. It pairs a Teensy LC microcontroller with a 2.15" Pervasive Displays e-paper panel (part E2215CS062), connected via a 34-position FPC connector, and a row of capacitive touch buttons along one edge that let the wearer flip through a small gallery of images - among them a Hackaday Jolly Wrencher logo. He showed it off at Hackaday's Breakfast at DEF CON meetup, where it was featured in the site's "All the Badges of DEF CON 26" roundup.

The badge is powered by a 3.7V 500mAh LiPo battery, with an assembly note that the trace between VIN and VUSB must be cut for battery operation to work correctly. It was a one-off personal build rather than something produced or sold in quantity, and there is no known price or distribution history. Its design did go on to inspire a related, larger collaborative badge project at the 2018 Open Hardware Summit at MIT, though that is a distinct build built by a different group.

## Make your own

The full KiCad hardware design is open source under the Apache-2.0 license at github.com/pdp7/kicad-teensy-epaper, including schematics, PCB layout, gerbers, a bill of materials, and build photos. A bare-board order can also be placed directly from the project's OSH Park shared-project page.
