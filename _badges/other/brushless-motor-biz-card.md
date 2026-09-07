---
title: Brushless Motor Biz Card
id: other-brushless-motor-biz-card
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2024
makers:
- name: ageppert
  url: https://github.com/ageppert
summary: 'A US-business-card-sized PCB that lets you wind and run your own working brushless motor, with an ATmega328PB, capacitive touch controls, and a QWIIC/SAO port.'
functions: 'Educational kit: you hand-wind the PCB-etched motor coils, then the onboard ATmega328PB drives it with open-loop sine-wave commutation via three half-bridge FET driver circuits. Capacitive touch buttons (mode, +, -, select) and an RGB LED select and indicate motor modes; the front silkscreen doubles as an illustrated schematic with labeled test points.'
look:
  colors: []
  shape: card
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: ATmega328PB
  leds:
    count: 1
    type: RGB
    note: single RGB indicator LED for mode/status
  display: none
  connectivity:
  - i2c
  - usb
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
  open_source: 'yes'
  hardware_url: https://github.com/ageppert/Brushless-Motor-Biz-Card
  firmware_url: https://github.com/ageppert/Brushless-Motor-Biz-Card
  eda_tool: KiCad
links:
- label: github.com/ageppert/Brushless-Motor-Biz-Card
  url: https://github.com/ageppert/Brushless-Motor-Biz-Card
  kind: repo
- label: Hackaday.io project page
  url: https://hackaday.io/project/196576
  kind: hackaday
images:
  - file: assets/images/badges/other/brushless-motor-biz-card/dc0c68d6c7.jpg
    source: "https://github.com/ageppert/Brushless-Motor-Biz-Card"
    credit: "ageppert"
    caption: "Front of the Brushless Motor Business Card, showing the PCB motor, driver FETs, capacitive buttons and RGB LED"
  - file: assets/images/badges/other/brushless-motor-biz-card/94e1e86727.jpg
    source: "https://github.com/ageppert/Brushless-Motor-Biz-Card"
    credit: "ageppert"
    caption: "Back of the Brushless Motor Business Card, showing the schematic silkscreen and test points"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- 'Made for Hackaday.io''s 2024 Business Card Contest, an online contest rather than a physical convention; no matching event id exists in events.yml, so event is left as ''other''.'
status: released
sources:
- kind: url
  url: https://github.com/ageppert/Brushless-Motor-Biz-Card
  title: Brushless Motor Biz Card
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://hackaday.io/project/196576
  title: Brushless Motor and Driver Business Card Kit (Hackaday.io project 196576)
  accessed: '2026-09-07'
  note: 'Primary source for MCU (ATmega328PB), features (capacitive touch, RGB LED, QWIIC/I2C port, half-bridge FET drivers), dimensions, KiCad/Inkscape/OnShape tooling, 2024 Business Card Contest entry, and open-source status.'
- kind: url
  url: https://raw.githubusercontent.com/ageppert/Brushless-Motor-Biz-Card/main/README.md
  title: Brushless-Motor-Biz-Card README
  accessed: '2026-09-07'
  note: 'Confirmed project description and HWV0.1 prototype status; no pricing/quantity given.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No price, quantity made, or distribution channel was found anywhere in the repo, README, or Hackaday.io page — it reads as a maker''s open-source design/contest entry rather than something sold, so get_one fields are left empty/unknown. No SAO header pin count or version was stated (it exposes an I2C/QWIIC port that can drive an SAO-style OLED, but is not itself an SAO). No LED count/type beyond a single RGB status LED was documented.'
last_modified_date: '2026-09-07'
---

The Brushless Motor Business Card is an open-source educational PCB by GitHub/Hackaday.io maker ageppert, built to standard US business-card dimensions (2.0 x 3.5 in) with a working brushless motor integrated into the board itself. The builder hand-winds the PCB-etched stator coils (selectable delta or wye configuration via solder jumpers), and an onboard ATmega328PB microcontroller drives the three-phase motor through discrete half-bridge FET circuits using open-loop sine-wave commutation. The card was entered in Hackaday.io's 2024 Business Card Contest, an online design contest rather than a physical convention, which is why this entry keeps the generic "other" event.

Beyond the motor, the card carries capacitive-touch mode/+/-/select buttons, a single RGB status LED, an I2C/QWIIC port that can drive an add-on SAO-style OLED display, an R/C-style input with tachometer output, optional external motor/hall-sensor connections, and an ISP header for reprogramming. The front silkscreen is illustrated as a schematic with labeled test points, turning the card itself into a teaching aid for how the driver circuit works.

All hardware (KiCad) and firmware design files are published on GitHub, with mechanical design done in OnShape; the maker describes the project as fully open source. No information was found on price, quantity produced, or any sale/distribution channel, suggesting this has circulated as a shared open-source design and contest entry rather than a batch sold or given away at an event.
