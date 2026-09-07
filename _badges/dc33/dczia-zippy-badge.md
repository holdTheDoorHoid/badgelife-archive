---
title: Zippy Badge
id: dc33-dczia-zippy-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: DCZia
  url: https://github.com/dczia
summary: A wearable badge shaped and colored like a classic Zip disk, with a 42-NeoPixel matrix that shines through a translucent shell in sound- and motion-reactive light shows.
functions: A four-way joystick cycles between modes and adjusts brightness; modes include a rainbow display, an accelerometer-reactive mode that shifts color with tilt, and a microphone-driven sound-reactive "party mode."
look:
  colors:
  - clear
  - multicolor
  shape: rectangle
  themes:
  - retro computer
  - wearable
tech:
  mcu: RP2040
  leds:
    count: 42
    type: WS2812B
    note: 'Described by the maker as "NeoPixels" on a Raspberry Pi Pico 2040-based board.'
  display: none
  connectivity:
  - usb
  battery: USB-C or AA battery pack
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
  hardware_url: https://github.com/dczia/zippy-badge
  firmware_url: https://github.com/dczia/zippy-badge
  eda_tool: null
links:
- label: github.com/dczia/zippy-badge
  url: https://github.com/dczia/zippy-badge
  kind: repo
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/dczia/zippy-badge
  title: DCZia zippy-badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''unknown''.'
- kind: url
  url: https://github.com/dczia/zippy-badge
  title: 'GitHub - dczia/zippy-badge'
  accessed: '2026-09-07'
  note: 'Repo README confirms Zippy Badge made for DEF CON 33 (2025) by DCZia, RP2040/CircuitPython, 1-42 NeoPixels, joystick + accelerometer + microphone inputs, USB-C or AA power, open-source Hardware/Software/Shells folders.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This is a duplicate of the existing, more fully researched entry dc33-zippy (same repo, same badge). Filled in from the maker''s GitHub repo only; price, quantity, and exact SAO header version were not confirmed from this source (see dc33-zippy for Tindie storefront details, which name a price of $80 and note limited stock as of 2026-09-06). Did not add images to avoid re-downloading the same photo already saved for dc33-zippy.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/dczia-zippy-badge/
---

Zippy is DCZia's badge for DEF CON 33 (2025), styled after a classic Zip disk with a translucent plastic shell over the PCB. A Raspberry Pi RP2040 running CircuitPython drives a 42-LED NeoPixel matrix visible through the shell, with a four-way joystick for cycling between a rainbow mode, an accelerometer-reactive tilt mode, and a microphone-driven sound-reactive "party mode." It runs on USB-C power or an AA battery pack, and the case is held together with four M2x4 screws; the maker also publishes custom 3D-printable shell designs.

Hardware and firmware are open source on GitHub, continuing DCZia's series of DEF CON badges. This entry duplicates the archive's `dc33-zippy` entry, which was researched from DCZia's Tindie storefront ("snurkle engineering") and carries pricing ($80) and stock details not confirmed from the GitHub repo alone.

## Make your own

Hardware and firmware live in the [zippy-badge](https://github.com/dczia/zippy-badge) repository, with Hardware, Software (CircuitPython), and Shells (3D-printable case) folders. Connect the badge over USB-C so it mounts as a CircuitPython drive, then copy the firmware onto it to reflash.
