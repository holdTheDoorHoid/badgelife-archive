---
title: dc29-badge-stuff (custom music mod for the DC29 badge)
id: dc29-badge-stuff-custom-music-mod-for-the-dc29-badge
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc29
year: 2021
makers:
- name: duk-37
  url: https://github.com/duk-37
summary: 'A GitHub repo of hex-editing instructions and sample code for replacing the music/sound routine on the official DEF CON 29 badge firmware.'
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/duk-37/dc29-badge-stuff
  eda_tool: null
links:
- label: github.com/duk-37/dc29-badge-stuff
  url: https://github.com/duk-37/dc29-badge-stuff
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: not_an_item
sources:
- kind: url
  url: https://github.com/duk-37/dc29-badge-stuff
  title: dc29-badge-stuff (custom music mod for the DC29 badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc29''.'
- kind: url
  url: https://github.com/duk-37/dc29-badge-stuff
  title: "duk-37/dc29-badge-stuff: Do funny things with your DEF CON 29 badge."
  accessed: '2026-09-07'
  note: 'Read via GitHub API/README. Confirmed the GitHub username is "duk-37" (the sheet''s link label had a typo, "duck-37"); confirmed the repo is a hex-editing tutorial for swapping the sound routine on the stock DC29 badge firmware, not a distinct badge/SAO design.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    Not an item for the archive. The repo (github.com/duk-37/dc29-badge-stuff,
    GitHub description "Do funny things with your DEF CON 29 badge") is a set
    of instructions plus sample C code for dumping the DC29 badge's stock UF2
    firmware, compiling a replacement music/sound routine with a bare-metal
    ARMv6 clang toolchain, and hex-patching the compiled bytes into the
    firmware image at a fixed file offset before reflashing. It documents
    modifying the official DEF CON 29 electronic badge (a separate archive
    entry, not this one) rather than describing standalone badge/SAO hardware.
    Also corrected the maker's GitHub username from "duck-37" (a typo carried
    over from the source sheet's link label) to "duk-37".
last_modified_date: '2026-09-07'
---

A small GitHub repo, [dc29-badge-stuff](https://github.com/duk-37/dc29-badge-stuff) by GitHub user duk-37, walks through modifying the sound/music behavior of the official DEF CON 29 electronic badge. It is not a badge or SAO in its own right: it is a firmware how-to, covering how to pull the badge's stock UF2 firmware image over USB (by holding the bottom-right button while plugging in), compile a replacement "music" routine written in C with a bare-metal ARMv6 clang toolchain, and hex-patch the compiled bytes into the firmware image at a fixed file offset before reflashing.

Because the repo documents a software mod for the stock DC29 badge rather than a distinct piece of hardware, this entry is marked `not_an_item`. Any hardware details belong on the archive's entry for the official DEF CON 29 badge itself, not here.
