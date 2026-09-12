---
title: DEF CON 14 Badge
id: dc14-badge
layout: badge
parent: DC14
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc14
year: 2006
makers:
- name: Grand Idea Studio (Joe Grand / Kingpin)
  url: https://grandideastudio.com/portfolio/other/defcon-14-badge/
summary: 'The first electronic badge issued at DEF CON: a PIC10F202-driven PCB badge with two blinking blue LEDs, made to cut down on counterfeiting while staying open for attendees to hack.'
functions: 'A single pushbutton cycles the two LEDs through five states: both on, both blinking, alternating, a pseudo-random pattern, and sleep.'
look:
  colors:
  - black
  - red
  - green
  - blue
  - purple
  - gold
  - silver
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: PIC10F202
  leds:
    count: 2
    type: discrete
    note: two 10mm jumbo blue LEDs
  display: none
  connectivity: []
  battery: coin cell
  sao_version: none
get_one:
  price: under $5 (cost to produce; badges were included with convention registration, not sold separately)
  price_usd: null
  quantity: over 6,000
  availability: sold_out
  availability_note: checked 2026-09-08 via grandideastudio.com; historical item, no longer distributed
  distribution:
  - free_drop
  where: 'Given to DEF CON 14 (2006) attendees; sold out within hours of the convention opening. Seven soldermask colors denoted attendee category: Human, Goon, Press, Speaker, Vendor, VIP, and Limited Edition.'
make_your_own:
  open_source: true
  hardware_url: https://grandideastudio.com/media/dc14_bdg_schematic.pdf
  firmware_url: https://grandideastudio.com/media/dc14_bdg_source.zip
  gerbers_url: null
  bom_url: https://grandideastudio.com/media/dc14_bdg_bom.pdf
  eda_tool: null
  license: null
  fab_url: null
  notes: 'Also published: assembly drawings (top/bottom), test procedure, a "Behind the Scenes" paper and slide deck.'
links:
- label: grandideastudio.com/portfolio/other/defcon-14-badge
  url: https://grandideastudio.com/portfolio/other/defcon-14-badge/
  kind: website
  archived: https://web.archive.org/web/20260309222325/https://grandideastudio.com/portfolio/other/defcon-14-badge/
- label: DEF CON 14 Badge schematic (PDF)
  url: https://grandideastudio.com/media/dc14_bdg_schematic.pdf
  kind: doc
  archived: https://web.archive.org/web/20260309222327/https://grandideastudio.com/media/dc14_bdg_schematic.pdf
- label: DEF CON 14 Badge bill of materials (PDF)
  url: https://grandideastudio.com/media/dc14_bdg_bom.pdf
  kind: doc
  archived: https://web.archive.org/web/20260309222327/https://grandideastudio.com/media/dc14_bdg_bom.pdf
- label: DEF CON 14 Badge source code (PIC MPLAB / CCS PIC C)
  url: https://grandideastudio.com/media/dc14_bdg_source.zip
  kind: repo
  archived: https://web.archive.org/web/20260309222327/https://grandideastudio.com/media/dc14_bdg_source.zip
- label: DEF CON 14 Badge photos (Flickr)
  url: https://www.flickr.com/photos/joesmooth/sets/72157594230629796
  kind: social
images:
- file: assets/images/badges/dc14/badge/bfd8fb62c4.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-14-badge/
  credit: Grand Idea Studio
  caption: DEF CON 14 badge, front
  archived: https://web.archive.org/web/20260309222325/https://grandideastudio.com/portfolio/other/defcon-14-badge/
- file: assets/images/badges/dc14/badge/fe3403cffc.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-14-badge/
  credit: Grand Idea Studio
  caption: DEF CON 14 badge, detail
  archived: https://web.archive.org/web/20260309222325/https://grandideastudio.com/portfolio/other/defcon-14-badge/
contact: {}
notes:
- 'The first-ever DEF CON electronic badge: a PIC10F202-driven board shaped like the DEF CON logo with two blinking blue LEDs, issued in seven soldermask colors (Human, Goon, Press, Speaker, Vendor, VIP, Limited Edition) with over 6,000 made. Found by the event-year sweep, task dc14-all.'
- The sweep's original notes matched the maker's own page; title and event were already correct, no changes needed there.
status: released
sources:
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-14-badge/
  title: DEF CON 14 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc14-all); event read as ''dc14''.'
  archived: https://web.archive.org/web/20260309222325/https://grandideastudio.com/portfolio/other/defcon-14-badge/
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-14-badge/
  title: 'Grand Idea Studio: DEFCON 14 Badge'
  accessed: '2026-09-08'
  note: Confirmed maker, event/year, MCU, LED count/behavior, soldermask colors, quantity (6,000+), cost (<$5/unit), distribution (given to attendees, sold out fast), and design-file links.
  archived: https://web.archive.org/web/20260309222325/https://grandideastudio.com/portfolio/other/defcon-14-badge/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Price is production cost (<$5/unit); no per-badge retail price was charged since it came with registration. No PCB shape/color swatch or gerbers were published, so look.shape and make_your_own.gerbers_url are left empty. EDA tool and license not stated on the page.
last_modified_date: '2026-09-08'
---

The DEF CON 14 badge, issued in 2006, was the first electronic badge given out at the convention. Designed by Grand Idea Studio (Joe Grand, aka Kingpin), it centers on a Microchip PIC10F202 six-pin microcontroller driving two 10mm jumbo blue LEDs, cycled through five states (on, blinking, alternating, pseudo-random, and sleep) with a single pushbutton. Grand Idea Studio built the badge with "active electronics" specifically to make counterfeiting harder while keeping the circuit open for attendees to explore and modify. More than 6,000 units were made, sold out within hours of the con opening, and issued in seven soldermask colors marking attendee type: Human, Goon, Press, Speaker, Vendor, VIP, and a Limited Edition color reserved for Grand Idea Studio and the DEF CON organizers. Total cost per badge, including assembly and testing, was kept under $5.

To mark the badge's hackable design, Grand Idea Studio ran a DEF CON Badge Hacking Contest that weekend. The winning entry, the "Event Generator Ghoul," turned a badge's LEDs into trigger signals for an analog modular synthesizer; other entries included a flamethrower badge and a firmware hack that blinked "DEFCON 14" in Morse code.

## Make your own

Grand Idea Studio has published the full documentation set for this badge: schematic, bill of materials, top/bottom assembly drawings, a test procedure, and the PIC10F202 source code (for MPLAB and CCS PIC C). No Gerbers or EDA project files are published alongside them.
