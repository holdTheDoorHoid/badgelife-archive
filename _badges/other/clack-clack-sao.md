---
title: Clack Clack SAO
id: other-clack-clack-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2022
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/twinkletwinkie
summary: A Simple Add-On shaped like a red octagon with a large Cherry MX Blue-style "Panic" button that lights up nine LEDs bright red when pressed; sold assembled on Tindie and also shared as open Gerbers on Hackaday.io.
functions: Pressing the big red panic button lights up its LEDs; purely a blinky/tactile novelty add-on, no other interactivity.
look:
  colors:
  - red
  shape: circle
  themes:
  - meme
tech:
  mcu: none
  leds:
    count: 9
    type: reverse-mount
    note: Nine side-view/reverse-mount LEDs glow red when the panic button is pressed.
  display: none
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: $25.00
  price_usd: 25
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold assembled on Tindie by TwinkleTwinkie; listing is now marked retired/no longer available.
make_your_own:
  open_source: true
  hardware_url: https://cdn.hackaday.io/files/1862817969846304/ClackClack-2020-08-11-2347.zip
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/186281-clack-clack-sao
  url: https://hackaday.io/project/186281-clack-clack-sao
  kind: hackaday
- label: cdn.hackaday.io/files/1862817969846304/ClackClack-2020-08-11-2347.zip
  url: https://cdn.hackaday.io/files/1862817969846304/ClackClack-2020-08-11-2347.zip
  kind: hackaday
- label: hackaday.io/twinkletwinkie
  url: https://hackaday.io/twinkletwinkie
  kind: hackaday
  archived: https://web.archive.org/web/20260523064136/https://hackaday.io/twinkletwinkie
- label: tindie.com/products/twinkletwinkie/twinkletwinkies-clackclack-panic-sao
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-clackclack-panic-sao/
  kind: store
  archived: https://web.archive.org/web/20260506214136/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-clackclack-panic-sao/
images:
- file: assets/images/badges/other/clack-clack-sao/e3e2d69fa0.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-clackclack-panic-sao/
  credit: TwinkleTwinkie
  caption: The ClackClack Panic SAO, a red octagonal board with a large red panic button
  archived: https://web.archive.org/web/20260506214136/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-clackclack-panic-sao/
- file: assets/images/badges/other/clack-clack-sao/b0da069113.jpg
  source: https://hackaday.io/project/186281-clack-clack-sao
  credit: TwinkleTwinkie
  caption: Clack Clack SAO project photo on Hackaday.io
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/186281-clack-clack-sao
  title: Clack Clack SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/twinkletwinkie
  title: TwinkleTwinkie's Profile | Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker identity (Hackaday.io member, SAO/badgelife designer); this specific project isn't listed among the profile's featured projects but its own project page names TwinkleTwinkie as the author.
  archived: https://web.archive.org/web/20260523064136/https://hackaday.io/twinkletwinkie
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-clackclack-panic-sao/
  title: TwinkleTwinkie's "ClackClack" Panic! SAO
  accessed: '2026-09-07'
  note: 'Storefront listing: price ($25), LED count (9), SAO v1.69bis compatibility, red octagon shape, blue mechanical switch with resin keycap, 3.3V power, sold fully assembled, now retired/sold out.'
  archived: https://web.archive.org/web/20260506214136/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-clackclack-panic-sao/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No specific convention or year of debut is stated on either the Hackaday.io project page or the Tindie listing; this is a general-release SAO rather than a badge made for one particular event, so event is left as 'other'. The Hackaday.io project itself is dated 2022, but the Gerber archive filename (ClackClack-2020-08-11-2347.zip) and the earliest Tindie product photo (dated 2020-09-17) suggest the design dates to 2020, with the Hackaday.io writeup posted later; year is left at the sheet's original 2022 pending a clearer source. Quantity made is not stated anywhere found.
last_modified_date: '2026-09-07'
---

The Clack Clack SAO is a small add-on board by PCB artist and badgelife designer TwinkleTwinkie (Duluth, GA), built around a single mechanical switch: a Cherry MX Blue-style key fitted with a custom red resin keycap that reads "Panic." Pressing it lights up nine reverse-mount LEDs around the red octagonal board, and its name comes from the audible "clack" of the blue switch itself. It runs on 3.3V (SAO header power) and needs no microcontroller — the lighting is driven directly off the switch.

It was sold fully assembled through TwinkleTwinkie's Tindie store for $25 and is compatible with the newer SAO v1.69bis (6-pin) standard while remaining backward compatible with the original 4-pin SAO header. The listing has since been marked retired and is no longer available for purchase. For anyone who wants to build their own, the bare Gerber files were also shared as a free download on the project's Hackaday.io page, though no firmware is involved since the board is a passive, switch-driven design. Neither page ties the badge to a specific convention or year of release, so it reads as a general-release SAO rather than one made for a single event's badge.

