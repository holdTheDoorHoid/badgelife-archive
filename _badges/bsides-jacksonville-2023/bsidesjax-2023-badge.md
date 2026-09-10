---
title: BSidesJAX 2023 Badge
id: bsides-jacksonville-2023-bsidesjax-2023-badge
layout: badge
parent: BSides Jacksonville 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-jacksonville-2023
year: 2023
makers:
- name: Panda (@hacksbearywell)
  url: https://github.com/blackandwhitehat
summary: The 2023 BSidesJAX attendee badge, a purple PCB badge etched with a "Rising from the depths" kraken/octopus design, with two LEDs, a coin-cell power switch, and an SAO header.
functions: Two LEDs light when the slide switch is on; a 6-pin SAO header lets attendees plug in add-on boards. No microcontroller is present, so there is no other interactive behavior.
look:
  colors:
  - purple
  - gold
  shape: rectangle
  themes:
  - animal
  - horror
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two through-hole yellow LEDs, hand-soldered by the attendee.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: v2
  sao_ports: 1
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of BSides Jacksonville 2023; sponsored by Guidepoint Security.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: The GitHub repo only holds a README and a soldering/assembly guide image; no schematic, PCB, or gerber files are published.
links:
- label: github.com/blackandwhitehat/BSidesJAX_2023_Badge
  url: https://github.com/blackandwhitehat/BSidesJAX_2023_Badge
  kind: repo
  archived: https://web.archive.org/web/20260907110102/https://github.com/blackandwhitehat/BSidesJAX_2023_Badge
images:
- file: assets/images/badges/bsides-jacksonville-2023/bsidesjax-2023-badge/e65d66f2ee.jpg
  source: https://github.com/blackandwhitehat/BSidesJAX_2023_Badge
  credit: Panda (@hacksbearywell)
  caption: Front and back of the purple BSidesJAX 2023 attendee badge, showing the kraken/octopus artwork, LEDs, slide switch, CR2032 holder, SAO header, and Guidepoint Security sponsor logo
  archived: https://web.archive.org/web/20260907110102/https://github.com/blackandwhitehat/BSidesJAX_2023_Badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/blackandwhitehat/BSidesJAX_2023_Badge
  title: BSidesJAX_2023_Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides Jacksonville 2023''.'
  archived: https://web.archive.org/web/20260907110102/https://github.com/blackandwhitehat/BSidesJAX_2023_Badge
- kind: url
  url: https://raw.githubusercontent.com/blackandwhitehat/BSidesJAX_2023_Badge/main/risingfromthedepths.png
  title: Badge Soldering Guide (risingfromthedepths.png)
  accessed: '2026-09-07'
  note: Assembly guide image; front and back photos of the badge itself reveal the design, LEDs, switch, battery holder, SAO header pinout, sponsor, and the credit "Badge by Panda @hacksbearywell".
  archived: https://web.archive.org/web/20260907110119/https://raw.githubusercontent.com/blackandwhitehat/BSidesJAX_2023_Badge/main/risingfromthedepths.png
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The repo is limited to a README and one soldering-guide image; no schematic, gerbers, firmware, or BOM are published, so make_your_own is marked partial rather than yes. Price/quantity are not stated anywhere found; treated as a free attendee giveaway based on the "ATTENDEE" silkscreen and sponsor branding, not a confirmed price. The maker credits "Panda (@hacksbearywell)" on the badge silkscreen; the GitHub account holding the repo is "blackandwhitehat" — could not confirm whether these are the same person or a team, so both are noted. A same-maker follow-up exists for 2024 (github.com/blackandwhitehat/BSidesJAX_2024_Badge) — reported separately, not created here.
last_modified_date: '2026-09-07'
---

The 2023 BSidesJAX attendee badge is a purple PCB etched with a "Rising from the depths" kraken/octopus motif on the front, credited on the back silkscreen to "Panda (@hacksbearywell)". It is a simple, solder-it-yourself badge rather than a microcontroller-based one: attendees hand-solder two through-hole LEDs, a slide power switch, and a CR2032 coin-cell holder, all lit through a basic circuit with no chip onboard. The back carries a 6-pin SAO header (GPIO1/SDA/VCC, GPIO2/SCL/GND) so attendees could plug in add-on boards, along with QR codes for the schedule, SAO sign-up, and the con's Discord, plus a "2023 Badge Sponsor" logo for Guidepoint Security.

No hardware design files, firmware, or BOM were published for this badge — the maker's GitHub repository contains only a README and a single illustrated "Badge Soldering Guide" image that doubles as documentation of what the badge looks like and how to assemble it (it also walks through using a Pinecil soldering iron, unrelated to the badge's own function). No price or production quantity is stated anywhere found; it reads as a standard giveaway to BSidesJAX 2023 attendees rather than a sold item.
