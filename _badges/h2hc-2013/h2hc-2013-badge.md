---
title: H2HC 2013 Badge
id: h2hc-2013-h2hc-2013-badge
layout: badge
parent: H2HC 2013
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: h2hc-2013
year: 2013
makers:
- name: Great Scott Gadgets
  url: https://www.greatscottgadgets.com/h2hc2013badge/
summary: A USB-enabled ARM Cortex-M3 development board built by Great Scott Gadgets for the 10th-anniversary H2HC conference in Brazil, doubling as an experimental prototype for a next-generation GoodFET.
functions: 'Ships with no firmware, only the LPC1343''s ROM USB Mass Storage bootloader: plug in over USB, drag a firmware.bin onto the exposed drive, and press reset to run it. A TARGET pin header is laid out for future GoodFET-compatible use, though GoodFET firmware for it was never written.'
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - hardware tool
tech:
  mcu: LPC1343
  leds: null
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to attendees of H2HC 2013 in Brazil.
make_your_own:
  open_source: yes
  hardware_url: http://goodfet.sourceforge.net/
  firmware_url: null
  eda_tool: KiCad
  notes: 'KiCad design files are in the GoodFET SVN repo under contrib/gflpc1343/h2hc2013badge/. No project-specific firmware existed at launch; the maker''s page instead points to the LPC1343 Code Base as a starter project.'
links:
- label: badge.gallery/series/h2hc
  url: https://badge.gallery/series/h2hc
  kind: website
- label: Great Scott Gadgets - H2HC 2013 Badge
  url: https://www.greatscottgadgets.com/h2hc2013badge/
  kind: website
  note: "Maker's own project page: description, bootloader/dev setup instructions, open-source hardware statement."
images: []
contact: {}
notes:
- LPC1343 ARM development conference badge for H2HC 2013. Found by the event-year sweep, task con-ekoparty.
- 'Sheet listed the maker as "Unspecified (H2HC)"; the badge''s own project page identifies the maker as Great Scott Gadgets.'
status: released
sources:
- kind: url
  url: https://badge.gallery/series/h2hc
  title: H2HC 2013 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''H2HC 2013''.'
- kind: url
  url: https://www.greatscottgadgets.com/h2hc2013badge/
  title: H2HC 2013 Badge - Great Scott Gadgets
  accessed: '2026-09-08'
  note: "Maker's own project page; source for maker identity, chip, bootloader/USB behavior, open-source hardware/KiCad location, and event context (10th H2HC anniversary, Brazil)."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'No images of the physical badge were found on either the maker''s page or badge.gallery. Price, quantity made, LED count, and a project-specific firmware repo are not stated anywhere found and are left empty. No storefront or press coverage located beyond the two sources above.'
last_modified_date: '2026-09-08'
---

The H2HC 2013 Badge was made by Great Scott Gadgets to mark the 10th anniversary of the Hackers to Hackers Conference (H2HC) in Brazil. It is a bare USB-enabled ARM Cortex-M3 development board built around NXP's LPC1343, intended less as a wearable badge and more as an approachable entry point into embedded ARM development for conference attendees.

Out of the box the badge runs only the LPC1343's built-in ROM bootloader, which presents itself as a USB Mass Storage drive holding a single `firmware.bin` file; overwriting that file and pressing reset loads and runs the attendee's own code. Great Scott Gadgets' project page documents toolchain setup (the GNU ARM embedded GCC toolchain) and a Linux-specific workaround (the `simpleflash` tool from the r0ket project) for flashing, since the stock bootloader was apparently only tested on Windows.

The board is built on "gflpc1343," described as an experimental GoodFET design also known as GreatFET, and carries a TARGET pin header meant for future compatibility with existing GoodFET tools — though no GoodFET-specific firmware for the badge itself was written. It is open-source hardware, with KiCad design files published in the GoodFET SourceForge SVN repository. No pricing, quantity-made, or press coverage was found beyond the maker's own page and its badge.gallery listing.
