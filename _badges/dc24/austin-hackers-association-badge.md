---
title: AHA Badge
id: dc24-austin-hackers-association-badge
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc24
year: 2016
makers:
- name: Austin Hackers Association
  url: https://github.com/AustinHackers
summary: A DIY laser-tag badge built by the Austin Hackers Association (AHA) hacker group for DEF CON 24 (2016), pairing an e-paper display with an RF radio for over-the-air tag/hit signaling.
functions: Plays a laser-tag-style game over RF (no actual laser/IR emitter found in the sources), shows the wearer's name and status on an e-paper display, and enumerates as a USB mass-storage device for loading content.
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
tech:
  mcu: NXP Kinetis MKL27Z256 (Cortex-M0+)
  leds: null
  display: e-paper (EPD)
  connectivity:
  - sub-ghz
  - usb
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
  open_source: yes
  hardware_url: https://github.com/AustinHackers/ahabadge/tree/master/DEFCON%2024/laser-tag%20badge
  firmware_url: https://github.com/AustinHackers/ahabadge/tree/master/DEFCON%2024/laser-tag%20software
  eda_tool: Eagle
links:
- label: github.com/AustinHackers/ahabadge
  url: https://github.com/AustinHackers/ahabadge
  kind: repo
- label: DEF CON 24 badge folder (schematic, board, firmware)
  url: https://github.com/AustinHackers/ahabadge/tree/master/DEFCON%2024
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/AustinHackers/ahabadge
  title: Austin Hackers Association badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/AustinHackers/ahabadge/master/README.md
  title: 'AustinHackers/ahabadge: README'
  accessed: '2026-09-07'
  note: Confirms this is the "AHA" badge line and that the DEF CON 24 folder holds this year's badge; a v2 exists on a separate branch.
- kind: url
  url: https://raw.githubusercontent.com/AustinHackers/ahabadge/master/DEFCON%2024/README.md
  title: DEFCON 24 badge README
  accessed: '2026-09-07'
  note: Warns that v0/v1 boards can short and destroy the MCU over USB without a fix capacitor; points to the laser-tag software README for build/flash steps.
- kind: url
  url: https://raw.githubusercontent.com/AustinHackers/ahabadge/master/DEFCON%2024/laser-tag%20badge/TODO
  title: laser-tag badge TODO
  accessed: '2026-09-07'
  note: Lists an e-paper display (EPD) and a 5-way switch as existing (if "obsolete") parts, and flags battery design as unfinished.
- kind: url
  url: https://api.github.com/repos/AustinHackers/ahabadge/contents/DEFCON%2024
  title: DEF CON 24 folder listing
  accessed: '2026-09-07'
  note: Folder contains laser-tag badge (Eagle schematic/board), laser-tag software, an RFM69HCW daughterboard folder (sub-GHz radio module), Eagle libraries, and a KSDK_1.2.0 folder (NXP Kinetis SDK).
- kind: url
  url: https://raw.githubusercontent.com/AustinHackers/ahabadge/master/DEFCON%2024/laser-tag%20software/CMakeLists.txt
  title: laser-tag software CMakeLists.txt
  accessed: '2026-09-07'
  note: 'Identifies the exact chip: NXP/Freescale Kinetis MKL27Z256VLH4 (linker script and -DCPU_MKL27Z256VLH4 build flag).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Everything here comes from the maker''s own GitHub repo (AustinHackers/ahabadge); no press coverage, storefront, or price/quantity/availability information was found anywhere, and none of the sources include a photo of the assembled badge itself (the one image in the repo, vregin_cap.jpg, shows a bodge-wire repair capacitor, not the badge). The firmware source (radio.c, RFM69registers.h) confirms an RFM69HCW sub-GHz radio for the "laser tag" gameplay, but no laser/IR component was found, so the tag mechanism is RF-based despite the name. A "version_2.x" branch exists for a later revision, not otherwise explored. Event corrected from ''other'' to DEF CON 24 (dc24) based on the repo''s own DEFCON 24 folder.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/austin-hackers-association-badge/
---

The Austin Hackers Association (AHA), a Texas hacker group, built this badge for DEF CON 24 in 2016 as part of a home-grown laser-tag game. The board runs an NXP Kinetis MKL27Z256 microcontroller (Cortex-M0+) and drives an e-paper display for showing the wearer's name and game status, with an RFM69HCW sub-GHz radio module on a daughterboard handling the over-the-air tag/hit signaling in place of an actual optical emitter. It also enumerates as a USB mass-storage device, letting wearers load images and text onto the badge.

The project's own README flags a hardware bug in the early v0/v1 boards: plugging them into USB could short and destroy the MCU, fixed with a 10uF capacitor added between the VSS and VREGIN pins. A TODO file in the repository notes the e-paper display and 5-way switch were considered obsolete parts even at the time, and that the battery setup (originally sized for the MCU's footprint) was never finalized before the badge shipped. AHA published the full schematic, board files (Eagle), and firmware source, along with a later "version_2.x" revision on a separate branch, but no price, production quantity, or distribution details were found in any available source.

## Make your own

Hardware: the DEF CON 24 badge Eagle schematic and board files, an RFM69HCW daughterboard design, and Eagle component libraries are all in the repo's `DEFCON 24` folder. Firmware: the `laser-tag software` folder holds the full C source (radio, e-paper, USB descriptor, text rendering) built against NXP's KSDK 1.2.0 (also included) via CMake (`build_all.sh` / `build_release.sh`), flashed and debugged with OpenOCD/GDB per the folder's own README.
