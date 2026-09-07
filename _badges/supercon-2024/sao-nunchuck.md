---
title: SAO Nunchuck
id: supercon-2024-sao-nunchuck
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Andy Geppert
  url: https://github.com/ageppert
summary: An SAO adapter board that lets a Wii Nunchuck (or wired Classic Controller) talk I2C to a badge through a standard SAO port.
functions: Breaks out the Wii Nunchuck's I2C interface (address 0x52) to an SAO header, giving a host badge access to the Nunchuck's joystick, buttons, and accelerometer; also carries two QWIIC/STEMMA QT ports for chaining other I2C sensors.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - hardware tool
  - retro computer
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Listed on Tindie; prototype run fabricated through PCBX.com.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ageppert/SAO_Nunchuck
  firmware_url: https://github.com/ageppert/SAO_Nunchuck
  eda_tool: null
links:
- label: github.com/ageppert/SAO_Nunchuck
  url: https://github.com/ageppert/SAO_Nunchuck
  kind: repo
- label: hackaday.io/project/198000-sao-nunchuck
  url: https://hackaday.io/project/198000-sao-nunchuck
  kind: hackaday
images:
- file: assets/images/badges/supercon-2024/sao-nunchuck/387d91a023.jpg
  source: "https://github.com/ageppert/SAO_Nunchuck"
  credit: "Andy Geppert"
  caption: "SAO Nunchuck v1.0 board with a Wii Nunchuck attached"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/ageppert/SAO_Nunchuck
  title: SAO Nunchuck
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/ageppert/SAO_Nunchuck/blob/main/README.md
  title: 'ageppert/SAO_Nunchuck: README'
  accessed: '2026-09-07'
  note: 'Confirms hardware v1.0, I2C Nunchuck adapter, links to WiiChuck and NintendoExtensionCtrl libraries.'
- kind: url
  url: https://hackaday.io/project/198000-sao-nunchuck
  title: SAO Nunchuck - Hackaday.io
  accessed: '2026-09-07'
  note: 'Confirms maker (Andy Geppert), Supercon 8 (2024) SAO Contest submission (created 2024-09-17), QWIIC/STEMMA QT ports, ENIG/matte black finish, Tindie listing.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Made for the Hackaday Supercon 8 (2024) SAO Contest; event corrected from
    'other' to supercon-2024. No LEDs, MCU, or display on the board itself
    (it is a passive I2C breakout for the Nunchuck connector plus two QWIIC/STEMMA
    QT ports). Could not confirm price, quantity made, or current Tindie
    availability status without visiting the storefront directly (link not
    reachable via automated fetch in this pass). Hardware and firmware/demo
    code are both published on GitHub, so open_source is set to yes.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/sao-nunchuck/
---

The SAO Nunchuck is an add-on board by Andy Geppert (ageppert) that lets a Wii Nunchuck controller, or a wired Wii Classic Controller, plug into any badge with a standard SAO port. It bridges the Nunchuck's I2C interface (device address 0x52) straight through to the host badge, exposing the controller's joystick, buttons, and accelerometer data. The board was made for Hackaday's Supercon 8 SAO Contest in 2024, with its GitHub repository and Hackaday.io project page both dated September 2024.

Hardware-wise it is a simple, LED-free passive adapter rather than a microcontroller board: the SAO header can be mounted either along the bottom edge or on the underside of the PCB for two different physical orientations, and two QWIIC/STEMMA QT ports on the back let it also chain into the broader Sparkfun/Adafruit I2C sensor ecosystem. All signals run at 3.3V, and the board is finished in ENIG with a matte black solder mask. A small prototype batch was fabricated through PCBX.com, and the maker lists it for sale on Tindie, though this pass could not confirm current pricing or stock.

## Make your own

Hardware design files and Arduino-based demo firmware for the RP2040 are published on GitHub at github.com/ageppert/SAO_Nunchuck. The maker recommends pairing the board with either the WiiChuck library (madhephaestus) or NintendoExtensionCtrl (dmadison) to read the Nunchuck over I2C.
