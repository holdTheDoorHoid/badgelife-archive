---
title: Wild West Hackin' Fest Deadwood 2025 E-Badge
id: wild-west-hackin-fest-2025-wild-west-hackin-fest-deadwood-2025-e-badge
layout: badge
parent: Wild West Hackin' Fest 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: wild-west-hackin-fest-2025
year: 2025
makers:
- name: Wild West Hackin' Fest (sponsored by Antisyphon Training)
summary: An ESP32-S3 electronic badge built as the Meta CTF badge-hacking challenge for WWHF Deadwood 2025.
functions: 'Boots through simulated retro OS screens (DOS, Windows NT, macOS, Commodore) hiding CTF flags; eight LEDs and a light sensor carry binary/Morse-code puzzles; BLE messaging and USB-C serial output add further challenge stages; 23 flags total spanning BIOS text, shell simulations, BLE characteristics, and cipher/encoding puzzles (ROT13, Caesar, Pigpen, Bacon cipher, semaphore, Morse).'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - security
  - retro computer
tech:
  mcu: ESP32-S3-WROOM-1
  leds:
    count: 8
    type: null
    note: Four upper, four lower; used for binary and Morse-code challenges.
  display: 128x64 OLED-like display
  connectivity:
  - ble
  - usb
  battery: LiPo, charged via onboard TP4056 charge controller
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/events/wild-west-hackin-fest-deadwood-2025
  url: https://badge.gallery/events/wild-west-hackin-fest-deadwood-2025
  kind: website
- label: wildwesthackinfest.com/e-badge
  url: https://wildwesthackinfest.com/e-badge/
  kind: website
- label: github.com/aalex954/WWHF2025-Badge-Writeup
  url: https://github.com/aalex954/WWHF2025-Badge-Writeup
  kind: repo
- label: 'blog.netrunsecurity.com: Badge Hacking - WWHF Deadwood 2025'
  url: https://blog.netrunsecurity.com/badge-hacking-wwhf-deadwood/
  kind: article
- label: 'badge.gallery: ESP32-S3 teardown trail'
  url: https://badge.gallery/addons/wild-west-hackin-fest-deadwood-2025-e-badge/esp32-s3-teardown-trail
  kind: article
images: []
contact: {}
notes:
- ESP32-S3-WROOM-1 badge with OLED, BLE and eight programmable LEDs used as the credential and MetaCTF badge-challenge artifact at WWHF Deadwood 2025. Found by the event-year sweep, task con-kernelcon.
- 'Sweep''s title matched the maker''s own naming exactly; no correction needed.'
status: released
sources:
- kind: url
  url: https://badge.gallery/events/wild-west-hackin-fest-deadwood-2025
  title: Wild West Hackin' Fest Deadwood 2025 E-Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kernelcon); event read as ''Wild West Hackin'' Fest Deadwood 2025''.'
- kind: url
  url: https://wildwesthackinfest.com/e-badge/
  title: e-badge - Wild West Hackin' Fest
  accessed: '2026-09-08'
  note: 'Official announcement page (content since updated to reference 2026); confirms Antisyphon Training sponsorship, MetaCTF badge-CTF integration, and contact team (Ray Feltch, David Fletcher, Rick Wisser).'
- kind: url
  url: https://github.com/aalex954/WWHF2025-Badge-Writeup
  title: WWHF2025-Badge-Writeup
  accessed: '2026-09-08'
  note: 'Attendee CTF writeup (No_Use_For_A_Name) confirming ESP32-S3 240MHz/512KB SRAM/8MB flash, BLE via nRF Connect, light sensor, 23 flags across BIOS/shell/BLE/cipher challenges, retro-OS boot simulations.'
- kind: url
  url: https://blog.netrunsecurity.com/badge-hacking-wwhf-deadwood/
  title: Badge Hacking - WWHF Deadwood 2025 (NetRunSecurity)
  accessed: '2026-09-08'
  note: 'Confirms ESP32-S3-WROOM-1, 128x64 OLED-like display, TP4056 LiPo charger, USB-C serial at 115200 baud, eight-LED binary/Morse behavior.'
- kind: url
  url: https://badge.gallery/addons/wild-west-hackin-fest-deadwood-2025-e-badge/esp32-s3-teardown-trail
  title: ESP32-S3 teardown trail
  accessed: '2026-09-08'
  note: 'badge.gallery add-on page mirroring the NetRunSecurity teardown details.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'No maker-published hardware/firmware repo, price, quantity, or distribution details found; all technical detail comes from third-party attendee writeups (aalex954, NetRunSecurity), not from Antisyphon/WWHF themselves. No rights-cleared photos of the badge itself were found on any source checked. sao_version left null and LED type left null since no source specifies them.'
last_modified_date: '2026-09-08'
---

The Wild West Hackin' Fest Deadwood 2025 e-badge was an ESP32-S3-WROOM-1 electronic badge built as the conference's Meta CTF badge-hacking challenge, sponsored by Antisyphon Training. It carries a 128x64 OLED-like display, eight LEDs (four upper, four lower), a light sensor, Bluetooth Low Energy, and USB-C serial output, with a LiPo battery charged through an onboard TP4056 controller.

On boot the badge cycles through simulated retro operating-system screens (DOS, Windows NT, classic Mac OS, and Commodore), hiding pieces of a 23-flag capture-the-flag challenge across BIOS text, shell-window simulations, BLE characteristic messages, and classic encoding puzzles (ROT13, Caesar, Pigpen, Bacon cipher, semaphore, Morse code). MetaCTF handled scoring and registration for the badge CTF. Firmware could reportedly be extracted from the device with esptool for offline analysis, which attendees used to solve some of the challenges.

No official hardware or firmware repository, price, production quantity, or distribution details were published by Antisyphon or WWHF that could be found; everything technical in this entry comes from attendee writeups (a GitHub CTF writeup by aalex954/"No_Use_For_A_Name" and a NetRunSecurity blog teardown) rather than from the maker's own materials.
