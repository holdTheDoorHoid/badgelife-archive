---
title: Dumb Badge
id: other-dumb-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: unknown
event: other
year: 0
makers:
- name: bbenchoff
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
- label: github.com/bbenchoff/Dumb-Badge
  url: https://github.com/bbenchoff/Dumb-Badge
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: not_an_item
sources:
- kind: url
  url: https://github.com/bbenchoff/Dumb-Badge
  title: Dumb Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/bbenchoff/Dumb-Badge/master/README.md
  title: 'VT-69 Portable Terminal (README)'
  accessed: '2026-09-07'
  note: 'The repo README identifies the project as the "VT-69 Portable Terminal," a standalone battery-powered dumb terminal (ATSAMD51, 4" 800x480 LCD, 69-key silicone keyboard, RS-232/USB-C serial). No badge, SAO, or conference is mentioned anywhere in the README or the linked documentation index.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    This repo is not a hacker-conference badge or SAO. The README describes the "VT-69 Portable
    Terminal": a portable, battery-powered dumb terminal (VT-100/VT-220/Wyse-style) built around an
    ATSAMD51 MCU, a 4" 800x480 LCD limited to 80x24 text, a custom 69-key silicone membrane keyboard,
    RS-232 and USB-C serial, and an internal LiPo battery. It functions as a standalone shell terminal
    or text-adventure console, not as a wearable badge or an SAO that plugs into one. No conference,
    year, price, or distribution/availability information is given anywhere in the repo; the images
    referenced by the README actually live in a separate/renamed repo, github.com/ViolenceWorks/VT-69,
    which mirrors the same content and documentation with no added event context either. Leaving this
    entry marked not_an_item rather than filling in badge-shaped fields, since nothing here supports
    treating it as a badge/SAO record.
last_modified_date: '2026-09-07'
---

The GitHub repository "Dumb-Badge" by bbenchoff is actually the project page for the VT-69, a portable, battery-powered dumb terminal in the style of a VT-100, VT-220, or Wyse WY-50. It is a standalone electronics build, not a conference badge or SAO: a 4" 800x480 LCD limited to text-only 80x24 output, a custom 69-key silicone membrane keyboard, an ATSAMD51 microcontroller, RS-232 and USB-C serial connectivity, and an internal LiPo battery good for more than 12 hours. The project is fully documented in the repo (electronics, firmware, mechanical, and keyboard design files) but the README and its documentation index make no mention of any hacker conference, badge event, or SAO header.

Because this page describes a general hobby terminal project rather than a specific badge or SAO made for a con, it does not belong in the archive as a badge/SAO record.
