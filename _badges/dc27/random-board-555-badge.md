---
title: Random Board 555 Badge
id: dc27-random-board-555-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Greymanhw (@greymanhw)
summary: 'A repurposed green PCB of unknown origin, given to the maker by another attendee at DEF CON 26, hacked into a badge with a 555 timer and shift register driving ten point-to-point wired LEDs.'
functions: 'Blinks ten LEDs, driven by a 555 timer astable circuit feeding a shift register.'
look:
  colors: [green]
  shape: null
  themes: []
tech:
  mcu: none
  leds:
    count: 10
    type: discrete
    note: Point-to-point wired, driven by a 555 timer and shift register rather than a microcontroller.
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
  where: 'One-off personal project; not sold or distributed.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
images:
  - file: assets/images/badges/dc27/random-board-555-badge/f73004ca45.jpg
    source: "https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/"
    credit: "Hackaday / Greymanhw"
    caption: "A repurposed green PCB hosting a 555 timer, shift register, and 10 point-to-point wired LEDs"
contact: {}
notes:
- 555-timer-based independent badge by Greymanhw shown at DEF CON 27. Found by the event-year sweep, task dc27-badges.
- 'Duplicate: this entry describes the same badge as dc27-555-timer-shift-register-badge (same maker, same event, same Hackaday source, same photo). That entry was researched more fully; consider merging into it.'
status: listed
sources:
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Random Board 555 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-badges); event read as ''dc27''.'
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: 'DEF CON 27: Pictorial Guide To The Unofficial Electronic Badges'
  accessed: '2026-09-08'
  note: 'Confirmed the badge: Greymanhw''s scrap green PCB fitted with a 555 timer, shift register, and 10 point-to-point wired LEDs. Source of the entry''s photo.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed by Hackaday''s DC27 badge roundup. The maker calls it a scrap PCB of unknown origin repurposed with a 555 timer, shift register, and 10 point-to-point wired LEDs; no maker-given title is known, so the sweep''s descriptive title is kept. No price, quantity, or distribution info exists because this reads as a one-off personal project, not something sold or given away. This entry duplicates dc27-555-timer-shift-register-badge, which was researched in more depth (maker''s GitHub/X checked, DEF CON forum repost found); that entry is the better one to keep.'
last_modified_date: '2026-09-08'
---

A one-off DEF CON 27 badge by the maker known as Greymanhw, built from a mystery green PCB someone else handed them at DEF CON 26. Not knowing what the board was originally meant to do, Greymanhw repurposed it, wiring in a 555 timer and a shift register to drive ten LEDs connected point-to-point. It appeared in Hackaday's September 2019 pictorial roundup of DEF CON 27's independent ("badgelife") badges, which is the only documentation found of it.

No evidence turned up that the badge was sold, kitted, or open-sourced — it reads as a scrappy, one-off hack rather than a distributed badge.

This entry duplicates `dc27-555-timer-shift-register-badge`, an entry describing the same badge from the same source and photo; that entry has additional research (maker's GitHub/X checked, a DEF CON forum repost of the source found) and is the better one to keep if the two are merged.
