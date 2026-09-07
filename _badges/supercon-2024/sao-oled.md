---
title: SAO OLED
id: supercon-2024-sao-oled
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Andy Geppert
  url: https://hackaday.io/andy-geppert
summary: A passive SAO that adds a 0.96" 128x64 monochrome I2C OLED display to a badge or project, with a pass-through SAO header and a QWIIC/STEMMA QT port.
functions: Displays instructions, information, or status text/graphics driven by the host badge's microcontroller over I2C; has no onboard MCU of its own.
look:
  colors: []
  shape: rectangle
  themes: []
tech:
  mcu: none
  leds: null
  display: 0.96" OLED (128x64 monochrome, I2C)
  connectivity:
  - i2c
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold as a kit through core64.io (Andy Geppert / MachineIdeas.com); creator brought units to Supercon.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ageppert/SAO_OLED
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/194077-sao-oled
  url: https://hackaday.io/project/194077-sao-oled
  kind: hackaday
- label: SAO_OLED (GitHub)
  url: https://github.com/ageppert/SAO_OLED
  kind: repo
- label: core64.io
  url: https://core64.io
  kind: website
images:
- file: assets/images/badges/supercon-2024/sao-oled/3f282e6585.jpg
  source: "https://hackaday.io/project/194077-sao-oled"
  credit: "Andy Geppert"
  caption: "SAO OLED add-on board with 0.96\" I2C OLED display"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/194077-sao-oled
  title: SAO OLED
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 SAO Contest entry''.'
- kind: url
  url: https://hackaday.io/project/194077-sao-oled
  title: SAO OLED
  accessed: '2026-09-07'
  note: 'Maker, contest (Supercon 8 SAO Contest, submitted 12/15/2023), features, connectors, and no-onboard-MCU design confirmed.'
- kind: url
  url: https://github.com/ageppert/SAO_OLED
  title: ageppert/SAO_OLED
  accessed: '2026-09-07'
  note: 'Repo contains an "Electronic Design" folder and assembly instruction images; no gerbers, firmware, or BOM visible in the top-level listing, so open_source is marked partial rather than yes.'
- kind: url
  url: https://core64.io
  title: Core64 / MachineIdeas.com
  accessed: '2026-09-07'
  note: 'Confirms SAO OLED is one of Andy Geppert''s (MachineIdeas.com) kits alongside Core64, Core64c, and Core16; no price or quantity listed on the page as fetched.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This was made for the Supercon 8 (2024) SAO Contest, not Supercon 2025 — see event_corrected_to. No price, quantity, or LED info found on any source. The GitHub repo has an "Electronic Design" folder but its contents (gerbers/schematic files) were not individually confirmed, so open_source is "partial" rather than "yes". No firmware repo found (device has no onboard MCU; it is driven by the host via the Adafruit SSD1306 library).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2025/sao-oled/
---

The SAO OLED is a simple add-on board by Andy Geppert (MachineIdeas.com, maker of the Core64/Core16 badge kits) that gives any badge or project a small display without needing its own microcontroller. It carries a 0.96" 128x64 monochrome I2C OLED and is driven directly by the host device, typically using the Adafruit SSD1306 Arduino library. It was submitted to the Supercon 8 (2024) SAO Contest in December 2023, and Geppert brought assembled units to that year's Supercon.

Besides the standard SAO header, the board includes a pass-through SAO connector so another add-on can be stacked behind it, plus a QWIIC/STEMMA QT port for connecting other I2C peripherals. It's sold as a kit through core64.io alongside Geppert's other Core-series boards.

## Make your own

Hardware files live in the [SAO_OLED GitHub repo](https://github.com/ageppert/SAO_OLED), which includes an "Electronic Design" folder and two assembly-instruction images; no separate firmware is needed since the display is controlled entirely from the host badge.
