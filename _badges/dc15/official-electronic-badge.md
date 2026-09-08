---
title: DEF CON 15 Official Electronic Badge
id: dc15-official-electronic-badge
layout: badge
parent: DC15
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc15
year: 2007
makers:
- name: Grand Idea Studio (Joe Grand)
summary: The official electronic badge for DEF CON 15, a battery-powered PCB badge with a 95-LED matrix that scrolls a user-customizable text message.
functions: 'Five operating states: default scrolling-text display, custom message entry (via two capacitive-touch sensors), scroll-speed selection, a persistence-of-vision hidden message shown when waved through the air, and sleep mode. Unpopulated footprints allowed for optional accelerometer and RF transceiver add-ons.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: Freescale MC9S08QG8
  leds:
    count: 95
    type: discrete
    note: Arranged in a 5-column by 19-row matrix.
  display: LED matrix 5x19
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '6,800'
  availability: free
  distribution:
  - free_drop
  where: Distributed as the official conference badge at DEF CON 15 (2007), in six variants (Human, Goon, Press, Speaker, Vendor, Uber) distinguished by cutout text and soldermask color.
make_your_own:
  open_source: yes
  hardware_url: https://grandideastudio.com/media/dc15_bdg_schematic.pdf
  firmware_url: https://grandideastudio.com/media/dc15_bdg_codewarrior.zip
  eda_tool: null
links:
- label: grandideastudio.com/portfolio/other/defcon-15-badge
  url: https://grandideastudio.com/portfolio/other/defcon-15-badge/
  kind: website
images:
  - file: assets/images/badges/dc15/official-electronic-badge/2e4e3bbf57.jpg
    source: "https://grandideastudio.com/portfolio/other/defcon-15-badge/"
    credit: "Grand Idea Studio"
    caption: "DEF CON 15 badge, front"
  - file: assets/images/badges/dc15/official-electronic-badge/6a6eb0d6e1.jpg
    source: "https://grandideastudio.com/portfolio/other/defcon-15-badge/"
    credit: "Grand Idea Studio"
    caption: "DEF CON 15 badge variants"
contact: {}
notes:
- Official 2007 badge built around a Freescale MC9S08QG8 MCU driving a 5x19 LED matrix for scrolling text, issued in six variants (Human, Goon, Press, Speaker, Vendor, Uber) distinguished by cutout text and soldermask color, ~6,800 units made; schematic/BOM/source published by Grand Idea Studio. Found by the event-year sweep, task dc15-all.
- 'This is the same badge already covered in more detail at dc15-badge-2007 ("DEF CON 15 Badge (2007)"); that entry sources media.defcon.org directly and has fuller tech/get_one fields (battery, distribution details). Flagged as a likely duplicate rather than merged or deleted, per research rules.'
status: listed
sources:
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-15-badge/
  title: DEF CON 15 Official Electronic Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc15-all); event read as ''dc15''.'
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-15-badge/
  title: DEF CON 15 Official Electronic Badge — Grand Idea Studio portfolio page
  accessed: '2026-09-08'
  note: Confirmed maker, MCU, LED matrix, variants, quantity (~6,800), and located schematic/BOM/assembly/firmware/source links plus badge photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own portfolio page confirms all core facts already in the sweep notes (chip, matrix, six variants, ~6,800 made) and adds full design-file links (schematic, BOM, assembly drawing, test procedure, CodeWarrior firmware source) and five badge photos. Likely a duplicate of dc15-badge-2007, which sources media.defcon.org directly and carries more detail (battery type, exact distribution venue/dates); left as a separate entry per instructions rather than merged.
last_modified_date: '2026-09-08'
---

The DEF CON 15 official electronic badge, designed by Joe Grand of Grand Idea Studio, was the conference's badge for the 2007 event. It is a battery-powered PCB built around a Freescale MC9S08QG8 8-bit microcontroller driving a 95-LED array arranged in a 5x19 matrix, primarily used to scroll a short text message that attendees could customize.

Two capacitive touch sensors on the board let the wearer cycle through five operating states: the default scrolling display, a message-entry mode for typing a custom string, a scroll-speed selector, a persistence-of-vision mode that reveals a hidden image or message when the badge is waved through the air, and a sleep mode. The board also included unpopulated footprints for an optional accelerometer and RF transceiver, though these were not part of the stock badge.

Roughly 6,800 badges were made across six variants — Human, Goon, Press, Speaker, Vendor, and Uber — distinguished by cutout text and soldermask color, and handed out to the corresponding attendee categories. Grand Idea Studio published the full schematic, bill of materials, assembly drawing, test procedure, and CodeWarrior firmware source for the badge on their site.

## Make your own

Grand Idea Studio's portfolio page hosts the schematic (PDF), BOM (PDF), assembly drawing (PDF), test procedure (PDF), and the original CodeWarrior firmware project (ZIP) for anyone who wants to reproduce the badge's hardware and firmware.
