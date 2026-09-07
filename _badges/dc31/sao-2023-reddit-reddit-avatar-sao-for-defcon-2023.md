---
title: sao-2023-reddit — Reddit avatar SAO for DEFCON 2023
id: dc31-sao-2023-reddit-reddit-avatar-sao-for-defcon-2023
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: pale-shadow
  url: https://github.com/pale-shadow
summary: A Reddit "Snoo" mascot-shaped PCB pendant made for DEF CON 31, wearing a reddit-logo medallion silkscreened "r/Defcon 2023".
functions: Lights two reverse-mount LEDs from an onboard coin-cell battery; no other electronics.
look:
  colors: []
  shape: mascot
  themes:
  - mascot
  - meme
  - pop culture
tech:
  mcu: none
  leds:
    count: 2
    type: PLCC-2 reverse-mount
    note: Wired in parallel through a single 0805 current-limiting resistor.
  display: none
  connectivity: []
  battery: CR2032 (Keystone 3002 holder)
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
  hardware_url: https://github.com/pale-shadow/sao-2023-reddit/tree/main/pcb
  firmware_url: null
  eda_tool: KiCad
  gerbers_url: https://github.com/pale-shadow/sao-2023-reddit/tree/main/pcb/gerbers
  notes: Repo also includes the source artwork (GIMP .xcf files) used to trace the silkscreen.
links:
- label: github.com/pale-shadow/sao-2023-reddit
  url: https://github.com/pale-shadow/sao-2023-reddit
  kind: repo
images:
- file: assets/images/badges/dc31/sao-2023-reddit-reddit-avatar-sao-for-defcon-2023/aedd229781.jpg
  source: "https://github.com/pale-shadow/sao-2023-reddit"
  credit: "pale-shadow"
  caption: "3D render of the Reddit Snoo-shaped SAO PCB, with a reddit-logo pendant and 'r/Defcon 2023' silkscreen text on the body"
- file: assets/images/badges/dc31/sao-2023-reddit-reddit-avatar-sao-for-defcon-2023/c3529e9a57.png
  source: "https://github.com/pale-shadow/sao-2023-reddit"
  credit: "pale-shadow"
  caption: "PCB front-copper layout of the Snoo-shaped SAO, from the assembly documentation"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/pale-shadow/sao-2023-reddit
  title: sao-2023-reddit — Reddit avatar SAO for DEFCON 2023
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 2023''.'
- kind: url
  url: https://raw.githubusercontent.com/pale-shadow/sao-2023-reddit/main/README.md
  title: sao-2023-reddit README
  accessed: '2026-09-07'
  note: Confirms title "Shitty Add-On of Reddit avatar for DEFCON 2023" and points to the assembly-page silkscreen images.
- kind: url
  url: https://github.com/pale-shadow/sao-2023-reddit/tree/main/artwork
  title: sao-2023-reddit artwork directory listing
  accessed: '2026-09-07'
  note: Lists the source artwork (reddit.jpg render, GIMP .xcf files, KiCad silkscreen modules, PDF, assembly page PNGs) used to build the image set for this entry.
- kind: url
  url: https://github.com/pale-shadow/sao-2023-reddit/tree/main/pcb
  title: sao-2023-reddit pcb directory listing
  accessed: '2026-09-07'
  note: Confirms KiCad schematic/PCB files and a gerbers/ subfolder are published.
- kind: url
  url: https://raw.githubusercontent.com/pale-shadow/sao-2023-reddit/main/pcb/reddit.kicad_sch
  title: reddit.kicad_sch (raw schematic)
  accessed: '2026-09-07'
  note: Component list -- BT1 coin-cell holder (Keystone 3002), D1/D2 PLCC-2 reverse-mount LEDs, R1 0805 resistor. No SAO header/connector component present.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The maker's own GitHub repo (org "pale-shadow", README credits user DEAD10C5) confirms this is a
    Reddit "Snoo" mascot-shaped PCB made for DEF CON 31 (2023); corrected event from "other" to dc31
    per events.yml. Despite being named and typed as a "SAO", the published schematic contains no SAO
    connector at all -- just a CR2032 coin-cell holder, two reverse-mount LEDs, and a series resistor --
    so tech.sao_version is set to "none" rather than guessed; it reads as a standalone battery-powered
    blinky pendant that borrows the "shitty add-on" name/format without actually plugging into a
    badge's SAO header. No price, quantity, or distribution details were published anywhere in the
    repo, and no Hackaday.io page, storefront, or social post about it could be found, so get_one
    fields and look.colors are left empty rather than inferred from the KiCad 3D-render colors (which
    are EDA defaults, not necessarily the real solder-mask color). A different, unrelated SAO --
    dc31-defcon-subreddit-sao by maker MetaN3rd, also Reddit/r/Defcon-themed and also DEF CON 31 -- is
    not a duplicate of this entry; they are two separate projects by two separate makers.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/sao-2023-reddit-reddit-avatar-sao-for-defcon-2023/
---

A GitHub user going by pale-shadow (repo credits DEAD10C5) designed this PCB as a "Shitty Add-On" for DEF CON 31 in 2023: a two-layer board cut into the outline of Reddit's alien mascot "Snoo," with a small reddit-logo medallion and "r/Defcon 2023" silkscreened onto its belly. Electrically it is deliberately minimal -- a CR2032 coin cell in a Keystone 3002 holder lights two reverse-mount PLCC-2 LEDs through a single current-limiting resistor, with no microcontroller and, notably, no SAO connector footprint anywhere in the published schematic, so it appears to be a self-contained blinky rather than something that actually plugs into a host badge.

The repository publishes the full KiCad source (schematic, PCB layout, gerbers) along with the original GIMP artwork used to trace the mascot silkscreen, so the design is fully reproducible even though no firmware is involved. No pricing, production quantity, or distribution details for the physical item were published anywhere the research could find -- no Hackaday.io page, storefront listing, or social post turned up beyond the repo itself.
