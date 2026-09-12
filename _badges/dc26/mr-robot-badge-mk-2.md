---
title: Mr. Robot Badge Mk. 2
id: dc26-mr-robot-badge-mk-2
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Brian Benchoff
  url: https://bbenchoff.com
summary: An independent LED-matrix conference badge made by Brian Benchoff for DEF CON 26, built around an ESP8266 and an ISSI IS31FL3741 driver chip to run an 18x18 LED matrix, with five Shitty Add-On ports for other badgemakers' add-ons.
functions: Runs blinky LED matrix effects (including a Conway's Game of Life demo) driven by the IS31FL3741 over I2C; reprogrammable over a serial-to-USB connection; hosts up to five SAO add-on boards.
look:
  colors:
  - clear
  - black
  - white
  shape: rectangle
  themes:
  - robot
  - tv
tech:
  mcu: ESP8266
  leds:
    count: 324
    type: IS31FL3741-driven
    note: 18x18 LED matrix addressed over I2C via the ISSI IS31FL3741 driver chip.
  display: LED matrix 18x18
  connectivity:
  - i2c
  inputs:
  - buttons
  battery: 2x AA
  sao_version: v1
  sao_ports: 5
get_one:
  price: ''
  price_usd: null
  quantity: ~1000
  availability: sold_out
  availability_note: No active storefront found as of 2026-09-07; badge was distributed at DEF CON 26 in August 2018.
  distribution: []
  where: Distributed to attendees at DEF CON 26 (August 2018); shipped/handed out in anti-static bubble mailers, each including one of ten random SAO add-on variants (~100 of each).
make_your_own:
  open_source: true
  hardware_url: https://github.com/bbenchoff/MrRobotBadge
  firmware_url: https://github.com/bbenchoff/MrRobotBadge
  eda_tool: null
links:
- label: hackaday.io/project/94291-mr-robot-badge-mk-2
  url: https://hackaday.io/project/94291-mr-robot-badge-mk-2
  kind: hackaday
- label: Mr. Robot Badge Mk. 2 build logs
  url: https://hackaday.io/project/94291/logs
  kind: hackaday
- label: bbenchoff/MrRobotBadge (GitHub)
  url: https://github.com/bbenchoff/MrRobotBadge
  kind: repo
- label: Mr. Robot Badge - Benchoff Design Portfolio
  url: https://bbenchoff.com/pages/MrRobot.html
  kind: website
- label: 'Hackaday: All The Badges Of DEF CON 26 (vol 2)'
  url: https://hackaday.com/2018/08/21/all-the-badges-of-def-con-26-vol-2/
  kind: article
images:
- file: assets/images/badges/dc26/mr-robot-badge-mk-2/8d202652a3.jpg
  source: https://bbenchoff.com/pages/MrRobot.html
  credit: Brian Benchoff
  caption: Mr. Robot Badge Mk. 2, DEF CON 26
- file: assets/images/badges/dc26/mr-robot-badge-mk-2/d9d86ee15d.png
  source: https://bbenchoff.com/pages/MrRobot.html
  credit: Brian Benchoff
  caption: PCB layer stackup for the Mr. Robot Badge Mk. 2
contact: {}
notes:
- URL slug inferred from log path /project/94291/logs; verify exact slug.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/94291-mr-robot-badge-mk-2
  title: Mr. Robot Badge Mk. 2
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/94291-mr-robot-badge-mk-2
  title: Mr. Robot Badge Mk. 2
  accessed: '2026-09-07'
  note: Confirmed maker (Benchoff), event/year (DEF CON 26, 2018), MCU/LED driver, battery, five SAO ports, and Game Boy-style buttons.
- kind: url
  url: https://hackaday.io/project/94291/logs
  title: Mr. Robot Badge Mk. 2 build logs
  accessed: '2026-09-07'
  note: Confirmed 2x AA battery choice, ~1000 unit production run, five SAO connectors with ~10 random add-on variants, and prototype development cost (not a retail price).
- kind: url
  url: https://bbenchoff.com/pages/MrRobot.html
  title: Mr. Robot Badge - Benchoff Design Portfolio
  accessed: '2026-09-07'
  note: Maker's own project page; confirmed ESP8266 MCU, IS31FL3741 driver, GitHub repo link, and source images of the badge and PCB.
- kind: url
  url: https://hackaday.com/2018/08/21/all-the-badges-of-def-con-26-vol-2/
  title: All The Badges Of DEF CON 26 (vol 2)
  accessed: '2026-09-07'
  note: Press coverage confirming the 18x18 LED matrix driven by IS31FL3741 over I2C and reprogrammability via serial-to-USB.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Second badge in Benchoff's "Mr. Robot Badge" line (Mk. 1 was for DEF CON 25, a separate Hackaday.io project at /project/18508-mr-robot-badge, not this entry). No retail price was ever published — the ~$4841.77 figure on the build log covers prototype/bulk-component development cost for two prototypes plus the ~1000-unit run, not a per-unit price. Exact distribution method (sold vs. given away) at DEF CON 26 is not stated explicitly in the sources found, so get_one.distribution is left empty rather than guessed. EDA tool used is not stated in any source checked.
last_modified_date: '2026-09-11'
redirect_from:
- /badges/other/mr-robot-badge-mk-2/
model:
  file: assets/models/dc26/mr-robot-badge-mk-2.glb
  method: kicad
  source_file: MrRobotBadge.brd
  generated: '2026-09-11'
  bytes: 934736
---

The Mr. Robot Badge Mk. 2 is Brian Benchoff's second-generation independent conference badge, built for DEF CON 26 in August 2018 as part of the badgelife hardware demoscene. It upgrades the original Mr. Robot Badge (made for DEF CON 25) around a newly-released ISSI IS31FL3741 LED driver chip, which lets an ESP8266 microcontroller drive a much larger 18x18 LED matrix over I2C than the previous design could manage, producing dense blinky animations (Benchoff demonstrated a Conway's Game of Life implementation as one example). The badge runs on two keyed AA battery holders and can be reprogrammed over a serial-to-USB connection.

Benchoff manufactured roughly 1,000 units of the Mk. 2 for DEF CON 26 and shipped them in anti-static bubble mailers. Each badge carries five ports built to the "Shitty Add-On" standard he helped establish that year (power, ground, and I2C), and about ten different third-party SAO add-on designs — roughly 100 of each — were randomly bundled with badges, including a dual-color pad-printed add-on called the Tide Pod Blockchain.

## Make your own

Hardware and firmware files are published on GitHub at bbenchoff/MrRobotBadge. The EDA tool used for the design was not stated in any source checked.
