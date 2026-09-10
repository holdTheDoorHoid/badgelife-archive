---
title: DC503 DEF CON 26 VIP Banglet
id: dc26-dc503-def-con-26-vip-banglet
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc26
year: 2018
makers:
- name: Nisha Kumar / DC503
  url: https://nishakm.github.io/
summary: A Bluetooth-recon wrist party badge made by the DC503 (Portland) DEF CON group for DEF CON 26, with LEDs that light up and color-code nearby Bluetooth devices.
functions: 'Passive scan mode: lights LEDs proportional to nearby Bluetooth devices detected, colored by MAC address. Has additional hidden "party modes" reachable over its BLE UART service, controllable from apps like Adafruit Bluefruit LE Connect, Serial Bluetooth Terminal, or Bluetooth Terminal. Firmware is reprogrammable with provided sample code.'
look:
  colors: []
  shape: null
  themes:
  - wearable
  - bluetooth
tech:
  mcu: nRF52 (BMD-300 module)
  leds:
    count: null
    type: null
    note: Number lit corresponds to nearby Bluetooth devices detected; color keyed to device MAC address.
  display: none
  connectivity:
  - bluetooth
  - ble
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
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
  notes: Repo contains eaglecad/ (schematics and board files), sketches/ (nRF52 Arduino-style firmware), and 3dprints/ (3D-printed shell files, including hard and soft bangle shell variants). Credits multiple contributors for hardware, 3D modeling, PCB, and firmware work, with reference to Adafruit's designs and code.
links:
- label: badge.gallery/series/dc503
  url: https://badge.gallery/series/dc503
  kind: website
- label: github.com/pdxbadgers/2018-banglet
  url: https://github.com/pdxbadgers/2018-banglet
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- This appears to be the same item as dc26-503banglet (DC503 Banglet) and dc26-dc503-banglet-badge-dc26 (DC503 Banglet Badge (DC26)), which are already researched under those ids.
status: released
sources:
- kind: url
  url: https://badge.gallery/series/dc503
  title: DC503 DEF CON 26 VIP Banglet
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/pdxbadgers/2018-banglet
  title: 'GitHub - pdxbadgers/2018-banglet: DEFCON 26 DC503 VIP Banglet'
  accessed: '2026-09-10'
  note: Maker's own repo (README, Apache-2.0 license, eaglecad/sketches/3dprints folders); confirms the item is real, its purpose, and that hardware/firmware/3D files are published.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed via the maker''s own pdxbadgers/2018-banglet GitHub repo (Apache-2.0, README titled "DEFCON 26 DC503 VIP Banglet"). This is very likely the same physical item already documented in more depth (LED count of 12, BMD-300 chip, 3V LiPo battery, 100+ quantity, maker photo) at dc26-503banglet, and possibly also dc26-dc503-banglet-badge-dc26 - the archive appears to have three separate entries for one badge under different sweep-generated titles. Left LED count, exact battery, and quantity empty here since this entry''s own sources (the repo README) do not state them directly; see dc26-503banglet for those details with citations. No price was ever advertised (free party giveaway). No photo found on the sources this entry cites.'
last_modified_date: '2026-09-10'
---

The DC503 DEF CON 26 VIP Banglet is a Bluetooth-recon wrist-worn party badge made by the DC503 group (the Portland, Oregon DEF CON meetup, credited on GitHub as "pdxbadgers") for their party at DEF CON 26 in 2018. It runs a passive scan mode that lights up LEDs to indicate nearby Bluetooth devices, with LED color keyed to each device's MAC address, and hides additional "party modes" reachable over its BLE UART service from apps like Adafruit's Bluefruit LE Connect, Serial Bluetooth Terminal, or Bluetooth Terminal. It moved the badge concept from the neck to the wrist, following an earlier DC503 wagon-party badge from 2017.

Hardware (EagleCAD schematics and board files), firmware (nRF52 Arduino-style sketches), and 3D-printable bracelet shell files (both hard hinged and soft flexible variants) are published under the Apache-2.0 license in the pdxbadgers/2018-banglet GitHub repository, with credit split across several contributors for concept, PCB design, 3D design, and firmware work.

This entry is very likely the same physical badge already documented in more detail under `dc26-503banglet` (DC503 Banglet), which cites the maker's own blog post with the BMD-300 chip, 12-LED count, LiPo battery, quantity (100+), and a maker photo; a third entry, `dc26-dc503-banglet-badge-dc26`, may also refer to the same item. No price was ever advertised since it was a free party giveaway.

## Make your own

The pdxbadgers/2018-banglet repo has everything needed to build one: `eaglecad/` for the PCB schematic and board files, `sketches/` for the nRF52 firmware, and `3dprints/` for the 3D-printable bracelet shell (hard and soft variants). It is licensed Apache-2.0.
