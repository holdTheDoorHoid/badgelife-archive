---
title: DEF CON 30 Badge (2022)
id: dc30-badge-2022
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: MK Factor (with The Dark Tangent)
  url: https://mkfactor.com/
summary: The official DEF CON 30 "human" badge, a musical electronic badge with a capacitive-touch keyboard, built-in speaker and microphone, that plays and records audio and doubles as a USB MIDI device.
functions: Plays built-in sounds via a capacitive touch keyboard; records audio samples from an onboard microphone or line-in jack; acts as a class-compliant USB MIDI device, sending MIDI events when keys are pressed; includes a self-test mode and a USB (UF2) firmware-reflashing bootloader; part of the DEF CON 30 badge challenge/puzzle.
look:
  colors:
  - white
  - black
  shape: null
  themes:
  - music
  - puzzle
  - ctf
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity:
  - usb
  inputs:
  - touch
  - capacitive
  battery: null
  sao_version: null
get_one:
  price: "$75"
  price_usd: 75
  quantity: ''
  availability: sold_out
  availability_note: 'Checked 2026-09-07: shop.defcon.org listing for the DEF CON 30 human badge with lanyard (product page since removed from the live store; price and images recovered via Wayback Machine snapshot from 2024-12-16).'
  distribution:
  - purchase
  where: Included with DEF CON 30 in-person "Human" attendee registration (white soldermask / black silkscreen design); also sold separately with lanyard through the DEF CON shop.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: defcon.org/html/defcon-30/dc-30-index.html
  url: https://defcon.org/html/defcon-30/dc-30-index.html
  kind: website
- label: DEF CON 30 Badge Instructions
  url: https://defcon.org/badge/30/
  kind: doc
- label: 'Tindie Blog: Badge Me if You Can – DEF CON 30'
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  kind: article
- label: 'DEFCON 30 - Making of the DEF CON Badge (Security Boulevard)'
  url: https://securityboulevard.com/2022/09/defcon-30-the-dark-tangents-and-mk-factors-welcome-to-def-con-and-the-making-of-the-def-con-badge/
  kind: article
- label: MK Factor
  url: https://mkfactor.com/
  kind: website
images:
- file: assets/images/badges/dc30/badge-2022/70c74c044d.jpg
  source: "https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/"
  credit: "Tindie Blog"
  caption: "The DEF CON 30 official human badge, showing its capacitive touch keys and curved PCB face."
contact: {}
notes:
- Confirmed this session via defcon.org DC30 index page text naming MK Factor and The Dark Tangent as 'the badge creators.'
- 'MK Factor also designed the DEF CON 29 badge; see "Designing the DEF CON 29 & 30 Badges (feat. MK Factor)" on YouTube.'
- Distinct attendee-type badge variants existed (Human, Contest, Goon, Artist, Press, Vendor, Speaker, Call for Papers); this entry covers the standard "Human" attendee badge (white soldermask/black silkscreen).
status: released
sources:
- kind: url
  url: https://defcon.org/html/defcon-30/dc-30-index.html
  title: DEF CON 30 Badge (2022)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''DEF CON 30''.'
- kind: url
  url: https://defcon.org/badge/30/
  title: DEF CON 30 Badge Instructions
  accessed: '2026-09-07'
  note: Official instructions page; describes buttons/keys, onboard mic, line-in jack, USB MIDI behavior, self-test mode, and UF2 bootloader re-flashing.
- kind: url
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  title: 'Tindie Blog: Badge Me if You Can – DEF CON 30'
  accessed: '2026-09-07'
  note: Names MK Factor (@theMKFactor) as designer, confirms RP2040 MCU, capacitive touch keyboard, speaker/mic, curved PCB face holding a pressure-connected speaker; source of the saved photo.
- kind: url
  url: https://securityboulevard.com/2022/09/defcon-30-the-dark-tangents-and-mk-factors-welcome-to-def-con-and-the-making-of-the-def-con-badge/
  title: "DEFCON 30 - The Dark Tangent's And MK Factor's 'Welcome To DEF CON And The Making Of The DEF CON Badge'"
  accessed: '2026-09-07'
  note: Confirms the badge design talk given by The Dark Tangent and MK Factor; badge was themed around DEF CON 30's "Hacker Homecoming" theme.
- kind: url
  url: https://web.archive.org/web/20241216141438/https://shop.defcon.org/products/def-con-30-human-badge-with-lanyard
  title: DEF CON 30 Human badge with lanyard - DEF CON Shop (Wayback Machine snapshot)
  accessed: '2026-09-07'
  note: Live shop.defcon.org listing now 404s; Wayback snapshot gives price ($75) and confirms "Human" badge variant name and lanyard bundling.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'LED count/type, exact display info (a small status screen is mentioned in the instructions but its size/type is not specified), battery/power source, quantity made, and open-source hardware/firmware links were not found in the sources checked. The badge challenge/puzzle had a separate writeup repo (github.com/Kybr-git/DC30-Badge-Challenge-Writeup) not reviewed in depth here. Other attendee-type badge variants (Contest, Goon, Artist, Press, Vendor, Speaker, Call for Papers) exist but were not separately researched.'
last_modified_date: '2026-09-07'
---

The DEF CON 30 "Human" badge is the official electronic badge given to general attendees of DEF CON 30 (Las Vegas, August 2022), designed by MK Factor working with DEF CON founder The Dark Tangent. Built around an RP2040 microcontroller, it replaces a typical button-and-LED badge interface with a capacitive-touch keyboard set into a curved PCB "face" that also holds a pressure-connected speaker in place — letting wearers play built-in sounds, record their own samples through an onboard microphone or line-in jack, and use the badge as a class-compliant USB MIDI controller when plugged into a computer. A self-test mode and a USB UF2 bootloader for re-flashing firmware were both built in, and the badge doubled as part of that year's on-badge puzzle/challenge.

DEF CON badges are typically split by attendee role — Human, Contest, Goon, Artist, Press, Vendor, Speaker, and Call for Papers all had their own badge variants for DC30 — and this entry covers the standard white-soldermask, black-silkscreen "Human" badge that most attendees received with registration; DEF CON's shop also sold it separately with a lanyard for $75. MK Factor had designed the previous year's DEF CON 29 badge as well, and the making of the DC30 badge was the subject of the con's opening talk with The Dark Tangent.

Design files, LED/display specifics, and total production quantity were not found in the sources reviewed and are left blank pending further research.
