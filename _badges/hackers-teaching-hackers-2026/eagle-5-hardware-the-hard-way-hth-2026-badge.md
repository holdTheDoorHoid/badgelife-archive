---
title: Eagle 5 (Hardware the Hard Way / HTH 2026 Badge)
id: hackers-teaching-hackers-2026-eagle-5-hardware-the-hard-way-hth-2026-badge
layout: badge
parent: Hardware the Hard Way 2026 (HTH 2026)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackers-teaching-hackers-2026
year: 2026
makers:
- name: syn-ack-zack
summary: A Reticulum-mesh LoRa badge for HTH 2026 that acts as an RNode modem over USB, letting attendees relay encrypted mesh messages with no apps, logins, or cloud service.
functions: Joins a Reticulum mesh network as an RNode modem (KISS TNC over a dedicated CDC serial port, compatible with Sideband and MeshChat); also exposes an on-badge CLI over a second serial port and drives LED animations.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - hardware tool
tech:
  mcu: nRF52840
  leds:
    count: 10
    type: RGB
    note: 9 single-color LEDs driven by a 74HC595 shift register, plus 1 RGB LED
  display: null
  connectivity:
  - lora
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
  open_source: yes
  hardware_url: null
  firmware_url: https://github.com/syn-ack-zack/eagle5-badge-firmware
  eda_tool: null
  license: GPLv3
  notes: Firmware builds on RNode Firmware by Mark Qvist. A browser-based flasher (no local toolchain needed) is at flash.eagle5.network, linked from the project's own site eagle5.network.
links:
- label: github.com/syn-ack-zack/eagle5-badge-firmware
  url: https://github.com/syn-ack-zack/eagle5-badge-firmware
  kind: repo
- label: eagle5.network
  url: https://eagle5.network
  kind: website
images:
- file: assets/images/badges/hackers-teaching-hackers-2026/eagle-5-hardware-the-hard-way-hth-2026-badge/517faa8e3d.jpg
  source: "https://github.com/syn-ack-zack/eagle5-badge-firmware"
  credit: "syn-ack-zack"
  caption: "The Eagle 5 badge lit up, showing its LEDs"
contact: {}
notes:
- nRF52840 + SX1262 LoRa badge for HTH 2026 that runs as an RNode modem and joins a Reticulum mesh network, with a browser-based flasher at eagle5.network. Found by the event-year sweep, task con-blue-team-con.
status: listed
sources:
- kind: url
  url: https://github.com/syn-ack-zack/eagle5-badge-firmware
  title: Eagle 5 (Hardware the Hard Way / HTH 2026 Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-blue-team-con); event read as ''Hackers Teaching Hackers 2026''.'
- kind: url
  url: https://github.com/syn-ack-zack/eagle5-badge-firmware
  title: syn-ack-zack/eagle5-badge-firmware
  accessed: '2026-09-08'
  note: Confirmed maker, MCU (nRF52840), radio (SX1262 LoRa), LED setup (74HC595 + 9 single-color LEDs + 1 RGB), RNode/Reticulum function, GPLv3 license, and the docs/eagle5.jpg photo.
- kind: url
  url: https://eagle5.network
  title: Eagle 5 Network
  accessed: '2026-09-08'
  note: Confirms the badge was built by "a small crew of security professionals" for HTH 2026 (May), describes it as a Reticulum mesh radio badge, and links the flash.eagle5.network flasher.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker's GitHub repo and project site (eagle5.network) both confirm the badge, its hardware, and its function; no price, quantity, or availability info was published anywhere found. Sweep's one-line note matches what the sources say.
last_modified_date: '2026-09-08'
---

The Eagle 5 is a LoRa-based mesh-radio badge built by syn-ack-zack for Hackers Teaching Hackers 2026 (HTH 2026, held in May). Rather than a game or a blinky novelty, it works as a real communications tool: plugged in over USB, it presents itself as an RNode modem and joins a Reticulum mesh network, letting attendees exchange encrypted messages device-to-device with no phone app, account, or cloud service required. A second CDC serial port carries an on-badge CLI, separate from the RNode/KISS TNC interface used by mesh clients like Sideband and MeshChat.

Hardware-wise it runs an nRF52840 (with the Adafruit nRF52 core and UF2 bootloader) paired with a Semtech SX1262 LoRa transceiver, and lights up nine single-color LEDs through a 74HC595 shift register plus one RGB LED for status/animation.

The firmware is open source under GPLv3, building on Mark Qvist's RNode Firmware, and is published on GitHub. The project's own site, eagle5.network, links a browser-based flasher (flash.eagle5.network) so owners can reflash the badge without installing a local toolchain. No price, production quantity, or distribution details were published in the sources checked.
