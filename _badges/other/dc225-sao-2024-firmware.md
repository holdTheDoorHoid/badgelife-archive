---
title: DC225 SAO 2024
id: other-dc225-sao-2024-firmware
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2024
makers:
- name: DC225
  url: https://defcon225.org/
summary: 'A CTF-style Shitty Add-On built for the DC225 (Baton Rouge, LA) DEF CON group''s 2024 meetup, controlled over IR.'
functions: 'Receives IR remote commands to reveal CTF flags, run a "disco" LED animation mode, and switch the onboard LED between preset colors (green, blue, purple, yellow, white).'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
  - village badge
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - ir
  battery: null
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ynots0ups/DC225_SAO_2024/blob/main/DC225-SAO-v2024-3_KiCad.zip
  firmware_url: https://github.com/ynots0ups/DC225_SAO_2024
  eda_tool: KiCad
links:
- label: github.com/ynots0ups/DC225_SAO_2024
  url: https://github.com/ynots0ups/DC225_SAO_2024
  kind: repo
images: []
contact: {}
notes:
- 'Title on the community sheet was "DC225_SAO_2024 firmware"; the repo README calls the underlying project the "2024 DC225 Shitty Add-on CTF."'
status: released
sources:
- kind: url
  url: https://github.com/ynots0ups/DC225_SAO_2024
  title: DC225_SAO_2024 firmware
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 2024''.'
- kind: url
  url: https://github.com/ynots0ups/DC225_SAO_2024
  title: 'ynots0ups/DC225_SAO_2024: Firmware for the 2024 DC225 Shitty Add-on CTF'
  accessed: '2026-09-07'
  note: 'Repo contents (README, KiCad zip, .ir command list, firmware-special folder) confirm it is an IR-controlled CTF SAO with a KiCad v2024-3 PCB design; no chip/LED part numbers, price, quantity, or hardware photos given.'
- kind: url
  url: https://defcon225.org/
  title: DEFCON225 (DC225) | Baton Rouge, LA
  accessed: '2026-09-07'
  note: 'Confirms DC225 is a local DEF CON group (area code 225, Baton Rouge, LA) rather than the annual DEF CON conference; this SAO was made for the group''s own 2024 meetup/CTF, not for DEF CON 32.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'DC225 is a local DEF CON group (DCG) based in Baton Rouge, LA, not the annual DEF CON convention, so this stays filed under "other" rather than dc32 (DEF CON 32, 2024) -- there is no matching event id in events.yml for DC group meetups. The GitHub repo has firmware, a KiCad PCB (v2024-3), and an IR command list (flag-reveal, disco mode, color-change) but no README beyond the IR command table, no maker name beyond the group/GitHub handle "ynots0ups", no chip/LED part numbers, price, production quantity, or availability info, and no photos of the physical SAO (only a generic auto-generated GitHub social-preview card, not saved as an image). Left tech.mcu, tech.leds, tech.display, tech.battery, look.colors/shape, and get_one fields empty/null since no source stated them.'
last_modified_date: '2026-09-07'
---

The DC225 SAO 2024 is a Shitty Add-On built by the DC225 DEF CON group -- a Baton Rouge, Louisiana-based local DEF CON group covering the 225 area code and surrounding region -- for their own 2024 meetup. Unlike badges made for the annual DEF CON convention in Las Vegas, this one was designed for the group's own gathering, and its firmware README describes it as built for a "Shitty Add-on CTF."

The SAO is controlled over infrared: sending specific IR codes reveals CTF flags, triggers a "disco" LED animation mode, or switches an onboard LED between five preset colors (green, blue, purple, yellow, white). The hardware itself is a custom KiCad PCB (design revision v2024-3), and the GitHub repository publishes both that KiCad design and the firmware/IR command set, though it stops short of naming the specific MCU or LED parts used.

## Make your own

The maker's GitHub repository (github.com/ynots0ups/DC225_SAO_2024) includes a KiCad PCB design (`DC225-SAO-v2024-3_KiCad.zip`), firmware source, a `firmware-special` variant folder, and an `.ir` file listing the IR command codes for the flag, disco, and color-change modes -- enough to reproduce the hardware and firmware, though no bill of materials or assembly instructions are included.
