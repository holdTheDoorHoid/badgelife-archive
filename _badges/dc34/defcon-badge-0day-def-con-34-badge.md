---
title: defcon-badge-0day — DEF CON 34 badge
id: dc34-defcon-badge-0day-def-con-34-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Trinity-SYT-SECURITY
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
- label: github.com/Trinity-SYT-SECURITY/defcon-badge-0day
  url: https://github.com/Trinity-SYT-SECURITY/defcon-badge-0day
  kind: repo
images: []
contact: {}
notes:
- 'Not a badge or SAO design: this repo is a security-research writeup and PoC tooling for a USB input-flood vulnerability the author found in the official DEF CON 34 conference badge (Baochip-1x SoC running Xous OS, OLED display, physical buttons, USB). No badge design, PCB, or SAO of the author''s own is included.'
status: unknown
sources:
- kind: url
  url: https://github.com/Trinity-SYT-SECURITY/defcon-badge-0day
  title: defcon-badge-0day — DEF CON 34 badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 34''.'
- kind: url
  url: https://github.com/Trinity-SYT-SECURITY/defcon-badge-0day
  title: 'GitHub repo README — vulnerability disclosure'
  accessed: '2026-09-07'
  note: 'Confirms this is a security-research repo (MIT licensed) documenting an unauthenticated USB peer that can freeze the official DEF CON 34 badge (display, buttons, console) until power is removed; not itself a badge/SAO product. No LED, price, quantity, or image details given.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This is not a badge/SAO entry. The repository by Trinity-SYT-SECURITY is a security-research writeup and proof-of-concept for a USB input-flood denial-of-service vulnerability in the official DEF CON 34 conference badge (Baochip-1x SoC, Xous OS). It contains no original badge hardware, PCB design, or SAO of the maker''s own — only tooling to reproduce the bug and documentation for responsible disclosure. The official DEF CON 34 badge itself does not yet have its own archive entry; if one is created, it should credit the DEF CON badge team, not Trinity-SYT-SECURITY, as the badge maker.'
last_modified_date: '2026-09-07'
---

This entry was created by an automated sweep that mistook a security-research repository for a badge project. **Trinity-SYT-SECURITY/defcon-badge-0day** is not a badge or SAO design; it is a writeup and proof-of-concept tool documenting a denial-of-service vulnerability the researcher found in the official DEF CON 34 conference badge. The bug: an unauthenticated USB peer can flood console input fast enough to freeze the badge's display, physical buttons, and console until power is removed. The official badge itself runs a Baochip-1x SoC under Xous OS with an OLED display, physical buttons, and USB connectivity — hardware built by the DEF CON badge team, not by Trinity-SYT-SECURITY.

No LED count, price, production quantity, availability, or image URLs are given in the repository, since none of that applies to a vulnerability report. The repo is MIT licensed and framed around responsible disclosure rather than product distribution.
