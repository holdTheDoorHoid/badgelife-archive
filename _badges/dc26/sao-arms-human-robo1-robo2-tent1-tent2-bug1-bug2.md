---
title: SAO arms (human/robo1/robo2/tent1/tent2/bug1/bug2)
id: dc26-sao-arms-human-robo1-robo2-tent1-tent2-bug1-bug2
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc26
year: 2018
makers:
- name: Joe Fitz (securelyfitz)
  url: https://github.com/securelyfitz
summary: A set of PCB "arm" extenders (human, robo1, robo2, tent1, tent2, bug1, bug2) that plug onto Joe FitzPatrick's microbadge to build a custom creature, part of the same build-your-own-badge kit as the sao-faces set.
functions: Purely mechanical/cosmetic add-on boards; no active electronics of their own. Snap or solder onto a microbadge (or another SAO host) alongside a face board to assemble a custom little character.
look:
  colors: []
  shape: arm
  themes:
  - robot
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/securelyfitz/sao-arms
  firmware_url: null
  eda_tool: null
links:
- label: github.com/securelyfitz/sao-arms
  url: https://github.com/securelyfitz/sao-arms
  kind: repo
- label: github.com/securelyfitz/microbadge
  url: https://github.com/securelyfitz/microbadge
  kind: repo
- label: github.com/securelyfitz/sao-faces
  url: https://github.com/securelyfitz/sao-faces
  kind: repo
images:
- file: assets/images/badges/dc26/sao-arms-human-robo1-robo2-tent1-tent2-bug1-bug2/7c2b7b901c.jpg
  source: "https://github.com/securelyfitz/sao-arms"
  credit: "Joe FitzPatrick (securelyfitz)"
  caption: "Silkscreen artwork for the robo2 arm variant"
- file: assets/images/badges/dc26/sao-arms-human-robo1-robo2-tent1-tent2-bug1-bug2/14fa6671ba.jpg
  source: "https://github.com/securelyfitz/sao-arms"
  credit: "Joe FitzPatrick (securelyfitz)"
  caption: "Silkscreen artwork for the bug1 arm variant"
contact: {}
notes:
- Sweep's sources list named the GitHub repo directly; the one-line note ("Reported as an 'other item found' during the stub research pass") did not describe the item itself.
status: listed
sources:
- kind: url
  url: https://github.com/securelyfitz/sao-arms
  title: SAO arms (human/robo1/robo2/tent1/tent2/bug1/bug2)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/securelyfitz/microbadge
  title: microbadge - functional badge in 1 square centimeter
  accessed: '2026-09-10'
  note: "Confirmed event/year (DEF CON 26, 2018: '1100 of them assembled in time for defcoin'), ATtiny85 MCU, and that arms/faces are add-ons for this host board."
- kind: url
  url: https://github.com/securelyfitz/sao-faces
  title: sao-faces
  accessed: '2026-09-10'
  note: Confirms arms and faces are companion repos meant to be combined on a microbadge.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >-
    This is a design-files repo (schematics, board outlines, Gerber/CAM, and BMP silkscreen art)
    for seven interchangeable "arm" shapes, not a standalone product with its own price or
    distribution numbers - price/quantity/availability were never given separately from the
    microbadge host board it plugs into (that entry, dc26-ubadge-microbadge, records "under $1"
    and "1,100 assembled" for the host). No MCU/LEDs of its own since these are passive
    plug-on boards. No maker photos of an assembled arm+face+microbadge combo were found, only
    the board-outline artwork used here. License is not stated in the repo.
last_modified_date: '2026-09-10'
---

Joe FitzPatrick (securelyfitz) designed this set of seven "arm" PCB shapes -- a human arm, two robotic arm variants (robo1, robo2), two tentacle-style arms (tent1, tent2), and two bug-leg variants (bug1, bug2) -- as building blocks for a build-your-own creature badge. They are meant to be paired with the companion `sao-faces` boards (terminator, badgewife, smiley) and plugged onto his `microbadge`, a tiny ATtiny85-based SAO host that FitzPatrick built roughly 1,100 of for DEF CON 26 in 2018. Mixing and matching an arm shape with a face shape lets a builder assemble their own little character out of otherwise-identical small PCBs.

The arms carry no electronics of their own; they are purely structural/cosmetic extenders, so there is no MCU, LED, or display to report for this repo specifically. The GitHub repository publishes schematics, board files, and CAM/Gerber outputs for each of the seven shapes, along with BMP artwork of the silkscreen outlines (two of which are used as the images above), making the hardware openly reproducible even though no license file accompanies it.

## Make your own

The repo (github.com/securelyfitz/sao-arms) contains `.sch`/`.brd` files and CAM/Gerber ZIPs for each arm variant (human, robo1, robo2, tent1, tent2, bug1, bug2). Per the README, see the `microbadge` repo's README for details on how the arms and faces attach to the host board.
