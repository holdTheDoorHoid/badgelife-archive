---
title: Sailor Moon Badge
id: dc31-sailor-moon-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Ninjaican
summary: A DIY solder-kit badge featuring Sailor Moon artwork backlit by four pink LEDs, built around a discrete-transistor astable multivibrator instead of a microcontroller.
functions: Four 3mm pink LEDs fade in and out to backlight the artwork, driven by a BC547/BC557 astable multivibrator circuit (no microcontroller). Header pins double as a fold-out stand so the badge can be displayed upright.
look:
  colors: []
  shape: null
  themes:
  - anime
  - pop culture
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: Four 3mm pink LEDs, faded via a BC547/BC557 astable multivibrator (no driver IC or MCU).
  display: null
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: $40.00
  price_usd: 40.0
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Distributed in person at DEF CON 31 via surprise "badge drops" announced on social media by the maker (handle alt_bier). Sold mostly as DIY solder kits, with some pre-assembled units also given/sold out.'
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/gowenrw/sailor_moon_badge
  firmware_url: null
  eda_tool: KiCad
notes:
- Available In-person at con wherever alt_bier is doing badge drops (look for tweets). Alt_bier likes to do drops right when you least expect it. Might as well remain awake for the entire con (1-2-3 rule).
- 'The project site (sailormoon.altbier.us) spells the maker''s handle "Ninjician"; the community sheet spells it "Ninjaican." Kept the sheet spelling for the maker field.'
status: released
sources:
- kind: sheet
  event: dc31
  row: 64
  updated: '2023-08-03'
- kind: url
  url: https://sailormoon.altbier.us/
  title: Sailor Moon Badge - DC31 (Ninjaican/altbier project page)
  accessed: '2026-09-06'
  note: Confirmed maker, LED count/color, driving circuit (astable multivibrator, no MCU), DIY-kit distribution, and stand feature; provided links to the GitHub repo and product photos.
- kind: url
  url: https://github.com/gowenrw/sailor_moon_badge
  title: gowenrw/sailor_moon_badge on GitHub
  accessed: '2026-09-06'
  note: Confirms open-source status (MIT license), KiCad 6.x project, and that the repo bundles art, code, CAD, and fab files for the DC31 badge.
links:
- label: sailormoon.altbier.us
  url: https://sailormoon.altbier.us/
  kind: website
- label: gowenrw/sailor_moon_badge (GitHub)
  url: https://github.com/gowenrw/sailor_moon_badge
  kind: repo
images:
- file: assets/images/badges/dc31/sailor-moon-badge/b14898a858.jpg
  source: "https://sailormoon.altbier.us/"
  credit: "Ninjaican"
  caption: "Sailor Moon badge, front view showing artwork"
- file: assets/images/badges/dc31/sailor-moon-badge/b475501480.jpg
  source: "https://sailormoon.altbier.us/"
  credit: "Ninjaican"
  caption: "Sailor Moon badge, back view showing LED circuit"
contact: {}
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core facts (maker, circuit, LEDs, distribution, open-source repo) confirmed directly on the maker''s own project page and GitHub repo. Not found: exact quantity made, whether it was free or paid at the drop (the $40 price from the community sheet is unconfirmed elsewhere), and PCB colorway/shape details (no colors/shape stated on the source pages, left empty rather than guessed). The repo owner GitHub handle (gowenrw) differs from the maker handle used on the project site (alt_bier/Ninjician) and the sheet (Ninjaican); likely the same person or a close collaborator, but not stated explicitly, so makers.name was left as the sheet''s original spelling.'
last_modified_date: '2026-09-06'
---

The Sailor Moon Badge is a DC31 (2023) indie badge by Ninjaican, distributed the way a lot of alt_bier's badges are: as a surprise in-person drop at the con, announced without much warning on social media, mostly as a DIY solder kit with a handful of pre-assembled units available for people who didn't want to build their own.

Electrically it's deliberately simple: rather than a microcontroller, it uses a discrete BC547/BC557 astable multivibrator to fade four 3mm pink LEDs behind Sailor Moon artwork, giving a soft pulsing backlight. Header pins on the board double as a fold-out stand, so the badge can stand upright on a shelf next to other collectibles once the con is over.

The hardware, artwork, and fab files are published on GitHub (gowenrw/sailor_moon_badge) as a KiCad 6.x project under the MIT license, making it fully open source, though a firmware repo doesn't apply here since the board has no microcontroller to program.
