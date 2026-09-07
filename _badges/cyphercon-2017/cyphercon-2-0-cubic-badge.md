---
title: Cyphercon 2.0 Cubic Badge
id: cyphercon-2017-cyphercon-2-0-cubic-badge
layout: badge
parent: Cyphercon 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2017
year: 2017
makers:
- name: Tymkrs
summary: 'A cube-shaped conference badge with cutout faces exposing its LEDs, microprocessors, and internal bus, built around a puzzle where attendees reassemble a fictional relay computer.'
functions: 'A text-adventure game whose goal is to reassemble a relay-based computer using parts scrounged from a missile silo; solving it unlocks an emulator for a vintage time-sharing OS that lets the badge write and deploy code to other badges over a mesh network. The USB port also charges the battery and exposes a CDC serial connection for terminal access to the game.'
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - retro computer
  - hardware tool
tech:
  mcu: PIC + Parallax Propeller
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'over 400'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2017/04/09/the-cubic-cyphercon-badge
  url: https://hackaday.com/2017/04/09/the-cubic-cyphercon-badge/
  kind: article
  archived: https://web.archive.org/web/20260418165945/https://hackaday.com/2017/04/09/the-cubic-cyphercon-badge/
images:
- file: assets/images/badges/cyphercon-2017/cyphercon-2-0-cubic-badge/33c6a4e659.jpg
  source: "https://hackaday.com/2017/04/09/the-cubic-cyphercon-badge/"
  credit: "Tymkrs / Hackaday"
  caption: "The Cyphercon 2.0 cubic badge with cutout faces exposing LEDs and internal electronics"
contact: {}
notes:
- Cube-shaped badge with cutouts exposing LEDs/microprocessor/bus and a single USB port; hand-soldered, ~400 units; runs a text-adventure game.
status: released
sources:
- kind: url
  url: https://hackaday.com/2017/04/09/the-cubic-cyphercon-badge/
  title: Cyphercon 2.0 Cubic Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: bsides-regional (US regional hacker cons: BSides variants, ShmooCon, Thotcon, CypherCon, DerbyCon, CarolinaCon, GrrCON, ToorCon, HOPE, CactusCon, WWHF, Circle City Con, Layer8, Blue Team Con, ShellCon, NorthSec, Hackfest)); event read as ''CypherCon (Milwaukee, 2017)''.'
  archived: https://web.archive.org/web/20260418165945/https://hackaday.com/2017/04/09/the-cubic-cyphercon-badge/
- kind: url
  url: https://hackaday.com/2017/04/09/the-cubic-cyphercon-badge/
  title: The Cubic Cyphercon Badge
  accessed: '2026-09-07'
  note: 'Confirmed maker (Tymkrs), event (Cyphercon 2017, Milwaukee), chips (PIC + Propeller), function (text-adventure/relay-computer puzzle leading to a time-sharing OS emulator and mesh code deployment), USB role (charging + CDC serial), and quantity built (400+). Article notes Propeller code is unprotected but PIC firmware is available on request, so hardware/firmware openness is only partial and no repo link was given.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found was the original Hackaday writeup; no Tymkrs storefront, project page, or GitHub repo for this specific badge was located (Tymkrs'' own site has no mention of it). Price, exact LED count/type, display, battery spec, and availability could not be confirmed and are left empty.'
last_modified_date: '2026-09-07'
---

The Cyphercon 2.0 Cubic Badge was built by the Tymkrs maker collective for Cyphercon 2017 in Milwaukee. Rather than a flat PCB, it takes the form of a cube with cutout faces that expose the LEDs, microprocessors, and bus wiring inside, so the electronics themselves are part of the badge's look. Tymkrs hand-built more than 400 of them for the event.

Functionally, the badge runs a text-adventure game built around a PIC microcontroller and a Parallax Propeller chip: the story frames the puzzle as reassembling a relay-based computer from parts scavenged around a missile silo. Completing it unlocks an emulator for a vintage time-sharing operating system, letting a badge write and push code out to other badges over a mesh network. A single USB port does double duty, recharging the badge's battery and exposing a CDC serial connection so attendees can reach the game through a terminal emulator.

The Hackaday writeup notes that the Propeller side's code was left unprotected, while the PIC firmware was kept protected but available from Tymkrs on request — making the badge only partially open. No dedicated project page, repo, or storefront for this badge could be found beyond that article, so pricing, exact LED specs, and post-event availability remain unknown.
