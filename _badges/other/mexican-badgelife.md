---
title: Mexican_BadgeLife
id: other-mexican-badgelife
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: markwinap
  url: https://github.com/markwinap
  role: designer
- name: Francisco Gonzalez Canales
  role: contributor
summary: A simple LED "El Santo" badge shaped like the mask of the famous Mexican masked wrestler, built around a 555-timer blink circuit rather than a microcontroller.
functions: Blinks two white LEDs using a discrete 555-timer (ICM7555) astable circuit; no interactivity or MCU-driven modes.
look:
  colors: [green, yellow, black]
  shape: mask
  themes: [wearable, hardware tool]
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 2x white 3mm THT LEDs
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
  hardware_url: https://github.com/markwinap/Mexican_BadgeLife/tree/master/El_Santo/Kicad_Project/El_Santo
  firmware_url: null
  eda_tool: KiCad
  license: GPL-3.0
  notes: Repo also includes Inkscape SVG mask art and PNG silkscreen/copper layer exports for the "El_Santo" board.
links:
- label: github.com/markwinap/Mexican_BadgeLife
  url: https://github.com/markwinap/Mexican_BadgeLife
  kind: repo
images:
  - file: assets/images/badges/other/mexican-badgelife/58a57c1e48.png
    source: "https://github.com/markwinap/Mexican_BadgeLife"
    credit: "markwinap (Marco David Martinez)"
    caption: "El Santo badge silkscreen artwork, a luchador mask design"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/markwinap/Mexican_BadgeLife
  title: Mexican_BadgeLife
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/markwinap/Mexican_BadgeLife/tree/master/El_Santo/Kicad_Project/El_Santo
  title: El_Santo KiCad project files
  accessed: '2026-09-07'
  note: 'PCB title block reads "El Santo LED Badge"; footprints/values show a CR2032 (BS-7 holder), 2x 3mm white LEDs, an ICM7555 timer, 2N3904 transistor, and resistor/capacitor values consistent with a 555 astable blink circuit.'
- kind: url
  url: https://api.github.com/repos/markwinap/Mexican_BadgeLife/commits
  title: Mexican_BadgeLife commit history
  accessed: '2026-09-07'
  note: 'Two commits from 2018-09-20 by Marco David Martinez (markwinap@gmail.com) and Francisco Gonzalez Canales, both using @SOAM.TCS.com company email addresses, adding the PCB and schematic. No mention of any specific conference.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'README.md in the repo contains only the project title, no descriptive text. No web presence beyond the GitHub repo was found (searches for "markwinap El_Santo badge" returned unrelated results). The design is a themed silkscreen mask of El Santo (a famous Mexican luchador) over a simple discrete 555-timer LED blinker, not a microcontroller-based board. No event, price, quantity, or distribution details could be found; this may have been a personal/hobby project rather than a badge distributed at a specific convention. Left event as "other" since no con is named in any source.'
last_modified_date: '2026-09-07'
---

The Mexican_BadgeLife repository by GitHub user markwinap (Marco David Martinez) holds a single badge design called "El Santo," named for and shaped like the mask of the legendary Mexican luchador of the same name. Rather than using a microcontroller, the board is a straightforward analog blinker: an ICM7555 timer chip wired as an astable oscillator drives two white 3mm through-hole LEDs, powered by a CR2032 coin cell in a BS-7 holder, with a 2N3904 transistor and a handful of resistors and capacitors rounding out the circuit.

The KiCad project (PCB and schematic) plus Inkscape SVG artwork and PNG silkscreen/copper layer exports were committed to the repository on September 20, 2018 by markwinap and a collaborator, Francisco Gonzalez Canales; both commits use company email addresses from the same employer, suggesting this may have started as a personal or workplace project rather than a badge made for a specific hackercon. The repository's README contains only the project title, and no press coverage, storefront listing, or social posts about the badge could be found, so its distribution, pricing, and quantity remain unknown. The hardware files are published under the GPL-3.0 license, making the design open for anyone to build.
