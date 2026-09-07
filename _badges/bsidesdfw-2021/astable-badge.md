---
title: Astable Badge
id: bsidesdfw-2021-astable-badge
layout: badge
parent: BSidesdfw 2021
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsidesdfw-2021
year: 2021
makers:
- name: Alt_Bier
  url: https://github.com/gowenrw
summary: A through-hole soldering-education badge built around an astable multivibrator circuit that blinks LEDs using two transistors instead of an IC.
functions: Blinks two user-chosen LEDs via a two-transistor astable multivibrator; adjustable-speed blinking via onboard trim potentiometers; test points let builders probe the circuit with a logic analyzer.
look:
  colors: []
  shape: null
  themes:
  - cyberpunk
  - movie
  - learn to solder
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Kit ships with five 3mm THT LEDs (red, green, blue, yellow, white); builder solders in two of their choice.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed at BSidesDFW 2021, associated with the Hardware Hacking Village (HHV) badge-soldering session.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/gowenrw/astable_badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: astablebadge.altbier.us
  url: https://astablebadge.altbier.us/
  kind: website
  archived: https://web.archive.org/web/20260907110511/https://astablebadge.altbier.us/
- label: gowenrw/astable_badge (GitHub)
  url: https://github.com/gowenrw/astable_badge
  kind: repo
- label: Badge kit assembly instructions
  url: https://astablebadge.altbier.us/badgekit.html
  kind: doc
- label: altbier.us/bsidesdfw
  url: https://altbier.us/bsidesdfw/
  kind: website
images:
- file: assets/images/badges/bsidesdfw-2021/astable-badge/f01da05c77.jpg
  source: https://astablebadge.altbier.us/
  credit: Alt_Bier (gowenrw)
  caption: Assembled Astable Badge with Cyber-Dolphin artwork
- file: assets/images/badges/bsidesdfw-2021/astable-badge/f5bcc7b6c9.jpg
  source: https://astablebadge.altbier.us/
  credit: Alt_Bier (gowenrw)
  caption: Front of the unpopulated Astable Badge PCB
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://astablebadge.altbier.us/
  title: Astable Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''BSidesDFW 2021''.'
  archived: https://web.archive.org/web/20260907110511/https://astablebadge.altbier.us/
- kind: url
  url: https://github.com/gowenrw/astable_badge
  title: gowenrw/astable_badge
  accessed: '2026-09-07'
  note: Confirms open-source hardware (KiCad, Gerbers, art files) under an MIT license.
- kind: url
  url: https://altbier.us/bsidesdfw/
  title: BSidesDFW - altbier.us
  accessed: '2026-09-07'
  note: Confirms the badge was associated with the BSidesDFW 2021 Hardware Hacking Village and its kit/instructions pages.
- kind: url
  url: https://astablebadge.altbier.us/badgekit.html
  title: Astable Badge kit instructions
  accessed: '2026-09-07'
  note: Kit contents (PCB, lanyard, sticker, CR2032, 5 THT LEDs of different colors, resistors, capacitors, 2x 2N2222A transistors, battery holder, optional headers) and assembly steps.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Price, quantity made, and exact PCB solder-mask color were not stated on any source checked. Maker's site says the badge was designed to avoid using an IC due to the 2021 global chip shortage, and its Cyber-Dolphin artwork is themed after Johnny Mnemonic (which is set in the year the badge was made). The badge was tied to a BSidesDFW 2021 Hardware Hacking Village session on the astable multivibrator circuit. Maker (Alt_Bier / gowenrw) has other entries in this archive from later DEF CONs (dc30, dc31, dc32).
last_modified_date: '2026-09-07'
model:
  file: assets/models/bsidesdfw-2021/astable-badge.glb
  method: kicad
  source_file: eda/astable_badge/astable_badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 291220
---

The Astable Badge is a soldering-education badge Alt_Bier (gowenrw on GitHub) built for BSidesDFW 2021 at the request of CyberLowdown, who asked for a badge tied to the con. Rather than use a microcontroller, the badge is built around a classic two-transistor astable multivibrator: with no IC in the design, builders solder in resistors, capacitors, two 2N2222A transistors, and two of five included 3mm LEDs (red, green, blue, yellow, or white) themselves, then use onboard trim potentiometers to adjust the blink speed and test points to probe the circuit with a logic analyzer. The maker has said the IC-free design was a deliberate choice made in response to the global chip shortage happening at the time.

The badge's artwork is a Cyber-Dolphin, styled after Johnny Mnemonic, a film the maker noted is set in 2021 (the badge's release year). It was distributed at BSidesDFW 2021 in connection with the con's Hardware Hacking Village (HHV), which ran a session covering the astable multivibrator circuit used in the badge, though the exact price, quantity produced, and distribution method (kit sale vs. free village drop) were not stated on any page checked.

## Make your own

The hardware is fully open source under an MIT license, with KiCad schematics/PCB files, Gerbers, and the Cyber-Dolphin artwork published in the [astable_badge GitHub repo](https://github.com/gowenrw/astable_badge). The maker's site also hosts a full [assembly walkthrough](https://astablebadge.altbier.us/badgekit.html) covering the through-hole soldering order (resistors, transistors, trim pots, capacitors, LEDs, battery holder, then optional header pins) and the tools needed (a 40-70W iron, 63/37 rosin-core solder, diagonal cutters, and optionally a multimeter or logic analyzer).
