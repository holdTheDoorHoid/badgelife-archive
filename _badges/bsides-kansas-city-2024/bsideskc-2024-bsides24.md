---
title: 'BSidesKC 2024 Learn to Solder Badge (Down the Rabbit Hole)'
id: bsides-kansas-city-2024-bsideskc-2024-bsides24
layout: badge
parent: BSides Kansas City 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-kansas-city-2024
year: 2024
makers:
- name: BadgePirates
  url: https://github.com/BadgePiratesLLC
summary: A learn-to-solder badge BadgePirates built for BSidesKC 2024, carrying a black-and-gold rabbit-head "Down the Rabbit Hole" design on the front and the through-hole/SMD soldering exercise on the back.
functions: 'A teaching kit: attendees solder a through-hole SPDT slide switch, a CR2032 coin-cell holder, and two surface-mount reverse-mount LEDs onto the board, wired as the rabbit''s eyes.'
look:
  colors:
  - black
  - gold
  shape: rectangle
  themes:
  - rabbit
  - learn to solder
tech:
  mcu: none
  leds:
    count: 2
    type: reverse-mount
    note: Blue reverse-mount LEDs placed over the rabbit's eyes; polarity marked by a dot on the package.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/BadgePiratesLLC/BsidesKC_2024/tree/main/CAD/BsidesKC24-Inkscape
  firmware_url: null
  eda_tool: KiCad
  notes: KiCad project, schematic, PCB, and gerbers are in the repo's CAD folder; Artwork folder has the front graphics (Inkscape SVG/PNG); a PDF with soldering instructions is at the repo root.
links:
- label: github.com/BadgePiratesLLC/BsidesKC_2024
  url: https://github.com/BadgePiratesLLC/BsidesKC_2024
  kind: repo
- label: BsidesKC24 Learn to Solder Instructions (PDF)
  url: https://raw.githubusercontent.com/BadgePiratesLLC/BsidesKC_2024/main/BsidesKC24-Learn-To-Solder-Instructions.pdf
  kind: doc
images:
- file: assets/images/badges/bsides-kansas-city-2024/bsideskc-2024-bsides24/de90649304.jpg
  source: "https://github.com/BadgePiratesLLC/BsidesKC_2024/tree/main/Artwork"
  credit: "BadgePirates"
  caption: "CAD render of the front of the BSidesKC 2024 Learn to Solder badge, a rabbit-head 'Down the Rabbit Hole' design"
contact: {}
notes:
- 2024 BSidesKC badge from BadgePirates' catalog. Found by the event-year sweep, task bsides-any.
- 'The sweep''s original title was "BSidesKC 2024 (BSides24)"; the repo and its instructions PDF identify it as this year''s "Learn to Solder" kit, so the title was updated to match.'
status: released
sources:
- kind: url
  url: https://github.com/BadgePiratesLLC/BsidesKC_2024
  title: BSidesKC 2024 (BSides24)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides Kansas City 2024''.'
- kind: url
  url: https://github.com/BadgePiratesLLC/BsidesKC_2024/tree/main/CAD/BsidesKC24-Inkscape
  title: 'BsidesKC_2024 repo: CAD folder (KiCad project + gerbers)'
  accessed: '2026-09-10'
  note: Confirms open-source KiCad hardware files and gerbers for the board.
- kind: url
  url: https://raw.githubusercontent.com/BadgePiratesLLC/BsidesKC_2024/main/BsidesKC24-Learn-To-Solder-Instructions.pdf
  title: BsidesKC24 Learn To Solder Instructions (PDF)
  accessed: '2026-09-10'
  note: 'Describes the badge as this year''s Learn to Solder kit: two blue reverse-mount LEDs (D1/D2, wired as the rabbit''s eyes), a CR2032 holder, and a through-hole SPDT slide switch; includes photos of the assembled back side.'
- kind: url
  url: https://raw.githubusercontent.com/BadgePiratesLLC/BsidesKC_2024/main/Artwork/BSidesKC24-L2S.png
  title: BSidesKC24-L2S.png (front artwork/CAD render)
  accessed: '2026-09-10'
  note: Source image for the saved photo; shows the rabbit-head "Down the Rabbit Hole" front design with BSidesKC Kansas City branding.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: No maker's-own price, quantity, or distribution details were found (likely handed out free at the con's Learn to Solder table, but that is not stated anywhere in the sources, so get_one fields are left empty). No firmware is involved — the board is passive (two LEDs, a switch, and a battery holder), so tech.mcu is 'none' and make_your_own.firmware_url is left null. Could not confirm whether the badge was also distributed to non-attendees or sold separately.
last_modified_date: '2026-09-10'
---

BadgePirates built this board as BSidesKC 2024's "Learn to Solder" kit: a beginner soldering exercise handed out (or run as a workshop station) at the con rather than a standalone attendee badge. The front carries a black-and-gold rabbit-head graphic with "Down the Rabbit Hole" and "BSides Kansas City" lettering; the back is where the soldering happens.

Builders populate a through-hole SPDT slide switch and a CR2032 coin-cell holder, then two surface-mount reverse-mount LEDs (D1 and D2) that sit over the rabbit's eyes on the front graphic, giving the finished board glowing blue eyes once the switch is closed. The instructions PDF walks through the "tack one pad, then solder the far side" technique for the SMD LEDs and calls out their polarity marking.

The project's GitHub repo (BadgePiratesLLC/BsidesKC_2024) is a full open-hardware release: KiCad schematic, PCB layout, and gerbers under `CAD/BsidesKC24-Inkscape`, the Inkscape source art and PNG renders under `Artwork`, and the instructions PDF at the repo root. No firmware is involved — the LEDs run directly off the coin cell through the switch, with no microcontroller on the board.

## Make your own

The KiCad project (schematic, PCB, and gerbers) is in `CAD/BsidesKC24-Inkscape` of the [GitHub repo](https://github.com/BadgePiratesLLC/BsidesKC_2024); the front graphics are in `Artwork` as Inkscape SVG and PNG. The repo's [Learn to Solder Instructions PDF](https://raw.githubusercontent.com/BadgePiratesLLC/BsidesKC_2024/main/BsidesKC24-Learn-To-Solder-Instructions.pdf) documents the build order and component placement (D1/D2 reverse-mount LEDs, CR2032 holder, SPDT slide switch).
