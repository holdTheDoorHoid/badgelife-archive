---
title: BSides PDX 2018 badge
id: other-securelyfitz-2018-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: pdxbadgers
  url: https://github.com/pdxbadgers
summary: The official electronic badge for BSides PDX 2018, cut in the shape of Oregon with a purple soldermask and Portland-themed silkscreen icons (rose, bike, bridge, Bigfoot, donut, coffee, rain).
functions: Runs on an ATtiny861A driving a charlieplexed LED array (four PWM RGB LEDs plus twelve yellow LEDs) with two front buttons for input; the firmware repo ships as individual test modules (LED cycling, RGB PWM, button test, timer test) rather than one finished game.
look:
  colors:
  - purple
  - yellow
  shape: oregon outline
  themes:
  - logo
  - text
tech:
  mcu: ATtiny861A
  leds:
    count: 16
    type: discrete
    note: 4x RGB LEDs (PWM-driven, gull-wing 4-pin) plus 12x yellow LEDs, charlieplexed
  display: none
  connectivity:
  - usb
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/pdxbadgers/badge-2018/tree/master/HW
  firmware_url: https://github.com/pdxbadgers/badge-2018/tree/master/FW
  eda_tool: KiCad
links:
- label: github.com/securelyfitz/badge-2018 (fork)
  url: https://github.com/securelyfitz/badge-2018
  kind: repo
- label: github.com/pdxbadgers/badge-2018 (original)
  url: https://github.com/pdxbadgers/badge-2018
  kind: repo
images:
- file: assets/images/badges/other/securelyfitz-2018-badge/51317151de.jpg
  source: https://github.com/pdxbadgers/badge-2018
  credit: pdxbadgers
  caption: Front of the Oregon-shaped BSides PDX 2018 badge PCB
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- The entry's original repo link (securelyfitz/badge-2018) is a fork; the badge itself is the official BSides PDX 2018 conference badge, designed and maintained by the pdxbadgers GitHub org.
status: released
sources:
- kind: url
  url: https://github.com/securelyfitz/badge-2018
  title: securelyfitz 2018 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/pdxbadgers/badge-2018
  title: pdxbadgers/badge-2018
  accessed: '2026-09-07'
  note: Original (non-fork) repo; confirmed it is the BSides PDX 2018 badge and identified maker org.
- kind: url
  url: https://raw.githubusercontent.com/pdxbadgers/badge-2018/master/HW/BOM.csv
  title: badge-2018 HW/BOM.csv
  accessed: '2026-09-07'
  note: Bill of materials confirming ATtiny861A MCU, 4x RGB + 12x yellow LEDs, CR2032 battery, micro-USB connector, two buttons.
- kind: url
  url: https://github.com/pdxbadgers/badge-2018/tree/master/FW
  title: badge-2018 FW directory
  accessed: '2026-09-07'
  note: Firmware layout; confirms charlieplexed LED driving, micronucleus USB bootloader, and per-feature test programs rather than one integrated game/firmware.
- kind: url
  url: https://github.com/pdxbadgers/badge-2018/tree/master/ART
  title: badge-2018 ART directory
  accessed: '2026-09-07'
  note: Source of the board art image used for this entry; confirms Oregon-outline shape, purple/yellow color scheme, and BSides Portland branding (front) plus a sponsor-logo back panel.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No BSidesPDX event id exists yet in _data/events.yml, so event is left as "other" — this is the BSides PDX 2018 (Portland, Oregon) conference badge. Price, exact production quantity, and distribution method (e.g. included with registration vs. sold) are not stated anywhere in the repo and were left empty rather than guessed; the BOM's "order quantity" column is bulk component stock ordered from DigiKey, not a badge count, so it was not used as quantity. No SAO header is documented on this board despite the HW README linking to the DC26 SAO KiCad footprint as a generic library reference, so sao_version was left null rather than assumed. Micro-USB connector appears to be for micronucleus bootloader programming, not general data/charging use.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/securelyfitz-2018-badge.glb
  method: kicad
  source_file: HW/BSidesPDX_2018/BSidesPDX_2018.kicad_pcb
  generated: '2026-09-10'
  bytes: 462348
---

The BSides PDX 2018 badge is the official electronic conference badge for BSides Portland 2018, designed by the volunteer group behind the pdxbadgers GitHub org. The PCB is cut into the outline of the state of Oregon, finished in a purple soldermask with yellow silkscreen icons — a rose, a bicycle, a bridge, Bigfoot, a donut, a coffee cup, rain clouds, a book, and a light-rail train — arranged around a "BSIDES PORTLAND" logo, nodding to local Portland culture. The back of the board carries the conference's sponsor logos (Platinum through Silver tiers), a common badgelife touch for community-run BSides events.

Electrically it is built around an ATtiny861A microcontroller driving a small charlieplexed LED array: four PWM-controlled RGB LEDs and twelve yellow LEDs, with two tactile buttons for input, and a coin-cell (CR2032) as the power source. A micro-USB connector is present for firmware updates via the micronucleus USB bootloader rather than for data or charging. The hardware (KiCad schematics, PCB layout, and BOM) and firmware (C source, organized as a set of individual test/demo programs for the LEDs, buttons, and timers) are both published under the pdxbadgers/badge-2018 repository on GitHub; the entry's originally-listed link (securelyfitz/badge-2018) is a personal fork of that same project rather than a separate design.

Specifics that would normally round out an entry like this — unit price, exact production run, and whether it was handed out with registration or sold separately — are not documented in the public repository and are left blank here rather than guessed.
