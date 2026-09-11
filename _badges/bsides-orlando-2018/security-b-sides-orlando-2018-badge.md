---
title: Security B-Sides Orlando 2018 Badge
id: bsides-orlando-2018-security-b-sides-orlando-2018-badge
layout: badge
parent: BSides Orlando 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-orlando-2018
year: 2018
makers:
- name: Jonathan Singer
  url: https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
  role: circuit board design
- name: Heather Lawrence
  role: graphics
summary: A discrete-component "marquee" attendee badge for BSides Orlando 2018, hand-built from a kit and lit by a ring of individual color LEDs around a steampunk gear illustration.
functions: 'No microcontroller: a discrete-component blinking circuit (resistors, capacitors, transistors) drives a ring of individually-colored through-hole LEDs around the badge edge in a marquee-style chase/blink pattern. A slide switch turns the badge on and off.'
look:
  colors:
  - red
  - blue
  - white
  shape: rectangle
  themes:
  - steampunk
  - security
  - badge
tech:
  mcu: none
  leds:
    count: 12
    type: discrete
    note: Individually-colored 5mm through-hole LEDs (red, green, blue) labeled LED1-LED11, driven by a discrete transistor/resistor/capacitor circuit rather than a microcontroller.
  display: none
  connectivity: []
  battery: 2x AA (supplied loose in a bag with the kit)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  - kit
  where: Given to BSides Orlando 2018 attendees as a self-assembly kit.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge/files
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/160630-security-b-sides-orlando-2018-badge
  url: https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260907110153/https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
images:
- file: assets/images/badges/bsides-orlando-2018/security-b-sides-orlando-2018-badge/17e94c7127.jpg
  source: https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
  credit: Jonathan Singer
  caption: 'Assembled badge, powered on: a red PCB with a steampunk gear illustration and a ring of lit red, green, and blue LEDs'
  archived: https://web.archive.org/web/20260907110153/https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
- file: assets/images/badges/bsides-orlando-2018/security-b-sides-orlando-2018-badge/7dc6edac9b.jpg
  source: https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
  credit: Jonathan Singer
  caption: Front and back of the badge in both red and blue PCB colors, alongside the kit's bagged battery and BSides Orlando stickers
  archived: https://web.archive.org/web/20260907110153/https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
  title: Security B-Sides Orlando 2018 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''BSides Orlando 2018''.'
  archived: https://web.archive.org/web/20260907110153/https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
- kind: url
  url: https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
  title: Security B-Sides Orlando 2018 Badge
  accessed: '2026-09-07'
  note: 'Confirmed maker (Jonathan Singer, circuit board) and description ("Simple discrete marquee badge for BSides Orlando given to attendees as a kit"); page lists 9 Gerber fabrication files (uploaded 2018-08-21) under project files. Photos show "Graphics by: Heather Lawrence, Circuit Board by: Jonathan Singer" printed on the PCB back, a "Permit Technologik" steampunk gear theme, both red and blue PCB color runs, a 12-position LED ring (LED1-LED11 silkscreen labels), a power slide switch, and a loose 2xAA battery pack included with the kit.'
  archived: https://web.archive.org/web/20260907110153/https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Gerber files confirm the hardware design is shared, but no bill of materials, schematic, or firmware/source beyond the PCB artwork was found, and no license is stated, so open_source is marked "partial" rather than "yes". Price, quantity produced, and whether it was distributed to all attendees or a subset were not found on the project page or in a web search (only 2 searches ran before this session's search budget was exhausted). Battery type is inferred from the loose cells visible in the kit photo (they read as AA cells) rather than a stated spec.
last_modified_date: '2026-09-07'
---

The Security B-Sides Orlando 2018 badge is a self-assembly "marquee" badge given to attendees of BSides Orlando in 2018. Rather than a microcontroller, it uses a discrete-component circuit (resistors, capacitors, and transistors visible on the board) to drive a ring of individually colored through-hole LEDs around the edge of the card-shaped PCB in a blinking pattern, switched on with a small slide switch and powered by a pair of AA batteries included loose in the kit bag.

The board's front carries a steampunk-styled illustration of interlocking gears under the banner "Permit Technologik," with "BSIDES ORLANDO" and the year "2018" worked into the artwork; the back credits "Graphics by: Heather Lawrence, Circuit Board by: Jonathan Singer." It was produced in at least two PCB solder-mask colors (red and blue). Jonathan Singer published nine Gerber fabrication files for the board on its Hackaday.io project page, making the PCB artwork reproducible, though no schematic, bill of materials, or firmware/source beyond those Gerbers has been found.

## Make your own

Gerber fabrication files (copper, soldermask, and silkscreen layers for both sides) are available on the project's [Hackaday.io files page](https://hackaday.io/project/160630-security-b-sides-orlando-2018-badge/files), sufficient to have the PCB re-fabricated. No schematic, bill of materials, or firmware is published alongside them.
