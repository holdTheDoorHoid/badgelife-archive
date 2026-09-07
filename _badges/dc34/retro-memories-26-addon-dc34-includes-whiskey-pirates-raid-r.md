---
title: "Retro Memories 26"
id: dc34-retro-memories-26-addon-dc34-includes-whiskey-pirates-raid-r
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: trueControl
  url: https://basic.truecontrol.org/
summary: An RP2350-based DEF CON 34 badge addon that boots into one of three personalities selectable at power-on -- a nametag/screensaver mode, an emulated classic Mac running After Dark, or a magnet-controlled port of DOOM -- released in three artwork variants (Retro Tech, Whiskey Pirates, Ultra Compact) that share the same board and firmware.
functions: 'Three selectable personalities chosen by holding buttons while powering on: (1) Nametag/screensaver mode -- the nametag itself was not finished in time for DC34, so it only cycles random screensavers, changed by tapping any button; (2) an emulated Mac Plus-ish machine running "After Dark 2.0" on a stripped-down System 2.x; (3) a magnet-controlled port of DOOM (based on the DC32 rp2040-doom fork) played by moving a small neodymium magnet near the board to walk/strafe/turn, rotating the addon to turn, pulling the magnet away to open doors, and tapping the board to fire.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - pirate
  - arcade
tech:
  mcu: RP2350A
  leds:
    count: 4
    type: RGB
    note: rear-firing RGB LEDs for badge/shirt light accents
  display: 1bpp OLED
  connectivity:
  - usb
  battery: null
  sao_version: null
  power: USB-C
  inputs:
  - buttons
  - accelerometer
  - magnetometer
make_your_own:
  open_source: yes
  hardware_url: https://git.trueserve.org/trueControl/dc34-retro-memories-addon
  firmware_url: https://git.trueserve.org/trueControl/dc34-pico-mac-oled
  eda_tool: null
  notes: 'Three separate firmware repos: emulated Mac (dc34-pico-mac-oled), magnet DOOM (dc34-retro-doom-oled), and the incomplete nametag/screensaver firmware (dc34-rtc-wp-addon). Schematics (REV1, color and black-and-white PDFs) are linked from the project page.'
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
links:
- label: basic.truecontrol.org/database/dc34/retro-memories
  url: https://basic.truecontrol.org/database/dc34/retro-memories/
  kind: website
- label: git.trueserve.org/trueControl/dc34-retro-memories-addon (hardware)
  url: https://git.trueserve.org/trueControl/dc34-retro-memories-addon
  kind: repo
- label: git.trueserve.org/trueControl/dc34-pico-mac-oled (Mac firmware)
  url: https://git.trueserve.org/trueControl/dc34-pico-mac-oled
  kind: repo
- label: git.trueserve.org/trueControl/dc34-retro-doom-oled (DOOM firmware)
  url: https://git.trueserve.org/trueControl/dc34-retro-doom-oled
  kind: repo
- label: git.trueserve.org/trueControl/dc34-rtc-wp-addon (nametag firmware)
  url: https://git.trueserve.org/trueControl/dc34-rtc-wp-addon
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- 'The original sheet link (https://basic.truecontrol.org/dc34/retro-memories/) 404s; the live page is at https://basic.truecontrol.org/database/dc34/retro-memories/.'
- 'Title on the maker''s page is just "Retro Memories 26"; the sheet-derived title appended variant/event details in parentheses, kept in the file id/slug only.'
- 'No photos of the physical board were found on the project page or its linked repos -- the page has schematics only, no product images.'
- 'Made for DEF CON 34 (2026, badges delivered 20260727 per the maker''s own deadline log). Price, quantity made, and availability/distribution are not stated anywhere on the maker''s page.'
status: released
sources:
- kind: url
  url: https://basic.truecontrol.org/dc34/retro-memories/
  title: Retro Memories 26 Addon (DC34, includes Whiskey Pirates RAID, Retro Tech DC34 edition, Ultra Compact)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other''. This exact URL 404s.'
- kind: url
  url: https://basic.truecontrol.org/database/dc34/retro-memories/
  title: Retro Memories 26 - trueControl BASIC
  accessed: '2026-09-07'
  note: 'The maker''s actual live project page (correct path includes /database/); source of concept, three-variant split, personalities/controls, hardware specs, and firmware/schematic links.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched both cited sources. Confirmed the sheet''s original URL (https://basic.truecontrol.org/dc34/retro-memories/) 404s, and confirmed the live project page (https://basic.truecontrol.org/database/dc34/retro-memories/) supports every populated field -- MCU (RP2350A), LEDs (4x rear-firing RGB), display (1bpp OLED), USB-C power, accelerometer/magnetometer inputs, the three personalities and their controls (nametag/screensaver unfinished, Mac/After Dark emulator, magnet-controlled DOOM), the three artwork variants (Retro Tech, Whiskey Pirates, Ultra Compact), DEF CON 34 event/year, and all four linked repos (hardware + 3 firmware), which were also checked directly and all return HTTP 200. No price, quantity, or distribution info appears anywhere, and no product photos of the physical board exist in either source, so those fields correctly stay empty. Confidence held at medium (not high) because price/quantity/availability/distribution remain unknown and no photo could be found, per the research guide. Note for a future pass: a separate entry at _badges/dc34/retro-memories-26-addon.md appears to cover this same physical item (same maker/MCU/LEDs/display, sourced from Uberflux with photos, price $55, and sold-out status) -- likely a duplicate that should be merged or cross-referenced, but out of scope for this fact-check task.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/retro-memories-26-addon-dc34-includes-whiskey-pirates-raid-r/
---

Retro Memories 26 is a DEF CON 34 (2026) badge addon from trueControl that began as an RP2040 board meant to show retro-inspired screensavers, reusing design work from a badge being built in parallel. As the board was reshaped and the chip swapped to an RP2350A, the single design split into three artwork variants sharing the same board and firmware: Retro Tech, Whiskey Pirates, and Ultra Compact.

The addon boots into one of three selectable personalities depending on which buttons are held while powering on. A nametag/screensaver mode was not finished in time for the con, so it only cycles random screensavers on tap. A second mode emulates a stripped-down Mac Plus-ish machine, with just enough memory to run "After Dark 2.0" on System 2.x. The third mode is a heavily modified port of DOOM (built on a DC32-era rp2040-doom fork) controlled entirely by moving a small neodymium magnet near the board -- proximity and orientation drive movement and turning, pulling the magnet away opens doors, and tapping the board fires. The board carries an SC7A20H accelerometer, an AK09919C magnetometer, ambient light sensing, four rear-firing RGB LEDs, a 1bpp OLED, USB-C for firmware flashing, and 8 KiB of EEPROM so settings survive a firmware wipe.

Hardware and all three firmwares (Mac emulator, DOOM port, and the incomplete nametag) are published in separate git repos under trueControl's own git server, along with REV1 schematics in color and black-and-white. No pricing, production quantity, or distribution details were published on the project page, and no photos of the finished board were found in any linked source.
