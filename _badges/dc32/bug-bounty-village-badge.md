---
title: Bug Bounty Village Badge
id: dc32-bug-bounty-village-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Abhinav SP / Hackerware.io
  url: https://www.hackster.io/HacksFromPanda
summary: The inaugural Bug Bounty Village badge, a full-colour UV-printed PCB shaped to the village's logo with backlit eyes and a Matrix-style LED "code rain" background, built around an onboard CTF.
functions: Backlit LED eyes/laptop-logo glow, Matrix-style dropdown LED background effect, and an onboard CTF where four buttons let wearers enter flags to unlock four reserved LEDs.
look:
  colors:
  - green
  - black
  - multicolor
  shape: logo
  themes:
  - security
  - ctf
  - village badge
  - hardware tool
tech:
  mcu: ATmega16A
  leds:
    count: 41
    type: reverse-mount SMD (1206)
    note: Reverse-mounted 1206 SMD LEDs shine through tiny drilled holes for the Matrix "code rain" background effect; four LEDs are reserved as CTF flag indicators.
  display: none
  connectivity: []
  inputs:
  - buttons
  battery: 2x CR2032 (planned; some sources say upgraded to 3x AAA)
  sao_version: none
get_one:
  price: Free
  price_usd: 0.0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  - village
  where: Given out at the Bug Bounty Village at DEF CON 32, on site only; the village's social accounts announced how to get one.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: hackaday
  label: Bug Bounty Village Badge (Hackster.io project page)
  url: https://www.hackster.io/HacksFromPanda/bug-bounty-village-badge-a29e98
- kind: website
  label: Bug Bounty Village
  url: https://www.bugbountydefcon.com/
  archived: https://web.archive.org/web/20260509232338/https://www.bugbountydefcon.com/
images:
- file: assets/images/badges/dc32/bug-bounty-village-badge/697c5f0bf0.jpg
  source: https://www.hackster.io/HacksFromPanda/bug-bounty-village-badge-a29e98
  credit: Abhinav SP / Hackerware.io
  caption: Assembled Bug Bounty Village badge PCB
- file: assets/images/badges/dc32/bug-bounty-village-badge/35f2664f07.jpg
  source: https://www.hackster.io/HacksFromPanda/bug-bounty-village-badge-a29e98
  credit: Abhinav SP / Hackerware.io
  caption: Bug Bounty Village badges with UV-printed artwork during assembly
contact:
  handles:
  - '@infinitelogins'
  - '@arl_rose'
  - '@BugBountyDEFCON'
notes:
- Follow @BugBountyDEFCON on twitter/x to learn how to get an exclusive Bug Bounty Village Badge during DEF CON. Only available for people on site at DEF CON 32.
status: released
sources:
- kind: sheet
  event: dc32
  row: 3
  updated: '2024-08-01'
- kind: url
  url: https://www.hackster.io/HacksFromPanda/bug-bounty-village-badge-a29e98
  title: Bug Bounty Village Badge - Hackster.io
  accessed: '2026-09-06'
  note: Maker's own project page (Abhinav SP / Hackerware.io); design story, BOM, photos, and the CR2032 power detail.
- kind: url
  url: https://forum.defcon.org/node/253153
  title: Limited Edition Bug Bounty Village Badge - Available for Pre-Order - DEF CON Forums
  accessed: '2026-09-06'
  note: Referenced while searching; describes a later-year (DC33) pre-order badge, used only to confirm the DC32 badge's ATmega16A/41-LED/4-button spec via cross-referenced coverage, not as the source of DC32-specific claims.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Maker's Hackster.io page (fetched via Wayback Machine copy after hackster.io blocked direct/automated fetches) confirms the design story, that it was made for Bug Bounty Village's inaugural DEF CON 32 village, the reverse-mount SMD LED matrix-rain effect, UV-printed artwork, and 2x CR2032 power plan, with a partial hardware BOM (custom PCB, 13x 1206 SMD LEDs listed in that BOM excerpt, capacitors, transistors, resistors, coin-cell holders). Search-engine summaries (not independently verified against a primary source) additionally describe an ATmega16A MCU, a total of 41 LEDs, four tactile push buttons for CTF/mode control, and mention the badge was later upgraded from CR2032 to 3x AAA power - these are included as likely-accurate but lower-confidence detail since the underlying press/forum pages could not be fetched directly. No price/quantity-made figures or open-source hardware/firmware files were found; it was a free giveaway to attendees, distribution said to be gated through
    the village's social media accounts. The original defcon.org forum thread (node/248952) could not be reached (connection reset).
last_modified_date: '2026-09-06'
---

Bug Bounty Village's co-founders, Harley and Ariel, asked hardware artist Abhinav SP of Hackerware.io to design a "cool blinky badge" for the village's first appearance at DEF CON 32 in 2024. Abhinav built the badge directly around the village's own logo: a double-sided PCB cut to the shape of the logo, with the eyes and laptop icon lit from backlit LEDs and the background turned into a Matrix-style "code rain" effect using reverse-mounted 1206 SMD LEDs shining up through tiny drilled holes. The color on the board comes from UV printing over the PCB rather than conventional silkscreen, and the badge was sponsored by XBOW.

The badge doubles as a small CTF: four tactile push buttons control the LED modes and let a wearer type in flags, with four LEDs at the bottom staying dark until the correct flag is entered. It was originally designed to run off two CR2032 coin cells. It was given away for free to attendees at the Bug Bounty Village on site at DEF CON 32, with the village's social accounts (@BugBountyDEFCON, plus organizers @infinitelogins and @arl_rose) used to announce how to claim one; no price or total production quantity was published.
