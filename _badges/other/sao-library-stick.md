---
title: library stick
id: other-sao-library-stick
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 0
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A stick-shaped PCB carrying a row of SAO headers, made by davedarko to display and show off a collection of simple add-ons (SAOs) rather than to be worn itself.
functions: 'Holds a row of SAOs plugged into its headers so a collection can be displayed and lit up together; no MCU or logic of its own.'
look:
  colors: [black]
  shape: rectangle
  themes: [hardware tool]
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SAO%20library%20stick
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/SAO%20library%20stick
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SAO%20library%20stick
  kind: repo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/SAO%20library%20stick%20short
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SAO%20library%20stick%20short
  kind: repo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/SAO_stick_sideways
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SAO_stick_sideways
  kind: repo
images:
  - file: assets/images/badges/other/sao-library-stick/35c72c63a2.jpg
    source: "https://github.com/davedarko/Simple-Add-ons-SAO"
    credit: "davedarko"
    caption: "Several library stick boards, each loaded with a row of SAOs, mounted on a wooden display frame at Hackspace Xhain"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/README.md
  title: Simple-Add-ons-SAO README
  accessed: '2026-09-07'
  note: "Repo README lists the library stick as 'other' type, description 'show off all your simple add-ons', and confirms the current SAO header standard is V1.69bis (2x3 ISP connector)."
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SAO%20library%20stick
  title: SAO library stick folder
  accessed: '2026-09-07'
  note: Folder holds KiCad schematic/PCB/Gerber files for the long version; no BOM or standalone README present.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/img/IMG_20240414_173038.jpg
  title: Photo of library sticks in use
  accessed: '2026-09-07'
  note: "Photo (in the repo's img/ folder) shows multiple library sticks, each holding roughly nine SAOs, mounted in a wooden frame in front of a 'Hackspace Xhain' sign; used to save the entry's image."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    No dedicated event or year is given for the library stick itself; it is a general-purpose
    display accessory for davedarko's SAO collection rather than something made for one con, so
    event is left as "other". The repo README credits the "long" version to Eagle CAD, but the
    repository folder for it now contains only KiCad files (schematic, PCB, Gerbers) — the two
    disagree and it isn't clear if the Eagle files were replaced or the README line is stale, so
    EDA tool is reported as KiCad from what's actually in the folder. Two further variants exist
    in the same repo, "SAO library stick short" and "SAO_stick_sideways" (both KiCad, both with
    Gerbers/production files), added as links but not separately researched. Could not find a
    stated SAO header count, price, quantity, or distribution — davedarko appears to have made
    these for himself/his own display rather than sold them, based on the repo and photo (shown
    at Hackspace Xhain, a Berlin hackerspace, not identified as a con). make_your_own.open_source
    set to "partial": Gerbers and KiCad source are published for two of the three variants, but no
    license file was found in the repository and no firmware applies (the stick has no MCU).
last_modified_date: '2026-09-07'
---

The library stick is a simple accessory from prolific SAO designer davedarko (creator of the Knight Rider badge, Mr. Robot SAO, and many other add-ons in the same `Simple-Add-ons-SAO` GitHub repository): a stick-shaped PCB with a row of SAO headers and no microcontroller of its own, meant purely to hold and show off a collection of other people's SAOs at once rather than to be worn as a badge. The repository's README describes it simply as something to "show off all your simple add-ons," and it uses the current V1.69bis (2x3 ISP-style) SAO header standard.

A photo in the repository shows several of these sticks mounted together in a wooden display frame, each one populated with roughly nine different SAOs — skulls, animals, video-game and movie references — lit up in front of a "Hackspace Xhain" sign, suggesting the sticks were built for davedarko's own collection and shown at that Berlin hackerspace rather than sold or distributed at a specific convention.

The repository holds three related variants: the original long "SAO library stick," a "SAO library stick short," and a "SAO_stick_sideways" version, all with KiCad source files, and two of the three ship exported Gerbers ready for fabrication. No BOM, price, or quantity information is published for any of them.
