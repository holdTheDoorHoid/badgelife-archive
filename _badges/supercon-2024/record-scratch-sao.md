---
title: Record Scratch SAO
id: supercon-2024-record-scratch-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Applied Procrastination
  url: https://hackaday.io/AppliedProc
summary: An RP2040-based SAO with four circular capacitive touch pads, a MAX98357A I2S amplifier and a tiny speaker that lets you scratch a vinyl-record graphic to make record-scratch sounds, routed on a single layer and built for the Supercon 8 SAO Contest.
functions: Scratching the four capacitive touch pads on the record graphic triggers record-scratch sound effects played through the onboard speaker; includes a reset button, a BOOT button, and an addressable RGB LED.
look:
  colors:
  - black
  - white
  shape: circle
  themes:
  - music
  - retro computer
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity:
  - audio
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
images:
- file: assets/images/badges/supercon-2024/record-scratch-sao/750b40f90d.jpg
  source: https://hackaday.io/project/198458-record-scratch-sao
  credit: Applied Procrastination
  caption: Record Scratch SAO, a vinyl-record-shaped SAO with capacitive touch pads
  archived: https://web.archive.org/web/20251209091422/https://hackaday.io/project/198458-record-scratch-sao
- file: assets/images/badges/supercon-2024/record-scratch-sao/b78fe175ef.jpg
  source: https://hackaday.io/project/198458-record-scratch-sao
  credit: Applied Procrastination
  caption: Record Scratch SAO board detail, showing the RP2040, touchpad labels and speaker footprint
  archived: https://web.archive.org/web/20251209091422/https://hackaday.io/project/198458-record-scratch-sao
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198458-record-scratch-sao
  title: Record Scratch SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20251209091422/https://hackaday.io/project/198458-record-scratch-sao
- kind: url
  url: https://hackaday.io/project/198458-record-scratch-sao
  title: Record Scratch SAO
  accessed: '2026-09-07'
  note: 'Confirmed maker, event/contest, and hardware details: RP2040, 4 capacitive touch pads, MAX98357A I2S amp, small speaker, USB-C, addressable RGB LED, 4MB flash, single-layer PCB, KiCad files linked. Provided the project photo and board render used for images.'
  archived: https://web.archive.org/web/20251209091422/https://hackaday.io/project/198458-record-scratch-sao
- kind: url
  url: https://hackaday.io/AppliedProc
  title: Applied Procrastination (Hackaday.io profile)
  accessed: '2026-09-07'
  note: Maker is a group of students at the University of Oslo, Norway. No pricing, quantity, or availability details found on the profile.
  archived: https://web.archive.org/web/20260208040948/https://hackaday.io/AppliedProc
- kind: url
  url: https://github.com/SimenZhor/Record-scratch-SAO
  title: Record-scratch-SAO (GitHub, unreachable)
  accessed: '2026-09-07'
  note: Returned 404; the repo is not visible under this URL or in a public listing of the SimenZhor account as of the check date. Could not confirm the design files are still published at this address.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event, MCU, touch/audio hardware, single-layer PCB) come from the maker''s own Hackaday.io project page. The linked GitHub repo (github.com/SimenZhor/Record-scratch-SAO) 404s and does not appear in the SimenZhor account''s public repo list, so hardware_url/firmware_url/gerbers_url were left empty rather than guessed; eda_tool (KiCad) and open_source: partial are based on the Hackaday page stating KiCad schematics/PCB files are downloadable there, not on the dead GitHub link. No price, quantity-made, or continuing-availability information was published. LED count/type and battery are not stated (the board is USB-powered per the photos/description, with an onboard RGB LED of unspecified count/type). Status set to released since the project page documents a built, working unit (project logs on prototyping and assembly) rather than a mere announcement.'
last_modified_date: '2026-09-07'
---

The Record Scratch SAO is a Simple Add-On built by Applied Procrastination, a maker group of University of Oslo students, for the Supercon 8 (2024) SAO Contest. The board is cut in the shape of a vinyl record and centers on an RP2040 microcontroller paired with a MAX98357A I2S amplifier driving a small onboard speaker. Four circular capacitive touch pads are etched into the record graphic itself, so touching and dragging a finger across the "grooves" triggers record-scratch sound effects — turning the badge add-on into a tiny playable turntable. The board also carries a USB-C connector (data only), a reset button, a BOOT button, and an addressable RGB LED, and is routed as a single-layer PCB to keep the vinyl-record artwork visible in the copper and silkscreen.

The maker's Hackaday.io project page documents the build across several project logs covering motivation, prototyping, and implementation, and states that KiCad schematics and PCB files are available for download. A companion GitHub repository is linked from the project (github.com/SimenZhor/Record-scratch-SAO), but it returned a 404 at the time of this research pass and does not show up in a listing of that GitHub account's public repositories, so it could not be used to confirm firmware or hardware file locations. No pricing, production quantity, or ongoing-availability information for the SAO was found on the maker's pages.
