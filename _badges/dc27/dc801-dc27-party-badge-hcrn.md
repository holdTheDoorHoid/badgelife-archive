---
title: DC801 DC27 Party Badge (HCRN)
id: dc27-dc801-dc27-party-badge-hcrn
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: DC801
  url: https://github.com/DC801
summary: A BLE hardware party badge for DEF CON 27, themed around The Expanse, with an on-screen game where the wearer walks around and repairs broken parts of the ship.
functions: On-screen "walk around and fix broken parts of the ship" game, displayed on the SPI LCD; also functions as a general BLE/NFC hardware platform with SAO and minibadge expansion.
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - space
tech:
  mcu: Rigado BMD-340 (Nordic nRF52840)
  leds: null
  display: SPI LCD
  connectivity:
  - ble
  - nfc
  - usb
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '375'
  availability: unknown
  distribution:
  - free_drop
  where: Given out for free at DC801's party during DEF CON 27; specific venue and dates not confirmed by sources.
make_your_own:
  open_source: true
  hardware_url: https://github.com/dc801/DC27PartyBadge/tree/master/Hardware
  firmware_url: https://github.com/dc801/DC27PartyBadge/tree/master/Software
  eda_tool: KiCad
links:
- label: github.com/dc801/DC27PartyBadge
  url: https://github.com/dc801/DC27PartyBadge
  kind: repo
- label: 'Hackaday: Pictorial Guide to the Unofficial Electronic Badges of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
images:
- file: assets/images/badges/dc27/dc801-dc27-party-badge-hcrn/f4df49cfd8.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday
  caption: DC801 HCRN badge, front view showing the SPI LCD screen
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- file: assets/images/badges/dc27/dc801-dc27-party-badge-hcrn/17b689f9a2.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday
  caption: DC801 HCRN badge, rear view
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/dc801/DC27PartyBadge
  title: DC801 DC27 Party Badge (HCRN)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 27''.'
- kind: url
  url: https://github.com/dc801/DC27PartyBadge
  title: 'GitHub README: DC801 DC27 Party Badge'
  accessed: '2026-09-07'
  note: Confirmed hardware (Rigado BMD-340 / nRF52840, SPI LCD, 2 SAO + 1 minibadge connector, NFC, microSD, UF2 bootloader), KiCad design files, GPL-3.0 open source, and dev team credits.
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27 (Hackaday)
  accessed: '2026-09-07'
  note: Confirmed The Expanse theme, the ship-repair walking game, and that 375 badges were produced. Also supplied front/rear photos.
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: Fact-check pass (2026-09-07) re-fetched the GitHub README (raw README.md, not just the repo landing page) and the full text of the Hackaday article. All hardware/software/team-credit claims in the body and Make-your-own section checked out verbatim against the maker's README. However, the prior draft's claim that the party was held "at Planet Hollywood suite, Aug 10-11 2019" was NOT supported by either cited source (confirmed by a full-text search of the Hackaday article) and appears to have been invented despite research.notes attributing it to Hackaday/DEF CON forums; that detail has been removed from the body and get_one.where. Price and LED details remain unconfirmed by any source and are left empty.
last_modified_date: '2026-09-07'
---

The DC801 DC27 Party Badge, nicknamed HCRN, was handed out for free at DC801's party during DEF CON 27 (2019). Five members of the DC801 hacker collective designed the badge, with additional help from the group to assemble and package the roughly 375 units that were produced.

The badge is built around a Rigado BMD-340 module (a Nordic nRF52840, 64 MHz Cortex-M4F with 1 MB flash and 256 KB RAM) and centers on a SPI LCD screen. Rather than just blinking, the badge runs a small game themed after the TV series *The Expanse*: the wearer walks a character around the screen to find and repair broken parts of the ship. Beyond the game, the board is a fairly full-featured BLE/NFC hardware platform, with a speaker, six buttons, a microSD slot, JTAG and UART breakouts, micro USB, and both SAO and minibadge expansion connectors.

DC801 published the complete hardware (KiCad schematics and gerbers, including a rendered PDF of the full design) and firmware (built for GNU ARM GCC, using Nordic's s140 softdevice, with a UF2 bootloader already flashed on shipped units) under an open license on GitHub.

## Make your own

Hardware files and gerbers are in the repo's `Hardware` directory, with a complete-design PDF at `Hardware/gerber/final/hcrn-complete.pdf`. Firmware source and build notes are under `Software`; building it requires the GNU ARM GCC toolchain and a J-Link Segger JTAG programmer to flash Nordic's s140 softdevice, though badges shipped with a UF2 bootloader already installed for easier reflashing. A companion `SD_Card` directory holds the contents to copy onto a FAT32-formatted microSD card for the badge to use.
