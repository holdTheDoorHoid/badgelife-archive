---
title: BSides-Badge25 (ch4r13, ESP32-C3)
id: bsides-2025-bsides-badge25-ch4r13-esp32-c3
layout: badge
parent: BSides 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-2025
year: 2025
makers:
- name: ch4r13
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
- label: github.com/ch4r13/BSides-Badge25
  url: https://github.com/ch4r13/BSides-Badge25
  kind: repo
  archived: https://web.archive.org/web/20260907104956/https://github.com/ch4r13/BSides-Badge25
images: []
contact: {}
notes: []
status: not_an_item
sources:
- kind: url
  url: https://github.com/ch4r13/BSides-Badge25
  title: BSides-Badge25 (ch4r13, ESP32-C3)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides 2025''.'
  archived: https://web.archive.org/web/20260907104956/https://github.com/ch4r13/BSides-Badge25
- kind: url
  url: https://api.github.com/repos/ch4r13/BSides-Badge25
  title: 'ch4r13/BSides-Badge25: repo metadata (GitHub API)'
  accessed: '2026-09-07'
  note: 'Confirms repo description "Memory dump from ESP32-C3" and full file listing.'
- kind: url
  url: https://api.github.com/repos/ch4r13/BSides-Badge25/contents
  title: 'ch4r13/BSides-Badge25: repository contents listing'
  accessed: '2026-09-07'
  note: 'Repo contains only esp32c3_dump_4mb.bin (a raw 4MB flash dump) and a binwalk_output/ directory of extraction results; no README, no hardware design files, no firmware source, no schematic or case for a specific badge.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This repo is not a badge/SAO project page. It is a reverse-engineering artifact: a raw flash memory dump (esp32c3_dump_4mb.bin) pulled from some ESP32-C3-based device, plus binwalk extraction output, with no README, no maker statement about a badge, no hardware files, and no firmware source. It does not describe, sell, or document a specific physical badge or SAO -- it is evidence of someone dumping a chip''s flash, not the item itself. Leaving all badge-specific fields empty per the never-invent rule.'
last_modified_date: '2026-09-07'
---

This entry was created from a GitHub repository, `ch4r13/BSides-Badge25`, that the archive's discovery sweep matched to badge-related topics. On inspection the repository is not a badge or SAO project: it holds a single 4MB raw flash dump (`esp32c3_dump_4mb.bin`) pulled from an ESP32-C3-based device, alongside a `binwalk_output/` folder of automated firmware-extraction results. There is no README, no description of a physical badge, no schematic, PCB, firmware source, or bill of materials, and no statement from `ch4r13` about designing, making, or distributing a badge.

The repo name and description ("Memory dump from ESP32-C3") suggest it is the record of someone dumping and analyzing the firmware of a BSides 2025 badge that already exists elsewhere, rather than the badge project itself. No corresponding badge project page, maker page, or storefront for a "BSides-Badge25" was found to link this dump back to. Because no source describes an actual physical item, this entry is marked `not_an_item` and no badge-specific fields are filled in.
