---
title: BSidesJAX 2024 Hydra Badge
id: other-bsidesjax-2024-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2024
makers:
- name: blackandwhitehat / Panda
summary: A learn-to-solder badge kit shaped like a hydra head, assembled by attendees at the BSides Jacksonville 2024 Soldering Village.
functions: 'No electronic functions beyond lighting two attendee-chosen LEDs; the badge itself is a soldering exercise, not an interactive device.'
look:
  colors:
  - blue
  - gold
  shape: dragon
  themes:
  - fantasy
  - learn to solder
  - village badge
tech:
  mcu: none
  leds:
    count: 2
    type: null
    note: Two LEDs "of your choosing" supplied or chosen by the attendee, not fixed by the design.
  display: none
  connectivity: []
  battery: coin cell (holder + battery included; exact type not stated)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  - kit
  where: Distributed to attendees at the BSides Jacksonville 2024 Soldering Village to assemble on site.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/blackandwhitehat/BSidesJAX_2024_Badge
  url: https://github.com/blackandwhitehat/BSidesJAX_2024_Badge
  kind: repo
- label: 2024 Hydra Badge Assembly Video (YouTube)
  url: https://www.youtube.com/watch?v=xDVRaMgNc40
  kind: video
images:
  - file: assets/images/badges/other/bsidesjax-2024-badge/b2e81c1000.jpg
    source: "https://www.youtube.com/watch?v=xDVRaMgNc40"
    credit: "blackandwhitehat"
    caption: "Hydra Badge assembly video thumbnail showing the blue hydra-head shaped PCB badge with gold SMD components and attendee name field"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- 'No matching event id exists in events.yml for BSides Jacksonville 2024 (only bsides-jacksonville-2018 and bsides-jacksonville-2023 are defined); event left as "other" pending that entry being added.'
status: released
sources:
- kind: url
  url: https://github.com/blackandwhitehat/BSidesJAX_2024_Badge
  title: BSidesJAX 2024 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''bsides-jacksonville-2024 (if it exists) or other''.'
- kind: url
  url: https://raw.githubusercontent.com/blackandwhitehat/BSidesJAX_2024_Badge/main/Readme.md
  title: 'Readme.md - Badge Assembly Instructions'
  accessed: '2026-09-07'
  note: Confirmed the badge's real name ("2024 Hydra Badge"), that it is a two-circuit Soldering Village learn-to-solder kit (through-hole LEDs/switch/battery/SAO header on Circuit 1, SMD components on Circuit 2), and assembly methods (iron and hotplate).
- kind: url
  url: https://www.youtube.com/watch?v=xDVRaMgNc40
  title: BSides Jacksonville Hydra Badge Assembly video thumbnail
  accessed: '2026-09-07'
  note: Thumbnail image shows the actual badge — a blue PCB shaped like a hydra/dragon head with gold SMD components and an attendee name field, confirming shape and colors.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The GitHub repo contains only assembly instructions (no schematics, gerbers, or BOM), so hardware/firmware openness, exact MCU (there likely isn't one — it reads as a passive learn-to-solder board with no microcontroller), LED type, exact battery type, SAO header version, price, and quantity made could not be confirmed from any source and are left empty. No maker storefront, Hackaday page, or press coverage was found beyond the GitHub repo and its linked YouTube video.
last_modified_date: '2026-09-07'
---

The BSidesJAX 2024 Hydra Badge is a learn-to-solder kit built for the Soldering Village at BSides Jacksonville 2024, made by a maker going by blackandwhitehat (also credited as "Panda"). The PCB is cut into the shape of a hydra or dragon head in blue soldermask with gold-finished pads, and doubles as the attendee's name badge (it carries printed "ATTENDEE" and "NAME" fields).

Assembly happens in two stages, walked through in an accompanying YouTube video and a written guide. Circuit 1 is through-hole: attendees solder a switch, battery holder and battery, an SAO header, and two LEDs of their own choosing to light up the board. Circuit 2 is a surface-mount exercise, with small SMD components sorted and soldered by color, taught with both a hand iron and a hotplate/reflow method. The badge does not appear to carry a microcontroller — its purpose is the soldering exercise itself rather than any onboard logic, game, or radio feature.

No storefront, price, or production quantity could be found; it reads as a free workshop kit given to attendees who took part in the Soldering Village rather than a badge that was sold. No hardware design files (schematics, Gerbers, or a BOM) are published in the linked repository, which contains only the assembly instructions.

