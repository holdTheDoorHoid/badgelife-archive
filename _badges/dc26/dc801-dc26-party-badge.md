---
title: DC801 DC26 Party Badge
id: dc26-dc801-dc26-party-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: DC801
  url: https://github.com/dc801
summary: A BLE-enabled hardware badge DC801 built for DEF CON 26, built around a Rigado BMD-300 (Nordic nRF52832) module with an SPI LCD, speaker, seven buttons, microSD storage, and two SAO/minibadge headers.
functions: Firmware and specific badge functions ("what's it do? Awesome things") are not documented in the repo README beyond pointing to the Software directory; concrete functions such as games or CTF elements were not found.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: nRF52832 (Rigado BMD-300 module)
  leds: null
  display: SPI LCD
  connectivity:
  - ble
  battery: LiPo (MCP73831 charger)
  sao_version: null
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/dc801/DC26PartyBadge/tree/master/Hardware
  firmware_url: https://github.com/dc801/DC26PartyBadge/tree/master/Software
  eda_tool: KiCad
links:
- label: github.com/dc801/DC26PartyBadge
  url: https://github.com/dc801/DC26PartyBadge
  kind: repo
- label: Source files (GitHub)
  url: https://github.com/hamster/DC26PartyBadge
  kind: hardware
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/dc801/DC26PartyBadge
  title: DC801 DC26 Party Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 26''.'
- kind: url
  url: https://raw.githubusercontent.com/dc801/DC26PartyBadge/master/README.md
  title: DC801 DC26 Party Badge README
  accessed: '2026-09-07'
  note: Confirms hardware spec (Rigado BMD-300/nRF52832, SPI LCD, speaker, 6 buttons + 1 hidden, microSD, 2 SAO connectors, 2 minibadges, LiPo charger, KiCad design) and that firmware/hardware are both published open source; does not state price, quantity, or exact release date.
- kind: url
  url: https://api.github.com/repos/dc801/DC26PartyBadge/contents/Hardware
  title: DC26PartyBadge Hardware directory listing
  accessed: '2026-09-07'
  note: Confirms KiCad board file (named "dragon-joke"), BOM.xlsx, and a Hardware/3d folder of component STEP/SLDPRT models; no rendered photos or PCB renders found in the repo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Only source found is the maker's own GitHub repo; no press coverage, storefront, or photos of the assembled badge were located. Price, quantity made, and exact distribution method (party badge implies free/attendee giveaway at a DC801 event, but this is not stated by the source) are unknown. LED presence/count is not mentioned anywhere in the repo. The KiCad board file is named "dragon-joke" but no shape/theme claim is made from that alone. No image URLs were found to save.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/dc801-dc26-party-badge.glb
  method: kicad
  source_file: Hardware/dragon.kicad_pcb
  generated: '2026-09-07'
  bytes: 475040
---

The DC801 DC26 Party Badge is a Bluetooth Low Energy hardware badge that the Denver-area hacker group DC801 built for DEF CON 26 (2018). It is built around a Rigado BMD-300 module (a Nordic nRF52832 with a 16 MHz Cortex-M4F core, 512 kB flash, 64 kB RAM) and packs in a fair amount of I/O for a party badge: an SPI LCD screen, a speaker, six buttons plus one hidden button, a microSD card slot, micro USB, a JTAG header, and two SAO connectors alongside two minibadge headers. Power comes from a LiPo battery managed by an MCP73831 charger.

Both the hardware (KiCad schematics and board files, including 3D step models of components) and firmware are published on GitHub. The README does not spell out what the badge's software actually does beyond a joking "Awesome things, that's what!", pointing instead to the Software directory for specifics, and no assembled-badge photos, press coverage, or storefront listings were found to confirm price, quantity produced, or how it was distributed at the con.

## Make your own

Hardware design files (KiCad) and a BOM are in the repo's `Hardware` directory, and firmware (built with GNU ARM GCC, targeting Nordic's S132 softdevice, flashed via a Segger J-Link) is in `Software`. SD card contents to accompany the badge are provided in `SD_Card` and should be copied onto a FAT32-formatted card.
