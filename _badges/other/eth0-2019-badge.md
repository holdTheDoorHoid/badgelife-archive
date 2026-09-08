---
title: ETH0 2019 Badge
id: other-eth0-2019-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2019
makers:
- name: 'Badge.Team (art: Nikolett; PCB: Renze)'
  url: https://badge.team/
summary: A bare protoboard badge for ETH0 Autumn 2019, a small informal Dutch hacker camp, letting attendees build their own SMD/through-hole circuits instead of running pre-made firmware.
functions: No built-in function; it is a blank prototyping platform. Attendees soldered their own circuits onto it, from simple CR2032 LED badges to a 4093-based astable-oscillator blinker and a Neopixel badge; the standout build was a fan-made "Tamafoxi" Tamagotchi clone with an OLED display, buttons, and an added ESP32 board running badge.team firmware.
look:
  colors: []
  shape: null
  themes:
  - kit
  - learn to solder
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees of ETH0 Autumn 2019
make_your_own:
  open_source: partial
  hardware_url: https://github.com/electroniceel
  firmware_url: null
  eda_tool: null
  license: CC-BY
  notes: The board is not a badge.team original design; it reuses a CC-BY protoboard layout by Electronic Eel, made for both SMD and through-hole parts.
links:
- label: badge.team/docs/badges/eth0-2019
  url: https://badge.team/docs/badges/eth0-2019/
  kind: website
- label: 'Hackaday: Eth0 Autumn 2019: Tiny Camp, Creative Badge'
  url: https://hackaday.com/2019/11/03/eth0-autumn-2019-tiny-camp-creative-badge/
  kind: article
  archived: https://web.archive.org/web/20260114235338/https://hackaday.com/2019/11/03/eth0-autumn-2019-tiny-camp-creative-badge/
images: []
contact: {}
notes:
- DIY protoboard badge adapted from an Electronic Eel CC-licensed prototyping board layout, for building your own SMD circuits.
- ETH0 is a small, informal Dutch hacker camp with no fixed schedule; the badge itself carries no ESP32 or badge.team firmware, unlike most badge.team badges.
status: released
sources:
- kind: url
  url: https://badge.team/docs/badges/eth0-2019/
  title: ETH0 2019 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''ETH0 2019''.'
- kind: url
  url: https://hackaday.com/2019/11/03/eth0-autumn-2019-tiny-camp-creative-badge/
  title: 'Eth0 Autumn 2019: Tiny Camp, Creative Badge'
  accessed: '2026-09-07'
  note: Event context (small informal Dutch hacker camp near Lichtenvoorde, NL), badge description, and examples of attendee-built circuits including the Tamafoxi.
  archived: https://web.archive.org/web/20260114235338/https://hackaday.com/2019/11/03/eth0-autumn-2019-tiny-camp-creative-badge/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: ETH0 is an informal, recurring Dutch hacker camp series with no fixed venue and no listing in events.yml, so event is left as other; this specific gathering was "ETH0 Autumn 2019" near Lichtenvoorde, Netherlands. No price, quantity, MCU/LED specs, or photo of the badge itself were found in the available sources (only a line-art SVG outline, which fetch_image.py cannot save as it is not a raster image). No dedicated Electronic Eel repo URL for the exact protoboard layout was confirmed beyond their GitHub org page.
last_modified_date: '2026-09-07'
---

The ETH0 2019 badge was handed out at ETH0 Autumn 2019, a small, informally run hacker camp held at a private camping hostel near Lichtenvoorde in the eastern Netherlands. Rather than the ESP32-based, badge.team-firmware badges the same Dutch badge crew usually builds for larger events, this one was deliberately bare: a prototyping board with artwork by Nikolett and PCB design by Renze, built around a CC-BY protoboard layout published by Electronic Eel that supports both SMD and through-hole parts.

The badge had no pre-loaded function of its own — it was a blank canvas for attendees to solder together their own circuits over the weekend. Results ranged from simple CR2032-powered LED badges and 4093 Schmitt-trigger astable-oscillator blinkers to Neopixel builds, and, most notably, a fan-made "Tamafoxi" Tamagotchi clone with an OLED display and buttons, built by attaching an ESP32 board to the back and running badge.team firmware on it.

No pricing, production quantity, or photographs of an assembled badge were found; the only image located was a line-art SVG outline of the bare board on the badge.team documentation page, which is not a format the archive's image tool can save.
