---
title: AI Village Badge
id: dc32-ai-village-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: AI Village, Abhinav Panda / Hackerware.io
  url: https://www.hackerware.io/
summary: A blinky PCB badge shaped like two robot dogs, made for the AI Village at DEF CON 32.
functions: A full-colour blinky badge. The dog-tag pendant blinks RGB, the eyes do a slow RGB colour transition, and the horns alternate their glow as if sending a signal.
look:
  colors:
  - gold
  - multicolor
  shape: robot dog
  themes:
  - robot
  - animal
  - dog
  - ai
tech:
  mcu: null
  leds:
    count: 9
    type: RGB
    note: 4x 1206 SMD LEDs plus 5x 1204 side-emitting RGB LEDs, per the maker's parts list.
  display: none
  connectivity: []
  battery: 2x CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Given out at the AI Village at DEF CON 32; the maker's write-up describes distinct standard, Generative Red Team (GRT), and village staff/speaker versions, but does not say how attendees obtained one.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: hackaday
  label: 'The AI Village Badge (Hackster.io project log)'
  url: https://www.hackster.io/HacksFromPanda/the-ai-village-badge-98ed97
- kind: website
  label: Hackerware.io
  url: https://www.hackerware.io/
images:
- file: assets/images/badges/dc32/ai-village-badge/c56e3b4d82.jpg
  source: "https://www.hackster.io/HacksFromPanda/the-ai-village-badge-98ed97"
  credit: "Abhinav SP / Hackerware.io"
  caption: "The AI Village Badge, showing the robot dog artwork with RGB dog tag and UV-printed HAL surface"
contact: {}
notes:
- Watch out for AIV announcements for badge drops!
- 'Sheet listed maker as "AI Village, Abhinav Panda / Hackerware.io"; the project itself credits designer Abhinav SP (Hackerware.io) with artwork by Kassandra Jodar, and a GRT colour variant by Lauren.'
status: released
sources:
- kind: sheet
  event: dc32
  row: 12
  updated: '2024-07-28'
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-ai-village-badge-98ed97
  title: The AI Village Badge
  accessed: '2026-09-06'
  note: Primary source for the badge's design, artwork, LED behavior, HAL/UV-print/varnish process, CR2032 power, and hardware component list (LED counts).
- kind: url
  url: https://www.hackerware.io/
  title: 'Hackerware - #BadgeLife'
  accessed: '2026-09-06'
  note: Confirms Abhinav Panda (Abhinav SP) is the founder of Hackerware.io; did not add further badge-specific details.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    Maker's own Hackster.io project log confirms the design (two robot dogs, artwork by
    Kassandra Jodar), the blinky RGB circuit, the HAL-surface + UV print + varnish
    fabrication process, 2x CR2032 power, and a hardware parts list (4x 1206 SMD LEDs,
    5x 1204 side-emitting RGB LEDs, no MCU listed, suggesting a discrete/passive blink
    driver rather than a microcontroller — left tech.mcu empty since no chip is named).
    Could not find price, quantity made, exact distribution method (drop, contest reward,
    or staff-only), or any hardware/firmware/gerber files — the project page has no
    repo or store links. No separate Hackaday.io or GitHub project found under this name.
last_modified_date: '2026-09-06'
---

The AI Village Badge is a full-colour blinky PCB badge made for the AI Village at DEF CON 32 (2024), designed by Abhinav Panda (Abhinav SP) of Hackerware.io. It takes the shape of two robot dogs — Vers and Cya — using artwork created by Kassandra Jodar for the village's 2024 edition, itself inspired by real dogs. The RGB dog-tag pendant blinks, the eyes cycle through a slow colour transition, and the horns alternate their glow as if signaling.

Fabrication-wise, part of the dog's body is finished in reflective HAL (hot air leveling) rather than a matte UV print, after tests comparing HAL and bare-copper finishes; copper oxidized within days, so the team settled on HAL plus a thin transparent varnish coat applied right after UV printing to protect and level the surface without dulling the artwork's colours. The badge runs on two CR2032 coin cells and, per its published parts list, uses nine RGB-capable LEDs (four 1206 SMD LEDs and five 1204 side-emitting RGB LEDs) with no microcontroller listed, pointing to a simple discrete blink circuit rather than a programmable one.

Several variants were made: a standard attendee version, an alternate colour scheme for the Generative Red Team (GRT) challenge designed by Lauren, and distinct versions for village staff and speakers. The maker's write-up does not say how many were made or exactly how they were distributed to attendees, and no store, repository, or gerber files are linked from the project page.
