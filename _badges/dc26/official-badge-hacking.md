---
title: DEF CON 26 Official Badge Hacking
id: dc26-official-badge-hacking
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc26
year: 2018
makers: []
summary: 'A Hackaday.io group project documenting the collaborative reverse-engineering of the official DEF CON 26 conference badge, not a badge or SAO of its own.'
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/160333-def-con-26-official-badge-hacking
  url: https://hackaday.io/project/160333-def-con-26-official-badge-hacking
  kind: hackaday
images: []
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/160333-def-con-26-official-badge-hacking
  title: DEF CON 26 Official Badge Hacking
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''DEF CON 26''.'
- kind: url
  url: https://hackaday.io/project/160333-def-con-26-official-badge-hacking
  title: DEF CON 26 Official Badge Hacking
  accessed: '2026-09-07'
  note: 'Re-fetched to characterize the page: a 439-member collaborative Hackaday.io project (created Aug 9, 2018) logging reverse-engineering of the official DC26 conference badge''s serial-console game, not a maker''s own badge or SAO listing.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    This is not a distinct badge/SAO. It is a community Hackaday.io project page where
    attendees collaboratively decoded the puzzle/game built into the official DEF CON 26
    conference badge (a text-adventure over serial console, with human/goon/speaker badge
    variants running different firmware). No single maker, product listing, price, or
    design files are associated with the page itself; it documents hacking of a badge that
    DEF CON itself produced. No open-source files were found on the project page. Treating
    as not_an_item rather than deleting or reassigning, per research-guide.md's special-case
    handling for pages that are not themselves a specific badge/SAO.
last_modified_date: '2026-09-07'
---

This Hackaday.io page (project #160333, created August 9, 2018) is not a badge or SAO in its own right — it is a collaborative reverse-engineering effort by roughly 439 people working out the puzzle embedded in that year's official DEF CON 26 conference badge. The badge ran a text-based adventure game over its serial console, with players moving through themed rooms (a ramen shop, a business district, an arcade, a garage, a mechanics bay) whose choices unlocked hex codes and lit up letters on the badge's own LEDs.

DEF CON 26 issued at least three badge variants — attendee ("human"), staff ("goon"), and speaker/press — each running different firmware that spat out badge-specific text in the game. Participants found that badges could communicate with each other to unlock further content, that a chip labeled U7 in the "ramen shop" section of the game had accessible test pins, and that placing a magnet near certain badge traces triggered a train-themed sequence. No design files, pricing, or quantity figures are published on the project page; it functions purely as a shared log of findings rather than a store listing or hardware release.
