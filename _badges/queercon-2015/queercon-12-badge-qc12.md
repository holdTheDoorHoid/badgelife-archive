---
title: Queercon 12 badge (QC12)
id: queercon-2015-queercon-12-badge-qc12
layout: badge
parent: Queercon 12 (2015)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: queercon-2015
year: 2015
makers:
- name: George Louthan (duplico), animations by Jonathan Nelson
summary: 'A Tamagotchi-homage electronic badge with an OLED menu screen and RF "neighbor" interactions that let nearby badges trade animated flag designs.'
functions: 'Menu-driven OLED interface; RF discovery of nearby badges with shared, animated "flag" designs; interacted with badge base stations (see the companion qc12base project).'
look:
  colors: []
  shape: null
  themes:
  - wearable
tech:
  mcu: MSP430FR5949
  leds: null
  display: OLED graphical display
  connectivity:
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
  open_source: 'yes'
  hardware_url: https://github.com/duplico/qc12
  firmware_url: https://github.com/duplico/qc12
  eda_tool: null
links:
- label: github.com/duplico/qc12
  url: https://github.com/duplico/qc12
  kind: repo
- label: github.com/Queercon/QC12-Badge
  url: https://github.com/Queercon/QC12-Badge
  kind: repo
- label: github.com/duplico/qc12base
  url: https://github.com/duplico/qc12base
  kind: repo
images: []
contact: {}
notes:
- '"Tamagotchi homage" badge on an MSP430FR5949 with an OLED graphical display and RF neighbor interactions that share animated flag designs. Found by the event-year sweep, task queercon.'
status: released
sources:
- kind: url
  url: https://github.com/duplico/qc12
  title: Queercon 12 badge (QC12)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:queercon); event read as ''queercon-2015''.'
- kind: url
  url: https://github.com/duplico/qc12
  title: 'duplico/qc12: Queercon 12 electronic badge'
  accessed: '2026-09-08'
  note: 'README and repo listing confirmed maker, MCU (MSP430FR5949), OLED display, RF neighbor/flag-sharing feature, and CC BY-SA 4.0 (hardware/animations) + BSD 3-clause (software) licensing.'
- kind: url
  url: https://github.com/Queercon/QC12-Badge
  title: 'Queercon/QC12-Badge'
  accessed: '2026-09-08'
  note: 'Confirmed as an org-account mirror of the same firmware repo; no separate hardware (KiCad/Eagle/Gerber) files found in either repo.'
- kind: url
  url: https://github.com/duplico/qc12base
  title: 'duplico/qc12base: Queercon 12 badge base stations'
  accessed: '2026-09-08'
  note: 'Companion base-station project for QC12, referenced for the "RF neighbor interactions" functions field.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, released badge (not just a sweep snippet): duplico''s own GitHub repo and an official Queercon org mirror both describe it. Could not find price, quantity made, LED count/type, battery, PCB color, or a photo of the physical badge in either repo, in a search of Hackaday''s Queercon tag (which covers QC10, QC13-QC16 but has no dedicated QC12 article), or on duplico''s personal site (dupli.co) or badge.lgbt. The GitHub repo is CCS/MSP430 firmware only; no KiCad/Eagle/Gerber hardware files were found, so eda_tool is left null despite hardware_url being set. Status set to "released" (not "listed") because this is confirmed as an actual distributed badge, not just a sheet entry.'
last_modified_date: '2026-09-08'
---

Queercon 12 (2015), DEF CON 23's LGBT sub-conference, issued an electronic badge built around a Tamagotchi-style conceit: an OLED menu screen driven by an MSP430FR5949 microcontroller, with RF "neighbor" interactions that let badges near each other discover one another and trade animated flag designs. It was designed by George Louthan (duplico), the longtime lead of Queercon's badge team, with animation work by Jonathan Nelson.

The badge shipped with a companion base-station project (qc12base) that badges could interact with over the same RF link, extending the neighbor-discovery mechanic beyond badge-to-badge pairing. Both the badge firmware and the animation artwork are open source: the hardware design and animations are released under CC BY-SA 4.0, and the software under a BSD 3-clause license, per the repository's README. No hardware design files (schematics, PCB layout, or Gerbers) were found alongside the firmware in either duplico's repo or the official Queercon org mirror, so specifics like LED count, battery type, board color, price, and production quantity remain undocumented in the sources checked.

## Make your own

Firmware source (Code Composer Studio project targeting the MSP430FR5949) is at [github.com/duplico/qc12](https://github.com/duplico/qc12), mirrored under the Queercon org at [github.com/Queercon/QC12-Badge](https://github.com/Queercon/QC12-Badge). The companion base-station firmware is at [github.com/duplico/qc12base](https://github.com/duplico/qc12base). No published hardware (schematic/PCB) files were located.
