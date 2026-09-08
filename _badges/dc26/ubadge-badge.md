---
title: uBadge (μBadge)
id: dc26-ubadge-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Joe Fitz (securelyfitz)
  url: https://github.com/securelyfitz
summary: A roughly 1cm-square Digispark/ATtiny85 board, stripped down to bare minimum, that plugs together with matching "arm" and "face" add-ons over an SAO-style header.
functions: Runs Arduino-compatible sketches via the Digispark/micronucleus USB bootloader; plug-together arms, faces, and add-ons (NeoPixel strips, I2C breakouts, orientation rotators) let several units be linked and powered together.
look:
  colors: []
  shape: null
  themes:
  - minimalist
  - hardware tool
tech:
  mcu: ATtiny85
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '~1100 assembled'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/securelyfitz/microbadge
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  kind: article
- label: github.com/securelyfitz/microbadge
  url: https://github.com/securelyfitz/microbadge
  kind: repo
images:
  - file: assets/images/badges/dc26/ubadge-badge/6faa6f202a.jpg
    source: "https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/"
    credit: "Hackaday"
    caption: "The uBadge, a Digispark/ATtiny85-based add-on"
  - file: assets/images/badges/dc26/ubadge-badge/a77589b691.jpg
    source: "https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/"
    credit: "Hackaday"
    caption: "Multiple uBadges linked via extended add-on header arms"
contact: {}
notes:
- Minimalist DC26 badge built on a Digispark/ATtiny85 board with a custom SAO add-on header. Found by the event-year sweep, task dc26-indie.
- 'This appears to be the same project as the archive''s dc26-ubadge-microbadge entry (same maker, same ATtiny85/Digispark description, same ~1100-unit DEF CON 26 build); see duplicate note in research.notes.'
status: listed
sources:
- kind: url
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  title: uBadge (μBadge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc26-indie); event read as ''dc26''.'
- kind: url
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  title: All The Badges Of DEF CON 26, Vol 1
  accessed: '2026-09-08'
  note: Confirms the uBadge is Joe Fitz's ATtiny85/Digispark micro badge, panelized in a 10x10 grid across 11 panels, meant to plug into extended add-on-header "arms"; no price, LED, or display info given.
- kind: url
  url: https://github.com/securelyfitz/microbadge
  title: securelyfitz/microbadge
  accessed: '2026-09-08'
  note: Maker's own repo for the same project (called "microbadge" / "µBadge" here) confirms ATtiny85 + micronucleus bootloader, SAO-compatible header, ~1100 units built for DEF CON 26 ("defcoin"), external 3.3V power (no onboard regulator), and a /hardware directory with design files; no explicit license found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Likely a duplicate of dc26-ubadge-microbadge (same maker, same ATtiny85/Digispark description, same ~1100-unit DEF CON 26 build, same GitHub repo). No pricing, LED, or display specs found in any source — this is a bare MCU add-on with no onboard display or addressable LEDs mentioned. No storefront or availability info found; treat availability as unknown. type set to sao rather than badge since it plugs into a host badge/other uBadges over an SAO-style header rather than being worn standalone with its own display.'
last_modified_date: '2026-09-08'
---

The uBadge (also called μBadge or microbadge) is Joe Fitz's (securelyfitz) minimalist add-on for DEF CON 26, built around a stripped-down Digispark/ATtiny85 board roughly a centimeter square. Fitz removed the USB-A connector and onboard voltage regulator from the standard Digispark design to shrink the footprint and cost, leaving a bare-minimum board that programs over micro-USB using the Arduino-compatible micronucleus bootloader and runs on external 3.3V power.

The real hook is the SAO-style add-on header: uBadges are meant to plug together with matching "arm," "face," and adapter pieces (including NeoPixel strips, I2C breakouts, and orientation rotators), letting several units link up and share power. Roughly 1,100 were assembled for DEF CON 26 — Hackaday describes them as panelized in a 10x10 grid, with 11 panels populated — and Fitz's own repo refers to the run as "defcoin."

Hardware design files live in Fitz's `securelyfitz/microbadge` GitHub repo under a `/hardware` directory, though no explicit open-source license was found there. No firmware repo, price, or storefront information turned up in the sources checked.

## Make your own

Hardware files (schematic/board) are published in the `/hardware` directory of the [microbadge GitHub repo](https://github.com/securelyfitz/microbadge); no separate firmware repo or BOM link was found.
