---
title: 555 Timer & Shift Register Badge
id: dc27-555-timer-shift-register-badge
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
- label: DEF CON Forums repost of the Hackaday DC27 badge roundup
  url: https://forum.defcon.org/node/229873
  kind: article
- label: greymanhw on X (formerly Twitter)
  url: https://x.com/greymanhw
  kind: social
- label: greymanhw on GitHub
  url: https://github.com/greymanhw
  kind: repo
images:
  - file: assets/images/badges/dc27/555-timer-shift-register-badge/f73004ca45.jpg
    source: "https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/"
    credit: "Hackaday / Greymanhw"
    caption: "A repurposed green PCB hosting a 555 timer, shift register, and 10 point-to-point wired LEDs"
contact: {}
notes:
- A repurposed-green-PCB independent badge for DC27 built around a 555 timer and shift register, per Hackaday's roundup. Found by the event-year sweep, task dc27-indie.
- 'Duplicate: this entry describes the same badge as dc27-random-board-555-badge (same maker, same event, same Hackaday source). Both entries were created independently by the discovery sweep; consider merging.'
status: listed
sources:
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: 555 Timer & Shift Register Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-indie); event read as ''dc27''.'
- kind: url
  url: https://forum.defcon.org/node/229873
  title: 'Hackaday: Mike Szczys, DEF CON 27: Pictorial Guide To ...'
  accessed: '2026-09-08'
  note: 'Repost of the same Hackaday text on the DEF CON forums; confirms the badge description, no new details.'
- kind: url
  url: https://x.com/greymanhw
  title: greymanhw unlocking hardware features! (@greymanhw) / X
  accessed: '2026-09-08'
  note: "Maker's own account; checked for badge photos/details, none specific to this DC27 badge found in the fetched content."
- kind: url
  url: https://github.com/greymanhw
  title: greymanhw (GitHub)
  accessed: '2026-09-08'
  note: "Maker's repos (tft_wifi_ble_scanner, gold-star, esp32scratches) do not include this badge; it does not appear to be open-sourced."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed by Hackaday''s DC27 badge roundup (and its DEF CON forum repost), both citing the same original text/photo, so effectively one source. The maker calls it a scrap PCB of unknown origin repurposed with a 555 timer, shift register, and 10 point-to-point wired LEDs; no title of the maker''s own is known, so the sweep''s descriptive title is kept. No price, quantity, or distribution info exists because this reads as a one-off personal project, not something sold or given away. Maker''s GitHub and X were checked; neither turned up build files or additional photos of this specific badge. This entry duplicates dc27-random-board-555-badge, created independently by an earlier sweep pass from the same source.'
last_modified_date: '2026-09-08'
---

A one-off DEF CON 27 badge by the maker known as Greymanhw, built from a mystery green PCB someone else handed them at DEF CON 26. Not knowing what the board was originally meant to do, Greymanhw repurposed it, wiring in a 555 timer and a shift register to drive ten LEDs connected point-to-point. It appeared in Hackaday's September 2019 pictorial roundup of DEF CON 27's independent ("badgelife") badges, which is the only documentation found of it.

No evidence turned up that the badge was sold, kitted, or open-sourced — it reads as a scrappy, one-off hack rather than a distributed badge. The maker's GitHub (tft_wifi_ble_scanner, gold-star, esp32scratches) and X account do not reference this specific board.

This entry appears to duplicate `dc27-random-board-555-badge`, an earlier sweep entry describing the same badge from the same source; the two likely should be merged.
