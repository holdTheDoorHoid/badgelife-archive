---
title: malo-sao-flasher — Web-based reflashing/animation browser for MalO SAO
id: other-malo-sao-flasher-web-based-reflashing-animation-browser-for
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 0
makers:
- name: BenHaddley
summary: 'A browser-based companion tool for the MalO SAO badge (DEF CON 34): reflashes the badge and browses its animations entirely from a static web page, no install required.'
functions: 'Reflash Wizard automates the MalO SAO factory-reset/reflash procedure using the File System Access API (desktop Chrome/Edge only); an Animation Browser decodes and plays the badge''s .cmp/.dur/.ord animation files in-browser; a manual fallback gives OS-specific command-line instructions for browsers without File System Access support.'
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
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
links:
- label: github.com/BenHaddley/malo-sao-flasher
  url: https://github.com/BenHaddley/malo-sao-flasher
  kind: repo
- label: github.com/parallellogic-/MalO_SAO
  url: https://github.com/parallellogic-/MalO_SAO
  kind: repo
images: []
contact: {}
notes:
- software companion, not the hardware itself
- 'This entry is a browser tool for the MalO SAO badge, which already has its own archive entry (dc34-malo-sao / dc34-malo). This tool is not itself a badge or SAO.'
status: not_an_item
sources:
- kind: url
  url: https://github.com/BenHaddley/malo-sao-flasher
  title: malo-sao-flasher — Web-based reflashing/animation browser for MalO SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/BenHaddley/malo-sao-flasher
  title: malo-sao-flasher README
  accessed: '2026-09-07'
  note: 'Confirmed the tool is a static, browser-based reflash/animation-browser for the MalO SAO badge; no build step or install required; requires desktop Chrome/Edge for the File System Access API used by the reflash wizard.'
- kind: url
  url: https://github.com/parallellogic-/MalO_SAO
  title: parallellogic-/MalO_SAO
  accessed: '2026-09-07'
  note: 'MalO SAO is the SCP-1471-themed SAO distributed at DEF CON 34 (Badgelife Village), designed by ParallelLogic (RP2350B, 1.5" 128x128 OLED, 6-pin SAO). This flasher tool exists solely to support that badge; the badge itself already has an archive entry.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This is a software tool (a static web page for reflashing and animation-browsing), not a badge or SAO in its own right, so it is marked not_an_item rather than filled in as hardware. The hardware it supports, MalO SAO by ParallelLogic (DEF CON 34, Badgelife Village), already has its own entries in the archive (dc34-malo-sao, dc34-malo) — see existing_titles.txt. No maker bio, event, or hardware specs apply to this repo itself beyond what is noted here. event/year left as-is per instructions for not_an_item pages; if this tool should carry the dc34 event tag for cross-reference purposes, that is a judgment call for a maintainer.'
last_modified_date: '2026-09-07'
---

**malo-sao-flasher** is a small, no-build, static web page written by BenHaddley that serves as a browser-based companion utility for the **MalO SAO**, the SCP-1471-themed shitty add-on distributed by ParallelLogic at DEF CON 34's Badgelife Village. Rather than being a badge or SAO itself, it is a tool: point a desktop Chrome or Edge browser at the page, and its "Reflash Wizard" walks through the MalO SAO's factory-reset and reflash procedure using the browser's File System Access API, with no downloads or installed software required. A separate "Animation Browser" mode decodes the badge's `.cmp`/`.dur`/`.ord` animation file formats in JavaScript so people can preview and page through the badge's built-in animations directly in the browser. For browsers that lack File System Access support, the page falls back to printing out the equivalent OS-specific command-line instructions.

Because this repository is a software utility rather than hardware, it does not carry its own maker credit, event drop, or physical specs in the way a badge entry does — those live on the MalO SAO hardware entry itself (ParallelLogic's RP2350B-based board with a 1.5" 128×128 grayscale OLED and a 6-pin SAO connector), which is already present elsewhere in this archive. This entry is kept as a record of the companion tool and cross-linked to that hardware project.
