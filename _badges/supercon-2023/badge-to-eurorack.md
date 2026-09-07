---
title: Badge to Eurorack
id: supercon-2023-badge-to-eurorack
layout: badge
parent: Supercon 2023
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2023
year: 2023
makers:
- name: Alex (tinyledmatrix)
  url: https://hackaday.io/tinyledmatrix
summary: A 3D-printed frame and adapter PCB that mounts the Hackaday Supercon 2023 badge (Vectorscope) into a standard Eurorack synthesizer case.
functions: 'Converts the badge into a Eurorack module: level-shifts the badge''s 0-3V signals to Eurorack levels, breaks out four 3.5mm jacks for audio/CV I/O, exposes USB for firmware updates, and regulates Eurorack rail power down for the badge via an LM317 LDO.'
look:
  colors: []
  shape: null
  themes:
  - music
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
  open_source: yes
  hardware_url: https://hackaday.io/project/193397-badge-to-eurorack
  firmware_url: https://github.com/Hack-a-Day/Vectorscope
  eda_tool: null
links:
- label: hackaday.io/project/193397-badge-to-eurorack
  url: https://hackaday.io/project/193397-badge-to-eurorack
  kind: hackaday
- label: Hack-a-Day/Vectorscope (Supercon 2023 badge repo)
  url: https://github.com/Hack-a-Day/Vectorscope
  kind: repo
images:
- file: assets/images/badges/supercon-2023/badge-to-eurorack/e1fa736308.jpg
  source: "https://hackaday.io/project/193397-badge-to-eurorack"
  credit: "Alex (tinyledmatrix)"
  caption: "Supercon 2023 badge mounted in the Eurorack adapter frame"
- file: assets/images/badges/supercon-2023/badge-to-eurorack/6bc5e95724.jpg
  source: "https://hackaday.io/project/193397-badge-to-eurorack"
  credit: "Alex (tinyledmatrix)"
  caption: "Level-shifting and Eurorack power adapter PCB for the badge"
contact: {}
notes: []
status: released
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a DIY accessory/mod project, not a standalone badge or SAO: it adapts the official Hackaday Supercon 2023 badge (the Vectorscope) to fit and interface with a Eurorack modular synthesizer case. Created by Alex (tinyledmatrix), a German electrical engineer known for LED-display projects, and posted to Hackaday.io on 2023-10-29. No price, quantity-made, or distribution info is given since it is a personal build rather than a sold item; the Hackaday.io project lists no formal completion/release date beyond the initial post. MCU/LED/display specs belong to the underlying Supercon 2023 badge itself, not to this adapter, so those tech fields are left empty here.'
last_modified_date: '2026-09-07'
sources:
- kind: url
  url: https://hackaday.io/project/193397-badge-to-eurorack
  title: Badge to Eurorack
  accessed: '2026-09-07'
  note: 'Primary project page: maker, event, purpose, features, components, open-source repo link, images.'
- kind: url
  url: https://hackaday.io/tinyledmatrix
  title: Alex (tinyledmatrix) - Hackaday.io profile
  accessed: '2026-09-07'
  note: 'Confirms maker handle/name and background; project itself not listed on profile page content retrieved.'
redirect_from:
- /badges/other/badge-to-eurorack/
---

[Alex (tinyledmatrix)](https://hackaday.io/tinyledmatrix), a German electrical engineer known for tiny-LED-matrix projects, built this adapter to bring the Hackaday Supercon 2023 badge ("Vectorscope") into a Eurorack modular synthesizer rack. Rather than being a badge or SAO in its own right, it is a 3D-printed frame plus a small prototype PCB that mounts the badge in standard Eurorack format and interfaces with the rack's power and signal buses.

The adapter board level-shifts the badge's native 0-3V signal range up to Eurorack-standard levels, breaks out four 3.5mm jacks for audio/CV input and output, keeps the badge's USB port accessible for firmware updates once installed, and steps Eurorack's rail voltage down for the badge through an LM317 low-dropout regulator. The project was posted to Hackaday.io on October 29, 2023, alongside build photos of the badge in its frame and the adapter PCB.

## Make your own

The adapter's own hardware files were not found published separately from the Hackaday.io write-up, but it is built around the open-source Supercon 2023 badge, whose firmware and hardware are published at [Hack-a-Day/Vectorscope](https://github.com/Hack-a-Day/Vectorscope) on GitHub.
