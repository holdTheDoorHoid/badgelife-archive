---
title: Bug Bounty Village Badge
id: dc34-bug-bounty-village-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Abhinav Panda / Hackerware.io
  url: https://hackerware.io
summary: A laser-cut acrylic badge for the DEF CON 34 Bug Bounty Village depicting a hooded, masked figure ringed with RGB LEDs, built around a five-flag binary CTF solved with three buttons.
functions: Five-flag binary CTF puzzle solved using three physical buttons (MENU, 0, 1), a customizable OLED display, and user-selectable RGB LED team colors
look:
  colors:
  - black
  - multicolor
  shape: hooded figure
  themes:
  - security
  - ctf
  - hardware tool
  - hacker
tech:
  mcu: ATmega32
  leds:
    count: null
    type: RGB
    note: Programmable RGB perimeter lighting ringing the hooded-figure artwork; team color is user-selectable.
  display: OLED (custom, user-customizable content)
  connectivity: []
  inputs:
  - buttons
  battery: null
  sao_version: none
get_one:
  price: Free Giveaway
  price_usd: 0.0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  - village
  where: Given away in person at the DEF CON 34 Bug Bounty Village, sponsored by Intigriti
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: x.com/BugBountyDEFCON/status/2085018218762997884?s=20
  url: https://x.com/BugBountyDEFCON/status/2085018218762997884?s=20
  kind: video
- label: Hackerware.io - Bug Bounty Village Badge 2026 (DEF CON 34)
  url: https://hackerware.io/bbv2026
  kind: website
- label: Hackerware.io / Hackerwares.in (maker portfolio)
  url: https://hackerwares.in
  kind: website
images:
- file: assets/images/badges/dc34/bug-bounty-village-badge/7438068d90.jpg
  source: "https://hackerwares.in"
  credit: "Hackerware.io / Abhinav Panda"
  caption: "Bug Bounty Village badge: hooded masked figure design with RGB LED ring, OLED display, and MENU/CTF/0/1 buttons"
contact:
  discord: abhinav_panda
  emails:
  - abhinav@hackerwares.in
  raw:
  - 'Twitter: TweetsFromPanda'
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 64
  updated: 8/7/2026 18:21:39
  listing: New
- kind: url
  url: https://x.com/BugBountyDEFCON/status/2085018218762997884?s=20
  title: "Bug Bounty Village on X: announcing the DEF CON 34 badge"
  accessed: '2026-09-06'
  note: Announcement post confirming Intigriti sponsorship and free in-person giveaway; carries an og:image video thumbnail of the badge.
- kind: url
  url: https://hackerware.io/bbv2026
  title: Bug Bounty Village Badge 2026 - DEF CON 34
  accessed: '2026-09-06'
  note: Maker's own project page; source for MCU (ATmega32), OLED display, RGB LEDs, five-flag CTF with three buttons, and the hooded-figure design.
- kind: url
  url: https://hackerwares.in
  title: Hackerware.io portfolio
  accessed: '2026-09-06'
  note: Confirms the badge is by Hackerware.io/Abhinav Panda and provided the gallery photo (g-bbv.jpg) used above.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts (MCU, display, LEDs, CTF mechanic) come from the maker's own project page. Exact LED count, quantity produced, and open-source status were not stated anywhere found; left empty rather than guessed.
last_modified_date: '2026-09-06'
---

The Bug Bounty Village badge for DEF CON 34 is a laser-cut acrylic badge mounted on a fully assembled PCB, built by Abhinav Panda of Hackerware.io. The artwork depicts a hooded, masked figure at a laptop, ringed with programmable RGB LEDs on a black board, with MENU, CTF, 0, and 1 buttons and a small customizable OLED display. Bug Bounty Village announced the badge in August 2026, crediting Intigriti as the sponsor that made a free, in-person giveaway of "heaps" of the badges possible at the con.

Functionally, the badge centers on a five-flag binary CTF that attendees solve using the three physical buttons, with the OLED display and RGB LED team color both configurable by the wearer. It runs on an ATmega32 microcontroller. No SAO header, no open-source hardware or firmware release, and no exact production quantity were found in the sources checked; those fields are left blank rather than guessed.
