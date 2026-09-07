---
title: Mr Robot Badge
id: dc25-mr-robot-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: Benchoff
  url: https://hackaday.io/benchoff
summary: An independent DEF CON 25 badge shaped like the Mr. Robot mask, with a skin-tone soldermask, an ESP8266, a 16x9 charlieplexed LED matrix of 144 LEDs driven by an IS31FL3731, an ambient light sensor, seven buttons, four AA cells, and an ARG component; about 500 were built and handed out in Las Vegas in 2017.
functions: An alternate-reality-game element built into the badge (steganography/puzzle elements); the LED matrix and light sensor support interactive lighting effects.
look:
  colors:
  - skin-tone
  shape: mask
  themes:
  - tv
  - hardware tool
tech:
  mcu: ESP8266
  leds:
    count: 144
    type: charlieplexed
    note: 16x9 RGB LED matrix driven by an IS31FL3731 driver chip
  display: LED matrix 16x9
  connectivity:
  - wifi
  battery: 4x AA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: about 480-500
  availability: unknown
  distribution:
  - free_drop
  where: Handed out at DEF CON 25 in Las Vegas, August 2017.
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/18508-mr-robot-badge
  firmware_url: https://hackaday.io/project/18508-mr-robot-badge
  eda_tool: KiCad
links:
- label: hackaday.io/project/18508-mr-robot-badge
  url: https://hackaday.io/project/18508-mr-robot-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260116150752/https://hackaday.io/project/18508-mr-robot-badge
- label: mrrobotbadge.tv
  url: http://mrrobotbadge.tv
  kind: website
- label: Source files (GitHub)
  url: https://github.com/bbenchoff/MrRobotBadge/tree/master/Shitty%20Add-Ons
  kind: hardware
images:
- file: assets/images/badges/dc25/mr-robot-badge/7d3875d088.png
  source: https://hackaday.io/project/18508-mr-robot-badge
  credit: Benchoff
  caption: The Mr. Robot Badge, DEF CON 25
- file: assets/images/badges/dc25/mr-robot-badge/aac5188f7a.jpg
  source: https://hackaday.io/project/18508-mr-robot-badge
  credit: Benchoff
  caption: Mr. Robot Badge assembled with battery pack
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/18508-mr-robot-badge
  title: Mr Robot Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260116150752/https://hackaday.io/project/18508-mr-robot-badge
- kind: url
  url: https://hackaday.io/project/18508-mr-robot-badge
  title: Mr Robot Badge - Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed maker (Benchoff), event/year (DEF CON 25, 2017), MCU (ESP8266), LED matrix (144 LEDs, 16x9, IS31FL3731 driver, charlieplexed), light sensor (LTR-239ALS-01), seven buttons, 4xAA power, ARG element, quantity (~480-500 built), and that KiCad project files/Gerbers, schematic, vector art, and firmware are published on the project page. Also source of image URLs (og:image and gallery photos).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: mrrobotbadge.tv returned no content when fetched (likely expired/parked domain or JS-only site) so it could not be used as a source; left in links for reference. Price is not stated anywhere found (it was a free DEF CON drop, not sold), so get_one.price left blank. Exact quantity varies slightly by source (480 vs 500); recorded as 'about 480-500'. No separate design-file repo URL beyond the Hackaday.io project page itself, so hardware_url/firmware_url point there.
last_modified_date: '2026-09-07'
---

The Mr. Robot Badge was an independent electronic badge created by Brian Benchoff (a Hackaday writer, working under the handle "Benchoff" on Hackaday.io) for DEF CON 25 in Las Vegas in August 2017. Shaped like the mask worn by the "fsociety" hackers in the TV series *Mr. Robot*, the badge used a skin-tone soldermask and silkscreen artwork to render the mask's face directly on the PCB. Around 480 to 500 units were built and handed out for free at the con.

Electronically, the badge runs on an ESP8266 with Wi-Fi, and drives a 16x9 charlieplexed matrix of 144 RGB LEDs through an IS31FL3731 LED driver chip, giving it an animated light-up face. It also carries an ambient light sensor, seven buttons for interaction, and runs off four AA batteries. The badge incorporated an alternate-reality-game (ARG) element, continuing a tradition of independent DEF CON badges that double as puzzles.

The full KiCad project (including Gerbers), a schematic PDF, vector art files, and firmware binaries are published on the Hackaday.io project page, making the design open source and reproducible.
