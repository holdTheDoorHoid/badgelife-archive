---
title: AI Village DEFCON31 Badge
id: dc31-ai-village-defcon31-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: ben-hawks / AI Village
  url: https://github.com/ben-hawks
summary: 'The staff badge AI Village built for its own crew at DEF CON 31 (2023): a Raspberry Pi Pico W board with an e-paper display, six buttons, and four SAO ports.'
functions: Runs custom firmware on the Pico W behind a 2.9" e-ink screen; six front buttons (A, B, C, up, down, reset) for on-badge menus/games; a real-time clock keeps time between charges; a buzzer for audio feedback; a microSD slot for storage; two QWiic/STEMMA QT ports and an I2C header let it drive external sensors or add-ons alongside its four SAO ports.
look:
  colors: []
  shape: null
  themes:
  - security
  - village badge
tech:
  mcu: RP2040 (Raspberry Pi Pico W module)
  leds:
    count: 1
    type: discrete
    note: single blue status LED (not addressable)
  display: 2.9" e-paper (GoodDisplay GDEW029I6FD)
  connectivity:
  - wifi
  - i2c
  - usb
  inputs:
  - buttons
  battery: 2x AAA
  sao_version: v1.69bis
  sao_ports: 4
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Given to AI Village staff/volunteers at DEF CON 31; not sold publicly as far as sources found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/ben-hawks/AIV_DC31_Badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/ben-hawks/AIV_DC31_Badge
  url: https://github.com/ben-hawks/AIV_DC31_Badge
  kind: repo
images: []
contact: {}
notes:
- The KiCad project file is named "AIV_DC31_Staff", indicating this specific board is the AI Village staff/volunteer badge for DEF CON 31, not a general-attendee giveaway.
status: released
sources:
- kind: url
  url: https://github.com/ben-hawks/AIV_DC31_Badge
  title: AI Village DEFCON31 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 31 (2023) - outside the DC24-29 window, listed for reference only''.'
- kind: url
  url: https://github.com/ben-hawks/AIV_DC31_Badge/blob/main/production/bom.csv
  title: 'AIV_DC31_Badge: production/bom.csv'
  accessed: '2026-09-07'
  note: Bill of materials confirming Raspberry Pi Pico W module, PCF85063A RTC, GDEW029I6FD e-paper panel, 4x SAOv1.69bis headers, 2x QWiic/STEMMA QT connectors, microSD slot, single blue LED, buzzer, 6 buttons, and 2x AAA battery holder.
- kind: url
  url: https://github.com/ben-hawks/AIV_DC31_Badge/git/trees/main
  title: AIV_DC31_Badge repository file tree
  accessed: '2026-09-07'
  note: File listing confirms the sole board file is "AIV_DC31_Staff.kicad_pcb" (staff variant) and that full KiCad schematics, PCB layout, gerbers, BOM, and datasheets are published (open hardware); no firmware source or README found in the repo, and no photos of an assembled unit were located.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Chip/display/feature details come from the maker's own KiCad BOM and schematic files, which is strong evidence, but no README, blog post, or press coverage describing the badge's story, price, or distribution numbers was found, and no photo of an assembled/worn badge turned up in a web search or on the repo itself. Left get_one.price, get_one.quantity, and images empty rather than guess.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc31/ai-village-defcon31-badge.glb
  method: kicad
  source_file: AIV_DC31_Staff.kicad_pcb
  generated: '2026-09-07'
  bytes: 438296
---

This is the staff badge AI Village built for its own crew at DEF CON 31 in 2023, designed by ben-hawks and published as an open KiCad project on GitHub. The board is built around a Raspberry Pi Pico W module (RP2040 with Wi-Fi), driving a 2.9" e-paper display behind six front buttons (A, B, C, up, down, and reset) for on-badge navigation. A PCF85063A real-time clock keeps time, a small buzzer provides audio feedback, and a microSD slot offers local storage. The badge runs on two AAA batteries and carries four SAO v1.69bis ports plus two QWiic/STEMMA QT connectors and a bare I2C header, so it could host add-ons and other badges' SAOs at once. A single blue LED serves as a status indicator rather than the animated arrays common on many badgelife boards.

The repository's board file is named "AIV_DC31_Staff," which points to this specific design being made for AI Village's own staff and volunteers rather than as a general-attendee giveaway; sources found did not describe a separate attendee badge from the same team. No pricing, production quantity, or distribution details were published alongside the hardware files, and no photos of an assembled unit turned up in a web search, so those fields are left blank here.

## Make your own

The full hardware design is open: KiCad schematics and PCB layout, a custom component/footprint library, 3D step models, datasheets for the major parts, and finished production files (gerbers, BOM, pick-and-place positions, netlist) are all in the GitHub repository at github.com/ben-hawks/AIV_DC31_Badge. No firmware source was found in the repo, so the software that ran on these badges at DEF CON 31 is not confirmed to be published.
