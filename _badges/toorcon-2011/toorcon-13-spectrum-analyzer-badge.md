---
title: ToorCon 13 Spectrum Analyzer Badge
id: toorcon-2011-toorcon-13-spectrum-analyzer-badge
layout: badge
parent: ToorCon 13
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: toorcon-2011
year: 2011
makers:
- name: Great Scott Gadgets
  url: https://greatscottgadgets.com/tc13badge/
summary: An RF spectrum-analyzer conference badge for the 2.4 GHz band, using 13 LEDs to show activity across the 13 Wi-Fi channels.
functions: 'Push-button activated RF spectrum analyzer: lights the LED for each 2.4 GHz Wi-Fi channel that has activity, and also picks up Bluetooth, ZigBee, microwave ovens, and other in-band emitters. Sleeps between button presses to save battery.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - measurement
  - hardware tool
tech:
  mcu: Renesas R5F212L4 (R8C/2L)
  leds:
    count: 13
    type: discrete
    note: One LED per 2.4 GHz Wi-Fi channel; an optional large hacking kit adds an LPC1756 for full Ubertooth (Bluetooth monitoring) capability.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given out as the official conference badge to ToorCon 13 (San Diego, October 7-9, 2011) attendees; optional USB-power and Ubertooth hacking kits were sold/available on-site.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/greatscottgadgets/ubertooth/tree/master/hardware/tc13badge
  firmware_url: https://github.com/greatscottgadgets/ubertooth
  eda_tool: null
links:
- label: badge.gallery/badges/toorcon-13-spectrum-analyzer-badge
  url: https://badge.gallery/badges/toorcon-13-spectrum-analyzer-badge
  kind: website
- label: greatscottgadgets.com/tc13badge
  url: https://greatscottgadgets.com/tc13badge/
  kind: website
- label: greatscottgadgets/ubertooth (hardware/tc13badge)
  url: https://github.com/greatscottgadgets/ubertooth/tree/master/hardware/tc13badge
  kind: repo
images:
- file: assets/images/badges/toorcon-2011/toorcon-13-spectrum-analyzer-badge/2503e3a0f6.jpg
  source: "https://greatscottgadgets.com/tc13badge/"
  credit: "Great Scott Gadgets"
  caption: "ToorCon 13 badge PCB diagram"
contact: {}
notes:
- Official ToorCon 13 (2011) badge, a 2.4 GHz RF spectrum-analyzer with 13 LEDs. Found by the event-year sweep, task con-toorcon.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/toorcon-13-spectrum-analyzer-badge
  title: ToorCon 13 Spectrum Analyzer Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-toorcon); event read as ''ToorCon 2011''.'
- kind: url
  url: https://greatscottgadgets.com/tc13badge/
  title: ToorCon 13 Badge - Great Scott Gadgets
  accessed: '2026-09-08'
  note: Maker's own page; confirms function, MCU, LEDs, battery, distribution, hardware/firmware repo location, and badge photo.
- kind: url
  url: https://github.com/greatscottgadgets/ubertooth/blob/master/hardware/tc13badge/README
  title: ubertooth/hardware/tc13badge/README at master
  accessed: '2026-09-08'
  note: Confirms Michael Ossmann/Great Scott Gadgets as the badge's designer within the Ubertooth repository.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Price and total quantity made were not stated on any source found; left empty. The maker''s page copyright notice reads 2009 but the badge itself is confirmed for ToorCon 13, which ran October 7-9, 2011 (matches event id toorcon-2011); treated as a copyright-boilerplate discrepancy, not a redate. Two optional hacking kits (small: adds USB power; large: adds Ubertooth/Bluetooth-monitoring capability) were sold alongside the badge but are not separate archive entries.'
last_modified_date: '2026-09-08'
---

The ToorCon 13 badge, designed by Great Scott Gadgets (Michael Ossmann) for ToorCon San Diego 13 in October 2011, doubles as a simple 2.4 GHz spectrum analyzer. Its 13 LEDs map to the 13 evenly-spaced Wi-Fi channels in the band; pressing the badge's button wakes it briefly to show which channels have activity, and it also reacts to Bluetooth, ZigBee, microwave ovens, and other emitters sharing the band. It runs on a Renesas R5F212L4 (R8C/2L) microcontroller from a CR2032 coin cell and sleeps between button presses to conserve battery.

The badge was handed out as the official ToorCon 13 conference badge. Great Scott Gadgets also offered optional on-site hacking kits: a small kit added USB power, while a large kit supplied the extra parts (including an LPC1756) needed to turn the badge into a functional Ubertooth device for passive Bluetooth monitoring.

## Make your own

Hardware and firmware are open-source and published in the Project Ubertooth GitHub repository under the `hardware/tc13badge` path (code name `tc13badge`). No EDA tool or bill-of-materials link was found in the sources checked; check the repository directly for design files.
