---
title: DC31 Plumbus BFB
id: dc31-plumbus-bfb
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: hexum064
  url: https://hackaday.io/hexum064
- name: pinguino
  url: https://hackaday.io/pinguino
- name: erin
  url: https://hackaday.io/erin
summary: 'An unofficial, independently-made electronic badge for DEF CON 31, built by the BFB team as a follow-up to their earlier "Big Fucking Badge" projects, deliberately made smaller, cheaper and less power-hungry.'
functions: 'Four tactile dome-switch buttons and hall-effect sensors drive interactive game modes and a puzzle with a hidden prize/easter egg; programmable LED lighting patterns; standby/low-power operation; has an SAO connector for add-ons.'
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - pop culture
tech:
  mcu: Microchip xMega (xmega32e5 / xmega16e5)
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '99 (plus one bad unit)'
  availability: unknown
  distribution: []
  where: 'Distributed to attendees at DEF CON 31, 2023; not a commercial product.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/189615-dc31-plumbus-bfb
  url: https://hackaday.io/project/189615-dc31-plumbus-bfb
  kind: hackaday
- label: DC31 SAO (companion SAO by the same BFB team)
  url: https://hackaday.io/project/192013-dc31-sao
  kind: hackaday
images:
- file: assets/images/badges/dc31/plumbus-bfb/f44c9f4d86.jpg
  source: "https://hackaday.io/project/189615-dc31-plumbus-bfb"
  credit: "BFB team (hexum064)"
  caption: "DC31 Plumbus BFB badge"
- file: assets/images/badges/dc31/plumbus-bfb/21ae1a33fb.jpg
  source: "https://hackaday.io/project/189615-dc31-plumbus-bfb"
  credit: "BFB team (hexum064)"
  caption: "DC31 Plumbus BFB badge, assembled"
contact:
  twitter: "@TeamBFBPublic"
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/189615-dc31-plumbus-bfb
  title: DC31 Plumbus BFB
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''DEF CON 31''.'
- kind: url
  url: https://hackaday.io/project/189615-dc31-plumbus-bfb
  title: DC31 Plumbus BFB
  accessed: '2026-09-07'
  note: 'Maker names, features (buttons, hall-effect sensors, LEDs, game/puzzle modes, no on-badge screen), MCU (xMega 32e5/16e5), quantity made (99 + 1 bad), manufactured via AllPCB, contact handles.'
- kind: url
  url: https://hackaday.io/project/192013-dc31-sao
  title: DC31 SAO
  accessed: '2026-09-07'
  note: 'Companion SAO project by the same BFB team (hexum064) for the DC31 badge slot -- a separate item, noted here for context, not folded into this entry.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker team, event/year, features, MCU, unit count) come from the maker''s own Hackaday.io project log, so reasonably solid, but the log does not give an LED count/type, a display spec beyond "no screen on the actual badge," a price, or links to hardware/firmware source files, so those fields are left empty rather than guessed. No separate GitHub repo was found for this specific badge (searches only surfaced the Hackaday project itself and unrelated DEF CON badge repos). Availability marked unknown/general release since it was a free conference badge, not sold, but no explicit "free" distribution tag was stated by the maker for this specific board (the companion SAO asked for a $10 donation, which is a different item).'
last_modified_date: '2026-09-07'
---

The DC31 Plumbus BFB is an independently-made electronic conference badge built for DEF CON 31 (2023) by the BFB team -- hexum064, pinguino, and Erin -- as a successor to their earlier "Big Fucking Badge" line. The team's stated goal for this generation was to make something less complex, less heavy, less battery-hungry, and less expensive than their prior badges, while keeping the series' irreverent character. The board uses a Microchip xMega microcontroller (the team worked with both xmega32e5 and xmega16e5 variants during development) and was fabricated through AllPCB; 99 working units were produced, plus one that came out bad.

Functionally, the badge relies on four tactile dome-switch buttons and hall-effect sensors as its inputs, driving interactive game modes and a puzzle that hides a prize/easter egg for players who solve it, alongside programmable LED lighting patterns. Despite an OLED display being used on a development/test rig, the team notes the shipped badge itself has no screen. The badge carries an SAO connector, and the same team separately built and sold a companion "DC31 SAO" (a Nyan-cat RGB display with a Simon-style memory game) meant to plug into DC31-style badge slots, including this one -- that SAO is a distinct project and is not part of this entry.

No public hardware or firmware repository was located for this specific badge during research, and the maker's project log does not give an LED count/type or a price, so those fields are left blank rather than guessed. The badge was distributed to attendees at DEF CON 31 rather than sold commercially.
