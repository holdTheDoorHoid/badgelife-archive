---
title: Han SAOlo
id: supercon-2024-han-saolo
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://hackaday.io/hacker/3459-davedarko
summary: A Star Wars-themed Simple Add-On depicting Han Solo frozen in carbonite, drawn in a dimetric 45-degree style with exposed HASL copper as the artwork and silkscreen for a 3D effect, driven by an ATtiny412 with five SK6805 RGB LEDs playing a carbonite-defreezing animation; submitted to the Supercon 8 SAO Contest.
functions: Five addressable RGB LEDs run a scheduled animation that mimics the Return of the Jedi carbonite-defrosting scene; the black solder mask over the LEDs gives Han's face a glowing effect when lit.
look:
  colors:
  - black
  - copper
  shape: rectangle
  themes:
  - movie
  - sci-fi
  - pop culture
tech:
  mcu: ATtiny412
  leds:
    count: 5
    type: SK6805-EC3210R
    note: Silkscreen and black solder mask make the LEDs glow through Han's carbonite-encased face.
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: v2
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SoloCarbonite
  firmware_url: null
  eda_tool: null
get_one:
  price: ''
  price_usd: null
  quantity: ~30
  availability: sold_out
  availability_note: Hand-assembled batch of about 30 given away at Supercon 8 (2024); checked 2026-09-07, no ongoing sale found.
  distribution:
  - contest
  - free_drop
  where: Distributed in person at Supercon 8 as part of the Supercon 8 SAO Contest; sponsored and fully assembled by JLCPCB.
links:
- label: hackaday.io/project/197803-han-saolo
  url: https://hackaday.io/project/197803-han-saolo
  kind: hackaday
  archived: https://web.archive.org/web/20260311225117/https://hackaday.io/project/197803-han-saolo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/SoloCarbonite
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SoloCarbonite
  kind: repo
images:
- file: assets/images/badges/supercon-2024/han-saolo/40249f99d2.jpg
  source: https://hackaday.io/project/197803-han-saolo
  credit: davedarko
  caption: 'Han SAOlo front and back: exposed-copper carbonite artwork and the ATtiny412/SK6805 PCB'
  archived: https://web.archive.org/web/20260311225117/https://hackaday.io/project/197803-han-saolo
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197803-han-saolo
  title: Han SAOlo
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260311225117/https://hackaday.io/project/197803-han-saolo
- kind: url
  url: https://hackaday.io/project/197803-han-saolo
  title: Han SAOlo
  accessed: '2026-09-07'
  note: 'Maker''s Hackaday.io project page: confirms Supercon 8 SAO Contest, ATtiny412, 5x SK6805-EC3210R LEDs, ~30 units hand-assembled and sponsored/populated by JLCPCB, described as the most popular SAO given away at the event.'
  archived: https://web.archive.org/web/20260311225117/https://hackaday.io/project/197803-han-saolo
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SoloCarbonite
  title: Simple-Add-ons-SAO / SoloCarbonite
  accessed: '2026-09-07'
  note: Repo folder holding the project writeup; confirmed design files live here, but no KiCad/Gerber files were visible in the folder listing itself.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/SoloCarbonite/2411_Hans_SAOLO.md
  title: Hans SAOLO (repo writeup)
  accessed: '2026-09-07'
  note: Maker's short writeup; says the blinking is done "thanks to the help of an Attiny13", which conflicts with the ATtiny412 named on the Hackaday.io page and silkscreened on the PCB photo. Treated as an early/loose draft; ATtiny412 is used in tech.mcu since it is confirmed by both the Hackaday page and the board photo itself.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (event, maker, MCU, LED count/type, connector, ~30 units, JLCPCB sponsorship) confirmed by the maker's own Hackaday.io project page and by a photo of the physical board. The repo's short writeup names an ATtiny13 instead of ATtiny412 for the blinking logic -- likely a stale/imprecise note, since the board silkscreen in the photo reads "AT-ATtiny412". Price was never advertised since this was a contest giveaway, not a sale, so get_one.price is left empty. No separate firmware or Gerber files were found in the linked repo folder beyond the writeup markdown, so firmware_url is left null and open_source is "partial".
last_modified_date: '2026-09-07'
---

Han SAOlo is a Simple Add-On (SAO) that recreates Han Solo frozen in carbonite from *Return of the Jedi*, made by davedarko (hackaday.io/hacker/3459-davedarko) for the Supercon 8 SAO Contest in November 2024. The artwork exploits exposed, tinned HASL copper for the carbonite block's rough metallic texture, laid out in a dimetric 45-degree perspective with silkscreen adding shading and depth. A black solder mask sits over Han's face so that, when the board's five SK6805-EC3210R addressable RGB LEDs run their animation, his face appears to glow -- referencing the on-screen defrosting scene. An ATtiny412 drives the LED sequencing, and the board carries an IIC/QWIIC-style header alongside the usual SAO connector, since a standard IDC header didn't fit the board's dimensions.

About 30 units were hand-assembled, with JLCPCB sponsoring and fully populating the boards, and handed out at Supercon; the maker's project page describes it as the most popular SAO given away there. Design files are hosted in davedarko's Simple-Add-ons-SAO GitHub repository under the SoloCarbonite folder, alongside a short build writeup, though no separate Gerber or firmware source files were found there at the time of this research.
