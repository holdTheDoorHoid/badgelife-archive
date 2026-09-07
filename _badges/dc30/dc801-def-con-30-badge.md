---
title: SAO Modem 1.69bis
id: dc30-dc801-def-con-30-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: hamster
  url: https://github.com/hamster
summary: A DEF CON 30 SAO shaped as a throwback to external Courier modems, with six LEDs that blink for power and for I2C/GPIO bus activity rather than any real network connection.
functions: 'Six status LEDs mimic a 1990s modem''s lights: AA (power, lit when 3.3V is present), OH (flashes on I2C SCL activity), SD (flashes on I2C SDA activity), RTS (flashes on GPIO1 activity), CTS (flashes on GPIO2 activity), and SYN (wired to a spare pad the builder can use for anything). It does not actually communicate with anything; it is purely decorative bus-activity blinky.'
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
tech:
  mcu: none
  leds:
    count: 6
    type: discrete
    note: AA/OH/SD/RTS/CTS/SYN, driven directly by power and I2C/GPIO signal lines rather than a microcontroller
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: $8.00
  price_usd: 8.0
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold through DEF CON's official online shop (shop.defcon.org); the product listing has since been taken down.
make_your_own:
  open_source: true
  hardware_url: https://github.com/hamster/defcon30/tree/main/modem
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/hamster/defcon30
  url: https://github.com/hamster/defcon30
  kind: repo
- label: DEF CON 30 SAO Modem (DEF CON shop, archived)
  url: http://web.archive.org/web/20241210024140/https://shop.defcon.org/products/def-con-30-sao-modem
  kind: store
- label: DCZia '30-in-One' DEF CON 30 Badge (hamster's Tindie shop, snurkle engineering)
  url: https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/
  kind: store
images:
- file: assets/images/badges/dc30/dc801-def-con-30-badge/6f2e621e46.jpg
  source: https://github.com/hamster/defcon30
  credit: hamster
  caption: SAO Modem 1.69bis, assembled and lit
- file: assets/images/badges/dc30/dc801-def-con-30-badge/f86a1d1087.jpg
  source: https://github.com/hamster/defcon30
  credit: hamster
  caption: SAO Modem 1.69bis close-up of the six status LEDs
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- 'Corrected from the sheet: the maker is "hamster" (GitHub/Twitter handle, also sells as "snurkle engineering" on Tindie), not DC801. The repo has no connection to the DC801 hacker group.'
- 'The linked repo actually covers two separate DEF CON 30 SAOs by the same maker: this one (SAO Modem 1.69bis) and a second, "SAO Jack," a learn-to-solder kit with DEF CON-themed artwork. Jack was not researched here; see other_items_found.'
status: released
sources:
- kind: url
  url: https://github.com/hamster/defcon30
  title: DC801 DEF CON 30 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc30''.'
- kind: url
  url: https://raw.githubusercontent.com/hamster/defcon30/master/README.md
  title: hamster/defcon30 README
  accessed: '2026-09-07'
  note: Identified the repo as two separate SAOs (Modem 1.69bis and Jack) by maker "hamster", not DC801.
- kind: url
  url: https://raw.githubusercontent.com/hamster/defcon30/master/modem/README.md
  title: SAO Modem 1.69bis README
  accessed: '2026-09-07'
  note: LED functions, no-MCU design, SAO connector assembly notes.
- kind: url
  url: http://web.archive.org/web/20241210024140/https://shop.defcon.org/products/def-con-30-sao-modem
  title: DEF CON 30 SAO Modem – DEF CON Merchandise (archived)
  accessed: '2026-09-07'
  note: Confirms this SAO was sold officially through DEF CON's shop at $8.00; live page now 404s.
- kind: url
  url: https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/
  title: DCZia '30-in-One' defcon 30 Badge - snurkle engineering (hamster)
  accessed: '2026-09-07'
  note: Confirms hamster's other alias (snurkle engineering, Sandy UT) and general SAO/badge activity; unrelated product.
- kind: url
  url: https://api.github.com/repos/hamster/defcon30/contents/modem
  title: hamster/defcon30 modem directory listing
  accessed: '2026-09-07'
  note: Confirms KiCad source files (schematic, PCB, BOM) are published for the hardware.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Sold officially through the DEF CON shop, which confirms the item and price, but quantity made and exact sell-out date are not published anywhere found. SAO version (4-pin vs 6-pin) is not stated in the README or repo and was left null rather than guessed. PCB color/finish not visible clearly enough in the available photos to state with confidence, so look.colors was left empty. A second SAO from the same repo and maker ("SAO Jack") was not written up as part of this entry; it deserves its own entry.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc30/dc801-def-con-30-badge.glb
  method: gerber
  source_file: modem/modem-panel.kicad_pcb
  generated: '2026-09-07'
  bytes: 467284
  size_mm:
  - 273.4
  - 123.6
---

This SAO was one of two DEF CON 30 add-ons designed by a maker known as "hamster" (who also sells hardware as "snurkle engineering" on Tindie, based in Sandy, UT). Styled as a miniature homage to the external Courier modems of the 1990s, it carries six LEDs labeled AA, OH, SD, RTS, CTS, and SYN, echoing the blinking status lights of a real modem. None of them actually indicate network activity; instead they light up from the host badge's power rail and from activity on the I2C and GPIO lines the SAO taps into, with a spare pad (SYN) left for the builder to wire up however they like. There is no microcontroller on the board.

The SAO Modem 1.69bis was sold through DEF CON's own online shop for $8, alongside the maker's original GitHub repository, which also publishes the KiCad schematic, PCB layout, and bill of materials under an MIT license. The shop listing has since been taken down, and no published figures describe how many were made or sold.

The same repository and maker also produced a second, unrelated DEF CON 30 SAO called "SAO Jack," a simple learn-to-solder kit built around four LEDs and DEF CON-themed artwork; that item was not researched as part of this entry and would warrant a separate one.
