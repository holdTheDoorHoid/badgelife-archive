---
title: GPS Hexpansion
id: emf-camp-2026-gps-hexpansion
layout: badge
parent: EMF Camp 2026
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: emf-camp-2026
year: 2026
makers:
- name: TechCabin
  url: https://github.com/TechCabin
  role: hardware and software design
- name: The Machine Shop
  url: https://themachineshop.uk/products/gps-hexpansion
  role: seller
summary: A GPS hexpansion module for the Tildagon badge, built around the L80RE-M37 GPS receiver, that feeds NMEA position data to badge apps over UART.
functions: Reads NMEA sentences ($GNRMC, $GPGGA) from the onboard GPS module and exposes latitude, longitude and fix status to badge apps; used by an official "GPS" app and a "GPSSketcher" drawing app, and by Mat Booth's Speedometer app.
look:
  colors: []
  shape: hexagon
  themes:
  - hardware tool
  - gps
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: one red, one yellow status LED
  display: none
  connectivity:
  - gps
  - uart
  battery: powered by host badge
  sao_version: none
get_one:
  price: £15
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: Listed as sold out on themachineshop.uk as of 2026-09-08.
  distribution:
  - purchase
  where: Sold via themachineshop.uk, an add-on ("hexpansion") for the Tildagon badge used at EMF Camp.
make_your_own:
  open_source: true
  hardware_url: https://github.com/TechCabin/EMFBadge-Hexpansions-GPS
  firmware_url: https://github.com/TechCabin/EMFBadge-Hexpansions-GPS
  eda_tool: KiCad
  license: MIT
  notes: Repo includes KiCad hardware files, Gerbers, and MicroPython software for NMEA parsing; instructions cover programming the hexpansion's EEPROM.
links:
- label: matbooth.co.uk/projects/emf
  url: https://matbooth.co.uk/projects/emf/
  kind: website
- label: TechCabin/EMFBadge-Hexpansions-GPS (GitHub)
  url: https://github.com/TechCabin/EMFBadge-Hexpansions-GPS
  kind: repo
- label: GPS Hexpansion - The Machine Shop
  url: https://themachineshop.uk/products/gps-hexpansion
  kind: store
- label: Tildagon Badge Documentation
  url: https://tildagon.badge.emfcamp.org/
  kind: doc
- label: GPS - Tildagon App Store
  url: https://apps.badge.emfcamp.org/apps/43422242
  kind: doc
images:
- file: assets/images/badges/emf-camp-2026/gps-hexpansion/0c2a31eab8.jpg
  source: https://github.com/TechCabin/EMFBadge-Hexpansions-GPS
  credit: TechCabin
  caption: GPS Hexpansion board, top side, showing the L80RE-M37 GPS module
- file: assets/images/badges/emf-camp-2026/gps-hexpansion/f5fb860098.jpg
  source: https://github.com/TechCabin/EMFBadge-Hexpansions-GPS
  credit: TechCabin
  caption: GPS Hexpansion plugged into a Tildagon badge
contact: {}
notes:
- GPS-equipped Tildagon hexpansion with firmware broadcasting position over the badge event system, later adopted as the official driver; also powers a Speedometer app. Found by the event-year sweep, task emf-addons.
- The sweep's source (Mat Booth's project page) covers his firmware/apps for the hexpansion, not the hardware itself; the physical module is made by TechCabin and sold through The Machine Shop.
status: sold_out
sources:
- kind: url
  url: https://matbooth.co.uk/projects/emf/
  title: GPS Hexpansion
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''EMF Camp 2024''.'
- kind: url
  url: https://github.com/TechCabin/EMFBadge-Hexpansions-GPS
  title: EMFBadge-Hexpansions-GPS (TechCabin)
  accessed: '2026-09-08'
  note: Hardware maker, chip, EEPROM, LEDs, license, open-source files, images; repo created March 2026.
- kind: url
  url: https://themachineshop.uk/products/gps-hexpansion
  title: GPS Hexpansion - The Machine Shop
  accessed: '2026-09-08'
  note: Price (£15), sold-out status, GPS module confirmation.
- kind: url
  url: https://tildagon.badge.emfcamp.org/
  title: Tildagon Badge Documentation
  accessed: '2026-09-08'
  note: Confirms the module is sold by The Machine Shop and that the Tildagon badge (introduced 2024) was reused at EMF Camp 2026.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Event corrected from emf-camp-2024 to emf-camp-2026: the GPS Hexpansion module itself (TechCabin/The Machine Shop) has a GitHub repo created March 2026 and a store listing describing it as for "the EMF2026 Tildagon Badge." The Tildagon badge was introduced at EMF Camp 2024 and deliberately reused at EMF Camp 2026 (per EMF Camp''s own blog and Hackaday), so this is a genuinely separate, later product rather than a mislabel. Mat Booth wrote GPS-consuming firmware/apps (Speedometer) that the sweep''s source page describes, and his firmware reportedly became the basis for the official driver, but he is not the hardware maker. Could not confirm total quantity made or exact release date within 2026.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/emf-camp-2024/gps-hexpansion/
model:
  file: assets/models/emf-camp-2026/gps-hexpansion.glb
  method: kicad
  source_file: KiCAD/hexpansion-L80.kicad_pcb
  generated: '2026-09-10'
  bytes: 177336
---

The GPS Hexpansion is an add-on module for EMF Camp's Tildagon badge, built around a Quectel L80RE-M37 GPS receiver with a built-in patch antenna and a connector for an external antenna with automatic switchover. It carries an M24C16 EEPROM (used to identify the hexpansion to the badge) and two status LEDs (red and yellow). It is designed and sold by TechCabin/The Machine Shop through themachineshop.uk for £15, and was listed as sold out as of this check.

On the software side, the module reads NMEA sentences ($GNRMC, $GPGGA) over UART and exposes latitude, longitude, and fix status to badge apps; an official "GPS" app and a drawing app called "GPSSketcher" are built on top of it in the Tildagon app store. Hardware (KiCad, Gerbers) and firmware are published under the MIT license on GitHub. Separately, EMF Camp hardware hacker Mat Booth wrote his own GPS-consuming firmware and a Speedometer app for the module, which he reports became the basis for the badge's official GPS driver.

The Tildagon badge itself was introduced at EMF Camp 2024 and deliberately designed for reuse, and was brought back for EMF Camp 2026 with a new front board ("Spaceagon"). The GPS Hexpansion's GitHub repository was created in March 2026 and its documentation describes it as built for "the EMF2026 Tildagon Badge," so it is recorded here as a 2026 accessory rather than a 2024 one.
