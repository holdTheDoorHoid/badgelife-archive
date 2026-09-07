---
title: Dial-Badge
id: other-dial-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2023
makers:
- name: Michael Möller
  url: https://hackaday.io/Msquare
summary: 'A vintage rotary telephone dial wired to the stock Supercon conference badge at Hackaday Berlin 2023, so a dialed number shows up on the badge''s display.'
functions: 'Detects rotary-dial pulses and counts them to determine the dialed digit, shows the digit in a register on the badge''s default display page, and includes a Matrix-style falling-lines display mode.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
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
  availability: not_released
  distribution: []
  where: 'One-off contest build, not distributed.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://hackaday.io/project/190236-dial-badge
  eda_tool: null
links:
- label: hackaday.io/project/190236-dial-badge
  url: https://hackaday.io/project/190236-dial-badge
  kind: hackaday
images:
  - file: assets/images/badges/other/dial-badge/908ea081b2.jpg
    source: "https://hackaday.io/project/190236-dial-badge"
    credit: "Michael Möller"
    caption: "Telephone dial wired to the Supercon badge with a cardboard mount"
  - file: assets/images/badges/other/dial-badge/f7c69e1cbc.jpg
    source: "https://hackaday.io/project/190236-dial-badge"
    credit: "Michael Möller"
    caption: "Dialed digit shown on the badge's display"
contact: {}
notes:
- 'Sheet title was "Dial Badge"; the maker''s own project title is "Dial-Badge".'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/190236-dial-badge
  title: Dial Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/190236-dial-badge
  title: Dial-Badge | Hackaday.io
  accessed: '2026-09-07'
  note: 'Project description, photos, and code files confirming maker, event, and functions.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a small badge-hack entry for the "small badge-hack" contest at Hackaday Berlin 2023 (March 2023), not a standalone manufactured badge or SAO: the maker attached an old telephone dial to the stock conference (Supercon-style) badge issued at that event and wrote software so the dialed number shows on the badge''s display. It won "Best in Hardware Category" in that contest. No matching event id exists in events.yml for Hackaday Berlin 2023 (the closest is hackaday-europe-2025, a different year in the same Berlin series), so event is left as "other" per the research guide. MCU/chip, LED count, display type, and battery are not stated on the project page for the dial hack itself (they belong to the host badge, which the maker says he never even read documentation for). Five hand-assembled code files are posted on the project page as plain text; no schematic or PCB files were published since the "hardware" is a dial, a scrap of cardboard, and masking tape.'
last_modified_date: '2026-09-07'
---

Michael Möller entered this hack into the "small badge-hack" contest held alongside Hackaday Berlin 2023 in March 2023, and won Best in Hardware Category. He'd brought an old rotary telephone dial to the event for unrelated reasons, and on a whim wired it into the conference's stock Supercon-style badge, writing software so that rotating the dial and counting the resulting pulses would display the dialed digit on the badge's screen. For "extra credit" he did the whole thing without ever reading the badge's documentation or using an assembler — the firmware was hand-assembled and binary-edited directly, and the physical mount was cardboard, a pocket knife, and masking tape (with a borrowed soldering iron for the wiring).

Beyond showing the last dialed digit, the software adds a Matrix-style display mode with falling lines. The project page hosts five plain-text files of the hand-coded assembly as the only published "source," alongside a demo video and photos of the dial mounted to the badge.

This is a one-off contest entry rather than a produced/distributed badge or SAO, so quantity, price, and availability fields don't apply beyond "not released" — no one but Möller has one.
