---
title: Queercon 15 Badge
id: queercon-2018-queercon-15-badge
layout: badge
parent: Queercon 15 (2018)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: queercon-2018
year: 2018
makers:
- name: Evan Mackay
- name: George Louthan
  url: https://github.com/duplico
- name: Jonathan Nelson
summary: 'The Queercon 15 badge is an electronic con badge, worn at DEF CON 26 (2018), whose real purpose is a collaborative text-adventure game: each badge holds 1/16 of a hidden story file that assembles as attendees exchange data over a wireless link.'
functions: 'Wireless badge-to-badge communication that assembles a shared "Expeditionary Force"-themed story file across the con; on-badge visualizations and animations; six faceplate LEDs that track collective game progress; a scoreboard at the Queercon suite that queries nearby badges; a cake recipe hidden in copper-layer micro-lettering as an easter egg.'
look:
  colors: [black]
  shape: null
  themes: [sci-fi, puzzle, ctf]
tech:
  mcu: MSP430FR2422 + MSP430FR2972IPMR
  leds: 
    count: null
    type: RGB
    note: Multiple right-angle RGB LEDs around the board perimeter, plus six upward-facing RGB LEDs under the faceplate that show game progress; driven by an HT16D35B LED driver.
  display: two character LCDs
  connectivity: []
  battery: 2x AA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '450'
  availability: free
  distribution: [free_drop]
  where: Given to Queercon attendees at DEF CON 26, August 2018.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/duplico/qc15_badge
  eda_tool: Altium
links:
- label: hackaday.com/2018/08/21/all-the-badges-of-def-con-26-vol-2
  url: https://hackaday.com/2018/08/21/all-the-badges-of-def-con-26-vol-2/
  kind: article
- label: 'Teardown: Queercon 15 Badge (and The Game Hidden Within)'
  url: https://hackaday.com/2018/08/11/teardown-queercon-15-badge-and-the-game-hidden-within/
  kind: article
- label: duplico/qc15_badge (firmware repo)
  url: https://github.com/duplico/qc15_badge
  kind: repo
images:
  - file: assets/images/badges/queercon-2018/queercon-15-badge/dc1e1e0f6e.jpg
    source: "https://hackaday.com/2018/08/11/teardown-queercon-15-badge-and-the-game-hidden-within/"
    credit: "Hackaday"
    caption: "Exploded view of the Queercon 15 badge's three layers"
  - file: assets/images/badges/queercon-2018/queercon-15-badge/8fb34f1856.jpg
    source: "https://hackaday.com/2018/08/11/teardown-queercon-15-badge-and-the-game-hidden-within/"
    credit: "Hackaday"
    caption: "Collection of Queercon 15 faceplate variants"
contact: {}
notes:
- Queercon 15 badge (held alongside DEF CON 26) with a cake recipe hidden in micro-lettering; Queercon has no event id yet in events.yml. Found by the event-year sweep, task dc26-indie.
- Maker was recorded on the community sheet only as "MaraJade" (a Queercon team handle); Hackaday's teardown credits the design team as Evan Mackay, George Louthan, and Jonathan Nelson, so that team is used here instead.
status: released
sources:
- kind: url
  url: https://hackaday.com/2018/08/21/all-the-badges-of-def-con-26-vol-2/
  title: Queercon 15 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc26-indie); event read as ''queercon-2018''.'
- kind: url
  url: https://hackaday.com/2018/08/11/teardown-queercon-15-badge-and-the-game-hidden-within/
  title: 'Teardown: Queercon 15 Badge (and The Game Hidden Within)'
  accessed: '2026-09-08'
  note: 'Primary source for makers, MCU, LED driver, display, battery, game mechanic, and production quantity (450 units).'
- kind: url
  url: https://github.com/duplico/qc15_badge
  title: duplico/qc15_badge
  accessed: '2026-09-08'
  note: 'Confirms firmware is public on GitHub; repo page did not surface hardware-openness or EDA tool details directly (inferred Altium from a linked schematic PDF filename seen in search results, not directly fetched).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Firmware repository is public (duplico/qc15_badge), but no separate hardware/Gerber repository was found, so open_source is marked partial rather than yes. Exact LED count and price were not stated in the sources checked (the badge was a free con-distributed item, not sold). EDA tool (Altium) is inferred from a schematic file path glimpsed in a search snippet (blinkylightsninja.files.wordpress.com troubleshooting-guide PDF, filename referencing "QC15 Badge Altium") rather than confirmed by directly reading that document; treat as low-confidence. tech.connectivity left empty: the badge uses a HopeRF RFM75 2.4GHz proprietary radio for badge-to-badge communication, which does not fit any term in the controlled vocabulary (not wifi/ble/lora/zigbee/etc.); noted in prose instead.'
last_modified_date: '2026-09-08'
---

The Queercon 15 badge, distributed to attendees of Queercon's party-within-a-con at DEF CON 26 in August 2018, looks like an ordinary decorative con badge but is built around a hidden collaborative game. Each of the roughly 450 badges made carries a sixteenth of a larger story file — a nod to the "Expeditionary Force" novel series — and badges assemble the full text by wirelessly exchanging pieces with each other over the course of the convention. A scoreboard at the Queercon suite tracked the group's progress, and six RGB LEDs under the badge's faceplate lit up to show how far the collective puzzle had advanced.

Under the hood, the badge runs two MSP430 microcontrollers (an MSP430FR2422 and an MSP430FR2972IPMR): one drives buttons, the character-LCD displays, and the game logic, while the other manages a HopeRF RFM75 radio module for badge-to-badge communication. An HT16D35B chip drives the badge's ring of right-angle RGB LEDs. The badge runs on two AA batteries and was designed with a three-layer sandwich construction — a decorative PCB faceplate with no circuitry, a laser-cut acrylic diffuser, and the electronics layer underneath with matte-black solder mask. As an easter egg, a cake recipe (a reference to Portal) is hidden in micro-lettering on one of the copper layers.

The design team is credited by Hackaday's teardown as Evan Mackay, George Louthan, and Jonathan Nelson, working with a larger Queercon badge team; the community sheet that seeded this entry recorded only the handle "MaraJade." The badge's firmware is published on GitHub (duplico/qc15_badge), including a custom "Statemaker" tool that generated the game's state machines from Google Sheets exports; no separate hardware/Gerber repository was located, so the project is treated as only partially open source.
