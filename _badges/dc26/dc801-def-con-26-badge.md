---
title: DCZia DEF CON 26 badge
id: dc26-dc801-def-con-26-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
series: DCZia
makers:
- name: DCZia
  url: https://github.com/dczia
- name: hamster (snurkle engineering)
  url: https://www.tindie.com/stores/hamster/
  role: designer / seller
summary: A 4x4 grid of mechanical Gateron Blue keyswitches with RGB LEDs and transparent keycaps underneath, topped with a small OLED, built by the DCZia crew for DEF CON 26.
functions: Lights up its 16 keyswitches with RGB effects, shows menus and a light show on the OLED, and advertises over BLE with a DEF CON-specific manufacturer ID.
look:
  colors:
  - black
  - multicolor
  shape: rectangle
  themes: []
  form_factor: pcb badge
tech:
  mcu: ESP32
  leds:
    count: 16
    type: Neopixel Mini RGB (WS2812-style)
    note: one LED under each of the 16 Gateron Blue keyswitches, shining through clear/translucent 3D-printed keycaps
  display: 0.91" 128x32 OLED (SSD1306)
  connectivity:
  - ble
  - wifi
  - usb
  inputs:
  - buttons
  battery: 2x or 3x AA (USB power also offered on the sold version)
  sao_version: null
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing for the assembled/kitted version shows "no longer available" (checked 2026-09-07).
  distribution:
  - purchase
  where: Sold by hamster's snurkle engineering shop on Tindie, with the ESP32 and other SMD parts pre-populated and the through-hole parts kitted for the buyer to solder.
make_your_own:
  open_source: true
  hardware_url: https://github.com/hamster/Defcon26-Badge
  firmware_url: https://github.com/hamster/Defcon26-Badge
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: Unlicense
  fab_url: null
  notes: STL files for the 3D-printed keycaps are also in the repo.
links:
- label: github.com/hamster/Defcon26-Badge
  url: https://github.com/hamster/Defcon26-Badge
  kind: repo
- label: github.com/dczia/Defcon26-Badge
  url: https://github.com/dczia/Defcon26-Badge
  kind: repo
  archived: https://web.archive.org/web/20260512135511/https://github.com/dczia/Defcon26-Badge
- label: DCZia DEF CON 26 Mechanical Keyboard Badge (Tindie)
  url: https://www.tindie.com/products/hamster/dczia-defcon-26-mechanical-keyboard-badge/
  kind: store
  archived: https://web.archive.org/web/20260510011747/https://www.tindie.com/products/hamster/dczia-defcon-26-mechanical-keyboard-badge/
images:
- file: assets/images/badges/dc26/dc801-def-con-26-badge/fff1e117c8.jpg
  source: https://www.tindie.com/products/hamster/dczia-defcon-26-mechanical-keyboard-badge/
  credit: snurkle engineering (hamster)
  caption: 'DCZia DEF CON 26 badge: 4x4 mechanical keyswitch grid with RGB backlighting'
  archived: https://web.archive.org/web/20260510011747/https://www.tindie.com/products/hamster/dczia-defcon-26-mechanical-keyboard-badge/
- file: assets/images/badges/dc26/dc801-def-con-26-badge/488e63d96c.jpg
  source: https://www.tindie.com/products/hamster/dczia-defcon-26-mechanical-keyboard-badge/
  credit: snurkle engineering (hamster)
  caption: DCZia DEF CON 26 badge, assembled with keycaps and OLED lit
  archived: https://web.archive.org/web/20260510011747/https://www.tindie.com/products/hamster/dczia-defcon-26-mechanical-keyboard-badge/
contact: {}
notes:
- The community sheet titled this "DC801 DEF CON 26 badge"; the maker's own README and the Tindie listing both name it the "DCZia 2018" / "DCZia DEF CON 26" badge. The designer (hamster) is DC801-affiliated (Sandy, UT / snurkle engineering also sells separate DC801-branded SAOs), but this specific board is DCZia's, not the unrelated DC801 "party badge" (nRF52832/BMD-300, LCD, tic-tac-toe) covered the same year by Hackaday's DEF CON 26 badge roundup — that is a different item, see other_items_found.
status: released
sources:
- kind: url
  url: https://github.com/hamster/Defcon26-Badge
  title: DC801 DEF CON 26 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc26''.'
- kind: url
  url: https://raw.githubusercontent.com/hamster/Defcon26-Badge/master/README.md
  title: DCZia 2018 README
  accessed: '2026-09-07'
  note: Maker's own description, feature list, chip/display/LED/switch specs, license, dev history.
- kind: url
  url: https://www.tindie.com/products/hamster/dczia-defcon-26-mechanical-keyboard-badge/
  title: DCZia DEF CON 26 Mechanical Keyboard Badge (Tindie)
  accessed: '2026-09-07'
  note: Confirms seller (snurkle engineering / hamster), sold-out status, SAO/minibadge headers, USB power option, and product photos.
  archived: https://web.archive.org/web/20260510011747/https://www.tindie.com/products/hamster/dczia-defcon-26-mechanical-keyboard-badge/
- kind: url
  url: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  title: All The Badges Of DEF CON 26 (vol 3)
  accessed: '2026-09-07'
  note: Covers a different DC801 badge (nRF52832/BMD-300 "party badge") from the same year; used to confirm this is a distinct item, not a duplicate.
  archived: https://web.archive.org/web/20260417144127/https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's README and the Tindie storefront agree on the core facts. Price and exact production quantity are not stated anywhere found. Tindie's listing text loosely describes a "128x60 OLED" while the maker's own README specifies a 0.91" 128x32 SSD1306; the README is treated as authoritative since it is the maker's own build documentation written throughout development.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/dc801-def-con-26-badge.glb
  method: kicad
  source_file: Hardware/KeyGridBadge/KeyGridBadge.kicad_pcb
  generated: '2026-09-07'
  bytes: 536836
---

The DCZia badge was DEF CON 26's entry in an annual line of mechanical-keyswitch badges built by the DCZia crew (with hamster of Salt Lake City's snurkle engineering doing the hardware design). It packs a 4x4 grid of Gateron Blue keyswitches, each lit from underneath by a mini RGB LED and topped with a clear 3D-printed keycap, plus a small SSD1306 OLED at the top for menus and status. An ESP32 drives the whole thing, talking BLE (and possibly Wi-Fi) and advertising with a DEF CON 26-specific manufacturer ID so badges could recognize each other on the floor.

Hardware went through several prototype revisions (Proto Dos, Proto Tres) between February and August 2018 before the final board shipped, powered by two or three AA batteries. hamster's snurkle engineering shop sold it on Tindie with the ESP32 and other SMD parts pre-soldered and the through-hole parts left for the buyer to assemble; it also carries two SAO headers and a minibadge socket. That Tindie listing is now marked sold out.

## Make your own

Hardware and firmware are both published under the Unlicense in the [hamster/Defcon26-Badge](https://github.com/hamster/Defcon26-Badge) repo (mirrored under the [dczia](https://github.com/dczia/Defcon26-Badge) GitHub org), including the STL files for the keycaps and an Arduino-based ESP32 sketch. No Gerbers or a bill of materials were found published alongside it.
