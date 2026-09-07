---
title: Prophet AI Badge
id: dc34-prophet-ai-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Abhinav Panda / Hackerware.io
  url: https://www.hackerware.io/
summary: A hand-built puzzle badge made for Prophet Security, styled as a "temporal energy cell" with three cipher-locked LED sets unlocked through a CTF.
functions: Three separate locked puzzles; solvers decode ciphers printed on the lanyard, convert the answers to 7-bit binary keys, and enter them on the badge's buttons to light each LED set in turn.
look:
  colors: [red, yellow]
  shape: null
  themes: [sci-fi, ctf, puzzle, security]
tech:
  mcu: Nuvoton
  leds:
    count: null
    type: discrete
    note: Three red-and-yellow LED sets, each unlocked by solving one puzzle stage.
  display: none
  connectivity: []
  battery: 2x coin cell
  sao_version: none
get_one:
  price: Free Giveaways
  price_usd: 0.0
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: Given away at Hackerware/Prophet Security's booth during DEF CON 34 week in Las Vegas.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackerware.io/prophet-ai
  url: https://hackerware.io/prophet-ai
  kind: store
- label: x.com/TweetsFromPanda/status/2085867981016375706
  url: https://x.com/TweetsFromPanda/status/2085867981016375706
  kind: video
- label: Hackerware.io
  url: https://www.hackerware.io/
  kind: website
  archived: false
- label: 'Facebook: Prophet AI Badge announcement'
  url: https://www.facebook.com/Hackerware/posts/prophet-ai-badge-is-a-hand-built-temporal-energy-cellsolve-ctf-challenges-and-un/1461017809384107/
  kind: social
  archived: false
images:
- file: assets/images/badges/dc34/prophet-ai-badge/195725f59e.jpg
  source: "https://www.facebook.com/Hackerware/posts/prophet-ai-badge-is-a-hand-built-temporal-energy-cellsolve-ctf-challenges-and-un/1461017809384107/"
  credit: "Hackerware.io"
  caption: "Prophet AI Badge, a hand-built temporal energy cell badge"
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
  row: 63
  updated: 8/7/2026 18:19:26
  listing: New
- kind: url
  url: https://hackerware.io/prophet-ai
  title: Prophet AI Badge - Hackerware.io
  accessed: '2026-09-06'
  note: Describes the badge as a hand-built temporal energy cell/puzzle device; lists Nuvoton MCU, 2x coin cell, buzzer, 3D-printed enclosure, three red/yellow LED sets unlocked via CTF puzzles using ciphers on the lanyard converted to 7-bit binary keys.
- kind: url
  url: https://www.hackerware.io/
  title: Hackerware - #BadgeLife | Hardware Design, Security, & Research.
  accessed: '2026-09-06'
  note: Confirms Abhinav Panda/Hackerware.io as maker and lists Prophet AI Badge among their portfolio of conference badges.
- kind: url
  url: https://www.facebook.com/Hackerware/posts/prophet-ai-badge-is-a-hand-built-temporal-energy-cellsolve-ctf-challenges-and-un/1461017809384107/
  title: 'Hackerware Facebook: Prophet AI Badge announcement'
  accessed: '2026-09-06'
  note: Announcement post (dated August 7, 2026, matching the sheet import date) with three photos of the badge; source of the saved image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Maker's own page (hackerware.io/prophet-ai) and Hackerware's portfolio page confirm the badge, its maker, and its puzzle/CTF mechanic. Web search summaries associate this badge with Prophet Security's presence at Black Hat USA 2026 (the same Las Vegas hacker-con week as DEF CON 34) rather than with DEF CON's own badge program; the community sheet logs it under dc34, and no source directly contradicts that, so the event field is left as imported. Price/quantity/open-source status are not stated anywhere found; LED count and exact chip model (beyond "Nuvoton") were not specified by the maker.
last_modified_date: '2026-09-06'
---

The Prophet AI Badge is a hand-built puzzle badge that Hackerware.io (Abhinav Panda) made for the AI security company Prophet Security, distributed as a free giveaway during DEF CON 34 week in Las Vegas in August 2026. Styled as a "temporal energy cell," the badge runs on a Nuvoton microcontroller and two coin-cell batteries, with a buzzer for audio feedback, housed in a cream 3D-printed enclosure that opens for tinkering.

Its hook is a layered CTF: three separate puzzles, each solved by decoding a cipher printed on the badge's lanyard, converting the answer into a 7-bit binary key, and entering it via buttons on the badge. Each solved puzzle lights up one of three red-and-yellow LED sets on the board, playing on the "temporal" theme of a device that "behaves like it's already seen tomorrow."

No pricing (it was a free giveaway), production quantity, or open-source hardware/firmware release could be confirmed from the maker's site or social posts.
