---
title: 2018 CL4P_TR4P SAO
id: dc26-2018-cl4p-tr4p-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: SparX
  url: https://www.pcbway.com/project/member/?bmbno=F0A1C4EA-6FC9-48
summary: A Claptrap (Borderlands) themed Shitty Add-On on a 75 x 75.4 mm matte-black immersion-gold PCB that uses the standard 4-pin SAO connector and an MCP23017 I2C expander to drive LEDs on the robot's face, with 220-ohm resistors on the back, presented at DEF CON 26 in 2018.
functions: ''
look:
  colors:
  - black
  - gold
  shape: robot
  themes:
  - robot
  - pop culture
tech:
  mcu: null
  leds: null
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
  firmware_url: null
  eda_tool: null
  gerbers_url: https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
  license: CC BY-SA 3.0
links:
- label: www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
  url: https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
  kind: fab
  archived: https://web.archive.org/web/20260907114017/https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
images:
- file: assets/images/badges/dc26/2018-cl4p-tr4p-sao/40b1fe6c16.png
  source: https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
  credit: SparX
  caption: Claptrap-themed SAO PCB shared on PCBWay
  archived: https://web.archive.org/web/20260907114017/https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
  title: 2018 CL4P_TR4P SAO - Share Project - PCBWay
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260907114017/https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
- kind: url
  url: https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
  title: 2018 CL4P_TR4P SAO - Share Project - PCBWay
  accessed: '2026-09-07'
  note: Confirmed maker (SparX), event/year (DEF CON, 2018), 4-pin SAO connector, MCP23017 I2C LED driver, 220-ohm resistors, 2-layer FR-4 board 75 x 75.4 mm, immersion gold finish with matte black soldermask and white silkscreen, and CC BY-SA 3.0 license. No price, quantity, or firmware repo listed.
  archived: https://web.archive.org/web/20260907114017/https://www.pcbway.com/project/shareproject/2018_CL4P_TR4P_SAO.html
- kind: url
  url: https://www.pcbway.com/project/member/?bmbno=F0A1C4EA-6FC9-48
  title: SparX - PCBWay Community member profile
  accessed: '2026-09-07'
  note: Checked maker's PCBWay profile for more projects or context; profile shows no other posts or shared projects.
  archived: https://web.archive.org/web/20260907114031/https://www.pcbway.com/project/member/?bmbno=F0A1C4EA-6FC9-48
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Only source found is the maker's own PCBWay shared-project page (a fab share, not a full write-up), which is why several fields (functions, LED count/type, MCU beyond the MCP23017 I/O expander, price, quantity made, availability) remain empty or null. A web search budget limit prevented additional searches for press coverage, a Hackaday.io page, or Twitter/Bluesky posts that might round out distribution and quantity details. The MCP23017 is an I2C GPIO expander, not a microcontroller, so tech.mcu is left null rather than guessed; it likely runs off the host badge's I2C bus with no onboard MCU. Design files (Gerbers) are shared via PCBWay's ordering flow under CC BY-SA 3.0, but no separate hardware/firmware repo was found.
last_modified_date: '2026-09-07'
---

The 2018 CL4P_TR4P SAO is a Claptrap-themed Shitty Add-On made by SparX for DEF CON 26. Claptrap is the excitable robot sidekick from Gearbox's Borderlands game series, and the SAO's face is laid out to evoke the character on a 75 x 75.4 mm two-layer PCB finished in immersion gold with a matte black soldermask and white silkscreen.

Electrically it is a passive-ish add-on built around an MCP23017 I2C GPIO expander, which drives LEDs on the robot's face through 220-ohm current-limiting resistors on the back of the board; it connects to a host badge over the standard 4-pin SAO header. No onboard microcontroller, LED count/type, price, or production quantity is documented on the maker's own project page, which is the only source found for this item.

The board's design files are shared through PCBWay's community "Share Project" platform under a CC BY-SA 3.0 license, making the Gerbers available to order or reference, though no separate firmware or hardware repository was located.
