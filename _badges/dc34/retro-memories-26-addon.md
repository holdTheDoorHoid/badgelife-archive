---
title: Retro Memories 26 addon
id: dc34-retro-memories-26-addon
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: true (trueControl)
  url: https://basic.truecontrol.org/
summary: A DEF CON 34 badge addon from trueControl with a 128x64 OLED and rear-firing RGB LEDs, sold in three retro-computing art variants including a Mac 68K emulator firmware.
functions: Runs a Mac 68K emulator with After Dark 2.0-style screensavers, a nametag mode, and a Doom demo mode with magnet controls; four rear buttons and an accelerometer/magnetometer provide input.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - pop culture
tech:
  mcu: RP2350
  leds:
    count: 4
    type: RGB
    note: rear-firing
  display: 128x64 1-bit OLED
  connectivity:
  - usb
  battery: null
  sao_version: null
  power: USB-C
  inputs:
  - buttons
  - accelerometer
  - magnetometer
get_one:
  price: $55
  price_usd: 55
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold at DEF CON 34 (2026) via Uberflux; listed as sold out with zero remaining in both art variants as of the September 2026 check.
make_your_own:
  open_source: true
  hardware_url: https://git.trueserve.org/trueControl/dc34-retro-memories-addon
  firmware_url: https://git.trueserve.org/trueControl/dc34-pico-mac-oled
  eda_tool: null
  notes: 'Three separate firmware repos: emulated Mac (dc34-pico-mac-oled), magnet DOOM (dc34-retro-doom-oled), and the incomplete nametag/screensaver firmware (dc34-rtc-wp-addon). Schematics (REV1, color and black-and-white PDFs) are linked from the project page.'
links:
- label: uberflux.com/product/TRUE-RM26
  url: https://uberflux.com/product/TRUE-RM26
  kind: store
- label: basic.truecontrol.org (trueControl badge info center)
  url: https://basic.truecontrol.org/
  kind: website
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
images:
- file: assets/images/badges/dc34/retro-memories-26-addon/5322d7a6cb.jpg
  source: https://uberflux.com/product/TRUE-RM26
  credit: trueControl
  caption: Retro Memories 26 addon, product photo
- file: assets/images/badges/dc34/retro-memories-26-addon/17a2a0b7c8.jpg
  source: https://uberflux.com/product/TRUE-RM26
  credit: trueControl
  caption: Retro Memories 26 addon, alternate art variant
