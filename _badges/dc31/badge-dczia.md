---
title: Electric Sampler (DCZia)
id: dc31-badge-dczia
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: DCZia
  url: https://dczia.net/
summary: A eurorack-format sampler, step sequencer, and MIDI controller badge built around a Raspberry Pi RP2040, sold assembled or as a solder-it-yourself kit by DCZia member Snurkle Engineering.
functions: 'Multiple modes selected with a rotary encoder and OLED screen: an LED light mode; a sampler mode with an 8-key step sequencer and per-step volume, loading WAV samples from an onboard microSD card; a pre-programmed sequencer mode; a MIDI controller mode; and a USB HID keyboard mode.'
look:
  colors:
  - pink
  - multicolor
  shape: rectangle
  themes:
  - music
  - synthwave
  - hardware tool
tech:
  mcu: RP2040
  leds:
    count: null
    type: null
    note: 8 backlit sequence keys (Cherry MX yellow mechanical switches)
  display: small OLED
  connectivity:
  - midi
  - usb
  battery: battery-powered with a built-in speaker
  sao_version: null
get_one:
  price: $110
  price_usd: 110
  quantity: ''
  availability: sold_out
  availability_note: Listed sold out on Tindie as of Sep 25, 2023; checked 2026-09-07.
  distribution:
  - purchase
  where: Sold via Snurkle Engineering's Tindie store (in Sandy, UT), both as a partial-assembly kit and, for an added cost, fully assembled; also distributed at DEF CON 31 itself.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/dczia/Defcon31-Badge/tree/main/Hardware
  firmware_url: https://github.com/dczia/Defcon31-Badge/tree/main/Firmware
  eda_tool: KiCad
  fab_url: null
  bom_url: https://github.com/dczia/Defcon31-Badge/blob/main/Hardware/Final/DCZIA%20DC31%20BADGE%20BOM.xlsx
  license: null
  notes: No LICENSE file found in the repo; hardware and firmware/software are published but terms aren't stated.
links:
- label: github.com/dczia/Defcon31-Badge
  url: https://github.com/dczia/Defcon31-Badge
  kind: repo
- label: 'Tindie: DCZia Electric Sampler'
  url: https://www.tindie.com/products/hamster/dczia-electric-sampler/
  kind: store
- label: 'Tindie: DCZia DEF CON 31 updated front panel'
  url: https://www.tindie.com/products/hamster/dczia-defcon-31-updated-front-panel/
  kind: store
- label: DCZia
  url: https://dczia.net/
  kind: website
images:
- file: assets/images/badges/dc31/badge-dczia/7f5ceab44c.jpg
  source: "https://www.tindie.com/products/hamster/dczia-electric-sampler/"
  credit: "snurkle engineering / DCZia"
  caption: "DCZia Electric Sampler badge, assembled"
- file: assets/images/badges/dc31/badge-dczia/9e2b3beb0b.jpg
  source: "https://www.tindie.com/products/hamster/dczia-electric-sampler/"
  credit: "snurkle engineering / DCZia"
  caption: "DCZia Electric Sampler badge, alternate view"
contact: {}
notes:
- 'Duplicate of dc31-electric-sampler-badge, which already has a fuller writeup; this entry adds the price, sold-out status, and Tindie storefront/photos that the other entry lacked.'
status: released
sources:
- kind: url
  url: https://github.com/dczia/Defcon31-Badge
  title: Defcon31-Badge (DCZia)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 31''.'
- kind: url
  url: https://github.com/dczia/Defcon31-Badge
  title: dczia/Defcon31-Badge - DCZia DC31 Badge
  accessed: '2026-09-07'
  note: README confirms name (Electric Sampler), RP2040/OLED/audio/MIDI/sync/microSD/eurorack specs, and build/assembly instructions.
- kind: url
  url: https://www.tindie.com/products/hamster/dczia-electric-sampler/
  title: DCZia Electric Sampler - snurkle engineering
  accessed: '2026-09-07'
  note: Price ($110), sold-out status (since Sep 25, 2023), maker/seller identity, feature list, and product photos.
- kind: url
  url: https://dczia.net/about.html
  title: About DCZia
  accessed: '2026-09-07'
  note: Confirms DCZia as a group formed around DEF CON 22 with New Mexico roots, and lists Electric Sampler as their DEF CON 31 (2023) badge.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Duplicate of dc31-electric-sampler-badge (same badge, same repo). LED count/type and exact quantity made are not stated anywhere found; left empty. Maker name on Tindie is the seller "snurkle engineering" (a DCZia member), distinct from the DCZia group name used on GitHub/website.'
last_modified_date: '2026-09-07'
---

The Electric Sampler is DCZia's badge for DEF CON 31 (2023): a Raspberry Pi RP2040-powered, Eurorack-format drum machine, sampler, and step sequencer with a full-color dye-sublimated PCB front panel. It has a small OLED screen, two rotary encoders, eight backlit Cherry MX-switch sequence keys, 3.5mm audio out, 3.5mm MIDI in/out, 3.5mm sync in/out, a microSD card slot, an SAO port, and both battery power (with a built-in speaker) and a Eurorack power connector, so it keeps working as a small instrument after the con.

It was sold through DCZia member Snurkle Engineering's Tindie store for $110, either as a mostly-assembled kit (surface-mount parts pre-populated, buyer solders on switches, jacks, screen, encoders, and battery) or fully built for an added fee, with an optional 16-character custom text option; it was also handed out at DEF CON 31 itself. The listing sold out by September 25, 2023. Hardware (KiCad schematics/PCB, STEP models, BOM) and firmware are published on GitHub, though no license file is included.

This entry duplicates `dc31-electric-sampler-badge`, which covers the same badge in more depth on functions and the build guide; this one adds the confirmed retail price, sold-out status, and Tindie photos.
