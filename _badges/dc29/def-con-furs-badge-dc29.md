---
title: DEF CON Furs Badge DC29
id: dc29-def-con-furs-badge-dc29
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: DEF CON Furs (defconfurs org)
  url: https://dcfurs.com/
summary: 'A DIY electronic badge DEF CON Furs made for its 2021 (DEF CON 29) meetup, driven by an IS31FL3737 LED driver with a rain/stars animation.'
functions: 'Runs an ambient LED animation (falling "droplets", "rain", and twinkling "stars" patterns) driven by firmware on the badge; no interactive game or CTF mentioned in the available source.'
look:
  colors: []
  shape: null
  themes:
  - animal
tech:
  mcu: null
  leds:
    count: null
    type: RGB
    note: 'Driven through a Lumissil/ISSI IS31FL3737 12x12 RGB LED matrix driver IC (I2C); firmware addresses at least 24 individually-addressed RGB positions.'
  display: null
  connectivity:
  - i2c
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
  hardware_url: https://github.com/defconfurs/dcfurs-badge-dc29
  firmware_url: https://github.com/defconfurs/dcfurs-badge-dc29
  eda_tool: null
  notes: 'Repo holds an Arduino-style firmware sketch (DCFurs29.ino, plus a separate "blink" test sketch and an Arduino_is31fl3737 driver library) and a schematic PDF ("DCFurs2021Badge - 2021-06-22.pdf"); no bill of materials, Gerbers, or full PCB CAD files were found in the repo, so hardware is only partially open (schematic only, no fab-ready layout).'
links:
- label: github.com/defconfurs/dcfurs-badge-dc29
  url: https://github.com/defconfurs/dcfurs-badge-dc29
  kind: repo
- label: DEFCON Furs
  url: https://dcfurs.com/
  kind: website
- label: DEFCON Furs 2021 event site
  url: https://2021.dcfurs.com/
  kind: website
images: []
contact: {}
notes:
- 'GitHub repo title reads "2021 DEFCON Furs Badge"; DC29 corresponds to DEF CON 29, held August 2021.'
status: released
sources:
- kind: url
  url: https://github.com/defconfurs/dcfurs-badge-dc29
  title: DEF CON Furs Badge DC29
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 29 (2021)''.'
- kind: url
  url: https://github.com/defconfurs/dcfurs-badge-dc29
  title: 'defconfurs/dcfurs-badge-dc29 repo contents (GitHub API)'
  accessed: '2026-09-07'
  note: 'Confirmed repo contains a schematic PDF, an Arduino sketch (DCFurs29.ino) using an Arduino_is31fl3737 library, a separate "blink" test sketch, and an "is31fl3737" driver folder; no MCU part number, BOM, or Gerbers present.'
- kind: url
  url: https://raw.githubusercontent.com/defconfurs/dcfurs-badge-dc29/main/DCFurs29/DCFurs29.ino
  title: DCFurs29.ino firmware source
  accessed: '2026-09-07'
  note: 'Firmware drives an IS31FL3737 LED driver over I2C to run "droplet", "rain", and "stars" LED animations across at least 24 addressed RGB LED positions; no MCU part identified in source.'
- kind: url
  url: https://dcfurs.com/
  title: DEFCON Furs
  accessed: '2026-09-07'
  note: 'Confirms DEF CON Furs is the organizing group behind the badge and links out to a "DEFCON Furs 2021 Site"; no badge-specific details for 2021 shown on the current main page.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Could not determine the MCU part number, LED count, price, quantity made, or distribution method (free vs. sold) from any source found; the 2021.dcfurs.com event site did not resolve live and no Wayback snapshot was checked for badge-specific text. No photo of the physical badge was located (repo has no images; only a schematic PDF). look.shape, look.colors, tech.mcu, tech.display, tech.battery, and get_one fields left empty/null accordingly.'
last_modified_date: '2026-09-07'
---

DEF CON Furs, the furry-community group that runs meetups alongside DEF CON, made its own badge for its 2021 gathering held during DEF CON 29. The badge is built around a Lumissil/ISSI IS31FL3737 RGB LED driver chip addressed over I2C, and its Arduino-style firmware ("DCFurs29.ino") drives ambient animations described in the source as "droplet," "rain," and "stars" patterns across at least two dozen individually addressed RGB LED positions.

The project's GitHub repository publishes a schematic PDF and the firmware (an Arduino sketch plus a standalone "blink" test sketch and a small IS31FL3737 driver library), but no bill of materials, PCB layout files, or Gerbers, so the hardware side is only partially open. No source found during this research states the badge's price, how many were made, how it was distributed to attendees, or its physical appearance (color, shape, or exact LED count) — those fields are left blank rather than guessed.

## Make your own

The firmware can be reviewed or reflashed from the repository's `DCFurs29/DCFurs29.ino` sketch, which depends on an `Arduino_is31fl3737` driver library, alongside a separate `blink` sketch for basic LED testing. Reproducing the hardware itself would require redrawing a PCB from the published schematic PDF, since no ready-to-fab board files are included.
