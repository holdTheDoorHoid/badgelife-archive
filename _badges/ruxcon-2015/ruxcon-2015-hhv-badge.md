---
title: Ruxcon 2015 HHV Badge
id: ruxcon-2015-ruxcon-2015-hhv-badge
layout: badge
parent: Ruxcon 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: ruxcon-2015
year: 2015
makers:
- name: Peter Fillmore / Ruxcon Hardware Hacking Village
summary: A crocodile-shaped, STM32F0-based badge built for the Ruxcon 2015 Hardware Hacking Village, designed to be soldered and programmed by attendees as a learn-to-solder / learn-to-hack exercise.
functions: Ships with a blinky-LED demo cycling three onboard LEDs; the assembly/programming write-up notes other example firmware for Wi-Fi connectivity, OLED screens, and general SPI/I2C interaction. Has a 4-switch d-pad, UART and SWD/JTAG programming headers, and I2C/SPI broken out for expansion.
look:
  colors: []
  shape: crocodile
  themes:
  - village badge
  - learn to solder
  - hardware tool
tech:
  mcu: STM32F0 (STM32F030K6)
  leds:
    count: 3
    type: discrete
    note: green, orange, and red status LEDs
  display: none
  connectivity:
  - i2c
  - uart
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed to Ruxcon 2015 attendees through the Hardware Hacking Village (HHV), where it was assembled and programmed as a village activity.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/peterfillmore/RuxconBadge2015
  firmware_url: https://github.com/peterfillmore/RuxconBadge2015
  eda_tool: null
links:
- label: github.com/peterfillmore/RuxconBadge2015
  url: https://github.com/peterfillmore/RuxconBadge2015
  kind: repo
- label: www.drkns.net/ruxcon-badge-2015-assembly
  url: https://www.drkns.net/ruxcon-badge-2015-assembly/
  kind: website
- label: www.drkns.net/ruxcon-badge-2015-programming
  url: https://www.drkns.net/ruxcon-badge-2015-programming/
  kind: website
images:
- file: assets/images/badges/ruxcon-2015/ruxcon-2015-hhv-badge/643eab3cb8.png
  source: "https://www.drkns.net/ruxcon-badge-2015-assembly/"
  credit: "Peter Fillmore / drkns.net"
  caption: "Assembled Ruxcon 2015 HHV badge, crocodile-shaped PCB"
contact: {}
notes:
- STM32-based electronic badge for the Ruxcon Hardware Hacking Village 2015, with public KiCad/schematic files and CR2032 power, documented on GitHub and in a build/programming writeup at drkns.net. Found by the event-year sweep, task con-kiwicon.
status: released
sources:
- kind: url
  url: https://github.com/peterfillmore/RuxconBadge2015
  title: Ruxcon 2015 HHV Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kiwicon); event read as ''Ruxcon 2015''.'
- kind: url
  url: https://github.com/peterfillmore/RuxconBadge2015
  title: peterfillmore/RuxconBadge2015 (GitHub, archived)
  accessed: '2026-09-08'
  note: Confirms maker (Peter Fillmore), Unlicense/public-domain hardware and firmware in /hardware and /firmware, and an included assembly PDF. Repo is archived (read-only) as of 2026-03-06.
- kind: url
  url: https://www.drkns.net/ruxcon-badge-2015-assembly/
  title: Ruxcon Badge 2015 - Assembly
  accessed: '2026-09-08'
  note: Confirms crocodile PCB shape, STM32F0x MCU, CR2032 power, 3 LEDs, 4-switch d-pad, P1/P6 UART and SWD/JTAG headers, and assembly credits (Dr Silvio, Aspect, Kylie) alongside Peter Fillmore. Provided the badge-clipped.png photo used here.
- kind: url
  url: https://www.drkns.net/ruxcon-badge-2015-programming/
  title: Ruxcon Badge 2015 - Programming
  accessed: '2026-09-08'
  note: Confirms STM32F030K6 part number and gives firmware demo details (blinky LED cycle; example code for Wi-Fi, OLED, SPI/I2C) and SWD-via-Bus-Pirate flashing steps.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: No price or production-quantity figures were published anywhere found; it was a free village build, so price/quantity fields are left empty rather than guessed. No storefront or aftermarket listing was found, so availability is left unknown rather than assumed sold_out. eda_tool for the hardware files was not confirmed from the pages fetched (repo file listing was not browsed in detail), so left null.
last_modified_date: '2026-09-08'
---

The Ruxcon 2015 HHV badge is a crocodile-shaped PCB built by Peter Fillmore for the Hardware Hacking Village at Ruxcon 2015 in Melbourne. It's built around an STM32F0 (STM32F030K6) ARM Cortex-M0 microcontroller with 32KB of flash, three status LEDs (green, orange, red), a four-switch d-pad, and both UART and SWD/JTAG programming headers, run from a CR2032 coin cell. It was designed as a village activity: attendees soldered the board themselves and then flashed it, learning basic embedded development along the way.

Peter Fillmore documented the whole process publicly, and a companion pair of write-ups on drkns.net (with assembly help credited to Dr Silvio, Aspect, and Kylie) walk through identifying components, hand-soldering the fine-pitch microcontroller, and programming the board over SWD using a Bus Pirate. Example firmware ranges from a simple LED-blink demo to short demonstrations of Wi-Fi connectivity, OLED displays, and general SPI/I2C use, though the badge itself shipped with the blinky demo.

## Make your own

Hardware and firmware are published on GitHub at [peterfillmore/RuxconBadge2015](https://github.com/peterfillmore/RuxconBadge2015) under the Unlicense (public domain), including a PDF assembly guide, with schematics and source in the repo's `/hardware` and `/firmware` folders. The [assembly](https://www.drkns.net/ruxcon-badge-2015-assembly/) and [programming](https://www.drkns.net/ruxcon-badge-2015-programming/) write-ups on drkns.net add step-by-step photos for soldering the board and flashing it over SWD with a Bus Pirate. Note: the GitHub repository is archived (read-only) as of March 2026.
