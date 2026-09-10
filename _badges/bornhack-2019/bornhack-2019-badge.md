---
title: BornHack 2019 badge
id: bornhack-2019-bornhack-2019-badge
layout: badge
parent: Bornhack 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2019
year: 2019
makers:
- name: BornHack
  url: https://bornhack.dk/
summary: A lightsaber-handle-shaped conference badge for BornHack 2019, built around a SiLabs Happy Gecko MCU with a 240x240 color display, joystick, IR link and microSD slot.
functions: Shows the event schedule, a button test app, a bitmap image viewer, and an IR dump/communication tool; the main menu can be extended with custom C apps.
look:
  colors: []
  shape: other
  themes:
  - sci-fi
  - hardware tool
tech:
  mcu: EFM32HG322F64G (SiLabs Happy Gecko, Cortex-M0+)
  leds:
    count: null
    type: discrete
    note: Red and blue indicator LEDs, including one next to the BOOT button.
  display: 240x240 color LCD (ST7789 controller, 6-bit per channel)
  connectivity:
  - ir
  - usb
  - i2c
  - uart
  inputs:
  - joystick
  - buttons
  battery: 2x AA
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: free
  price_usd: null
  quantity: approximately 500
  availability: free
  distribution:
  - free_drop
  where: Given to attendees at BornHack 2019; assembled on-site by volunteers.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2019/tree/hardware
  firmware_url: https://github.com/bornhack/badge2019
  eda_tool: KiCad
  notes: Firmware is GPL-3.0 and built on the geckonator library; hardware design files (schematic and PCB) are on the hardware branch.
links:
- label: github.com/bornhack/badge2019
  url: https://github.com/bornhack/badge2019
  kind: repo
  archived: https://web.archive.org/web/20251125035429/https://github.com/bornhack/badge2019
- label: 'Hands-On: BornHack''s Light Sabre Badge (Hackaday)'
  url: https://hackaday.com/2019/09/13/hands-on-bornhacks-light-sabre-badge/
  kind: article
  archived: https://web.archive.org/web/20260316055747/https://hackaday.com/2019/09/13/hands-on-bornhacks-light-sabre-badge/
images:
- file: assets/images/badges/bornhack-2019/bornhack-2019-badge/a9c5f6c2e2.jpg
  source: https://hackaday.com/2019/09/13/hands-on-bornhacks-light-sabre-badge/
  credit: Hackaday
  caption: Front of the BornHack 2019 badge, showing the lightsaber-inspired handle and 240x240 color display
  archived: https://web.archive.org/web/20260316055747/https://hackaday.com/2019/09/13/hands-on-bornhacks-light-sabre-badge/
- file: assets/images/badges/bornhack-2019/bornhack-2019-badge/e458516dd3.jpg
  source: https://hackaday.com/2019/09/13/hands-on-bornhacks-light-sabre-badge/
  credit: Hackaday
  caption: Back of the BornHack 2019 badge showing the AA battery holders and exposed serial/I2C pads
  archived: https://web.archive.org/web/20260316055747/https://hackaday.com/2019/09/13/hands-on-bornhacks-light-sabre-badge/
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2019
  title: BornHack 2019 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''bornhack-2019''.'
  archived: https://web.archive.org/web/20251125035429/https://github.com/bornhack/badge2019
- kind: url
  url: https://github.com/bornhack/badge2019/tree/hardware
  title: bornhack/badge2019 at hardware
  accessed: '2026-09-07'
  note: 'Hardware branch README: chip, display, SAO v1.69bis expansion header, KiCad files, double-sided PCB with battery clips on back.'
- kind: url
  url: https://hackaday.com/2019/09/13/hands-on-bornhacks-light-sabre-badge/
  title: 'Hands-On: BornHack''s Light Sabre Badge'
  accessed: '2026-09-07'
  note: Form factor, designer name, button/joystick layout, 2xAA battery, IR emitter/receiver detail, ~500 units assembled on-site by volunteers, given free to attendees, front/back photos.
  archived: https://web.archive.org/web/20260316055747/https://hackaday.com/2019/09/13/hands-on-bornhacks-light-sabre-badge/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Designer credited by Hackaday as Thomas Flummer. Exact LED count and PCB solder-mask color not stated in sources found; left empty rather than guessed. No price since it was included with conference attendance rather than sold separately.
last_modified_date: '2026-09-07'
model:
  file: assets/models/bornhack-2019/bornhack-2019-badge.glb
  method: kicad
  source_file: bh_2019_badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 413380
---

The BornHack 2019 badge was shaped like a lightsaber handle, designed by Thomas Flummer, so it sits comfortably in the hand with its electronics kept away from clothing. Like the 2017 and 2018 badges before it, it uses a SiLabs "Happy Gecko" EFM32HG322F64G microcontroller, this time paired with a 240x240 pixel color LCD (ST7789 controller). Three thumb-reachable buttons sit along the left edge next to a four-way joystick and two extra buttons, and the badge also carries a microSD card slot, a basic IR emitter/receiver pair, a micro-USB port, and a 6-pin shitty-add-on (v1.69bis) expansion header with I2C and two GPIO pins broken out. Power comes from two AA batteries held in clips on the back of the double-sided PCB, which also exposes serial and I2C test pads.

Around 500 badges were assembled on-site at the event by volunteer labor after component sourcing delays pushed the build later than planned, and finished units were given to BornHack 2019 attendees rather than sold. The stock firmware, built on the "geckonator" library BornHack has reused across badge years, ships with a menu of small apps (a button tester, a bitmap viewer, an IR dump tool, and the event schedule) and is designed so hackers can drop in their own C source files and have them picked up by the build automatically.

## Make your own

The firmware (GPL-3.0) and KiCad hardware design files are both published on GitHub, with the PCB/schematic kept on a separate `hardware` branch from the code. To build the firmware, clone the repo, install an `arm-none-eabi-gcc` toolchain, run `make`, then flash the resulting `code.bin` over USB by holding the badge's BOOT button while plugging it in.
