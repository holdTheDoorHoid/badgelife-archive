---
title: Hackaday Supercon 2024 SAO Badge (Supercon 8 Badge)
id: supercon-2024-hackaday-supercon-2024-sao-badge-supercon-8-badge
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2024
year: 2024
makers:
- name: Hackaday
  url: https://hackaday.com
summary: The official badge for Hackaday Supercon 8 (2024), built as a hub for six SAO add-ons rather than a badge with SAO ports bolted on as an afterthought.
functions: Six independent SAO slots each with their own I2C bus and GPIO access, driven by a Raspberry Pi Pico W over MicroPython; ships with four starter add-ons (a capacitive touch wheel, an LED spiral petal matrix, a blank protoboard petal, and an I2C proto petal built around a CH32V003) and can talk badge-to-badge over MQTT.
look:
  colors: []
  shape: radial
  themes:
  - hardware tool
  - learn to solder
  - radio
tech:
  mcu: Raspberry Pi Pico W (RP2040)
  leds: null
  display: none
  connectivity:
  - wifi
  - bluetooth
  - i2c
  battery: AA battery, with pads for external power
  sao_version: v1
  sao_ports: 6
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of Hackaday Supercon 8 (2024); design files published for anyone to build their own.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  firmware_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  eda_tool: null
links:
- label: hackaday.com/2024/10/22/the-2024-hackaday-supercon-sao-badge-reveal
  url: https://hackaday.com/2024/10/22/the-2024-hackaday-supercon-sao-badge-reveal/
  kind: article
- label: Hack-a-Day/2024-Supercon-8-Add-On-Badge (GitHub)
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2024/hackaday-supercon-2024-sao-badge-supercon-8-badge/418bf4f81d.jpg
  source: "https://hackaday.com/2024/10/22/the-2024-hackaday-supercon-sao-badge-reveal/"
  credit: "Hackaday"
  caption: "Supercon 8 SAO badge, front, six-petal radial layout"
- file: assets/images/badges/supercon-2024/hackaday-supercon-2024-sao-badge-supercon-8-badge/7c2170ef4d.jpg
  source: "https://hackaday.com/2024/10/22/the-2024-hackaday-supercon-sao-badge-reveal/"
  credit: "Hackaday"
  caption: "Supercon 8 SAO badge, back side"
contact: {}
notes:
- Six-SAO-port radial 'electronic flower' design
status: released
sources:
- kind: url
  url: https://hackaday.com/2024/10/22/the-2024-hackaday-supercon-sao-badge-reveal/
  title: Hackaday Supercon 2024 SAO Badge (Supercon 8 Badge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''Hackaday Supercon 2024''.'
- kind: url
  url: https://hackaday.com/2024/10/22/the-2024-hackaday-supercon-sao-badge-reveal/
  title: "The 2024 Hackaday Supercon SAO Badge Reveal"
  accessed: '2026-09-07'
  note: 'Confirmed Pico W MCU, six SAO slots, AA battery, four starter add-ons, free distribution to attendees, and design-file release.'
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  title: "Hack-a-Day/2024-Supercon-8-Add-On-Badge"
  accessed: '2026-09-07'
  note: 'Confirmed open hardware/firmware repo; CH32V003 chip used on the I2C proto petal add-on; badge described as "a simple hub for six SAOs".'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: PCB solder-mask color, exact LED count/part number, board dimensions, and quantity produced are not stated by either the Hackaday article or the GitHub repo, so those fields are left empty rather than guessed. The GitHub README also notes reuse at "2025 Hackaday Europe."
last_modified_date: '2026-09-07'
---

The Supercon 8 badge, given to attendees of Hackaday Supercon in Pasadena in November 2024, was designed around a simple idea taken to its logical extreme: instead of a badge with one or two SAO headers as an afterthought, this one is built as a hub for six SAO ("Simple/Shitty Add-On") slots arranged radially, each with its own I2C bus and direct GPIO access. A Raspberry Pi Pico W runs the show over MicroPython, giving the badge Wi-Fi and Bluetooth for badge-to-badge communication (including over MQTT), plus three front buttons and power from a single AA battery with pads for external power.

It ships with four starter "petal" add-ons that plug into those SAO slots: a capacitive touch wheel (designed with contributions from Todbot), a spiral LED matrix petal (with design input from Voja Antonic), a blank protoboard petal for building your own add-on, and an I2C proto petal built around a CH32V003 RISC-V microcontroller for anyone who wants to make an active, programmable SAO. Hardware files, firmware, and documentation for both the main badge and the starter petals are published on GitHub, and the badge was given free to Supercon 8 attendees rather than sold.

## Make your own

Hardware, MicroPython firmware, and build documentation for the main badge and its four starter petals are published at github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge, including a walkthrough for building custom I2C devices on the proto petal.
