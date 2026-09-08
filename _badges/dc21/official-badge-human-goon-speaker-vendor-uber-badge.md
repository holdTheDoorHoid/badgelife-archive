---
title: DEF CON 21 Official Badge (Human/Goon/Speaker/Vendor + Uber Badge)
id: dc21-official-badge-human-goon-speaker-vendor-uber-badge
layout: badge
parent: DC21
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc21
year: 2013
makers:
- name: Ryan Clarke (LostboY / 1o57)
summary: 'A "non-electronic-electronic" DEF CON 21 badge: a playing-card design fabricated as a bare PCB, using copper, solder mask, and silkscreen as its three colors, built around a multi-stage crypto puzzle.'
functions: 'Playing-card crypto puzzle: attendees decode ciphertext and symbols silkscreened/etched onto the card to progress through challenge stages; different attendee classes (human, goon, speaker, vendor, press) got different card suits/colors, and the puzzle encouraged talking to other badge-holders to solve it.'
look:
  colors:
  - copper
  - black
  - white
  shape: card
  themes:
  - crypto
  - puzzle
  - security
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Given to attendees at DEF CON 21 (2013) as their conference badge; not sold separately.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: defcon.org/html/links/dc-badge.html
  url: https://defcon.org/html/links/dc-badge.html
  kind: website
- label: 'Hackaday at DEF CON 21'
  url: https://hackaday.com/2013/08/01/hackaday-at-def-con-21/
  kind: article
images:
  - file: assets/images/badges/dc21/official-badge-human-goon-speaker-vendor-uber-badge/c2e9b801f4.jpg
    source: "https://hackaday.com/2013/08/01/hackaday-at-def-con-21/"
    credit: "Hackaday"
    caption: "DEF CON 21 badge, a Jack playing card design printed on PCB (Hackaday, 2013)"
contact: {}
notes:
- PCB playing-card themed 'non-electronic-electronic' badge with a crypto puzzle (Human=white, Goon=red queen, Speaker=blue king, Vendor=green jack); the Uber/black badge variant incorporated an actual mechanical watch movement as a tribute to the designer's grandfather. Found by the event-year sweep, task dc21-all.
- 'This entry duplicates dc21-badge (same badge, same maker, same year) — see research.notes.'
status: listed
sources:
- kind: url
  url: https://defcon.org/html/links/dc-badge.html
  title: DEF CON 21 Official Badge (Human/Goon/Speaker/Vendor + Uber Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc21-all); event read as ''dc21''.'
- kind: url
  url: https://defcon.org/html/links/dc-badge.html
  title: DEF CON 21 Badge Information
  accessed: '2026-09-08'
  note: 'Confirmed non-electronic PCB playing-card design, crypto puzzle theme, and the Uber badge''s mechanical watch movement tribute to the designer''s grandfather.'
- kind: url
  url: https://hackaday.com/2013/08/01/hackaday-at-def-con-21/
  title: Hackaday at DEF CON 21
  accessed: '2026-09-08'
  note: 'Confirmed the badge is a Jack playing-card design printed on PCB using silkscreen, solder mask, and copper layers for three colors, and is a crypto challenge; source of the badge photo.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'This entry is a duplicate of dc21-badge (id dc21-badge, same maker Ryan Clarke/LostboY, same year, same badge.gallery-sourced description). No pricing or quantity figures were found in either DEF CON''s own page or Hackaday''s coverage; DEF CON badges of this era were included with conference admission rather than sold, so get_one.where reflects that. Per-role colors (human/goon/speaker/vendor/press) noted in the original sweep were not independently re-confirmed by the sources fetched here, so look.colors is left conservative (copper/black/white from the PCB itself) rather than listing every claimed role color.'
last_modified_date: '2026-09-08'
---

The DEF CON 21 (2013) badge, designed by Ryan "LostboY" Clarke (also known as 1o57), broke from the electronic badges of recent years and went "non-electronic-electronic": a playing-card design fabricated entirely as a bare printed circuit board, using the copper, solder-mask, and silkscreen layers as its three colors instead of any active electronics. The card art doubled as a multi-stage cryptography puzzle, and different attendee categories (human, goon, speaker, vendor, press) received different card suits and colors, encouraging people to trade information and talk to each other to solve it.

The premium Uber badge variant took the theme further by embedding an actual mechanical watch movement in the card, a tribute Clarke made to his grandfather, a watchmaker, framing the badge's craftsmanship as an extension of that lineage.

No price or production-quantity figures turned up in DEF CON's own badge page or in contemporary Hackaday coverage; badges of this kind were distributed to attendees as part of admission rather than sold as a separate product. This entry describes the same badge as the archive's existing `dc21-badge` entry (same designer, same year, same non-electronic-electronic playing-card concept), and the two should likely be merged.
