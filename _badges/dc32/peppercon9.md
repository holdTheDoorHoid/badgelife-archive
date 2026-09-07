---
title: PepperCon9
id: dc32-peppercon9
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
summary: A pepper-shaped GAT/SAO addon ("ANARCHY IN THE LVCC") built for the "Peppercon 9" party at DEF CON 32, lit by 64 LEDs arranged in the shape of a pepper.
functions: Two touch sensors on the pepper's "hat" cycle through 6 pepper-shaped LED programs plus a 7th that randomly auto-cycles the first 6 (shown by a blinking aux LED), and separately cycle 3 RGB programs plus off; an onboard ambient light sensor auto-dims the LEDs at night and brightens them in daylight; the chosen programs are saved a few seconds after selection and restored on next power-up.
look:
  colors: []
  shape: pepper
  themes:
  - food
  form_factor: pcb sao
tech:
  mcu: CH32V203G6U6
  leds:
    count: 64
    type: IS31FL3729 LED matrix
    note: 64 LEDs arranged in the shape of a pepper; adjustable current control plus 8-bit PWM per channel.
  display: none
  connectivity: []
  inputs:
  - touch
  - accelerometer
  battery: null
  sao_version: v1.69bis
get_one:
  price: $40.00
  price_usd: 40.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold in person at DEF CON 32 (Whiskey Pirate Crew); no ongoing storefront was found.
make_your_own:
  open_source: partial
  hardware_url: https://git.trueserve.org/trueControl/dc32-peppercon9-addon/src/branch/master/hardware/SCH_peppercon9_gat_REV1.pdf
  firmware_url: https://git.trueserve.org/trueControl/dc32-peppercon9-addon
  eda_tool: null
links:
- label: Peppercon9 Addon - trueControl BASIC
  url: https://basic.truecontrol.org/database/dc32/peppercon9/
  kind: website
- label: trueControl/dc32-peppercon9-addon (trueserve Git)
  url: https://git.trueserve.org/trueControl/dc32-peppercon9-addon
  kind: repo
  archived: https://web.archive.org/web/20260417182626/https://git.trueserve.org/trueControl/dc32-peppercon9-addon
- label: SCH_peppercon9_gat_REV1.pdf (schematic)
  url: https://git.trueserve.org/trueControl/dc32-peppercon9-addon/src/branch/master/hardware/SCH_peppercon9_gat_REV1.pdf
  kind: doc
- label: dc32-peppercon9-addon v0.0.1-dc32 release (firmware binaries)
  url: https://git.trueserve.org/trueControl/dc32-peppercon9-addon/releases
  kind: repo
images: []
contact:
  handles:
  - '@whiskeyhackers'
  raw:
  - link on twitter
notes:
- Cash on-site right now. If you want to. pay with a card, True will be available Wednesday night at a location TBD while he is assembling badges. Check twitter link for more information.
status: released
sources:
- kind: sheet
  event: dc32
  row: 115
  updated: ''
- kind: url
  url: https://basic.truecontrol.org/database/dc32/peppercon9/
  title: Peppercon9 Addon - trueControl BASIC
  accessed: '2026-09-07'
  note: Maker's own project page; source for the summary, MCU/LED-driver specs, LED count and shape, sensors, user manual (touch programs, ambient dimming, saved settings), and the firmware repo clone URL. Confirms the addon was made specifically for a "Peppercon 9" party at DEF CON 32.
- kind: url
  url: https://git.trueserve.org/trueControl/dc32-peppercon9-addon
  title: trueControl/dc32-peppercon9-addon - trueserve Git
  accessed: '2026-09-07'
  note: Confirms firmware (MounRiver Studio / WCH CH32V RISC-V project) and a hardware/ directory containing a board schematic; one tagged release, "v0.0.1-dc32 - Shipping Release," dated 2024-08-08, with compiled firmware binaries attached.
  archived: https://web.archive.org/web/20260417182626/https://git.trueserve.org/trueControl/dc32-peppercon9-addon
- kind: url
  url: https://git.trueserve.org/trueControl/dc32-peppercon9-addon/src/branch/master/hardware/SCH_peppercon9_gat_REV1.pdf
  title: SCH_peppercon9_gat_REV1.pdf
  accessed: '2026-09-07'
  note: Confirmed the schematic PDF exists in the hardware/ directory of the repo (linked, not opened as a document).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The maker''s own trueControl BASIC page and git.trueserve.org repo confirm the core technical facts (MCU, LED driver/count, sensors, UI, and that it shipped for DEF CON 32), but no photo of the physical item was found anywhere reachable: the trueControl page has no embedded images, no Hackaday.io project exists for it (unlike the same maker''s "Flames" addon), and whiskeypirates.com could not be fetched (expired TLS certificate). PCB/solder-mask color, exact quantity made, and current availability are not stated by the maker anywhere found; the $40 price and "cash on-site" distribution detail come only from the community sheet and could not be independently confirmed. Session web-search quota was exhausted and Google/Bing/DuckDuckGo/web.archive.org fetches were all blocked or unusable for this task; the maker''s own site (found via a sibling entry, dc32-flames) was the actual source. Connectivity/i2c was not explicitly stated on the maker''s page for this item (unlike the sibling
    "Flames" addon) so tech.connectivity is left empty rather than assumed.'
last_modified_date: '2026-09-07'
---

Peppercon9, subtitled "ANARCHY IN THE LVCC," is a pepper-shaped GAT/SAO addon built by the Whiskey Pirate Crew (posting as "trueControl"/"True," the same longtime DEF CON badge-hacking group behind that year's "Flames" addon and the Infinite WiFi Portal) for a "Peppercon 9" gathering at DEF CON 32. It is a fully custom SAO v1.69bis-compatible board: a WCH CH32V203G6U6 RISC-V microcontroller (32 KB flash, 10 KB RAM, built-in USB bootloader) drives an IS31FL3729 LED matrix lighting 64 LEDs arranged in the outline of a pepper, alongside a LIS2DW accelerometer and an ambient light sensor.

Two touch sensors on the pepper's "hat" cycle through six pre-programmed pepper-lighting patterns, plus a seventh mode that randomly auto-cycles the first six (flagged by a blinking indicator LED), and separately step through three RGB color programs plus off. The board automatically compensates its brightness for the room — dimmer at night, brighter in daylight — and remembers the last-selected programs across power cycles. The maker's own build notes are candid that it was finished in a rush before the con ("there's probably bugs... in the code, not in the pepper. Actually there are hardware bugs in the pepper but we won't talk about those here").

It was sold in person at DEF CON 32 for $40 cash (per the community sheet); no ongoing storefront listing was found. Firmware (a MounRiver Studio / WCH CH32V project) and a board schematic PDF are published in the maker's self-hosted git repository, with one tagged "Shipping Release" (v0.0.1-dc32) carrying compiled firmware binaries — but no Gerbers, BOM, or full CAD source were found alongside them, and no photo of the finished piece could be located.

## Make your own

Firmware and a schematic are published at `git.trueserve.org/trueControl/dc32-peppercon9-addon` (clone with `git clone https://git.trueserve.org/trueControl/dc32-peppercon9-addon`); firmware builds with MounRiver Studio (WCH's free IDE for its RISC-V parts). The hardware/ directory holds a board schematic PDF but no Gerbers or BOM, so a from-scratch rebuild would require redrawing the board.
