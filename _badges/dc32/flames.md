---
title: Flames
id: dc32-flames
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: Whiskey Pirate Crew (not badgelife)
  url: https://basic.truecontrol.org/
summary: A plane-shaped SAO satirizing Boeing's safety and quality-control failures, with a blue 737-outline PCB, an acrylic flame overlay, and a lit-up "BOEING" tail logo.
functions: Two onboard buttons cycle five "flames" animation modes (flame flicker, rainbow puke, flasher, a random auto-cycle of the three, and off) and three brightness levels for a text/logo mode; the active mode is saved automatically after a short delay.
look:
  colors:
  - blue
  - red
  - orange
  - clear
  themes:
  - meme
  - logo
  form_factor: pcb sao
tech:
  mcu: CH32V203G6U6
  leds:
    count: null
    type: RGB
    note: AW20036 LED-matrix driver (3x12 channels) powering RGB pixels plus dedicated orange top LEDs; adjustable current control with 8-bit PWM and 6-bit per-channel current.
  display: none
  connectivity:
  - usb
  - i2c
  inputs:
  - buttons
  battery: null
  sao_version: v1.69bis
get_one:
  price: $40.00
  price_usd: 40.0
  quantity: a couple dozen (assembled for Supercon 8, per the maker's build log)
  availability: unknown
  distribution:
  - purchase
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://cdn.hackaday.io/files/1985358494121440/SCH_flames_gat_REV1.pdf
  firmware_url: https://git.trueserve.org/trueControl/dc32-flames-addon
  eda_tool: null
links:
- label: hackaday.io/project/198535-flames
  url: https://hackaday.io/project/198535-flames
  kind: hackaday
  archived: https://web.archive.org/web/20260310103338/https://hackaday.io/project/198535-flames
- label: hackaday.io/project/198535/logs
  url: https://hackaday.io/project/198535/logs
  kind: hackaday
- label: basic.truecontrol.org/database/dc32/boeing-flames
  url: https://basic.truecontrol.org/database/dc32/boeing-flames/
  kind: website
- label: git.trueserve.org/trueControl/dc32-flames-addon
  url: https://git.trueserve.org/trueControl/dc32-flames-addon
  kind: website
  archived: https://web.archive.org/web/20260417182652/https://git.trueserve.org/trueControl/dc32-flames-addon
- label: cdn.hackaday.io/files/1985358494121440/SCH_flames_gat_REV1.pdf
  url: https://cdn.hackaday.io/files/1985358494121440/SCH_flames_gat_REV1.pdf
  kind: hackaday
images:
- file: assets/images/badges/dc32/flames/05ba189a16.jpg
  source: https://hackaday.io/project/198535-flames
  credit: trueControl (Whiskey Pirate Crew)
  caption: Flames SAO, plane-shaped Boeing-satire addon
  archived: https://web.archive.org/web/20260310103338/https://hackaday.io/project/198535-flames
- file: assets/images/badges/dc32/flames/2fd376740f.jpg
  source: https://hackaday.io/project/198535-flames
  credit: trueControl (Whiskey Pirate Crew)
  caption: Flames SAO, alternate angle showing the flame acrylic and Boeing tail logo
  archived: https://web.archive.org/web/20260310103338/https://hackaday.io/project/198535-flames
contact: {}
notes: []
status: released
sources:
- kind: sheet
  event: dc32
  row: 116
  updated: ''
- kind: url
  url: https://hackaday.io/project/198535-flames
  title: '"Flames" - Hackaday.io project page'
  accessed: '2026-09-06'
  note: Description, maker (user "true"), MCU/LED-driver specs, event context (Supercon 8 SAO contest), and project photos.
  archived: https://web.archive.org/web/20260310103338/https://hackaday.io/project/198535-flames
- kind: url
  url: https://hackaday.io/project/198535/logs
  title: '"Flames" - Hackaday.io build logs'
  accessed: '2026-09-06'
  note: Confirms roughly two dozen units were assembled; quote on intent/ambiguity of the joke.
- kind: url
  url: https://basic.truecontrol.org/database/dc32/boeing-flames/
  title: '"Flames" Addon - trueControl BASIC'
  accessed: '2026-09-06'
  note: Maker's own page for the addon, listed under the DC32 @ LVCC menu; confirms SAO v1.69bis compatibility, CH32V203G6U6 MCU, AW20036 LED driver, two-button UI, and the five flame-animation / brightness user manual; links the firmware git repo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Maker's own trueControl BASIC page files this addon under "DC32 @ LVCC," confirming the DC32 event tag even though the Hackaday.io project log describes the units being assembled/soldered in the run-up to Supercon 8 (Oct 2024) — the two events are close together and the design appears to have served both. LED count and exact battery/power path (SAO-header vs USB-only) were not stated by the maker, so those fields are left null. Current sale availability could not be confirmed (no storefront found); price of $40 is from the community sheet.
last_modified_date: '2026-09-06'
---

"Flames" is a Simple Add-On built by trueControl (posting as "true" on Hackaday.io, part of the self-described "Whiskey Pirate Crew," a longtime DEF CON badge-hacking group that is explicit about not being "badgelife" in the commercial sense). The SAO is a dig at Boeing: a blue PCB engraved with a 737 outline and the Boeing logo sits under a clear acrylic overlay engraved with flames, so the plane appears to be on fire when illuminated. The maker's own build log leans hard into the joke, calling the project "made in haste" and "shoehorned in available parts" as a knowing parallel to criticism of Boeing's engineering and quality-control culture, and dedicating the piece to "remembering mismanagement" and "remembering lives lost."

Under the humor, it is a fully custom SAO: a WCH CH32V203G6U6 RISC-V microcontroller (32 KB flash, 10 KB RAM, built-in USB bootloader) drives an Awinic AW20036 LED-matrix driver that lights RGB pixels behind the flame artwork plus dedicated orange LEDs, all controlled over I2C per the GAT Addon / SAO v1.69bis standard. Two onboard buttons switch between five animation modes — flame flicker, a rainbow "puke" mode, a flasher, a random auto-cycling mode, and off — plus three brightness levels for a secondary text/logo mode, with the last-used setting saved automatically. The maker assembled roughly two dozen units, built and sold around DEF CON 32 and also carried into Supercon 8 the same year. Firmware is published on the maker's self-hosted git server, and a schematic PDF is posted to the Hackaday.io project page, though no complete hardware design-file release (Gerbers/BOM) was found.

## Make your own

Firmware and build notes are published at `git.trueserve.org/trueControl/dc32-flames-addon` (clone with `git clone https://git.trueserve.org/trueControl/dc32-flames-addon`), and the schematic is posted as a standalone PDF on Hackaday.io. No Gerbers, BOM, or CAD source were found published alongside these, so a from-scratch rebuild would require redrawing the board from the schematic.
