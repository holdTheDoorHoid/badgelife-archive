---
title: Planet Express SAOship
id: other-planet-express-saoship
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 2019
makers:
- name: thelogicofpi
  url: https://hackaday.io/hacker/315117-thelogicofpi
summary: A Futurama Planet Express ship shaped desk/shelf display board that powers up to four SAO v1.69bis add-ons and blinks 32 LEDs in eleven selectable patterns, driven by an ATtiny85 and two MCP23017 I2C expanders on two AAA batteries.
functions: 'Holds and powers up to 4 SAO v1.69bis add-ons while driving 32 LEDs through eleven display modes (including all-on, flashing, alternating, binary counter, Knight Rider scanner, and random flashing); a power switch toggles between mode-selection and normal display.'
look:
  colors: []
  shape: spaceship
  themes:
  - sci-fi
  - space
  - tv
  - pop culture
tech:
  mcu: ATtiny85
  leds:
    count: 32
    type: discrete
    note: red, orange, yellow, and green LEDs driven via two MCP23017 I2C expanders
  display: null
  connectivity:
  - i2c
  battery: 2x AAA
  sao_version: v1.69bis
get_one:
  price: "$65"
  price_usd: 65
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold on Tindie by the maker's shop, PCB PINS; listed out of stock as of Feb 20, 2020.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/jeffwurz/Saoship
  eda_tool: null
links:
- label: hackaday.io/project/166236-planet-express-saoship
  url: https://hackaday.io/project/166236-planet-express-saoship
  kind: hackaday
- label: github.com/jeffwurz/Saoship
  url: https://github.com/jeffwurz/Saoship
  kind: repo
- label: youtu.be/PobDxoNRZ2U
  url: https://youtu.be/PobDxoNRZ2U
  kind: video
- label: tindie.com/products/thelogicofpi/planet-express-saoship
  url: https://www.tindie.com/products/thelogicofpi/planet-express-saoship/
  kind: store
images:
  - file: assets/images/badges/other/planet-express-saoship/1de36fe789.jpg
    source: "https://www.tindie.com/products/thelogicofpi/planet-express-saoship/"
    credit: "thelogicofpi (PCB PINS)"
    caption: "Planet Express SAOship board holding SAOs, LEDs lit"
  - file: assets/images/badges/other/planet-express-saoship/aba4dee5aa.jpg
    source: "https://hackaday.io/project/166236-planet-express-saoship"
    credit: "thelogicofpi"
    caption: "Planet Express SAOship, Futurama-themed SAO holder board"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/166236-planet-express-saoship
  title: Planet Express SAOship
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/166236-planet-express-saoship
  title: Planet Express SAOship
  accessed: '2026-09-07'
  note: Confirmed maker, date (June 24, 2019), chip, LED count, MCP23017 expanders, AAA battery power, and lighting modes.
- kind: url
  url: https://github.com/jeffwurz/Saoship
  title: jeffwurz/Saoship - LED drivers for SAOship
  accessed: '2026-09-07'
  note: Repo described as "led drivers for SAOship"; confirms firmware source is public, but README had no further hardware detail retrievable.
- kind: url
  url: https://www.tindie.com/products/thelogicofpi/planet-express-saoship/
  title: Planet Express SAOship from PCB PINS on Tindie
  accessed: '2026-09-07'
  note: Confirms price ($65), sold-out status since Feb 20 2020, shop name PCB PINS (Sacramento, CA), and provided the product photo used here.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a Futurama-themed accessory board (holds/displays other SAOs), not a badge worn at a specific conference, and no source ties it to a particular con — it reads as a general 2019 Tindie release by the maker's shop "PCB PINS" (thelogicofpi / jeffwurz). Left event as "other" since no con/year source was found; year 2019 is confirmed via the Hackaday.io project creation date. Quantity made is not stated anywhere found. The maker (Tindie shop thelogicofpi, aka PCB PINS) also sells several companion Futurama SAOs meant to plug into this board — see other_items_found.
last_modified_date: '2026-09-07'
---

The Planet Express SAOship is a Futurama-themed desk display designed by thelogicofpi (posting the project to Hackaday.io on June 24, 2019, and selling it through the Tindie shop PCB PINS). Shaped like the Planet Express delivery ship, the board is not itself worn as a conference badge but acts as a holder and light show for up to four "Shitty Add-On" (SAO v1.69bis) boards plugged into it. An ATtiny85 drives two MCP23017 I2C GPIO expanders that in turn control 32 red, orange, yellow, and green LEDs across eleven selectable patterns — all-on, flashing, alternating, a binary counter, a Knight Rider-style scanner, and random flashing among them — with a physical power switch used to toggle between pattern-selection and normal running modes. Power comes from two AAA batteries through an AMS1117 3.3V regulator.

The board was sold on Tindie for $65 and has been listed as out of stock since February 20, 2020; no source found states how many units were made. The firmware (LED driver code for the ATtiny85) is published on GitHub at jeffwurz/Saoship, though the hardware design files were not found published alongside it, so it is only partially open source. A demo video is posted to YouTube.

No source connects this board to a specific convention or year of a con; it appears to have been a standalone 2019 release rather than badge-sheet swag for a particular event, so it remains filed under "other."
