---
title: The PirateBox Badge
id: dc31-the-piratebox-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Bogon
  url: https://defcon.social/@Bogon
summary: A purple PCB badge shaped like a fox/canine head, built around a Hi-Link HLK-7688A Wi-Fi module so it can run its own PirateBox-style offline file-sharing network. Announced for DEF CON 31 but pulled at the last minute when the maker (Bogon, DEF CON's Embedded Systems Village staff) hit RF problems and ran out of time to make it right.
functions: 'Runs as a PirateBox: a self-hosted, offline Wi-Fi access point/file-share people connect to directly, independent of any network infrastructure. Board has a toggle switch silkscreened "Piracy" and status LEDs for power and battery.'
look:
  colors:
  - purple
  - gold
  - white
  shape: fox head
  themes:
  - pirate
  - radio
  - animal
tech:
  mcu: Hi-Link HLK-7688A (Wi-Fi/MIPS module)
  leds:
    count: 5
    type: discrete
    note: One green LED forms the fox's eye; four more (silkscreened D1-D4, next to "Power" and "BaL Stat" labels) sit by the front buttons.
  display: none
  connectivity:
  - wifi
  battery: LiPo (JST connector and a "BaL Stat" charge-status LED are present on the board; capacity not stated anywhere found)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  availability_note: 'Checked 2026-09-06: maker announced on 2023-08-01, the day before DEF CON 31, that the badge would not ship that year.'
  distribution: []
  where: RF Gremlins and other stuff prevented Bogon from getting these out in time. Story found in the supplied link. This is tough decision to make but when you have a high quality product, you do not want it out nonfunctional.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: t.co/nnC1QLgXft
  url: https://t.co/nnC1QLgXft
  kind: website
- label: 'Bogon on DEF CON Social: "Not-so-great PirateBox Badge announcement"'
  url: https://defcon.social/@Bogon/110816746775909971
  kind: social
images:
- file: assets/images/badges/dc31/the-piratebox-badge/4bb7711799.jpg
  source: https://defcon.social/@Bogon/110816746775909971
  credit: Bogon
  caption: The purple fox-head PirateBox Badge PCB, showing its Hi-Link HLK-7688A Wi-Fi module, green eye LED, and "Piracy" toggle switch, photographed the day the release was delayed.
contact: {}
notes:
- The Pirate Box badge is not affiliated with the ESV but the drops will occur near there.
- 'The community sheet credited "Embedded Systems Village" as the maker; the maker''s own DEF CON Social account ("Bogon") describes it as a personal project by ESV staff, not an official ESV badge, matching the note above.'
status: announced
sources:
- kind: sheet
  event: dc31
  row: 40
  updated: '2023-08-01'
- kind: url
  url: https://defcon.social/@Bogon/110816746775909971
  title: 'Bogon: "Not-so-great PirateBox Badge announcement"'
  accessed: '2026-09-06'
  note: Maker's own post explaining the badge was delayed past DEF CON 31 due to "RF gremlins and competing responsibilities"; source of the badge photo.
- kind: url
  url: https://defcon.social/@Bogon
  title: Bogon (@Bogon@defcon.social) profile
  accessed: '2026-09-06'
  note: Confirms Bogon is DEF CON Embedded Systems Village staff and former IoT Village tech lead.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: 'Only the maker''s own Mastodon post and photo could be found; no store listing, repo, Hackaday.io project, price, quantity, or firmware/hardware source was located despite searching. The badge''s hardware (Hi-Link HLK-7688A Wi-Fi module, LEDs, "Piracy" switch, battery connector) was read directly off the announcement photo rather than a spec sheet, so treat those as observed, not maker-confirmed, details. Unknown whether the badge was ever released in a later year.'
last_modified_date: '2026-09-06'
---

The PirateBox Badge was a purple, fox-head-shaped PCB badge planned for DEF CON 31 (2023) by a maker who goes by "Bogon," a staffer with DEF CON's Embedded Systems Village. Built around a Hi-Link HLK-7688A Wi-Fi module, it was designed to run as a self-contained PirateBox: an offline wireless access point that lets people connect directly to the badge to share files, independent of any surrounding network. The board carries a glowing green eye LED, four more status LEDs near its front buttons (marked "Power" and "BaL Stat" for battery status), and a toggle switch silkscreened "Piracy."

The day before DEF CON 31 opened, Bogon posted on DEF CON Social that the badges would not make it out that year. "RF gremlins and competing responsibilities" had gotten in the way, and rather than hand out a badge that didn't work right, the release was pushed back, with a promise of more details and possible preorders after the con. The community badge sheet's note that "the Pirate Box badge is not affiliated with the ESV but the drops will occur near there" lines up with Bogon's own bio: this was a personal project by an ESV staffer, not an official Embedded Systems Village badge.

No further public announcement, store listing, or source-file release could be found, so it is unclear whether the badge ultimately shipped in a later year.
