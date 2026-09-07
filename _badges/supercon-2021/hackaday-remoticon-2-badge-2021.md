---
title: Hackaday Remoticon 2 Badge (2021)
id: supercon-2021-hackaday-remoticon-2-badge-2021
layout: badge
parent: Hackaday Supercon 2021
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2021
year: 2021
makers:
- name: Thomas Flummer
  url: https://hackaday.io/hacker/41938-thomas-flummer
summary: A do-it-yourself KiCad badge design released for the 2021 virtual Remoticon.2 (Hackaday Supercon 2021), meant to be fabbed and populated by the attendee rather than handed out finished.
functions: 'Ships as a bare canvas: a grid of 0.1" pads that the builder removes and replaces with whatever parts they have on hand. The designer''s own build used it as a carrier for a custom RISC-V MicroMod module, with joystick, USB through-hole pins, and a screen connector populated.'
look:
  colors:
  - purple
  shape: rectangle
  themes:
  - retro computer
  - kit
  - hardware tool
tech:
  mcu: null
  leds: null
  display: 0.1" pad grid, or a screen when the builder adds one
  connectivity:
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution:
  - kit
  where: 'Not distributed as a finished badge. Files were shared for attendees to order their own boards; the designer also posted OSH Park "shared project" order links for two variants (the MicroMod carrier and the plain 0.1" pad version) so people could order without editing the files themselves.'
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/182027-remoticon-2-badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.com/2021/11/10/the-hackaday-remoticon-2-badge-an-exercise-in-your-own-ingenuity
  url: https://hackaday.com/2021/11/10/the-hackaday-remoticon-2-badge-an-exercise-in-your-own-ingenuity/
  kind: article
- label: Remoticon 2 badge (Hackaday.io project)
  url: https://hackaday.io/project/182027-remoticon-2-badge
  kind: hackaday
- label: OSH Park shared project — MicroMod carrier variant
  url: https://oshpark.com/shared_projects/gRSf01dV
  kind: fab
- label: OSH Park shared project — plain 0.1" pad variant
  url: https://oshpark.com/shared_projects/YJqAizIf
  kind: fab
images:
- file: assets/images/badges/supercon-2021/hackaday-remoticon-2-badge-2021/a71a89a447.jpg
  source: "https://hackaday.io/project/182027-remoticon-2-badge"
  credit: "Thomas Flummer"
  caption: "The Remoticon.2 badge PCB, a purple OSH Park board with joystick and USB pads"
- file: assets/images/badges/supercon-2021/hackaday-remoticon-2-badge-2021/fd59bd9bc3.jpg
  source: "https://hackaday.io/project/182027-remoticon-2-badge"
  credit: "Thomas Flummer"
  caption: "Two Remoticon.2 badges after hand-soldering their SMT spacers"
contact: {}
notes:
- Hackaday.io lists the project title as "Remoticon 2 badge"; this entry keeps the sheet's fuller title.
- 'The designer built his own example around a custom RISC-V MicroMod module he designed himself (not a commercial SparkFun part); as of a Nov. 2021 comment he had not yet published that module''s own files, so it is not counted here as part of this project''s open-source release.'
- The Hackaday.com writeup describes the KiCad files as released under a CC BY-SA license; this was not independently confirmed on the Hackaday.io project page itself.
- No fixed price, quantity, or finished-badge distribution channel was found — this was a file release for self-fabrication, not a badge handed out or sold as a unit.
status: listed
sources:
- kind: url
  url: https://hackaday.com/2021/11/10/the-hackaday-remoticon-2-badge-an-exercise-in-your-own-ingenuity/
  title: Hackaday Remoticon 2 Badge (2021)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''Hackaday Remoticon 2 (virtual Supercon)''.'
- kind: url
  url: https://hackaday.com/2021/11/10/the-hackaday-remoticon-2-badge-an-exercise-in-your-own-ingenuity/
  title: 'The Hackaday Remoticon 2 Badge: An Exercise In Your Own Ingenuity'
  accessed: '2026-09-07'
  note: Identified designer (Thomas Flummer), confirmed KiCad file release and CC BY-SA license claim, and linked to the Hackaday.io project page.
- kind: url
  url: https://hackaday.io/project/182027-remoticon-2-badge
  title: Remoticon 2 badge (Hackaday.io)
  accessed: '2026-09-07'
  note: Primary source for description, functions, files (KiCad/Gerbers/artwork), OSH Park shared-project links, photos, and the designer's comment about the unreleased RISC-V MicroMod module.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (maker, event, what it is, how it was released) confirmed on the maker's own Hackaday.io project page. Price/quantity/availability fields left empty because this was never sold or handed out as a finished unit. Firmware is not applicable (no MCU in the base design).
last_modified_date: '2026-09-07'
---

Thomas Flummer designed the Remoticon.2 badge as a KiCad file release rather than a physical product: a purple PCB (matching OSH Park's signature purple) with a grid of 0.1" pads that attendees of the virtual 2021 Hackaday Supercon (branded "Remoticon.2") could strip out and replace with whatever parts they already had, while keeping silkscreen artwork tying it to the event's visual identity. It was a pandemic-era answer to the usual conference badge drop: instead of a finished board shipped to everyone, Flummer posted the KiCad project, Gerbers, and artwork files so people could order their own boards from a fab in time for the event, or use two OSH Park "shared project" links he set up for a MicroMod-carrier variant and a plain pad-grid variant.

Flummer's own build fitted the MicroMod-footprint variant with a RISC-V MicroMod module of his own design, along with joystick connectors, USB through-hole pins, and a screen. In a comment thread on the project he noted that module's own design files weren't public yet, so the badge itself remains open source but that specific carrier board he photographed is not fully reproducible from the published files alone.

## Make your own

The full badge is published on the project's Hackaday.io page: a KiCad project (`remoticon.2.badge.micromod.zip`), matching Gerbers and stencil files, and an Adobe Illustrator artwork file with per-layer PNG exports. Two ready-to-order OSH Park shared-project links are also available for people who don't want to edit the files themselves — one for the MicroMod carrier layout, one for the simpler 0.1"-pad-only version.
