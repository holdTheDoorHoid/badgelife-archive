---
title: DC503 Banglet
id: dc26-503banglet
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc26
year: 2018
makers:
- name: Nisha Kumar
  url: https://nishakm.github.io/
summary: A Bluetooth-recon party bracelet made for the DC503 (Portland) DEF CON 26 meetup, with 12 LEDs that light up and color-code nearby Bluetooth devices.
functions: 'Passive scan mode: lights a number of LEDs proportional to nearby Bluetooth devices detected, colored by MAC address. Has additional hidden "party modes" reachable over its BLE UART service, controllable from apps like Adafruit Bluefruit LE Connect, Serial Bluetooth Terminal, or Bluetooth Terminal. Firmware is reprogrammable with provided sample code.'
look:
  colors: []
  shape: null
  themes:
  - wearable
  - bluetooth
tech:
  mcu: BMD-300
  leds:
    count: 12
    type: null
    note: Number lit corresponds to nearby Bluetooth devices detected; color keyed to device MAC address.
  display: none
  connectivity:
  - bluetooth
  - ble
  battery: 3V LiPo, USB rechargeable
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '100+'
  availability: unknown
  distribution:
  - free_drop
  where: Given out to attendees of the DC503 (Portland DEF CON group) party at DEF CON 26, 2018.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/pdxbadgers/2018-banglet
  firmware_url: https://github.com/pdxbadgers/2018-banglet
  eda_tool: EagleCAD
  license: Apache-2.0
  notes: Repo contains eaglecad/ (schematics and board files), sketches/ (firmware, built on the Adafruit Bluefruit Feather architecture), and 3dprints/ (3D-printed shell files). Credits multiple contributors for hardware, 3D modeling, PCB, and firmware work, with reference to Adafruit's designs and code.
links:
- label: github.com/nishakm/blinkybracelet/tree/master/banglet
  url: https://github.com/nishakm/blinkybracelet/tree/master/banglet
  kind: repo
- label: github.com/pdxbadgers/2018-banglet
  url: https://github.com/pdxbadgers/2018-banglet
  kind: repo
- label: 'nishakm.github.io: DC503 Banglet overview'
  url: https://nishakm.github.io/things/dc503banglet/
  kind: article
images:
- file: assets/images/badges/dc26/503banglet/776b23e46b.jpg
  source: "https://nishakm.github.io/things/dc503banglet/"
  credit: "Nisha Kumar"
  caption: "3D-printed banglet shell design"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'Sheet listed the maker as "Nisha K."; her own site gives her full name as Nisha Kumar.'
status: released
sources:
- kind: url
  url: https://github.com/nishakm/blinkybracelet/tree/master/banglet
  title: 503Banglet
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''other''.'
- kind: url
  url: https://nishakm.github.io/things/dc503banglet/
  title: 'Nisha Kumar: DC503 Banglet overview'
  accessed: '2026-09-07'
  note: Maker's own write-up; source of the DEF CON 26 (2018) date, feature description, hardware (BMD-300, 12 LEDs, LiPo battery), quantity (100+), and images.
- kind: url
  url: https://github.com/pdxbadgers/2018-banglet
  title: pdxbadgers/2018-banglet
  accessed: '2026-09-07'
  note: The actual hardware/firmware repo for the 2018 build (distinct from the earlier nishakm/blinkybracelet prototype repo); confirms Apache-2.0 license and file contents (eaglecad, sketches, 3dprints).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own blog post (nishakm.github.io) is the primary source and matches the pdxbadgers/2018-banglet repo it links to; the entry''s original link (nishakm/blinkybracelet) appears to be an earlier/related prototype repo rather than the final 2018 party build. Price was never advertised (free party giveaway); exact LED type (WS2812B vs discrete) and PCB colors not stated in sources found. Could not save a maker photo of the banglet lit up in scan mode - the linked Twitter/X image (pbs.twimg.com/media/DjT3Kg5VsAAS8bW.jpg) returned 404 (dead media link).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/503banglet/
---

The DC503 Banglet is a Bluetooth-recon party bracelet made by Nisha Kumar for the DC503 group (the Portland, Oregon DEF CON meetup) to hand out at their party during DEF CON 26 in 2018. Built around a Rigado BMD-300 module on the Adafruit Bluefruit Feather architecture, it runs in a passive scan mode where its 12 LEDs light up to indicate how many nearby Bluetooth devices it detects, with LED color keyed to each device's MAC address. It also hides additional "party modes" accessible over its BLE UART service, controllable from phone apps such as Adafruit's Bluefruit LE Connect, Serial Bluetooth Terminal, or Bluetooth Terminal, and the firmware is reprogrammable with sample code the team provided.

More than 100 units were produced and given away free to party attendees; no price was ever advertised since it was not sold. The hardware (EagleCAD schematics and board files), firmware (Arduino-style sketches), and a 3D-printable bracelet shell are all published under the Apache-2.0 license in the pdxbadgers/2018-banglet GitHub repository, with credit split across several contributors for the PCB, firmware, and 3D design work. The entry's original link, nishakm/blinkybracelet, appears to be an earlier or related prototype repository by the same maker rather than the final 2018 party build documented on her blog.

## Make your own

The pdxbadgers/2018-banglet repo has everything needed to build one: `eaglecad/` for the PCB schematic and board files, `sketches/` for the BMD-300 firmware (based on Adafruit's Bluefruit Feather examples), and `3dprints/` for the 3D-printable bracelet shell. It is licensed Apache-2.0.
