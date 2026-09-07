---
title: NerdFlare Solder Challenge 26
id: other-nerdflare-solder-challenge-26
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 2026
makers:
- name: NerdFlare
  url: https://nerdflare.github.io
summary: A soldering-skill practice board made by Cal Poly's NerdFlare club, with five LEDs in decreasing package sizes wired to an ATtiny85 microcontroller.
functions: Chases through five LEDs one at a time (through-hole, 1206, 0805, 0603, and 0402 packages), letting a builder confirm each size was soldered correctly as it lights up in turn.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: ATtiny85V
  leds:
    count: 5
    type: discrete
    note: One each of THT, 1206, 0805, 0603, and 0402 package LEDs, lit in sequence to test solder joints at each size.
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
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/NerdFlare/NF-SolderChallenge26/tree/main/pcb
  firmware_url: https://github.com/NerdFlare/NF-SolderChallenge26/tree/main/code/nf-solderchallenge26
  eda_tool: KiCad
links:
- label: github.com/NerdFlare/NF-SolderChallenge26
  url: https://github.com/NerdFlare/NF-SolderChallenge26
  kind: repo
- label: nerdflare.github.io
  url: https://nerdflare.github.io
  kind: website
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: unknown
sources:
- kind: url
  url: https://github.com/NerdFlare/NF-SolderChallenge26
  title: NerdFlare Solder Challenge 26
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/NerdFlare/NF-SolderChallenge26/main/code/nf-solderchallenge26/nf-solderchallenge26.ino
  title: nf-solderchallenge26.ino
  accessed: '2026-09-07'
  note: Firmware confirms 5 LED pins chased in sequence via digitalWrite/delay.
- kind: url
  url: https://raw.githubusercontent.com/NerdFlare/NF-SolderChallenge26/main/pcb/NerdFlare-solder-challenge26.kicad_sch
  title: NerdFlare-solder-challenge26.kicad_sch
  accessed: '2026-09-07'
  note: Schematic lists ATtiny85V-10S MCU, AVR-ISP-6 programming header, a battery cell, and one LED/resistor pair per package size.
- kind: url
  url: https://github.com/NerdFlare
  title: Cal Poly NerdFlare (GitHub org)
  accessed: '2026-09-07'
  note: Confirms NerdFlare is a Cal Poly student club, not a con vendor; repo description dates the board to the 2026 challenge.
- kind: url
  url: https://nerdflare.github.io
  title: Cal Poly NerdFlare
  accessed: '2026-09-07'
  note: 'Club site: "Cal Poly club dedicated to making art from technology."'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: NerdFlare is Cal Poly's electronics-art club (not a hacker-con vendor), and this board is an internal 2026 soldering challenge/practice piece rather than something sold or distributed at a convention, so no matching event id exists in events.yml and it stays filed under "other". No product photos, price, quantity, distribution details, or PCB color were found anywhere in the repo or the club site; the repo has no README. Battery cell type and board shape/color are unconfirmed since no images exist. The club's other repos (NerdFlareBadge25, NerdFlareBadge26, sparky-sao-display, iFixit-SAO-2026) look like separate badge/SAO projects that could merit their own entries.
last_modified_date: '2026-09-07'
---

The NerdFlare Solder Challenge 26 is a small practice PCB built by Cal Poly's NerdFlare club — a student group described on its own site as being "dedicated to making art from technology" — for its 2026 soldering challenge. Rather than being a badge worn at a hacker conference, it's a teaching/testing board: five LEDs, one each in through-hole, 1206, 0805, 0603, and 0402 package sizes, are wired to an ATtiny85V microcontroller that lights them one after another. A builder who solders all five joints correctly sees the chase run cleanly across every package size, from the easiest (THT) down to the smallest (0402), making it a self-checking exercise in solder precision.

The hardware (KiCad schematic and PCB) and firmware (a short Arduino sketch) are both published on GitHub under NerdFlare's organization account, alongside the club's other projects, which include a couple of annual team badges and at least one other SAO. No storefront, price, quantity, or photos of the assembled board were found, and the repository carries no README, so distribution details (whether it was a giveaway, a club-meeting kit, or something else) remain unknown.
