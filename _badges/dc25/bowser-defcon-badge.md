---
title: bowser-defcon-badge
id: dc25-bowser-defcon-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: reverse0x90
summary: A DIY DEF CON badge built on a Cypress PSoC 4 prototyping kit, with morse-code and binary message modes plus a built-in party (LED) mode.
functions: 'Three switchable modes: Morse Message Mode (left toggle), Binary Message Mode (right toggle), and Party Mode (toggled via the on-board CY8CKIT-049-42XX switch).'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: PSoC 4 (Cypress CY8CKIT-049-42XX)
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/reverse0x90/bowser-defcon-badge
  eda_tool: null
links:
- label: github.com/reverse0x90/bowser-defcon-badge
  url: https://github.com/reverse0x90/bowser-defcon-badge
  kind: repo
images: []
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/reverse0x90/bowser-defcon-badge
  title: bowser-defcon-badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/reverse0x90/bowser-defcon-badge/master/README.md
  title: 'reverse0x90/bowser-defcon-badge: README'
  accessed: '2026-09-07'
  note: 'README text confirming the three operating modes and that the project runs on the CY8CKIT-049-42XX board.'
- kind: url
  url: https://api.github.com/repos/reverse0x90/bowser-defcon-badge
  title: 'GitHub API: repo metadata for reverse0x90/bowser-defcon-badge'
  accessed: '2026-09-07'
  note: 'Repo has no description, no topics, no license field, and no images; created and pushed 2017-07-21, four commits total.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    The repo (PSoC Creator project files under a "Defcon_Badge" folder) contains only source/build
    files and a short README; it never states which DEF CON or year it targets. The repo was
    created and last pushed on 2017-07-21, six days before DEF CON 25 (July 27-30, 2017), and the
    project/repo name references "Defcon Badge," so event/year here (dc25 / 2017) is inferred from
    that timing rather than stated outright by the maker -- flagging as low confidence. No maker
    bio, storefront, images, price, quantity, or distribution details were found anywhere; this may
    have been a one-off personal build rather than a badge distributed to others. The MCU is a
    Cypress PSoC 4 development kit (CY8CKIT-049-42XX), which is an off-the-shelf prototyping board,
    not a custom PCB -- no hardware/PCB files are in the repo, only firmware, hence
    make_your_own.open_source is "partial" (firmware only). No image of the physical item was found.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/bowser-defcon-badge/
---

This is a DIY DEF CON badge built by GitHub user reverse0x90 around a Cypress CY8CKIT-049-42XX PSoC 4 prototyping kit rather than a custom-fabricated PCB. According to the project's README, the badge runs in three switchable modes: a Morse Message Mode and a Binary Message Mode, each triggered by an onboard toggle, plus a Party Mode activated through the prototyping board's own switch (presumably a blinking-LED show mode).

The GitHub repository, named "bowser-defcon-badge," holds only PSoC Creator firmware/build files for the badge and gives no further detail about its physical form, whether "Bowser" refers to a Super Mario Bros. theme or something else, how many were made, or how it was distributed. The repository was created and pushed on July 21, 2017, six days before DEF CON 25 began, which is the basis for dating it to that event; the maker's own pages do not state this directly. No photos of the finished badge, pricing, or quantity information could be located.

## Make your own

Firmware source for the PSoC 4 project is published at the repo above under the `Defcon_Badge` folder (a PSoC Creator `.cydsn` project). No PCB design files, bill of materials, or license were found, so treat it as firmware-only unless further files turn up.
