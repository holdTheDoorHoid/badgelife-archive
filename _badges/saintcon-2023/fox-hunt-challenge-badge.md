---
title: Fox Hunt Challenge Badge
id: saintcon-2023-fox-hunt-challenge-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: bfcoder
summary: A SAINTCON 2023 contest minibadge for the Fox Hunt challenge, a radio-direction-finding
  game where players locate hidden morse-code beacons around the con.
functions: Awarded for taking part in the Fox Hunt challenge; the badge itself is a simple
  passive PCB (one LED, one resistor) with no on-board radio or game logic of its own.
look:
  colors:
  - red
  shape: fox head
  themes:
  - animal
  - radio
  - ctf
tech:
  mcu: none
  leds:
    count: 1
    type: 1206 discrete
    note: Single white LED (D1), hand-soldered single-pad style.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - contest
  where: Handed out at SAINTCON 2023 to attendees who participated in the Fox Hunt challenge
    (finding hidden morse-code beacons via ham radio or SDR).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: doc
images: []
contact: {}
notes:
- 2023 Contest minibadge for the Fox Hunt radio-direction-finding challenge (hidden morse-code beacons). Found by the event-year sweep, task saintcon-2023.
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: Fox Hunt Challenge Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: 2023 SAINTCON Minibadge Guide (page 48, "Fox Hunt Challenge Badge")
  accessed: '2026-09-10'
  note: Official con minibadge guide page for this badge confirms maker (bfcoder), description, difficulty/rarity, assembly (1 LED, 1 resistor, FR4 PCB, 2-pin header), and distribution method (contest participation).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Core facts confirmed directly from SAINTCON's own 2023 Minibadge Guide (a PDF, page 48), which is the maker/event's own document. The badge is a fox-head-shaped red PCB minibadge with a single white LED and no MCU or radio hardware of its own -- the "fox hunt" is a physical/RF scavenger hunt using the players' own ham/SDR gear, not something the badge itself performs. Could not find a hostable image URL for the badge photo (it exists only as an embedded image inside the PDF guide, not as a standalone web image), so no photo was saved to images. Quantity made, battery/power details (if any -- the 2-pin header suggests it may plug into a lanyard/coin-cell holder used across the minibadge line), and open-source status are not stated anywhere in the source and were left empty rather than guessed.
last_modified_date: '2026-09-10'
---

The Fox Hunt Challenge Badge is a SAINTCON 2023 contest minibadge, designed by bfcoder and awarded to attendees who took part in the con's Fox Hunt challenge: a radio-direction-finding game in which beacons hidden around the venue transmit morse code on assigned frequencies, and players track them down using ham radio, software-defined radio, or other RF-hunting gear. Per SAINTCON's own 2023 Minibadge Guide, the challenge was rated beginner difficulty and uncommon rarity, and the badge was simply given to anyone who came and participated -- no purchase involved.

Electrically the badge is bare-bones: a red, fox-head-shaped FR4 PCB carrying a single 1206 white LED (D1) and a matching 1206 resistor, populated through 2-pin headers, with no microcontroller, radio, or display on board. It is a keepsake/participation token for the challenge rather than a functional part of the hunt itself -- the direction-finding is done with the player's own equipment, not the badge.
