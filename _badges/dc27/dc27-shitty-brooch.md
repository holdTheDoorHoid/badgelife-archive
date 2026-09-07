---
title: Shitty Brooch
id: dc27-dc27-shitty-brooch
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc27
year: 2019
makers:
- name: AND!XOR
  url: https://github.com/ANDnXOR
summary: A lapel-pin brooch with a CR2032 holder and 2x3 female header that powers an SAO without a badge, published by AND!XOR for DEF CON 27 with schematic and Gerbers.
functions: Powers a Shitty Add-On (SAO) directly, letting someone wear an SAO on a lapel with no host badge required.
look:
  colors: []
  shape: null
  themes:
  - pin
  - jewelry
  - wearable
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: CR2032
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/zapp1337/sao-reference-designs/tree/master/DC27/Shitty-Brooch
  firmware_url: null
  eda_tool: null
links:
- label: github.com/ANDnXOR/sao-reference-designs/tree/master
  url: https://github.com/ANDnXOR/sao-reference-designs/tree/master
  kind: repo
- label: github.com/zapp1337/sao-reference-designs/tree/master/DC27/Shitty-Brooch
  url: https://github.com/zapp1337/sao-reference-designs/tree/master/DC27/Shitty-Brooch
  kind: repo
- label: 'Hackaday Links: April 7, 2019'
  url: https://hackaday.com/2019/04/07/hackaday-links-april-7-2019/
  kind: article
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/ANDnXOR/sao-reference-designs/tree/master
  title: AND!XOR SAO Reference Designs
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/zapp1337/sao-reference-designs/tree/master/DC27/Shitty-Brooch
  title: 'zapp1337/sao-reference-designs: DC27/Shitty-Brooch'
  accessed: '2026-09-07'
  note: 'Design-file directory: BOM (CR2032 in a Keystone 3034 holder, 2x3 female header, blank lapel pin with rubber backs), schematic PNG, and full Gerber/drill set for fabrication. zapp1337 is "Zapp" of AND!XOR (per their Hackaday.io profile), so this fork is the maker''s own copy of the design.'
- kind: url
  url: https://hackaday.com/2019/04/07/hackaday-links-april-7-2019/
  title: 'Hackaday Links: April 7, 2019'
  accessed: '2026-09-07'
  note: Confirms AND!XOR released the Shitty Brooch, which "powers all Shitty Add-Ons with a CR2032 battery," with files posted to GitHub. No price/quantity given.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No maker's-own product photo of the assembled brooch was found (the repo has only a schematic PNG and Gerber files, no rendered image), so no images could be saved. Price, quantity made, and distribution method (free giveaway vs. sold) are not stated anywhere found. tech.leds and tech.display left null since it is a passive power carrier with no chip of its own.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc27/dc27-shitty-brooch.glb
  method: gerber
  source_file: DC27/Shitty-Brooch
  generated: '2026-09-07'
  bytes: 74540
  size_mm:
  - 25.0
  - 43.5
---

The Shitty Brooch is a small accessory board released by AND!XOR for DEF CON 27 (2019) that lets someone wear a Shitty Add-On (SAO) without needing a host badge at all. It holds a CR2032 coin cell in a Keystone 3034 holder and breaks out a standard 2x3 female SAO header, with a blank lapel pin and rubber pin-backs completing the wearable form factor.

The design was published as open hardware in AND!XOR's `sao-reference-designs` GitHub repo, under a `DC27/Shitty-Brooch` folder maintained by "Zapp," one of the AND!XOR team members. It includes a schematic image and a complete set of Gerber and drill files, so anyone could fabricate their own copy. Hackaday's links roundup from April 2019 confirmed the release and noted the files were up on GitHub, but no source found states a price, production quantity, or exactly how it was distributed (sold, given away, or both).
