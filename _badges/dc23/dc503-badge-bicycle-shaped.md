---
title: DC503 Badge (bicycle-shaped)
id: dc23-dc503-badge-bicycle-shaped
layout: badge
parent: DC23
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc23
year: 2015
makers:
- name: Joe Fitz / DC503
summary: A bicycle-shaped, ATtiny85-driven LED badge made by DC503 (a Portland hacker group) as the entry ticket to their DEF CON 23 party.
functions: 'Ambient LED animation only: capacitive touch on the "gears" speeds up the rotation effect (as if pedaling), while touching the "handlebars" slows it down.'
look:
  colors: []
  shape: bicycle
  themes:
  - vehicle
tech:
  mcu: ATtiny85
  leds:
    count: 14
    type: discrete
    note: Mounted on the back of the board, shining through the substrate to the front; driven via two PWM channels (4 LEDs VCC-to-PWM1, 4 more PWM1-to-GND, driven out of phase, same trick repeated on the second PWM pin).
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 100 boards spun; 50 populated for crowdfunding backers, 10 more assembled on-site for organizers
  availability: sold_out
  distribution:
  - crowdfunding
  where: Distributed to DC503's crowdfunding backers, plus a small on-site batch for organizers; served as the entry badge for the DC503 DEF CON 23 party.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  kind: website
  archived: https://web.archive.org/web/20260613124820/https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
images:
- file: assets/images/badges/dc23/dc503-badge-bicycle-shaped/2f9e91e0bc.jpg
  source: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  credit: Hackaday
  caption: The DC503 bicycle-shaped badge
  archived: https://web.archive.org/web/20260613124820/https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
- file: assets/images/badges/dc23/dc503-badge-bicycle-shaped/0383d6fa82.jpg
  source: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  credit: Hackaday
  caption: DC503 badge detail, close-up of LED and button layout
  archived: https://web.archive.org/web/20260613124820/https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
contact: {}
notes:
- Sweep's title matches the maker/press wording; no change needed.
status: released
sources:
- kind: url
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  title: DC503 Badge (bicycle-shaped)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
  archived: https://web.archive.org/web/20260613124820/https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
- kind: url
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  title: All The Unofficial Electronic Badges Of DEF CON
  accessed: '2026-09-10'
  note: Confirmed maker, shape, LED/MCU details, button behavior, production quantity (100 spun, 50+10), and distribution via crowdfunding for the DC503 DEF CON 23 party.
  archived: https://web.archive.org/web/20260613124820/https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Only source found is the Hackaday roundup article; no maker storefront, repo, or standalone project page was located. No price is stated anywhere. Colors/PCB finish not described in the source, so left empty. DC503 is a Portland-area group tied to the CTRL-H Hackerspace; this 2015/DEF CON 23 bicycle badge is distinct from the later dc25-dc503-badge (DC503 Wagon Party Badge) and dc27-dc503-dc503-badge-dc27 (5ohBEE) entries.
last_modified_date: '2026-09-10'
---

The DC503 badge was a bicycle-shaped party badge made by DC503, a group of Portland-area hackers connected to the CTRL-H Hackerspace, for DEF CON 23 in 2015. It served as the entry ticket to the group's annual DEF CON party and was distributed to the crowdfunding backers who helped fund it.

The board carries 14 LEDs mounted on the back of the PCB that shine through the substrate to light up the front, driven by an ATtiny85 across two PWM channels using an out-of-phase driving trick to get more apparent brightness from fewer I/O pins. Two capacitive touch pads carry the bicycle theme through to the interaction: touching the pad on the "gears" speeds up the LED animation as if pedaling, while touching the "handlebars" (where the brakes would be) slows it back down.

Production was small: 100 boards were fabricated, with 50 populated and handed out to backers and another 10 assembled on-site for the organizing crew. No open-source files, storefront, or price were found; the only source located for this entry is a 2015 Hackaday roundup of unofficial DEF CON badges.
