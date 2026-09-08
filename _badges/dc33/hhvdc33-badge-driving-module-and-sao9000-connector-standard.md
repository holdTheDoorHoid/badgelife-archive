---
title: HHVDC33 badge-driving module and SAO9000 connector standard
id: dc33-hhvdc33-badge-driving-module-and-sao9000-connector-standard
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc33
year: 2025
makers:
- name: HHV Technologies / DEF CON Hardware Hacking Village
  url: https://dchhv.org
summary: A badge-driving IC and companion SAO9000 add-on connector standard built for the DEF CON 33 Hardware Hacking Village's CTF challenge, extending the SAO spec with four extra pins and orientation protection.
functions: 'CTF challenge build: attendees assembled an SAO9000 add-on and interfaced it with the HHVDC33 driving chip; the chip drives LEDs with pre-programmed effects and includes an embedded hall-effect sensor.'
look:
  colors:
  - gold
  shape: null
  themes:
  - hardware tool
  - ctf
  - village badge
tech:
  mcu: RP2350
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: 'SAO9000 (SAO plus 4 extra pins, keyed/orientation-protected)'
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution:
  - village
  where: Distributed as a hands-on build at the DEF CON 33 Hardware Hacking Village CTF challenge (Aug 8-10, 2025); limited demonstration units, not sold.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/DCHHV/DC33-HHV-CTF
  firmware_url: https://github.com/DCHHV/DC33-HHV-CTF
  eda_tool: null
links:
- label: dchhv.org/challenges/dc33.html
  url: https://dchhv.org/challenges/dc33.html
  kind: website
- label: DCHHV/DC33-HHV-CTF (GitHub)
  url: https://github.com/DCHHV/DC33-HHV-CTF
  kind: repo
- label: HHVDC33 datasheet (PDF)
  url: https://dchhv.org/assets/challenges/dc33/HHVDC33.pdf
  kind: doc
images:
- file: assets/images/badges/dc33/hhvdc33-badge-driving-module-and-sao9000-connector-standard/ad23ef5adb.jpg
  source: "https://dchhv.org/challenges/dc33.html"
  credit: "DEF CON Hardware Hacking Village (HHV Technologies)"
  caption: "Winner golden HHVDC33 chip"
- file: assets/images/badges/dc33/hhvdc33-badge-driving-module-and-sao9000-connector-standard/80c5837de0.jpg
  source: "https://dchhv.org/challenges/dc33.html"
  credit: "DEF CON Hardware Hacking Village (HHV Technologies)"
  caption: "Completed SAO9000 add-on build"
contact: {}
notes:
- DC33 Hardware Hacking Village challenge centered on the HHVDC33 badge-driving module and the SAO9000 add-on standard (adds four extra pins and orientation protection over standard SAO), with a CTF demo badge for attendees to build against. Found by the event-year sweep, task dc33-saos.
- 'Title kept as the sweep found it; the maker''s own page and repo also use "HHVDC33" and "SAO9000" as the names.'
status: listed
sources:
- kind: url
  url: https://dchhv.org/challenges/dc33.html
  title: HHVDC33 badge-driving module and SAO9000 connector standard
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc33-saos); event read as ''dc33''.'
- kind: url
  url: https://github.com/DCHHV/DC33-HHV-CTF
  title: DCHHV/DC33-HHV-CTF (GitHub)
  accessed: '2026-09-08'
  note: 'Hardware/firmware repo: schematics, gerbers, BOM, STL enclosure files, and RP2350 firmware builds (ELF/HEX/UF2).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Maker''s own event page and GitHub repo confirm the item and describe its function, MCU (RP2350), and open-source files. Price, LED count/type, display, and production quantity were not stated anywhere found. This was a limited CTF demo/build activity rather than a sold product, so get_one fields reflect that.'
last_modified_date: '2026-09-08'
---

The HHVDC33 badge-driving module and its companion SAO9000 connector standard were built by DEF CON Hardware Hacking Village (HHV Technologies) as the centerpiece of the DEF CON 33 (August 8-10, 2025) hardware hacking challenge. The HHVDC33 is described as an advanced badge-driving chip offering "unmatched LED performance" with expanded control options, pre-programmed LED effects, and an embedded hall-effect sensor. The SAO9000 extends the standard Shitty Add-On connector with four extra pins for richer badge-to-addon communication and adds physical orientation protection to prevent miskeyed installs.

Attendees at the HHV village assembled an SAO9000 add-on kit by hand as part of the CTF activity; a small number of demonstration units, including a "winner" gold-plated chip, were shown off rather than sold. Hardware and firmware are open source: the DCHHV/DC33-HHV-CTF GitHub repository holds schematics, PCB layouts, gerbers, a bill of materials, 3D-printable enclosure (STL) files, and firmware for an RP2350 microcontroller in ELF, HEX, and UF2 formats. A datasheet PDF for the HHVDC33 chip is also published on the HHV site.

## Make your own

The GitHub repo (https://github.com/DCHHV/DC33-HHV-CTF) has everything needed to reproduce the build: PCB schematic/layout files, gerbers and BOM for fabrication, STL files for a 3D-printed enclosure, and pre-built RP2350 firmware images (ELF/HEX/UF2, the last of which can be drag-and-drop loaded over USB).
