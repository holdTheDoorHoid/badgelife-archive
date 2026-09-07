---
title: FLORIDA_MAN Badge 2018
id: dc26-florida-man-badge-2018
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Jonathan Singer
  url: https://hackaday.io/hacker/244949-jonathan-singer
summary: An unofficial DEF CON 26 badge by Jonathan Singer built from discrete SMD parts on a conch-shaped PCB, with four red and three yellow LEDs, two SPDT slide switches and a 5V linear regulator, with gerbers and pick-and-place files published on Hackaday.io.
functions: ''
look:
  colors: []
  shape: conch shell
  themes: []
tech:
  mcu: none
  leds:
    count: 7
    type: discrete
    note: 4x red clear 0805 SMD LEDs, 3x yellow clear 0805 SMD LEDs
  display: null
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/159719/files
  firmware_url: null
  eda_tool: null
  gerbers_url: https://hackaday.io/project/159719/files
  notes: 'Full Gerber set (top/bottom copper, top/bottom mask, bottom silkscreen, board outline), plus pick-and-place and drill files, published on the Hackaday.io project. No schematic, BOM, or firmware source (the board has no MCU) was found published.'
links:
- label: hackaday.io/project/159719-floridaman-badge-2018
  url: https://hackaday.io/project/159719-floridaman-badge-2018
  kind: hackaday
- label: hackaday.io/project/159719/files
  url: https://hackaday.io/project/159719/files
  kind: hackaday
- label: hackaday.io/project/159719/gallery
  url: https://hackaday.io/project/159719/gallery
  kind: hackaday
images:
- file: assets/images/badges/dc26/florida-man-badge-2018/0e5f89982f.jpg
  source: "https://hackaday.io/project/159719/gallery"
  credit: "Jonathan Singer"
  caption: "The FLORIDA_MAN badge, a conch-shell-shaped PCB"
- file: assets/images/badges/dc26/florida-man-badge-2018/841683eb4f.jpg
  source: "https://hackaday.io/project/159719/gallery"
  credit: "Jonathan Singer"
  caption: "The assembled FLORIDA_MAN badge PCB"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/159719-floridaman-badge-2018
  title: FLORIDA_MAN Badge 2018
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/159719-floridaman-badge-2018
  title: FLORIDA_MAN Badge 2018
  accessed: '2026-09-07'
  note: 'Confirmed maker (Jonathan Singer), event (unofficial DEF CON 26 badge, 2018), and component list (2 SPDT slide switches, 5V linear regulator, capacitors, red/yellow 0805 SMD LEDs).'
- kind: url
  url: https://hackaday.io/project/159719/files
  title: FLORIDA_MAN Badge 2018 - Files
  accessed: '2026-09-07'
  note: 'Listed the 9 published Gerber/manufacturing files, confirming the conch-shaped board outline and that pick-and-place and drill files are published (no schematic or BOM found).'
- kind: url
  url: https://hackaday.io/project/159719/gallery
  title: FLORIDA_MAN Badge 2018 - Gallery
  accessed: '2026-09-07'
  note: 'Source of the two saved photos of the assembled board.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io project page and files list confirm the badge''s design and DEF CON 26 (2018) origin. No price, quantity made, distribution method, or current availability were found anywhere on the project page or in its files/gallery subpages; those fields are left empty rather than guessed. No schematic or BOM file was found alongside the Gerbers. The maker''s Hackaday profile page returned a login wall and could not be checked for other work. "Florida Man" appears to be a recurring unofficial-badge theme used by different makers across several DEF CONs (31, 32, 33, 34 all have separate "Florida Man"-titled entries in this archive); this 2018 board by Jonathan Singer is a distinct, unrelated item from those.'
last_modified_date: '2026-09-07'
---

The FLORIDA_MAN badge is an unofficial DEF CON 26 (2018) badge designed by Jonathan Singer, built as a discrete-component circuit rather than around a microcontroller. The PCB itself is cut in the shape of a conch shell, and its Gerber files (uploaded July 13, 2018) show a two-layer board with a bottom-heavy copper and silkscreen layout consistent with a hand-built SMD assembly.

Electrically, the badge is populated with seven 0805 SMD LEDs (four red, three yellow), two SPDT slide switches, a 5V linear regulator, and supporting capacitors — enough to run simple LED patterns or manual switch-selected lighting without any onboard logic chip. No schematic or firmware is published, consistent with a board that has no MCU.

Singer published a complete Gerber set for the board (top and bottom copper, top and bottom solder mask, bottom silkscreen, and board outline) along with pick-and-place and drill files, making the board reproducible by anyone with access to a PCB fab and SMD assembly. No information on price, production quantity, or how (or whether) it was distributed at DEF CON 26 was found in any of the maker's published pages.

## Make your own

The full Gerber set, pick-and-place coordinates (`conch_pnp.txt`), and drill file (`conch_drill.txt`) are published at [hackaday.io/project/159719/files](https://hackaday.io/project/159719/files). No BOM or schematic accompanies them, so reproducing the board exactly would mean inferring the passive values and LED colors from the pick-and-place file and the photos on the project's gallery page.
