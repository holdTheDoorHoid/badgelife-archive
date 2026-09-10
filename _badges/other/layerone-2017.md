---
title: LayerOne 2017 Electronic Badge
id: other-layerone-2017
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2017
makers:
- name: charliex
  url: https://hackaday.io/charliex
- name: mmca
  role: battery design
summary: A car-hacking educational badge for LayerOne 2017 built around dual CAN bus interfaces, letting attendees sniff, log, and replay CAN packets to learn vehicle-hacking techniques.
functions: CAN bus sniffing, logging, graphing and packet replay for vehicle-hacking games/education; runs a NES emulator; USB host/device; SD card storage; audio out.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - learn to solder
tech:
  mcu: STM32F446
  leds: null
  display: 2.2-2.4" TFT LCD (ILI9341/45)
  connectivity:
  - usb
  battery: 18650 Li-Ion, onboard charging via BQ24075
  sao_version: null
get_one:
  price: $60
  price_usd: 60
  quantity: approximately 400 planned for the 2017 conference
  availability: sold_out
  distribution:
  - purchase
  where: Sold via the maker's Tindie store (charliex6); as of research date the seller listing shows "taking a break" / not accepting orders.
make_your_own:
  open_source: true
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/13262-layerone-2017
  url: https://hackaday.io/project/13262-layerone-2017
  kind: hackaday
  archived: https://web.archive.org/web/20260626022109/https://hackaday.io/project/13262-layerone-2017
- label: tindie.com/products/charliex6/layerone-2017-electronic-badge
  url: https://www.tindie.com/products/charliex6/layerone-2017-electronic-badge/
  kind: store
  archived: https://web.archive.org/web/20260503131646/https://www.tindie.com/products/charliex6/layerone-2017-electronic-badge/
- label: OBD II CAN Bus cable for the badge (Tindie)
  url: https://www.tindie.com/products/charliex6/obd-ii-can-bus-cable-for-layerone-2017-badge/
  kind: store
  archived: https://web.archive.org/web/20260509111158/https://www.tindie.com/products/charliex6/obd-ii-can-bus-cable-for-layerone-2017-badge/
images:
- file: assets/images/badges/other/layerone-2017/2c6a7c83c7.jpg
  source: https://www.tindie.com/products/charliex6/layerone-2017-electronic-badge/
  credit: charliex
  caption: LayerOne 2017 electronic badge, front view
  archived: https://web.archive.org/web/20260503131646/https://www.tindie.com/products/charliex6/layerone-2017-electronic-badge/
contact: {}
notes:
- Made for the LayerOne conference (Los Angeles), which has no matching id in _data/events.yml.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/13262-layerone-2017
  title: LayerOne 2017
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''LayerOne 2017''.'
  archived: https://web.archive.org/web/20260626022109/https://hackaday.io/project/13262-layerone-2017
- kind: url
  url: https://hackaday.io/project/13262-layerone-2017
  title: LayerOne 2017 | Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker (charliex, with mmca on battery design), MCU (STM32F446), display, CAN bus feature set, ~400 units planned, SVN design files.
  archived: https://web.archive.org/web/20260626022109/https://hackaday.io/project/13262-layerone-2017
- kind: url
  url: https://www.tindie.com/products/charliex6/layerone-2017-electronic-badge/
  title: layerOne 2017 Electronic Badge - Tindie
  accessed: '2026-09-07'
  note: Price ($60), seller currently not accepting orders, and product photo.
  archived: https://web.archive.org/web/20260503131646/https://www.tindie.com/products/charliex6/layerone-2017-electronic-badge/
- kind: url
  url: https://www.tindie.com/products/charliex6/obd-ii-can-bus-cable-for-layerone-2017-badge/
  title: OBD II CAN Bus cable for layerOne 2017 badge - Tindie
  accessed: '2026-09-07'
  note: Confirms accessory cable existed for OBD II / J2534 connections for the badge.
  archived: https://web.archive.org/web/20260509111158/https://www.tindie.com/products/charliex6/obd-ii-can-bus-cable-for-layerone-2017-badge/
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No matching LayerOne event id exists in _data/events.yml, so event is left as "other"; this badge was made for the LayerOne conference, 2017. LED count/type, exact hardware/firmware repo URLs, and EDA tool were not stated in a form clean enough to cite precisely (an SVN repo listing exists on the Tindie page and Eagle is referenced on the Hackaday page, but were left unfilled by the original research pass rather than added here, since this pass is fact-checking, not new research). Availability marked sold_out based on the Tindie listing being closed to new orders as of the check date, though this could also reflect a temporary seller break rather than a permanent sellout. Fact-check (2026-09-07): confirmed maker/role, MCU, display, battery/charger IC, CAN bus specs, ~400-unit quantity, price, NES emulator, and image against the cited Hackaday.io and Tindie pages. Removed "sub-ghz" from tech.connectivity — neither cited source mentions any sub-GHz/RF wireless capability; the badge''s
    only radio-adjacent link is the wired CAN bus, which is not sub-GHz RF. All remaining populated fields and body sentences are supported by the cited sources.'
last_modified_date: '2026-09-07'
---

The LayerOne 2017 badge was a car-hacking teaching tool built around an STM32F446 microcontroller and a 2.2–2.4" color TFT display, designed by Hackaday.io user charliex with mmca finishing the battery design. Its centerpiece is a dual CAN bus interface (SN65HVD230 transceivers, 1 Mbps) that let attendees sniff, log, graph, and replay CAN packets as a way of learning vehicle-hacking fundamentals, alongside more conventional badge features like USB host/device support, an SD card slot, a headphone jack, and an 18650 Li-Ion battery with onboard charging.

Roughly 400 units were planned for the 2017 conference. The maker later sold badges directly through a Tindie store for $60, along with a companion OBD II/CAN bus cable accessory for connecting the badge to a real vehicle's OBD II port. As of this research, the Tindie listing shows the seller is not currently accepting orders. Design files were kept in an SVN repository rather than a public GitHub/GitLab link, and the project page mentions multiple firmware experiments, including a NES emulator adapted to use the CAN bus.
