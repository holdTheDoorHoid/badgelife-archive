---
title: Arcanum Badge
id: dc34-arcanum-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
series: Arcanum
makers:
- name: Abhinav Panda / Hackerware.io
  url: https://hackerware.io
summary: A hand-assembled electronic badge for the cybersecurity firm Arcanum, stacking three acrylic layers over a servo-driven spinning disc lit by filament LEDs, addressable RGB, and hand-set gemstones.
functions: 3 layers of acrylic, lights and art in motion, adorned with gemstones. A servo motor turns a second acrylic disc bearing arcanist symbols; a button cycles four modes (Sync-spin, Randomizer, Disco, Puzzle), and a vibration motor buzzes at cues in each mode. In Randomizer mode the disc rocks to a stop with a window landing on a random digit 0-9 printed on the base layer.
look:
  colors:
  - purple
  - gold
  - multicolor
  shape: shield
  themes:
  - fantasy
  - security
  - puzzle
  - jewelry
  form_factor: pcb badge
tech:
  mcu: ATmega32
  leds:
    count: null
    type: RGB, filament LED noodles
    note: Addressable RGB LEDs drive the animated modes; bendable filament LEDs form glowing spokes across the face.
  display: none
  connectivity: []
  inputs:
  - buttons
  power: 3x AAA
  battery: 3x AAA
  sao_version: null
get_one:
  price: Free giveaways, follow Arcanum and Jhaddix handles
  price_usd: 0.0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Free giveaways, follow Arcanum and Jhaddix handles
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: Arcanum badge product page (Hackerware.io)
  url: https://hackerware.io/arcanum
  kind: website
- label: x.com/TweetsFromPanda/status/2085874637951373502?s=20
  url: https://x.com/TweetsFromPanda/status/2085874637951373502?s=20
  kind: video
- label: Arcanum Security (client)
  url: https://arcanum-sec.com/
  kind: website
  archived: https://web.archive.org/web/20260814141750/https://arcanum-sec.com/
images:
- file: assets/images/badges/dc34/arcanum-badge/3e153314f4.jpg
  source: https://hackerware.io/arcanum
  credit: Hackerware
  caption: The finished Arcanum badge lit up, showing glowing filament spokes, RGB LEDs and set gemstones under clear acrylic
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
  row: 68
  updated: 8/7/2026 18:45:52
  listing: New
- kind: url
  url: https://hackerware.io/arcanum
  title: Arcanum — Hackerware
  accessed: '2026-09-06'
  note: Maker's own product page; source for name, maker, MCU (ATmega32), build (3 acrylic layers, servo disc), lighting (filament + RGB + gemstones), four operating modes, vibration motor, and 3xAAA power.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts confirmed on the maker's own product page (hackerware.io/arcanum), which also names the client, "Arcanum" (arcanum-sec.com), a cybersecurity consulting/training firm this badge was made for. This continues a yearly series - dc32-arcanum-badge and dc33-arcanum-gospel-book-badge are the same maker/client line at earlier DEF CONs. Could not verify the linked tweet (x.com/TweetsFromPanda/status/2085874637951373502) - X returned an HTTP 402 payment-required error to automated fetches. No price, exact LED count, or production quantity is published; it is described only as a free giveaway tied to following the Arcanum and Jhaddix social handles.
last_modified_date: '2026-09-06'
---

The Arcanum Badge is Hackerware's most intricate build, made as a giveaway for the cybersecurity firm Arcanum (arcanum-sec.com) and, per the maker, assembled entirely by hand over hours per unit. It stacks three separate acrylic layers on a purple PCB: a base layer that carries the artwork and every light source (bendable filament LED "noodles," addressable RGB, and gemstones set by a jeweller), a second acrylic disc turned by a servo motor and printed with six arcanist symbols (Foresight, Access, Resilience, Mastery, Patience, Discernment), and a clear top layer that protects the assembly while letting the light and motion show through.

An ATmega32 microcontroller drives four selectable modes reached with a button: Sync-spin (disc motion locked to the light animation), Randomizer (the disc rocks to a stop, landing a window over a random printed digit 0-9), Disco (lights and disc at full speed), and Puzzle (a movement sequence stops on a hidden cue that rewards a correct read with a new glow sequence). A vibration motor buzzes at cued moments in each mode. Power comes from 3x AAA batteries.

This is the third badge in an annual "Arcanum" line from the same maker for the same client, following dc32-arcanum-badge and dc33-arcanum-gospel-book-badge. It was distributed as a free giveaway at DEF CON 34, tied to following the Arcanum and Jhaddix social accounts, rather than sold.
