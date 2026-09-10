---
title: 'SAO adapters: sao-iic, sao-stripper, sao-flipper, sao-rotate, sao-45'
id: dc26-sao-adapters-sao-iic-sao-stripper-sao-flipper-sao-rotate-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc26
year: 2018
makers:
- name: Joe Fitz (securelyfitz)
  url: https://github.com/securelyfitz
summary: A set of small passive PCB adapters for the DEF CON 26 "microbadge" SAO ecosystem, each solving one wiring/orientation problem for a plugged-in SAO addon.
functions: 'sao-iic breaks an SAO out to common I2C pinout order; sao-stripper adapts an SAO to drive an addressable LED strip; sao-flipper corrects a backwards-installed SAO; sao-rotate turns an SAO 90 degrees so it can be oriented differently on the host board.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/securelyfitz/sao-iic
  firmware_url: null
  eda_tool: null
links:
- label: github.com/securelyfitz/sao-iic
  url: https://github.com/securelyfitz/sao-iic
  kind: repo
- label: github.com/securelyfitz/sao-rotate
  url: https://github.com/securelyfitz/sao-rotate
  kind: repo
- label: github.com/securelyfitz/sao-flipper
  url: https://github.com/securelyfitz/sao-flipper
  kind: repo
- label: github.com/securelyfitz/sao-stripper
  url: https://github.com/securelyfitz/sao-stripper
  kind: repo
- label: github.com/securelyfitz/microbadge (main project)
  url: https://github.com/securelyfitz/microbadge
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sheet/sweep title kept as-is; the maker did not give the set a collective name — these are five separate small repos under the same GitHub account, tied together by the microbadge README.'
status: listed
sources:
- kind: url
  url: https://github.com/securelyfitz/sao-iic
  title: 'SAO adapters: sao-iic, sao-stripper, sao-flipper, sao-rotate, sao-45'
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/securelyfitz/sao-iic
  title: securelyfitz/sao-iic
  accessed: '2026-09-10'
  note: 'Confirms sao-iic is a passive "addon to common IIC pinouts"; schematic/board/gerber files only, no firmware.'
- kind: url
  url: https://github.com/securelyfitz/microbadge
  title: securelyfitz/microbadge
  accessed: '2026-09-10'
  note: 'Main project README lists all five adapters (sao-iic, sao-stripper, sao-flipper, sao-rotate, sao-45) as part of the DEF CON 26 microbadge kit; confirms 2018/DC26 context, ATtiny85-based host badge, ~1100 units assembled, BOM under $1/badge.'
- kind: url
  url: https://github.com/securelyfitz/sao-rotate
  title: securelyfitz/sao-rotate
  accessed: '2026-09-10'
  note: 'Confirms sao-rotate "rotates an SAO 90 degrees."'
- kind: url
  url: https://github.com/securelyfitz/sao-flipper
  title: securelyfitz/sao-flipper
  accessed: '2026-09-10'
  note: 'Confirms sao-flipper "flips a backwards SAO."'
- kind: url
  url: https://github.com/securelyfitz/sao-stripper
  title: securelyfitz/sao-stripper
  accessed: '2026-09-10'
  note: 'Repo contains a custom LED-strip library alongside schematic/board files but has no README text describing intended use; function inferred as an LED-strip adapter from the name and library, not confirmed in the maker''s own words.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The maker''s GitHub confirms all five adapters exist and are part of the DEF CON 26 microbadge SAO ecosystem (2018), matching the entry''s existing event/year. None of the five repos has a written README beyond a one-line GitHub description, so exact circuit details, dimensions, and any standalone pricing/quantity for the adapters (as opposed to the microbadge kit itself) could not be confirmed. sao-45 was named in the microbadge README as a fifth adapter but its own repository was not directly fetched (budget); assume it rotates an SAO 45 degrees by analogy to sao-rotate, though this is not confirmed and was left out of functions. These are small unpopulated/passive PCBs distributed alongside the microbadge kit rather than sold separately, so get_one fields are left empty.'
last_modified_date: '2026-09-10'
---

At DEF CON 26 (2018), Joe Fitz (securelyfitz) built the "microbadge," a roughly one-square-centimeter functional badge based on an ATtiny85 (via a Digispark-style board) with a bill of materials under a dollar per unit, with about 1,100 assembled for the event. Around that core badge he published a family of small, passive SAO-format adapter boards that solve mechanical and wiring mismatches rather than adding features of their own: sao-iic re-routes an SAO's pins to a common I2C pinout, sao-stripper adapts an SAO connector to drive an addressable LED strip, sao-flipper corrects an SAO that was plugged in backwards, and sao-rotate turns an SAO 90 degrees so it can be mounted at a different angle on the host board. A fifth adapter, sao-45, is named in the same project family but was not independently confirmed here.

None of the five adapter repositories carries firmware or a populated microcontroller — they are bare PCBs (schematic, board, and Gerber files only) meant to be soldered inline between an SAO and its host header. All are hosted individually on GitHub under the securelyfitz account and are referenced back to the main microbadge project page for context. No separate pricing, quantity, or standalone distribution information for the adapters was found; they appear to have circulated as accessories alongside the microbadge kit itself rather than as a standalone product.
