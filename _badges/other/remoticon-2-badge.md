---
title: Remoticon 2 badge
id: other-remoticon-2-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2021
makers:
- name: Thomas Flummer
  url: https://hackaday.io/tf
summary: A DIY badge kit for Hackaday's virtual Remoticon 2 (2021) conference, distributed as open KiCad files rather than a finished board so attendees could fab and populate it with whatever parts they had on hand.
functions: 'A blank prototyping canvas in the Remoticon visual identity: a grid of 0.1" spaced pads for freeform circuitry, with a demonstrated build as a MicroMod carrier board (socket for a MicroMod processor, OLED display, and Qwiic connector).'
look:
  colors:
  - purple
  shape: rectangle
  themes:
  - kit
  - retro computer
tech:
  mcu: MicroMod (any compatible processor board, incl. RISC-V options)
  leds: null
  display: 0.96" OLED (as built by the maker; optional)
  connectivity:
  - i2c
  battery: null
  sao_version: null
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/182027-remoticon-2-badge
  firmware_url: null
  eda_tool: KiCad
  license: CC BY-SA
  notes: Released as KiCad project, Gerber, stencil, and Illustrator artwork files; also shared on OSH Park for direct ordering. No fixed BOM — the badge is meant to be populated with whatever parts the builder has.
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Not distributed as a finished product; attendees ordered the bare PCB themselves from a fab (OSH Park shared project) and self-assembled.
links:
- label: hackaday.io/project/182027-remoticon-2-badge
  url: https://hackaday.io/project/182027-remoticon-2-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260411210325/https://hackaday.io/project/182027-remoticon-2-badge
- label: 'OSH Park: Shared Projects by flummer'
  url: https://oshpark.com/profiles/flummer
  kind: fab
  archived: https://web.archive.org/web/20260420101539/https://oshpark.com/profiles/flummer
- label: 'Hackaday: The Hackaday Remoticon 2 Badge: An Exercise In Your Own Ingenuity'
  url: https://hackaday.com/2021/11/10/the-hackaday-remoticon-2-badge-an-exercise-in-your-own-ingenuity/
  kind: article
  archived: https://web.archive.org/web/20260212200641/https://hackaday.com/2021/11/10/the-hackaday-remoticon-2-badge-an-exercise-in-your-own-ingenuity/
images:
- file: assets/images/badges/other/remoticon-2-badge/1378ac4d73.jpg
  source: https://hackaday.io/project/182027-remoticon-2-badge
  credit: Thomas Flummer
  caption: Remoticon 2 badge PCB, OSH Park purple
  archived: https://web.archive.org/web/20260411210325/https://hackaday.io/project/182027-remoticon-2-badge
- file: assets/images/badges/other/remoticon-2-badge/0d67a4ee14.jpg
  source: https://hackaday.io/project/182027-remoticon-2-badge
  credit: Thomas Flummer
  caption: Remoticon 2 badge, MicroMod carrier build with OLED
  archived: https://web.archive.org/web/20260411210325/https://hackaday.io/project/182027-remoticon-2-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/182027-remoticon-2-badge
  title: Remoticon 2 badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Official 2021 Remoticon 2 badge; KiCad-file badge design attendees could customize/fab themselves''.'
  archived: https://web.archive.org/web/20260411210325/https://hackaday.io/project/182027-remoticon-2-badge
- kind: url
  url: https://hackaday.io/project/182027-remoticon-2-badge
  title: Remoticon 2 badge (project page)
  accessed: '2026-09-07'
  note: Confirmed maker (Thomas Flummer, with contributors oshpark and Cau5tic), event (Remoticon.2, 2021), purple OSH Park PCB, grid of 0.1" pads, MicroMod carrier example with OLED and joystick provisions, KiCad/Gerber/stencil/Illustrator files.
  archived: https://web.archive.org/web/20260411210325/https://hackaday.io/project/182027-remoticon-2-badge
- kind: url
  url: https://hackaday.com/2021/11/10/the-hackaday-remoticon-2-badge-an-exercise-in-your-own-ingenuity/
  title: 'The Hackaday Remoticon 2 Badge: An Exercise In Your Own Ingenuity'
  accessed: '2026-09-07'
  note: Confirms CC BY-SA license, MicroMod carrier with Qwiic connector, and that the badge was distributed purely as design files (no assembled kit) due to the virtual/pandemic-era nature of the event.
  archived: https://web.archive.org/web/20260212200641/https://hackaday.com/2021/11/10/the-hackaday-remoticon-2-badge-an-exercise-in-your-own-ingenuity/
- kind: url
  url: https://github.com/flummer/remoticon2020-badge
  title: 'GitHub: flummer/remoticon2020-badge'
  accessed: '2026-09-07'
  note: Checked for overlap; this is a separate, earlier "unofficial" badge for Remoticon 2020, not the Remoticon 2 (2021) badge in this entry - kept apart to avoid conflating the two.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is Hackaday's own Remoticon (a virtual Hackaday conference held in place of Supercon during the pandemic), not Hackaday Superconference - no matching event id exists in events.yml for "Remoticon 2021" or "Remoticon 2", so event is left as "other". Price, quantity made, and exact LED/battery details were not stated in any source found; left empty rather than guessed. A separate, unrelated "remoticon2020-badge" repo by the same maker exists for the prior year's event and should not be merged with this entry.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/remoticon-2-badge.glb
  method: kicad
  source_file: remoticon.2.badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 351568
---

For Hackaday's 2021 Remoticon 2 - a virtual conference run in place of an in-person Supercon during the pandemic - designer Thomas Flummer took an unusual approach to the "no physical badge distribution is possible" problem: instead of shipping an assembled badge, he released a KiCad design for a purple, OSH Park-style PCB with a grid of 0.1" pads that attendees could order from any fab and populate with whatever parts they already had. The goal was a board that fit Remoticon's visual identity while leaving the actual build entirely up to the maker.

Flummer's own demonstration build used the badge as a MicroMod carrier, with a socket for a MicroMod processor board (including RISC-V options), a Qwiic I2C connector, and a small OLED display, plus room for joystick controls. Because it was released as files rather than a product, there was no official kit, BOM, or price - people who wanted one ordered bare boards themselves, commonly through OSH Park's shared-projects page for the design.

## Make your own

The project is published under a CC BY-SA license with KiCad project files, Gerbers, a stencil file, and Adobe Illustrator artwork for the silkscreen, all linked from the Hackaday.io project page. The board can be ordered as-is from OSH Park's shared project listing or fabricated at any PCB house; no fixed parts list is provided since the design is meant as a blank canvas rather than a finished device.
