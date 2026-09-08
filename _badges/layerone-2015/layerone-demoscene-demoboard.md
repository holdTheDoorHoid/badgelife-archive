---
title: LayerOne Demoscene Board
id: layerone-2015-layerone-demoscene-demoboard
layout: badge
parent: LayerOne 2015
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: layerone-2015
year: 2015
makers:
- name: arko
  url: https://hackaday.io/arko
summary: A PIC24F-based demoscene coding platform built for the LayerOne demo party, with VGA video out and 8-bit audio out for writing size- and resource-constrained graphics/music demos.
functions: Runs user-written demoscene code (graphics and music demos) under tight memory/flash constraints; outputs video over VGA and audio over a 3.5mm jack; programmed and powered over USB.
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: PIC24FJ256DA206
  leds: null
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold via the Hackaday Store and Tindie around the board's 2015 introduction; a Hackaday article from that year says it could no longer be bought.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/arkorobotics/L1DemosceneBoard
  firmware_url: https://github.com/arkorobotics/L1DemosceneBoard
  eda_tool: null
links:
- label: hackaday.com/2015/05/26/layerone-demoscene
  url: https://hackaday.com/2015/05/26/layerone-demoscene/
  kind: article
- label: hackaday.com/2015/03/05/revive-the-demoscene-with-a-layerone-demoscene-board
  url: https://hackaday.com/2015/03/05/revive-the-demoscene-with-a-layerone-demoscene-board/
  kind: article
- label: Layerone Demoscene Board (Hackaday.io project)
  url: https://hackaday.io/project/3877-layerone-demoscene-board/
  kind: hackaday
- label: github.com/arkorobotics/L1DemosceneBoard
  url: https://github.com/arkorobotics/L1DemosceneBoard
  kind: repo
images:
- file: assets/images/badges/layerone-2015/layerone-demoscene-demoboard/c60a6237d2.jpg
  source: "https://hackaday.io/project/3877-layerone-demoscene-board/"
  credit: "arko"
  caption: "The LayerOne Demoscene Board"
contact: {}
notes:
- A PIC24F-based demoboard with VGA and 1/8" mono audio out, built for a LayerOne demoscene party. Found by the event-year sweep, task con-layerone.
- The community sheet listed the maker as "null space labs" (LayerOne's organizing hackerspace); the board itself was designed by "arko" (Arko Robotics), per the board's own Hackaday.io project page. Sheet also titled it "LayerOne Demoscene Demoboard"; the maker's own page calls it "Layerone Demoscene Board" (used here, minus the double "demo").
- Could not confirm exact price or quantity made.
status: released
sources:
- kind: url
  url: https://hackaday.com/2015/05/26/layerone-demoscene/
  title: LayerOne Demoscene Demoboard Party
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''LayerOne''.'
- kind: url
  url: https://hackaday.com/2015/03/05/revive-the-demoscene-with-a-layerone-demoscene-board/
  title: Revive The Demoscene With A LayerOne Demoscene Board
  accessed: '2026-09-08'
  note: Confirms PIC24F, three graphics acceleration units, color lookup tables, 16-bit VGA up to 640x480, 8-bit audio.
- kind: url
  url: https://hackaday.io/project/3877-layerone-demoscene-board/
  title: Layerone Demoscene Board (Hackaday.io project)
  accessed: '2026-09-08'
  note: Maker's own project page - designer "arko", exact MCU part PIC24FJ256DA206, 96K SRAM/256K flash, USB micro-AB power/programming, sold via Tindie/Hackaday Store; source of the board photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (designer, chip, event, I/O) confirmed via Hackaday coverage, the maker's own Hackaday.io project page, and the linked GitHub repo. Price and exact quantity made were not found in the sources checked, so those fields are left empty.
last_modified_date: '2026-09-08'
---

The LayerOne Demoscene Board is a small PIC24F-based coding platform designed by "arko" (Arko Robotics) for the LayerOne demo party, first introduced in early 2015. Built around a PIC24FJ256DA206 (16-bit core with an on-chip GFX accelerator, 96K SRAM, 256K flash), it outputs 16-bit VGA video up to 640x480 and 8-bit audio through a 3.5mm jack, and is programmed and powered over a USB Micro-AB connector.

The board was made for the LayerOne demoscene competition ("demoparty"), where entrants write graphics and music demos squeezed into the board's tight, fixed hardware resources — the point of the compo, in classic demoscene fashion, being to produce effects that look like they shouldn't be possible on such limited silicon. A May 2015 Hackaday writeup on the event's demo party covered a two-category competition, one restricted to this board specifically, with the winning entry (by the European team COINE) drawing comments about its unusually rich color and resolution for the hardware.

The board was sold for a time through the Hackaday Store and on Tindie; contemporary coverage from later in 2015 notes it had already sold out. The design is open source, with hardware and firmware published in arko's `L1DemosceneBoard` GitHub repository alongside the project's Hackaday.io writeup.
