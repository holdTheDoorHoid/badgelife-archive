---
title: SAO Demo Controller V2
id: supercon-2024-sao-demo-controller-v2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Andy Geppert
  url: https://hackaday.io/project/198034-sao-demo-controller-v2
  role: designer
- name: VinicioGonzalez
  role: team member
summary: A small inline SAO built around an RP2040 that lets developers test and demonstrate I2C-based SAOs that need "smarts" but don't have a microcontroller of their own built in.
functions: Acts as an intermediary "brain" between a host badge and a downstream SAO, letting a maker prototype and demo an I2C-based SAO design before it has to work with a real badge's firmware.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: RP2040
  leds:
    count: 1
    type: RGB
    note: Built into the Waveshare RP2040-Zero module used as the base board.
  display: none
  connectivity:
  - i2c
  - usb
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Maker said in Hackaday.io project comments that it would be sold on Tindie; a direct listing link was not found during this pass.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ageppert/SAO_Demo_Controller
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/198034-sao-demo-controller-v2
  url: https://hackaday.io/project/198034-sao-demo-controller-v2
  kind: hackaday
- label: github.com/ageppert/SAO_Demo_Controller
  url: https://github.com/ageppert/SAO_Demo_Controller
  kind: repo
images:
- file: assets/images/badges/supercon-2024/sao-demo-controller-v2/cca7d00671.jpg
  source: https://hackaday.io/project/198034-sao-demo-controller-v2
  credit: Andy Geppert
  caption: SAO Demo Controller V2 board
- file: assets/images/badges/supercon-2024/sao-demo-controller-v2/dd69c4c5b4.jpg
  source: https://hackaday.io/project/198034-sao-demo-controller-v2
  credit: Andy Geppert
  caption: SAO Demo Controller V2 in use with an SAO attached
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198034-sao-demo-controller-v2
  title: SAO DEMO Controller V2
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 SAO Contest entry (test/demo controller for SAOs)''.'
- kind: url
  url: https://hackaday.io/project/198034-sao-demo-controller-v2
  title: SAO Demo Controller V2 - Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed maker (Andy Geppert, with VinicioGonzalez), Supercon 8 (2024) SAO Contest entry, RP2040-Zero base, single onboard RGB LED, V2 feature list, and gallery images; page states it would be sold on Tindie.
- kind: url
  url: https://github.com/ageppert/SAO_Demo_Controller
  title: ageppert/SAO_Demo_Controller GitHub repository
  accessed: '2026-09-07'
  note: Confirms hardware design files are published (repo shows v1.0/2.0/3.X hardware folders); no README details on license, BOM, or pricing were found, and no firmware repository was located.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io project and GitHub repo confirm the core facts (who, what, event, MCU). Price, quantity made, exact availability status, license, and a working Tindie listing link were not found in this pass -- left empty rather than guessed. Event corrected from supercon-2025 to supercon-2024: the project page states it was made for "Supercon 8: SAO Contest", which is Hackaday Supercon 8 (2024) per _data/events.yml, not Supercon 2025. A second, differently-slugged Hackaday.io page (hackaday.io/project/198034-sao-demo-controller, no "-v2") appears to be the same project, possibly an earlier/alternate URL for the same listing.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/supercon-2025/sao-demo-controller-v2/
model:
  file: assets/models/supercon-2024/sao-demo-controller-v2.glb
  method: kicad
  source_file: Electronic Design/SAO Demo Controller V4 Design Files KiCAD 10/SAO_Demo_Controller.kicad_pcb
  generated: '2026-09-10'
  bytes: 489128
---

The SAO Demo Controller V2 is a small inline board built by Andy Geppert (with teammate VinicioGonzalez) around a Waveshare RP2040-Zero module. Rather than being a badge or SAO meant to be worn, it is a development tool: it sits between a host badge and a downstream SAO over I2C, giving the downstream SAO the "smarts" it doesn't have of its own so a maker can test and demo an I2C-based SAO design before wiring it into a real badge's firmware. It carries a right-angle SAO connector, dual QWIIC/STEMMA QT sockets for I2C accessories, reset and boot buttons, and USB-C for power and programming, plus the single onboard RGB LED that comes with the RP2040-Zero module.

It was submitted to the SAO Contest at Supercon 8 (2024), and V2 refines an earlier V1 design with improved power routing, a repositioned SAO output for easier access, selectable GPIO mapping, and a voltage divider for monitoring power. The maker's Hackaday.io project page indicates a later V3.X revision adds further protection for using multiple power inputs at once.

Hardware design files are published on GitHub, so the project counts as at least partially open source, though this pass did not find a published BOM, license file contents, or firmware repository, and no confirmed price or unit count. The maker mentioned in project comments that it would be sold on Tindie, but a working storefront link was not located.
