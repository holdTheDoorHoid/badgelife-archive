---
title: Falken Wombat Badge (BSides Adelaide)
id: other-falken-wombat-badge-bsides-adelaide
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2024
makers:
- name: Hackerware.io
  url: https://www.hackerware.io/
summary: A full-colour UV-printed CTF badge made for BSides Adelaide 2024, depicting the con's wombat mascot mid-transformation into a cyborg.
functions: 'Runs a CTF: an RGB LED lights by default, and six SMD LEDs on the badge each correspond to a separate challenge, lighting up as solvers find the correct flags. A Micro-USB port is used for interfacing during the CTF, with a coin cell and supporting components mounted on the back.'
look:
  colors: [multicolor]
  shape: null
  themes: [animal, robot, cyborg, ctf, security]
tech:
  mcu: null
  leds: null
  display: null
  connectivity: [usb]
  battery: coin cell
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed to attendees of BSides Adelaide 2024; a soldering village at the conference let attendees solder their own LEDs onto the badge.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.hackster.io/HacksFromPanda/the-falken-wombat-badge-bsides-adelaide-8c1db3
  url: https://www.hackster.io/HacksFromPanda/the-falken-wombat-badge-bsides-adelaide-8c1db3
  kind: article
- label: hackerware.io/wombat
  url: https://hackerware.io/wombat
  kind: website
images:
  - file: assets/images/badges/other/falken-wombat-badge-bsides-adelaide/7c5703f2d3.jpg
    source: "https://hackerware.io/wombat"
    credit: "Hackerware.io"
    caption: "The Falken Wombat Badge, full-colour UV printed CTF badge for BSides Adelaide"
contact: {}
notes:
- 'Cyborg wombat design, full-colour UV printing, CTF.'
- 'A sequel, "The FALKEN Wombat Badge 2", was made by the same team for BSides Adelaide 2025 with a different (button/binary) CTF mechanism; see other_items_found.'
- 'No "BSides Adelaide" event id exists in _data/events.yml, so event is left as "other" per the research guide; the con and year are BSides Adelaide, 2024.'
status: released
sources:
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-falken-wombat-badge-bsides-adelaide-8c1db3
  title: Falken Wombat Badge (BSides Adelaide)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''BSides Adelaide''.'
- kind: url
  url: https://hackerware.io/wombat
  title: The BSides Adelaide Wombat Badge
  accessed: '2026-09-07'
  note: 'Maker''s own project page; confirms it is a full-colour UV printed CTF badge for BSides Adelaide, credited Hackerwares 2024; source of the badge photo.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'hackster.io blocked automated fetches (Cloudflare 403); details drawn from search-result summaries of that page plus the maker''s own hackerware.io/wombat page. MCU, LED count/type, display, exact price, and quantity made were not stated by any source found and are left empty. Year (2024) and CTF mechanism (RGB LED default, 6 SMD LEDs per challenge, Micro-USB interface, coin cell) come from search-indexed hackster.io content; could not verify directly on the page due to the block.'
last_modified_date: '2026-09-07'
---

The Falken Wombat Badge was made by Hackerware.io (Abhinav SP) for BSides Adelaide 2024. It reimagines the conference's wombat mascot as a cyborg, rendered across the PCB in full-colour UV printing. The badge doubles as a capture-the-flag challenge: an RGB LED runs by default, while six SMD LEDs each represent a separate CTF challenge and light up as attendees find the corresponding flags.

Interfacing for the CTF ran over a Micro-USB port, with a coin cell and supporting components mounted on the back of the board. At the conference, a soldering village let attendees solder their own LEDs onto the badge in colors of their choosing, personalizing it as they went.

The badge's success led to a follow-up, the FALKEN Wombat Badge 2, made by the same team for BSides Adelaide 2025 with a reworked, USB-free CTF built around binary switch input.
