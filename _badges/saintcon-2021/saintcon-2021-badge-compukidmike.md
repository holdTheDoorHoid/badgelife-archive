---
title: SAINTCON 2021 badge (compukidmike)
id: saintcon-2021-saintcon-2021-badge-compukidmike
layout: badge
parent: Saintcon 2021
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2021
year: 2021
makers:
- name: compukidmike
  url: https://github.com/compukidmike
- name: Professor_Plum
- name: Sodium_Hydrogen
summary: An electronic conference badge for SAINTCON 2021 styled as a combination padlock with a working, openable shackle, built around a round LCD and NFC.
functions: NFC read/write of tags, card emulation, contact sharing, and item trading between badges; displays imagery on a round LCD.
look:
  colors: []
  shape: null
  themes:
  - security
  - puzzle
form_factor: pcb badge
tech:
  mcu: ATSAME53J18A
  leds: null
  display: round LCD
  connectivity:
  - nfc
  - usb
  battery: USB and battery, with power switch
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/compukidmike/Saintcon2021
  firmware_url: https://github.com/compukidmike/Saintcon2021
  eda_tool: null
links:
- label: github.com/compukidmike/Saintcon2021
  url: https://github.com/compukidmike/Saintcon2021
  kind: repo
images:
- file: assets/images/badges/saintcon-2021/saintcon-2021-badge-compukidmike/855f61a472.jpg
  source: https://github.com/compukidmike/Saintcon2021
  credit: compukidmike
  caption: Badge front, unlocked (shackle open)
- file: assets/images/badges/saintcon-2021/saintcon-2021-badge-compukidmike/97f385edc8.jpg
  source: https://github.com/compukidmike/Saintcon2021
  credit: compukidmike
  caption: Badge front, locked (shackle closed)
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2021
  title: SAINTCON 2021 badge (compukidmike)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''saintcon-2021''.'
- kind: url
  url: https://github.com/compukidmike/Saintcon2021
  title: compukidmike/Saintcon2021 README
  accessed: '2026-09-07'
  note: Primary source for description, makers, MCU, NFC controller, display, storage, power, firmware/bootloader details, and badge photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No price, quantity made, or distribution method found (this appears to be an attendee/staff badge rather than a sold item, but the repo does not say explicitly). No LED info found. Web search budget was exhausted this session, so only the GitHub repo itself was checked; a Hackaday.io writeup or forum thread, if one exists, was not searched.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2021/saintcon-2021-badge-compukidmike.glb
  method: kicad
  source_file: Hardware/Saintcon2021/Saintcon2020.kicad_pcb
  generated: '2026-09-10'
  bytes: 125428
---

The SAINTCON 2021 badge, built by compukidmike with Professor_Plum and Sodium_Hydrogen, takes the shape of a combination padlock complete with a shackle that physically opens. Under the hood it runs an Microchip ATSAME53J18A microcontroller alongside an ST25R95 NFC controller, letting the badge read and write NFC tags, emulate cards, share contact info, and trade items with other badges over NFC. A round LCD display sits on the front, backed by an 8MB SPI flash chip used to store the images shown on it.

The physical design was demanding: the team packed the badge's electronics into a five-board, four-layer-thick stack, with only about 1mm of clearance beneath the 2.2mm round LCD, all while working through chip shortages that affected component choices. The badge can be powered over USB or from a battery via an onboard power switch, and includes a USB mass-storage bootloader for reflashing, along with Python tooling for managing the flash-based image assets.

The full hardware design and firmware are published on GitHub (123 commits at last check), making this an open-source build, though the repository does not state a price, production quantity, or how the badge was distributed to attendees.
