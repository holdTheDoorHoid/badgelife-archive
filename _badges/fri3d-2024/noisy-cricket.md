---
title: Noisy Cricket
id: fri3d-2024-noisy-cricket
layout: badge
parent: Fri3D 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: fri3d-2024
year: 2024
makers:
- name: Fri3d Camp
summary: 'A simple noise-making soldering-practice add-on for the Fri3d Camp 2024 badge, built around a single NPN transistor astable circuit that drives a buzzer-like tone through the badge''s pin header.'
functions: 'Produces a buzzing/noise tone using a discrete transistor oscillator circuit; doubles as a beginner soldering exercise with an LED indicator.'
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Distributed as a soldering-workshop kit at Fri3d Camp 2024, assembled onto the main Fri3d 2024 badge via its pin header.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: fri3dcamp.github.io/badge_2024/en/noisycricket
  url: https://fri3dcamp.github.io/badge_2024/en/noisycricket/
  kind: website
images:
  - file: assets/images/badges/fri3d-2024/noisy-cricket/9810ddb9a9.jpg
    source: "https://fri3dcamp.github.io/badge_2024/en/noisycricket/"
    credit: "Fri3d Camp"
    caption: "Assembled Noisy Cricket board"
  - file: assets/images/badges/fri3d-2024/noisy-cricket/9ae3af5238.jpg
    source: "https://fri3dcamp.github.io/badge_2024/en/noisycricket/"
    credit: "Fri3d Camp"
    caption: "Noisy Cricket mounted on the Fri3d Camp 2024 badge"
contact: {}
notes:
- Sound/buzzer add-on board for the Fri3d Camp 2024 badge with its own assembly/soldering guide. Found by the event-year sweep, task fri3d.
- 'Title matches the sweep''s wording exactly; the maker''s own docs also call it "Noisy Cricket."'
status: listed
sources:
- kind: url
  url: https://fri3dcamp.github.io/badge_2024/en/noisycricket/
  title: Noisy Cricket
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:fri3d); event read as ''fri3d-2024''.'
- kind: url
  url: https://fri3dcamp.github.io/badge_2024/en/noisycricket/
  title: Noisy Cricket - Fri3d Camp 2024 assembly guide
  accessed: '2026-09-08'
  note: 'Confirmed the item as a soldering-workshop add-on: a discrete-transistor noise oscillator (2N3904, two resistors, electrolytic capacitor, LED) that mounts to the badge via pin header; no pricing, quantity, or open-source file links given on the page.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed real via the maker''s own assembly-guide page, which is the only source found; a general web search turned up nothing beyond this page. Price, quantity made, and availability are not stated anywhere on the page, so those fields are left empty/unknown. No separate hardware/firmware repo was found (it is a simple discrete circuit, not likely to have a KiCad file published), so make_your_own is left null rather than guessed.'
last_modified_date: '2026-09-08'
---

The Noisy Cricket is a small soldering-practice add-on distributed at Fri3d Camp 2024, meant to be built and attached to that year's main Fri3d Camp badge. Rather than a microcontroller-based SAO, it is a discrete-component circuit: an NPN 2N3904 transistor, two resistors (33 Ω and 120 Ω), a 33 µF electrolytic capacitor, and an LED, wired as a simple oscillator that produces a buzzing tone. It connects to the host badge through a pin header, which can be soldered in either of two orientations so the finished board sits flat against the badge or points forward from it.

Fri3d Camp published a step-by-step assembly guide for it, complete with photos of each soldering stage and explicit polarity warnings for the capacitor and LED, framing it as a hands-on soldering exercise for camp attendees rather than a standalone electronic gadget. The guide also flags a minor documentation quirk: the transistor's actual placement on the board differs slightly from the printed silkscreen diagram.

No pricing, production quantity, or availability information is published, and no separate hardware or firmware repository was found, which is consistent with it being a fixed, non-programmable circuit rather than a code-driven badge.
