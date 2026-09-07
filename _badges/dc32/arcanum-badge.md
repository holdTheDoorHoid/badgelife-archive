---
title: Arcanum Badge
id: dc32-arcanum-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Abhinav Panda/Hackerware.io
summary: A glow-in-the-dark acrylic badge Hackerware.io built for Jason Haddix's Arcanum, combining UV-printed PCB art with a laser-engraved acrylic overlay and RGB LEDs.
functions: A full-colour Arcanum badge combining the magic of glow in the dark and acrylic
look:
  colors:
  - blue
  - purple
  - clear
  - silver
  shape: null
  themes:
  - hardware tool
  - security
  - logo
tech:
  mcu: null
  leds:
    count: null
    type: RGB
    note: Side-emitting RGB LEDs light the laser-engraved acrylic logo; separate LEDs light red "eyes" and blue/purple hoodie grid squares; an LDR (photoresistor) switches in the purple hoodie LEDs in darkness.
  display: null
  connectivity: []
  battery: 2x coin cell
  sao_version: null
get_one:
  price: Free
  price_usd: 0.0
  quantity: '100'
  availability: free
  distribution:
  - free_drop
  where: Available at DEFCON 32
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: hackaday
  url: https://www.hackster.io/HacksFromPanda/the-arcanum-badge-217cfd
  label: 'The Arcanum Badge (Hackster.io project writeup)'
- kind: website
  url: https://www.hackerware.io/
  label: Hackerware.io
images:
- file: assets/images/badges/dc32/arcanum-badge/0013539b0e.jpg
  source: "https://www.hackster.io/HacksFromPanda/the-arcanum-badge-217cfd"
  credit: "Hackerware.io / Abhinav Panda"
  caption: "The finished Arcanum badge with acrylic overlay and lit LEDs"
- file: assets/images/badges/dc32/arcanum-badge/18ea2cf14e.jpg
  source: "https://www.hackster.io/HacksFromPanda/the-arcanum-badge-217cfd"
  credit: "Hackerware.io / Abhinav Panda"
  caption: "Close-up of the Arcanum badge glowing with red eyes and RGB hoodie LEDs"
contact:
  handles:
  - '@jhaddix'
  - '@arcanuminfosec'
  raw:
  - Twitter  and
notes:
- They will be at BsidesLV, BlackHat, and DEFCON doing drops everyday, First X people to arrive will get a badge and a swag bag
- 'Per the maker''s Hackster.io writeup: Jason Haddix of Arcanum asked Hackerware.io to design "a spectacular out of the box blinky badge." It was Arcanum''s first badge and combines a UV-printed PCB with a laser-engraved transparent acrylic overlay screwed on top, showing the Arcanum hoodied-hacker logo in blue/purple duotone.'
status: listed
sources:
- kind: sheet
  event: dc32
  row: 4
  updated: '2024-07-28'
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-arcanum-badge-217cfd
  title: 'The Arcanum Badge - Hackster.io'
  accessed: '2026-09-07'
  note: Maker's own project writeup; source for design, materials, LEDs, battery, and process details.
- kind: url
  url: https://www.hackerware.io/
  title: 'Hackerware - #BadgeLife | Hardware Design, Security, & Research.'
  accessed: '2026-09-07'
  note: Maker's studio site, confirms Hackerware.io as the fabricator/designer.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's Hackster.io writeup confirms design and construction (UV-printed PCB, laser-engraved acrylic overlay, side-emitting RGB LEDs, red "eye" LEDs, LDR-triggered purple hoodie LEDs, 2 coin cells) but does not state an MCU, LED count, SAO header, open-source status, or a specific production quantity beyond the sheet's "100". No storefront or repo found; likely a free-drop-only badge with no public hardware files. Not to be confused with the later, unrelated "Arcanum Gospel Book Badge" (DC33) from the same maker.
last_modified_date: '2026-09-07'
---

The Arcanum Badge was made by Abhinav Panda's Hackerware.io for Jason Haddix's Arcanum, and was the first badge Arcanum ever commissioned. Haddix asked Hackerware.io for "a spectacular out of the box blinky badge," and the team built around the Arcanum logo — a hoodied hacker silhouette in a blue-and-purple duotone — with one side meant to read in daylight and the other to glow in the dark, a nod to the different roles a hacker plays.

Construction combines a UV-printed PCB with a separate, laser-engraved transparent acrylic overlay screwed on top in the exact shape of the badge, so the LEDs underneath shine through without interference. Side-emitting RGB LEDs light the engraved Arcanum logo from the edge, while additional LEDs form red "eyes" and a square grid of blue hoodie lights (square rather than the studio's usual circular glow, meant to evoke a digital grid). A photoresistor (LDR) senses ambient light and switches on extra purple hoodie LEDs when the badge is in the dark. It runs on two coin cell batteries. The maker's writeup also describes a fabrication fix mid-run: an early UV-print layer on the PCB itself was dimming the LEDs, so the team erased that layer, restored the boards to bare HASL finish, and instead printed the artwork mirrored onto the back of the acrylic layer, which brightened the LED glow and added a "floating halo" look.

Per the community sheet, about 100 were made and given away free at DEF CON 32, with Arcanum also doing drops at BSidesLV and Black Hat that year. No storefront, repository, or design files were found, and the writeup does not name an MCU or state an exact LED count, so those fields are left blank rather than guessed.
