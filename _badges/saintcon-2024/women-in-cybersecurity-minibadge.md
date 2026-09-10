---
title: Women In Cybersecurity minibadge
id: saintcon-2024-women-in-cybersecurity-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: SHIFTY
summary: A community minibadge honoring Women in Cybersecurity, designed by SHIFTY for SAINTCON 2024's minibadge trading community.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: 'none'
  leds:
    count: 2
    type: discrete
    note: Two through-hole LEDs, each with its own current-limiting resistor; no driver IC.
  display: 'none'
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - swap
  where: Traded in person at SAINTCON 2024's Minibadge Community space.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Women%20In%20Cybersecurity%20-%20SHIFTY
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Women%20In%20Cybersecurity%20-%20SHIFTY
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Women%20In%20Cybersecurity%20-%20SHIFTY
  kind: repo
- label: SAINTCON Minibadge Community
  url: https://saintcon.org/minibadges/
  kind: website
images: []
contact: {}
notes:
- Women In Cybersecurity community minibadge for SAINTCON 2024, credited to SHIFTY. Found by the event-year sweep, task saintcon-2024.
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Women%20In%20Cybersecurity%20-%20SHIFTY
  title: Women In Cybersecurity minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Women%20In%20Cybersecurity%20-%20SHIFTY/Women%20In%20Cybersecurity%20-%20SHIFTY.kicad_sch
  title: Women In Cybersecurity - SHIFTY.kicad_sch
  accessed: '2026-09-10'
  note: 'Schematic confirms 2 LEDs, 2 resistors, and a MiniBadge:MiniBadge_Simple connector footprint (no MCU) - a passive LED minibadge powered through the host badge''s minibadge connector.'
- kind: url
  url: https://saintcon.org/minibadges/
  title: MiniBadges - SAINTCON
  accessed: '2026-09-10'
  note: 'Confirms the MiniBadge community at SAINTCON is led by SHIFTY and distinctm1nd, who coordinate submitted/official minibadges traded at the conference each year; general community context, does not name this specific badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The GitHub repo (utahsaint-org/MiniBadges2024, a collection of SAINTCON 2024 minibadge design files) confirms this is a real, fabricated minibadge design credited to SHIFTY, with KiCad schematic/PCB, SVG artwork, and PSD source files - not just a sweep snippet. The schematic shows a simple 2-LED circuit on the standard MiniBadge_Simple connector footprint (powered by the host conference badge, no onboard MCU). Could not find price, quantity made, or a photo of the assembled badge: the repo''s own PNG exports are flat gerber-layer renders (copper/mask/silkscreen) that did not reproduce as usable photos, and a 38 MB SAINTCON 2024 MiniBadge Build Guide PDF (linked from saintcon.org) likely documents it but was too large to search within the research budget for this pass. No dedicated maker page or trading-history writeup for this specific badge was found beyond the repo and the general SAINTCON Minibadge Community pages.'
last_modified_date: '2026-09-10'
---

The Women In Cybersecurity minibadge is a small trading PCB designed by SHIFTY for SAINTCON 2024's Minibadge Community, the con's long-running badge-trading and -making scene (led by SHIFTY and distinctm1nd). Its KiCad source lives in the `utahsaint-org/MiniBadges2024` GitHub repository alongside dozens of other 2024 SAINTCON minibadges, in a folder named "Women In Cybersecurity - SHIFTY."

Electrically it is a simple, unpowered minibadge: the schematic shows two LEDs, each with its own current-limiting resistor, wired to a standard `MiniBadge_Simple` connector footprint. There is no microcontroller on board - it draws power through the pogo-pin/edge connector from whichever host badge it is plugged into, in keeping with the SAINTCON minibadge standard.

Design files (KiCad schematic and PCB, plus SVG and Photoshop artwork sources) are published in the repo, but no storefront listing, price, production quantity, or photo of the finished, assembled badge was found. It was most likely made available through in-person trading at SAINTCON 2024 rather than sold, consistent with how the Minibadge Community typically distributes submissions.

## Make your own

The KiCad project (schematic and PCB layout) is in the linked GitHub repository under "Women In Cybersecurity - SHIFTY." No firmware is involved since the board has no MCU; building one would mean fabricating the PCB from the KiCad files, populating two LEDs and two resistors, and adding a MiniBadge-standard connector to plug into a host badge.
