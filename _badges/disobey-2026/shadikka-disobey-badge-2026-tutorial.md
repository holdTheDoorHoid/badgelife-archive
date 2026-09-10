---
title: shadikka/disobey-badge-2026-tutorial
id: disobey-2026-shadikka-disobey-badge-2026-tutorial
layout: badge
parent: Disobey 2026
grand_parent: Badge Archive
nav_exclude: true
type: other
event: disobey-2026
year: 2026
makers:
- name: shadikka
summary: ''
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
- label: github.com/shadikka/disobey-badge-2026-tutorial
  url: https://github.com/shadikka/disobey-badge-2026-tutorial
  kind: website
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
status: not_an_item
sources:
- kind: url
  url: https://github.com/shadikka/disobey-badge-2026-tutorial
  title: shadikka/disobey-badge-2026-tutorial
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/shadikka/disobey-badge-2026-tutorial
  title: 'GitHub README: disobey-badge-2026-tutorial'
  accessed: '2026-09-10'
  note: Confirms this is an embedded-Rust programming tutorial for the official Disobey 2026 badge, not a separate badge/SAO product. Author is Anssi Matti Helin (GitHub user shadikka).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Not a distinct badge/SAO. This repo is a step-by-step tutorial (embedded Rust, using the Embassy framework, targeting the ESP32-S3) teaching Disobey 2026 attendees how to write and flash their own firmware onto the official conference badge. The badge itself is already catalogued as disobey-2026-disobey-2025-2026-badge. Author: Anssi Matti Helin. Repo license: MIT for code, CC-BY-NC-SA 4.0 for tutorial text.'
last_modified_date: '2026-09-10'
---

This repository is not a badge or SAO in its own right. It is a tutorial, written by Anssi Matti Helin (GitHub user shadikka) for Disobey 2026, that teaches attendees embedded Rust programming so they can write and flash their own firmware onto the conference's official ESP32-S3 badge, already catalogued separately as the Disobey 2026 badge.

The tutorial walks through progressively more capable firmware examples, starting from "hello world," using the Rust Embassy async framework, and covers toolchain setup (rustup, espup, espflash) needed to build and flash the badge. Its stated goal is to let attendees "run anything you want on" the hardware they paid for. Source code is MIT-licensed; the tutorial text itself is CC-BY-NC-SA 4.0.

