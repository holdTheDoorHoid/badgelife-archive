---
title: HackCUBE
id: hitb-2018-unicorncube-hackcube-device
layout: badge
parent: Hitbsecconf 2018
grand_parent: Badge Archive
nav_exclude: true
type: other
event: hitb-2018
year: 2018
makers:
- name: 360 UnicornTeam
  url: https://github.com/unicornteam
summary: A pocket-sized wireless hacking and RF pentest tool built by Qihoo 360's UnicornTeam, first shown to the public at HITBSecConf2018 Amsterdam and sold in limited quantities at the Badge Village alongside the conference badge.
functions: 'Combines an Arduino Micro Pro (sub-GHz RF via CC1101 at 315/433MHz, nRF24L01+ at 2.4GHz, and EM4095 for 125kHz RFID) with a Raspberry Pi Zero W (WiFi/Bluetooth, USB HID emulation, 13.56MHz NFC) in one 8.5cm^3 cube. Demonstrated uses include rogue WiFi access points, sub-GHz brute-force attacks on wireless locks and remotes, TPMS (tire pressure sensor) sniffing/spoofing at 433.92MHz, RFID/NFC card reading, and acting as a HID keyboard/mouse injector. External SDR hardware such as HackRF, RTL-SDR, and CC2541 dongles can be attached.'
look:
  colors:
  - black
  shape: null
  themes:
  - hardware tool
  - radio
  - security
tech:
  mcu: Arduino Micro Pro + Raspberry Pi Zero W
  leds:
    count: 64
    type: RGB
    note: 8x8 RGB LED matrix used for status feedback
  display: LED matrix 8x8
  connectivity:
  - wifi
  - bluetooth
  - nfc
  - rfid
  - sub-ghz
  - usb
  battery: not specified (described as battery powered)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - purchase
  - preorder
  - village
  where: 'HITBSecConf2018 Amsterdam Badge Village, alongside the conference badge and the book "Inside Radio: An Attack and Defense Guide"'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/unicornteam/HackCube
  firmware_url: https://github.com/unicornteam/HackCube
  eda_tool: null
links:
- label: archive.conference.hitb.org/hitbsecconf2018ams/commsec-village
  url: https://archive.conference.hitb.org/hitbsecconf2018ams/commsec-village/
  kind: website
- label: HITB LAB session - Wireless Hacking with HackCUBE
  url: https://archive.conference.hitb.org/hitbsecconf2018ams/sessions/hitb-lab-wireless-hacking-with-hackcube/
  kind: article
- label: UnicornTeam/hackcube on GitHub
  url: https://github.com/unicornteam/HackCube
  kind: repo
- label: 'Wireless Hacking with ''HackCUBE'' (slides, HITB2018 AMS)'
  url: https://conference.hitb.org/hitbsecconf2018ams/materials/D1T3%20-%20Yunding%20Jian,%20Jie%20Fu%20&%20Chaoran%20Wang%20-%20Wireless%20Hacking%20with%20HackCUBE.pdf
  kind: doc
images:
  - file: assets/images/badges/hitb-2018/unicorncube-hackcube-device/336fdfc87a.jpg
    source: "https://github.com/UnicornTeam/hackcube"
    credit: "UnicornTeam"
    caption: "The HackCUBE device"
  - file: assets/images/badges/hitb-2018/unicorncube-hackcube-device/4e5c518dd2.jpg
    source: "https://github.com/UnicornTeam/hackcube"
    credit: "UnicornTeam"
    caption: "HackCUBE opened, showing internal boards"
contact: {}
notes:
- 'The sweep listed the title as "UnicornCUBE/HackCUBE device"; the maker''s own materials only use the name "HackCUBE" (UnicornCUBE does not appear as a separate product name in any source found — likely the sweep folding the team name "Unicorn Team" and the product "HackCUBE" together, or referring to two names used interchangeably for the same device at the Badge Village listing).'
- Not a wearable badge or SAO; it is a standalone RF/wireless pentest tool sold at the HITB Badge Village. Kept under type: other since it is a real, specific, collectible item from the badge scene rather than a con's generic merch.
status: released
sources:
- kind: url
  url: https://archive.conference.hitb.org/hitbsecconf2018ams/commsec-village/
  title: UnicornCUBE/HackCUBE device
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://archive.conference.hitb.org/hitbsecconf2018ams/sessions/hitb-lab-wireless-hacking-with-hackcube/
  title: 'HITB LAB: Wireless Hacking with HackCUBE'
  accessed: '2026-09-10'
  note: Confirms maker, size (8.5cm^3), battery power, and first public showing at HITB AMS 2018.
- kind: url
  url: https://github.com/unicornteam/HackCube
  title: UnicornTeam/hackcube (GitHub, archived)
  accessed: '2026-09-10'
  note: Confirms hardware (Arduino Micro Pro + Raspberry Pi Zero W, CC1101/nRF24L01+/EM4095 radios), features, and 8x8 RGB LED matrix; source for photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Price and quantity made were not stated anywhere found. Battery capacity/type not specified beyond "battery powered." GitHub repo is archived (read-only) with no explicit license file found in the fetched content, so open_source is marked partial rather than yes.
last_modified_date: '2026-09-10'
---

The HackCUBE is a pocket-sized wireless security research tool built by Qihoo 360's UnicornTeam (also credited as "360 UnicornTeam"), a group better known within the badge scene for the HITBSecConf2018 Amsterdam and Dubai conference badges. Rather than a wearable badge or SAO, it is a standalone 8.5cm³ cube that pairs an Arduino Micro Pro handling sub-GHz and low-frequency RF (CC1101, nRF24L01+, EM4095) with a Raspberry Pi Zero W handling WiFi, Bluetooth, NFC, and USB HID emulation, with an 8x8 RGB LED matrix for status feedback. It was first shown publicly at HITBSecConf2018 Amsterdam, where a hands-on lab session ("Wireless Hacking with HackCUBE") demonstrated attacks such as rogue access points, sub-GHz remote/lock brute-forcing, TPMS sniffing and spoofing, and RFID/NFC card reads. Limited quantities were made available for purchase and pre-order at the conference's Badge Village alongside the HITB badge itself.

The team continued developing the platform afterward as "HackCUBE-Special," presented in further hands-on labs at HITBSecConf2019 Amsterdam. Hardware notes and firmware for the original HackCUBE were published on GitHub under UnicornTeam's org, though the repository has since been archived (read-only) and no explicit open-source license was found in it.

## Make your own

Hardware notes and source are published at [github.com/unicornteam/HackCube](https://github.com/unicornteam/HackCube), covering the Arduino/Raspberry Pi wiring, the RF module set, and example scripts for the WiFi, sub-GHz, TPMS, and NFC/RFID demos shown in the HITB lab session.
