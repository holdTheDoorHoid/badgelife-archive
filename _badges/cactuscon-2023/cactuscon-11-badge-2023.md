---
title: CactusCon 11 Badge (2023)
id: cactuscon-2023-cactuscon-11-badge-2023
layout: badge
parent: CactusCon 11 (2023)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2023
year: 2023
makers:
- name: Badge Pirates
  url: https://www.badgepirates.com/
summary: The official electronic badge for CactusCon 11 (2023), built by Badge Pirates around a "Nightmare House" IoT theme.
functions: Home-automation-style IoT demo badge with controllable LEDs and buttons for user customization; supports an optional OLED add-on and exposes GPIO for hacking.
look:
  colors: []
  shape: null
  themes:
  - iot
  - horror
  - hardware tool
tech:
  mcu: ESP32-S2 WROOM
  leds:
    count: 6
    type: RGB
    note: Two reverse-mount RGB LEDs (window effect), three addressable RGB NeoPixels, and one reverse-mount red LED.
  display: OLED (optional)
  connectivity:
  - wifi
  - usb
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
  hardware_url: https://github.com/BadgePiratesLLC/CactusCon_11
  firmware_url: https://github.com/BadgePiratesLLC/CactusCon_11
  eda_tool: null
links:
- label: badge.gallery/badges/cactuscon-11-badge
  url: https://badge.gallery/badges/cactuscon-11-badge
  kind: website
- label: blog.badgepirates.com/CactusConBadge
  url: https://blog.badgepirates.com/CactusConBadge/
  kind: article
- label: github.com/BadgePiratesLLC/CactusCon_11
  url: https://github.com/BadgePiratesLLC/CactusCon_11
  kind: repo
images:
- file: assets/images/badges/cactuscon-2023/cactuscon-11-badge-2023/79c761dd8f.jpg
  source: "https://blog.badgepirates.com/CactusConBadge/"
  credit: "Badge Pirates"
  caption: "CactusCon 11 badge staged photo"
contact: {}
notes:
- Official conference badge for CactusCon 11 (2023), made by Badge Pirates. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task con-layerone.
- Confirmed by Badge Pirates' own blog post and GitHub repo; the sweep's wording matched the maker's title exactly.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/cactuscon-11-badge
  title: CactusCon 11 Badge (2023)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''CactusCon 2023''.'
- kind: url
  url: https://blog.badgepirates.com/CactusConBadge/
  title: 'CactusCon 11 Badge (2023) - Badgepirates'
  accessed: '2026-09-10'
  note: 'Maker''s own writeup: theme, functions, chip, LEDs, display, links to GitHub/Tindie/YouTube; image URL.'
- kind: url
  url: https://github.com/BadgePiratesLLC/CactusCon_11
  title: 'GitHub - BadgePiratesLLC/CactusCon_11'
  accessed: '2026-09-10'
  note: 'Design/firmware repo (CAD, Code, Documents, Images folders); archived Oct 17 2023; README has no further detail.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >-
    Core facts (maker, event, theme, chip, LEDs, display) confirmed by Badge Pirates' own
    blog post. Price, quantity sold, and specific availability were not stated on any source
    checked. The GitHub repo (CactusCon_11) contains CAD/Code/Documents/Images folders,
    suggesting hardware and firmware were published, but no explicit open-source license was
    found in the README, so open_source is marked "partial" rather than "yes". A separate
    development board was reportedly available at the Hardware Hacking Village per
    badge.gallery, but this was not independently confirmed on a Badge Pirates page.
last_modified_date: '2026-09-10'
---

Badge Pirates built the CactusCon 11 (2023) badge around a "Nightmare House" theme that leans into an Internet-of-Things gag: the badge behaves like a miniature smart-home controller, complete with window-style RGB LEDs, three addressable NeoPixels, and a reverse-mount red LED styled as a "definitely not a camera" drone light. It runs on an ESP32-S2 WROOM with built-in 2.4 GHz Wi-Fi, exposes GPIO for hacking, includes a CH340N USB-serial chip for programming, and supports an optional OLED add-on.

Design and firmware files were published on GitHub under BadgePiratesLLC/CactusCon_11 (archived October 2023), with folders for CAD, code, documentation, and images, though the repository does not spell out an explicit license. Badge Pirates also wrote up the build on their blog, and mentioned links to a Tindie store and YouTube video for anyone wanting to build or buy their own. Price and total quantity produced were not stated in any source found.
