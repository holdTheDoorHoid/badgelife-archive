---
title: DEF CON 24 Official Badge (robot skull, Intel Quark D2000)
id: dc24-official-badge-robot-skull-intel-quark-d2000
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc24
year: 2016
makers:
- name: 1o57 (Ryan Clarke)
summary: The official DEF CON 24 human attendee badge, a robot-skull-shaped PCB built around an Intel Quark D2000 x86 microcontroller, with an embedded multi-layer puzzle.
functions: Runs 1o57's annual DEF CON badge puzzle/ARG; buttons appear arranged as two directional pads for puzzle input, and the badge conceals encoded text in an inner copper layer plus a set of unexplained through-hole vias.
look:
  colors: []
  shape: skull
  themes:
  - skull
  - robot
  - puzzle
  - ctf
tech:
  mcu: Intel Quark D2000
  leds:
    count: 5
    type: null
    note: null
  display: none
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to DEF CON 24 attendees as their conference badge (human/attendee variant); goon and other role variants also existed.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2016/08/05/def-cons-x86-badge
  url: https://hackaday.com/2016/08/05/def-cons-x86-badge/
  kind: article
  archived: https://web.archive.org/web/20251008134802/https://hackaday.com/2016/08/05/def-cons-x86-badge/
- label: cktben/dc24_badge (unofficial firmware)
  url: https://github.com/cktben/dc24_badge
  kind: repo
images:
- file: assets/images/badges/dc24/official-badge-robot-skull-intel-quark-d2000/cebfb00205.jpg
  source: https://hackaday.com/2016/08/05/def-cons-x86-badge/
  credit: 1o57 / DEF CON
  caption: Front of the DEF CON 24 human attendee badge (robot skull shape)
  archived: https://web.archive.org/web/20251008134802/https://hackaday.com/2016/08/05/def-cons-x86-badge/
- file: assets/images/badges/dc24/official-badge-robot-skull-intel-quark-d2000/02669e9cdf.jpg
  source: https://hackaday.com/2016/08/05/def-cons-x86-badge/
  credit: 1o57 / DEF CON
  caption: Back of the DEF CON 24 human attendee badge
  archived: https://web.archive.org/web/20251008134802/https://hackaday.com/2016/08/05/def-cons-x86-badge/
contact: {}
notes:
- The official DC24 attendee badge, a robot-skull shaped electronic badge built around an Intel Quark D2000 (x86) MCU with 8 buttons, 5 LEDs, and embedded cryptographic puzzles. Found by the event-year sweep, task dc24-all.
- Sweep-imported title matched the maker's own framing (Hackaday calls it DEF CON's "x86 badge"); no change made to the title.
status: released
sources:
- kind: url
  url: https://hackaday.com/2016/08/05/def-cons-x86-badge/
  title: DEF CON 24 Official Badge (robot skull, Intel Quark D2000)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc24-all); event read as ''dc24''.'
  archived: https://web.archive.org/web/20251008134802/https://hackaday.com/2016/08/05/def-cons-x86-badge/
- kind: url
  url: https://hackaday.com/2016/08/05/def-cons-x86-badge/
  title: DEF CON's X86 Badge - Hackaday
  accessed: '2026-09-08'
  note: Core facts (Quark D2000, 32MHz/32kB flash/8kB RAM, 8 buttons, 5 LEDs, CR2032, embedded puzzle text in copper layer, unexplained vias); also source of the front/back photos.
  archived: https://web.archive.org/web/20251008134802/https://hackaday.com/2016/08/05/def-cons-x86-badge/
- kind: url
  url: https://github.com/cktben/dc24_badge
  title: cktben/dc24_badge - New firmware for the DEFCON 24 badge
  accessed: '2026-09-08'
  note: Third-party (unofficial) replacement firmware and pinout notes for the badge's Quark D2000; confirms the badge but is not the maker's own hardware/firmware release, so make_your_own is left unfilled.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via Hackaday's contemporaneous coverage (which is where the sweep's snippet came from). Could not find a maker-published (1o57/DEF CON) page with official specs, price/quantity, or open-source hardware/firmware files -- only third-party coverage and an unofficial community firmware repo (cktben/dc24_badge). LED type, colors, and any distribution beyond the free attendee giveaway are unconfirmed and left empty. No price applies since it was distributed for free with admission.
last_modified_date: '2026-09-08'
---

The DEF CON 24 (2016) official attendee badge is shaped like a robot skull and built around an Intel Quark D2000, a 32 MHz x86 microcontroller with 32 kB of flash and 8 kB of RAM -- an unusually minimal chip for a badge marketed as DEF CON's "x86 badge." It carries 8 buttons arranged as two directional pads, 5 LEDs, and runs off a CR2032 coin cell. As with other badges designed by 1o57 (Ryan Clarke), it functions as the physical anchor of that year's badge puzzle/ARG, with encoded text hidden in an inner copper layer and a cluster of through-hole vias on the board whose purpose was left for attendees to discover.

The badge was given out to attendees as part of conference admission (the "human" variant); goon and other role-specific badges shared the same general design. No maker-published hardware or firmware release has been located; a third-party repository (cktben/dc24_badge) offers unofficial replacement firmware and pinout documentation for hobbyists repairing or hacking their unit, which is not the same as an official open-source release.
