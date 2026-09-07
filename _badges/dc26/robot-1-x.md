---
title: Robot 1-X
id: dc26-robot-1-x
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: TI
  url: https://hackaday.io/tamperinfo
summary: A DEF CON 26 Shitty Add-On in the shape of Robot 1-X, built around an ATtiny85 with three LEDs; the final R4 revision has a purple solder mask and 144 were made (about 125 offered at the con), preceded by a 40-unit blue R2 revision with white LEDs.
functions: 'Blinky/lighting SAO; the maker intended custom I2C-driven animation when plugged into the AND!XOR DC26 badge, but ran out of time to finish that firmware before the con.'
look:
  colors: [purple, blue, white]
  shape: robot
  themes: [robot, sao]
tech:
  mcu: ATtiny85-20SU
  leds:
    count: 3
    type: discrete
    note: 'R4: 3x LY T776-Q2T1-26 LEDs. R2 (blue PCB): originally OSRAM TOPLED, replaced with white 1210 LEDs after the color washed out under the blue solder mask.'
  display: none
  connectivity: [i2c]
  battery: powered by host badge
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: '144 (R4, purple) + 40 (R2, blue) = ~184 total; about 125 of the R4 run were available at the con'
  availability: free
  distribution: [free_drop]
  where: Given away at DEF CON 26 (2018) by the maker; some were offered in exchange for help finishing the I2C animation firmware.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/160221-robot-1-x
  url: https://hackaday.io/project/160221-robot-1-x
  kind: hackaday
- label: twitter.com/tamperinfo/status/1022242364239298564
  url: https://twitter.com/tamperinfo/status/1022242364239298564
  kind: social
images:
  - file: assets/images/badges/dc26/robot-1-x/e6434cd9a8.jpg
    source: "https://hackaday.io/project/160221-robot-1-x"
    credit: "TI (tamperinfo)"
    caption: "Robot 1-X R4 SAO with purple solder mask"
  - file: assets/images/badges/dc26/robot-1-x/d62d7ca342.jpg
    source: "https://hackaday.io/project/160221-robot-1-x"
    credit: "TI (tamperinfo)"
    caption: "Robot 1-X SAO, gallery photo"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/160221-robot-1-x
  title: Robot 1-X
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/160221-robot-1-x
  title: Robot 1-X (project logs and components)
  accessed: '2026-09-07'
  note: 'Confirmed maker (TI/tamperinfo), MCU (ATtiny85-20SU), LED parts and counts for both revisions (R4 purple/125 of 144 available, R2 blue/40), free distribution at DC26, intended I2C link to the AND!XOR DC26 badge, and that bottom-of-PCB photos were withheld pre-con. A commenter asked about a GitHub release for board/code; no reply is visible on the page, so open-source status is left unknown.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'The X/Twitter link (https://x.com/tamperinfo/status/1022242364239298564) returned HTTP 402 and could not be read; it was linked from the Hackaday log as an early demo of the intended I2C animation. Whether hardware/firmware were ever open-sourced is unconfirmed - a project comment asks the maker directly and no answer is visible on the page.'
last_modified_date: '2026-09-07'
---

Robot 1-X is a DEF CON 26 (2018) Shitty Add-On made by TI (hackaday.io/tamperinfo), styled after the robot character of the same name. It runs on an ATtiny85-20SU with three discrete LEDs. The maker produced two revisions: an initial 40-unit run with a blue solder mask (R2), where the original OSRAM TOPLED washed out under the blue mask and was swapped for a white 1210 LED (giving it more of a deep-green look), and a final 144-unit run with a purple solder mask (R4) that simplified programming down to six pin headers or two pogo pins. About 125 of the R4 units were actually available at the con; the rest of the roughly 184 total made up prototypes, spares, and units set aside.

TI's original plan was custom I2C-driven animation when Robot 1-X was plugged into the AND!XOR DC26 badge, and a Twitter/X post was linked as an early demo of that effect, but time ran out before the con and the firmware for that feature was never finished. The maker offered free badges to anyone willing to pick up the I2C work. Photos of the underside of the PCB were deliberately withheld before DEF CON to keep the design under wraps until people had the badge in hand. A commenter later asked whether the board and code would be posted to GitHub; there is no visible reply, so it is unclear whether the design files were ever released.
