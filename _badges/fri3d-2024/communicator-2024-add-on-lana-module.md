---
title: Communicator (2024 add-on)
id: fri3d-2024-communicator-2024-add-on-lana-module
layout: badge
parent: Fri3D 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: fri3d-2024
year: 2024
makers:
- name: Fri3d Camp
summary: A keyboard-and-audio add-on for the Fri3d Camp 2024 badge, built around a small RISC-V "LANA TNY" controller board.
functions: Acts as a HID keyboard for the badge (and standalone over USB), plus adds a microphone and small speaker for audio input/output. Outputs 8-byte HID report packets over USB, I2C (address 0x38), and UART.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: CH32V203G6U6 (RISC-V, on the LANA TNY board)
  leds: null
  display: null
  connectivity:
  - usb
  - i2c
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - kit
  where: Distributed to Fri3d Camp 2024 attendees as an add-on kit for the badge; self-assembled (solder the speaker and headers, mount the silicone keyboard).
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Fri3dCamp/communicator_2024
  firmware_url: https://github.com/Fri3dCamp/communicator_2024
  eda_tool: null
  license: Apache-2.0
  notes: Hardware design and production files (Gerbers, datasheets) are in the repo. The LANA TNY module is programmed with Embeetle IDE or MounRiver Studio; see the repo's programming guide and https://phyx.be/LANA_TNY/.
links:
- label: fri3dcamp.github.io/badge_2024/en
  url: https://fri3dcamp.github.io/badge_2024/en/
  kind: website
- label: Communicator add-on documentation
  url: https://fri3dcamp.github.io/badge_2024/en/communicator/
  kind: doc
- label: Fri3dCamp/communicator_2024 (GitHub)
  url: https://github.com/Fri3dCamp/communicator_2024
  kind: repo
- label: LANA TNY module (phyx.be)
  url: https://phyx.be/LANA_TNY/
  kind: website
images:
- file: assets/images/badges/fri3d-2024/communicator-2024-add-on-lana-module/f1f394e4df.png
  source: "https://github.com/Fri3dCamp/communicator_2024"
  credit: "Fri3d Camp"
  caption: "Assembled Communicator 2024 add-on with keyboard and speaker"
- file: assets/images/badges/fri3d-2024/communicator-2024-add-on-lana-module/1411d6835b.jpg
  source: "https://fri3dcamp.github.io/badge_2024/en/communicator/"
  credit: "Fri3d Camp"
  caption: "Communicator 2024 add-on kit contents"
contact: {}
notes:
- 'The event-year sweep''s snippet described this as a "LoRa-based" communicator; that appears to be a
  misreading of "LANA" (the name of the small CH32V203-based controller board used here) as "LoRa". The
  maker''s own pages and GitHub repo confirm no radio module or display is present — it is a keyboard
  and audio (mic + speaker) add-on. The sweep also titled the entry "Communicator (2024 add-on, LANA
  Module)"; the maker''s site just calls it "Communicator", so the title has been shortened to match
  while keeping "LANA" details in the tech/make_your_own fields.'
status: released
sources:
- kind: url
  url: https://fri3dcamp.github.io/badge_2024/en/
  title: Communicator (2024 add-on, LANA Module)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:fri3d); event read as ''fri3d-2024''.'
- kind: url
  url: https://fri3dcamp.github.io/badge_2024/en/communicator/
  title: Communicator - Fri3d Camp 2024 badge docs
  accessed: '2026-09-10'
  note: Confirms the Communicator is a keyboard + microphone + speaker add-on built on the LANA TNY board; no radio or display. Lists the HID protocol details.
- kind: url
  url: https://github.com/Fri3dCamp/communicator_2024
  title: Fri3dCamp/communicator_2024
  accessed: '2026-09-10'
  note: Apache-2.0 hardware design/production files repo; confirms CH32V203G6U6 MCU on the LANA TNY board, kit contents, and assembly steps; source of both saved images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Price and quantity made are not published anywhere found; left empty. No SAO header (this plugs into the badge's own connector, not a generic SAO port), so sao_version left null. Confirmed real (not a search-snippet-only rumor); corrected the sweep's mistaken "LoRa" characterization.
last_modified_date: '2026-09-10'
---

The Communicator is an official add-on for the Fri3d Camp 2024 badge, given out to camp attendees as a self-assembly kit. At its core is the LANA TNY, a small RISC-V (CH32V203G6U6) controller board that reads a backlit silicone QWERTY keyboard designed by Solder Party and drives a microphone/speaker pair for basic audio input and output. Once assembled and clipped onto the badge, it behaves as a HID keyboard, sending 8-byte HID report packets over USB, I2C, or UART; the keyboard can also work as a standalone USB keyboard when unplugged from the badge (though not while it's still connected).

Despite its "LANA Module" name suggesting a LoRa radio, the Communicator has no wireless radio and no display — it's purely a text-input and audio expansion. Hardware design files, datasheets, and firmware/programming instructions (via Embeetle IDE or MounRiver Studio) are published on GitHub under an Apache-2.0 license, including a step-by-step guide for flashing the LANA TNY module over its USB-C port.

## Make your own

Hardware design and production files (Gerbers, BOM, datasheets) are in [Fri3dCamp/communicator_2024](https://github.com/Fri3dCamp/communicator_2024) under Apache-2.0. To reflash the LANA TNY controller, install Embeetle IDE (or MounRiver Studio), open the `lana-tny-01-communicator-2024` project, hold the BOOT switch while plugging in USB-C to enter bootloader mode, then flash — Windows users may need Zadig to install the right USB driver first. Full steps are on the repo's programming guide.
