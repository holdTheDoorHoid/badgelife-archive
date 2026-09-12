---
title: DC503 Banglet Badge (DC26)
id: dc26-dc503-banglet-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Nisha K.
  url: https://nishakm.github.io/
  role: original concept, board design, firmware
- name: r00tkillah
  role: board design, PCB assembly
- name: DC503
  role: party crew / commissioner
summary: A wrist-worn party badge made for the DC503 party at DEF CON 26 (2018) that scans for nearby Bluetooth devices and lights its 12 LEDs by count and MAC-address-derived color.
functions: 'Passive Bluetooth scanning: lights up LEDs corresponding to the number of nearby BT devices detected, with LED colors derived from each device''s MAC address. Has a Bluetooth-UART shell (accessible via a BLE terminal app) that lists detected device MAC addresses and unlocks additional hidden modes based on how many devices have been detected.'
look:
  colors: []
  shape: bangle
  themes:
  - wearable
  - radio
  - security
tech:
  mcu: BMD-300 (Rigado nRF52-based BLE module)
  leds:
    count: 12
    type: RGB
    note: Not Neopixels/WS2812 - a custom smaller charlieplexed-style arrangement chosen to fit the bangle's slim form factor.
  display: none
  connectivity:
  - ble
  battery: LiPo 3V, USB rechargeable
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: over 100
  availability: not_released
  availability_note: Made as a party favor for the DC503 party at DEF CON 26 (2018); not sold. Checked 2026-09-07, no storefront found.
  distribution:
  - free_drop
  where: Given out at the DC503 party at DEF CON 26, 2018.
make_your_own:
  open_source: true
  hardware_url: https://github.com/pdxbadgers/2018-banglet
  firmware_url: https://github.com/pdxbadgers/2018-banglet
  gerbers_url: null
  bom_url: null
  eda_tool: Eagle
  license: Apache-2.0
  fab_url: null
  notes: Repo (pdxbadgers/2018-banglet) contains eaglecad/ board files, sketches/ (Arduino firmware, main sketch banglet.ino) and 3dprints/ enclosure files.
links:
- label: nishakm.github.io/things/dc503banglet
  url: https://nishakm.github.io/things/dc503banglet/
  kind: website
- label: pdxbadgers/2018-banglet (GitHub)
  url: https://github.com/pdxbadgers/2018-banglet
  kind: repo
- label: YouTube demo (connecting to the banglet)
  url: https://www.youtube.com/embed/ctZMv4urpgQ
  kind: video
images:
- file: assets/images/badges/dc26/dc503-banglet-badge-dc26/776b23e46b.jpg
  source: https://nishakm.github.io/things/dc503banglet/
  credit: Nisha K.
  caption: Banglet shell command interface screenshot
contact: {}
notes:
- The maker's page (nishakm.github.io) linked to this badge under a URL path that no longer exists (/engineering/dc503banglet/, 404); the current live page is at /things/dc503banglet/.
- A photo of the banglet lit up ("banglet in scan mode") was linked from the maker's page via a pbs.twimg.com URL that now 404s (expired Twitter media); could not be saved.
status: released
sources:
- kind: url
  url: http://nishakm.github.io/engineering/dc503banglet/
  title: DC503 Banglet Badge (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
- kind: url
  url: https://nishakm.github.io/things/dc503banglet/
  title: The DC503 Banglet for DefCon26
  accessed: '2026-09-07'
  note: Current live URL for the maker's write-up (the original sourced URL 404s). Confirms maker, event/year, BLE scanning function, 12 LEDs, BMD-300 chip, LiPo/USB power, GitHub repo link, and background story.
- kind: url
  url: https://github.com/pdxbadgers/2018-banglet
  title: pdxbadgers/2018-banglet
  accessed: '2026-09-07'
  note: README confirms "DEFCON 26 DC503 VIP Banglet" name, full maker/credit list, and repo contents (eaglecad, sketches, 3dprints); Apache-2.0 license.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price and exact quantity beyond "over 100" not stated by any source; treated as a free party giveaway, not a sold item. Only one usable photo found (a screenshot of the BLE shell) - the maker's photo of the lit-up banglet on a wrist is a dead Twitter media link.
last_modified_date: '2026-09-11'
model:
  file: assets/models/dc26/dc503-banglet-badge-dc26.glb
  method: kicad
  source_file: dc5032018banglet.brd
  generated: '2026-09-11'
  bytes: 141904
---

The DC503 Banglet was the party badge made for the DC503 crew's party at DEF CON 26 in 2018. Maker Nisha K. had previously built a one-off LED bangle for a friend attending DEF CON 25, and was approached by r00tkillah to scale that idea up into a run of over 100 units, this time built around the BMD-300 Bluetooth module (the same chip family used in the prior year's Wagon Badge). The result, nicknamed "the Banglet," is a wrist-worn device rather than a neck badge, chosen partly because badges on lanyards were seen as overused.

In its default passive mode the Banglet continuously scans for nearby Bluetooth devices and lights its 12 LEDs to show how many it has found, with each LED's color derived from the detected device's MAC address. It also exposes a Bluetooth-UART shell: connecting with a BLE terminal app (the team used Adafruit's Bluefruit LE Connect) lets the wearer list the MAC addresses it has seen and unlock additional hidden modes depending on how many devices have been detected. It runs on a small 3V LiPo cell that can be charged over USB, and the enclosure design borrows from an Adafruit NeoPixel bracelet project, including its magnetic wrist-fastening approach.

The project was a group effort credited to Nisha K. (concept, board design, firmware) and r00tkillah (board design) alongside several other PDX-area badge makers for PCB work, 3D design, and code. Hardware (Eagle board files), firmware (Arduino sketches), and 3D-print files are published under Apache-2.0 at github.com/pdxbadgers/2018-banglet.

## Make your own

The GitHub repo (pdxbadgers/2018-banglet) has everything needed to reproduce or reprogram a unit: `eaglecad/` for the PCB design, `sketches/` for the Arduino firmware (the shipped sketch is `banglet.ino`, though the repo's other sketches are also usable), and `3dprints/` for the wrist-enclosure files. The board is based on Adafruit's Bluefruit Feather / BMD-300 reference design, so Adafruit's own nRF52 Arduino learning guide is a useful companion for anyone building or modifying the firmware.
