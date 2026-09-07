---
title: TRON Badge
id: dc30-tron-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Ironwood Cyber
  url: https://github.com/Ironwood-Cyber
summary: A round, TRON-themed badge (the maker called it the "Tron Disc") given away free by cybersecurity company Ironwood Cyber at DEF CON 30, built around two concentric rings of addressable LEDs.
functions: 'Lights 70 addressable RGB LEDs arranged in two concentric rings; the front board is a capacitive-touch interface for the rear board''s electronics. A companion web app (in development as of the giveaway) was meant to let owners build custom light sequences from stacked animation layers to send to the badge.'
look:
  colors:
  - black
  - teal
  shape: circle
  themes:
  - sci-fi
  - movie
tech:
  mcu: ESP-series (exact part not stated)
  leds:
    count: 70
    type: RGB
    note: Two concentric rings (inner and outer), diffused through 3D-printed material between the two boards.
  display: null
  connectivity: []
  battery: LiPo, rechargeable
  sao_version: null
get_one:
  price: Free
  price_usd: 0.0
  quantity: '80 (per the maker, given away over several weeks)'
  availability: free
  distribution:
  - raffle
  - free_drop
  where: 'Twitter and LinkedIn raffles plus unannounced in-person drops during DEF CON 30 (one at the Flamingo); pickup only, not shipped.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  firmware_url: null
  eda_tool: KiCad
links:
- label: www.reddit.com/r/Defcon/comments/w5hozv/comment/ih8090z
  url: https://www.reddit.com/r/Defcon/comments/w5hozv/comment/ih8090z
  kind: social
- label: Ironwood Cyber (@IronwoodCyber) on Twitter, badge reveal
  url: https://twitter.com/IronwoodCyber/status/1550170683308638208
  kind: social
- label: Schematics repo (Ironwood-Cyber/dc30-badge-hw)
  url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  kind: repo
images:
- file: assets/images/badges/dc30/tron-badge/e802582f60.jpg
  source: "https://twitter.com/IronwoodCyber/status/1550170683308638208"
  credit: "Ironwood Cyber"
  caption: "Tron Disc badge lit up, revealed on Twitter, July 2022"
- file: assets/images/badges/dc30/tron-badge/369baeafcb.jpg
  source: "https://twitter.com/IronwoodCyber/status/1550606356150976512"
  credit: "Ironwood Cyber"
  caption: "Assembling Tron Disc boards: LED ring, black PCB, and center RF module, July 2022"
contact: {}
notes:
- Twitter raffle/drops. Info on twitter (@IronwoodCyber). Check link for greater details
- 'Maker''s own name for it is the "Tron Disc" badge/"Tron disc badge"; kept the sheet''s title "TRON Badge" per the archive''s naming rule since that is close enough and is the sheet''s wording.'
status: released
sources:
- kind: sheet
  event: dc30
  row: 38
  updated: '2022-07-22'
- kind: url
  url: https://www.reddit.com/r/Defcon/comments/w5hozv/comment/ih8090z
  title: 'r/Defcon: "Update on tron disc badge. info in comments" (archived)'
  accessed: '2026-09-06'
  note: 'Reddit blocks live fetches; read via Wayback Machine snapshot (2022-07-24). Maker (u/OP, presumably Ironwood Cyber) says 80 badges total given away over several weeks via Twitter raffles, a LinkedIn raffle, and ~2 in-person site drops during DEF CON, pickup only (no shipping); mentions an exposed-FR4 prototype and a HASL/silver prototype before settling on copper for the final run, and a companion web app (by u/cwsharkbones) for building custom LED light sequences.'
- kind: url
  url: https://twitter.com/IronwoodCyber
  title: Ironwood Cyber (@IronwoodCyber) on Twitter/X
  accessed: '2026-09-06'
  note: 'Read via Wayback Machine snapshots (July-August 2022, live fetch blocked). Confirms Ironwood Cyber is a Fort Worth, TX cybersecurity company (Enlight/Firethorn products) running the badge giveaway as marketing outreach; tweets show "Our #DEFCON badge is live", a "10 Tron Disc #DEFCON badges" raffle, and a "Free badges for the first 20 people" in-person drop near the Flamingo during DEF CON 30, confirming DC30/2022 and free/raffle distribution.'
- kind: url
  url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  title: 'Ironwood-Cyber/dc30-badge-hw: Tron badge hardware schematics'
  accessed: '2026-09-06'
  note: 'Confirmed reachable (HTTP 200). README describes the badge: two PCBs joined by 3D-printed diffusion material, a touch-input front board, 70 addressable LEDs in two rings, rechargeable LiPo circuit, and USB reprogramming via esp-idf/UART.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'This entry duplicates dc30-ironwood-cyber-tron-badge (same maker, same event, same hardware repo) - see that entry for maker/dev-team credits (kimboslice, notthatguy, joehacksalot, Shiloh, LeetPanda, Spaghetti Code) pulled from the badge.life archive, which this entry does not repeat. No exact MCU part number, price beyond "free", firmware repo, or Gerbers/BOM were found. Live fetches of reddit.com and twitter.com/x.com are blocked in this environment; all social-media facts above came from Wayback Machine snapshots instead, so distribution details reflect August 2022 archived pages rather than the current (possibly deleted) accounts.'
last_modified_date: '2026-09-06'
---

Ironwood Cyber, a small Fort Worth, Texas cybersecurity startup, brought a round TRON-themed badge to DEF CON 30 (2022) as a free giveaway and outreach project. The maker calls it the "Tron Disc": two stacked PCBs, a rear board carrying an ESP-series microcontroller, a rechargeable LiPo battery, and 70 addressable RGB LEDs arranged in two concentric rings, paired with a front board that adds a capacitive-touch interface, with 3D-printed material between the boards diffusing the light into the glowing ring look seen in the team's reveal photos and videos.

About 80 badges were made and given away for free over several weeks, split across one or two Twitter raffles, a LinkedIn raffle, and a handful of unannounced in-person drops during the con itself (including one near the Flamingo) - pickup only, with no shipping option. A teammate was also building a companion web app so owners could design their own layered LED animation sequences to push to the badge, though it had not shipped by the time of the giveaway. Hardware schematics (KiCad) are published on GitHub, though no firmware source, bill of materials, or price/production-cost figures were ever made public.

## Make your own

Hardware schematics (KiCad) are available in the [dc30-badge-hw repository](https://github.com/Ironwood-Cyber/dc30-badge-hw), which documents the two-board LED-ring design and its LiPo/USB circuitry. No firmware source or Gerber files have been published alongside it.
