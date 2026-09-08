---
title: Hackaday Berlin 2023 Voja4 Badge
id: hackaday-berlin-2023-hackaday-berlin-2023-voja4-badge
layout: badge
parent: Hackaday Berlin 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackaday-berlin-2023
year: 2023
makers:
- name: Voja Antonic
summary: 'A 4-bit "down-to-the-metal" computer-trainer badge, re-skinned for Hackaday Berlin 2023 from Voja Antonic''s 2022 Supercon Voja4 design.'
functions: 'Emulates a 4-bit Harvard-architecture CPU (12-bit instruction words, 4,096-word instruction memory, 256 nibbles of data memory, 16 registers, 8-level stack) on a PIC24 microcontroller, with results shown on a 16x8 LED raster display; programs can be written directly in the badge''s own machine code, loaded onward, or run from onboard example programs. Has a GPIO connector and serial interface; hackers at the event added extensions such as a punchcard reader.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - learn to solder
tech:
  mcu: PIC24
  leds:
    count: 128
    type: null
    note: 16x8 LED raster display (not addressable RGB)
  display: LED matrix 16x8
  connectivity:
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to Hackaday Berlin 2023 attendees as the event's conference badge.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/170385-v0j4/details
  url: https://hackaday.io/project/170385-v0j4/details
  kind: hackaday
- label: hackaday.io/berlin2023
  url: https://hackaday.io/berlin2023/
  kind: hackaday
- label: hackaday.com/2023/03/14/hackaday-berlin-the-badge-workshops-and-lightning-talks
  url: https://hackaday.com/2023/03/14/hackaday-berlin-the-badge-workshops-and-lightning-talks/
  kind: article
- label: badge.gallery/badges/hackaday-berlin-2023-voja4
  url: https://badge.gallery/badges/hackaday-berlin-2023-voja4
  kind: website
- label: commons.wikimedia.org/.../Hackaday_Berlin_2023_electronic_badge_Voja4
  url: https://commons.wikimedia.org/wiki/Category:Hackaday_Berlin_2023_electronic_badge_Voja4_designed_by_Voja_Antoni%C4%87
  kind: website
images:
  - file: assets/images/badges/hackaday-berlin-2023/hackaday-berlin-2023-voja4-badge/58565a4228.jpg
    source: "https://commons.wikimedia.org/wiki/Category:Hackaday_Berlin_2023_electronic_badge_Voja4_designed_by_Voja_Antoni%C4%87"
    credit: "Mitch Altman (CC BY-SA 2.0, via Flickr/Wikimedia Commons)"
    caption: "Attendee holding the Hackaday Berlin 2023 Voja4 badge"
contact: {}
notes:
- Official Hackaday Berlin 2023 conference badge, a Berlin-themed revision of the 2022 Supercon Voja4 4-bit computer-trainer badge with SAO expansion; not yet filed under a hackaday-berlin-2023 event. Found by the event-year sweep, task hackaday-europe.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/170385-v0j4/details
  title: Hackaday Berlin 2023 Voja4 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:hackaday-europe); event read as ''hackaday-berlin-2023''.'
- kind: url
  url: https://hackaday.io/project/170385-v0j4/details
  title: v0j4 (Voja4) project page
  accessed: '2026-09-08'
  note: 'Describes the underlying v0j4 architecture; this hackaday.io page mainly covers the original 2020/2022 badge, not a Berlin-specific revision.'
- kind: url
  url: https://badge.gallery/badges/hackaday-berlin-2023-voja4
  title: badge.gallery - Hackaday Berlin 2023 Voja4 Badge
  accessed: '2026-09-08'
  note: 'Confirms the badge was a Berlin re-skin of the Voja4 for the March 25-26 2023 event at MotionLab.Berlin; notes no Berlin-specific firmware/schematic/Gerbers were recovered.'
- kind: url
  url: https://hackaday.com/2023/03/14/hackaday-berlin-the-badge-workshops-and-lightning-talks/
  title: 'Hackaday Berlin: The Badge, Workshops, And Lightning Talks'
  accessed: '2026-09-08'
  note: 'Confirms the badge was "re-skinned for Berlin, with a couple hardware tweaks" and "100% compatible" with the Supercon 2022 badge; attendees received it with their tickets; mentions community mods like a punchcard reader.'
- kind: url
  url: https://commons.wikimedia.org/wiki/Category:Hackaday_Berlin_2023_electronic_badge_Voja4_designed_by_Voja_Antoni%C4%87
  title: 'Wikimedia Commons: Hackaday Berlin 2023 electronic badge Voja4'
  accessed: '2026-09-08'
  note: 'Source of the photo used here; photos by Mitch Altman, CC BY-SA 2.0, taken at the event March 25-26 2023.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, distinct badge: the official Hackaday Berlin 2023 conference badge, a Berlin re-skin of Voja Antonic''s 2022 Supercon Voja4 4-bit computer-trainer, "100% compatible" with that design per Hackaday''s own article. No Berlin-specific firmware, schematic, BOM, or Gerber archive was located (badge.gallery notes the same gap), so make_your_own.open_source is set to partial (design lineage and general Voja4 firmware/hardware are open, but no Berlin-specific repo was found) rather than a hard yes. Price and production quantity are not published anywhere found; it was distributed free with event admission, so get_one.price/quantity are left empty. tech.leds.type left null since the display is a driven LED matrix, not addressable RGB LEDs.'
last_modified_date: '2026-09-08'
---

The Hackaday Berlin 2023 badge is a Berlin-themed re-skin of Voja Antonic's Voja4, the 4-bit "computer trainer" badge that first appeared at Hackaday Supercon 2022. Functionally it is "100% compatible" with that original: a PIC24 microcontroller emulates a small 4-bit Harvard-architecture CPU with 4,096 words of instruction memory, 256 nibbles of data memory, 16 registers, and an 8-level stack, with program and memory state visualized on a 16x8 LED raster display. It was handed out to attendees at Hackaday Berlin 2023, held March 25-26, 2023 at MotionLab.Berlin, as their conference badge.

The badge continues the lineage of Antonic's earlier retrocomputing designs (including badges for Hackaday Belgrade and BalCCon), teaching computing fundamentals by having attendees write and step through actual machine code rather than a high-level language. At the Berlin event, attendees extended the platform further, including building a working punchcard reader for it and contributing software.

No Berlin-specific firmware repository, schematic, BOM, or Gerber archive turned up in this pass; the general Voja4 architecture and prior badge revisions are documented on Voja Antonic's Hackaday.io project pages, but a Berlin-specific hardware/firmware fork was not located.
