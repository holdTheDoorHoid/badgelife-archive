---
title: Retro Tech DC33 Addon
id: dc33-retro-tech-dc33-addon
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: trueControl
  url: https://basic.truecontrol.org/
summary: A GAT-standard (SAO v1.69bis compatible) addon for the Retro Tech Community at DEF CON 33, with a jogwheel and knob interface and nine RGB LEDs spelling out "RETRO".
functions: Jogwheel (up/down/press) and analog knob act as a virtual toggle/menu system for programming the addon; a UART bootloader and USB connector allow firmware updates; 8Kbit EEPROM stores user configuration.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: CH32X033F8P6
  leds:
    count: 12
    type: RGB
    note: IS31FL3729 LED matrix driver powers 9x RGB LEDs (one per "RETRO" character) plus 3x single-color (white/amber/green) cursor LEDs, with adjustable current control and 8-bit PWM per channel.
  display: none
  connectivity:
  - usb
  - uart
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: $42 preorder
  price_usd: 42.0
  quantity: ''
  availability: sold_out
  distribution:
  - preorder
  - free_drop
  where: 'Preordered through the trueControl webshop for pickup at DEF CON 33 (August 2025); trueControl said they would freely give away roughly 2/3 to 3/4 of the units made to attendees at the Retro Tech Community, with preorders funding the run and guaranteeing pickup.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://git.trueserve.org/trueControl/dc33-retro-tech-addon
  eda_tool: null
links:
- label: basic.truecontrol.org/dc33/retro-tech
  url: https://basic.truecontrol.org/dc33/retro-tech/
  kind: website
- label: basic.truecontrol.org/database/dc33/retro-tech (specs & manual)
  url: https://basic.truecontrol.org/database/dc33/retro-tech/
  kind: doc
- label: git.trueserve.org/trueControl/dc33-retro-tech-addon (firmware)
  url: https://git.trueserve.org/trueControl/dc33-retro-tech-addon
  kind: repo
- label: trueControl Shop listing
  url: https://shop.truecontrol.org/index.php?route=product/product&path=83&product_id=430
  kind: store
images:
- file: assets/images/badges/dc33/retro-tech-dc33-addon/2c69c5d591.jpg
  source: "https://shop.truecontrol.org/index.php?route=product/product&path=83&product_id=430"
  credit: "trueControl"
  caption: "Retro Tech Community GAT addon for DEF CON 33"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- The original front-facing page at basic.truecontrol.org/dc33/retro-tech/ 404s; the working URL is basic.truecontrol.org/database/dc33/retro-tech/ (a "database" prefix was added to the site's path structure).
- A related earlier addon "Retro Tech Community Addon" was made for DC32 (2024); this DC33 version is described by the maker as "a re-issue of the DC32 addon with some enhancements."
status: released
sources:
- kind: url
  url: https://basic.truecontrol.org/dc33/retro-tech/
  title: Retro Tech DC33 Addon
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc33''. This exact URL now 404s.'
- kind: url
  url: https://basic.truecontrol.org/database/dc33/retro-tech/
  title: Retro Tech DC33 Addon - trueControl BASIC
  accessed: '2026-09-07'
  note: Working replacement for the dead link above; gave specs (MCU, LEDs, interface), firmware repo link, and manual link.
- kind: url
  url: https://git.trueserve.org/trueControl/dc33-retro-tech-addon
  title: trueControl/dc33-retro-tech-addon - trueserve Git
  accessed: '2026-09-07'
  note: Firmware repo README; confirmed hardware specs and gave build/flash instructions (MounRiver Studio II, WCH-LinkE). No hardware design files (schematic/PCB) found in the repo, only firmware.
- kind: url
  url: https://shop.truecontrol.org/index.php?route=product/product&path=83&product_id=430
  title: Surprise Retro badge addon at DC33 - trueControl Shop
  accessed: '2026-09-07'
  note: Store listing; gave price ($42 preorder), distribution model (preorder funds a free-giveaway run), pickup-only at DEF CON 33, and the product photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own pages (BASIC docs site, firmware repo, and webshop) all agree on specs and event. Exact quantity made was not stated anywhere found, so get_one.quantity is left empty. No hardware design files (schematic/PCB/Gerbers) were found, only the firmware repo, so make_your_own.open_source is "partial" rather than "yes". look.colors and look.shape were not stated by any source and the single product photo shows the addon in its final case, so left as found rather than guessed from the image.'
last_modified_date: '2026-09-07'
---

The Retro Tech DC33 Addon is a GAT-standard SAO made by trueControl (credited to "true and Cprossu") for the Retro Tech Community at DEF CON 33 in 2025. It is a re-issue of a similar addon trueControl made for the Retro Tech Community at DEF CON 32 the year before, "with some enhancements." The addon runs on a CH32X033F8P6 RISC-V microcontroller and uses an IS31FL3729 LED driver to light nine RGB LEDs — one for each letter of "RETRO" — plus three single-color cursor LEDs in white, amber, and green. A jogwheel (up/down/press) and an analog knob give it a virtual toggle/menu interface reminiscent of old computer peripherals, and aux pins on the SAO header break out the MCU's UART for a bootloader-based firmware update path over USB.

trueControl sold the addon as a $42 preorder through their webshop, with the money funding a production run most of which (roughly two-thirds to three-quarters) was given away for free to attendees of the Retro Tech Community at the con; preordering just reserved a guaranteed unit for in-person pickup at DEF CON 33. The visual design was kept secret ahead of the con, and the maker described it candidly as "a rapidly designed badge addon," created under time pressure and later firmware-polished.

Firmware for the addon is published on trueControl's self-hosted Gitea instance as a MounRiver Studio II (RISC-V) project, flashable with a WCH-LinkE debug probe or via USB with WCHISPTool. No hardware design files (schematic or PCB/Gerbers) were found alongside the firmware, so the hardware side of the project is not confirmed open source.
