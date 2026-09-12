---
title: DEFCON 18 Badge
id: dc18-badge
layout: badge
parent: DC18
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc18
year: 2010
makers:
- name: Joe Grand / Grand Idea Studio
  url: https://grandideastudio.com/portfolio/other/defcon-18-badge/
summary: 'The official DEF CON 18 (2010) attendee badge: an aluminum-substrate PCB with laser-etched graphics and USB connectivity, built around a Freescale digital signal controller and a reflective cholesteric LCD.'
functions: Hidden modes for various conference contests; the badge itself was the target platform for that year's Badge Hacking Contest (21 official entries, won by a UPC-A/UPC-E barcode writer/emulator).
look:
  colors:
  - silver
  shape: null
  themes:
  - hardware tool
  - security
tech:
  mcu: MC56F8006
  leds: null
  display: 128x32 Kent Displays reflective cholesteric LCD (ChLCD)
  connectivity:
  - usb
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 7,780
  availability: unknown
  distribution: []
  where: Given to DEF CON 18 attendees; variants (Human, Goon, Press, Speaker, Vendor, Contest Organizer, Uber) denoted attendee type.
make_your_own:
  open_source: true
  hardware_url: https://grandideastudio.com/media/dc18_bdg_schematic.pdf
  firmware_url: https://grandideastudio.com/media/dc18_bdg_source.zip
  eda_tool: null
  bom_url: https://grandideastudio.com/media/dc18_bdg_bom.pdf
  notes: 'Also published: assembly drawing, test procedure (with video), a conference-brochure article ("The DEFCON 18 Badge: Fifth Time''s the Charm"), and a Nuts & Volts magazine article (Sept 2011).'
links:
- label: grandideastudio.com/portfolio/other/defcon-18-badge
  url: https://grandideastudio.com/portfolio/other/defcon-18-badge/
  kind: website
  archived: https://web.archive.org/web/20260303002724/https://grandideastudio.com/portfolio/other/defcon-18-badge/
- label: DEFCON 18 Badge schematic
  url: https://grandideastudio.com/media/dc18_bdg_schematic.pdf
  kind: doc
  archived: https://web.archive.org/web/20260303002725/https://grandideastudio.com/media/dc18_bdg_schematic.pdf
- label: DEFCON 18 Badge source code (Freescale CodeWarrior)
  url: https://grandideastudio.com/media/dc18_bdg_source.zip
  kind: repo
  archived: https://web.archive.org/web/20260303002725/https://grandideastudio.com/media/dc18_bdg_source.zip
- label: DEFCON Forums - DC18 Badge Hacking Contest results
  url: https://forum.defcon.org/showthread.php?p=116737
  kind: article
images:
- file: assets/images/badges/dc18/badge/648ac79941.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-18-badge/
  credit: Grand Idea Studio
  caption: DEFCON 18 badge, aluminum-substrate PCB with laser-etched graphics and cholesteric LCD
  archived: https://web.archive.org/web/20260303002724/https://grandideastudio.com/portfolio/other/defcon-18-badge/
- file: assets/images/badges/dc18/badge/86b7b7c596.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-18-badge/
  credit: Grand Idea Studio
  caption: DEFCON 18 badge, close-up view
  archived: https://web.archive.org/web/20260303002724/https://grandideastudio.com/portfolio/other/defcon-18-badge/
contact: {}
notes:
- 'Official DEF CON 18 conference badge: Freescale MC56F8006 DSC, 128x32 Kent Displays cholesteric LCD, laser-etched aluminum-substrate PCB, 7,780 units made across Human/Goon/Press/Speaker/Vendor/Contest Organizer/Uber variants; documented with schematic, BOM and source at grandideastudio.com. Found by the event-year sweep, task dc18-all.'
status: released
sources:
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-18-badge/
  title: DEFCON 18 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc18-all); event read as ''dc18''.'
  archived: https://web.archive.org/web/20260303002724/https://grandideastudio.com/portfolio/other/defcon-18-badge/
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-18-badge/
  title: DEFCON 18 Badge
  accessed: '2026-09-08'
  note: Confirmed maker, event/year, MCU, display, battery, quantity, contest details, and documentation links (schematic, BOM, source code).
  archived: https://web.archive.org/web/20260303002724/https://grandideastudio.com/portfolio/other/defcon-18-badge/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own portfolio page confirms all core facts. LED info and price/distribution details (given to attendees, no sale price) are not stated on the page, so left empty. Quantity and variant breakdown confirmed. No open questions or source disagreements.
last_modified_date: '2026-09-08'
---

The DEFCON 18 Badge was created by Joe Grand of Grand Idea Studio for the 2010 edition of DEF CON. It features active electronics mounted on an artistically designed, laser-etched aluminum-substrate PCB, built around a Freescale MC56F8006 16-bit digital signal controller and a Kent Displays 128x32 pixel reflective cholesteric liquid crystal display (ChLCD). It also includes USB connectivity, seamless power switching, and hidden modes tied to various conference contests, and runs on a single CR2032 coin cell.

A total of 7,780 badges were manufactured, each laser-engraved with graphics denoting the recipient's attendee type: Human, Goon, Press, Speaker, Vendor, Contest Organizer, or Uber (awarded to official contest winners). This was the fifth consecutive year Joe Grand hosted the DEF CON Badge Hacking Contest built around his badge design; the 2010 contest drew 21 official entries, won by a UPC-A/UPC-E barcode writer/emulator built to fool retail self-checkout scanners.

## Make your own

Grand Idea Studio published full documentation for the badge: a schematic, bill of materials, assembly drawing, test procedure (with a companion video), and the source code (developed in Freescale's CodeWarrior for 56800/E digital signal controllers). A conference-brochure article and a September 2011 Nuts & Volts magazine article also cover its design.
