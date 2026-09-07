---
title: BadgeLife SAO Soldering Kit
id: dc33-badgelife-sao-soldering-kit
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc33
year: 2025
makers:
- name: Make it Hackin
  url: https://www.tindie.com/stores/makeithackin/
summary: A beginner soldering kit that builds into a simple SAO with two reverse-mount LEDs, sold by Make it Hackin.
functions: It lights up! Two reverse-mount LEDs light when the assembled SAO is plugged into a badge's SAO header.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 2
    type: reverse-mount
    note: Each LED is paired with a 68 ohm resistor.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: $5-$10
  price_usd: 5.0
  quantity: ''
  availability: available
  distribution:
  - purchase
  - kit
  where: 'Sold by Make it Hackin on Tindie (https://www.tindie.com/products/makeithackin/badgelife-sao-kit/); listed at $5 on the DEF CON 33 community badge sheet and $10 on the current Tindie listing.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/MakeItHackin/BadgeLifeSAO
  firmware_url: null
  eda_tool: null
links:
- label: github.com/MakeItHackin/BadgeLifeSAO
  url: https://github.com/MakeItHackin/BadgeLifeSAO
  kind: repo
- label: BadgeLife SAO Kit on Tindie
  url: https://www.tindie.com/products/makeithackin/badgelife-sao-kit/
  kind: store
- label: Assembly tutorial (YouTube)
  url: https://youtu.be/Q6jLFrrscGw?t=40
  kind: video
images:
- file: assets/images/badges/dc33/badgelife-sao-soldering-kit/e132b6c318.jpg
  source: "https://github.com/MakeItHackin/BadgeLifeSAO"
  credit: "Make it Hackin"
  caption: "Assembled BadgeLife SAO kit with googly eyes and reverse-mount LEDs"
- file: assets/images/badges/dc33/badgelife-sao-soldering-kit/380894aa1c.jpg
  source: "https://www.tindie.com/products/makeithackin/badgelife-sao-kit/"
  credit: "Make it Hackin"
  caption: "BadgeLife SAO Kit product photo on Tindie"
contact:
  emails:
  - andrew@makeithackin.com
notes:
- Teaches you how to solder both through-hole and surface mount components
status: listed
sources:
- kind: sheet
  event: dc33
  row: 42
  updated: 8/3/2025 10:45:44
- kind: url
  url: https://github.com/MakeItHackin/BadgeLifeSAO
  title: "MakeItHackin/BadgeLifeSAO on GitHub"
  accessed: '2026-09-06'
  note: Maker's own project page; kit contents, assembly notes, links to Tindie store and tutorial video.
- kind: url
  url: https://www.tindie.com/products/makeithackin/badgelife-sao-kit/
  title: "BadgeLife SAO Kit from MakeItHackin on Tindie"
  accessed: '2026-09-06'
  note: Storefront listing; price ($10), kit contents, product photos, maker location (Huntsville, AL).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    The maker's GitHub repo and Tindie storefront both describe this exact kit
    (BadgeLife circuit board, two 68 ohm resistors, two reverse-mount LEDs, 2x3
    pin header, stickers, googly eyes) with a YouTube assembly tutorial. Could
    not confirm quantity made, an exact DEF CON 33 tie-in beyond the sheet
    listing, or whether this specific batch differs from the general Tindie
    listing (Tindie currently lists it at $10 with a bonus "C0V1D CTF SAO"
    while supplies last, versus $5 on the DEF CON 33 sheet) - noted as a price
    discrepancy rather than resolved. No MCU is used; it is a passive LED
    circuit. Design files (schematic/gerbers) were not found published in the
    GitHub repo beyond images and the README.
last_modified_date: '2026-09-06'
---

The BadgeLife SAO Soldering Kit is a beginner-friendly soldering project from Make it Hackin (Andrew, based in Huntsville, Alabama), sold through the maker's Tindie store and documented on GitHub. It is not a badge in its own right but a small add-on ("SAO") meant to plug into another badge's SAO header, aimed at people who want to practice both through-hole and surface-mount soldering.

Assembled, the kit is a simple passive circuit: two reverse-mount LEDs, each in series with a 68 ohm resistor, wired to a standard 2x3 SAO pin header, so the LEDs light up using power drawn from the host badge. There is no microcontroller. The kit ships with a small circuit board, the LEDs and resistors, the header, a couple of stickers ("Hacker Summer Camp" and "Make It Hackin"), and a pair of googly eyes for decoration. A YouTube video walks through assembly, and the maker notes that SAO header orientation varies by badge, so builders need to check polarity before plugging it in.

The GitHub repository (github.com/MakeItHackin/BadgeLifeSAO) hosts the project's description, a product photo, and links to the Tindie listing and tutorial, but does not include published schematics or Gerbers, so it is only partially open. The community sheet for DEF CON 33 lists the price at $5; the current Tindie listing prices it at $10 and throws in a bonus "C0V1D CTF SAO" while supplies last, which may reflect a later update to the listing rather than the DEF CON 33 sale price.
