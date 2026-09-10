---
title: SAINTCON 2023 badge (compukidmike)
id: saintcon-2023-saintcon-2023-badge-compukidmike
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2023
year: 2023
makers:
- name: compukidmike
summary: A custom ESP32-S3 conference badge built for SAINTCON 2023, with an RPG-style attract-mode game (battles and inventory) and remote party codes.
functions: Interactive menu system; arcade-style attract/demo mode after 15 seconds idle showing battles, inventory, and committee faces; remote party creation via codes (firmware V1.4); joystick input.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - security
tech:
  mcu: ESP32-S3
  leds: null
  display: LCD
  connectivity:
  - wifi
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
  open_source: true
  hardware_url: https://github.com/compukidmike/saintcon2023/tree/main/Hardware
  firmware_url: https://github.com/compukidmike/saintcon2023/tree/main/Firmware
  eda_tool: KiCad
  gerbers_url: https://github.com/compukidmike/saintcon2023/blob/main/Hardware/Saintcon2023Gerbers.zip
  bom_url: https://github.com/compukidmike/saintcon2023/blob/main/Hardware/Saintcon2023BOM.pdf
  notes: Repo includes a joystick-cap STL for 3D printing, plus a Firmware dev environment built around an ESP32-S3 DevKitC-1 with a W6100 Ethernet module for development/testing.
links:
- label: github.com/compukidmike/saintcon2023
  url: https://github.com/compukidmike/saintcon2023
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/saintcon2023
  title: SAINTCON 2023 badge (compukidmike)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''saintcon-2023''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/saintcon2023/main/README.md
  title: 'saintcon2023 README: firmware flashing and update instructions'
  accessed: '2026-09-07'
  note: Confirms ESP32-S3 chip, attract-mode game description, WiFi-based OTA update network, firmware version V1.4.
- kind: url
  url: https://github.com/compukidmike/saintcon2023/tree/main/Hardware
  title: saintcon2023 Hardware directory listing
  accessed: '2026-09-07'
  note: Lists published BOM (PDF/XLSX), KiCad project zip, Gerbers zip, and a joystick-cap STL.
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/saintcon2023/main/Firmware/README.md
  title: saintcon2023 Firmware README
  accessed: '2026-09-07'
  note: Notes an LCD display and a W6100 Ethernet module used in the dev/test setup (ESP32-S3 DevKitC-1).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No price, quantity made, or distribution method (free con badge vs. sold) is stated anywhere in the repo; left unknown rather than guessed. No LED count/type or battery details found. No photos of the assembled badge were found in the repo or on its pages (no images/ folder, no README screenshots), so no images could be saved. Repo does not say whether this is the official SAINTCON 2023 conference badge or an independent/personal badge made for the con; the "committee faces" and party-wide "BadgeNet-OutOfScope" update network suggest it may be an official or team-affiliated badge, but this is not confirmed by a source and is not asserted in the entry.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2023/saintcon-2023-badge-compukidmike.glb
  method: gerber
  source_file: Hardware/Saintcon2023Gerbers.zip
  generated: '2026-09-10'
  bytes: 220928
  size_mm:
  - 118.9
  - 98.0
---

This is a custom electronic conference badge built by compukidmike (CompuKidMike) for SAINTCON 2023, running on an ESP32-S3 with an LCD display, joystick input, and Wi-Fi. Beyond its main menu, the badge has an optional arcade-style attract/demo mode that kicks in after 15 seconds of idling, playing out RPG-style battles and an inventory screen intermixed with committee member faces and LED effects. Firmware could be updated wirelessly over a dedicated conference network ("BadgeNet-OutOfScope") or manually via USB with esptool, and firmware version V1.4 added the ability to create game "parties" remotely using codes.

The project is fully open-hardware: the GitHub repository publishes the complete KiCad schematic/PCB files, Gerbers, and a bill of materials, along with a 3D-printable STL for a custom joystick cap. No information was found on price, quantity produced, or how it was distributed (whether it was a free conference badge, an independent build compukidmike gave away, or something else), and no photos of the finished badge were located.