contact: {}
notes:
- 'Uberflux. $55, status: sold out.'
- Spotted by a research agent while working on a neighbouring entry (run 2).
- The original sheet link (https://basic.truecontrol.org/dc34/retro-memories/) 404s; the live page is at https://basic.truecontrol.org/database/dc34/retro-memories/.
- Title on the maker's page is just "Retro Memories 26"; the sheet-derived title appended variant/event details in parentheses, kept in the file id/slug only.
- No photos of the physical board were found on the project page or its linked repos -- the page has schematics only, no product images.
- Made for DEF CON 34 (2026, badges delivered 20260727 per the maker's own deadline log). Price, quantity made, and availability/distribution are not stated anywhere on the maker's page.
status: released
sources:
- kind: url
  url: https://uberflux.com/product/TRUE-RM26
  title: Retro Memories 26 addon
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/TRUE-RM26
  title: Retro Memories 26 Addon - Uberflux
  accessed: '2026-09-07'
  note: Confirmed maker, event (DEF CON 34, 2026), price, specs (RP2350, OLED, RGB LEDs, buttons, accelerometer/magnetometer, USB-C), firmware options, and sold-out status.
- kind: url
  url: https://basic.truecontrol.org/
  title: trueControl BASIC - Badge / Addon Service & Information Center
  accessed: '2026-09-07'
  note: 'trueControl''s own badge info site lists "Retro Memories 26" under DC34 @ LVCC with three art variants: Whiskey Pirates RAID, Retro Tech (DC34 edition), and Ultra Compact; confirms it is a DEF CON 34 addon by trueControl.'
- kind: url
  url: https://basic.truecontrol.org/dc34/retro-memories/
  title: Retro Memories 26 Addon (DC34, includes Whiskey Pirates RAID, Retro Tech DC34 edition, Ultra Compact)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other''. This exact URL 404s.'
- kind: url
  url: https://basic.truecontrol.org/database/dc34/retro-memories/
  title: Retro Memories 26 - trueControl BASIC
  accessed: '2026-09-07'
  note: The maker's actual live project page (correct path includes /database/); source of concept, three-variant split, personalities/controls, hardware specs, and firmware/schematic links.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: The maker's own storefront (Uberflux) and trueControl's own badge info site (basic.truecontrol.org) agree this was made for DEF CON 34 (2026). The Uberflux listing describes two purchasable art variants ("Retro Technology" and "Ultra Compact"), while trueControl's own site lists three variants (adding a "Whiskey Pirates RAID" variant) - noted here as a minor disagreement, possibly a variant sold through a different channel (e.g. directly to the Whiskey Pirates crew) rather than via the general Uberflux storefront. The dedicated trueControl page for this addon (basic.truecontrol.org/dc34/retro-memories/) did not load during research, so further detail (BOM, firmware source, exact per-variant unit counts) could not be confirmed. Battery/power spec, SAO header version, and total quantity made are not stated by either source and are left empty. Event corrected from "other" to DEF CON 34 (dc34). Merged with duplicate entry 'Retro Memories 26' (dc34-retro-memories-26-addon-dc34-includes-whiskey-pirates-raid-r).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/retro-memories-26-addon/
- /badges/dc34/retro-memories-26-addon-dc34-includes-whiskey-pirates-raid-r/
---

The Retro Memories 26 addon is a DEF CON 34 (2026) badge addon made by true, under the trueControl name, sold through the Uberflux storefront for $55. It's built around an RP2350 microcontroller with a 128x64 1-bit OLED display, four rear-firing RGB LEDs, four rear-mounted buttons, an accelerometer and magnetometer, ambient light sensing, and USB-C with a built-in boost converter. A small lanyard retention hole lets it hang alongside other DEF CON gear.

The addon leans into a retro-computing theme: its firmware includes a Mac 68K emulator that runs After Dark 2.0-style screensavers, alongside a nametag mode and a Doom demo mode controlled with a magnet. It was sold in two retro-styled art variants through Uberflux - a vector-drawn "Retro Technology" design and a compact Mac-inspired "Ultra Compact" design - with trueControl's own badge info site additionally listing a third "Whiskey Pirates RAID" variant. Both Uberflux-listed variants sold out at the con (52 units of the Ultra Compact design and 16 of the Retro Technology design, per the listing), with the maker noting possible post-con availability through their own webstore.

## Notes merged from the duplicate entry "Retro Memories 26"

Retro Memories 26 is a DEF CON 34 (2026) badge addon from trueControl that began as an RP2040 board meant to show retro-inspired screensavers, reusing design work from a badge being built in parallel. As the board was reshaped and the chip swapped to an RP2350A, the single design split into three artwork variants sharing the same board and firmware: Retro Tech, Whiskey Pirates, and Ultra Compact.

The addon boots into one of three selectable personalities depending on which buttons are held while powering on. A nametag/screensaver mode was not finished in time for the con, so it only cycles random screensavers on tap. A second mode emulates a stripped-down Mac Plus-ish machine, with just enough memory to run "After Dark 2.0" on System 2.x. The third mode is a heavily modified port of DOOM (built on a DC32-era rp2040-doom fork) controlled entirely by moving a small neodymium magnet near the board -- proximity and orientation drive movement and turning, pulling the magnet away opens doors, and tapping the board fires. The board carries an SC7A20H accelerometer, an AK09919C magnetometer, ambient light sensing, four rear-firing RGB LEDs, a 1bpp OLED, USB-C for firmware flashing, and 8 KiB of EEPROM so settings survive a firmware wipe.

Hardware and all three firmwares (Mac emulator, DOOM port, and the incomplete nametag) are published in separate git repos under trueControl's own git server, along with REV1 schematics in color and black-and-white. No pricing, production quantity, or distribution details were published on the project page, and no photos of the finished board were found in any linked source.
