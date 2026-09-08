---
title: Terminator-01
id: hackers-teaching-hackers-2024-terminator-01-hth-2024-badge
layout: badge
parent: Hackers Teaching Hackers 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackers-teaching-hackers-2024
year: 2024
makers:
- name: syn-ack-zack / HTHackers
  url: https://github.com/syn-ack-zack/Terminator-01
summary: A sunglasses-shaped conference badge for HTH 2024 that acts as an ESP32 client for Open Interpreter's "01" voice-interface project, letting the wearer trigger voice lines by touching capacitive teeth on the front.
functions: 'On boot, tries to connect to a configured "01 light server" over WiFi. Three voice lines can be played by touching capacitive teeth on the front of the sunglasses. The center HTH logo toggles wireless connectivity on/off. WiFi and server address are configured via a captive portal (badge broadcasts SSID "T-1337-v#", portal at http://4.3.2.1) or a serial menu at 115200 baud. The serial menu also gates a CTF: three of its five options are challenges with a published wiki walkthrough.'
look:
  colors:
  - black
  shape: sunglasses
  themes:
  - sci-fi
  - wearable
  - security
  - ctf
tech:
  mcu: ESP32-C3-Mini
  leds: null
  display: none
  connectivity:
  - wifi
  - uart
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/syn-ack-zack/Terminator-01
  eda_tool: null
  notes: 'The GitHub repo (and the HTHackers fork) currently contains only a README with build notes; no firmware source or hardware design files are checked in to either repo as of the last check.'
links:
- label: github.com/HTHackers/Terminator-01
  url: https://github.com/HTHackers/Terminator-01
  kind: repo
- label: github.com/syn-ack-zack/Terminator-01 (original)
  url: https://github.com/syn-ack-zack/Terminator-01
  kind: repo
- label: Terminator-01 CTF walkthrough (wiki)
  url: https://github.com/syn-ack-zack/Terminator-01/wiki
  kind: doc
- label: Open Interpreter 01 ESP32 client (badge's compatible platform)
  url: https://01.openinterpreter.com/client/esp32
  kind: doc
images:
- file: assets/images/badges/hackers-teaching-hackers-2024/terminator-01-hth-2024-badge/c54e0e21b9.png
  source: "https://github.com/HTHackers/Terminator-01"
  credit: "syn-ack-zack / HTHackers"
  caption: "Terminator-01 sunglasses badge, front view"
- file: assets/images/badges/hackers-teaching-hackers-2024/terminator-01-hth-2024-badge/9cb3be1b32.jpg
  source: "https://github.com/HTHackers/Terminator-01"
  credit: "syn-ack-zack / HTHackers"
  caption: "Terminator-01 badge, capacitive touch teeth detail"
contact: {}
notes:
- 'Original sweep note: "ESP32-C3 sunglasses-shaped voice-interface badge for HTH 2024 with capacitive touch-teeth and onboard speech playback." Confirmed accurate against the maker''s README.'
- 'Title corrected from "Terminator-01 (HTH 2024 Badge)" (the sweep''s title, taken from the fork''s repo description) to "Terminator-01", the name used in the README itself.'
- 'HTHackers/Terminator-01 is a GitHub fork of the original maker''s own repo, syn-ack-zack/Terminator-01; both are cited as sources.'
status: released
sources:
- kind: url
  url: https://github.com/HTHackers/Terminator-01
  title: Terminator-01 (HTH 2024 Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-blue-team-con); event read as ''Hackers Teaching Hackers 2024''.'
- kind: url
  url: https://raw.githubusercontent.com/HTHackers/Terminator-01/main/README.md
  title: Terminator-01 README
  accessed: '2026-09-08'
  note: 'Full README text: hardware (ESP32-C3-Mini, MAX98357A DAC, SPH0645LM4H I2S mic), badge operation, WiFi/captive-portal setup, CTF references, and the badge''s photos.'
- kind: url
  url: https://github.com/syn-ack-zack/Terminator-01
  title: syn-ack-zack/Terminator-01
  accessed: '2026-09-08'
  note: 'Confirmed HTHackers/Terminator-01 is a fork of this original maker repo; also contains only a README (no firmware/hardware files present).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core identity, function, and MCU confirmed directly from the maker''s README. Could not confirm price, quantity made, or availability/distribution (badge appears to have been a con-distributed/CTF badge, not sold, but no source states this explicitly, so get_one fields are left empty). No firmware or hardware design files are actually present in either the original or fork GitHub repos despite the README describing a software/hardware project, so open_source is marked "partial" (README/documentation only) rather than "yes"; hardware_url left null. LEDs and SAO header not mentioned anywhere and are assumed absent (sunglasses have no LEDs visible in photos). Did not open the CTF wiki walkthrough, out of scope for cataloging.'
last_modified_date: '2026-09-08'
---

Terminator-01 is a sunglasses-shaped conference badge made by syn-ack-zack for the 2024 Hackers Teaching Hackers (HTH) conference, distributed and later maintained through a GitHub fork under the HTHackers organization. It is built around an ESP32-C3-Mini paired with a MAX98357A DAC and an SPH0645LM4H I2S microphone, and it functions as a hardware client for Open Interpreter's "01" project — a natural-language voice interface normally run against a local or self-hosted "01 light server."

On the wearer's side, three capacitive-touch pads shaped like teeth on the front of the sunglasses each trigger a stored voice line, while touching the HTH logo in the center toggles the badge's WiFi radio on and off. Getting the badge talking to a server requires configuration: on first boot it looks for saved WiFi and server details, and if none are found it broadcasts its own access point (SSID "T-1337-v#") with a captive portal at 4.3.2.1 for entering them, or the same settings can be pushed over a USB-serial connection at 115200 baud using an onboard menu system.

That serial menu doubles as a built-in CTF: three of its five options are challenges rather than configuration commands, with a walkthrough published separately on the project's GitHub wiki. Despite the README describing the hardware and firmware in detail, neither the original repository nor the HTHackers fork actually contains source or design files at the time of this check — both hold only the README — so the project's open-source status is best described as documentation-only for now.
