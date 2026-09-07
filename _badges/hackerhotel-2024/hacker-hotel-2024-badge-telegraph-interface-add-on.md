---
title: Hackerhotel 2024 Badge
id: hackerhotel-2024-hacker-hotel-2024-badge-telegraph-interface-add-on
layout: badge
parent: Hackerhotel 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackerhotel-2024
year: 2024
makers:
- name: badge.team
  url: https://badge.team/
  role: 'hardware/firmware: Tilde.industries and Nicolai Electronics'
summary: The official conference badge for Hackerhotel 2024, themed around a 19th-century Cooke and Wheatstone telegraph, with an LED grid and rotary switches standing in for the telegraph's needles as the primary text-input method.
functions: 'Text entry via a Cooke & Wheatstone-style telegraph interface: five three-way switches (rotate left/right, press) move a diamond-shaped grid of LEDs to spell letters, confirmed with a clicking relay for tactile feedback. Also runs onsite puzzles, a nonvolatile nametag, mesh-networked messaging, and a Battleships game playable badge-to-badge.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - puzzle
  - village badge
tech:
  mcu: ESP32-C6 + CH32V003
  leds:
    count: null
    type: null
    note: Diamond-shaped LED grid forming the telegraph needle display, plus an addressable status LED
  display: E-paper, 296x128, red/black
  connectivity:
  - wifi
  - ble
  - i2c
  battery: USB-C rechargeable
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed as the conference badge to Hackerhotel 2024 attendees; not sold commercially
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/badgeteam/hackerhotel-2024-hardware
  firmware_url: https://github.com/badgeteam/hackerhotel-2024-firmware-esp32c6
  eda_tool: KiCad
  license: CERN-OHL-P
  notes: A second firmware repo covers the CH32V003 co-processor at https://github.com/badgeteam/hackerhotel-2024-firmware-ch32v003
links:
- label: hackaday.com/2024/03/30/a-telegraph-interface-for-the-hacker-hotel-2024-badge
  url: https://hackaday.com/2024/03/30/a-telegraph-interface-for-the-hacker-hotel-2024-badge/
  kind: article
- label: badge.team/docs/badges/hackerhotel-2024
  url: https://badge.team/docs/badges/hackerhotel-2024/
  kind: doc
- label: github.com/badgeteam/hackerhotel-2024-hardware
  url: https://github.com/badgeteam/hackerhotel-2024-hardware
  kind: repo
- label: github.com/badgeteam/hackerhotel-2024-firmware-esp32c6
  url: https://github.com/badgeteam/hackerhotel-2024-firmware-esp32c6
  kind: repo
- label: github.com/badgeteam/hackerhotel-2024-firmware-ch32v003
  url: https://github.com/badgeteam/hackerhotel-2024-firmware-ch32v003
  kind: repo
images:
  - file: assets/images/badges/hackerhotel-2024/hacker-hotel-2024-badge-telegraph-interface-add-on/fda087b89f.jpg
    source: "https://badge.team/docs/badges/hackerhotel-2024/"
    credit: "badge.team"
    caption: "Hackerhotel 2024 badge front, showing the telegraph-style LED grid and switches"
  - file: assets/images/badges/hackerhotel-2024/hacker-hotel-2024-badge-telegraph-interface-add-on/962284ae57.jpg
    source: "https://badge.team/docs/badges/hackerhotel-2024/"
    credit: "badge.team"
    caption: "Hackerhotel 2024 badge e-paper display close-up"
contact: {}
notes:
- 'Original sheet/sweep entry described this as a "Telegraph Interface add-on"; research found the telegraph interface is not a separate add-on but the input mechanism built into the Hackerhotel 2024 conference badge itself. Retitled and retyped accordingly (event corrected from ''other'' to hackerhotel-2024).'
status: released
sources:
- kind: url
  url: https://hackaday.com/2024/03/30/a-telegraph-interface-for-the-hacker-hotel-2024-badge/
  title: Hacker Hotel 2024 Badge (Telegraph Interface add-on)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''Hacker Hotel 2024''.'
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2024/
  title: 'Hackerhotel 2024 | Badge.Team'
  accessed: '2026-09-07'
  note: Maker's own documentation page; source for specs, images, distribution, and firmware/hardware repo links.
- kind: url
  url: https://github.com/badgeteam/hackerhotel-2024-hardware
  title: 'GitHub - badgeteam/hackerhotel-2024-hardware'
  accessed: '2026-09-07'
  note: Confirmed CERN-OHL-P open hardware license and maker credits (Tilde.industries, Nicolai Electronics).
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-checked 2026-09-07: badge.team docs page, the Hackaday article, and the hardware/firmware GitHub repos were re-fetched and confirm every non-empty field and body sentence (MCU, e-paper spec, switches/relay, wifi/ble/i2c, USB-C battery, CERN-OHL-P/KiCad, puzzles, nonvolatile nametag, mesh Battleships game, both images). Price/quantity/exact LED count remain unpublished and are left empty rather than guessed. Note: a separate entry, telegraph-badge-hackerhotel-2024.md, covers the same physical badge from an independent discovery sweep with some differing details (e.g. sao_version v1, colors black/red, different maker-list phrasing) - left untouched per one-entry-per-task scope; worth reconciling or deduplicating in a follow-up.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/hacker-hotel-2024-badge-telegraph-interface-add-on/
---

The Hackerhotel 2024 badge, made by badge.team (Tilde.industries and Nicolai Electronics), builds its entire interaction model around a 19th-century Cooke and Wheatstone telegraph. Instead of a keyboard, five three-way switches let the wearer rotate a diamond-shaped grid of LEDs to point at letters the way the original telegraph's five needles did; a small relay clicks audibly on each confirmed keystroke purely for tactile feedback. An ESP32-C6 handles processing and wireless (Wi-Fi 6, BLE, 802.15.4 mesh), while a CH32V003 co-processor manages the switch and LED I/O. A 296x128 red/black e-paper display, salvaged from surplus German supermarket shelf-edge labels, shows the nametag and puzzle state, and the badge exposes SAO and Qwiic connectors for add-ons.

Distributed as the conference badge for Hackerhotel 2024 attendees, it supported onsite puzzles themed to the Victorian telegraph setting, mesh-networked inter-badge messaging, and a badge-to-badge Battleships game. Hardware (KiCad, CERN-OHL-P) and firmware for both microcontrollers are published on the badgeteam GitHub org, making it fully open source.

This entry was originally imported from a discovery sweep as a standalone "Telegraph Interface add-on"; research turned up no separate add-on board — the telegraph interface is the badge's built-in input method, not a plug-in accessory, so the entry has been retitled and retyped as the badge itself.
