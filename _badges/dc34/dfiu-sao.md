---
title: DFIU SAO
id: dc34-dfiu-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: BigFuckingBadge
  url: https://www.bigfuckingbadge.com
summary: 'A face-shaped SAO bearing "Lintile", inspired by DEF CON''s Hacker Jeopardy, that plays a "Don''t Fuck It Up" chant.'
functions: If you touch Lintile's face, it plays the "don't fuck it up" chant. It can also be left playing the chant on a loop.
look:
  colors:
  - gold
  - white
  shape: face
  themes:
  - meme
  - pop culture
  - text
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $20
  price_usd: 20.0
  quantity: ''
  availability: limited
  distribution:
  - purchase
  - preorder
  where: 'Presale by request via email (bfb.team.public@gmail.com), paid over Venmo/PayPal/Cashapp/cash; drops at DEF CON 34''s BadgeLife Village.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.bigfuckingbadge.com
  url: https://www.bigfuckingbadge.com
  kind: store
- label: github.com/Hexum064/dfiu-ch32v003-pcb
  url: https://github.com/Hexum064/dfiu-ch32v003-pcb
  kind: repo
- label: github.com/Hexum064/dfiu-ch32v003-code
  url: https://github.com/Hexum064/dfiu-ch32v003-code
  kind: repo
images:
- file: assets/images/badges/dc34/dfiu-sao/c63d23d966.jpg
  source: "https://www.bigfuckingbadge.com"
  credit: "BigFuckingBadge"
  caption: "DFIU SAO, featuring Lintile's face"
contact:
  discord: Hexum064
  emails:
  - bfb.team.public@gmail.com
notes: []
status: listed
sources:
- kind: sheet
  event: dc34
  row: 39
  updated: 7/7/2026 11:18:23
  listing: New
- kind: url
  url: https://www.bigfuckingbadge.com
  title: "BIGFUCKINGBADGE.COM — Defcon 34 Badges and SAOs"
  accessed: '2026-09-06'
  note: "Confirms price ($20), description, presale/order process, DEF CON 34 BadgeLife Village drop times, and the item photo."
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: >-
    Maker's storefront confirms the item, price, and presale process, but gives no chip,
    LED, or quantity specifics. Both linked GitHub repos (dfiu-ch32v003-pcb,
    dfiu-ch32v003-code) return 404 as of 2026-09-06, so they could not be used to verify
    hardware/firmware details or confirm open-source status; their names suggest a
    CH32V003 MCU but this is unconfirmed and was left blank rather than guessed. Photo
    shows a face-shaped PCB (gold immersion finish over white silkscreen halftone
    portrait) with star-shaped cutouts that light up, implying onboard LEDs, but count
    and type are not stated anywhere and were left null.
last_modified_date: '2026-09-06'
---

The DFIU SAO is part of BigFuckingBadge's "OffensiveSAO" lineup for DEF CON 34, alongside that year's PORTAL Badge, PORTAL Gun SAO, IFLFU SAO, and "fuck" Note SAO. It is a face-shaped PCB depicting "Lintile," a nod to DEF CON's long-running Hacker Jeopardy event, and it plays a "Don't Fuck It Up" chant track when triggered — either as a one-off or looped to annoy anyone nearby. The board is a gold (copper/immersion) finish with a white silkscreen halftone portrait, and its star-shaped cutouts appear to be lit from behind, indicating onboard LEDs, though the maker's page does not specify the count, type, or driving microcontroller.

It sold for $20 as a presale item: the maker directed buyers to email bfb.team.public@gmail.com to arrange a presale and a drop time, with payment by Venmo, PayPal, Cashapp, or cash, and pickup scheduled around BadgeLife Village drop times at DEF CON 34 (Las Vegas, August 2026). The storefront listed quantities as "limited" but did not give an exact production number.

The entry's two linked GitHub repositories, `dfiu-ch32v003-pcb` and `dfiu-ch32v003-code`, would ordinarily be the place to confirm the MCU (their names suggest a CH32V003) and check for open-source hardware/firmware, but both returned a 404 at the time of this research and could not be read.
