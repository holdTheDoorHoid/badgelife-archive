---
title: SAOut Of This World
id: supercon-2024-saout-of-this-world
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Todd Zebert & Koppany Horvath (koppanyh)
  url: https://github.com/toddzebert
summary: A cartoonish flying-saucer-with-alien SAO built around the CH32V003F4U6 microcontroller, with 5 white star LEDs, 16 WS2812 addressable LEDs, two buttons and I2C target control, designed for the Supercon 2024 SAO Contest (deadline missed) and handed out as a run of 10 at Supercon 2024.
functions: Two buttons cycle through LED light effects; holding the left button enters a brightness-adjustment mode. The board also exposes an I2C target interface so a host badge can read/set effects and colors (partially implemented in firmware).
look:
  colors: []
  shape: spaceship
  themes:
  - sci-fi
  - space
  - robot
tech:
  mcu: CH32V003F4U6
  leds:
    count: 23
    type: WS2812
    note: 5 WS2812 in the upper trim, 16 WS2812 in the lower trim, plus 2 standard "sense" LEDs wired to sink/source current for sensing.
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '10'
  availability: free
  distribution:
  - free_drop
  where: Handed out in person at Supercon 2024 in Pasadena, CA; a run of 10 units.
make_your_own:
  open_source: true
  hardware_url: https://github.com/toddzebert/SAOut-Of-This-World/tree/main/hardware
  firmware_url: https://github.com/toddzebert/SAOut-Of-This-World/tree/main/firmware
  eda_tool: null
links:
- label: hackaday.io/project/202615-saout-of-this-world
  url: https://hackaday.io/project/202615-saout-of-this-world
  kind: hackaday
  archived: https://web.archive.org/web/20260418184948/https://hackaday.io/project/202615-saout-of-this-world
- label: github.com/toddzebert/SAOut-Of-This-World
  url: https://github.com/toddzebert/SAOut-Of-This-World
  kind: repo
- label: github.com/toddzebert/SAOut-Of-This-World/blob/main/hardware/readme.md
  url: https://github.com/toddzebert/SAOut-Of-This-World/blob/main/hardware/readme.md
  kind: repo
- label: github.com/toddzebert/SAOut-Of-This-World/blob/main/firmware/readme.md
  url: https://github.com/toddzebert/SAOut-Of-This-World/blob/main/firmware/readme.md
  kind: repo
images:
- file: assets/images/badges/supercon-2024/saout-of-this-world/25dad983cf.png
  source: https://hackaday.io/project/202615-saout-of-this-world
  credit: Todd Zebert & Koppany Horvath
  caption: SAOut Of This World SAO, flying-saucer-with-alien design
  archived: https://web.archive.org/web/20260418184948/https://hackaday.io/project/202615-saout-of-this-world
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/202615-saout-of-this-world
  title: SAOut Of This World | Hackaday.io
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260418184948/https://hackaday.io/project/202615-saout-of-this-world
- kind: url
  url: https://hackaday.io/project/202615-saout-of-this-world
  title: SAOut Of This World | Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed makers, MCU, LED counts, buttons, I2C, 2024 Supercon SAO Contest deadline miss, run of 10 handed out at Supercon 2024 in Pasadena.
  archived: https://web.archive.org/web/20260418184948/https://hackaday.io/project/202615-saout-of-this-world
- kind: url
  url: https://github.com/toddzebert/SAOut-Of-This-World
  title: toddzebert/SAOut-Of-This-World on GitHub
  accessed: '2026-09-07'
  note: Confirmed open-source hardware+firmware under a modified MIT license; koppanyh designed the PCB/artwork, Todd Zebert wrote firmware.
- kind: url
  url: https://github.com/toddzebert/SAOut-Of-This-World/blob/main/hardware/readme.md
  title: hardware/readme.md
  accessed: '2026-09-07'
  note: Confirmed CH32V003F4U6 pinout, two sense LEDs, two ground-referenced buttons, dedicated I2C SDA/SCL, SAO connector, USART pads, Neopixel connector, SWIO programming pad; no EDA tool or BOM/gerbers link given.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (maker, MCU, LED counts, contest-deadline-miss story, run of 10 at Supercon 2024) confirmed consistently across the Hackaday.io project page and the GitHub repo/hardware readme. Price is not applicable since it was a free giveaway, not sold; get_one.price left blank accordingly. EDA tool, BOM, and gerbers links were not stated in the hardware readme, so left null/empty. No duplicate found in existing_titles.txt.
last_modified_date: '2026-09-07'
---

SAOut Of This World is an SAO shaped like a cartoonish flying saucer beaming up a wide-eyed alien, built by Todd Zebert (firmware) and Koppany Horvath / koppanyh (PCB design and artwork). It runs on a CH32V003F4U6, a low-cost RISC-V microcontroller, and lights up with 5 WS2812 LEDs in the saucer's upper trim and 16 more in the lower trim, plus a pair of "sense" LEDs wired so the MCU can both source and sink current through them for input sensing. Two buttons let the wearer cycle through light effects, and holding the left button drops into a brightness-adjustment mode.

The board was originally built for the 2024 Supercon SAO Contest but missed that year's submission deadline; the makers finished it anyway and brought a run of 10 units to hand out in person at Supercon 2024 in Pasadena, CA in November 2024. Beyond its own animations, the SAO exposes an I2C target interface so a host badge can read or set its effects and colors, though the makers describe that host-control path as only partially implemented.

Hardware and firmware are both published on GitHub under a modified MIT license. The hardware readme documents the CH32V003F4U6 pinout in detail — SAO connector, a Neopixel (MOSI-based) output, USART pads, and an SWIO programming pad — though it does not specify which EDA tool was used or link a bill of materials or Gerber files.
