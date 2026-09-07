---
title: Shoot My Valentine
id: other-shoot-my-valentine
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: unknown
event: other
year: 0
makers: []
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/158740-shoot-my-valentine
  url: https://hackaday.io/project/158740-shoot-my-valentine
  kind: hackaday
images: []
contact: {}
notes: []
status: not_an_item
sources:
- kind: url
  url: https://hackaday.io/project/158740-shoot-my-valentine
  title: Shoot My Valentine
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://github.com/kramarb/basic-badge
  title: 'kramarb/basic-badge (BASIC interpreter for the Hackaday Belgrade 2018 badge)'
  accessed: '2026-09-07'
  note: 'Confirms this is firmware/a game written for the existing 2018 Hackaday Belgrade conference badge (PIC32MX370F512H), not a standalone badge or SAO design.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    Not a distinct badge/SAO. "Shoot My Valentine" is a two-player spacecraft
    combat game (missile limit, gradual reload, win-on-hit) written by
    hackathon participants (kramarb, Jure Potočnik, Marko Kočevar, jasmina.satler)
    at Hackaday Belgrade Conference 2018, running as software on two units of
    the official 2018 Hackaday Belgrade conference badge (hardware by Voja
    Antonic, PIC32MX370F512H MCU, BASIC interpreter firmware from
    github.com/kramarb/basic-badge). The badge itself already has its own
    archive entry elsewhere (or would need one under a Hackaday Belgrade event,
    which does not currently exist in events.yml); this project page documents
    a game demo, not new hardware. No event id for "Hackaday Belgrade" exists
    in _data/events.yml, so event is left as 'other'.
last_modified_date: '2026-09-07'
---

"Shoot My Valentine" is a two-player game written for the official 2018 Hackaday Belgrade conference badge, not a badge or SAO in its own right. Built by kramarb, Jure Potočnik, Marko Kočevar, and jasmina.satler at the Hackaday Belgrade Conference in May 2018, it turns the badge into a head-to-head spacecraft shooter: each player's ship fires missiles at the other's across a shared battlefield, with a missile limit and gradual reload to keep either side from spamming shots, and the game ends when one ship lands a hit.

The badge it runs on was designed by Voja Antonic (hardware) and Jaromir Sukuba (software) around a PIC32MX370F512H microcontroller, and shipped with a built-in BASIC interpreter that let attendees write and run their own programs directly on the hardware. The game's source lives in the `kramarb/basic-badge` GitHub repository, which is the interpreter/firmware codebase for that badge rather than a hardware project of its own.

Because this is a software demo for existing conference hardware, it does not fit the archive's badge/SAO schema as a standalone item, and is flagged as not-an-item rather than filled in as a badge.
